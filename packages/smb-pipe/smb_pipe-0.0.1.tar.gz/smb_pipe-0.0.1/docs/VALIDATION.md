# Validation Guide

## Overview

This document describes the validation pipeline for the cardiotoxicity prediction models using MIMIC-IV ECG data with ground truth LVEF (Left Ventricular Ejection Fraction) values.

## Ground Truth Data

Ground truth data comes from the [ECGFounder repository](https://github.com/PKUDigitalHealth/ECGFounder/tree/master/csv):
- **LVEF.csv**: Contains 75,412 records mapping MIMIC-IV ECG files to LVEF values
- **ptbxl_label_modified.csv**: PTB-XL dataset labels (not currently used)

### LVEF Classification
- **Class 0**: Cardiac dysfunction (LVEF < 50%)
- **Class 1**: Normal function (LVEF ≥ 50%)

### Risk Categories
- **High Risk**: LVEF < 40% (severe dysfunction)
- **Moderate Risk**: LVEF 40-50% (mild dysfunction)
- **Low Risk**: LVEF > 50% (normal function)

## Data Download

### MIMIC-IV ECG Waveforms

ECG waveforms are downloaded from [PhysioNet MIMIC-IV-ECG](https://physionet.org/content/mimic-iv-ecg/):
- **Location**: S3 bucket `s3://smb-dev-us-east-2-data/datasets/mimic-iv-ecg/1.0/waveforms/`
- **Format**: WFDB format (.dat binary + .hea header files)
- **Size**: ~2.5TB for complete dataset

**For complete download instructions, see [Data Guide](DATA.md)**

## LVEF Binary Classification Head

### Overview

The pipeline includes a dedicated binary classification head specifically for LVEF prediction:
- **Classes**: 0=dysfunction (LVEF < 50%), 1=normal (LVEF ≥ 50%)  
- **Architecture**: 256-unit hidden layer with dropout
- **Auto-loading**: Loads pre-trained weights from `models/lvef_head_weights.pt` if available

### Fine-Tuning the LVEF Head

**Prerequisites:**
- Local ECG files downloaded (see [Data Guide](DATA.md))
- Local manifest CSV generated: `uv run scripts/data/create_local_manifest.py`

**Training:**
```bash
# Train binary LVEF classifier on local data
cd /workspace/runpod-mm-cardiotox-inference
uv run python scripts/training/train_lvef_head_simple.py \
  --csv data/csv/lvef_with_local_paths.csv \
  --epochs 20 \
  --batch-size 16 \
  --learning-rate 1e-4
```

**Expected Results:**
- Uses 69,192 local ECG samples (55K train, 14K test)
- Class distribution: ~23% dysfunction, ~77% normal  
- Test accuracy: ~71% with synthetic embeddings
- Saves weights to `models/lvef_head_weights.pt` 
- Auto-loaded in future inference runs

**Note:** The simple trainer uses synthetic embeddings for demo. For production, extract real embeddings from PKUDigitalHealth/ECGFounder.

## Running Validation

### LVEF Batch Inference and Comparison

Run inference on local ECG files and generate CSV comparing ground truth vs predictions:

```bash
# Ensure HF_TOKEN is in your .env file, then run:
cd /workspace/runpod-mm-cardiotox-inference

# Use auto-loaded LVEF head
uv run python scripts/validation/run_lvef_batch_inference.py \
    --csv data/csv/lvef_with_local_paths.csv \
    --output outputs/lvef_predictions_comparison.csv \
    --max-samples 50 \
    --language-model standardmodelbio/Qwen3-WM-0.6B \
    --ecg-encoder PKUDigitalHealth/ECGFounder

# Or specify exact head to use
uv run python scripts/validation/run_lvef_batch_inference.py \
    --csv data/csv/lvef_with_local_paths.csv \
    --output outputs/lvef_predictions_specific.csv \
    --max-samples 50 \
    --lvef-head models/lvef_head_20250904_070457/weights.pt
```

**Output CSV columns:**
- `ground_truth_lvef`, `ground_truth_class` - Actual LVEF values and binary class
- `predicted_lvef_class`, `predicted_dysfunction_prob`, `predicted_normal_prob` - Model predictions
- `predicted_cardiotox_risk` - Cardiotoxicity risk category (low/moderate/high)
- `class_match` - 1 if prediction matches ground truth, 0 otherwise

### Legacy Validation Scripts

### Quick Test (2 samples)
```bash
# Test with 2 samples to verify setup
HF_TOKEN=your_token uv run python src/validate_with_metrics.py \
  --csv data/csv/lvef_test_small.csv \
  --output outputs/validation_test.json \
  --max-samples 2
```

### Full Validation
```bash
# Validate with all available samples
HF_TOKEN=your_token uv run python src/validate_with_metrics.py \
  --csv data/csv/lvef_validation_ready.csv \
  --output outputs/validation_full.json \
  --max-samples 50
```

### Parameters
- `--csv`: Path to CSV with ground truth (columns: subject_id, ecg_file, LVEF, class)
- `--output`: Output JSON file for results
- `--max-samples`: Limit number of samples to validate
- `--language-model`: Model to use (default: standardmodelbio/Qwen3-WM-0.6B)
Note: Encoders are provided via `--encoders` JSON in CLI where applicable.

## Metrics Calculated

### Binary Classification Metrics
- **Accuracy**: Overall correct predictions
- **Precision**: True positives / (True positives + False positives)
- **Recall**: True positives / (True positives + False negatives)
- **F1 Score**: Harmonic mean of precision and recall
- **Confusion Matrix**: 2x2 matrix of predictions vs ground truth

### Risk Category Metrics
- Same metrics as above but for 3-class classification (low/moderate/high risk)

### Additional Analysis
- **LVEF Correlation**: Correlation between LVEF values and risk predictions
- **Confidence Scores**: Model confidence statistics
- **Risk Score Distribution**: Statistics of predicted risk scores

## Results Interpretation

### Example Results (50 samples)
```
Binary Classification (Normal vs Dysfunction):
  Accuracy:  0.700
  Precision: 0.700
  Recall:    1.000
  F1 Score:  0.824

Risk Category Classification:
  Accuracy:  0.660
  Precision: 0.220
  Recall:    0.333
  F1 Score:  0.265
```

### Viewing Results

```bash
# View formatted summary
uv run python scripts/validation/summarize_validation.py outputs/validation_full.json

# View raw JSON results
cat outputs/validation_full.json | jq .
```

## Current Status

As of the last run:
- **Downloaded**: 353 MIMIC-IV ECG files with ground truth
- **Validated**: 50 samples
- **Binary Accuracy**: 70% (Normal vs Dysfunction)
- **Risk Category Accuracy**: 66%

## Next Steps

1. **Download More Data**: Use `scripts/data/mimic_to_s3.sh` to get more samples (see [Data Guide](DATA.md))
2. **Run Larger Validation**: Remove `--max-samples` limit for full validation
3. **Fine-tune Models**: Use validation results to improve model performance
4. **Cross-validation**: Implement k-fold cross-validation for robust metrics