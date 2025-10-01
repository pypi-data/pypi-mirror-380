#!/usr/bin/env python3
"""RunPod handler for multimodal cardiotoxicity inference."""

# --- Flash-Attention fallback helper -----------------------------------------
import os as _os, importlib as _importlib, warnings as _warnings


def _maybe_disable_flash_attn() -> None:
    """Disable Flash-Attn 2 kernels on unsupported GPUs or if module missing."""
    if _os.getenv("FLASH_ATTENTION_2_DISABLE") is not None:
        return

    need_disable = False
    try:
        _importlib.import_module("flash_attn_2")
    except Exception:
        need_disable = True
    else:
        import torch as _torch  # local import to avoid early CUDA init

        if _torch.cuda.is_available():
            major, _ = _torch.cuda.get_device_capability()
            if major < 8:
                need_disable = True

    if need_disable:
        _os.environ["FLASH_ATTENTION_2_DISABLE"] = "1"
        _warnings.warn("Flash-Attention disabled – unsupported GPU or module missing.")


_maybe_disable_flash_attn()

# -----------------------------------------------------------------------------
"""
RunPod Serverless Handler for Cardiotoxicity Inference

This handler processes ECG data and clinical notes to generate
cardiotoxicity risk predictions using multimodal AI models.
"""

import sys
import json
import csv
import tempfile
import traceback
from pathlib import Path
from typing import Dict, List, Any, Optional
import urllib.request
from datetime import datetime
import gc
import time

import runpod
import boto3
import torch
import numpy as np
from loguru import logger

# Configure logging for RunPod
logger.add("runpod_handler.log", rotation="100 MB")
try:
    import transformers  # type: ignore
except Exception:
    transformers = None  # type: ignore
try:
    import safetensors  # type: ignore
except Exception:
    safetensors = None  # type: ignore

# Global pipeline instance to reuse across invocations
_GLOBAL_PIPELINE = None

# ensure standard os is imported for remainder of file
import os  # noqa: E402

# Ensure package root is importable as 'src'
src_root = Path(__file__).parent
if str(src_root) not in sys.path:
    sys.path.insert(0, str(src_root))
os.environ.setdefault("PYTHONPATH", str(src_root))

# Import inference pipeline
from inference_pipeline import MultiModalMedicalInference
from utils import ECGDataLoader, generate_example_clinical_data
from utils.data_generation import create_synthetic_ecg_data


def download_from_s3(s3_path: str, aws_access_key: str, aws_secret_key: str) -> str:
    """Download file from S3 to temp location."""
    # Parse S3 path
    if not s3_path.startswith("s3://"):
        raise ValueError(f"Invalid S3 path: {s3_path}")
    
    parts = s3_path[5:].split("/", 1)
    if len(parts) != 2:
        raise ValueError(f"Invalid S3 path format: {s3_path}")
    
    bucket, key = parts
    
    # Create S3 client
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )
    
    # Download to temp file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mat")
    s3_client.download_file(bucket, key, temp_file.name)
    
    return temp_file.name


def download_from_url(url: str) -> str:
    """Download file from URL to temp location."""
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mat")
    urllib.request.urlretrieve(url, temp_file.name)
    return temp_file.name


def download_csv_from_s3(s3_path: str, aws_access_key: str, aws_secret_key: str) -> str:
    """Download CSV file from S3 to temp location."""
    # Parse S3 path
    if not s3_path.startswith("s3://"):
        raise ValueError(f"Invalid S3 path: {s3_path}")
    
    parts = s3_path[5:].split("/", 1)
    if len(parts) != 2:
        raise ValueError(f"Invalid S3 path format: {s3_path}")
    
    bucket, key = parts
    
    # Create S3 client
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )
    
    # Download to temp file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    s3_client.download_file(bucket, key, temp_file.name)
    
    return temp_file.name


