#!/usr/bin/env python
"""
Summarize validation results from JSON output
"""
import json
import sys
from pathlib import Path
import pandas as pd
import numpy as np

def load_validation_results(json_path):
    """Load validation results from JSON file"""
    with open(json_path, 'r') as f:
        return json.load(f)

def print_summary(results):
    """Print a formatted summary of validation results"""
    print("\n" + "=" * 70)
    print("CARDIOTOXICITY PREDICTION VALIDATION SUMMARY")
    print("=" * 70)
    
    # Model configuration
    print("\n📊 MODEL CONFIGURATION")
    print("-" * 30)
    config = results.get('model_config', {})
    print(f"Language Model: {config.get('language_model', 'N/A')}")
    print(f"ECG Encoder: {config.get('ecg_encoder', 'N/A')}")
    
    # Dataset info
    print("\n📈 DATASET")
    print("-" * 30)
    print(f"Total samples validated: {results.get('num_samples', 0)}")
    
    # Binary classification metrics
    print("\n🎯 BINARY CLASSIFICATION (Normal vs Dysfunction)")
    print("-" * 30)
    binary = results.get('binary_classification_metrics', {})
    print(f"Accuracy:  {binary.get('accuracy', 0):.3f}")
    print(f"Precision: {binary.get('precision', 0):.3f}")
    print(f"Recall:    {binary.get('recall', 0):.3f}")
    print(f"F1 Score:  {binary.get('f1_score', 0):.3f}")
    
    # Confusion matrix
    cm = binary.get('confusion_matrix', [[0,0],[0,0]])
    if len(cm) >= 2:
        print(f"\nConfusion Matrix:")
        print(f"                 Predicted")
        print(f"                 Dysf.  Norm.")
        print(f"Actual Dysf. :   {cm[0][0]:4d}  {cm[0][1]:4d}")
        print(f"Actual Norm. :   {cm[1][0]:4d}  {cm[1][1]:4d}")
        
        # Calculate additional metrics
        tn, fp = cm[0][0], cm[0][1] if len(cm[0]) > 1 else 0
        fn, tp = cm[1][0] if len(cm) > 1 else 0, cm[1][1] if len(cm) > 1 and len(cm[1]) > 1 else 0
        
        specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
        sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0
        
        print(f"\nSensitivity (True Positive Rate): {sensitivity:.3f}")
        print(f"Specificity (True Negative Rate): {specificity:.3f}")
    
    # Risk category metrics
    print("\n🚦 RISK CATEGORY CLASSIFICATION")
    print("-" * 30)
    risk = results.get('risk_category_metrics', {})
    print(f"Accuracy:  {risk.get('accuracy', 0):.3f}")
    print(f"Precision: {risk.get('precision', 0):.3f}")
    print(f"Recall:    {risk.get('recall', 0):.3f}")
    print(f"F1 Score:  {risk.get('f1_score', 0):.3f}")
    
    # Detailed results analysis
    if 'detailed_results' in results:
        detailed = results['detailed_results']
        df = pd.DataFrame(detailed)
        
        print("\n📊 DETAILED ANALYSIS")
        print("-" * 30)
        
        if 'lvef_true' in df.columns and 'immediate_risk_pred' in df.columns:
            # LVEF correlation with risk predictions
            correlation = df['lvef_true'].corr(df['immediate_risk_pred'])
            print(f"LVEF vs Risk Score Correlation: {correlation:.3f}")
            
            # Risk prediction statistics
            print(f"\nRisk Score Statistics:")
            print(f"  Mean:   {df['immediate_risk_pred'].mean():.3f}")
            print(f"  Std:    {df['immediate_risk_pred'].std():.3f}")
            print(f"  Median: {df['immediate_risk_pred'].median():.3f}")
            
        if 'confidence' in df.columns:
            print(f"\nModel Confidence:")
            print(f"  Mean:   {df['confidence'].mean():.3f}")
            print(f"  Min:    {df['confidence'].min():.3f}")
            print(f"  Max:    {df['confidence'].max():.3f}")
    
    print("\n" + "=" * 70)
    print("INTERPRETATION GUIDE")
    print("=" * 70)
    print("""
- LVEF < 40%: High risk (severe dysfunction)
- LVEF 40-50%: Moderate risk (mild dysfunction)  
- LVEF > 50%: Low risk (normal function)

Binary Classification:
- Class 0: Cardiac dysfunction (LVEF typically < 50%)
- Class 1: Normal function (LVEF typically ≥ 50%)

Note: Model predictions are based on ECG waveform analysis and may not
directly correlate with LVEF values. The model learns patterns in ECG
signals associated with cardiotoxicity risk.
""")

def main():
    if len(sys.argv) < 2:
        print("Usage: python summarize_validation.py <validation_results.json>")
        sys.exit(1)
    
    json_path = Path(sys.argv[1])
    if not json_path.exists():
        print(f"Error: File not found: {json_path}")
        sys.exit(1)
    
    results = load_validation_results(json_path)
    print_summary(results)

if __name__ == "__main__":
    main()