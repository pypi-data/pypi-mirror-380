#!/usr/bin/env python3
"""
Local testing for RunPod handler following their documentation.
https://docs.runpod.io/serverless/development/local-testing
"""

import os
import sys
import json
import runpod

# Add src to path from repository root.
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src'))

# Mock the RunPod serverless environment
os.environ["RUNPOD_ENVIRONMENT"] = "local_test"
os.environ["RUNPOD_DEBUG"] = "true"

def test_handler():
    """Test the handler locally."""
    
    # Import the handler
    try:
        from rp_handler import handler
        print("✓ Handler imported successfully")
    except Exception as e:
        print(f"✗ Failed to import handler: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Test 1: Health check (should work immediately)
    print("\n=== Test 1: Health Check ===")
    test_input = {
        "input": {
            "health_check": True
        }
    }
    
    try:
        result = handler(test_input)
        print(f"Result: {json.dumps(result, indent=2)}")
        assert result["status"] == "healthy", f"Expected healthy, got {result['status']}"
        print("✓ Health check passed")
    except Exception as e:
        print(f"✗ Health check failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Test 2: Test mode (lightweight, no model loading)
    print("\n=== Test 2: Test Mode ===")
    test_input = {
        "input": {
            "test_mode": True
        }
    }
    
    try:
        result = handler(test_input)
        print(f"Status: {result.get('status')}")
        print(f"Message: {result.get('message')}")
        
        if result.get("status") == "success":
            print("✓ Test mode passed")
        else:
            print(f"✗ Test mode returned: {result}")
            return False
    except Exception as e:
        print(f"✗ Test mode failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Test 3: Error handling
    print("\n=== Test 3: Error Handling ===")
    test_input = {
        "input": {
            "invalid_param": True
        }
    }
    
    try:
        result = handler(test_input)
        print(f"Result: {json.dumps(result, indent=2)}")
        # Should handle gracefully
        if "error" in result or result.get("status") == "error":
            print("✓ Error handled gracefully")
        else:
            print("⚠️ Unexpected result for invalid input")
    except Exception as e:
        print(f"⚠️ Exception on invalid input: {e}")
    
    return True

def test_with_runpod_local():
    """Test using RunPod's local testing method."""
    print("\n=== Testing with RunPod Local Mode ===")
    
    # Set up local testing as per RunPod docs
    os.environ["RUNPOD_DEBUG_LEVEL"] = "DEBUG"
    os.environ["RUNPOD_WEBHOOK_URL"] = "http://localhost:8000/webhook"
    
    # Import handler module
    import rp_handler
    
    # Create a test job
    test_job = {
        "id": "test-job-001",
        "input": {
            "test_mode": True
        }
    }
    
    print(f"Testing with job: {json.dumps(test_job, indent=2)}")
    
    # Run the handler directly
    try:
        # RunPod's local testing approach
        result = runpod.serverless.local_test(
            handler=rp_handler.handler,
            test_input=test_job
        )
        print(f"Result: {json.dumps(result, indent=2)}")
        return True
    except AttributeError:
        # Fallback if local_test doesn't exist
        print("RunPod local_test not available, using direct call")
        result = rp_handler.handler(test_job)
        print(f"Result: {json.dumps(result, indent=2)}")
        return True
    except Exception as e:
        print(f"✗ Local test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("=== RunPod Handler Local Testing ===")
    print("Following: https://docs.runpod.io/serverless/development/local-testing")
    print()
    
    # Run basic tests
    if test_handler():
        print("\n✅ Basic tests passed")
    else:
        print("\n❌ Basic tests failed")
        sys.exit(1)
    
    # Try RunPod's local testing method
    if "--runpod" in sys.argv:
        if test_with_runpod_local():
            print("\n✅ RunPod local test passed")
        else:
            print("\n❌ RunPod local test failed")
            sys.exit(1)