def parse_input_params(event: Dict[str, Any]) -> Dict[str, Any]:
    """
    Parse and validate input parameters from RunPod event.
    
    Expected input structure:
    {
        "input": {
            "ecg_files": ["path1.mat", "path2.mat"] or ["s3://bucket/key1.mat"],
            "clinical_notes": "Patient history...",
            "ecg_data_source": "local" | "s3" | "url",
            "aws_access_key_id": "...",  # if using S3
            "aws_secret_access_key": "...",  # if using S3
            
            # Optional clinical parameters
            "age": 65,
            "gender": "Female",
            "diagnosis": "Breast Cancer",
            "treatment": "Doxorubicin",
            "baseline_lvef": 58,
            "current_lvef": 52,
            "troponin_baseline": 0.02,
            "troponin_current": 0.08,
            
            # Optional model configuration
            "encoders": {"ecg": "PKUDigitalHealth/ECGFounder"},
            "language_model": "standardmodelbio/Qwen3-WM-0.6B",
            
            # Optional demo mode
            "demo_mode": false
        }
    }
    """
    input_data = event.get("input", {})
    
    # Default parameters
    params = {
        "ecg_files": input_data.get("ecg_files", []),
        "clinical_notes": input_data.get("clinical_notes", ""),
        "ecg_data_source": input_data.get("ecg_data_source", "local"),
        "aws_access_key_id": input_data.get("aws_access_key_id", os.getenv("AWS_ACCESS_KEY_ID", "")),
        "aws_secret_access_key": input_data.get("aws_secret_access_key", os.getenv("AWS_SECRET_ACCESS_KEY", "")),
        
        # Clinical parameters
        "age": input_data.get("age"),
        "gender": input_data.get("gender"),
        "diagnosis": input_data.get("diagnosis"),
        "treatment": input_data.get("treatment"),
        "baseline_lvef": input_data.get("baseline_lvef"),
        "current_lvef": input_data.get("current_lvef"),
        "troponin_baseline": input_data.get("troponin_baseline"),
        "troponin_current": input_data.get("troponin_current"),
        
        # Model configuration
        "encoders": input_data.get("encoders", {"ecg": input_data.get("ecg_encoder", "PKUDigitalHealth/ECGFounder")}),
        "language_model": input_data.get("language_model", "standardmodelbio/Qwen3-WM-0.6B"),
        
        # Special modes
        "demo_mode": input_data.get("demo_mode", False),
        "test_mode": input_data.get("test_mode", False),
        
        # CSV batch processing
        "csv_file": input_data.get("csv_file"),
        "csv_data_source": input_data.get("csv_data_source", "s3")
    }
    
    # Demo mode uses same defaults (ECGFounder + Qwen3-WM)

    # ----------------------------------------------
    # Relaxed validation: only require ECG files if
    # the selected language model appears to be
    # multimodal / ECG-aware.
    # ----------------------------------------------
    requires_ecg = not params["demo_mode"] and not params["test_mode"]
    if requires_ecg:
        model_id_lower = str(params["language_model"]).lower()
        ecg_encoder_specified = bool(params.get("encoders", {}).get("ecg"))
        # Heuristic: models containing "qwen" and our default ECG encoder signal multimodal support.
        is_multimodal = ecg_encoder_specified or "qwen" in model_id_lower or "wm" in model_id_lower
        requires_ecg = is_multimodal

    if requires_ecg and not params["ecg_files"]:
        raise ValueError("ecg_files is required for multimodal models. Provide --ecg-files or enable --demo/--test mode.")
    if requires_ecg and not params["clinical_notes"]:
        logger.warning("No clinical notes provided, using default prompt")
    
    return params


