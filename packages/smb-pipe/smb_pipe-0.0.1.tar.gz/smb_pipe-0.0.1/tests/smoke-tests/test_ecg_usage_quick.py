#!/usr/bin/env python3
"""
Quick, fool-proof ECG usage check (paired rows + permutation control).

Runs three passes on the same fixed subset of rows (default 40):
  1) Text-only (no ECG)
  2) With ECG (correct pairing)
  3) With ECG but ECG paths permuted across rows (mismatch)

Evidence of ECG usage:
  - class_changes between (2) and (3) > 0, or
  - average probability deltas between (2) and (3) > tiny epsilon

Run (opt-in heavy test):
  uv run pytest -q -s -m hf_integration tests/test_ecg_usage_quick.py
"""
from __future__ import annotations

import os
import sys
import csv
import json
import subprocess
from pathlib import Path
import pytest


pytestmark = pytest.mark.hf_integration


# Keep this test fast by default; override via ECG_ABLATION_SAMPLES
SAMPLES = int(os.environ.get("ECG_ABLATION_SAMPLES", 10))


def _write_fixed_csv(src_csv: Path, dst_csv: Path, n: int, seed: int = 42) -> int:
    import pandas as pd
    import os
    df = pd.read_csv(src_csv)
    # Keep rows with available local_dat_path or ecg_file to avoid skips
    mask = None
    if 'local_dat_path' in df.columns:
        exists_mask = df['local_dat_path'].apply(lambda p: isinstance(p, str) and len(p) > 0 and os.path.exists(p))
        colmask = exists_mask & df['local_dat_path'].notna()
        mask = colmask if mask is None else (mask | colmask)
    if 'ecg_file' in df.columns:
        # If only ecg_file is present, we cannot verify existence reliably here without a base dir; keep non-empty
        colmask = df['ecg_file'].astype(str).str.len().gt(0) & df['ecg_file'].notna()
        mask = colmask if mask is None else (mask | colmask)
    keep = df[mask] if mask is not None else df
    keep = keep.sample(n=min(n, len(keep)), random_state=seed)
    keep.to_csv(dst_csv, index=False)
    return len(keep)


def _permute_ecg(src_csv: Path, dst_csv: Path, seed: int = 123) -> None:
    import pandas as pd
    df = pd.read_csv(src_csv)
    if 'local_dat_path' in df.columns and df['local_dat_path'].notna().any():
        col = 'local_dat_path'
    elif 'ecg_file' in df.columns and df['ecg_file'].notna().any():
        col = 'ecg_file'
    else:
        raise RuntimeError("CSV has no ECG path column to permute")
    df[col] = df[col].sample(frac=1, random_state=seed).reset_index(drop=True)
    df.to_csv(dst_csv, index=False)


def _run_batch(project_root: Path, csv_path: Path, out_path: Path, ecg_encoder: str | None) -> None:
    cmd = [
        sys.executable,
        str(project_root / "src/batch_inference.py"),
        "--csv", str(csv_path),
        "--out", str(out_path),
        "--max-samples", str(SAMPLES),
        "--language-model", "standardmodelbio/Qwen3-WM-0.6B",
        "--quiet",
    ]
    if ecg_encoder:
        cmd += ["--ecg-encoder", ecg_encoder]
    r = subprocess.run(cmd, cwd=str(project_root), capture_output=True, text=True)
    assert r.returncode == 0, f"batch_inference failed: {r.stderr or r.stdout}"


def _load_preds(jsonl_path: Path) -> dict[int, dict]:
    rows: dict[int, dict] = {}
    for line in jsonl_path.read_text().splitlines():
        if not line.strip():
            continue
        obj = json.loads(line)
        if obj.get("status") and obj.get("status") != "success":
            continue
        row_idx = obj.get("row")
        pred = obj.get("predictions", {})
        lvef = pred.get("lvef_classification", {})
        risk = pred.get("cardiotoxicity_risk", {})
        md = obj.get("metadata", {})
        if row_idx is None:
            continue
        rows[int(row_idx)] = {
            "class": lvef.get("class"),
            "normal_prob": lvef.get("normal_prob"),
            "dysfunction_prob": lvef.get("dysfunction_prob"),
            "immediate": risk.get("immediate"),
            "ecg_used": md.get("ecg_used", False),
        }
    return rows


def test_ecg_usage_quick(tmp_path: Path):
    # Resolve repository root (tests/<subdir>/ -> tests -> repo root).
    project_root = Path(__file__).resolve().parents[2]
    csv_path = project_root / "data/csv/lvef_with_local_paths.csv"
    if not csv_path.exists():
        pytest.skip(f"Missing CSV: {csv_path}")

    fixed_csv = tmp_path / "fixed_rows.csv"
    selected = _write_fixed_csv(csv_path, fixed_csv, SAMPLES)
    assert selected > 0

    # Paths
    out_text = tmp_path / "text_only.jsonl"
    out_with = tmp_path / "with_ecg.jsonl"
    out_perm = tmp_path / "with_ecg_permuted.jsonl"

    # Text-only and with ECG (paired rows)
    _run_batch(project_root, fixed_csv, out_text, ecg_encoder=None)
    _run_batch(project_root, fixed_csv, out_with, ecg_encoder="PKUDigitalHealth/ECGFounder")

    # Permute ECG column and run again with ECG
    perm_csv = tmp_path / "fixed_rows_permuted.csv"
    _permute_ecg(fixed_csv, perm_csv)
    _run_batch(project_root, perm_csv, out_perm, ecg_encoder="PKUDigitalHealth/ECGFounder")

    # Load predictions
    P_text = _load_preds(out_text)
    P_with = _load_preds(out_with)
    P_perm = _load_preds(out_perm)

    # Sanity: ecg_used flags
    assert any(P_with[k].get("ecg_used", False) for k in P_with), "ecg_used should be True in ECG run"
    assert not any(P_text[k].get("ecg_used", False) for k in P_text), "ecg_used should be False in text-only run"

    # Pair keys
    keys = sorted(set(P_with.keys()) & set(P_text.keys()) & set(P_perm.keys()))
    assert len(keys) > 0

    # Compute class changes and probability deltas
    class_changes_with_vs_perm = sum(1 for k in keys if P_with[k]["class"] != P_perm[k]["class"])

    def _safe(v):
        try:
            return float(v) if v is not None else 0.0
        except Exception:
            return 0.0

    avg_delta_normal = sum(abs(_safe(P_with[k]["normal_prob"]) - _safe(P_perm[k]["normal_prob"])) for k in keys) / len(keys)
    avg_delta_immediate = sum(abs(_safe(P_with[k]["immediate"]) - _safe(P_perm[k]["immediate"])) for k in keys) / len(keys)

    print(f"class_changes_with_vs_perm: {class_changes_with_vs_perm} / {len(keys)}")
    print(f"avg_delta_normal_prob (with vs perm): {avg_delta_normal:.6f}")
    print(f"avg_delta_immediate (with vs perm): {avg_delta_immediate:.6f}")

    # Proof criteria: either class changes or non-trivial probability shift
    assert class_changes_with_vs_perm > 0 or (avg_delta_normal > 1e-6 or avg_delta_immediate > 1e-3)


