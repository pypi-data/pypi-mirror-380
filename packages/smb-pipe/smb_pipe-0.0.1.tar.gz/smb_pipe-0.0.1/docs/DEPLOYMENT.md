# Deployment Guide

## Local Testing

### Quick Start (Single Case via Batch Runner)

```bash
# Create a one-row CSV for a single patient
printf "ecg_file,clinical_notes\nexample.mat,Demo case\n" > /tmp/one_case.csv

# Run using the batch runner
uv run src/batch_inference.py \
  --csv /tmp/one_case.csv \
  --ecg-data-dir /workspace/physionet.org/files/mimic-iv-ecg/1.0
```

### Custom Models

```bash
# Multimodal (ECG + Text)
uv run src/batch_inference.py \
  --csv /tmp/one_case.csv \
  --language-model standardmodelbio/Qwen3-WM-0.6B \
  --ecg-encoder PKUDigitalHealth/ECGFounder

# Text-only
uv run src/batch_inference.py \
  --csv /tmp/one_case.csv \
  --language-model standardmodelbio/smb-mntp-llama-3.1-8b \
  --ecg-encoder ""
```

## Docker Deployment

### Build Image

```bash
# Linux/AMD64
docker build -t cardiotox:dev .

# macOS/Apple Silicon (cross-compile)
docker buildx build --platform linux/amd64 -t cardiotox:dev .
```

### Run Container

```bash
# Demo mode
docker run --rm -it cardiotox:dev \
  python -m src.rp_handler --test_input '{"input":{"demo_mode":true}}'

# With GPU (Linux)
docker run --rm -it --gpus all --ipc=host cardiotox:dev \
  python -m src.rp_handler --test_input '{"input":{"demo_mode":true}}'

# API server
docker run --rm -it -p 8000:8000 cardiotox:dev \
  python -m src.rp_handler --rp_serve_api
```

### Mount Local Data

```bash
docker run --rm -it \
  -v /path/to/ecg/data:/workspace/data \
  cardiotox:dev \
  python -m src.rp_handler --test_input '{"input":{
    "ecg_data_source":"local",
    "ecg_files":["/workspace/data/baseline.mat"]
  }}'
```

## RunPod Serverless

### Setup

1. **Build and Push Image**
   ```bash
   # GitHub Actions automatically builds on push to main
   git push origin main
   ```

2. **Create Endpoint**
   - Go to RunPod dashboard
   - Create serverless endpoint
   - Use your Docker image
   - Set environment variables (HF_TOKEN, etc.)

### Submit Jobs

```bash
export RUNPOD_API_KEY=your_key

# Demo mode
curl -X POST https://api.runpod.ai/v2/YOUR_ENDPOINT_ID/run \
  -H "Authorization: Bearer ${RUNPOD_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"input": {"demo_mode": true}}'

# With S3 data
curl -X POST https://api.runpod.ai/v2/YOUR_ENDPOINT_ID/run \
  -H "Authorization: Bearer ${RUNPOD_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
      "ecg_files": ["s3://bucket/ecg1.mat"],
      "clinical_notes": "Patient history...",
      "ecg_data_source": "s3",
      "aws_access_key_id": "AKIA...",
      "aws_secret_access_key": "..."
    }
  }'
```

### Using Python Client

```bash
uv run src/serverless_inference.py \
  --endpoint-id YOUR_ENDPOINT_ID \
  --ecg-files baseline.mat followup.mat \
  --clinical-notes "Patient with HER2+ breast cancer"
```

## API Server

### Start Server

```bash
# Local
uv run src/rp_handler.py --rp_serve_api

# Docker
docker run -d -p 8000:8000 --name cardiotox-api cardiotox:dev \
  python -m src.rp_handler --rp_serve_api
```

### Test Endpoints

```bash
# Health check
curl http://localhost:8000/health

# Sync inference
curl -X POST http://localhost:8000/runsync \
  -H 'Content-Type: application/json' \
  -d '{"input": {"demo_mode": true}}'

# Async inference
curl -X POST http://localhost:8000/run \
  -H 'Content-Type: application/json' \
  -d '{"input": {"demo_mode": true}}'
```

## Batch Processing

### CSV Format

Create CSV with columns:
- `patient_id`: Unique identifier
- `ecg_file` or `baseline_ecg_s3`: Path to ECG file
- `clinical_notes`: Clinical text
- `age`, `gender`, `diagnosis`, etc.: Optional metadata

### Local Batch

```bash
uv run src/batch_inference.py \
  --csv data/csv/patients.csv \
  --out outputs/predictions.jsonl
```

### Serverless Batch

```bash
# Upload CSV to S3
aws s3 cp patients.csv s3://bucket/batch/patients.csv

# Submit batch job
curl -X POST https://api.runpod.ai/v2/YOUR_ENDPOINT_ID/run \
  -H "Authorization: Bearer ${RUNPOD_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
      "csv_file": "s3://bucket/batch/patients.csv",
      "csv_data_source": "s3"
    }
  }'
```

## Environment Variables

### Required
- `HF_TOKEN`: HuggingFace token for private models

### Optional
 
- `AWS_ACCESS_KEY_ID`: S3 access (if using S3)
- `AWS_SECRET_ACCESS_KEY`: S3 secret (if using S3)
- `RUNPOD_API_KEY`: RunPod API access

### Setting Variables

```bash
# .env file (recommended)
cat > .env << EOF
HF_TOKEN=hf_your_token
WANDB_API_KEY=your_wandb_key
EOF

# Export in shell
export HF_TOKEN=hf_your_token

# Docker run
docker run --env-file .env cardiotox:dev ...

# RunPod endpoint
# Set in endpoint configuration UI
```

## Monitoring

### Experiment Tracking

Bring your own tracking (e.g., W&B, MLflow) in your wrapper scripts.

### Logs

- Local: Check console output
- Docker: `docker logs container-name`
- RunPod: View in dashboard or use API

## Troubleshooting

### Common Issues

1. **401 Unauthorized**: Set HF_TOKEN for private models
2. **CUDA out of memory**: Use smaller model or reduce batch size
3. **File not found**: Check ECG file paths and data mounting
4. **Slow inference**: Use GPU or smaller model

### Debug Mode

```bash
# Verbose logging
LOGURU_LEVEL=DEBUG uv run src/batch_inference.py --csv /tmp/one_case.csv
```