def prepare_ecg_files(params: Dict[str, Any]) -> tuple[List[str], str]:
    """
    Prepare ECG files based on data source.
    Returns list of local file paths and the data directory.
    """
    ecg_files = params["ecg_files"]
    ecg_data_source = params["ecg_data_source"]
    
    # Demo mode - create synthetic data
    if params["demo_mode"]:
        logger.info("Demo mode: Creating synthetic ECG data")
        ecg_data_dir = "/tmp/ecg_data"
        ecg_files = ["patient_001/baseline_ecg.mat", "patient_001/3month_ecg.mat"]
        create_synthetic_ecg_data(ecg_data_dir, ecg_files)
        return ecg_files, ecg_data_dir
    
    # Handle different data sources
    local_files = []
    temp_dir = tempfile.mkdtemp(prefix="ecg_")
    
    for ecg_file in ecg_files:
        if ecg_data_source == "s3":
            logger.info(f"Downloading from S3: {ecg_file}")
            local_path = download_from_s3(
                ecg_file,
                params["aws_access_key_id"],
                params["aws_secret_access_key"]
            )
            # Create relative path structure in temp dir
            file_name = Path(ecg_file).name
            dest_path = Path(temp_dir) / file_name
            os.rename(local_path, dest_path)
            local_files.append(file_name)
            
        elif ecg_data_source == "url":
            logger.info(f"Downloading from URL: {ecg_file}")
            local_path = download_from_url(ecg_file)
            file_name = Path(ecg_file).name
            dest_path = Path(temp_dir) / file_name
            os.rename(local_path, dest_path)
            local_files.append(file_name)
            
        else:  # local
            local_files.append(ecg_file)
            temp_dir = ""  # Use current directory
    
    return local_files, temp_dir


def process_csv_batch(params: Dict[str, Any], pipeline) -> List[Dict[str, Any]]:
    """Process multiple patients from CSV file."""
    logger.info("Processing CSV batch...")
    
    # Download CSV file
    if params["csv_data_source"] == "s3":
        csv_path = download_csv_from_s3(
            params["csv_file"],
            params["aws_access_key_id"],
            params["aws_secret_access_key"]
        )
    else:
        raise ValueError(f"Unsupported csv_data_source: {params['csv_data_source']}")
    
    results = []
    errors = []
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row_num, row in enumerate(reader, 1):
                try:
                    patient_id = row.get("patient_id", f"patient_{row_num:03d}")
                    logger.info(f"Processing patient {patient_id}")
                    
                    # Extract patient data from CSV row
                    patient_params = {
                        "ecg_files": [row["baseline_ecg_s3"], row["month3_ecg_s3"]],
                        "clinical_notes": row["clinical_notes"],
                        "ecg_data_source": "s3",
                        "aws_access_key_id": params["aws_access_key_id"],
                        "aws_secret_access_key": params["aws_secret_access_key"],
                        "demo_mode": False
                    }
                    
                    # Prepare ECG files for this patient
                    ecg_files, ecg_data_dir = prepare_ecg_files(patient_params)
                    
                    # Prepare clinical data for this patient
                    clinical_data = {
                        "clinical_notes": row["clinical_notes"],
                        "age": int(row["age"]) if row["age"] else None,
                        "gender": row["gender"] if row["gender"] else None,
                        "diagnosis": row["diagnosis"] if row["diagnosis"] else None,
                        "treatment": row["treatment"] if row["treatment"] else None,
                        "baseline_lvef": int(row["baseline_lvef"]) if row["baseline_lvef"] else None,
                        "current_lvef": int(row["current_lvef"]) if row["current_lvef"] else None,
                        "troponin_baseline": float(row["troponin_baseline"]) if row["troponin_baseline"] else None,
                        "troponin_current": float(row["troponin_current"]) if row["troponin_current"] else None
                    }
                    
                    # Run inference for this patient
                    predictions = pipeline.predict(
                        modalities_inputs={
                            "ecg": {"files": ecg_files, "data_dir": ecg_data_dir}
                        },
                        **clinical_data
                    )
                    
                    # Check for errors in predictions
                    if "error" in predictions:
                        raise RuntimeError(f"Inference failed: {predictions['error']}")
                    
                    # Store result
                    result = {
                        "patient_id": patient_id,
                        "status": "success",
                        "predictions": predictions
                    }
                    
                    # Include actual outcome/time if available
                    if "outcome" in row:
                        result["actual_outcome"] = int(row["outcome"])
                    if "time" in row:
                        result["actual_time"] = int(row["time"])
                    
                    results.append(result)
                    
                except Exception as e:
                    error_msg = f"Patient {patient_id}: {str(e)}"
                    logger.error(error_msg)
                    errors.append({
                        "patient_id": patient_id,
                        "error": str(e)
                    })
                    
    finally:
        # Clean up temp CSV file
        try:
            os.unlink(csv_path)
        except Exception:
            pass
    
    logger.info(f"Batch processing complete: {len(results)} successful, {len(errors)} failed")
    return results, errors


