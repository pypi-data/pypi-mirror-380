#!/usr/bin/env python3
"""
Submit inference jobs to RunPod serverless endpoint with W&B tracking.

Features:
- Async job submission using run() instead of runsync()
- Multiple concurrent job handling
- Real-time result polling and W&B logging
- Comprehensive job tracking and visualization
"""

import json
import os
import sys
import time
import argparse
from typing import List, Dict, Any, Optional
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from dotenv import load_dotenv
from loguru import logger


class RunPodJobTracker:
    """Track RunPod serverless inference jobs with W&B."""
    
    def __init__(self, endpoint_id: str, project_name: str = "cardiotox-inference"):
        self.endpoint_id = endpoint_id
        self.api_key = os.environ.get("RUNPOD_API_KEY")
        if not self.api_key:
            raise RuntimeError("RUNPOD_API_KEY not set in environment")
        
        # W&B removed; users can integrate their own tracking client-side.
        
        self.project_name = project_name
        self.base_url = f"https://api.runpod.ai/v2/{endpoint_id}"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        
    def submit_job(self, payload: Dict[str, Any], job_name: Optional[str] = None) -> Dict[str, Any]:
        """Submit a job using async run() endpoint."""
        url = f"{self.base_url}/run"
        
        # Start job submission (tracking removed here).
        run = None
        
        try:
            # Submit job
            response = requests.post(url, headers=self.headers, json=payload, timeout=30)
            response.raise_for_status()
            
            job_data = response.json()
            job_id = job_data.get("id")
            
            # Log submission to W&B
            # No-op logging (W&B removed).
            
            logger.info(f"Job {job_id} submitted successfully")
            
            # Store job ID in W&B config for tracking
            # No global config updates.
            
            return {
                "job_id": job_id,
                "submission_data": job_data,
                "status": "submitted"
            }
            
        except Exception as e:
            # No-op logging on failure.
            raise
            
    def poll_job_status(self, job_id: str, run: Any = None, max_wait: int = 300, poll_interval: int = 2) -> Dict[str, Any]:
        """Poll job status until completion or timeout."""
        url = f"{self.base_url}/status/{job_id}"
        start_time = time.time()
        
        while time.time() - start_time < max_wait:
            try:
                response = requests.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                
                status_data = response.json()
                current_status = status_data.get("status")
                
                # No-op logging.
                
                logger.info(f"Job {job_id}: {current_status}")
                
                # Check if job is complete
                if current_status == "COMPLETED":
                    # Get the output
                    output = status_data.get("output")
                    
                    # No-op logging on completion.
                    
                    # Log any metrics from the output
                    if output and isinstance(output, dict):
                        # Extract and log cardiotoxicity metrics
                        pass
                    
                    # No run to finish.
                    return {
                        "job_id": job_id,
                        "status": "completed",
                        "output": output,
                        "execution_time": status_data.get("executionTime", 0) / 1000.0,
                        "total_time": time.time() - start_time,
                    }
                    
                elif current_status in ["FAILED", "CANCELLED", "TIMED_OUT"]:
                    error_msg = status_data.get("error", "Unknown error")
                    
                    # No-op logging on failure.
                    return {
                        "job_id": job_id,
                        "status": current_status.lower(),
                        "error": error_msg,
                        "total_time": time.time() - start_time,
                    }
                    
                # Job still running, continue polling
                time.sleep(poll_interval)
                
            except Exception as e:
                logger.error(f"Error polling job {job_id}: {e}")
                # No-op logging on polling error.
                
        # Timeout reached
        # No-op logging on timeout.
        
        return {
            "job_id": job_id,
            "status": "timeout",
            "error": f"Job did not complete within {max_wait} seconds",
            "total_time": max_wait,
        }
        
    def run_job(self, payload: Dict[str, Any], job_name: Optional[str] = None, 
                max_wait: int = 300) -> Dict[str, Any]:
        """Submit and track a single job to completion."""
        # Submit job
        job_info = self.submit_job(payload, job_name)
        
        # Poll for results
    result = self.poll_job_status(
            job_info["job_id"], 
            max_wait=max_wait
        )
        
        return result
        
    def run_multiple_jobs(self, payloads: List[Dict[str, Any]], 
                         job_names: Optional[List[str]] = None,
                         max_workers: int = 5,
                         max_wait: int = 300) -> List[Dict[str, Any]]:
        """Submit and track multiple jobs concurrently."""
        if job_names is None:
            job_names = [f"job_{i}" for i in range(len(payloads))]
            
        results = []
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all jobs
            future_to_payload = {}
            for payload, name in zip(payloads, job_names):
                future = executor.submit(self.run_job, payload, name, max_wait)
                future_to_payload[future] = (payload, name)
            
            # Collect results as they complete
            for future in as_completed(future_to_payload):
                payload, name = future_to_payload[future]
                try:
                    result = future.result()
                    results.append(result)
                    logger.info(f"Job {name} completed with status: {result['status']}")
                except Exception as e:
                    logger.error(f"Job {name} failed: {e}")
                    results.append({
                        "job_name": name,
                        "status": "error",
                        "error": str(e),
                        "payload": payload,
                    })
                    
        return results


