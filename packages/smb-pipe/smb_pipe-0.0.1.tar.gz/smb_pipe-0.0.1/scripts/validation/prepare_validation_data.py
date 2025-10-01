#!/usr/bin/env python
"""
Prepare validation data by downloading ECG files and creating validation CSV
"""
import pandas as pd
import os
import subprocess
from pathlib import Path
from typing import List, Tuple

def prepare_ecg_paths(df: pd.DataFrame) -> pd.DataFrame:
    """Convert waveform_path to full ECG file paths"""
    base_path = "/workspace/physionet.org/files/mimic-iv-ecg/1.0/"
    df['ecg_file'] = base_path + df['waveform_path'] + '.dat'
    return df

def download_ecg_files(waveform_paths: List[str], base_url: str = "https://physionet.org/files/mimic-iv-ecg/1.0/") -> Tuple[int, int]:
    """Download ECG files (.dat and .hea) for given waveform paths"""
    success_count = 0
    total_count = len(waveform_paths)
    
    for i, path in enumerate(waveform_paths):
        if i % 10 == 0:
            print(f"Progress: {i}/{total_count} files processed...")
        
        # Create local directory
        local_path = f"/workspace/physionet.org/files/mimic-iv-ecg/1.0/{path}"
        local_dir = os.path.dirname(local_path)
        os.makedirs(local_dir, exist_ok=True)
        
        # Check if files already exist
        if os.path.exists(f"{local_path}.dat") and os.path.exists(f"{local_path}.hea"):
            success_count += 1
            continue
        
        # Download .dat and .hea files
        dat_url = f"{base_url}{path}.dat"
        hea_url = f"{base_url}{path}.hea"
        
        try:
            # Download .dat file
            result = subprocess.run(
                ["wget", "-q", "-O", f"{local_path}.dat", dat_url],
                capture_output=True,
                timeout=30
            )
            if result.returncode != 0:
                print(f"Failed to download {path}.dat")
                continue
            
            # Download .hea file
            result = subprocess.run(
                ["wget", "-q", "-O", f"{local_path}.hea", hea_url],
                capture_output=True,
                timeout=30
            )
            if result.returncode != 0:
                print(f"Failed to download {path}.hea")
                # Remove incomplete .dat file
                os.remove(f"{local_path}.dat")
                continue
                
            success_count += 1
        except Exception as e:
            print(f"Error downloading {path}: {e}")
    
    return success_count, total_count

def main():
    print("=" * 60)
    print("MIMIC-IV ECG Validation Data Preparation")
    print("=" * 60)
    
    # Load ground truth data
    print("\n1. Loading ground truth data...")
    df = pd.read_csv('/workspace/runpod-mm-cardiotox-inference/data/ground_truth/LVEF.csv')
    print(f"   Total records: {len(df)}")
    print(f"   Unique patients: {df['subject_id'].nunique()}")
    
    # Use subset for validation (first 1000 records or specify a different number)
    VALIDATION_SIZE = 1000  # Adjust this as needed
    df_validation = df.head(VALIDATION_SIZE)
    print(f"\n2. Using first {VALIDATION_SIZE} records for validation")
    
    # Prepare ECG paths
    df_validation = prepare_ecg_paths(df_validation)
    
    # Get unique waveform paths to download
    unique_paths = df_validation['waveform_path'].unique()
    print(f"   Unique ECG files needed: {len(unique_paths)}")
    
    # Download ECG files
    print(f"\n3. Downloading ECG files...")
    success, total = download_ecg_files(unique_paths.tolist())
    print(f"   Successfully downloaded: {success}/{total} files")
    
    # Filter to only include successfully downloaded files
    df_validation['file_exists'] = df_validation['ecg_file'].apply(os.path.exists)
    df_final = df_validation[df_validation['file_exists']].copy()
    df_final = df_final.drop('file_exists', axis=1)
    
    # Save validation CSV
    output_path = '/workspace/runpod-mm-cardiotox-inference/data/csv/lvef_validation.csv'
    df_final.to_csv(output_path, index=False)
    print(f"\n4. Validation CSV saved to: {output_path}")
    print(f"   Records with available ECG files: {len(df_final)}")
    
    # Show class distribution
    print(f"\n5. LVEF class distribution in validation set:")
    print(df_final['class'].value_counts().sort_index())
    
    print("\n" + "=" * 60)
    print("Preparation complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()