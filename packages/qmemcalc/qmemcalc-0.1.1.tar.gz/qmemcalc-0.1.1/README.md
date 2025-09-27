## qmemcalc

**Quantized Memory Calculator for Transformers (QLoRA / LoRA / Full Fine-Tuning)**

Estimate GPU memory requirements for training or fine-tuning transformer models with ease. Supports multiple precision types, quantization, and LoRA configurations.

[![PyPI Version](https://img.shields.io/pypi/v/qmemcalc)](https://pypi.org/project/qmemcalc/)
[![Python Version](https://img.shields.io/pypi/pyversions/qmemcalc)](https://pypi.org/project/qmemcalc/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

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

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

```
git clone https://github.com/sachin62025/qmemcalc.git
cd qmemcalc
pip install -e .
```

```

```
