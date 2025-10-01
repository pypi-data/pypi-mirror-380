#!/usr/bin/env python3
"""Direct test of handler function without RunPod server."""
import sys
import json
import os
from datetime import datetime

# Add src to path from repository root.
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src'))

# Mock runpod module to avoid server startup
class MockRunPod:
    class serverless:
        @staticmethod
        def start(config):
            print("MockRunPod: Would start server, but skipping for test")

sys.modules['runpod'] = MockRunPod()

# Now import handler
from rp_handler import handler

print("Testing handler with demo mode...")
start = datetime.now()

# Test with demo mode
result = handler({"input": {"demo_mode": True}})

elapsed = (datetime.now() - start).total_seconds()
print(f"\nTest completed in {elapsed:.2f} seconds")

# Print result
if "output" in result:
    output = result["output"]
    if "predictions" in output:
        pred = output["predictions"]
        print("\n=== Predictions ===")
        print(f"Risk Category: {pred.get('risk_category', 'N/A')}")
        if "cardiotoxicity_risk" in pred:
            risk = pred["cardiotoxicity_risk"]
            print(f"Immediate Risk: {risk.get('immediate', 'N/A'):.2%}")
            print(f"3-Month Risk: {risk.get('3_months', 'N/A'):.2%}")
            print(f"6-Month Risk: {risk.get('6_months', 'N/A'):.2%}")
            print(f"12-Month Risk: {risk.get('12_months', 'N/A'):.2%}")
        print(f"\nStatus: {output.get('status', 'N/A')}")
        print(f"Message: {output.get('message', 'N/A')}")
    else:
        print("\nOutput:", json.dumps(output, indent=2))
elif "error" in result:
    print(f"\nError: {result['error']}")
else:
    print("\nFull result:", json.dumps(result, indent=2))