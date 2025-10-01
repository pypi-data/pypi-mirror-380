#!/usr/bin/env python3
"""Test script for RunPod handler."""

import json
import os
import sys

# Set environment to avoid heavy model loading
os.environ["RUNPOD_ENVIRONMENT"] = "test"
os.environ["WANDB_MODE"] = "disabled"  # Disable W&B for testing

# Ensure src-based layout is on path from repo root.
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src'))

# Import handler
from rp_handler import handler

def test_health_check():
    """Test health check endpoint."""
    print("Testing health check...")
    event = {"input": {"health_check": True}}
    result = handler(event)
    print(f"Health check result: {json.dumps(result, indent=2)}")
    assert result["status"] == "healthy"
    print("✓ Health check passed")

def test_demo_mode():
    """Test demo mode (lightweight)."""
    print("\nTesting demo mode...")
    event = {"input": {"demo_mode": True}}
    
    # Override to use smaller model
    os.environ["DEMO_MODEL"] = "standardmodelbio/MACE-0.6B-base"
    
    try:
        result = handler(event)
        print(f"Demo mode status: {result.get('status')}")
        if result.get("status") == "success":
            print("✓ Demo mode passed")
        else:
            print(f"✗ Demo mode failed: {result.get('error')}")
    except Exception as e:
        print(f"✗ Demo mode error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_health_check()
    
    # Only test demo mode if requested
    if "--demo" in sys.argv:
        test_demo_mode()
    else:
        print("\nSkipping demo mode test (use --demo to run)")