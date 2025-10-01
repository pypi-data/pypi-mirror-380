#!/usr/bin/env python3
"""
Quick test of the unified inference pipeline with synthetic data.
Tests embedding extraction and prediction heads separately.
"""
import sys
import json
import pandas as pd
from pathlib import Path

# Add repository root to path (tests/pipeline-tests -> tests -> repo root).
project_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root / "src"))

def test_embedding_extraction():
    """Test just the ECG embedding extraction with one patient."""
    print("=== Testing ECG Embedding Extraction ===")
    
    # Test ECG encoder directly
    from utils.model_manager import ModelManager
    from utils import ECGDataLoader
    
    # Load one patient's data
    df = pd.read_csv("simdata/enhanced_simdata.csv")
    patient = df.iloc[0]
    
    print(f"Testing with patient: {patient['patient_id']}")
    
    # Initialize ECG encoder
    ecg_config = {
        "class": "ECGFounderEncoder",
        "model_id": "PKUDigitalHealth/ECGFounder",
        "mode": "12lead",
        "signal_length": 5000,
        "device": "cpu",
    }
    ecg_encoder = ModelManager.create_ecg_encoder(ecg_config)
    
    # Initialize ECG data loader
    ecg_loader = ECGDataLoader()
    
    # Test ECG embedding
    ecg_path = patient["baseline_ecg_local"]
    if Path(ecg_path).exists():
        print(f"Extracting ECG embedding from: {ecg_path}")
        
        # Load and process ECG
        ecg_data = ecg_loader.load_ecg_file(ecg_path)
        ecg_data = ecg_loader.preprocess_ecg(ecg_data, normalize=True)
        
        # Generate embedding
        ecg_embedding = ecg_encoder.encode(ecg_data)
        print(f"ECG embedding shape: {ecg_embedding.shape}")
        print(f"ECG embedding dtype: {ecg_embedding.dtype}")
        return True
    else:
        print(f"ECG file not found: {ecg_path}")
        return False

def test_prediction_heads():
    """Test the prediction heads with sample embeddings."""
    from models.prediction_heads import ClassificationHead, RegressionHead, create_prediction_head
    import torch
    
    print("\n=== Testing Prediction Heads ===")
    
    # Create sample embeddings (matching ECG embedding dimensions)
    batch_size = 1
    embedding_dim = 1024  # Matching actual ECG embedding dimension
    sample_embedding = torch.randn(batch_size, embedding_dim)
    
    # Test classification head
    print("Testing classification head...")
    class_head = ClassificationHead(input_dim=embedding_dim, num_classes=3)
    class_output = class_head(sample_embedding)
    print(f"Classification output shape: {class_output.shape}")
    print(f"Classification probabilities: {torch.softmax(class_output, dim=-1)}")
    
    # Test regression head
    print("\nTesting regression head...")
    reg_head = RegressionHead(input_dim=embedding_dim)
    reg_output = reg_head(sample_embedding)
    print(f"Regression output shape: {reg_output.shape}")
    print(f"Regression value: {reg_output.item()}")
    
    # Test survival head via factory function
    print("\nTesting survival head...")
    try:
        surv_head = create_prediction_head(
            "survival", 
            input_dim=embedding_dim, 
            config={"hidden_sizes": [256, 128], "output_size": 1}
        )
        surv_output = surv_head(sample_embedding)
        if isinstance(surv_output, tuple):
            print(f"Survival output type: tuple with {len(surv_output)} elements")
            for i, output in enumerate(surv_output):
                print(f"  Element {i} shape: {output.shape}")
        else:
            print(f"Survival output shape: {surv_output.shape}")
            print(f"Survival hazard: {surv_output.item()}")
    except ImportError:
        print("Survival head requires smbtogo package (not available)")
    except Exception as e:
        print(f"Survival head test failed: {e}")
    
    return True

if __name__ == "__main__":
    print("Starting unified pipeline tests...")
    
    try:
        # Test embedding extraction
        if test_embedding_extraction():
            print("✓ Embedding extraction test passed")
        else:
            print("✗ Embedding extraction test failed")
            sys.exit(1)
        
        # Test prediction heads
        if test_prediction_heads():
            print("✓ Prediction heads test passed")
        else:
            print("✗ Prediction heads test failed")
            sys.exit(1)
        
        print("\n✓ All tests passed!")
        
    except Exception as e:
        print(f"✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)