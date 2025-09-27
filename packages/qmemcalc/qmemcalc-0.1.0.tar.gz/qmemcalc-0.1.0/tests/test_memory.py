import pytest
from qmemcalc import estimate_memory

def test_basic_estimate():
    """
    Test basic memory estimation for a small model configuration.
    """
    result = estimate_memory(
        model_name="sshleifer/tiny-gpt2",
        batch_size=2,
        seq_len=16,
        lora_r=4,
        precision="fp16",
        quantization="none",
        optimizer="adamw",
        gradient_checkpointing=False
    )

    # Check that all expected keys are present
    keys = [
        "base_weights_MB",
        "trainable_weights_MB",
        "gradients_MB",
        "optimizer_MB",
        "activations_MB",
        "buffers_MB",
        "total_MB",
        "total_GB"
    ]
    for key in keys:
        assert key in result

    # Basic sanity check: total_MB should be > 0
    assert result["total_MB"] > 0
    print(result)

def test_lora_fraction():
    """
    Test memory estimation with LoRA fraction.
    """
    result = estimate_memory(
        model_name="sshleifer/tiny-gpt2",
        batch_size=2,
        seq_len=16,
        lora_fraction=0.1,
        precision="fp16",
        quantization="none",
        optimizer="adamw"
    )
    assert result["trainable_weights_MB"] > 0
    print(result)

def test_quantization_and_fp32():
    """
    Test memory estimation with FP32 and 4-bit quantization.
    """
    result = estimate_memory(
        model_name="sshleifer/tiny-gpt2",
        batch_size=2,
        seq_len=16,
        precision="fp32",
        quantization="4bit",
        optimizer="adamw"
    )
    # Base weights with 4bit should be smaller than FP32 size
    assert result["base_weights_MB"] > 0
    print(result)