def format_batch_response(results: List[Dict[str, Any]], errors: List[Dict[str, Any]], 
                         inference_time: float, params: Dict[str, Any]) -> Dict[str, Any]:
    """Format response for batch CSV processing."""
    return {
        "status": "success",
        "batch_mode": True,
        "message": f"Batch cardiotoxicity assessment completed for {len(results)} patients",
        "total_patients": len(results) + len(errors),
        "successful": len(results),
        "failed": len(errors),
        "results": results,
        "errors": errors if errors else None,
        "metadata": {
            "inference_time_seconds": inference_time,
            "csv_file": params.get("csv_file"),
            "models_used": {
                "encoders": params.get("encoders", {}),
                "language_model": params["language_model"]
            },
            "timestamp": datetime.now().isoformat(),
            "runtime_versions": {
                "python": sys.version.split()[0],
                "torch": getattr(torch, "__version__", "n/a"),
                "transformers": getattr(transformers, "__version__", "n/a"),
                "safetensors": getattr(safetensors, "__version__", "n/a"),
            }
        }
    }


def prepare_clinical_data(params: Dict[str, Any]) -> Dict[str, Any]:
    """Prepare clinical data dictionary from parameters."""
    clinical_data = {}
    
    # Use provided clinical notes or generate default
    if params["clinical_notes"]:
        clinical_data["clinical_notes"] = params["clinical_notes"]
    else:
        # Generate example clinical data if in demo mode
        if params["demo_mode"]:
            example_data = generate_example_clinical_data()
            clinical_data.update(example_data)
        else:
            clinical_data["clinical_notes"] = "Clinical assessment requested."
    
    # Add optional clinical parameters
    clinical_params = [
        "age", "gender", "diagnosis", "treatment",
        "baseline_lvef", "current_lvef", 
        "troponin_baseline", "troponin_current"
    ]
    
    for param in clinical_params:
        if params[param] is not None:
            clinical_data[param] = params[param]
    
    return clinical_data


def initialize_pipeline_if_needed(params: Dict[str, Any]):
    """Initialize the global pipeline if not already initialized."""
    global _GLOBAL_PIPELINE
    
    # Quick test mode - skip heavy initialization
    if params.get("test_mode"):
        logger.info("Test mode - returning mock pipeline")
        return None
    
    if _GLOBAL_PIPELINE is None:
        logger.info("Initializing global inference pipeline...")
        try:
            # Check available memory
            if torch.cuda.is_available():
                gpu_mem = torch.cuda.get_device_properties(0).total_memory / (1024**3)
                logger.info(f"GPU available with {gpu_mem:.1f}GB memory")
                available_mem = torch.cuda.mem_get_info()[0] / (1024**3)
                logger.info(f"Available GPU memory: {available_mem:.1f}GB")
            
            # For demo mode or low memory, force CPU
            desired_device = "cpu" if params.get("demo_mode") else ("cuda" if torch.cuda.is_available() else "cpu")
            
            # Use smaller model for testing/demo
            language_model = params.get("language_model", "standardmodelbio/MACE-0.6B-base")
            if params.get("demo_mode"):
                language_model = "standardmodelbio/MACE-0.6B-base"  # Smaller model for demo
            
            _GLOBAL_PIPELINE = MultiModalMedicalInference(
                ecg_encoder=params.get("ecg_encoder", "PKUDigitalHealth/ECGFounder"),
                language_model=language_model,
                device=desired_device,
            )
            logger.info("Pipeline initialized successfully")
            
            # Force garbage collection
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
                
        except Exception as e:
            logger.error(f"Failed to initialize pipeline: {e}")
            _GLOBAL_PIPELINE = None
            raise
    
    return _GLOBAL_PIPELINE

