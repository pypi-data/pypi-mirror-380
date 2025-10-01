# Data Preparation Guide

This guide covers downloading and preparing MIMIC-IV ECG data for model training and validation.

## Prerequisites

### AWS Credentials

Export AWS credentials with S3 access:

```bash
# Option 1: Set environment variables (recommended)
export AWS_ACCESS_KEY_ID="YOUR_ACCESS_KEY"
export AWS_SECRET_ACCESS_KEY="YOUR_SECRET_KEY"
export AWS_SESSION_TOKEN="YOUR_SESSION_TOKEN"  # if using SSO/temporary credentials
export AWS_DEFAULT_REGION="us-east-2"

# Option 2: Use AWS CLI profile
aws configure sso
# SSO start URL: https://standardmodelbio.awsapps.com/start/#
# SSO Region: us-east-2
```

### Required Files

Ensure LVEF ground truth data exists:
```bash
ls -la data/ground_truth/LVEF.csv  # Should be ~4.2MB with 75,412 records
```

## Download Commands

### Test Download (10 files)
```bash
cd /workspace/runpod-mm-cardiotox-inference
./scripts/data/mimic_to_s3.sh test
```

### LVEF Subset (75,412 files, ~17GB)
```bash
cd /workspace/runpod-mm-cardiotox-inference
nohup ./scripts/data/mimic_to_s3.sh lvef > /workspace/logs/lvef_background.log 2>&1 &
```

### Full Dataset (800k+ files, ~2.5TB)
```bash
cd /workspace/runpod-mm-cardiotox-inference
./scripts/data/mimic_to_s3.sh full  # Interactive confirmation required
```

## Monitoring Progress

### 🔄 **Live Progress Feed**
```bash
tail -f /workspace/logs/mimic_s3_progress.txt
```
Shows uploads in real-time as they happen

### 📈 **Background Job Progress** 
```bash
tail -f /workspace/logs/lvef_background.log
```
Shows CSV processing progress: `Progress: 3000/75412 (19:20:25)`

### 🎯 **Overall Status Dashboard**
```bash
./scripts/monitoring/job_status.sh
# Or for live monitoring:
./scripts/monitoring/job_status.sh --watch
```
Comprehensive status report with running jobs, health status, and progress

### 📊 **Quick Status Checks**

**Process Count:**
```bash
ps aux | grep mimic_to_s3 | grep -v grep | wc -l
```
Should show ~10-12 processes if running

**S3 File Count:**
```bash
aws s3 ls s3://smb-dev-us-east-2-data/datasets/mimic-iv-ecg/1.0/waveforms/ --recursive --region us-east-2 | wc -l
```
Current: 94,493 files, Target: 150,824 files (75,412 × 2)

**Recent Uploads:**
```bash
tail -10 /workspace/logs/mimic_s3_progress.txt
```

**Progress Percentage:**
```bash
echo "Progress: $((94493 * 100 / 150824))% complete"
```

### 🔍 **Diagnostic Commands**

**Check for Errors:**
```bash
cat /workspace/logs/mimic_s3_errors.log
```

**AWS Credentials Status:**
```bash
aws sts get-caller-identity
```

### 🛑 **Control Commands**

**Stop Download:**
```bash
pkill -f mimic_to_s3.sh
```

**Restart Download:**
```bash
# First export credentials, then:
cd /workspace/runpod-mm-cardiotox-inference
nohup ./scripts/mimic_to_s3.sh lvef > /workspace/logs/lvef_background.log 2>&1 &
```

## Troubleshooting

### Common Issues

**AWS Access Denied**
- Verify credentials are exported in current shell
- Test with: `aws sts get-caller-identity`
- Ensure user has S3 permissions for `s3://smb-dev-us-east-2-data/`

**Job Stops Immediately**
- Check for bash syntax errors in script
- Run in foreground first: `./scripts/mimic_to_s3.sh test`
- Check error log: `cat /workspace/logs/mimic_s3_errors.log`

**No Progress Logged**
- Verify log files are being written: `ls -la /workspace/logs/`
- Check if process is running: `ps aux | grep mimic_to_s3`

### Performance Expectations

- **LVEF subset**: ~63 hours at 20 files/minute
- **Network intensive**: Each file requires download from PhysioNet + upload to S3
- **Parallel processing**: 10 concurrent uploads by default
- **Resume capability**: Script skips files already in S3

## Local Data Management

### Create Local Manifest
```bash
# Generate CSV mapping ground truth to local file paths
uv run scripts/data/create_local_manifest.py

# Output: data/csv/lvef_with_local_paths.csv
# Contains: subject_id, waveform_path, LVEF, class, local_dat_path, local_hea_path
# Rerun after downloading more files to update paths
```

## File Structure

```
Target S3: s3://smb-dev-us-east-2-data/datasets/mimic-iv-ecg/1.0/waveforms/
Local: /workspace/physionet.org/files/mimic-iv-ecg/1.0/files/
├── files/
│   └── p1000/
│       └── p10000826/
│           └── s40695233/
│               ├── 40695233.dat  # Waveform data
│               └── 40695233.hea  # Header file
```

Each ECG recording consists of two files (.dat + .hea) that must be uploaded together.
