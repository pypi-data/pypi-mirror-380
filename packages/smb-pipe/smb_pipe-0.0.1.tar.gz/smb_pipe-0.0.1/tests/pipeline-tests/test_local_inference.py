#!/usr/bin/env python3
"""
Test the single-patient inference pipeline with synthetic data.
"""
import sys
import json
import pandas as pd
from pathlib import Path

# Add repository root to path (tests/pipeline-tests -> tests -> repo root).
project_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root / "src"))

from inference_pipeline import MultiModalMedicalInference 

def test_local_inference():
    """Test single-patient inference with synthetic data."""
    print("=== Testing Local Inference Pipeline ===")
    
    
    # Load synthetic data
    df = pd.read_csv("simdata/enhanced_simdata.csv")
    patient = df.iloc[0]
    
    print(f"Testing with patient: {patient['patient_id']}")
    
    # Initialize inference
    inference = MultiModalMedicalInference()
    
    # Prepare test data
    test_data = {
        "ecg_files": [patient["baseline_ecg_local"]],
        "clinical_notes": f"Patient {patient['patient_id']} - Age: {patient['age']}, Gender: {patient['gender']}, Treatment: {patient['treatment']}",
        "age": patient["age"],
        "gender": patient["gender"],
        "patient_id": patient["patient_id"]
    }
    
    print(f"Test data prepared:")
    print(f"  ECG file: {test_data['ecg_files'][0]}")
    print(f"  Clinical notes: {test_data['clinical_notes']}")
    
    # Run inference
    results = inference.predict(**test_data)
    
    print(f"\nInference Results:")
    print(f"  Status: {results.get('status', 'unknown')}")
    print(f"  Predictions available: {bool(results.get('predictions'))}")
    
    if results.get('predictions'):
        predictions = results['predictions']
        for key, value in predictions.items():
            print(f"    {key}: {value}")
    
    # Add assertions to verify the results
    assert results is not None, "Results should not be None"
    assert 'status' in results, "Results should contain 'status' field"
    assert 'predictions' in results, "Results should contain 'predictions' field"

if __name__ == "__main__":

    print(sys.path)
    try:
        test_local_inference()
        print("\n✓ Local inference test passed!")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Local inference test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)