def load_env() -> None:
    """Load environment variables from .env file."""
    here = Path(__file__).parent
    candidates = [
        here.parent / ".env",
        here / ".env",
        here.parent.parent / ".env",
    ]
    for path in candidates:
        if path.exists():
            load_dotenv(path)
            break


def build_payload(args: argparse.Namespace) -> Dict[str, Any]:
    """Build payload for RunPod API."""
    if args.test:
        return {"input": {"test_mode": True}}
    if args.demo:
        return {"input": {"demo_mode": True}}
    
    input_obj: Dict[str, Any] = {
        "ecg_files": args.ecg_files,
        "clinical_notes": args.clinical_notes or "Clinical assessment requested.",
        "ecg_data_source": args.ecg_data_source,
        "language_model": args.language_model,
    }
    # Optional encoders mapping (JSON string)
    if hasattr(args, "encoders") and args.encoders:
        try:
            input_obj["encoders"] = json.loads(args.encoders)
        except Exception:
            input_obj["encoders"] = {}
    
    # Add clinical parameters if provided
    # Note: argparse converts hyphens to underscores in attribute names
    clinical_params = [
        # Demographics
        ("age", args.age),
        ("gender", args.gender),
        ("bmi", args.bmi),
        # Diagnosis
        ("diagnosis", args.diagnosis),
        ("cancer_type", args.cancer_type),
        ("cancer_stage", args.cancer_stage),
        # Treatment
        ("treatment", args.treatment),
        ("chemotherapy_agent", args.chemotherapy_agent),
        ("chemotherapy_dose", args.chemotherapy_dose),
        ("cycles_completed", args.cycles_completed),
        ("radiotherapy_dose", args.radiotherapy_dose),
        # Cardiac metrics
        ("baseline_lvef", args.baseline_lvef),
        ("current_lvef", args.current_lvef),
        ("baseline_troponin", args.baseline_troponin),
        ("current_troponin", args.current_troponin),
        # Medical history (booleans - only include if True)
        ("hypertension", True if args.hypertension else None),
        ("diabetes", True if args.diabetes else None),
        ("smoking_history", args.smoking_history),
        ("family_history_cad", True if args.family_history_cad else None),
    ]
    
    # Only add parameters that are not None
    for param_name, param_value in clinical_params:
        if param_value is not None:
            input_obj[param_name] = param_value
    
    if args.ecg_data_source == "s3":
        input_obj["aws_access_key_id"] = args.aws_access_key_id or os.getenv("AWS_ACCESS_KEY_ID", "")
        input_obj["aws_secret_access_key"] = args.aws_secret_access_key or os.getenv("AWS_SECRET_ACCESS_KEY", "")
    
    return {"input": input_obj}


