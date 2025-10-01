# Cardiotoxicity Risk Assessment Pipeline

A multimodal AI system for predicting cardiotoxicity risk from ECG waveforms and clinical notes. Supports both multimodal (ECG + text) and text-only inference modes.

## Quick Start

```bash
# Install dependencies
uv sync

# Download MIMIC-IV ECG data (requires PhysioNet approval)
./scripts/data/mimic_to_s3.sh lvef          # LVEF subset (~17GB)
./scripts/monitoring/job_status.sh --watch  # Monitor progress

# Generate local file manifest
uv run scripts/data/create_local_manifest.py

# Run predictions on a CSV with explicit modality mapping
uv run src/batch_inference.py \
  --csv data/csv/lvef_with_local_paths.csv \
  --modalities '{"ecg":{"path_column":"local_dat_path"},"ehr":{"columns":["age","gender","diagnosis"]}}' \
  --out outputs/lvef_results.jsonl \
  --max-samples 50
```

## Features

- **Multimodal Analysis**: Combines ECG waveforms with clinical text
- **Risk Prediction**: Multi-horizon predictions (immediate, 3, 6, 12 months)
- **Model Flexibility**: Supports various model architectures
- **Production Ready**: Docker, RunPod serverless, batch processing
- **Validation Pipeline**: Metrics calculation against ground truth

## Model Support

| Model Type | Example | ECG Required | Use Case |
|------------|---------|--------------|----------|
| Multimodal | Qwen3-WM-0.6B | Yes ✅ | Full accuracy with ECG data |
| Text-only | Llama-3.1-8B | No ❌ | When ECG unavailable |

## Documentation

- **[Complete Workflow](docs/WORKFLOW.md)**: End-to-end LVEF classification pipeline
- **[Data Guide](docs/DATA.md)**: MIMIC-IV ECG download, monitoring, and local file management
- **[Validation Guide](docs/VALIDATION.md)**: Testing with ground truth LVEF data
- **[Deployment Guide](docs/DEPLOYMENT.md)**: Docker, RunPod serverless setup
- **[Batch Processing](docs/BATCH.md)**: Processing multiple patients efficiently

## Basic Usage

### Multimodal Inference (ECG + Text)

```python
from inference_pipeline import MultiModalMedicalInference

pipeline = MultiModalMedicalInference(
    language_model="standardmodelbio/Qwen3-WM-0.6B",
    encoders={"ecg": "PKUDigitalHealth/ECGFounder"}
)

predictions = pipeline.predict(
    modalities_inputs={"ecg": {"files": ["patient_ecg.mat"]}},
    clinical_notes="58-year-old female on doxorubicin"
)
```

### Text-Only Inference

```python
pipeline = MultiModalMedicalInference(
    language_model="standardmodelbio/smb-mntp-llama-3.1-8b",
)

predictions = pipeline.predict(
    clinical_notes="Patient with LVEF 45%, mild dyspnea"
)
```

## Output Format

```json
{
  "status": "success",
  "predictions": {
    "cardiotoxicity_risk": {
      "immediate": 0.23,
      "3_months": 0.31,
      "6_months": 0.35,
      "12_months": 0.40
    },
    "risk_category": "moderate",
    "recommendations": ["Monitor with ECG", "Consider dose adjustment"],
    "confidence_scores": {
      "ecg_quality": 0.95,
      "prediction_confidence": 0.78
    }
  }
}
```

## Notes

- The batch runner requires a `--modalities` JSON mapping that declares how to read inputs from the CSV. Example:
  - `{"ecg":{"path_column":"local_dat_path"},"ehr":{"columns":["age","gender","diagnosis"]}}`
- The core pipeline emits predictions only; evaluation/metrics are intentionally out-of-band for now.

## Requirements

- Python 3.11+
- CUDA GPU (optional, for faster inference)
- HuggingFace token (for private models)

## Environment Variables

```bash
# Required for private models
HF_TOKEN=hf_your_token_here

# Optional
RUNPOD_API_KEY=your_runpod_key   # For serverless deployment
```

## License

This project is licensed under the MIT License.