def handler_inner(event: Dict[str, Any]) -> Dict[str, Any]:
    """
    Inner handler function with main logic.
    
    Returns:
        Dictionary with status, predictions, and metadata
    """
    logger.info("=== Cardiotoxicity Inference Handler Started ===")
    
    # Handle health check
    if event.get("input", {}).get("health_check"):
        return {
            "status": "healthy",
            "message": "Handler is running",
            "timestamp": datetime.now().isoformat()
        }
    
    # Log runtime versions for troubleshooting
    try:
        logger.info(f"Runtime versions -> torch: {torch.__version__}, transformers: {getattr(transformers, '__version__', 'n/a')}, safetensors: {getattr(safetensors, '__version__', 'n/a')}")
    except Exception:
        pass
    
    try:
        # Parse input parameters
        params = parse_input_params(event)
        
        # Check if CSV batch mode
        if params.get("csv_file"):
            logger.info(f"CSV batch mode detected: {params['csv_file']}")
            
            # Get or initialize pipeline
            pipeline = initialize_pipeline_if_needed(params)
            
            # Process CSV batch
            start_time = datetime.now()
            batch_results, batch_errors = process_csv_batch(params, pipeline)
            inference_time = (datetime.now() - start_time).total_seconds()
            
            # Return batch response
            return format_batch_response(batch_results, batch_errors, inference_time, params)
        
        else:
            # Single patient mode (existing logic)
            logger.info(f"Single patient mode: demo_mode={params['demo_mode']}, "
                       f"ecg_files={len(params['ecg_files'])}, "
                       f"data_source={params['ecg_data_source']}")
            
            # Prepare ECG files
            ecg_files, ecg_data_dir = prepare_ecg_files(params)
            logger.info(f"Prepared {len(ecg_files)} ECG files in {ecg_data_dir or 'current directory'}")
            
            # Prepare clinical data
            clinical_data = prepare_clinical_data(params)
            
            # Get or initialize pipeline
            pipeline = initialize_pipeline_if_needed(params)
            
            # Handle test mode
            if params.get("test_mode"):
                logger.info("Test mode - returning mock predictions")
                return {
                    "status": "success",
                    "message": "Test mode - mock predictions",
                    "predictions": {
                        "cardiotoxicity_risk": {
                            "immediate": 0.15,
                            "3_months": 0.25,
                            "6_months": 0.35,
                            "12_months": 0.45
                        },
                        "risk_category": "moderate",
                        "clinical_reports": {"report_0": "Test mode report"},
                        "recommendations": ["Test recommendation"],
                        "generated_response": "Test mode response",
                        "confidence_scores": {
                            "ecg_quality": 0.95,
                            "prediction_confidence": 0.85
                        },
                        "metadata": {
                            "test_mode": True,
                            "timestamp": datetime.now().isoformat()
                        }
                    },
                    "metadata": {
                        "test_mode": True,
                        "timestamp": datetime.now().isoformat()
                    }
                }
            
            # Run inference
            logger.info("Running inference...")
            start_time = datetime.now()
            
            predictions = pipeline.predict(
                ecg_files=ecg_files,
                ecg_data_dir=ecg_data_dir,
                **clinical_data
            )
            
            inference_time = (datetime.now() - start_time).total_seconds()
            
            # Check for errors in predictions
            if predictions.get("status") == "failed":
                raise RuntimeError(f"Inference failed: {predictions.get('error', 'Unknown error')}")
            
            # The new prediction format already has the proper structure
            # Just add runtime metadata
            if "metadata" in predictions:
                predictions["metadata"]["demo_mode"] = params["demo_mode"]
                predictions["metadata"]["runtime_versions"] = {
                    "python": sys.version.split()[0],
                    "torch": getattr(torch, "__version__", "n/a"),
                    "transformers": getattr(transformers, "__version__", "n/a"),
                    "safetensors": getattr(safetensors, "__version__", "n/a"),
                }
            
            response = predictions  # Use predictions directly as it has the right structure
            
            logger.info(f"=== Inference Completed Successfully in {inference_time:.2f}s ===")
            return response
        
    except Exception as e:
        error_msg = str(e)
        error_trace = traceback.format_exc()
        
        logger.error(f"Handler error: {error_msg}")
        logger.error(f"Traceback: {error_trace}")
        
        return {
            "status": "error",
            "message": "Cardiotoxicity inference failed",
            "error": error_msg,
            "error_trace": error_trace,
            "metadata": {
                "timestamp": datetime.now().isoformat()
            }
        }


