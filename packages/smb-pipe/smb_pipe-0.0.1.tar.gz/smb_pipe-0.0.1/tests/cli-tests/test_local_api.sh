#!/bin/bash
# Test RunPod handler API locally before deployment

echo "🚀 Starting local API server..."
uv run src/rp_handler.py --rp_serve_api &
SERVER_PID=$!

# Wait for server to start
sleep 10

echo "📤 Sending test request..."
RESPONSE=$(curl -s -X POST http://localhost:8000/runsync \
  -H 'Content-Type: application/json' \
  -d '{"input": {"demo_mode": true}}')

# Check if response contains expected fields
if echo "$RESPONSE" | grep -q "cardiotoxicity_risk"; then
    echo "✅ Test passed! Response contains predictions"
    echo "$RESPONSE" | python -m json.tool | head -20
else
    echo "❌ Test failed! Response:"
    echo "$RESPONSE"
fi

# Cleanup
echo "🧹 Stopping server..."
kill $SERVER_PID 2>/dev/null

echo "✨ Test complete"