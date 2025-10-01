# Prediction Heads Training Guide

## Overview

The cardiotoxicity pipeline uses 4 specialized prediction heads built on top of the language model's hidden states. Currently, **only the LVEF head is trained** - the other 3 heads use random initialization.

## Architecture Summary

### Current Heads (in `src/models/prediction_heads.py`)

| Head | Purpose | Outputs | Status |
|------|---------|---------|--------|
| **LVEF Head** | Binary LVEF classification | `[dysfunction, normal]` | ✅ **Trained** |
| **Survival Head** | Time-based risk regression | `[immediate, 3mo, 6mo, 12mo]` | ❌ Untrained |
| **Classification Head** | Risk category classification | `[low, moderate, high]` | ❌ Untrained |
| **Confidence Head** | Quality/confidence scores | `[ecg_quality, pred_confidence]` | ❌ Untrained |

### Why Only 1 Trained Head?

**LVEF Head:** Has ground truth labels from MIMIC-IV dataset
```python
# In prediction_heads.py - only LVEF has weight loading
def _load_lvef_weights(self):
    # Loads from models/lvef_head_YYYYMMDD_HHMMSS/weights.pt
```

**Other Heads:** No ground truth data available yet
```python
# These use random initialization (torch.nn.Linear default)
self.survival_head = self._build_regression_head(...)     # Random weights
self.classification_head = self._build_classification_head(...)  # Random weights  
self.confidence_head = self._build_regression_head(...)   # Random weights
```

## Training the LVEF Head

### Current Training Status

The LVEF head is **already trained** with:
- **Data**: MIMIC-IV ECG dataset with LVEF ground truth
- **Task**: Binary classification (dysfunction <50% vs normal ≥50%)
- **Architecture**: `Hidden[1536] → Linear[256] → ReLU → Dropout[0.1] → Linear[2]`
- **Performance**: ~71% accuracy (see model metrics)

### Training Script Location

```bash
# LVEF head training (already completed)
uv run python scripts/training/train_lvef_head_simple.py \
    --csv data/csv/lvef_with_local_paths.csv \
    --epochs 20 \
    --batch-size 16 \
    --learning-rate 1e-4 \
    --input-dim 1024
```

### Retraining LVEF Head

**When to retrain:**
- New language model (different hidden_size)
- More LVEF ground truth data available
- Different architecture needed

**Training command:**
```bash
uv run python scripts/training/train_lvef_head_simple.py \
    --csv data/csv/lvef_with_local_paths.csv \
    --epochs 20 \
    --batch-size 16 \
    --learning-rate 1e-4 \
    --input-dim 1536  # Match your model's hidden_size
```

**Output:**
- Trained weights: `models/lvef_head_YYYYMMDD_HHMMSS/weights.pt`
- Metrics: `models/lvef_head_YYYYMMDD_HHMMSS/metrics.json`
- Training logs and validation curves

## Training Other Heads (Future Work)

### 1. Survival Head Training

**Requirements:**
- Ground truth survival/outcome data with timestamps
- Patient follow-up data at 3mo, 6mo, 12mo intervals
- Events: cardiotoxicity onset, hospitalization, etc.

**Data format needed:**
```csv
patient_id,clinical_notes,ecg_file,event_immediate,event_3mo,event_6mo,event_12mo
P001,"...",ecg1.mat,0,0,1,1  # Event at 6mo
P002,"...",ecg2.mat,0,0,0,0  # No events
```

**Training approach:**
- **Loss**: Binary cross-entropy for each time point
- **Metrics**: Time-to-event AUC, calibration curves
- **Validation**: Temporal split (train on earlier, test on later)

### 2. Classification Head Training  

**Requirements:**
- Ground truth risk stratification labels
- Expert annotations: low/moderate/high risk
- Clinical outcome validation

**Data format needed:**
```csv
patient_id,clinical_notes,ecg_file,risk_category
P001,"...",ecg1.mat,high
P002,"...",ecg2.mat,low
```

**Training approach:**
- **Loss**: Cross-entropy loss
- **Metrics**: Accuracy, F1 per class, confusion matrix
- **Class balancing**: Weight rare classes appropriately

