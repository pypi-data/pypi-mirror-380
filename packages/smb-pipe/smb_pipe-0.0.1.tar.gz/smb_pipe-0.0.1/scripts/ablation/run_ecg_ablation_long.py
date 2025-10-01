#!/usr/bin/env python3
"""
Long-run ECG ablation with a fixed sample count per pass, using the exact same
sampled rows for both runs to enable paired comparison.

This script runs two passes with the provided samples-per-pass:
  1) With ECG (multimodal)
  2) Text-only

Prints accuracies and per-sample class changes at the end.

Usage:
  uv run python scripts/ablation/run_ecg_ablation_long.py \
    --csv data/csv/lvef_with_local_paths.csv \
    --samples-per-pass 1200 \
    --language-model standardmodelbio/Qwen3-WM-0.6B \
    --ecg-encoder PKUDigitalHealth/ECGFounder \
    --quiet

Notes:
  - Actual runtime varies with hardware and cache state.
  - Warm-up defaults to 20 samples; adjust with --warmup-samples if needed.
  - You can cap with --max-samples to avoid running the entire dataset.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
import time
from pathlib import Path
import subprocess
from datetime import datetime


def parse_args():
    p = argparse.ArgumentParser(description="Long-run ECG ablation (duration-targeted)")
    p.add_argument("--csv", required=True, help="CSV with ground truth and file paths")
    p.add_argument("--language-model", default="standardmodelbio/Qwen3-WM-0.6B")
    p.add_argument("--ecg-encoder", default="PKUDigitalHealth/ECGFounder")
    p.add_argument("--samples-per-pass", type=int, required=True, help="Fixed number of samples per pass for both runs")
    p.add_argument("--max-samples", type=int, default=None, help="Optional cap on samples per pass (applies to both modes)")
    p.add_argument("--random-sample", action="store_true", help="Sample rows randomly instead of using the head")
    p.add_argument("--seed", type=int, default=42, help="Random seed for sampling when --random-sample is set")
    p.add_argument("--out-prefix", default="outputs/ablation8h", help="Output prefix for JSONL files")
    p.add_argument("--quiet", action="store_true", help="Minimize console output of child runs")
    p.add_argument("--log-file", default=None, help="Optional log file passed to batch_inference")
    return p.parse_args()


def _count_rows(csv_path: Path) -> int:
    n = 0
    with csv_path.open("r", encoding="utf-8") as f:
        r = csv.reader(f)
        header = next(r, None)
        for _ in r:
            n += 1
    return n


def _run_batch(project_root: Path, csv_path: Path, out_path: Path, max_samples: int,
               language_model: str, ecg_encoder: str | None, quiet: bool, log_file: str | None) -> float:
    cmd = [
        sys.executable,
        str(project_root / "src/batch_inference.py"),
        "--csv", str(csv_path),
        "--out", str(out_path),
        "--max-samples", str(max_samples),
        "--language-model", language_model,
    ]
    if ecg_encoder:
        cmd += ["--ecg-encoder", ecg_encoder]
    if quiet:
        cmd += ["--quiet"]
    if log_file:
        cmd += ["--log-file", log_file]

    t0 = time.time()
    res = subprocess.run(cmd, cwd=str(project_root), capture_output=True, text=True)
    dt = time.time() - t0
    if res.returncode != 0:
        raise RuntimeError(f"Batch run failed ({'with_ecg' if ecg_encoder else 'text_only'}):\nSTDOUT:\n{res.stdout}\nSTDERR:\n{res.stderr}")
    return dt


def _load_preds(jsonl_path: Path) -> dict[int, dict]:
    rows: dict[int, dict] = {}
    for line in jsonl_path.read_text().splitlines():
        if not line.strip():
            continue
        obj = json.loads(line)
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


def _load_truths(csv_path: Path, limit: int) -> list[int]:
    out: list[int] = []
    with csv_path.open("r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for i, row in enumerate(r):
            if i >= limit:
                break
            v = row.get("class")
            if v is not None and v != "":
                try:
                    out.append(int(v))
                except Exception:
                    pass
    return out


def _accuracy(preds: list[int], truth: list[int]) -> float | None:
    n = min(len(preds), len(truth))
    if n == 0:
        return None
    return sum(1 for a, b in zip(preds[:n], truth[:n]) if a == b) / n


def _write_fixed_csv(src_csv: Path, dst_csv: Path, n: int, random_sample: bool, seed: int) -> int:
    import pandas as pd
    df = pd.read_csv(src_csv)
    # Keep rows with available local_dat_path or ecg_file to avoid skips
    mask = None
    if 'local_dat_path' in df.columns:
        colmask = df['local_dat_path'].astype(str).str.len().gt(0) & df['local_dat_path'].notna()
        mask = colmask if mask is None else (mask | colmask)
    if 'ecg_file' in df.columns:
        colmask = df['ecg_file'].astype(str).str.len().gt(0) & df['ecg_file'].notna()
        mask = colmask if mask is None else (mask | colmask)
    keep = df[mask] if mask is not None else df
    if random_sample:
        keep = keep.sample(n=min(n, len(keep)), random_state=seed)
    else:
        keep = keep.head(n)
    keep.to_csv(dst_csv, index=False)
    return len(keep)


def main():
    args = parse_args()
    project_root = Path(__file__).resolve().parent.parent.parent
    csv_path = project_root / args.csv
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    # Determine dataset size
    total_rows = _count_rows(csv_path)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    cap = args.max_samples if args.max_samples else total_rows
    samples_per_pass = max(1, min(cap, int(args.samples_per_pass)))
    print(f"Samples per pass (requested): {samples_per_pass} (cap {cap}, dataset {total_rows})")

    # Materialize a fixed CSV with exactly the rows to evaluate
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fixed_csv = project_root / f"{args.out_prefix}_fixed_rows_{ts}.csv"
    selected = _write_fixed_csv(csv_path, fixed_csv, samples_per_pass, args.random_sample, args.seed)
    print(f"Fixed CSV written: {fixed_csv.name} with {selected} rows")

    # Run with ECG
    out_with = project_root / f"{args.out_prefix}_with_ecg_{ts}.jsonl"
    dt_with = _run_batch(
        project_root, fixed_csv, out_with, selected,
        args.language_model, args.ecg_encoder, args.quiet, args.log_file,
    )

    # Run text-only
    out_text = project_root / f"{args.out_prefix}_text_only_{ts}.jsonl"
    dt_text = _run_batch(
        project_root, fixed_csv, out_text, selected,
        args.language_model, None, args.quiet, args.log_file,
    )

    # Load predictions and truths for the evaluated subset
    preds_with = _load_preds(out_with)
    preds_text = _load_preds(out_text)
    truths = _load_truths(fixed_csv, limit=selected)

    # Align by row index present in both outputs
    keys = sorted(set(preds_with.keys()) & set(preds_text.keys()))
    classes_with = [int(preds_with[k]["class"]) for k in keys if preds_with[k]["class"] is not None]
    classes_text = [int(preds_text[k]["class"]) for k in keys if preds_text[k]["class"] is not None]
    truths_aligned = truths[:len(keys)]

    acc_with = _accuracy(classes_with, truths_aligned)
    acc_text = _accuracy(classes_text, truths_aligned)
    class_changes = sum(1 for k in keys if preds_with[k]["class"] != preds_text[k]["class"]) if keys else 0

    # Probability deltas to detect subtle differences
    def _safe(v):
        try:
            return float(v) if v is not None else 0.0
        except Exception:
            return 0.0
    avg_delta_normal = sum(abs(_safe(preds_with[k]["normal_prob"]) - _safe(preds_text[k]["normal_prob"])) for k in keys) / (len(keys) or 1)
    avg_delta_immediate = sum(abs(_safe(preds_with[k]["immediate"]) - _safe(preds_text[k]["immediate"])) for k in keys) / (len(keys) or 1)

    # Sanity: confirm ecg_used True/False in respective runs if present
    ecg_used_with = any(preds_with[k].get("ecg_used", False) for k in keys)
    ecg_used_text = any(preds_text[k].get("ecg_used", False) for k in keys)

    total_dt = dt_with + dt_text
    print("\nAblation (long-run) summary (paired rows):")
    print("  warmup: skipped (fixed samples mode)")
    print(f"  per_pass_samples: {selected}")
    print(f"  with_ecg_time: {dt_with/3600:.2f} h  text_only_time: {dt_text/3600:.2f} h  total: {total_dt/3600:.2f} h")
    print(f"  with_ecg_acc: {acc_with}")
    print(f"  text_only_acc: {acc_text}")
    print(f"  class_changes: {class_changes} / {len(keys)}")
    print(f"  avg_delta_normal_prob: {avg_delta_normal:.6f}  avg_delta_immediate: {avg_delta_immediate:.6f}")
    print(f"  ecg_used(with_ecg): {ecg_used_with}  ecg_used(text_only): {ecg_used_text}")
    print(f"  outputs: {out_with.name}, {out_text.name}")


if __name__ == "__main__":
    main()


