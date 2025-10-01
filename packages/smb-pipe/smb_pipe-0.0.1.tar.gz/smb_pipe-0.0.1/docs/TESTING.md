## Testing

### ECG Usage Verification

- Purpose: Fool-proof test that ECG embeddings are actively used and influence predictions
- Method: Paired rows with permutation control (runs text-only, with-ECG, and with-ECG-permuted)
- One-time setup (downloads to cache):

```bash
export HF_HOME=/workspace/.cache/huggingface
# If models require auth:
export HF_TOKEN=hf_your_token
```

- Quick run:

```bash
# Small, fast cohort (default now 10); override with ECG_ABLATION_SAMPLES
ECG_ABLATION_SAMPLES=10 uv run pytest -q -s -m hf_integration tests/test_ecg_usage_quick.py

# Faster on repeated runs by using HF cache
HF_HOME=/workspace/.cache/huggingface ECG_ABLATION_SAMPLES=8 \
  uv run pytest -q -s -m hf_integration tests/test_ecg_usage_quick.py
```

Notes:
- First run downloads models; subsequent runs use cache
- Test samples a small cohort (default 10 rows) and verifies ECG affects predictions
- Fails if permuted ECG produces identical results (proving ECG is ignored)


