# qmemcalc

Quantized Memory Calculator for Transformers (QLoRA / LoRA / full fine-tuning)

## Features

- Estimate GPU memory for FP32/FP16/BF16
- Supports 4-bit / 8-bit quantization
- LoRA rank or fraction support
- Extended optimizer support
- Gradient checkpointing
- CLI for quick estimation

## Installation

```bash
pip install qmemcalc
```

## Python API Usage

```bash
from qmemcalc import estimate_memory

result = estimate_memory(
    model_name="sshleifer/tiny-gpt2",
    batch_size=2,
    seq_len=16,
    lora_r=4,
    precision="fp16",
    quantization="4bit"
)

print(result)
```
