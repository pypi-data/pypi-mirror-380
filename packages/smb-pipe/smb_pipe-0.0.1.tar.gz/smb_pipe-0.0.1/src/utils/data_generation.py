"""Synthetic data generation utilities for testing."""

import os
import numpy as np
import scipy.io as sio
from typing import List
from loguru import logger


def create_synthetic_ecg_data(data_dir: str, ecg_files: List[str], patient_params: dict = None) -> None:
    """
    Create synthetic ECG data files for demo purposes.
    
    Args:
        data_dir: Base directory for ECG data
        ecg_files: List of ECG file paths to create
        patient_params: Optional dict with patient-specific parameters
    """
    logger.info("Creating synthetic ECG data for demonstration...")
    
    # Get patient-specific parameters or use defaults
    if patient_params is None:
        patient_params = {}
    
    patient_age = patient_params.get("age", 65)
    baseline_lvef = patient_params.get("baseline_lvef", 60)
    current_lvef = patient_params.get("current_lvef", 55)
    patient_hr = patient_params.get("heart_rate", 70)
    
    # Parameters for realistic ECG simulation
    sampling_rate = 500  # Hz
    duration = 10  # seconds
    num_samples = sampling_rate * duration
    num_channels = 12  # Standard 12-lead ECG
    
    for ecg_file in ecg_files:
        full_path = os.path.join(data_dir, ecg_file)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        # Generate synthetic ECG data
        # Simulate ECG with patient-specific characteristics and time-based changes
        if "baseline" in ecg_file:
            # Baseline ECG - use patient's baseline characteristics
            heart_rate = patient_hr
            # QRS amplitude correlates with LVEF
            qrs_amplitude = 1.0 + (baseline_lvef - 50) * 0.02  # Scale with LVEF
            noise_level = 0.03 + (patient_age - 40) * 0.001  # Age-related noise
        else:
            # Follow-up ECG - show treatment effects
            lvef_decline = baseline_lvef - current_lvef
            heart_rate = patient_hr + min(lvef_decline * 2, 20)  # HR increases with dysfunction
            qrs_amplitude = 1.0 + (current_lvef - 50) * 0.02  # Reduced with lower LVEF
            noise_level = 0.05 + (patient_age - 40) * 0.001 + lvef_decline * 0.005  # More noise with dysfunction
            
        # Create time array
        t = np.linspace(0, duration, num_samples)
        
        # Initialize ECG channels
        ecg_data = np.zeros((num_channels, num_samples))
        
        # Generate ECG-like waveforms for each channel
        for ch in range(num_channels):
            # Basic cardiac cycle components
            # P wave
            p_wave = 0.1 * np.sin(2 * np.pi * heart_rate/60 * t + ch * np.pi/6)
            
            # QRS complex (simplified)
            qrs_freq = heart_rate / 60
            qrs = np.zeros_like(t)
            for beat in range(int(duration * qrs_freq)):
                beat_time = beat / qrs_freq
                beat_idx = int(beat_time * sampling_rate)
                if beat_idx < num_samples - 20:
                    # Q wave
                    qrs[beat_idx:beat_idx+5] = -0.2 * qrs_amplitude
                    # R wave
                    qrs[beat_idx+5:beat_idx+10] = qrs_amplitude * (1 + 0.1 * ch)
                    # S wave
                    qrs[beat_idx+10:beat_idx+15] = -0.3 * qrs_amplitude
                    
            # T wave
            t_wave = 0.2 * np.sin(2 * np.pi * heart_rate/60 * t - np.pi/4 + ch * np.pi/12)
            
            # Combine components
            ecg_channel = p_wave + qrs + t_wave
            
            # Add baseline wander
            baseline_wander = 0.1 * np.sin(2 * np.pi * 0.2 * t)
            ecg_channel += baseline_wander
            
            # Add noise
            noise = np.random.normal(0, noise_level, num_samples)
            ecg_channel += noise
            
            # Apply channel-specific scaling
            channel_scales = [1.0, 1.1, 1.2, 0.9, 0.8, 1.0, 1.1, 0.9, 1.0, 1.2, 0.8, 1.0]
            ecg_data[ch] = ecg_channel * channel_scales[ch]
            
        # Save as .mat file
        mat_data = {
            'ecg': ecg_data,
            'sampling_rate': sampling_rate,
            'duration': duration,
            'num_channels': num_channels,
            'synthetic': True,
            'description': 'Synthetic ECG data for cardiotoxicity demo'
        }
        
        sio.savemat(full_path, mat_data)
        logger.info(f"Created synthetic ECG file: {full_path}")


def generate_example_clinical_data():
    """Generate example clinical data for testing."""
    return {
        "clinical_notes": """
        65-year-old female with locally advanced breast cancer (ER+/PR+/HER2-).
        Started adjuvant chemotherapy with doxorubicin (60 mg/m2) and cyclophosphamide 3 months ago.
        Completed 4 cycles. Patient reports mild fatigue but no chest pain or dyspnea.
        Past medical history: Hypertension (well-controlled), Type 2 diabetes.
        Current medications: Metformin, Lisinopril, Aspirin.
        Vital signs: BP 130/80, HR 78, regular rhythm.
        Physical exam: Normal S1/S2, no murmurs or gallops. No peripheral edema.
        Laboratory results: Troponin I increased from 0.02 to 0.08 ng/mL.
        LVEF by echo: 52% (baseline was 58%).
        """.strip(),
        
        "radiotherapy_dose": "45 Gy to left chest wall with boost to 50 Gy",
        
        "age": 65,
        "gender": "female",
        "cancer_type": "breast",
        "cancer_stage": "IIIA",
        "chemotherapy_agent": "doxorubicin",
        "chemotherapy_dose": "240 mg/m2 cumulative",
        "cycles_completed": 4,
        "baseline_lvef": "58%",
        "current_lvef": "52%",
        "baseline_troponin": "0.02 ng/mL",
        "current_troponin": "0.08 ng/mL",
        "diabetes": True,
        "hypertension": True,
        "bmi": 28.5,
        "smoking_history": "never",
        "family_history_cad": False,
    }