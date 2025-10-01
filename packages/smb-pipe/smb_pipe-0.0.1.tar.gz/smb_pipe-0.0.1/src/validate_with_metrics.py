#!/usr/bin/env python
"""
Validation script with metrics calculation for cardiotoxicity predictions
Compares model predictions against ground truth LVEF values
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Tuple
from dotenv import load_dotenv

import pandas as pd
import numpy as np
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_auc_score, classification_report,
    mean_absolute_error, mean_squared_error
)
from loguru import logger

# Load environment variables
load_dotenv()

from inference_pipeline import MultiModalMedicalInference

def lvef_to_risk_category(lvef: float) -> str:
    """
    Convert LVEF value to cardiotoxicity risk category
    LVEF < 40: High risk (severe dysfunction)
    LVEF 40-50: Moderate risk (mild dysfunction)  
    LVEF > 50: Low risk (normal function)
    """
    if lvef < 40:
        return "high"
    elif lvef <= 50:
        return "moderate"
    else:
        return "low"

def extract_risk_predictions(predictions: Dict) -> Dict[str, Any]:
    """Extract relevant risk predictions from model output"""
    if not predictions or predictions.get("status") != "success":
        return None
    
    pred_data = predictions.get("predictions", {})
    return {
        "risk_category": pred_data.get("risk_category", "unknown"),
        "immediate_risk": pred_data.get("cardiotoxicity_risk", {}).get("immediate", 0.5),
        "3_month_risk": pred_data.get("cardiotoxicity_risk", {}).get("3_months", 0.5),
        "6_month_risk": pred_data.get("cardiotoxicity_risk", {}).get("6_months", 0.5),
        "12_month_risk": pred_data.get("cardiotoxicity_risk", {}).get("12_months", 0.5),
        "confidence": pred_data.get("confidence_scores", {}).get("prediction_confidence", 0.0)
    }

def calculate_metrics(y_true: List, y_pred: List, labels: List[str] = None) -> Dict[str, float]:
    """Calculate classification metrics"""
    metrics = {}
    
    # Basic metrics
    metrics['accuracy'] = accuracy_score(y_true, y_pred)
    
    # Handle multiclass vs binary metrics
    unique_classes = list(set(y_true) | set(y_pred))
    if len(unique_classes) > 2:
        # Multiclass
        metrics['precision'] = precision_score(y_true, y_pred, average='macro', zero_division=0)
        metrics['recall'] = recall_score(y_true, y_pred, average='macro', zero_division=0)
        metrics['f1'] = f1_score(y_true, y_pred, average='macro', zero_division=0)
    else:
        # Binary
        metrics['precision'] = precision_score(y_true, y_pred, average='binary', pos_label=unique_classes[-1] if len(unique_classes) > 1 else unique_classes[0], zero_division=0)
        metrics['recall'] = recall_score(y_true, y_pred, average='binary', pos_label=unique_classes[-1] if len(unique_classes) > 1 else unique_classes[0], zero_division=0)
        metrics['f1'] = f1_score(y_true, y_pred, average='binary', pos_label=unique_classes[-1] if len(unique_classes) > 1 else unique_classes[0], zero_division=0)
    
    # Confusion matrix
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    metrics['confusion_matrix'] = cm.tolist()
    
    return metrics

def main():
    parser = argparse.ArgumentParser(description="Validate cardiotoxicity predictions with metrics")
    parser.add_argument(
        "--csv",
        type=str,
        required=True,
        help="Path to validation CSV with ground truth"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="outputs/validation_results.json",
        help="Output path for validation results"
    )
    parser.add_argument(
        "--max-samples",
        type=int,
        default=None,
        help="Maximum number of samples to validate"
    )
    parser.add_argument(
        "--language-model",
        type=str,
        default="standardmodelbio/Qwen3-WM-0.6B",
        help="Language model to use"
    )
    parser.add_argument(
        "--encoders",
        type=str,
        default=None,
        help="JSON mapping of modality to encoder id (e.g. '{\"ecg\": \"PKUDigitalHealth/ECGFounder\"}')"
    )
    
    args = parser.parse_args()
    
    # Load validation data
    logger.info(f"Loading validation data from {args.csv}")
    df = pd.read_csv(args.csv)
    
    if args.max_samples:
        df = df.head(args.max_samples)
    
    logger.info(f"Validating {len(df)} samples")
    
    # Initialize pipeline
    logger.info("Initializing inference pipeline...")
    encoders_map = None
    if args.encoders:
        try:
            import json as _json
            encoders_map = _json.loads(args.encoders)
            if not isinstance(encoders_map, dict):
                encoders_map = None
        except Exception:
            encoders_map = None
    pipe = MultiModalMedicalInference(
        language_model=args.language_model,
        encoders=encoders_map
    )
    
    # Process predictions
    results = []
    predictions = []
    ground_truths = []
    risk_categories_true = []
    risk_categories_pred = []
    
    for idx, row in df.iterrows():
        logger.info(f"Processing {idx+1}/{len(df)}: {row['ecg_file']}")
        
        try:
            # Run inference
            pred = pipe.predict(
                use_wandb=False,
                modalities_inputs={"ecg": {"files": [row['ecg_file']]}}
            )
            
            # Extract predictions
            risk_pred = extract_risk_predictions(pred)
            
            if risk_pred:
                # Ground truth
                lvef_true = row['LVEF']
                class_true = row['class']  # Binary: 0=dysfunction, 1=normal
                risk_true = lvef_to_risk_category(lvef_true)
                
                # Store results
                result = {
                    "subject_id": row['subject_id'],
                    "ecg_file": row['ecg_file'],
                    "lvef_true": lvef_true,
                    "class_true": class_true,
                    "risk_category_true": risk_true,
                    "risk_category_pred": risk_pred['risk_category'],
                    "immediate_risk_pred": risk_pred['immediate_risk'],
                    "confidence": risk_pred['confidence']
                }
                
                results.append(result)
                
                # For metrics calculation
                ground_truths.append(class_true)
                # Convert risk score to binary prediction (threshold at 0.5)
                predictions.append(1 if risk_pred['immediate_risk'] < 0.5 else 0)
                
                risk_categories_true.append(risk_true)
                risk_categories_pred.append(risk_pred['risk_category'])
                
        except Exception as e:
            logger.error(f"Error processing {row['ecg_file']}: {e}")
            continue
    
    # Calculate metrics
    logger.info("Calculating validation metrics...")
    
    # Binary classification metrics (normal vs dysfunction)
    binary_metrics = calculate_metrics(ground_truths, predictions, labels=[0, 1])
    
    # Risk category metrics
    risk_labels = ["low", "moderate", "high"]
    risk_metrics = calculate_metrics(risk_categories_true, risk_categories_pred, labels=risk_labels)
    
    # Create detailed report
    validation_report = {
        "timestamp": datetime.now().isoformat(),
        "num_samples": len(results),
        "model_config": {
            "language_model": args.language_model,
            "encoders": encoders_map or {}
        },
        "binary_classification_metrics": {
            "accuracy": binary_metrics['accuracy'],
            "precision": binary_metrics['precision'],
            "recall": binary_metrics['recall'],
            "f1_score": binary_metrics['f1'],
            "confusion_matrix": binary_metrics['confusion_matrix']
        },
        "risk_category_metrics": {
            "accuracy": risk_metrics['accuracy'],
            "precision": risk_metrics['precision'],
            "recall": risk_metrics['recall'],
            "f1_score": risk_metrics['f1'],
            "confusion_matrix": risk_metrics['confusion_matrix']
        },
        "detailed_results": results
    }
    
    # Save results
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(validation_report, f, indent=2)
    
    logger.info(f"Validation results saved to {output_path}")
    
    # Print summary
    print("\n" + "=" * 60)
    print("VALIDATION RESULTS SUMMARY")
    print("=" * 60)
    print(f"\nSamples validated: {len(results)}/{len(df)}")
    print(f"\nBinary Classification (Normal vs Dysfunction):")
    print(f"  Accuracy:  {binary_metrics['accuracy']:.3f}")
    print(f"  Precision: {binary_metrics['precision']:.3f}")
    print(f"  Recall:    {binary_metrics['recall']:.3f}")
    print(f"  F1 Score:  {binary_metrics['f1']:.3f}")
    print(f"\nRisk Category Classification:")
    print(f"  Accuracy:  {risk_metrics['accuracy']:.3f}")
    print(f"  Precision: {risk_metrics['precision']:.3f}")
    print(f"  Recall:    {risk_metrics['recall']:.3f}")
    print(f"  F1 Score:  {risk_metrics['f1']:.3f}")
    print("\nConfusion Matrix (Binary):")
    print(f"  True Negative:  {binary_metrics['confusion_matrix'][0][0]}")
    print(f"  False Positive: {binary_metrics['confusion_matrix'][0][1]}")
    print(f"  False Negative: {binary_metrics['confusion_matrix'][1][0]}")
    print(f"  True Positive:  {binary_metrics['confusion_matrix'][1][1]}")
    print("=" * 60)

if __name__ == "__main__":
    main()