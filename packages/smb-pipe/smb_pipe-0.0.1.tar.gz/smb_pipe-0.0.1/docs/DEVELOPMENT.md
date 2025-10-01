# Development Guide

## Project Structure

```
runpod-mm-cardiotox-inference/
├── src/
│   ├── inference_pipeline.py      # Main inference orchestrator
│   ├── batch_inference.py         # Batch processing
│   ├── validate_with_metrics.py   # Validation with metrics
│   ├── serverless_inference.py    # RunPod client
│   ├── rp_handler.py             # RunPod handler
│   ├── utils/
│   │   ├── model_manager.py      # Model loading/validation
│   │   ├── ecg_processing.py     # ECG data loading
│   │   ├── text_processor.py     # Text processing
│   │   ├── results_formatter.py  # Output formatting
│   │   └── (logging removed)     # Bring-your-own tracking
│   └── models/
│       └── prediction_heads.py   # Task-specific heads
├── scripts/
│   ├── mimic_to_s3.sh            # MIMIC data download to S3
│   ├── monitor_s3_upload.sh      # Download progress monitoring
│   ├── pull_from_s3.sh           # Download from S3 to local
│   ├── prepare_validation_data.py # Validation prep
│   └── summarize_validation.py   # Results summary
├── data/
│   ├── csv/                      # Input CSV files
│   └── ground_truth/             # Ground truth data
├── outputs/                       # Results and logs
└── docs/                         # Documentation
```

## Setting Up Development

### 1. Clone Repository

```bash
git clone https://github.com/your-org/runpod-mm-cardiotox-inference.git
cd runpod-mm-cardiotox-inference
```

### 2. Install Dependencies

```bash
# Using uv (recommended)
uv sync

# Or with pip
pip install -r requirements.txt
```

### 3. Set Environment Variables

```bash
# Create .env file
cat > .env << EOF
HF_TOKEN=hf_your_token
RUNPOD_API_KEY=your_key
EOF

# Load in shell
source .env
```

### 4. Download Test Data

```bash
# Download MIMIC-IV ECG samples
./scripts/mimic_to_s3.sh test  # See docs/DATA.md for full guide

# Download ground truth
wget -P data/ground_truth/ \
  https://raw.githubusercontent.com/PKUDigitalHealth/ECGFounder/main/csv/LVEF.csv
```

## Testing

### Unit Tests

```bash
# Run all tests
pytest tests/

# Run specific test
pytest tests/test_inference_pipeline.py

# With coverage
pytest --cov=src tests/
```

### Integration Tests

```bash
# Test local inference
./tests/test_local_inference.sh

# Test API server
./tests/test_local_api.sh

# Test RunPod handler
uv run src/rp_handler.py --test_input '{"input": {"demo_mode": true}}'
```

### Validation Tests

```bash
# Quick validation (2 samples)
uv run src/validate_with_metrics.py \
  --csv data/csv/lvef_test_small.csv \
  --max-samples 2

# Check results
uv run python scripts/summarize_validation.py outputs/validation_test.json
```

## Code Style

### Formatting

```bash
# Format with black
black src/ tests/

# Sort imports
isort src/ tests/

# Type checking
mypy src/
```

### Linting

```bash
# Lint with ruff
ruff check src/

# Fix issues
ruff check --fix src/
```

## Adding New Features

### 1. New Model Support

Edit `src/utils/model_manager.py`:

```python
def _detect_model_type(self, model_name: str) -> str:
    """Detect model capabilities"""
    if "your-model" in model_name.lower():
        return "your_type"
    # ...
```

### 2. New Data Format

Edit `src/utils/ecg_processing.py`:

```python
@staticmethod
def load_ecg_file(file_path: str) -> np.ndarray:
    if file_path.endswith('.your_format'):
        return YourLoader.load(file_path)
    # ...
```

### 3. New Metrics

Edit `src/validate_with_metrics.py`:

```python
def calculate_metrics(y_true, y_pred):
    metrics['your_metric'] = your_calculation(y_true, y_pred)
    # ...
```

## Debugging

### Enable Debug Logging

```bash
# Set log level
export LOGURU_LEVEL=DEBUG

# Or in Python
from loguru import logger
logger.add(sys.stderr, level="DEBUG")
```

### Common Issues

1. **Model loading fails**
   ```python
   # Check model exists
   from huggingface_hub import model_info
   info = model_info("model-name")
   print(info)
   ```

2. **ECG loading errors**
   ```python
   # Test ECG loading
   from utils.ecg_processing import ECGDataLoader
   loader = ECGDataLoader()
   data = loader.load_ecg_file("path/to/ecg.mat")
   print(data.shape)
   ```

3. **Memory issues**
   ```bash
   # Monitor GPU memory
   nvidia-smi -l 1
   
   # Clear cache
   import torch
   torch.cuda.empty_cache()
   ```

## Performance Optimization

### Model Optimization

```python
# Use half precision
model = model.half()

# Compile model (PyTorch 2.0+)
model = torch.compile(model)

# Quantization
from torch.quantization import quantize_dynamic
model = quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
```

### Batch Processing

```python
# Process in batches
batch_size = 8
for i in range(0, len(data), batch_size):
    batch = data[i:i+batch_size]
    predictions = model(batch)
```

### Caching

```python
# Cache model outputs
from functools import lru_cache

@lru_cache(maxsize=128)
def get_embeddings(ecg_path):
    return encoder(load_ecg(ecg_path))
```

## Contributing

### 1. Fork Repository

```bash
# Fork on GitHub, then clone
git clone https://github.com/your-username/runpod-mm-cardiotox-inference.git
```

### 2. Create Branch

```bash
git checkout -b feature/your-feature
```

### 3. Make Changes

```bash
# Edit files
# Run tests
pytest tests/
# Format code
black src/
```

### 4. Submit PR

```bash
git add -A
git commit -m "Add your feature"
git push origin feature/your-feature
# Create PR on GitHub
```

## Release Process

### 1. Update Version

```python
# src/__init__.py
__version__ = "1.2.0"
```

### 2. Update Changelog

```markdown
# CHANGELOG.md
## [1.2.0] - 2025-01-15
### Added
- New feature X
### Fixed
- Bug Y
```

### 3. Tag Release

```bash
git tag -a v1.2.0 -m "Release v1.2.0"
git push origin v1.2.0
```

### 4. Build Docker Image

```bash
docker build -t cardiotox:v1.2.0 .
docker push your-registry/cardiotox:v1.2.0
```

## Monitoring

Integrate your preferred experiment tracker (e.g., MLflow, W&B) in wrappers.

### Profiling

```python
# Profile code
import cProfile
cProfile.run('pipeline.predict(data)')

# Memory profiling
from memory_profiler import profile

@profile
def predict(data):
    # ...
```

## Documentation

### Update Docs

```bash
# Generate API docs
pdoc --html --output-dir docs/api src/

# Update README
# Edit README.md with new features
```

### Examples

Always provide examples:

```python
"""
Example:
    >>> from inference_pipeline import MultiModalMedicalInference
    >>> pipeline = MultiModalMedicalInference()
    >>> result = pipeline.predict(ecg_files=["test.mat"])
    >>> print(result['risk_category'])
    'moderate'
"""
```