#!/usr/bin/env python3
"""Evaluate LVEF binary classification using batch inference.

Runs inference on ECG files with local paths and compares predictions
against LVEF ground truth (dysfunction vs normal).

Usage:
    uv run scripts/evaluate_lvef_classification.py --csv data/csv/lvef_with_local_paths.csv --max-samples 100
"""

import argparse
import json
import pandas as pd
from pathlib import Path
from typing import List, Dict, Any
from loguru import logger
import numpy as np

from src.inference_pipeline import MultiModalMedicalInference


def map_risk_to_lvef_class(risk_category: str) -> int:
    """Map 3-class risk categories to binary LVEF classes.
    
    Args:
        risk_category: "low", "moderate", or "high"
        
    Returns:
        0 for dysfunction (low/moderate risk), 1 for normal (high risk)
    """
    # Note: This mapping may need adjustment based on model training
    # Low risk = healthy heart = normal function = class 1
    # Moderate/High risk = problematic heart = dysfunction = class 0
    if risk_category == "low":
        return 1  # Normal function
    else:  # moderate or high
        return 0  # Dysfunction


def evaluate_lvef_predictions(
    predictions: List[Dict[str, Any]], 
    ground_truth: List[int]
) -> Dict[str, float]:
    """Calculate binary classification metrics."""
    if len(predictions) != len(ground_truth):
        raise ValueError("Predictions and ground truth length mismatch")
    
    pred_classes = [map_risk_to_lvef_class(p["predictions"]["risk_category"]) for p in predictions]
    
    # Calculate metrics
    correct = sum(1 for p, gt in zip(pred_classes, ground_truth) if p == gt)
    total = len(ground_truth)
    accuracy = correct / total if total > 0 else 0.0
    
    # Calculate per-class metrics
    true_positives_normal = sum(1 for p, gt in zip(pred_classes, ground_truth) if p == 1 and gt == 1)
    true_negatives_dysfunction = sum(1 for p, gt in zip(pred_classes, ground_truth) if p == 0 and gt == 0)
    false_positives_normal = sum(1 for p, gt in zip(pred_classes, ground_truth) if p == 1 and gt == 0)
    false_negatives_normal = sum(1 for p, gt in zip(pred_classes, ground_truth) if p == 0 and gt == 1)
    
    # Precision and Recall for normal class
    precision_normal = true_positives_normal / (true_positives_normal + false_positives_normal) if (true_positives_normal + false_positives_normal) > 0 else 0.0
    recall_normal = true_positives_normal / (true_positives_normal + false_negatives_normal) if (true_positives_normal + false_negatives_normal) > 0 else 0.0
    f1_normal = 2 * precision_normal * recall_normal / (precision_normal + recall_normal) if (precision_normal + recall_normal) > 0 else 0.0
    
    return {
        "accuracy": accuracy,
        "correct": correct,
        "total": total,
        "precision_normal": precision_normal,
        "recall_normal": recall_normal,
        "f1_normal": f1_normal,
        "confusion_matrix": {
            "tp_normal": true_positives_normal,
            "tn_dysfunction": true_negatives_dysfunction, 
            "fp_normal": false_positives_normal,
            "fn_normal": false_negatives_normal
        }
    }


def main():
    parser = argparse.ArgumentParser(description="Evaluate LVEF classification")
    parser.add_argument("--csv", required=True, help="CSV with local_dat_path and LVEF ground truth")
    parser.add_argument("--max-samples", type=int, default=None, help="Limit number of samples to test")
    parser.add_argument("--language-model", default="standardmodelbio/Qwen3-WM-0.6B")
    parser.add_argument("--ecg-encoder", default="PKUDigitalHealth/ECGFounder")
    parser.add_argument("--output", default="outputs/lvef_classification_results.json", help="Output JSON file")
    
    args = parser.parse_args()
    
    # Load CSV
    df = pd.read_csv(args.csv)
    logger.info(f"Loaded {len(df)} records from {args.csv}")
    
    # Filter to only records with local files
    df_local = df[df['local_dat_path'].notna() & (df['local_dat_path'] != '')].copy()
    logger.info(f"Found {len(df_local)} records with local ECG files")
    
    if len(df_local) == 0:
        logger.error("No records with local files found. Run create_local_manifest.py first.")
        return 1
    
    # Limit samples if requested
    if args.max_samples:
        df_local = df_local.head(args.max_samples)
        logger.info(f"Limited to {len(df_local)} samples for testing")
    
    # Initialize pipeline
    logger.info("Initializing inference pipeline...")
    pipeline = MultiModalMedicalInference(
        ecg_encoder=args.ecg_encoder,
        language_model=args.language_model
    )
    
    # Run inference on each sample
    logger.info("Running inference...")
    predictions = []
    ground_truth = []
    
    for idx, row in df_local.iterrows():
        # Convert local paths to relative paths for the pipeline
        # The pipeline expects paths relative to ecg_data_dir
        dat_file = Path(row['local_dat_path']).name  # Just the filename
        ecg_data_dir = str(Path(row['local_dat_path']).parent)  # Directory containing the file
        
        try:
            result = pipeline.predict(
                ecg_files=[dat_file],
                ecg_data_dir=ecg_data_dir,
                clinical_notes="",  # ECG-only inference
                use_wandb=False
            )
            predictions.append(result)
            ground_truth.append(int(row['class']))
            
            if len(predictions) % 10 == 0:
                logger.info(f"Processed {len(predictions)}/{len(df_local)} samples")
                
        except Exception as e:
            logger.warning(f"Failed to process sample {idx}: {e}")
            continue
    
    if len(predictions) == 0:
        logger.error("No successful predictions generated")
        return 1
    
    # Evaluate predictions
    logger.info("Calculating metrics...")
    metrics = evaluate_lvef_predictions(predictions, ground_truth)
    
    # Save results
    results = {
        "evaluation_summary": metrics,
        "model_config": {
            "language_model": args.language_model,
            "ecg_encoder": args.ecg_encoder
        },
        "dataset_info": {
            "csv_file": args.csv,
            "total_samples_in_csv": len(df),
            "samples_with_local_files": len(df_local),
            "samples_processed": len(predictions)
        },
        "predictions": predictions  # Full prediction details
    }
    
    # Ensure output directory exists
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Print summary
    logger.success("LVEF Classification Results:")
    logger.success(f"  Accuracy: {metrics['accuracy']:.3f} ({metrics['correct']}/{metrics['total']})")
    logger.success(f"  F1 Score (Normal): {metrics['f1_normal']:.3f}")
    logger.success(f"  Precision (Normal): {metrics['precision_normal']:.3f}")
    logger.success(f"  Recall (Normal): {metrics['recall_normal']:.3f}")
    logger.info(f"Full results saved to: {output_path}")
    
    return 0


if __name__ == "__main__":
    exit(main())
