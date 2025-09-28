# pylint: disable=too-many-lines, too-many-arguments, too-many-positional-arguments, too-many-instance-attributes, too-many-locals

"""
This module implements the TPTT model with linear attention (LiZA) and LoRA support.
Author : Fabien FURFARO
TPTT : Transforming Pretrained Transformers into Titans (https://arxiv.org/abs/2506.17671)
"""

import logging
import math
import os
from pathlib import Path
import re
import shutil
from functools import partial
from typing import Any, Dict, List, Optional, Tuple, Union, Literal

import torch
import torch.nn.functional as F
from einops import rearrange
from huggingface_hub import hf_hub_download, list_repo_files
from peft import LoraConfig, PeftModel, get_peft_model
from safetensors import safe_open
from safetensors.torch import save_file
from torch import nn
from torch.utils.checkpoint import checkpoint
from transformers import (
    AutoConfig,
    AutoModel,
    AutoModelForCausalLM,
    DynamicCache,
    PreTrainedModel,
)
from transformers.configuration_utils import PretrainedConfig

from .configuration_tptt import TpttConfig

logger = logging.getLogger(__name__)  # monitoring


class LCache:
    """Cache for storing intermediate states of linear attention layers."""

    def __init__(self):
        """Stores per-layer intermediate states: {layer_idx: state_dict}"""
        self.inputs_states: Dict[int, Dict[str, torch.Tensor]] = (
            {}
        )  # recurrent states and qkv buffers

    def __getitem__(self, layer_idx: int) -> Optional[Dict[str, torch.Tensor]]:
        """Retrieve cached state for a given layer, or None if not present"""
        return self.inputs_states.get(layer_idx, None)

    def update(self, layer_idx: int, **kwargs):
        """Detach all tensors to avoid retaining computation graphs"""
        detached_kwargs = {
            k: v.detach() if isinstance(v, torch.Tensor) else v
            for k, v in kwargs.items()
        }
        # Update or create the state for the specified layer
        if layer_idx in self.inputs_states:
            self.inputs_states[layer_idx].update(detached_kwargs)
        else:
            self.inputs_states[layer_idx] = detached_kwargs

    def reset(self):
        """Clear all cached states and reset the token counter"""
        self.inputs_states.clear()


class CausalConv1d(nn.Module):
    """Causal 1D convolution (with offset)."""

    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size,
        dilation=1,
        offset=0,
        padding_mode="constant",
        padding_value=0,
    ):

        super().__init__()
        self.offset = offset
        self.kernel_size = kernel_size
        self.dilation = dilation
        self.padding_mode = padding_mode
        self.padding_value = padding_value
        self.left_pad = (kernel_size - 1) * dilation + max(0, offset)
        self.conv1d = nn.Conv1d(
            in_channels,
            out_channels,
            kernel_size,
            padding=0,
            dilation=dilation,
            groups=in_channels,
        )
        start_idx = max(0, -offset)
        self.output_slice = slice(start_idx, None)

    def forward(self, x):
        """Input shape: [B, F, S], output shape: [B, F, S]"""
        # Pad left only
        x = F.pad(
            x, (self.left_pad, 0), mode=self.padding_mode, value=self.padding_value
        )
        out = self.conv1d(x)
        return out[:, :, self.output_slice]


class CausalAvgPool1d(nn.Module):
    """Causal sliding window average (uniform)."""

    def __init__(
        self,
        input_size: int,
        output_size: Optional[int] = None,
        kernel_size=3,
        dilation=1,
        padding_mode="replicate",
        offset=0,
    ):
        super().__init__()
        if output_size is None:
            output_size = input_size
        self.input_size = input_size
        self.output_size = output_size
        self.kernel_size = kernel_size
        self.causal_conv = CausalConv1d(
            input_size,
            input_size,
            kernel_size=kernel_size,
            dilation=dilation,
            padding_mode=padding_mode,
            offset=offset,
        )
        with torch.no_grad():
            avg_kernel = torch.full(
                (input_size, 1, kernel_size), fill_value=1 / kernel_size
            )
            self.causal_conv.conv1d.weight.copy_(avg_kernel)
            self.causal_conv.conv1d.weight.requires_grad = False
            if self.causal_conv.conv1d.bias is not None:
                self.causal_conv.conv1d.bias.zero_()
                self.causal_conv.conv1d.bias.requires_grad = False
        self.pool = nn.AdaptiveAvgPool1d(output_size)

    def forward(self, x):
        """Input shape: [B, S, F], output shape: [B, output_size, F]"""
        # x expected shape: [B, S, F]
        x = x.transpose(1, 2)  # transpose to [B, F, S] for Conv1d
        y = self.causal_conv(x).transpose(1, 2)  # [B, S, F]
        return self.pool(y)  # [B, S, F → output_size]


class VirtualTokenExpander(nn.Module):
    """
    Expands input tokens into 'n' virtual tokens using derivative and rotative methods.
    """

    def __init__(
        self,
        num_heads: int,
        head_dim: int,
        n: int,
        mode: Literal["dt", "rot", "rdt"] = "rdt",
        flip: bool = True,
    ):
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = head_dim
        self.n = n
        self.mode = mode
        self.flip = flip

        # Binomial kernel for derivative trick
        deriv_coeffs = [(-1) ** k * math.comb(n - 1, k) for k in range(n)]
        deriv_coeffs_tensor = torch.tensor(deriv_coeffs, dtype=torch.float32)
        deriv_coeffs_tensor /= deriv_coeffs_tensor.abs().sum()
        # Register as buffer since it is constant, not learned
        self.register_buffer("deriv_coeffs", deriv_coeffs_tensor)

        # Rotative parameters for rotative trick
        angles = torch.arange(n, dtype=torch.float32) * (2 * math.pi / n)
        self.register_buffer("rot_cos", torch.cos(angles).view(1, 1, 1, n, 1))
        self.register_buffer("rot_sin", torch.sin(angles).view(1, 1, 1, n, 1))

    def _apply_derivative_conv(self, x: torch.Tensor) -> torch.Tensor:
        """Applies the derivative method via conv kernel."""
        batch_size, num_heads, _, head_dim = x.shape
        device, dtype = x.device, x.dtype

        # Padding on derivation sequence
        x_padded = torch.cat(
            [
                torch.zeros(
                    batch_size,
                    num_heads,
                    self.n - 1,
                    head_dim,
                    device=device,
                    dtype=dtype,
                ),
                x,
            ],
            dim=2,
        )

        # Convolution part (slidding windows)
        windows = x_padded.unfold(dimension=2, size=self.n, step=1)
        kernel = self.deriv_coeffs
        conv_out = windows * kernel.view(1, 1, 1, 1, self.n)

        # Reshaping [B, H, S, n, d]
        if self.flip:
            conv_out = conv_out.flip(-1)
        out = conv_out.permute(0, 1, 2, 4, 3)
        return out

    def _apply_rotative_expand(self, x: torch.Tensor) -> torch.Tensor:
        """Applies the rotative method via simple expansion."""
        batch_size, num_heads, seq_len, head_dim = x.shape
        cos, sin = self.rot_cos, self.rot_sin
        d_parity = head_dim // 2

        if head_dim % 2:
            x_pairs = x[..., :-1].view(batch_size, num_heads, seq_len, d_parity, 2)
        else:
            x_pairs = x.view(batch_size, num_heads, seq_len, d_parity, 2)

        x_pairs = x_pairs.unsqueeze(3).expand(
            batch_size, num_heads, seq_len, self.n, d_parity, 2
        )
        x0, x1 = x_pairs[..., 0], x_pairs[..., 1]

        x0r = x0 * cos - x1 * sin
        x1r = x0 * sin + x1 * cos

        rot = torch.stack([x0r, x1r], dim=-1).reshape(
            batch_size, num_heads, seq_len, self.n, d_parity * 2
        )
        if head_dim % 2:
            last = (
                x[..., -1]
                .unsqueeze(-1)
                .unsqueeze(3)
                .expand(batch_size, num_heads, seq_len, self.n, 1)
            )
            rot = torch.cat([rot, last], dim=-1)
        return rot.reshape(batch_size, num_heads, seq_len, self.n, head_dim)

    def forward(self, x: torch.Tensor, force: Optional[str] = None) -> torch.Tensor:
        """Forward pass to expand input tokens. [B, H, S, D] -> [B, H, S, n, D]"""
        mode = self.mode
        if force is not None:
            mode = force
        if mode == "dt":
            return self._apply_derivative_conv(x)
        elif mode == "rot":
            return self._apply_rotative_expand(x)
        elif mode == "rdt":
            d_out = self._apply_derivative_conv(x)
            r_out = self._apply_rotative_expand(x)
            return 0.5 * (d_out + r_out)
        elif mode == "cte":
            return x.unsqueeze(3).repeat(1, 1, 1, self.n, 1)
        else:
            raise ValueError(f"Unknown mode {self.mode}")