def handler(event: Dict[str, Any]) -> Dict[str, Any]:
    """
    Main handler with error recovery and memory management.
    """
    start_time = time.time()
    
    try:
        # Check GPU memory before processing
        if torch.cuda.is_available():
            free_mem = torch.cuda.mem_get_info()[0] / (1024**3)
            logger.info(f"Available GPU memory: {free_mem:.1f}GB")
            if free_mem < 2.0:
                logger.warning("Low GPU memory - forcing CPU mode")
                if "input" in event:
                    event["input"]["force_cpu"] = True
        
        # Run the actual handler
        result = handler_inner(event)
        
        # Log execution time
        duration = time.time() - start_time
        logger.info(f"Handler completed in {duration:.1f}s")
        
        # Clean up memory after processing
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        
        return result
        
    except Exception as e:
        error_msg = str(e)
        error_trace = traceback.format_exc()
        
        logger.error(f"Handler error: {error_msg}")
        logger.error(f"Traceback: {error_trace}")
        
        # Try to recover memory
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        
        return {
            "status": "error",
            "message": "Inference failed",
            "error": error_msg,
            "error_trace": error_trace[:1000],  # Limit trace size
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "duration": time.time() - start_time
            }
        }


def initialize_runpod():
    """Initialize RunPod environment."""
    logger.info("=== RunPod Initialization ===")
    
    # Set memory optimization
    os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:512"
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    
    # Log environment info
    logger.info(f"Python: {sys.version}")
    logger.info(f"PyTorch: {torch.__version__}")
    logger.info(f"CUDA available: {torch.cuda.is_available()}")
    
    if torch.cuda.is_available():
        logger.info(f"GPU: {torch.cuda.get_device_name(0)}")
        total_mem = torch.cuda.get_device_properties(0).total_memory / (1024**3)
        logger.info(f"Total GPU memory: {total_mem:.1f}GB")
    
    # Test handler with health check
    try:
        logger.info("Running initialization test...")
        test_event = {"input": {"health_check": True}}
        result = handler(test_event)
        if result["status"] == "healthy":
            logger.info("✓ Initialization test passed")
        else:
            logger.warning("Initialization test failed")
    except Exception as e:
        logger.error(f"Initialization test error: {e}")


# RunPod serverless entrypoint
if __name__ == "__main__":
    # Initialize environment
    initialize_runpod()
    
    # Start RunPod handler
    logger.info("Starting RunPod serverless handler...")
    runpod.serverless.start({"handler": handler})