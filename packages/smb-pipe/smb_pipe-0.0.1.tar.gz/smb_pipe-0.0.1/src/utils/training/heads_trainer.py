"""
Lightweight trainer for small prediction heads on cached embeddings.

Supports tasks: binary, multiclass, regression (Cox PH stub).

Usage (as module):
    from utils.training.heads_trainer import train_head_from_cache
    result = train_head_from_cache(...)

CLI usage:
    uv run python -m utils.training.heads_trainer --help
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import List, Tuple, Optional, Dict, Any

import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Train a small prediction head on cached embeddings")
    p.add_argument("--cache-dir", required=True, help="Embeddings cache directory with .pt files and manifest.json")
    p.add_argument("--labels-csv", required=True, help="CSV with columns: row_id, label (or label_* for multi)")
    p.add_argument("--task", required=True, choices=["binary", "multiclass", "regression", "survival_cox"]) 
    p.add_argument("--label-col", default="label")
    p.add_argument("--hidden", type=int, nargs="*", default=[256])
    p.add_argument("--dropout", type=float, default=0.1)
    p.add_argument("--batch-size", type=int, default=64)
    p.add_argument("--max-epochs", type=int, default=50)
    p.add_argument("--lr", type=float, default=1e-3)
    p.add_argument("--export-dir", required=True)
    # Tracking removed; integrate your own tracker externally if desired.
    return p.parse_args()


def _make_head(task: str, input_dim: int, hidden: List[int], dropout: float, num_classes: Optional[int] = None) -> Tuple[nn.Module, nn.Module, callable]:
    layers: List[nn.Module] = []
    in_dim = input_dim
    for h in hidden:
        layers += [nn.Linear(in_dim, h), nn.ReLU(), nn.Dropout(dropout)]
        in_dim = h

    if task == "binary":
        # Use 2 logits + CrossEntropy to be compatible with pipeline LVEF head
        layers += [nn.Linear(in_dim, 2)]
        head = nn.Sequential(*layers)
        loss = nn.CrossEntropyLoss()
        metric = lambda yhat, y: float(((yhat.argmax(dim=1) == y).float().mean()).item())
        return head, loss, metric

    if task == "multiclass":
        if not num_classes or num_classes < 2:
            raise ValueError("num_classes must be >=2 for multiclass")
        layers += [nn.Linear(in_dim, num_classes)]
        head = nn.Sequential(*layers)
        loss = nn.CrossEntropyLoss()
        metric = lambda yhat, y: float(((yhat.argmax(dim=1) == y).float().mean()).item())
        return head, loss, metric

    if task == "regression":
        layers += [nn.Linear(in_dim, 1)]
        head = nn.Sequential(*layers)
        loss = nn.MSELoss()
        metric = lambda yhat, y: float((yhat - y).abs().mean().item())
        return head, loss, metric

    if task == "survival_cox":
        raise NotImplementedError("Wire Cox-PH head here using pycox/torchtuples if desired.")

    raise ValueError(task)


def _load_cache(cache_dir: Path, labels_csv: Path, label_col: str, task: str) -> Tuple[torch.Tensor, torch.Tensor, Optional[int]]:
    import pandas as pd

    lbl = pd.read_csv(labels_csv)
    if "row_id" not in lbl.columns:
        raise ValueError("labels CSV must contain a 'row_id' column matching cache file names")
    if label_col not in lbl.columns:
        raise ValueError(f"labels CSV missing label column '{label_col}'")

    Xs: List[torch.Tensor] = []
    ys: List[Any] = []
    for row_id, y in zip(lbl["row_id"], lbl[label_col]):
        file_path = cache_dir / f"{row_id}.pt"
        if not file_path.exists():
            continue
        fused = torch.load(file_path, map_location="cpu")
        if fused.ndim > 1:
            fused = fused.view(-1)
        Xs.append(fused)
        ys.append(y)

    if not Xs:
        raise FileNotFoundError("No embeddings loaded from cache. Check row_id alignment with cache.")

    X = torch.stack(Xs)

    if task == "multiclass":
        import numpy as np
        classes = sorted(set(int(v) for v in ys))
        class_to_idx = {c: i for i, c in enumerate(classes)}
        y_tensor = torch.tensor([class_to_idx[int(v)] for v in ys], dtype=torch.long)
        num_classes = len(classes)
        return X, y_tensor, num_classes

    if task == "binary":
        # Expect labels as {0,1}; map to long class indices
        y_tensor = torch.tensor([int(v) for v in ys], dtype=torch.long)
        return X, y_tensor, 2

    if task == "regression":
        y_tensor = torch.tensor([float(v) for v in ys], dtype=torch.float32).view(-1, 1)
        return X, y_tensor, None

    # survival_cox not implemented
    raise NotImplementedError


def train_head_from_cache(
    cache_dir: str,
    labels_csv: str,
    task: str,
    label_col: str = "label",
    hidden: Optional[List[int]] = None,
    dropout: float = 0.1,
    batch_size: int = 64,
    max_epochs: int = 50,
    lr: float = 1e-3,
    export_dir: Optional[str] = None,
    # Tracking removed
) -> Dict[str, Any]:
    hidden = hidden or [256]
    cache_path = Path(cache_dir)
    export_path = Path(export_dir) if export_dir else (cache_path / "trained_head")
    export_path.mkdir(parents=True, exist_ok=True)

    manifest_path = cache_path / "manifest.json"
    if not manifest_path.exists():
        raise FileNotFoundError(f"manifest.json not found in {cache_path}")
    manifest = json.loads(manifest_path.read_text())

    sample_id = manifest["files"][0]["row_id"]
    sample_vec = torch.load(cache_path / f"{sample_id}.pt", map_location="cpu")
    input_dim = int(sample_vec.view(-1).numel())

    X, y, maybe_n_classes = _load_cache(cache_path, Path(labels_csv), label_col, task)
    head, loss_fn, metric = _make_head(task, input_dim, hidden, dropout, num_classes=maybe_n_classes)

    optimizer = torch.optim.AdamW([p for p in head.parameters() if p.requires_grad], lr=lr)
    trainset = TensorDataset(X, y)
    loader = DataLoader(trainset, batch_size=batch_size, shuffle=True)

    wb_run = None

    head.train()
    total_steps = 0
    for epoch in range(1, max_epochs + 1):
        total_loss = 0.0
        total_metric = 0.0
        n_obs = 0
        for xb, yb in loader:
            optimizer.zero_grad()
            out = head(xb)
            loss_val = loss_fn(out, yb)
            loss_val.backward()
            optimizer.step()
            total_steps += 1

            bs = xb.size(0)
            total_loss += float(loss_val.item()) * bs
            total_metric += metric(out.detach(), yb)
            n_obs += bs

        avg_loss = total_loss / max(1, n_obs)
        avg_metric = total_metric / max(1, len(loader))
        # Hook: external tracking can log metrics here.

    # Export
    weights_path = export_path / "weights.pt"
    torch.save(head.state_dict(), weights_path)

    cfg = {
        "task": task,
        "input_dim": input_dim,
        "hidden": hidden,
        "dropout": dropout,
        "optimizer": "AdamW",
        "lr": lr,
        "batch_size": batch_size,
        "max_epochs": max_epochs,
        "upstream": {
            "encoders": manifest.get("encoders"),
            "language_model": manifest.get("language_model"),
            "modalities": manifest.get("modalities"),
        },
    }
    (export_path / "head_config.json").write_text(json.dumps(cfg, indent=2))

    # Hook: external tracking can finalize here.

    return {
        "weights_path": str(weights_path),
        "config_path": str(export_path / "head_config.json"),
        "num_samples": len(trainset),
        "input_dim": input_dim,
    }


def main() -> None:
    args = _parse_args()
    train_head_from_cache(
        cache_dir=args.cache_dir,
        labels_csv=args.labels_csv,
        task=args.task,
        label_col=args.label_col,
        hidden=args.hidden,
        dropout=args.dropout,
        batch_size=args.batch_size,
        max_epochs=args.max_epochs,
        lr=args.lr,
        export_dir=args.export_dir,
        
    )


if __name__ == "__main__":
    main()