class LinearAttention(nn.Module):
    """
    Linear multi-head attention layer: [B, S, D] -> [B, S, D]
    Projections + gating + efficient linear attention mechanism (TPTT compatible).
    """

    def __init__(
        self,
        hidden_dim: int,
        num_heads: int,
        head_dim: Optional[int] = None,
        num_key_value_heads: Optional[int] = None,
        num_key_value_groups: Optional[int] = None,
        bias: bool = True,
        dropout: Optional[float] = None,
        linear_precision: torch.dtype = torch.float32,
        padding_side: str = "right",
        shared_attn: bool = False,  # shared attention
        layer_idx: int = 0,
        operator_mode: Optional[str] = "linear",
        use_linear_checkpoint: bool = False,
        recurrent_config: Optional[Dict[str, Any]] = None,
        linear_cache: Optional[LCache] = None,
        max_chunk_size: int = 64,
        bidirectional: bool = False,  # not used if causal
        pooling_config: Optional[Dict[str, Any]] = {},  # todo
    ):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.num_heads = num_heads
        self.head_dim = head_dim or hidden_dim // num_heads
        self.num_key_value_heads = num_key_value_heads or num_heads
        self.num_key_value_groups = num_key_value_groups or (
            num_heads // (num_key_value_heads or num_heads)
        )
        self.scaling = self.head_dim**-0.5
        self.layer_idx = layer_idx
        self.linear_cache = linear_cache or LCache()
        self.linear_precision = linear_precision
        self.padding_side = padding_side

        self.shared_attn = shared_attn

        if not shared_attn:
            self.q_proj = nn.Linear(hidden_dim, num_heads * self.head_dim, bias=bias)
            self.k_proj = nn.Linear(
                hidden_dim, self.num_key_value_heads * self.head_dim, bias=bias
            )
            self.v_proj = nn.Linear(
                hidden_dim, self.num_key_value_heads * self.head_dim, bias=bias
            )
            self.out_proj = nn.Linear(num_heads * self.head_dim, hidden_dim, bias=bias)

        if recurrent_config is None:
            operator_mode = "delta_product"  # force default operator mode if no config
            recurrent_config = {
                "order": 2,
                "alpha_gate": "c",
                "beta_gate": "k",
                "linear": True,
                "trick": "dt",
            }
        self.operator_mode = operator_mode
        self.recurrent_config = recurrent_config
        self.dropout = nn.Dropout(dropout) if dropout is not None else None

        self.linear_operator = LinearAttentionOp(
            use_linear_checkpoint=use_linear_checkpoint,
            max_chunk_size=max_chunk_size,
            linear_precision=linear_precision,
        )
        self.bidirectional = bidirectional
        # Causal average pooling for gating
        self.pooling_config = pooling_config
        self.pool_g = CausalAvgPool1d(self.head_dim * self.num_key_value_heads).to(
            dtype=linear_precision
        )
        # Trick for n-houselholder product
        self.virtual_token_expander = VirtualTokenExpander(
            self.num_heads,
            self.head_dim,
            recurrent_config["order"],
            recurrent_config["trick"],
        )

    def get_cache(self, use_cache: bool) -> Tuple[
        Optional[torch.Tensor],
        Optional[Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]],
    ]:
        """
        Retrieve recurrent state and qkvg buffers from the cache. (Only if causal)
        """
        if not use_cache:
            return None, None
        last_state = self.linear_cache[self.layer_idx]
        if last_state is not None:
            recurrent_state = last_state.get("recurrent_state", None)
            qkvg_buffers = last_state.get("qkvg", None)
        else:
            recurrent_state = None
            qkvg_buffers = None
        return recurrent_state, qkvg_buffers

    def save_cache(
        self,
        q: torch.Tensor,
        k: torch.Tensor,
        v: torch.Tensor,
        alpha: torch.Tensor,
        beta: torch.Tensor,
        state: torch.Tensor,
        n_orders: int,
    ) -> None:
        """
        Save the recurrent state and qkv buffers to the cache. (Only if causal)
        """
        if n_orders > 1:
            qkvg_buffers = (
                q[:, :, -(n_orders - 1) :, :],
                k[:, :, -(n_orders - 1) :, :],
                v[:, :, -(n_orders - 1) :, :],
                alpha[:, :, -(n_orders - 1) :, :],
                beta[:, :, -(n_orders - 1) :, :],
            )
        else:
            qkvg_buffers = None
        self.linear_cache.update(
            self.layer_idx, recurrent_state=state, qkvg=qkvg_buffers
        )

    def compute_gate(self, k: torch.Tensor, v: torch.Tensor) -> Tuple[torch.Tensor]:
        """
        Compute the gating tensor according to the beta_gate.
        """
        # Forget and Write Gating for linear attn (abusive term)
        f_g, w_g = self.pool_g(k), self.pool_g(v)
        f_g = rearrange(f_g, "b n (h m) -> b h n m", h=self.num_key_value_heads)
        w_g = rearrange(w_g, "b n (h m) -> b h n m", h=self.num_key_value_heads)
        f_g = f_g.repeat_interleave(self.num_key_value_groups, dim=1)
        w_g = w_g.repeat_interleave(self.num_key_value_groups, dim=1)
        f_g, w_g = torch.sigmoid(f_g), torch.sigmoid(w_g)

        # Convert to linear_precision for numerical stability and get model dtype
        f_g, w_g = (x.to(self.linear_precision).contiguous() for x in (f_g, w_g))

        # compute alpha and beta gate
        gate_map = {
            "k": f_g,
            "v": w_g,
            "kv": f_g * w_g,
            "c": torch.ones_like(f_g),
        }
        alpha = gate_map[self.recurrent_config["alpha_gate"]]
        beta = (
            torch.full_like(f_g, 0.5)
            if self.recurrent_config["beta_gate"] == "c"
            else gate_map[self.recurrent_config["beta_gate"]]
        )

        return alpha, beta

    def compute_extended_householder(self, q, k, v, alpha, beta, seq_len):
        """Expand HouseHolder state (n_h > 1) with correct sequence length after expansion"""
        n_orders = self.recurrent_config["order"]
        if n_orders == 1:
            return tuple(x.unsqueeze(3) for x in (q, k, v, alpha, beta))

        # Expand q, k, v
        tensors_qkv = [q, k, v]
        expanded_qkv = [self.virtual_token_expander(t) for t in tensors_qkv]

        # Expand alpha, beta with conditional force='cte'
        expanded_ab = [
            self.virtual_token_expander(
                t,
                force="cte" if self.recurrent_config[g] == "c" else None,
            )
            for t, g in zip([alpha, beta], ["alpha_gate", "beta_gate"])
        ]

        # Slice the last seq_len tokens on dim=2
        expanded = [t[:, :, -seq_len:, :, :] for t in expanded_qkv + expanded_ab]

        return tuple(expanded)

    def prepare_attention_input(
        self,
        q: torch.Tensor,
        k: torch.Tensor,
        v: torch.Tensor,
    ) -> torch.Tensor:
        """
        Prepare input for linear attention. q,k,v, Input shape: [B, S, D], output [B, S, D].
        """

        # Reshape for multi-head
        q = rearrange(q, "b n (h d) -> b h n d", h=self.num_heads)
        k = rearrange(k, "b n (h d) -> b h n d", h=self.num_key_value_heads)
        v = rearrange(v, "b n (h d) -> b h n d", h=self.num_key_value_heads)

        # Repeat for GQA
        k = k.repeat_interleave(self.num_key_value_groups, dim=1)
        v = v.repeat_interleave(self.num_key_value_groups, dim=1)

        ## DeltaNet-style: Silu activation and normalization
        q = F.normalize(F.silu(q), p=2, dim=-1, eps=1e-6)
        k = F.normalize(F.silu(k), p=2, dim=-1, eps=1e-6)

        ## linear stability part
        v = v * self.scaling

        # Convert to linear_precision for numerical stability and get model dtype
        q, k, v = (x.to(self.linear_precision).contiguous() for x in (q, k, v))
        return q, k, v

    def merge_head_output(self, out, out_proj, dtype, device):
        """Merge heads, RMSNorm. Input shape: [B, H, S, d], output [B, S, D]."""
        # Merge heads and project: [B, H, S, d] -> [B, S, H*d] -> Out proj
        out = rearrange(out, "b h s d -> b s (h d)")
        # Normalize output (RMS norm). Note: bidirectional compatibility
        out = out / out.pow(2).mean(dim=-1, keepdim=True).add(1e-6).sqrt()
        # Ensure dtype and device consistency
        out = out.to(dtype=dtype, device=device)
        # Apply output projection
        out = out_proj(out)  # [B, S, D]
        # Apply dropout if specified
        if self.dropout is not None:
            out = self.dropout(out)
        return out

    def forward(
        self,
        x: Union[List[torch.Tensor], torch.Tensor],
        attn_mask: Optional[torch.Tensor] = None,
        out_proj: Optional[nn.Module] = None,
        **kwargs: Any,
    ) -> torch.Tensor:
        """
        Forward pass for linear attention. Input shape: [B, S, D], output [B, S, D].
        """

        if not self.shared_attn:
            hidden_states = x[0] if isinstance(x, (list, tuple)) else x
            # Projections
            q = self.q_proj(hidden_states)
            k = self.k_proj(hidden_states)
            v = self.v_proj(hidden_states)
            out_proj = self.out_proj
        else:
            # Shared attention <=> no projections here
            q, k, v = x[0], x[1], x[2]
            out_proj = self.out_proj if out_proj is None else out_proj

        # get parameter
        linear_activation = self.recurrent_config["linear"]
        n_orders = self.recurrent_config["order"]
        dtype, device, seq_len = q.dtype, q.device, q.shape[1]

        # Masking if needed
        if attn_mask is not None:
            v = apply_linear_attention_mask(attn_mask, v, self.padding_side)

        # Compute Gating
        alpha, beta = self.compute_gate(k, v)

        # Prepare linear q,k,v for attention operation
        q, k, v = self.prepare_attention_input(q, k, v)

        # Retrieve cache for generation
        use_cache = kwargs.get("use_cache", False)
        recurrent_state, qkvg = self.get_cache(use_cache)

        if qkvg is not None and qkvg[0].shape[-1] == q.shape[-1]:
            # inertial part (kv speed variation)
            q = torch.cat([qkvg[0].to(q.device), q], dim=2)
            k = torch.cat([qkvg[1].to(q.device), k], dim=2)
            v = torch.cat([qkvg[2].to(q.device), v], dim=2)
            alpha = torch.cat([qkvg[3].to(q.device), alpha], dim=2)
            beta = torch.cat([qkvg[4].to(q.device), beta], dim=2)

        if use_cache:
            cache_tensors = {
                name: tensor.detach().clone()
                for name, tensor in zip(
                    ["q", "k", "v", "alpha", "beta"], [q, k, v, alpha, beta]
                )
            }

        # Extend input for n householder state [B,H,S,d] -> [B, H, S, n, d]
        q, k, v, alpha, beta = self.compute_extended_householder(
            q, k, v, alpha, beta, seq_len
        )

        # Linear Attention Core, output: [B, H, S, d]
        if self.bidirectional:  # Work only with uncausal attention
            # Forward direction
            out_forward, state = self.linear_operator(
                q=q,
                k=k,
                v=v,
                alpha=alpha,
                beta=beta,
                linear_activation=linear_activation,
                recurrent_state=recurrent_state,
                **kwargs,
            )
            # Backward direction: flip the input sequence on the time dimension (dim=2)
            kwargs_bwd = kwargs.copy()
            kwargs_bwd["use_cache"] = False
            out_backward, _ = self.linear_operator(
                q=torch.flip(q, dims=[2]),
                k=torch.flip(k, dims=[2]),
                v=torch.flip(v, dims=[2]),
                alpha=torch.flip(alpha, dims=[2]),
                beta=torch.flip(beta, dims=[2]),
                linear_activation=linear_activation,
                **kwargs_bwd,
            )
            # Flip the output back to restore proper order
            out_backward = torch.flip(out_backward, dims=[2])
            # Fusion: here, simple mean
            out = (out_forward + out_backward) / 2
        else:
            out, state = self.linear_operator(
                q=q,
                k=k,
                v=v,
                alpha=alpha,
                beta=beta,
                linear_activation=linear_activation,
                recurrent_state=recurrent_state,
                **kwargs,
            )

        # Save cache for generation (before n_householder expansion)
        if use_cache:
            self.save_cache(**cache_tensors, state=state, n_orders=n_orders)

        # RMSNorm and Projection attention
        out = self.merge_head_output(out, out_proj, dtype, device)
        return out


