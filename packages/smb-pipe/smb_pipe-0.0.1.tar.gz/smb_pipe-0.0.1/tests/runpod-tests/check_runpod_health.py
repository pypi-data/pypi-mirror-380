#!/usr/bin/env python3
"""Check RunPod endpoint health status."""

import os
import sys
import json
import requests
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_env_paths = [
    Path(__file__).resolve().parents[2] / ".env",
    Path(__file__).resolve().parents[1] / ".env",
]
for path in load_env_paths:
    if path.exists():
        load_dotenv(path)
        break

def check_health():
    """Check RunPod endpoint health."""
    
    # Get credentials
    api_key = os.environ.get("RUNPOD_API_KEY")
    endpoint_id = os.environ.get("RUNPOD_ENDPOINT_ID", "h3j2ceye1tifzr")
    
    if not api_key:
        print("❌ RUNPOD_API_KEY not set")
        return False
    
    # Check endpoint status
    url = f"https://api.runpod.ai/v2/{endpoint_id}/health"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    print(f"Checking endpoint: {endpoint_id}")
    print(f"URL: {url}")
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
            
            # Check workers
            workers = data.get("workers", {})
            if workers:
                print(f"\nWorkers Status:")
                for status, count in workers.items():
                    print(f"  {status}: {count}")
            
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error checking health: {e}")
        return False

def submit_health_check_job():
    """Submit a lightweight health check job."""
    
    api_key = os.environ.get("RUNPOD_API_KEY")
    endpoint_id = os.environ.get("RUNPOD_ENDPOINT_ID", "h3j2ceye1tifzr")
    
    if not api_key:
        print("❌ RUNPOD_API_KEY not set")
        return False
    
    # Submit health check job
    url = f"https://api.runpod.ai/v2/{endpoint_id}/runsync"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "input": {
            "health_check": True
        }
    }
    
    print(f"\nSubmitting health check job...")
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
            
            if data.get("status") == "healthy":
                print("✅ Health check job succeeded")
                return True
            else:
                print(f"⚠️ Unexpected response: {data}")
                return False
        else:
            print(f"❌ Health check job failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error submitting health check: {e}")
        return False

if __name__ == "__main__":
    print("=== RunPod Endpoint Health Check ===\n")
    
    # Check basic endpoint health
    if check_health():
        print("\n✅ Endpoint is reachable")
    else:
        print("\n❌ Endpoint is not reachable")
        sys.exit(1)
    
    # Try to submit a health check job
    if "--job" in sys.argv:
        print("\n" + "="*40)
        if submit_health_check_job():
            print("\n✅ Health check job completed")
        else:
            print("\n❌ Health check job failed")
            sys.exit(1)