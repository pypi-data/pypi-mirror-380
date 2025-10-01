# Vendor Directory

Contains third-party code vendored locally for compatibility.

## ECGFounder

**Path:** `ecgfounder/`  
**Purpose:** ECGFounder model architecture and checkpoint loading utilities  
**Source:** PKU Digital Health ECGFounder project  

ECGFounder publishes pre-trained weights as `.pth` files but doesn't provide standard HuggingFace model definitions. This vendored code bridges that gap by implementing the `Net1D` architecture and checkpoint loaders.

**Files:**
- `net1d.py` - Core ECGFounder CNN architecture (ResNet-style 1D convolutions)
- `model.py` - Factory functions to instantiate and load 12-lead/1-lead models  

**Usage:** Automatically used when `--ecg-encoder PKUDigitalHealth/ECGFounder` is specified.