class MemoryAsGate(nn.Module):
    """Memory as Gate module, for linear and vanilla attention mixing."""

    def __init__(self, hidden_dim=None, mode="constant", mag_ratio=0.5):
        super().__init__()
        self.min_val = 0.1
        self.max_val = 0.9
        self.mode = mode if hidden_dim is not None else "constant"
        self.hidden_dim = hidden_dim
        self.mag_weight = torch.tensor(mag_ratio)
        if mode == "constant":
            self.dynamic_gate = None
        elif mode == "dynamic":
            self.dynamic_gate = CausalConv1d(
                in_channels=hidden_dim, out_channels=1, kernel_size=16
            )
        else:
            raise ValueError(f"Unknown MaG mode {mode}")

    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        """Compute the gate ratio."""
        mag_weight = self.mag_weight.to(
            dtype=hidden_states.dtype, device=hidden_states.device
        )
        if self.mode == "constant":
            shape = list(hidden_states.shape)
            shape[-1] = 1
            gate_ratio = mag_weight.expand(*shape)
        elif self.mode == "dynamic":
            # hidden_states shape: [B, S, D]
            logits = self.dynamic_gate(hidden_states.transpose(1, 2)).transpose(
                1, 2
            )  # [B, S, 1]
            gate_ratio = torch.sigmoid(logits)
            min_val, max_val = self.min_val, self.max_val
            gate_ratio = min_val + (max_val - min_val) * gate_ratio
        return gate_ratio


