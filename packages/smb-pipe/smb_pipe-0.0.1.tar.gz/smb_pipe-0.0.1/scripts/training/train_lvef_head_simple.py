#!/usr/bin/env python3
"""Simple LVEF head fine-tuning script.

Usage:
    cd /workspace/runpod-mm-cardiotox-inference
    uv run python scripts/training/train_lvef_head_simple.py \
        --csv data/csv/lvef_with_local_paths.csv \
        --epochs 20 \
        --batch-size 16 \
        --learning-rate 1e-4
"""

import argparse
import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from pathlib import Path
import sys
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


def create_lvef_head(input_dim: int = 1024) -> nn.Module:
    """Create a simple binary LVEF classification head."""
    return nn.Sequential(
        nn.Linear(input_dim, 256),
        nn.ReLU(),
        nn.Dropout(0.1),
        nn.Linear(256, 2)  # Binary: 0=dysfunction, 1=normal
    )


def main():
    parser = argparse.ArgumentParser(description="Train LVEF binary classification head")
    parser.add_argument("--csv", required=True, help="CSV with LVEF ground truth")
    parser.add_argument("--epochs", type=int, default=10, help="Training epochs")
    parser.add_argument("--batch-size", type=int, default=16, help="Batch size")
    parser.add_argument("--learning-rate", type=float, default=1e-4, help="Learning rate")
    parser.add_argument("--input-dim", type=int, default=1024, help="Input embedding dimension (1024 for current model)")
    
    args = parser.parse_args()
    
    # Load data
    print("Loading data...")
    df = pd.read_csv(args.csv)
    df_local = df[df['local_dat_path'].notna() & (df['local_dat_path'] != '')].copy()
    
    print(f"Total records: {len(df)}")
    print(f"Records with local files: {len(df_local)}")
    
    if len(df_local) < 20:
        print("❌ Need at least 20 samples for training")
        return 1
    
    # Check class distribution
    class_counts = df_local['class'].value_counts().sort_index()
    print(f"Class distribution: {dict(class_counts)}")
    
    # For now, create synthetic embeddings for demo
    # In real implementation, you'd extract from the ECG encoder
    print(f"Creating synthetic embeddings for demo (dim={args.input_dim})...")
    X = torch.randn(len(df_local), args.input_dim)  # Synthetic embeddings
    y = torch.tensor(df_local['class'].values, dtype=torch.long)
    
    # Split data
    indices = torch.arange(len(df_local))
    train_idx, test_idx = train_test_split(
        indices, test_size=0.2, random_state=42, 
        stratify=df_local['class']
    )
    
    X_train, X_test = X[train_idx], X[test_idx] 
    y_train, y_test = y[train_idx], y[test_idx]
    
    print(f"Train samples: {len(X_train)}, Test samples: {len(X_test)}")
    
    # Create model
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = create_lvef_head(input_dim=args.input_dim).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.AdamW(model.parameters(), lr=args.learning_rate)
    
    # Training loop
    print("Training...")
    model.train()
    
    for epoch in range(args.epochs):
        total_loss = 0
        correct = 0
        
        # Simple batch processing
        for i in range(0, len(X_train), args.batch_size):
            batch_X = X_train[i:i+args.batch_size].to(device)
            batch_y = y_train[i:i+args.batch_size].to(device)
            
            optimizer.zero_grad()
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            correct += (predicted == batch_y).sum().item()
        
        accuracy = correct / len(X_train)
        avg_loss = total_loss / (len(X_train) // args.batch_size + 1)
        
        print(f"Epoch {epoch+1}/{args.epochs}: Loss={avg_loss:.4f}, Train Acc={accuracy:.4f}")
    
    # Test evaluation
    model.eval()
    with torch.no_grad():
        test_outputs = model(X_test.to(device))
        _, test_predicted = torch.max(test_outputs, 1)
        test_accuracy = accuracy_score(y_test.cpu(), test_predicted.cpu())
    
    print(f"\nFinal Test Accuracy: {test_accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test.cpu(), test_predicted.cpu(), 
                              target_names=['Dysfunction', 'Normal']))
    
    # Create model version directory
    from datetime import datetime
    import json
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    model_dir = Path(f"models/lvef_head_{timestamp}")
    model_dir.mkdir(parents=True, exist_ok=True)
    
    # Save weights
    weights_path = model_dir / "weights.pt"
    torch.save(model.state_dict(), weights_path)
    
    # Save training metrics
    metrics = {
        "test_accuracy": float(test_accuracy),
        "train_samples": len(X_train),
        "test_samples": len(X_test),
        "class_distribution": {
            "dysfunction": int(class_counts[0]),
            "normal": int(class_counts[1])
        },
        "final_train_accuracy": float(accuracy),
        "final_loss": float(avg_loss),
        "classification_report": classification_report(
            y_test.cpu(), test_predicted.cpu(), 
            target_names=['Dysfunction', 'Normal'],
            output_dict=True
        )
    }
    
    with open(model_dir / "metrics.json", 'w') as f:
        json.dump(metrics, f, indent=2)
    
    # Save training config
    config = {
        "epochs": args.epochs,
        "batch_size": args.batch_size,
        "learning_rate": args.learning_rate,
        "model_architecture": {
            "input_dim": 2048,
            "hidden_dim": 256,
            "output_dim": 2,
            "dropout": 0.1
        },
        "dataset": args.csv,
        "timestamp": timestamp,
        "embedding_type": "synthetic"  # Will be "real_ecgfounder" in production
    }
    
    with open(model_dir / "config.json", 'w') as f:
        json.dump(config, f, indent=2)
    
    # Save model README
    model_readme = f"""# LVEF Binary Classification Head

## Training Results
- **Test Accuracy**: {test_accuracy:.3f}
- **Train Accuracy**: {accuracy:.3f} 
- **Training Samples**: {len(X_train)}
- **Test Samples**: {len(X_test)}

## Class Distribution
- **Dysfunction (Class 0)**: {class_counts[0]} samples
- **Normal (Class 1)**: {class_counts[1]} samples

## Model Architecture
- **Input**: 2048-dim embeddings
- **Hidden**: 256 units with ReLU + Dropout(0.1)
- **Output**: 2-class binary classification

## Training Configuration
- **Epochs**: {args.epochs}
- **Batch Size**: {args.batch_size}
- **Learning Rate**: {args.learning_rate}
- **Embedding Type**: Synthetic (demo mode)

## Files
- `weights.pt`: Model state dict
- `metrics.json`: Detailed training metrics
- `config.json`: Training configuration

## Usage
Copy `weights.pt` to `../lvef_head_weights.pt` for automatic loading in inference pipeline.

## Notes
⚠️  This model was trained on synthetic embeddings for demonstration.
For production use, train with real ECG embeddings from PKUDigitalHealth/ECGFounder.
"""
    
    with open(model_dir / "README.md", 'w') as f:
        f.write(model_readme)
    
    # Copy weights to standard location for auto-loading
    standard_weights_path = Path("models/lvef_head_weights.pt")
    torch.save(model.state_dict(), standard_weights_path)
    
    print(f"✅ Model saved to: {model_dir}/")
    print(f"   - Weights: {weights_path}")
    print(f"   - Metrics: {model_dir}/metrics.json")
    print(f"   - Config: {model_dir}/config.json")
    print(f"   - Notes: {model_dir}/README.md")
    print(f"   - Auto-load: {standard_weights_path}")
    
    print(f"\n📊 Final Metrics:")
    print(f"   Test Accuracy: {test_accuracy:.3f}")
    print(f"   Dysfunction F1: {metrics['classification_report']['Dysfunction']['f1-score']:.3f}")
    print(f"   Normal F1: {metrics['classification_report']['Normal']['f1-score']:.3f}")
    
    print("\n📋 Next Steps:")
    print("1. This demo used synthetic embeddings")
    print("2. For real training, extract ECG embeddings from PKUDigitalHealth/ECGFounder")
    print("3. The saved weights are automatically loaded in future inference runs")
    
    return 0


if __name__ == "__main__":
    exit(main())
