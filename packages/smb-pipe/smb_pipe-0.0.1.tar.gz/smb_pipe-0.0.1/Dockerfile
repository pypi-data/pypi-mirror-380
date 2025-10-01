# Base image with CUDA 11.8 – compatible with T4/V100 GPUs in RunPod Serverless
FROM pytorch/pytorch:2.1.2-cuda11.8-cudnn8-runtime

# Set working directory
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN python -m pip install --upgrade pip

# Copy project files
COPY src/ ./src/
COPY README.md ./README.md

## Self-contained: no external repos required

# Install CUDA-11.8 wheels for torch/vision/audio (ship kernels for 7.0/7.5)
RUN pip install --no-cache-dir --index-url https://download.pytorch.org/whl/cu118 \
    torch==2.1.2+cu118 torchvision==0.16.2+cu118 torchaudio==2.1.2+cu118 && \
    pip install --no-cache-dir \
    boto3 \
    loguru \
    numpy \
    pyyaml \
    runpod \
    scipy \
    h5py \
    mat73 \
    wfdb \
    accelerate \
    transformers==4.55.0 \
    safetensors==0.4.3 \
    tokenizers==0.21.0 \
    wandb \
    python-dotenv

## Note: torch 2.5.1+cu121 installed. Ensure models load via safetensors to avoid torch.load safety checks.

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    TRANSFORMERS_CACHE=/workspace/.cache/huggingface \
    HF_HOME=/workspace/.cache/huggingface \
    TORCH_HOME=/workspace/.cache/torch \
    FLASH_ATTENTION_2_DISABLE=1

# Create cache directories
RUN mkdir -p /workspace/.cache/huggingface /workspace/.cache/torch

# Download models during build (optional - remove if too large)
# RUN python -c "from transformers import AutoTokenizer; import os; \
# hf_token=os.getenv('HF_TOKEN'); \
# AutoTokenizer.from_pretrained('standardmodelbio/Qwen3-MM-0.6B', token=hf_token)"

# Entry point for RunPod serverless (self-contained path)
ENV PYTHONPATH=/workspace/src
CMD ["python", "-m", "src.rp_handler"]