class LiZAttention(nn.Module):
    """LiZA Linear Attention module, mixing linear and vanilla attention."""

    def __init__(
        self,
        base_attn: nn.Module,
        layer_idx: int,
        base_config: PretrainedConfig,  # Backbone Config
        linear_cache: Optional[LCache] = None,
        operator_mode: str = "delta_rule",
        use_linear_checkpoint: bool = False,
        recurrent_config: Optional[Dict[str, Any]] = None,
        max_self_attn_length: Optional[int] = None,  # unnecessary
        base_scale_attn: bool = False,
        mag_weight: float = 0.5,
        cross_gate: bool = False,
        max_chunk_size: int = 64,
        linear_precision: Union[str, torch.dtype] = "float32",
        padding_side: str = "right",  # for tokenizer
        disable_linear_attn: bool = False,
        bidirectional: bool = False,  # if True, use bidirectional attention
        pooling_config: Optional[Dict[str, Any]] = None,
    ):
        super().__init__()
        if isinstance(linear_precision, str):
            linear_precision = getattr(torch, linear_precision)
        self.linear_precision = linear_precision
        self.base_attn: nn.Module = base_attn
        self.base_config = base_config
        self.layer_idx = layer_idx
        self.max_self_attn_length = max_self_attn_length
        self.base_scale_attn = base_scale_attn
        self.cross_gate = cross_gate
        self.max_chunk_size = max_chunk_size
        self.linear_precision = linear_precision
        self.padding_side = padding_side
        self.disable_linear_attn = disable_linear_attn

        # Attention parameters
        (
            self.num_heads,
            self.head_dim,
            self.num_key_value_heads,
            self.num_key_value_groups,
            self.hidden_dim,
        ) = self._get_attention_parameters(base_attn, base_config)
        self.scaling = self.head_dim**-0.5

        # MaG parameters
        self.memory_gate = MemoryAsGate(
            self.hidden_dim, mode="constant", mag_ratio=mag_weight
        )

        self.linear_attn = LinearAttention(
            layer_idx=layer_idx,
            shared_attn=True,
            operator_mode=operator_mode,
            use_linear_checkpoint=use_linear_checkpoint,
            recurrent_config=recurrent_config,
            hidden_dim=self.hidden_dim,
            num_heads=self.num_heads,
            head_dim=self.head_dim,
            num_key_value_heads=self.num_key_value_heads,
            num_key_value_groups=self.num_key_value_groups,
            linear_precision=linear_precision,
            linear_cache=linear_cache,
            max_chunk_size=max_chunk_size,
            padding_side=padding_side,
            bidirectional=bidirectional,
            pooling_config=pooling_config,
        )

    def _get_attention_parameters(
        self, base_attn: nn.Module, base_config: PretrainedConfig
    ) -> Tuple[Optional[int], Optional[int], Optional[int], Optional[int]]:
        """Retrieve the attention parameters from the base attention module."""
        # first order base attention module and second order config
        num_heads = (
            getattr(base_attn, "num_heads", None)
            or getattr(base_attn, "num_q_heads", None)
            or getattr(base_config, "num_heads", None)
            or getattr(base_config, "num_attention_heads", None)
        )
        head_dim = (
            getattr(base_attn, "head_dim", None)
            or getattr(base_attn, "attention_head_size", None)
            or getattr(base_config, "head_dim", None)
            or (
                getattr(base_config, "hidden_size", None) // num_heads
                if num_heads and getattr(base_config, "hidden_size", None)
                else None
            )
        )
        num_key_value_heads = (
            getattr(base_attn, "num_kv_heads", None)
            or getattr(base_attn, "num_k_heads", None)
            or getattr(base_config, "num_key_value_heads", None)
            or num_heads  # fallback
        )
        num_key_value_groups = getattr(base_attn, "num_key_value_groups", None) or (
            num_heads // num_key_value_heads if num_heads and num_key_value_heads else 1
        )
        hidden_dim = getattr(base_config, "hidden_size", None) or head_dim * num_heads
        return (
            num_heads,
            head_dim,
            num_key_value_heads,
            num_key_value_groups,
            hidden_dim,
        )

    def _apply_shared_projections(
        self, hidden_states: torch.Tensor
    ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, nn.Module]:
        base_attn = self.base_attn
        if hasattr(base_attn, "q_proj"):
            # LLama, OLMO and Mistral style
            q = base_attn.q_proj(hidden_states)
            k = base_attn.k_proj(hidden_states)
            v = base_attn.v_proj(hidden_states)
            out_proj = base_attn.o_proj
        elif hasattr(base_attn, "qkv_proj"):
            # OpenELM and GPT-Neo style : QKV fused, split on the last dimension
            qkv = base_attn.qkv_proj(hidden_states)
            q, k, v = split_qkv(base_attn, qkv)
            out_proj = base_attn.out_proj
        elif hasattr(base_attn, "c_attn") and hasattr(base_attn, "c_proj"):
            # GPT-2 style
            qkv = base_attn.c_attn(hidden_states)
            q, k, v = qkv.chunk(3, dim=-1)
            out_proj = base_attn.c_proj
        elif all(hasattr(base_attn, n) for n in ["query", "key", "value"]):
            # BERT - ViT
            q = base_attn.query(hidden_states)
            k = base_attn.key(hidden_states)
            v = base_attn.value(hidden_states)
            out_proj = getattr(base_attn, "dense", None)  # ou output.dense
        else:
            raise ValueError("Unsupported attention module: cannot find projections.")
        return q, k, v, out_proj

    def _process_self_attn(
        self,
        hidden_states: torch.Tensor,
        attention_mask: Optional[torch.Tensor],
        kwargs,
    ) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[DynamicCache], int]:
        """Process the self-attention part (with truncation)."""
        if self.max_self_attn_length:  # Not needed for SWA (nonparam memorize context)
            hidden_states, attention_mask = truncate_attention_mask(
                hidden_states, attention_mask, self.max_self_attn_length
            )

            if kwargs.get("position_embeddings", None) is not None:
                cos, sin = kwargs["position_embeddings"]
                cos = cos[:, -self.max_self_attn_length :]
                sin = sin[:, -self.max_self_attn_length :]
                kwargs["position_embeddings"] = (cos, sin)

            if isinstance(kwargs.get("past_key_value", None), DynamicCache):
                # cache management
                if (
                    len(kwargs["past_key_value"]) > self.layer_idx
                    and self.layer_idx == 0
                ):
                    kwargs["past_key_value"].crop(self.max_self_attn_length - 1)

        # Ensure attention mask is of the correct dtype and device
        if attention_mask is not None:
            attention_mask = attention_mask.to(
                dtype=hidden_states.dtype, device=hidden_states.device
            )
        # Standard attention (mask and rotation is applied inside)
        base_attn_outputs = self.base_attn(
            hidden_states,
            attention_mask=attention_mask,
            **kwargs,
        )

        if isinstance(base_attn_outputs, tuple):
            if len(base_attn_outputs) == 3:
                o_base, attn_weights, present_key_value = base_attn_outputs
                expected_attn_mode = 3
            elif len(base_attn_outputs) == 2:
                o_base, attn_weights = base_attn_outputs
                present_key_value, expected_attn_mode = None, 2
            else:
                raise ValueError(
                    f"Unexpected number of outputs from base_attn: {len(base_attn_outputs)}"
                )
        else:
            o_base = base_attn_outputs
            attn_weights, present_key_value, expected_attn_mode = None, None, 1
        return o_base, attn_weights, present_key_value, expected_attn_mode

    def _prepare_attn_mixin(
        self,
        o_lin: torch.Tensor,
        o_base: torch.Tensor,
        tensor_dtype: torch.dtype,
        eps: float = 1e-5,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """Prepare linear attn for mixing with self attn."""
        # Force cast typing, shape : [b n (h d)]
        o_lin = o_lin.to(tensor_dtype)
        o_base = o_base.to(tensor_dtype)
        # feature scaling
        if self.base_scale_attn:
            scaler = o_base.pow(2).mean(dim=-1, keepdim=True).add(eps).sqrt()
            o_lin = scaler * o_lin
        return o_lin, o_base

    def _apply_mag(
        self,
        mag_weight: torch.Tensor,
        linear_attention: torch.Tensor,
        softmax_attention: torch.Tensor,
    ) -> torch.Tensor:
        """Apply the MAG strategy"""
        # Ablation option
        if self.disable_linear_attn:
            return softmax_attention

        # Left-Padding management
        if linear_attention.shape[1] != softmax_attention.shape[1]:
            left_trunc = min(linear_attention.shape[1], softmax_attention.shape[1])
            linear_attention, softmax_attention = (
                linear_attention[:, -left_trunc:],
                softmax_attention[:, -left_trunc:],
            )
        # NAM : Neural Attention Mixer (Element-wise mix)
        softmax_weighted = (1 - mag_weight) * softmax_attention
        linear_weighted = mag_weight * linear_attention
        if self.cross_gate:
            output_attention = (
                softmax_weighted + linear_weighted + softmax_weighted * linear_weighted
            )  # complex cross product (unlinear interaction)
        else:
            output_attention = softmax_weighted + linear_weighted  # classic

        if torch.allclose(softmax_weighted, output_attention):
            logger.info(
                "[LOG] layer : %s, softmax_weighted and output_attention are close.",
                self.layer_idx,
            )
        # Final output
        return output_attention

    def forward(
        self,
        hidden_states: torch.Tensor,
        attention_mask: Optional[torch.Tensor] = None,
        **kwargs,
    ) -> torch.Tensor:
        """Mix linear and self attention forward"""
        device = hidden_states.device
        dtype = hidden_states.dtype
        self.base_attn.to(device)

        if self.training:
            kwargs.pop("past_key_value", None)
            kwargs["use_cache"] = False
        elif "use_cache" not in kwargs:
            kwargs.pop("past_key_value", None)
            kwargs["use_cache"] = False

        kwargs.pop("position_ids", None)  # obsolete

        # Apply shared projections
        q, k, v, out_proj = self._apply_shared_projections(hidden_states)

        # Apply linear attention to hidden states
        o_lin = self.linear_attn(
            x=[q, k, v], attn_mask=attention_mask, out_proj=out_proj, **kwargs
        )

        # Process self attn with truncation
        o_base, attn_weights, present_key_value, expected_attn_mode = (
            self._process_self_attn(hidden_states, attention_mask, kwargs)
        )

        # Prepare output mixing
        o_lin, o_base = self._prepare_attn_mixin(o_lin, o_base, dtype, eps=1e-5)

        # Apply Memory as Gate in self-attention (with length management and ablation)
        mag_weight = self.memory_gate(hidden_states)
        out = self._apply_mag(mag_weight, o_lin, o_base)

        # Return output following transformer convention
        if expected_attn_mode == 3:
            return out, attn_weights, present_key_value
        if expected_attn_mode == 2:
            return out, attn_weights
        return out

    @property
    def is_sliding(self):
        """Check if the base attention contain sliding window attention."""
        return getattr(self.base_attn, "is_sliding", False)


def load_tptt_safetensors(
    repo_or_path: str,
    model: Union[PreTrainedModel, PeftModel],
    subfolder: Optional[str] = None,
    token: Optional[str] = None,
) -> Union[PreTrainedModel, PeftModel]:
    """Load Tptt safetensor from LoRA/PEFT weights and adapt keys if needed."""
    # sharding not supported yet (e.g. : -00001-of-00005.safetensors, ...)
    fname = "adapter_model.safetensors"
    # subfolder management
    if subfolder:
        repo_or_path_norm = os.path.normpath(repo_or_path)
        subfolder_norm = os.path.normpath(subfolder)
        if not repo_or_path_norm.endswith(subfolder_norm):
            fname = f"{subfolder}/{fname}" if subfolder else fname
    # Find file path
    if os.path.isdir(repo_or_path):
        path = os.path.join(repo_or_path, fname)
        if not os.path.exists(path):
            return model
    else:
        if fname not in list_repo_files(repo_or_path, token=token):
            return model
        path = hf_hub_download(repo_or_path, fname, token=token)

    # Load weights from safetensors
    with safe_open(path, framework="pt") as f:
        state_dict = {k: f.get_tensor(k) for k in f.keys()}

    # Adapt LoRA/Specific keys if needed (add .default if expected by the model)
    def adapt_keys(sd, model):
        model_keys = list(model.state_dict().keys())
        if any(k.startswith("tptt_model.base_model.") for k in model_keys):
            prefix = "tptt_model.base_model."
        elif any(k.startswith("base_model.") for k in model_keys):
            prefix = "base_model."
        else:
            prefix = ""

        has_base_attn = any(".base_attn." in k for k in model_keys)

        def adapt_key(k):
            k_ = k if k.startswith(prefix) else prefix + k
            # first, verify and modify base_attn (LiZA)
            if ".base_attn." in k_ and not has_base_attn:
                k_ = k_.replace(".base_attn.", ".")
            # change LoRA if needed
            if (
                k_.endswith("lora_A.weight") or k_.endswith("lora_B.weight")
            ) and k_.replace(".weight", ".default.weight") in model_keys:
                k_ = k_.replace(".weight", ".default.weight")
            return k_

        return {adapt_key(k): v for k, v in sd.items()}

    state_dict = adapt_keys(state_dict, model)

    # Cast tensors to the expected dtype of the model parameters
    model_state_dict = model.state_dict()
    for k, v in state_dict.items():
        if k in model_state_dict:
            expected_dtype = model_state_dict[k].dtype
            if v.dtype != expected_dtype:
                state_dict[k] = v.to(expected_dtype)

    logger.info("Input LoRA/Specific keys: %s", [k for k in state_dict.keys()])

    # Load into model
    missing, unexpected = model.load_state_dict(state_dict, strict=False, assign=True)
    missing_lora = [k for k in missing if "lora" in k]
    if missing_lora:
        logger.warning("Missing keys: %s", missing_lora)
    if unexpected:
        logger.warning("Unexpected keys: %s", unexpected)
    return model


def get_tptt_model(  # pylint: disable=too-many-arguments, too-many-positional-arguments
    model: nn.Module,
    base_config: PretrainedConfig,  # ou LlamaConfig, MistralConfig, etc.
    linear_cache: Optional[LCache] = None,
    liza_attention: nn.Module = LiZAttention,
    target_modules_names: Optional[list[str]] = None,
    operator_mode: str = "delta_rule",
    use_linear_checkpoint: bool = False,
    recurrent_config: Optional[Dict[str, Any]] = None,
    base_scale_attn: bool = False,
    mag_weight: float = 0.5,
    cross_gate: bool = False,
    max_chunk_size: int = 64,
    linear_precision: torch.dtype = torch.float32,
    max_self_attn_length: Optional[int] = None,  # unnecessary
    padding_side: str = "right",  # for tokenizer
    bidirectional: bool = False,  # if True, use bidirectional attention
    pooling_config: Optional[Dict[str, Any]] = None,
    **kwargs,  # quickfix unexpected arguments
) -> Tuple[PreTrainedModel, LCache]:
    """Replace target modules in a model with LiZAttention."""
    if target_modules_names is None:
        target_modules_names = ["attn", "self_attn", "attention"]
    # Find target modules by suffix (e.g., "attn", "attention")
    target_modules_names = [
        name
        for name, _ in model.named_modules()
        if any(name.endswith(suffix) for suffix in target_modules_names)
        and not any(f".{suffix}." in name for suffix in target_modules_names)
    ]
    if not target_modules_names:
        raise ValueError(
            f"Target modules '{target_modules_names}' not found in the model."
        )
    # Prepare recurrent config
    linear_cache = linear_cache or LCache()
    # Inject LiZAttention into the model
    for name, _ in model.named_modules():
        if name in target_modules_names:
            parent = model
            *path, last = name.split(".")
            for p in path:
                parent = getattr(parent, p)
            layer_idx = extract_layer_idx(name)
            setattr(
                parent,
                last,
                liza_attention(
                    getattr(parent, last),
                    layer_idx=layer_idx,
                    base_config=base_config,
                    linear_cache=linear_cache,
                    operator_mode=operator_mode,
                    use_linear_checkpoint=use_linear_checkpoint,
                    recurrent_config=recurrent_config,
                    max_self_attn_length=max_self_attn_length,
                    base_scale_attn=base_scale_attn,
                    mag_weight=mag_weight,
                    cross_gate=cross_gate,
                    max_chunk_size=max_chunk_size,
                    linear_precision=linear_precision,
                    padding_side=padding_side,
                    bidirectional=bidirectional,
                    pooling_config=pooling_config,
                ),
            )
    return model, linear_cache


def save_tptt_safetensors(model, path: str, name: str = "adapter_model.safetensors"):
    """Save trainable LoRA/Specific weights and adapting key names"""
    # 1. Get the full state_dict
    all_sd = model.state_dict()

    # 2. Identify trainable parameter names (usually only LoRA/PEFT adapters)
    trainable_keys = [
        name for name, param in model.named_parameters() if param.requires_grad
    ]  # Also, you can manually select specific keys in model after load

    # 3. Filter and adapt the keys (Remove custom model encapsulation info)
    to_save = {
        k.replace("tptt_model.", "").replace("base_model.", ""): all_sd[k]
        for k in trainable_keys
    }

    # 4. Save the filtered adapters to a safetensors file
    if to_save:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        # sharding not supported yet (e.g. : -00001-of-00005.safetensors, ...)
        save_file(to_save, os.path.join(path, name))


class TpttModel(PreTrainedModel):
    """
    TPTT model wrapper with linear attention (LiZA) and LoRA support.
    Handles only architecture and weights.
    """

    config_class = TpttConfig

    def __init__(
        self,
        config: TpttConfig,
        **kwargs,
    ):
        """
        Initialize TpttModel with a given config and backbone.
        Injects LiZA attention modules into the backbone.
        """
        super().__init__(config, **kwargs)
        repo_or_path = getattr(config, "_base_path", None) or config._name_or_path

        # 1. Load backbone (with subfolder management) :
        kwargs_bb = kwargs.copy()
        if config.base_model_subfolder is not None:
            kwargs_bb["subfolder"] = config.base_model_subfolder
        else:
            kwargs_bb.pop("subfolder", None)

        if config.model_task == "causal_lm":
            tptt_model = AutoModelForCausalLM.from_pretrained(
                config.base_model_name, **kwargs_bb
            )
        else:
            tptt_model = AutoModel.from_pretrained(config.base_model_name, **kwargs_bb)

        # 2. Inject LiZA attention
        self.linear_cache = LCache()
        tptt_model, self.linear_cache = get_tptt_model(
            tptt_model, config, self.linear_cache, **config.to_dict()
        )

        # 3. Apply LoRA/Specific if present and configured
        if config.lora_config is not None:
            lora_config_obj = LoraConfig(**config.lora_config)
            tptt_model = get_peft_model(tptt_model, lora_config_obj)
        else:
            # Doesn't work if quantization is applied !
            tptt_model = set_trainable_parameters(tptt_model)

        # 4. Load safetensor if tptt/peft adaptor in repo
        if repo_or_path:
            tptt_model = load_tptt_safetensors(
                repo_or_path,
                tptt_model,
                subfolder=kwargs.get("subfolder", None),
                token=kwargs.get("token", None),
            )
        self.tptt_model = tptt_model

    def forward(
        self,
        input_ids: Optional[torch.LongTensor] = None,
        attention_mask: Optional[torch.Tensor] = None,
        labels: Optional[torch.LongTensor] = None,
        **kwargs,
    ):
        """Forward pass. All arguments are passed to the underlying base model."""
        if self.training:
            kwargs["use_cache"] = False
            kwargs.pop("num_items_in_batch", None)
        elif "use_cache" not in kwargs:  # evaluation
            kwargs.pop("num_items_in_batch", None)
            kwargs["use_cache"] = False
        return self.tptt_model(
            input_ids=input_ids, attention_mask=attention_mask, labels=labels, **kwargs
        )

    def generate(self, *args, **kwargs):
        """Delegate the generate call to the backbone model, which supports generation"""
        return self.tptt_model.generate(*args, **kwargs)

    def save_pretrained(self, path: str, **kwargs):
        """Save model weights, config, and source code to the given path."""
        # 0. Save complete tptt config (with or without LoRA)
        super().save_pretrained(path, **kwargs)  # pylint: disable=no-member
        self._adjust_save_strategy(path, **kwargs)
        # 1. Save true weights and adapte keys
        save_tptt_safetensors(self, path)
        # 2. Copy Python files for trust_remote_code
        self._copy_source_files(path, **kwargs)

    def _adjust_save_strategy(self, path: str, **kwargs):
        """Re-adapt/remove the weight safetensor and saved adapter config"""
        if isinstance(self.tptt_model, PeftModel):
            self.tptt_model.save_pretrained(path, **kwargs)
        safetensor_path = os.path.join(path, "model.safetensors")
        if os.path.exists(safetensor_path):
            os.remove(safetensor_path)
        adapter_path = os.path.join(path, "adapter_config.json")
        if os.path.exists(adapter_path):
            os.remove(adapter_path)

    def _copy_source_files(self, target_path: str, **kwargs):
        """Copy all .py files from package directory for trust_remote_code."""
        src_dir = os.path.dirname(os.path.abspath(__file__))
        dst_dir = (
            f"./{str(Path(target_path).parts[0])}"
            if kwargs.get("subfolder", False)
            else target_path
        )
        for fname in os.listdir(src_dir):
            if fname.endswith(".py"):
                src = os.path.join(src_dir, fname)
                dst = os.path.join(dst_dir, fname)
                shutil.copy2(src, dst)

    def retie_lm_after_load(self, **kwargs):
        """Re-link lm_head after loading external weights."""
        embed_lm = find_embedding_lm(self.tptt_model)
        if embed_lm is not None and hasattr(self.tptt_model, "lm_head"):
            if self.tptt_model.lm_head is None:  # ensure lm_head exists
                self.tptt_model.lm_head = nn.Linear(
                    embed_lm.weight.shape[1], embed_lm.weight.shape[0], bias=False
                )
            if kwargs.get("tie_word_embeddings", True):
                self.tptt_model.lm_head.weight = embed_lm.weight  # share weights
                logger.info("Weights of lm_head have been shared with embedding.")
            else:
                self.tptt_model.lm_head.weight = nn.Parameter(embed_lm.weight.clone())
                logger.info("Weights of lm_head have been cloned from the embedding.")

    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path=None, *model_args, **kwargs):
        """Custom from_pretrained that accepts the standard positional argument"""
        config = kwargs.pop("config", None)
        repo_or_path = (
            pretrained_model_name_or_path
            or kwargs.pop("pretrained_model_name_or_path", None)
            or kwargs.pop("repo_or_path", None)
            or (getattr(config, "_base_path", None) if config else None)
            or (getattr(config, "_name_or_path", None) if config else None)
        )

        if config is None and repo_or_path is not None:
            config = AutoConfig.from_pretrained(repo_or_path, **kwargs)
        model = cls(config, *model_args, **kwargs)
        model.retie_lm_after_load(**kwargs)
        return model


