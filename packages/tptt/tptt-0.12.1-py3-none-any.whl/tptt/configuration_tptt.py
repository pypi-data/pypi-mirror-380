# pylint: disable=too-many-arguments, too-many-positional-arguments, too-many-instance-attributes, too-many-locals
"""
Author : Fabien FURFARO
"""

import logging
import os
from datetime import datetime

from typing import Any, Dict, List, Optional, Union
from jinja2 import Environment, FileSystemLoader

import psutil
import torch
from transformers import AutoConfig, PretrainedConfig

logger = logging.getLogger(__name__)  # monitoring

# Constants
BYTES_IN_GB = 1024**3


def convert_sets_to_lists(obj):
    """Convert sets to list for LoRA serialized config"""
    if isinstance(obj, set):
        return list(obj)
    if isinstance(obj, dict):
        return {k: convert_sets_to_lists(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [convert_sets_to_lists(x) for x in obj]
    return obj


class TpttConfig(PretrainedConfig):
    """
    Configuration class for the TPTT model.
    This class merges the backbone config (e.g., Llama) with custom TPTT parameters,
    """

    model_type = "tptt"
    auto_map = {
        "AutoModelForCausalLM": "modeling_tptt.TpttModel",
        "AutoConfig": "configuration_tptt.TpttConfig",
    }
    architectures = ["TpttModel"]

    RECURRENT_MODES = {
        "delta_rule": {
            "order": 1,
            "alpha_gate": "c",
            "beta_gate": "k",
            "linear": True,
            "trick": "dt",
        },
        "gated_delta_rule": {
            "order": 1,
            "alpha_gate": "k",
            "beta_gate": "k",
            "linear": True,
            "trick": "dt",
        },
        "delta_rule_v": {
            "order": 1,
            "alpha_gate": "c",
            "beta_gate": "v",
            "linear": True,
            "trick": "dt",
        },
        "delta_rule_kv": {
            "order": 1,
            "alpha_gate": "c",
            "beta_gate": "kv",
            "linear": True,
            "trick": "dt",
        },
        "delta_rule_gelu": {
            "order": 1,
            "alpha_gate": "c",
            "beta_gate": "k",
            "linear": False,
            "trick": "dt",
        },
        "delta_product": {
            "order": 2,
            "alpha_gate": "c",
            "beta_gate": "k",
            "linear": True,
            "trick": "dt",
        },
        "gated_delta_product": {
            "order": 2,
            "alpha_gate": "k",
            "beta_gate": "k",
            "linear": True,
            "trick": "dt",
        },
        "delta_product_r": {
            "order": 2,
            "alpha_gate": "c",
            "beta_gate": "k",
            "linear": True,
            "trick": "rot",
        },
        "delta_product_c": {
            "order": 2,
            "alpha_gate": "c",
            "beta_gate": "k",
            "linear": True,
            "trick": "rdt",
        },
    }

    def __init__(
        self,
        base_model_config: Optional[Union[dict, PretrainedConfig]] = None,
        base_model_name: str = "google/gemma-3-270m",  #
        base_model_subfolder: Optional[str] = None,
        name_or_path: Optional[str] = None,
        model_task: str = "causal_lm",
        target_modules_names: Optional[List[str]] = None,
        operator_mode: Optional[str] = None,
        order: int = 1,
        alpha_gate: str = "1",
        beta_gate: str = "k",
        linear: bool = True,
        trick: str = "derivative",
        use_linear_checkpoint: Optional[bool] = None,
        max_self_attn_length: Optional[
            int
        ] = None,  # unnecessary if SWA, else, standards 8192
        base_scale_attn: bool = False,
        mag_weight: float = 0.5,  # if 1.0, use only linear operator
        cross_gate: bool = False,  # unlinear mixing strategy
        max_chunk_size: int = 64,  # 128 if adaptive chunking (longest)
        linear_precision: Union[str, torch.dtype] = "float32",
        lora_config: Optional[dict] = None,  # only serialized accepted
        padding_side: Optional[str] = None,  # for tokenizer, default "right"
        bidirectional: bool = False,  # if True, use bidirectional attention
        pooling_config: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        # If base_model_config is provided, load it and merge with this config
        if base_model_config is not None:
            if isinstance(base_model_config, PretrainedConfig):
                base_model_config = base_model_config.to_dict()
        else:
            # Load config from Hugging Face Hub or a local path
            base_model_config = AutoConfig.from_pretrained(
                base_model_name, **kwargs
            ).to_dict()
        # Merge all backbone fields into this config
        for k, v in base_model_config.items():
            setattr(self, k, v)

        self.base_model_name = base_model_name
        self.base_model_subfolder = base_model_subfolder
        self.model_task = model_task

        if name_or_path is not None:
            self._name_or_path = name_or_path
        else:
            if "/" in base_model_name:
                self._name_or_path = "Titans-" + base_model_name.split("/", 1)[1]
            else:
                self._name_or_path = "Titans-" + base_model_name

        self.target_modules_names = target_modules_names or [
            "attn",
            "self_attn",
            "attention",
        ]
        self.operator_mode = operator_mode

        # Detect available memory on accelerator device
        if torch.cuda.is_available():
            _, total_mem = torch.cuda.mem_get_info()
        else:
            total_mem = psutil.virtual_memory().total
        total_mem_gb = total_mem / BYTES_IN_GB

        self.use_linear_checkpoint = (
            total_mem_gb < 16
            if use_linear_checkpoint is None
            else use_linear_checkpoint
        )

        self.base_scale_attn = base_scale_attn
        self.mag_weight = mag_weight
        self.cross_gate = cross_gate
        self.max_chunk_size = max_chunk_size
        self.max_self_attn_length = max_self_attn_length
        if isinstance(linear_precision, torch.dtype):
            linear_precision = str(linear_precision).replace("torch.", "")
        self.linear_precision = linear_precision

        self.lora_config = lora_config
        if lora_config is not None:
            if hasattr(self.lora_config.get("peft_type"), "value"):
                self.lora_config["peft_type"] = self.lora_config["peft_type"].value
            self.lora_config = convert_sets_to_lists(self.lora_config)

        self.padding_side = padding_side
        self.bidirectional = bidirectional
        if self.bidirectional:
            print("Bidirectional is enabled, need to be uncausal and unpadded.")
        self.pooling_config = pooling_config

        super().__init__(**kwargs)  # flush unconsistend pretrained parameters (?)
        # Copy class attributes to instance for serialization (save dict)
        self.model_type = self.__class__.model_type
        self.auto_map = self.__class__.auto_map
        self.architectures = self.__class__.architectures
        # Padding side configuration if not set
        if self.padding_side is None:
            self.padding_side = "right"
            logger.info("Warning: padding_side is None, defaulting to 'right'.")
        # set recurrent configuration from operator mode
        if operator_mode is None:
            self.recurrent_config = {
                "order": order,
                "alpha_gate": alpha_gate,
                "beta_gate": beta_gate,
                "linear": linear,
                "trick": trick,
            }
        elif operator_mode in self.__class__.RECURRENT_MODES:
            self.recurrent_config = self.__class__.RECURRENT_MODES[operator_mode]
        else:
            raise ValueError(
                f"Unknown operator_mode: {operator_mode}. "
                f"Available modes: {list(self.__class__.RECURRENT_MODES.keys())}"
            )
        self.model_variant = get_model_name(
            lora_config is not None, cross_gate, **self.recurrent_config
        )
        logger.info("Using model variant: %s", self.model_variant)


TpttConfig.register_for_auto_class()


def get_model_name(
    lora: bool = True,
    cross_gate: bool = False,
    bidirectional: bool = False,
    order: int = 1,
    alpha_gate: str = "c",
    beta_gate: str = "k",
    linear: bool = True,
    trick: str = "dt",
    prefix: str = "liza",
    add_date: bool = True,
) -> str:
    """
    Generate a compact, explicit model folder name with parameters and optional date.
    Example output: liza_lora_a-c_b-k_o-1_lin_trick-d_2025-09-10
    """
    parts = [
        "lora" if lora else "full",
        "cross" if cross_gate else "mag",
        "bidir" if bidirectional else "causal",
        f"alpha-{alpha_gate}",
        f"beta-{beta_gate}",
        f"order-{order}",
        "linear" if linear else "gelu",
        f"trick-{trick}",
    ]
    name = prefix + "_" + "_".join(parts)
    if add_date:
        name += "_" + datetime.today().strftime("%Y-%m-%d")
    return name


def render_template(template_path: str, variables: dict) -> str:
    """Load and render a Jinja2 template from any file path."""
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
    template = env.get_template(os.path.basename(template_path))
    return template.render(**variables)


def write_model_card(output_path: str, content: str):
    """Write the generated content into README.md."""
    os.makedirs(output_path, exist_ok=True)
    readme_path = os.path.join(output_path, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)


def generate_model_card(
    output_path: str,
    config: Union[dict, object],
    template: Optional[
        str
    ],  # can be "model_card" OR an absolute/relative path to a .md file
    extra_variables: Optional[Dict] = None,
):
    """
    Generate a README.md file from a Jinja2 template and a configuration.

    - template can be either:
        * a full path to a template file
        * a short name (e.g., "model_card") -> will be looked up inside default_templates_dir
    """
    if template is None:
        template = "model_card_template"  # default template name
    # Locate the template
    if os.path.exists(template):  # direct file path provided
        template_path = template
    else:
        default_templates_dir = os.path.join(os.path.dirname(__file__), "templates")
        template_path = os.path.join(default_templates_dir, f"{template}.md")

    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template not found: {template_path}")

    variables = {
        "model_id": os.path.basename(output_path),
        "config": config,
    }
    if extra_variables:
        variables.update(extra_variables)

    content = render_template(template_path, variables)
    write_model_card(output_path, content)
