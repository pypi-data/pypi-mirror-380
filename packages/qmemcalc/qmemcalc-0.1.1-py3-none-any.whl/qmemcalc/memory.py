"""
qmemcalc.memory
----------------
GPU Memory Estimator for Transformers (QLoRA / LoRA / full fine-tuning)

Features:
- Handles FP32, FP16, BF16 precision
- Handles 4-bit / 8-bit quantization
- Supports full fine-tuning and LoRA/QLoRA adapters
- Extended optimizer support (Adam, AdamW, SGD, Adagrad, RMSprop, PagedAdamW)
- Gradient checkpointing factor
- Optional LoRA fraction instead of r
- Optional batch size suggestion for given GPU VRAM
"""

import argparse
from transformers import AutoConfig

OPTIMIZER_MEMORY_OVERHEAD = {
    "adam": 8,
    "adamw": 8,
    "paged_adamw_32bit": 8,
    "sgd": 4,
    "adagrad": 4,
    "rmsprop": 8
}

PRECISION_BYTES = {
    "fp32": 4,
    "fp16": 2,
    "bf16": 2
}

QUANTIZATION_BYTES = {
    "none": None,
    "8bit": 1,
    "4bit": 0.5
}


def estimate_memory(
    model_name: str,
    batch_size: int,
    seq_len: int,
    lora_r: int = 0,
    lora_fraction: float = None,
    precision: str = "fp32",
    quantization: str = "none",
    optimizer: str = "adamw",
    num_trainable_params: int = None,
    hidden_size: int = None,
    num_layers: int = None,
    gradient_checkpointing: bool = False,
    gpu_vram_MB: int = None
):
    """Estimate GPU memory usage (MB/GB) for Transformers with optional LoRA/QLoRA."""

    # Load model config
    config = AutoConfig.from_pretrained(model_name)

    hidden_size = hidden_size or getattr(config, "hidden_size", 768)
    num_layers = num_layers or getattr(config, "num_hidden_layers", 12)
    total_params = getattr(config, "num_parameters", None)

    # Fallback heuristic if total_params not defined
    if total_params is None:
        total_params = max(hidden_size**2 * num_layers * 4, 1)

    total_params = float(total_params)

    # Determine base model weight memory
    quant_bytes = QUANTIZATION_BYTES.get(quantization.lower())
    if quant_bytes is None:
        bytes_per_param = PRECISION_BYTES.get(precision.lower(), 4)
    else:
        bytes_per_param = quant_bytes

    base_weights_MB = total_params * bytes_per_param / 1e6
    base_weights_MB += 5  # metadata overhead

    # LoRA parameters
    if lora_fraction:
        lora_params = max(total_params * float(lora_fraction), 1)  # at least 1 param
    elif lora_r > 0:
        lora_params = max(2 * hidden_size * lora_r * num_layers, 1)
    else:
        lora_params = 0

    if num_trainable_params:
        lora_params = num_trainable_params

    # LoRA weights in FP16
    lora_weights_MB = lora_params * 2 / 1e6
    lora_grads_MB = lora_params * 2 / 1e6

    # Optimizer memory
    opt_overhead = OPTIMIZER_MEMORY_OVERHEAD.get(optimizer.lower(), 8)
    lora_optimizer_MB = lora_params * opt_overhead / 1e6

    # Activation memory (FP16)
    activations_MB = batch_size * seq_len * hidden_size * num_layers * 2 / 1e6
    if gradient_checkpointing:
        activations_MB *= 0.5

    # Buffers / miscellaneous
    buffers_MB = 0.10 * (base_weights_MB + activations_MB)

    total_MB = base_weights_MB + lora_weights_MB + lora_grads_MB + lora_optimizer_MB + activations_MB + buffers_MB

    result = {
        "base_weights_MB": round(base_weights_MB, 2),
        "trainable_weights_MB": round(max(lora_weights_MB, 0.001), 4),
        "gradients_MB": round(max(lora_grads_MB, 0.001), 4),
        "optimizer_MB": round(lora_optimizer_MB, 2),
        "activations_MB": round(activations_MB, 2),
        "buffers_MB": round(buffers_MB, 2),
        "total_MB": round(total_MB, 2),
        "total_GB": round(total_MB / 1024, 2)
    }

    # Optional: suggest max batch size for given GPU VRAM
    if gpu_vram_MB:
        safe_batch = max(1, int(batch_size * gpu_vram_MB / total_MB))
        result["suggested_max_batch_for_vram"] = safe_batch

    return result


def main():
    parser = argparse.ArgumentParser(description="GPU Memory Estimator for Transformers (QLoRA / LoRA)")
    parser.add_argument("--model_name", type=str, required=True, help="Hugging Face model name")
    parser.add_argument("--batch_size", type=int, required=True, help="Batch size per device")
    parser.add_argument("--seq_len", type=int, required=True, help="Sequence length")
    parser.add_argument("--lora_r", type=int, default=0, help="LoRA rank (optional)")
    parser.add_argument("--lora_fraction", type=float, default=None, help="Fraction of total params for LoRA")
    parser.add_argument("--precision", type=str, default="fp32", choices=["fp32", "fp16", "bf16"], help="Weight/activation precision")
    parser.add_argument("--quantization", type=str, default="none", choices=["none", "4bit", "8bit"], help="Quantization type")
    parser.add_argument("--optimizer", type=str, default="adamw", help="Optimizer type")
    parser.add_argument("--num_trainable_params", type=int, default=None, help="Override LoRA trainable params")
    parser.add_argument("--hidden_size", type=int, default=None, help="Model hidden size (optional)")
    parser.add_argument("--num_layers", type=int, default=None, help="Number of layers (optional)")
    parser.add_argument("--gradient_checkpointing", action="store_true", help="Enable gradient checkpointing")
    parser.add_argument("--gpu_vram_MB", type=int, default=None, help="GPU VRAM in MB for max batch suggestion")

    args = parser.parse_args()

    result = estimate_memory(
        model_name=args.model_name,
        batch_size=args.batch_size,
        seq_len=args.seq_len,
        lora_r=args.lora_r,
        lora_fraction=args.lora_fraction,
        precision=args.precision,
        quantization=args.quantization,
        optimizer=args.optimizer,
        num_trainable_params=args.num_trainable_params,
        hidden_size=args.hidden_size,
        num_layers=args.num_layers,
        gradient_checkpointing=args.gradient_checkpointing,
        gpu_vram_MB=args.gpu_vram_MB
    )

    print("\nEstimated GPU Memory Usage:")
    for k, v in result.items():
        print(f"{k:<35}: {v}")


if __name__ == "__main__":
    main()
