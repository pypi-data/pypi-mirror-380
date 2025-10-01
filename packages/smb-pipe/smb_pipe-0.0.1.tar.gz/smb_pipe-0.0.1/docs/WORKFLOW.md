# Complete LVEF Classification Workflow

This guide walks through the complete process of downloading MIMIC-IV ECG data, training an LVEF classification head, and running batch inference.

For single-patient inference, create a one-row CSV and use the batch runner.

## 📋 **Prerequisites**

- PhysioNet MIMIC-IV approval
- AWS credentials for S3 access
- HuggingFace token in `.env` file

## 🚀 **Step-by-Step Workflow**

### 1. Download ECG Data

**Option A: Download specific LVEF files**
```bash
cd /workspace/runpod-mm-cardiotox-inference
./scripts/data/mimic_to_s3.sh lvef  # Upload to S3 first
aws s3 sync s3://smb-dev-us-east-2-data/datasets/mimic-iv-ecg/1.0/waveforms/files/ /workspace/physionet.org/files/mimic-iv-ecg/1.0/files/ --region us-east-2
```

**Option B: Download complete dataset**
```bash
./scripts/data/mimic_to_s3.sh full  # Complete dataset to S3
aws s3 sync s3://smb-dev-us-east-2-data/datasets/mimic-iv-ecg/1.0/waveforms/files/ /workspace/physionet.org/files/mimic-iv-ecg/1.0/files/ --region us-east-2
```

### 2. Generate File Manifest

```bash
# Map ground truth LVEF labels to local file paths
uv run scripts/data/create_local_manifest.py

# Output: data/csv/lvef_with_local_paths.csv
# Shows which local files have LVEF ground truth
```

### 3. LVEF Classification Head

**Option A: Use Existing Trained Head (if compatible)**
```bash
# Check if trained head exists
ls -la models/lvef_head_weights.pt

# Test if it loads correctly (check for dimension mismatch)
uv run python scripts/validation/run_lvef_batch_inference.py \
    --csv data/csv/lvef_with_local_paths.csv \
    --output outputs/test_existing_head.csv \
    --max-samples 2

# If no errors, your existing head works! Proceed to Step 4.
# If dimension mismatch, use Option B to retrain.
```

**Option B: Train New Head (current architecture)**
```bash
# Fine-tune binary LVEF classifier with correct dimensions
uv run python scripts/training/train_lvef_head_simple.py \
    --csv data/csv/lvef_with_local_paths.csv \
    --epochs 20 \
    --batch-size 16 \
    --learning-rate 1e-4 \
    --input-dim 1024

# Creates: models/lvef_head_TIMESTAMP/ with weights, metrics, config
# Copies to models/lvef_head_weights.pt for auto-loading
```

**Option C: Use Specific Model Version**
```bash
# Copy specific version to standard location
cp models/lvef_head_YYYYMMDD_HHMMSS/weights.pt models/lvef_head_weights.pt

# Pipeline will auto-load this version
```

## 🔧 **Troubleshooting**

**If you see "dimension mismatch" errors:**
- Your existing head expects different embedding dimensions
- Retrain with `--input-dim 1024` for current model architecture
- Or backup old head: `mv models/lvef_head_weights.pt models/lvef_head_weights_old.pt`

### 4. Prepare CSV Data

**Required Columns (example):**
- `local_dat_path`: Path to ECG file (used when you map `ecg.path_column`)
- `clinical_notes`: Clinical text (optional; EHR columns can be folded in via `ehr.columns`)

**Optional Columns (passed as metadata):**
- `patient_id`, `age`, `gender`, `diagnosis`, `treatment`
- `baseline_lvef`, `current_lvef`, `troponin_baseline`, `troponin_current`

**Example CSV:**
```csv
patient_id,local_dat_path,clinical_notes,class,age,gender
P001,/path/to/ecg1.mat,"58F on doxorubicin therapy",0,58,F
P002,/path/to/ecg2.mat,"65M with baseline heart failure",1,65,M
```

### 5. Run Batch Inference (Main Pipeline)

