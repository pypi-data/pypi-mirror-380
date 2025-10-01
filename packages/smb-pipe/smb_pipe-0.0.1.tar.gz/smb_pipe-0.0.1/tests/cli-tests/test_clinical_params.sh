#!/bin/bash

# Test serverless inference with comprehensive clinical parameters

uv run src/serverless_inference.py \
  --demo \
  --age 65 \
  --gender female \
  --bmi 28.5 \
  --diagnosis "Breast Cancer" \
  --cancer-type breast \
  --cancer-stage IIIA \
  --treatment doxorubicin \
  --chemotherapy-agent doxorubicin \
  --chemotherapy-dose "240 mg/m2 cumulative" \
  --cycles-completed 4 \
  --radiotherapy-dose "45 Gy to left chest wall" \
  --baseline-lvef "58" \
  --current-lvef "52" \
  --baseline-troponin "0.02 ng/mL" \
  --current-troponin "0.08 ng/mL" \
  --hypertension \
  --diabetes \
  --smoking-history never \
  --family-history-cad