def parse_args(argv: List[str]) -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Submit inference jobs to RunPod with W&B tracking"
    )
    parser.add_argument(
        "--endpoint-id", 
        default=os.getenv("RUNPOD_ENDPOINT_ID", "h3j2ceye1tifzr"),
        help="RunPod endpoint ID"
    )
    parser.add_argument(
        "--demo", 
        action="store_true",
        help="Use demo mode (no files required)"
    )
    parser.add_argument(
        "--test",
        action="store_true", 
        help="Use test mode (lightweight, no model loading)"
    )
    parser.add_argument(
        "--max-wait",
        type=int,
        default=300,
        help="Maximum seconds to wait for job completion"
    )
    parser.add_argument(
        "--poll-interval",
        type=int,
        default=2,
        help="Seconds between status polls"
    )
    
    # Multiple job submission
    parser.add_argument(
        "--multi",
        type=int,
        default=1,
        help="Number of concurrent jobs to submit"
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=5,
        help="Maximum concurrent polling threads"
    )
    
    # W&B configuration
    parser.add_argument(
        "--wandb-project",
        default="cardiotox-inference",
        help="W&B project name"
    )
    parser.add_argument(
        "--job-name",
        default=None,
        help="Custom job name for W&B run"
    )
    
    # Input parameters
    parser.add_argument(
        "--ecg-files",
        nargs="*",
        default=[
            "s3://smb-dev-scratch/ecg/patient_001/baseline_ecg.mat",
            "s3://smb-dev-scratch/ecg/patient_001/3month_ecg.mat",
        ],
        help="ECG file paths (default: demo files on S3)"
    )
    parser.add_argument("--clinical-notes", default=None, help="Clinical notes")
    parser.add_argument(
        "--ecg-data-source",
        default="s3",
        choices=["local", "s3", "url"],
        help="ECG data source"
    )
    
    # Clinical parameters - Demographics
    parser.add_argument("--age", type=int, default=None, help="Patient age")
    parser.add_argument("--gender", default=None, help="Patient gender")
    parser.add_argument("--bmi", type=float, default=None, help="Body mass index")
    
    # Clinical parameters - Diagnosis
    parser.add_argument("--diagnosis", default=None, help="Primary diagnosis")
    parser.add_argument("--cancer-type", default=None, help="Type of cancer")
    parser.add_argument("--cancer-stage", default=None, help="Cancer stage")
    
    # Clinical parameters - Treatment
    parser.add_argument("--treatment", default=None, help="Treatment type")
    parser.add_argument("--chemotherapy-agent", default=None, help="Chemotherapy agent used")
    parser.add_argument("--chemotherapy-dose", default=None, help="Chemotherapy dose")
    parser.add_argument("--cycles-completed", type=int, default=None, help="Number of cycles completed")
    parser.add_argument("--radiotherapy-dose", default=None, help="Radiotherapy dose")
    
    # Clinical parameters - Cardiac metrics
    parser.add_argument("--baseline-lvef", default=None, help="Baseline LVEF (percent)")
    parser.add_argument("--current-lvef", default=None, help="Current LVEF (percent)")
    parser.add_argument("--baseline-troponin", default=None, help="Baseline troponin level")
    parser.add_argument("--current-troponin", default=None, help="Current troponin level")
    
    # Clinical parameters - Medical history
    parser.add_argument("--hypertension", action="store_true", help="Has hypertension")
    parser.add_argument("--diabetes", action="store_true", help="Has diabetes")
    parser.add_argument("--smoking-history", default=None, help="Smoking history")
    parser.add_argument("--family-history-cad", action="store_true", help="Family history of CAD")
    
    # Model configuration
    parser.add_argument(
        "--encoders",
        default=None,
        help="JSON mapping of modality to encoder id, e.g. '{\"ecg\": \"PKUDigitalHealth/ECGFounder\"}'"
    )
    parser.add_argument(
        "--language-model",
        default="standardmodelbio/Qwen3-WM-0.6B",
        help="Language model"
    )
    
    # AWS credentials for S3
    parser.add_argument("--aws-access-key-id", default=None)
    parser.add_argument("--aws-secret-access-key", default=None)
    
    return parser.parse_args(argv)


def main(argv: List[str]) -> int:
    """Main entry point."""
    load_env()
    args = parse_args(argv)
    
    # Initialize tracker
    tracker = RunPodJobTracker(
        endpoint_id=args.endpoint_id,
        project_name=args.wandb_project
    )
    
    # Build payload(s)
    base_payload = build_payload(args)
    
    # Always use the multiple job logic, even for single jobs
    num_jobs = args.multi
    logger.info(f"Submitting {num_jobs} job{'s' if num_jobs > 1 else ''}...")
    
    # Create job payloads and names
    payloads = []
    job_names = []
    for i in range(num_jobs):
        # You can modify payloads here to create variations
        payload = base_payload.copy()
        payloads.append(payload)
        
        # For single job, use the provided name directly
        if num_jobs == 1:
            job_names.append(args.job_name or f"job_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
        else:
            job_names.append(f"{args.job_name or 'job'}_{i:03d}")
    
    # Run all jobs (even if it's just one)
    results = tracker.run_multiple_jobs(
        payloads,
        job_names,
        max_workers=min(args.max_workers, num_jobs),  # Don't use more workers than jobs
        max_wait=args.max_wait
    )
    
    # Summary
    completed = sum(1 for r in results if r["status"] == "completed")
    failed = sum(1 for r in results if r["status"] in ["failed", "error", "timeout"])
    
    if num_jobs > 1:
        logger.info(f"\n=== Job Summary ===")
        logger.info(f"Total jobs: {num_jobs}")
        logger.info(f"Completed: {completed}")
        logger.info(f"Failed: {failed}")
    
    # Print results
    for i, result in enumerate(results):
        if num_jobs > 1:
            print(f"\n=== Job {i} ===")
        print(json.dumps(result, indent=2))
    
    # Return non-zero if any jobs failed
    if failed > 0:
        return 1
    
    logger.info(f"\nView results at: https://wandb.ai/{args.wandb_project}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))