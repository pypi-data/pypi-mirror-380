#!/usr/bin/env python3
"""Run batch inference on LVEF data and generate comparison CSV.

This script runs inference on local ECG files and creates a CSV comparing
ground truth LVEF labels with model predictions.

Usage:
    cd /workspace/runpod-mm-cardiotox-inference
    uv run python scripts/validation/run_lvef_batch_inference.py \
        --csv data/csv/lvef_with_local_paths.csv \
        --output outputs/lvef_predictions_comparison.csv \
        --max-samples 50
"""

import argparse
import pandas as pd
import json
import os
from pathlib import Path
import sys
from loguru import logger
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Use the same import pattern as batch_inference.py
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

try:
    from inference_pipeline import MultiModalMedicalInference
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Make sure to run from project root: cd /workspace/runpod-mm-cardiotox-inference")
    sys.exit(1)


def run_batch_inference_and_compare(
    csv_path: str,
    output_path: str,
    max_samples: int = None,
    language_model: str = "standardmodelbio/Qwen3-WM-0.6B",
    ecg_encoder: str = "PKUDigitalHealth/ECGFounder",
    lvef_head_path: str = None
) -> None:
    """Run inference and create comparison CSV."""
    
    # Load data
    logger.info(f"Loading data from {csv_path}")
    df = pd.read_csv(csv_path)
    
    # Filter to records with local files
    df_local = df[df['local_dat_path'].notna() & (df['local_dat_path'] != '')].copy()
    logger.info(f"Found {len(df_local)} records with local ECG files")
    
    if len(df_local) == 0:
        logger.error("No records with local files found. Run scripts/data/create_local_manifest.py first.")
        return
    
    # Limit samples if requested
    if max_samples:
        df_local = df_local.head(max_samples)
        logger.info(f"Limited to {len(df_local)} samples for testing")
    
    # Check HuggingFace authentication
    if not os.environ.get("HF_TOKEN"):
        logger.warning("⚠️  HF_TOKEN not found in environment. Private models may fail to load.")
        logger.info("Add HF_TOKEN to your .env file or export it: export HF_TOKEN=hf_your_token")
    
    # Initialize inference pipeline
    logger.info("Initializing multimodal inference pipeline...")
    logger.info(f"ECG Encoder: {ecg_encoder}")
    logger.info(f"Language Model: {language_model}")
    
    pipeline = MultiModalMedicalInference(
        ecg_encoder=ecg_encoder,
        language_model=language_model
    )
    
    # Load specific LVEF head if specified
    if lvef_head_path:
        logger.info(f"Loading custom LVEF head: {lvef_head_path}")
        try:
            import torch
            state_dict = torch.load(lvef_head_path, map_location=pipeline.device)
            pipeline.prediction_heads.lvef_head.load_state_dict(state_dict)
            logger.success(f"✅ Loaded custom LVEF head from {lvef_head_path}")
        except Exception as e:
            logger.error(f"❌ Failed to load custom LVEF head: {e}")
            logger.info("Falling back to auto-loaded head")
    else:
        logger.info("Using auto-loaded LVEF head from models/lvef_head_weights.pt")
    
    # Prepare results dataframe
    results = []
    
    logger.info("Running batch inference...")
    
    for idx, row in df_local.iterrows():
        try:
            # Prepare file paths for the pipeline
            dat_file = Path(row['local_dat_path']).name  # Just filename
            ecg_data_dir = str(Path(row['local_dat_path']).parent)  # Directory
            
            # Run inference (ECG + empty clinical notes)
            prediction = pipeline.predict(
                ecg_files=[dat_file],
                ecg_data_dir=ecg_data_dir,
                clinical_notes="",  # ECG-only inference
                use_wandb=False
            )
            
            # Extract key predictions
            lvef_pred = prediction["predictions"]["lvef_classification"]
            cardiotox_risk = prediction["predictions"]["risk_category"]
            confidence = prediction["predictions"]["confidence_scores"]["prediction_confidence"]
            
            # Create result row
            result_row = {
                # Original data
                'subject_id': row['subject_id'],
                'waveform_path': row['waveform_path'],
                
                # Ground truth
                'ground_truth_lvef': row['LVEF'],
                'ground_truth_class': int(row['class']),
                
                # Model predictions
                'predicted_lvef_class': lvef_pred['class'],
                'predicted_dysfunction_prob': lvef_pred['dysfunction_prob'],
                'predicted_normal_prob': lvef_pred['normal_prob'],
                'predicted_cardiotox_risk': cardiotox_risk,
                
                # Model confidence
                'prediction_confidence': confidence,
                
                # Match indicators
                'class_match': int(lvef_pred['class'] == int(row['class'])),
                'dysfunction_correct': int(lvef_pred['class'] == 0 and row['class'] == 0),
                'normal_correct': int(lvef_pred['class'] == 1 and row['class'] == 1),
                
                # File paths (for debugging)
                'local_dat_path': row['local_dat_path']
            }
            
            results.append(result_row)
            
            if len(results) % 10 == 0:
                logger.info(f"Processed {len(results)}/{len(df_local)} samples")
                
        except Exception as e:
            logger.warning(f"Failed to process sample {idx} (subject {row['subject_id']}): {e}")
            continue
    
    if len(results) == 0:
        logger.error("No successful predictions generated")
        return
    
    # Create results DataFrame
    results_df = pd.DataFrame(results)
    
    # Calculate summary statistics
    total_samples = len(results_df)
    correct_predictions = results_df['class_match'].sum()
    accuracy = correct_predictions / total_samples
    
    dysfunction_samples = results_df[results_df['ground_truth_class'] == 0]
    normal_samples = results_df[results_df['ground_truth_class'] == 1]
    
    dysfunction_accuracy = dysfunction_samples['class_match'].mean() if len(dysfunction_samples) > 0 else 0
    normal_accuracy = normal_samples['class_match'].mean() if len(normal_samples) > 0 else 0
    
    # Add summary as comment at top of CSV
    summary_comment = f"""# LVEF Binary Classification Results
# Total samples: {total_samples}
# Overall accuracy: {accuracy:.3f} ({correct_predictions}/{total_samples})
# Dysfunction accuracy: {dysfunction_accuracy:.3f} ({dysfunction_samples['class_match'].sum()}/{len(dysfunction_samples)})
# Normal accuracy: {normal_accuracy:.3f} ({normal_samples['class_match'].sum()}/{len(normal_samples)})
# Generated: {pd.Timestamp.now().isoformat()}
"""
    
    # Save results
    output_path_obj = Path(output_path)
    output_path_obj.parent.mkdir(parents=True, exist_ok=True)
    
    # Write summary comment first, then CSV
    with open(output_path, 'w') as f:
        f.write(summary_comment)
    
    # Append CSV (without header comments)
    results_df.to_csv(output_path, mode='a', index=False)
    
    logger.success("Results Summary:")
    logger.success(f"  Total samples: {total_samples}")
    logger.success(f"  Overall accuracy: {accuracy:.3f} ({correct_predictions}/{total_samples})")
    logger.success(f"  Dysfunction accuracy: {dysfunction_accuracy:.3f}")
    logger.success(f"  Normal accuracy: {normal_accuracy:.3f}")
    logger.success(f"  Results saved to: {output_path}")
    
    print("\nFirst 5 predictions:")
    print(results_df[['subject_id', 'ground_truth_class', 'predicted_lvef_class', 'class_match']].head())


def main():
    parser = argparse.ArgumentParser(
        description="Run batch inference on LVEF data and compare with ground truth"
    )
    parser.add_argument("--csv", required=True, help="CSV with local ECG paths and ground truth")
    parser.add_argument("--output", required=True, help="Output CSV path for comparison results")
    parser.add_argument("--max-samples", type=int, default=None, help="Limit number of samples")
    parser.add_argument("--language-model", default="standardmodelbio/Qwen3-WM-0.6B", help="Language model")
    parser.add_argument("--ecg-encoder", default="PKUDigitalHealth/ECGFounder", help="ECG encoder")
    parser.add_argument("--lvef-head", default=None, help="Path to LVEF head weights (auto-loads from models/lvef_head_weights.pt if not specified)")
    
    args = parser.parse_args()
    
    run_batch_inference_and_compare(
        csv_path=args.csv,
        output_path=args.output,
        max_samples=args.max_samples,
        language_model=args.language_model,
        ecg_encoder=args.ecg_encoder,
        lvef_head_path=args.lvef_head
    )


if __name__ == "__main__":
    main()