**Option A: Use Auto-Loaded LVEF Head**
```bash
# Main pipeline with auto-loaded LVEF head (no W&B logging)
uv run src/batch_inference.py \
    --csv data/csv/lvef_with_local_paths.csv \
    --modalities '{"ecg":{"path_column":"local_dat_path"},"ehr":{"columns":["age","gender","diagnosis"]}}' \
    --out outputs/lvef_batch_results.jsonl \
    --max-samples 50 \
    --language-model standardmodelbio/Qwen3-WM-0.6B \
    --ecg-encoder PKUDigitalHealth/ECGFounder \
    --quiet

# Output: JSONL with inference results including LVEF predictions
```

**Option B: Use Specific LVEF Head**
```bash
# Specify exact LVEF head to use (no W&B logging)
uv run src/batch_inference.py \
    --csv data/csv/lvef_with_local_paths.csv \
    --modalities '{"ecg":{"path_column":"local_dat_path"}}' \
    --out outputs/lvef_specific_head.jsonl \
    --max-samples 50 \
    --language-model standardmodelbio/Qwen3-WM-0.6B \
    --ecg-encoder PKUDigitalHealth/ECGFounder \
    --lvef-head models/lvef_head_20250904_070457/weights.pt \
    --quiet \
    --show-prompts


# Output: Results using specified LVEF head version
# --show-prompts: Display input prompt previews in console (even with --quiet)
```

**Option C: With W&B Logging (Single Batch Run)**
```bash
# Full pipeline with experiment tracking and aggregate metrics
uv run src/batch_inference.py \
    --csv data/csv/lvef_with_local_paths.csv \
    --modalities '{"ecg":{"path_column":"local_dat_path"}}' \
    --out outputs/lvef_logged_results.jsonl \
    --max-samples 100 \
    --language-model standardmodelbio/Qwen3-WM-0.6B \
    --ecg-encoder PKUDigitalHealth/ECGFounder \
    --quiet

# Logs: batch_accuracy, dysfunction_f1, normal_f1, sample counts, config
# Users can integrate their own experiment tracking if desired.
```

**Ablation Testing**  
For ECG ablation studies and modality verification, see **[ABLATION.md](ABLATION.md)** for comprehensive testing procedures.

### 5. Output Format

**JSONL Output** (when using `--out` flag):
```jsonl
{"row": 0, "patient_id": "P001", "predictions": {"lvef_classification": {"class": 1, "normal_prob": 0.85, "dysfunction_prob": 0.15}, "cardiotoxicity_risk": {"immediate": 0.12}}, "metadata": {"ecg_used": true}}
{"row": 1, "patient_id": "P002", "predictions": {...}, "metadata": {...}}
```

**Key Fields:**
- `predictions.lvef_classification.class`: 0=dysfunction, 1=normal  
- `predictions.cardiotoxicity_risk.immediate`: Risk score 0-1
- `metadata.ecg_used`: Whether ECG was used for this prediction

### 6. Analyze Results

```bash
# View inference results (JSONL format)
head -2 outputs/lvef_batch_results.jsonl | jq '.'

# Extract LVEF predictions for analysis
jq '.predictions.lvef_classification' outputs/lvef_batch_results.jsonl

Note: Full run logs are written to `outputs/logs/batch_<csv>_<timestamp>.log`. Override with `--log-file`.

# Check training metrics
ls models/lvef_head_*/
cat models/lvef_head_*/README.md
```

## 📊 **Expected Results**

With current dataset size (**69,192 LVEF files, 91.8% coverage**):
- **Training samples**: ~55K train, ~14K test  
- **Excellent coverage**: 91.8% of all LVEF records available
- **Model performance**: 92% accuracy on validation samples (better than 71% training due to transfer learning)
- **Robust predictions**: Large dataset provides reliable classification

**If using existing head:**
- Pipeline automatically loads latest versioned model from `models/lvef_head_YYYYMMDD_HHMMSS/`
- Check compatibility by running small inference test first
- Retrain if dimension mismatch occurs

## 🔄 **Monitoring Progress**

```bash
# Monitor downloads
./scripts/monitoring/job_status.sh --watch

# Check training progress
# (outputs directly to console)

# Monitor inference progress  
tail -f /workspace/logs/aws_sync_background.log
```

## 📝 **Notes**

- **Idempotent**: All scripts can be rerun safely
- **Versioned**: Each training run creates timestamped model directory
- **Auto-loading**: Latest trained weights load automatically
- **Expandable**: Rerun manifest generation as more files download
- **Prediction Heads**: See [TOOL_HEADS.md](TOOL_HEADS.md) for training and architecture details
