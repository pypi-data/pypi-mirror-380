# Ablation Testing Guide

## Overview

Ablation testing verifies that ECG embeddings (and future modalities) genuinely influence model predictions rather than being ignored. This is critical for validating multimodal models.

## Quick ECG Usage Verification

**Fool-proof permutation control test (recommended):**
```bash
uv run pytest -q -s -m hf_integration tests/test_ecg_usage_quick.py
```

**What it does:**
- Samples a small fixed cohort (default 40 rows)
- Runs 3 passes: text-only, with-ECG (correct pairing), with-ECG (ECG permuted)
- Fails if correct vs permuted produce identical classes and near-zero probability deltas
- **Proves** ECG affects predictions via permutation control

## Paired Row Ablation (Small Scale)

**Quick smoke test (paired rows, ~10–20 min on 1 GPU):**
```bash
uv run python scripts/ablation/run_ecg_ablation_long.py \
  --csv data/csv/lvef_with_local_paths.csv \
  --samples-per-pass 100 \
  --language-model standardmodelbio/Qwen3-WM-0.6B \
  --ecg-encoder PKUDigitalHealth/ECGFounder \
  --random-sample --seed 42 \
  --quiet
```

## Paired Row Ablation (Large Scale)

**Larger run (paired rows, hours depending on hardware):**
```bash
uv run python scripts/ablation/run_ecg_ablation_long.py \
  --csv data/csv/lvef_with_local_paths.csv \
  --samples-per-pass 1200 \
  --language-model standardmodelbio/Qwen3-WM-0.6B \
  --ecg-encoder PKUDigitalHealth/ECGFounder \
  --random-sample --seed 42 \
  --quiet
```

**Output locations:**
- Timestamped JSONL under `outputs/`
- Logs under `outputs/logs/` (use `--log-file` to override)

**What it reports:**
- `with_ecg_acc` vs `text_only_acc`
- `class_changes` count and average probability deltas
- Runs both modes on the **exact same rows** for fair comparison

## Interpreting Results

### Expected Patterns

**Strong ECG Usage (Ideal):**
- Accuracy difference: 5-15%
- Class changes: 10-30% of samples
- Probability deltas: >0.1 average

**Weak ECG Usage (Concerning):**
- Accuracy difference: 0-2%
- Class changes: <5% of samples  
- Probability deltas: <0.05 average

**No ECG Usage (Problem):**
- Identical accuracies
- Zero class changes
- Near-zero probability deltas

### Debugging Poor Results

1. **Check training**: Are ECG connectors trained?
2. **Check architecture**: Are embeddings reaching prediction heads?
3. **Check data**: Are ECG files loading correctly?
4. **Check embeddings**: Are ECG embeddings non-zero?

## Ablation for New Modalities

When adding new modalities (e.g., CT, lab results):

### 1. Unit Test Template
```python
# tests/test_[modality]_usage_quick.py
def test_new_modality_usage():
    # Similar to test_ecg_usage_quick.py but for new modality
    # Test with/without modality + permutation control
    pass
```

### 2. Integration Test  
```bash
# Extend run_ecg_ablation_long.py to support new modality flags
uv run python scripts/ablation/run_multimodal_ablation.py \
  --csv data.csv \
  --with-ecg --with-ct --with-labs \
  --ablate ecg  # Test removing ECG while keeping others
```

### 3. Cross-Modal Ablation
```bash
# Test all combinations
for modality in ecg ct labs; do
  python scripts/ablation/run_multimodal_ablation.py \
    --csv data.csv --ablate $modality
done
```

## Best Practices

1. **Use paired rows**: Same samples for with/without comparisons
2. **Use permutation control**: Shuffle modality assignments to prove usage
3. **Fixed random seeds**: Ensure reproducible results
4. **Multiple sample sizes**: Test on 50, 100, 500, 1200 samples
5. **Log everything**: Save full prompts, embeddings, predictions
6. **Statistical significance**: Use proper tests for accuracy comparisons

## Troubleshooting

**Issue: Zero class changes despite model differences**
- Check if probability differences exist but don't cross decision boundary
- Lower sample size might not show rare class changes
- Model might be overconfident on text alone

**Issue: Identical outputs**
- Verify modality embeddings are non-zero
- Check if embeddings reach the model forward pass
- Confirm model architecture supports multimodal inputs

**Issue: Inconsistent results**
- Use fixed random seeds
- Ensure same data preprocessing
- Check for data leakage between runs