### 3. Confidence Head Training

**Requirements:**
- ECG quality annotations (expert-labeled)
- Prediction confidence ground truth (model uncertainty)
- Out-of-distribution detection data

**Training approaches:**

**ECG Quality:**
```python
# Requires expert ECG quality annotations
# Loss: MSE or BCE depending on continuous/discrete labels
```

**Prediction Confidence:**
```python
# Self-supervised: Use prediction accuracy as confidence target
# Or use ensemble disagreement as uncertainty proxy
```

## Model Management

### Directory Structure
```
models/
├── lvef_head_20250904_070457/          # Trained LVEF head
│   ├── weights.pt                      # PyTorch state dict
│   ├── metrics.json                    # Training metrics
│   ├── config.json                     # Architecture config
│   └── README.md                       # Training details
├── survival_head_YYYYMMDD_HHMMSS/      # Future: trained survival head
└── classification_head_YYYYMMDD_HHMMSS/  # Future: trained classification head
```

### Loading Custom Heads

**Specific head:**
```python
# Load specific LVEF head version
pipeline = MultiModalMedicalInference(...)
pipeline.prediction_heads.load_lvef_head("models/lvef_head_20250904_070457/weights.pt")
```

**Auto-load latest:**
```python
# Automatically loads most recent by timestamp
pipeline.prediction_heads.load_lvef_head()  # Uses latest in models/lvef_head_*/
```

## Training New Heads

### 1. Create Training Script Template

```python
# scripts/training/train_[head_name]_head.py
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from sklearn.metrics import accuracy_score

def train_head(head_module, train_loader, val_loader, epochs=20):
    optimizer = torch.optim.Adam(head_module.parameters(), lr=1e-4)
    criterion = nn.CrossEntropyLoss()  # or MSELoss for regression
    
    for epoch in range(epochs):
        # Training loop
        head_module.train()
        for batch in train_loader:
            # Extract features, run head, compute loss
            pass
            
        # Validation
        head_module.eval()
        # Compute validation metrics
        
    return head_module
```

### 2. Data Preparation

```python
# Create dataset class for your head
class CardiotoxicityDataset(torch.utils.data.Dataset):
    def __init__(self, csv_file, pipeline):
        self.data = pd.read_csv(csv_file)
        self.pipeline = pipeline
        
    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        
        # Get hidden features from language model
        with torch.no_grad():
            hidden = self.pipeline.get_hidden_features(
                clinical_notes=row['clinical_notes'],
                ecg_files=[row['ecg_file']] if 'ecg_file' in row else None
            )
        
        target = row['target_label']  # Your ground truth
        return hidden, target
```

### 3. Evaluation Framework

```python
def evaluate_head(head_module, test_loader, task_type="classification"):
    head_module.eval()
    predictions, targets = [], []
    
    with torch.no_grad():
        for hidden, target in test_loader:
            pred = head_module(hidden)
            predictions.append(pred.cpu())
            targets.append(target.cpu())
    
    if task_type == "classification":
        return accuracy_score(targets, predictions.argmax(dim=1))
    else:  # regression
        return torch.nn.functional.mse_loss(predictions, targets)
```

## Best Practices

1. **Temporal Validation**: Train on earlier data, test on later data
2. **Cross-Validation**: 5-fold CV with patient-level splits
3. **Ablation Studies**: Train with/without ECG to prove multimodal benefit
4. **Calibration**: Ensure prediction probabilities are well-calibrated
5. **Documentation**: Save training configs, data splits, metrics
6. **Versioning**: Use timestamps for model versions
7. **Monitoring**: Track training/validation curves, early stopping

## Future Expansions

### Multi-Task Training
Train all heads jointly with shared representations:
```python
# Joint loss combining all tasks
total_loss = (
    lvef_loss + 
    survival_loss + 
    classification_loss + 
    confidence_loss
)
```

### New Modality Integration
When adding new modalities (CT, labs):
1. **Extend heads** to handle new input dimensions
2. **Retrain existing heads** with new modality features
3. **Create modality-specific heads** if needed
4. **Run ablations** to prove each modality's value
