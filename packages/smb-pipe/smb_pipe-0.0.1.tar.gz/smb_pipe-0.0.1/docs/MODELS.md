# Model Configuration Guide

## Supported Models

### Multimodal Models (ECG + Text)

These models require both an ECG encoder and can process ECG waveforms along with clinical text.

| Model | Size | ECG Required | Notes |
|-------|------|--------------|-------|
| `standardmodelbio/Qwen3-WM-0.6B` | 0.6B | Yes ✅ | Default, fastest inference |
| `standardmodelbio/Qwen3-WM-4B` | 4B | Yes ✅ | Better accuracy, slower |

**Required ECG Encoder**: `PKUDigitalHealth/ECGFounder`

### Text-Only Models

These models work with clinical notes only, no ECG data required.

| Model | Size | ECG Required | Notes |
|-------|------|--------------|-------|
| `standardmodelbio/smb-mntp-llama-3.1-8b` | 8B | No ❌ | Clinical text only |
| `standardmodelbio/MACE-0.6B-base` | 0.6B | No ❌ | Fast text-only inference |
| Standard HuggingFace LLMs | Varies | No ❌ | Any causal LM model |

## Usage Examples

### Multimodal Inference (ECG + Text)

```python
from inference_pipeline import MultiModalMedicalInference

# Initialize with ECG encoder
pipeline = MultiModalMedicalInference(
    ecg_encoder="PKUDigitalHealth/ECGFounder",
    language_model="standardmodelbio/Qwen3-WM-0.6B"
)

# Run inference
predictions = pipeline.predict(
    ecg_files=["patient_001/baseline_ecg.mat"],
    clinical_notes="58F on anthracycline therapy, LVEF 45%"
)
```

### Text-Only Inference

```python
# No ECG encoder needed
pipeline = MultiModalMedicalInference(
    ecg_encoder=None,  # Explicitly disable ECG
    language_model="standardmodelbio/smb-mntp-llama-3.1-8b"
)

predictions = pipeline.predict(
    clinical_notes="58F on anthracycline therapy, LVEF 45%, mild dyspnea"
)
```

## ECG Encoder Details

### PKUDigitalHealth/ECGFounder

- **Architecture**: Net1D convolutional network
- **Input**: 12-lead ECG, 500Hz, 10 seconds (12 × 5000 samples)
- **Output**: 1024-dimensional embedding
- **Weights**: Pre-trained on large ECG dataset
- **HuggingFace**: [Model Card](https://huggingface.co/PKUDigitalHealth/ECGFounder)

### SimpleECGEncoder (Built-in)

- For testing only
- Random projection of ECG signals
- Not recommended for production

## Model Selection Guidelines

### Choose Multimodal When:
- ECG waveform data is available
- Higher accuracy is needed
- Detecting subtle ECG patterns

### Choose Text-Only When:
- No ECG data available
- Faster inference needed
- Working with EHR text only

## Authentication

Private models require HuggingFace authentication:

```bash
# Set token in environment
export HF_TOKEN=hf_your_token_here

# Or in .env file
echo "HF_TOKEN=hf_your_token_here" >> .env
```

## Performance Comparison

| Model Type | Inference Time | Memory Usage | Accuracy* |
|------------|---------------|--------------|-----------|
| Qwen3-WM-0.6B (multimodal) | ~10s/sample | 3GB | 70% |
| Qwen3-WM-4B (multimodal) | ~20s/sample | 8GB | 75% |
| Llama-3.1-8B (text-only) | ~5s/sample | 16GB | 60% |

*Accuracy on LVEF binary classification task

## Fine-Tuning

The models can be fine-tuned for better performance:

1. **ECG Encoder**: Fine-tune on domain-specific ECG data
2. **Language Model**: Fine-tune on clinical notes with outcomes
3. **Prediction Heads**: Train task-specific heads for cardiotoxicity

See `docs/TRAINING.md` for fine-tuning instructions (coming soon).