TpttModel.register_for_auto_class("AutoModelForCausalLM")


class LinearAttentionOp(nn.Module):
    """Base class for linear attention operators."""

    def __init__(
        self,
        use_linear_checkpoint: bool = False,
        max_chunk_size: int = 64,
        linear_precision: torch.dtype = torch.float32,
    ):
        super().__init__()
        self.use_linear_checkpoint = use_linear_checkpoint
        self.max_chunk_size = max_chunk_size
        self.linear_precision = linear_precision

    def forward(
        self,
        q: torch.Tensor,
        k: torch.Tensor,
        v: torch.Tensor,
        alpha: torch.Tensor,
        beta: torch.Tensor,
        linear_activation: bool,
        recurrent_state: Optional[torch.Tensor] = None,
        **kwargs,
    ) -> torch.Tensor:
        """gate
        Forward pass for the attention operator.
        """
        # Ensure linear_precision for numerical stability (float32)
        q, k, v, alpha, beta = [
            x.to(self.linear_precision) for x in (q, k, v, alpha, beta)
        ]

        # Retrieve cache if needed
        use_cache = kwargs.get("use_cache", False)
        use_checkpoint = not (use_cache) and self.use_linear_checkpoint

        output, state = self.chunk_delta_product_forward(
            q,
            k,
            v,
            alpha,
            beta,
            self.max_chunk_size,
            linear_activation=linear_activation,
            initial_state=recurrent_state,
            use_checkpoint=use_checkpoint,
            linear_precision=self.linear_precision,
        )

        return output, state

    @staticmethod
    def chunk_delta_product_forward(
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        alpha: torch.Tensor,
        beta: torch.Tensor,
        chunk_size: int,
        linear_activation: bool = True,
        initial_state: Optional[torch.Tensor] = None,
        use_checkpoint: bool = True,
        linear_precision: torch.dtype = torch.float32,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Chunkwise parallel implementation https://arxiv.org/abs/2406.06484
        For each chunk, processes chunk_size * n_orders steps (virtual tokens) in order.
        """

        # --- Main chunk_delta_product_forward logic ---

        batch_size, num_heads, seq_len, n_orders, head_dim = query.shape
        chunk_size = get_valid_chunk_size(seq_len, chunk_size)
        num_chunks = seq_len // chunk_size

        # Reshape to combine seq_len and n_orders into virtual tokens
        query, key, value, alpha, beta = [
            x.reshape(batch_size, num_heads, seq_len * n_orders, -1)
            for x in (query, key, value, alpha, beta)
        ]

        # Chunk the sequences with virtual tokens
        q_chunks, k_chunks, v_chunks, alpha_chunks, beta_chunks = [
            x.reshape(batch_size, num_heads, num_chunks, chunk_size * n_orders, -1)
            for x in (query, key, value, alpha, beta)
        ]

        k_beta = k_chunks * beta_chunks
        v_beta = v_chunks * beta_chunks

        # [B,H,num_chunks,N,D] @ [B,H,num_chunks,D,N] -> [B,H,num_chunks,N,N]
        householder = -(k_beta @ k_chunks.transpose(-2, -1)).tril(-1)

        # size : N = chunk_size * n_orders -->  [(...),N,N]
        inv_hh = construct_causal_forward_solver(householder, dtype=linear_precision)

        w = torch.matmul(inv_hh, k_beta)
        u = torch.matmul(inv_hh, v_beta)

        state_shape = (batch_size, num_heads, n_orders, head_dim, head_dim)
        if initial_state is not None and initial_state.shape == state_shape:
            state = initial_state.to(device=query.device, dtype=linear_precision)
        else:
            state = torch.full(
                state_shape,
                fill_value=1e-6,  # stability if unlinear activation
                device=query.device,
                dtype=linear_precision,
            )

        # Reshape to separate n virtual tokens
        q_chunks, w, u, alpha_chunks = [
            x.reshape(batch_size, num_heads, num_chunks, chunk_size, n_orders, -1)
            for x in (q_chunks, w, u, alpha_chunks)
        ]

        # Process all chunks sequentially with per-token state
        output, final_state = sequential_delta_product_scan(
            q_chunks.to(dtype=linear_precision),
            w.to(dtype=linear_precision),
            u.to(dtype=linear_precision),
            alpha_chunks.to(dtype=linear_precision),
            linear_activation,
            state.to(dtype=linear_precision),
            linear_precision=linear_precision,
            use_checkpoint=use_checkpoint,
        )

        # Reshape back to [B, H, seq_len, D]
        output = output[:, :, :, :, -1, :]  # [B, H, num_chunks, chunk_size, D]
        output = output.reshape(batch_size, num_heads, seq_len, head_dim)
        return output.to(dtype=linear_precision), final_state.to(dtype=linear_precision)


def sequential_delta_product_scan(
    q_chunks: torch.Tensor,
    w: torch.Tensor,
    u: torch.Tensor,
    alpha_chunks: torch.Tensor,
    linear_activation: bool,
    initial_recurrent_state: torch.Tensor,
    linear_precision: torch.dtype,
    use_checkpoint: bool,
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    DeltaProduct implementation https://arxiv.org/abs/2502.10297
    Implements the per-token Householder state updates.
    """
    batch, head, num_chunks_inner, chunk_size, n_orders, dim = q_chunks.shape
    output_inner = torch.empty_like(q_chunks)
    # initial_recurrent_state is H_{last_token_of_prev_chunk, n-1} ([B, H, D, D])
    h_0_base = initial_recurrent_state[:, :, -1, :, :].clone()

    def process_one_chunk(
        q_chunk_params: torch.Tensor,
        w_chunk_params: torch.Tensor,
        u_chunk_params: torch.Tensor,
        a_chunk_params: torch.Tensor,
        h_0_base: torch.Tensor,
    ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """
        Process a single chunk (with per-token state for n_orders > 1).
        """
        o_intra_current_chunk = torch.zeros(
            batch,
            head,
            chunk_size,
            n_orders,
            dim,
            device=q_chunk_params.device,
            dtype=linear_precision,
        )
        o_inter_current_chunk = torch.zeros_like(o_intra_current_chunk)
        current_accumulated_state_per_token = (
            h_0_base.unsqueeze(2).expand(-1, -1, chunk_size, -1, -1).clone()
        )  # [B, H, chunk_size, D, D]

        for step in range(n_orders):
            q_s = q_chunk_params[:, :, :, step, :]
            w_s = w_chunk_params[:, :, :, step, :]
            u_s = u_chunk_params[:, :, :, step, :]
            a_s = a_chunk_params[:, :, :, step, :]

            # DeltaProduct recurrence per order (H_ij -> H_i(j+1))
            state_input_for_this_step = current_accumulated_state_per_token

            # Parallel DeltaProduct update in order j
            ## BLAS/cuBLAS einsum "bhcd,bhcdd->bhcd"
            k_trans_h_old = (
                torch.matmul(
                    w_s.unsqueeze(-2),
                    state_input_for_this_step,
                )
                .squeeze(-2)
                .to(dtype=linear_precision)
            )

            u_val = u_s - k_trans_h_old

            o_inter_current_chunk[:, :, :, step, :] = (
                torch.matmul(q_s.unsqueeze(-2), state_input_for_this_step)
                .squeeze(-2)
                .to(dtype=linear_precision)
            )

            ## BLAS/cuBLAS einsum "bhcd,bhcd->bhcd"
            o_intra_current_chunk[:, :, :, step, :] = (q_s * u_val).to(
                dtype=linear_precision
            )

            # DeltaProduct state update [BHCDD]
            gated_state = state_input_for_this_step * a_s.unsqueeze(-2)
            outer_product_term = torch.matmul(w_s.unsqueeze(-1), u_val.unsqueeze(-2))
            new_state_i_per_token = gated_state + outer_product_term
            current_accumulated_state_per_token = new_state_i_per_token.to(
                dtype=linear_precision
            )
        # Return all needed for next chunk
        return (
            o_intra_current_chunk,
            o_inter_current_chunk,
            current_accumulated_state_per_token[:, :, -1, :, :],  # new h_0_base
        )

    for chunk_idx_inner in range(num_chunks_inner):
        q_chunk_params = q_chunks[:, :, chunk_idx_inner]
        w_chunk_params = w[:, :, chunk_idx_inner]
        u_chunk_params = u[:, :, chunk_idx_inner]
        a_chunk_params = alpha_chunks[:, :, chunk_idx_inner]

        # Checkpointed call if training
        call = (
            partial(checkpoint, use_reentrant=False)
            if use_checkpoint
            else lambda f, *a: f(*a)
        )
        o_intra, o_inter, h_0_base = call(
            process_one_chunk,
            q_chunk_params,
            w_chunk_params,
            u_chunk_params,
            a_chunk_params,
            h_0_base,
        )
        if not linear_activation:  # unlinear activation between chunks
            h_0_base = unlinear_activation(h_0_base).to(dtype=linear_precision)
        output_inner[:, :, chunk_idx_inner] = o_intra + o_inter

    return output_inner, h_0_base


def unlinear_activation(x: torch.Tensor, scale: float = 2.0) -> torch.Tensor:
    """Unlinear activation between chunk"""
    x_n = x.norm(p=2, dim=-1, keepdim=True) + 1e-6
    x_gelu = F.gelu(scale * x / x_n, approximate="tanh")  # pylint: disable=not-callable
    return (x / scale) * x_gelu


def extract_layer_idx(module_name: str) -> int:
    """Extract the layer index from a module name string."""
    match = re.search(r"\.(\d+)\.", module_name)
    if match:
        return int(match.group(1))
    return -1


def find_embedding_lm(module: nn.Module) -> Optional[nn.Module]:
    """Find the embedding weight in a model module."""
    for _, child in module.named_modules():
        if hasattr(child, "embed_tokens") and hasattr(child.embed_tokens, "weight"):
            return child.embed_tokens
        if hasattr(child, "token_embeddings") and hasattr(
            child.token_embeddings, "weight"
        ):
            return child.token_embeddings
    return None


def set_trainable_parameters(
    model: PreTrainedModel, trainable_patterns: List[str] = None
) -> PreTrainedModel:
    """Freeze model parameters except trainable_patterns."""
    if trainable_patterns is None:
        trainable_patterns = [
            "q_proj",
            "k_proj",
            "v_proj",
            "o_proj",
            "qkv_proj",
            "out_proj",
            "c_attn",
            "c_proj",
            "query",
            "key",
            "value",
        ]

    for name, param in model.named_parameters():
        param.requires_grad = any(pattern in name for pattern in trainable_patterns)

    trainable_layers = [n for n, p in model.named_parameters() if p.requires_grad]
    logger.info("Trainable parameters after freeze: %s", trainable_layers)
    return model


def apply_linear_attention_mask(
    attention_mask: torch.Tensor, v: torch.Tensor, padding_side: str = "right"
) -> torch.Tensor:
    """Extract if padding --> [B,S]"""
    if attention_mask.dim() == 4 and attention_mask.shape[1] == 1:
        mask = attention_mask.diagonal(dim1=-2, dim2=-1).squeeze(1)
    else:
        mask = attention_mask.squeeze(
            dim=tuple(
                i
                for i in range(1, attention_mask.dim())
                if attention_mask.shape[i] == 1
            )
        )
    # Ensure cast to the same dtype as v and convert to binary mask
    if not (
        mask.dtype == torch.bool
        or (
            mask.dtype in [torch.uint8, torch.int32, torch.int64]
            and mask.max() <= 1
            and mask.min() >= 0
        )
    ):
        mask = (mask >= 0).to(v.dtype)  # [-inf, 0, 0, -inf] --> [0, 1, 1, 0]
    else:
        mask = mask.to(v.dtype)
    # mask is [batch, seq] --> Broadcast to v [batch, seq, (...)]
    if padding_side == "left":
        mask = mask[:, -v.shape[-2] :][(...,) + (None,) * (v.dim() - 2)]
    else:  # right padding
        mask = mask[:, : v.shape[-2]][(...,) + (None,) * (v.dim() - 2)]
    return v * mask


def truncate_attention_mask(
    hidden_states: torch.Tensor, attention_mask: torch.Tensor, max_length: int
) -> tuple[torch.Tensor, torch.Tensor]:
    """Truncate hidden_states and attention_mask to the last window of size max_length"""
    seq_dim = 1  # convention: (batch, seq, ...)
    seq_len = hidden_states.shape[seq_dim]
    if seq_len > max_length:
        hidden_states = hidden_states.narrow(seq_dim, seq_len - max_length, max_length)
        if attention_mask is not None:
            # mask [batch, seq]
            if attention_mask.dim() == 2:
                attention_mask = attention_mask[:, -max_length:]
            # mask [batch, seq, seq]
            elif attention_mask.dim() == 3:
                attention_mask = attention_mask[:, -max_length:, -max_length:]
            # mask [batch, 1, seq, seq]
            elif attention_mask.dim() == 4 and attention_mask.shape[1] == 1:
                attention_mask = attention_mask[:, :, -max_length:, -max_length:]
            else:
                raise ValueError(
                    "No dimension in attention_mask matches sequence length of hidden_states."
                )
    return hidden_states, attention_mask


def construct_causal_forward_solver(
    tri_tensor: torch.Tensor, dtype: torch.dtype = torch.float32
) -> torch.Tensor:
    """Forward substitution for fast inversion during chunk propagation."""
    tri_tensor = tri_tensor.to(dtype=dtype).clone()
    chunk_size = tri_tensor.shape[-1]

    for i in range(1, chunk_size):
        tri_tensor[..., i, :i] = tri_tensor[..., i, :i] + (
            tri_tensor[..., i, :, None].clone() * tri_tensor[..., :, :i].clone()
        ).sum(-2)

    tri_tensor = tri_tensor + torch.eye(
        chunk_size, dtype=dtype, device=tri_tensor.device
    )
    return tri_tensor.to(dtype=dtype)


def get_valid_chunk_size(total_l: int, chunk_size: int) -> int:
    """Return the largest chunk_size <= chunk_size that divides total_l."""
    for c in range(min(chunk_size, total_l), 0, -1):
        if total_l % c == 0:
            return c
    return 1


## RARELY
def split_qkv(
    base_attn: nn.Module, qkv: torch.Tensor
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """Split the QKV tensor into separate Q, K, and V tensors."""
    num_q_heads = getattr(base_attn, "num_q_heads", None)
    num_k_heads = getattr(base_attn, "num_k_heads", None)
    num_v_heads = getattr(base_attn, "num_v_heads", None)
    head_dim = getattr(base_attn, "head_dim", None)

    if num_q_heads is None or num_k_heads is None or num_v_heads is None:
        raise ValueError(
            "Base attention must have num_q_heads, num_k_heads, and num_v_heads defined."
        )

    q_len = num_q_heads * head_dim
    k_len = num_k_heads * head_dim
    v_len = num_v_heads * head_dim

    q, k, v = torch.split(qkv, [q_len, k_len, v_len], dim=-1)
    return q, k, v


## OPTIONAL
def match_dim(x: torch.Tensor, dim: int, target_size: int) -> torch.Tensor:
    """Match the size of tensor x along dimension dim to target_size by interpolation"""
    src_size = x.shape[dim]
    if src_size == target_size:
        return x
    x = torch.moveaxis(x, dim, -1)
    shape = x.shape
    if src_size < target_size:
        x = x.reshape(-1, 1, src_size)
        x = F.interpolate(x, size=target_size, mode="linear", align_corners=False)
        x = x.reshape(*shape[:-1], target_size)
    else:
        eye = torch.eye(target_size, src_size, device=x.device, dtype=x.dtype)
        x = F.linear(x, eye)  # pylint: disable=not-callable
    x = torch.moveaxis(x, -1, dim)
    return x


def ensure_stability(
    tensor: torch.Tensor, min_val: float = -1e4, max_val: float = 1e4
) -> torch.Tensor:
    """stability forcing"""
    dtype = tensor.dtype
    center = (max_val + min_val) / 2
    tensor = torch.clamp(tensor, min=min_val, max=max_val)
    tensor = torch.nan_to_num(tensor, nan=center, posinf=max_val, neginf=min_val)
    return tensor.to(dtype=dtype)


def soft_clamp(
    x: torch.Tensor, min_val: float = 1e-6, max_val: float = 1 - 1e-6
) -> torch.Tensor:
    """Differentiable clamping for stability"""
    dtype = x.dtype
    scale = (max_val - min_val) / 2
    center = (max_val + min_val) / 2
    return (torch.tanh((x - center) / scale) * scale + center).to(dtype=dtype)


def describe(x: torch.Tensor, name="tensor") -> None:
    """Prints the shape, min, max, mean, and std of a tensor."""
    stats = (x.min(), x.max(), x.mean(), x.std())
    print(
        f"{name} shape: {tuple(x.shape)}, "
        + f"min: {stats[0]:.4g}, max: {stats[1]:.4g}, "
        + f"mean: {stats[2]:.4g}, std: {stats[3]:.4g}, "
        + f"dtype: {x.dtype}, device: {x.device}"
    )
