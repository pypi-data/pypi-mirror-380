"""
Cardiotoxicity prediction heads for multimodal medical inference.

This module provides a consolidated prediction head manager specifically 
for cardiotoxicity risk assessment.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from pathlib import Path
from typing import Dict, Any, Optional
from loguru import logger


class CardiotoxicityPredictionHeads:
    """Manager for cardiotoxicity-specific prediction heads with built-in neural networks."""
    
    def __init__(self, hidden_size: int, device: str):
        """
        Initialize cardiotoxicity prediction heads.
        
        Args:
            hidden_size: Hidden size from the language model
            device: Device to run on
        """
        self.device = device
        self.risk_categories = ["low", "moderate", "high"]
        
        # Build survival head (regression for time-based risk predictions)
        self.survival_head = self._build_regression_head(
            input_dim=hidden_size,
            output_dim=4,  # immediate, 3_months, 6_months, 12_months
            hidden_dims=[512, 256],
            dropout=0.1
        ).to(device)
        
        # Build classification head (risk categories)
        self.classification_head = self._build_classification_head(
            input_dim=hidden_size,
            num_classes=3,  # Low, Moderate, High
            hidden_dims=[256],
            dropout=0.1
        ).to(device)
        
        # Build confidence head (regression for quality scores)
        self.confidence_head = self._build_regression_head(
            input_dim=hidden_size,
            output_dim=2,  # ecg_quality, prediction_confidence
            hidden_dims=[256],
            dropout=0.1
        ).to(device)
        
        # Build LVEF binary classification head (0=dysfunction <50%, 1=normal ≥50%)
        self.lvef_head = self._build_classification_head(
            input_dim=hidden_size,
            num_classes=2,  # Dysfunction, Normal
            hidden_dims=[256],
            dropout=0.1
        ).to(device)
        
        # Load pre-trained LVEF weights if available
        self._load_lvef_weights()
        
        # Set to eval mode
        self.survival_head.eval()
        self.classification_head.eval()
        self.confidence_head.eval()
        self.lvef_head.eval()
        
        logger.info("Cardiotoxicity prediction heads initialized")
    
    def _build_regression_head(
        self, 
        input_dim: int, 
        output_dim: int, 
        hidden_dims: list, 
        dropout: float
    ) -> nn.Module:
        """Build a regression head with specified architecture."""
        layers = []
        prev_dim = input_dim
        
        for hidden_dim in hidden_dims:
            layers.extend([
                nn.Linear(prev_dim, hidden_dim),
                nn.ReLU(),
                nn.Dropout(dropout)
            ])
            prev_dim = hidden_dim
            
        # Final output layer
        layers.append(nn.Linear(prev_dim, output_dim))
        
        return nn.Sequential(*layers)
    
    def _build_classification_head(
        self, 
        input_dim: int, 
        num_classes: int, 
        hidden_dims: list, 
        dropout: float
    ) -> nn.Module:
        """Build a classification head with specified architecture."""
        layers = []
        prev_dim = input_dim
        
        for hidden_dim in hidden_dims:
            layers.extend([
                nn.Linear(prev_dim, hidden_dim),
                nn.ReLU(),
                nn.Dropout(dropout)
            ])
            prev_dim = hidden_dim
            
        # Final classification layer
        layers.append(nn.Linear(prev_dim, num_classes))
        
        return nn.Sequential(*layers)
    
    def load_lvef_head(self, head_path: Optional[str] = None) -> bool:
        """Load LVEF head weights from specified path or use best available.
        
        Args:
            head_path: Optional path to specific LVEF head weights.
                      If None, uses latest versioned model or fallback.
        
        Returns:
            bool: True if weights loaded successfully, False otherwise.
        """
        if head_path:
            return self._load_lvef_from_path(head_path)
        else:
            return self._load_lvef_weights()
    
    def _load_lvef_from_path(self, path: str) -> bool:
        """Load LVEF weights from specific path."""
        try:
            state_dict = torch.load(path, map_location=self.device)
            self.lvef_head.load_state_dict(state_dict)
            logger.info(f"✅ Loaded custom LVEF head from {path}")
            return True
        except Exception as e:
            logger.warning(f"❌ Failed to load custom LVEF head from {path}: {e}")
            logger.info("Falling back to default head")
            return self._load_lvef_weights()
    
    def _load_lvef_weights(self) -> bool:
        """Load pre-trained LVEF head weights, preferring latest versioned model."""
        models_dir = Path(__file__).parent.parent.parent / "models"
        
        # Try to find latest versioned model first (preferred)
        lvef_dirs = list(models_dir.glob("lvef_head_*"))
        if lvef_dirs:
            # Get most recent by directory name (timestamp)
            latest_dir = max(lvef_dirs, key=lambda x: x.name)
            weights_path = latest_dir / "weights.pt"
            
            if weights_path.exists():
                try:
                    state_dict = torch.load(weights_path, map_location=self.device)
                    self.lvef_head.load_state_dict(state_dict)
                    
                    # Try to load metrics for logging
                    metrics_path = latest_dir / "metrics.json"
                    if metrics_path.exists():
                        import json
                        with open(metrics_path) as f:
                            metrics = json.load(f)
                        logger.info(f"✅ Loaded LVEF weights from {latest_dir} (Acc: {metrics['test_accuracy']:.3f})")
                    else:
                        logger.info(f"✅ Loaded LVEF weights from {latest_dir}")
                    return True
                except Exception as e:
                    logger.warning(f"Failed to load versioned LVEF weights: {e}")
        
        # Fallback to standard location if available
        standard_weights = models_dir / "lvef_head_weights.pt"
        if standard_weights.exists():
            try:
                state_dict = torch.load(standard_weights, map_location=self.device)
                self.lvef_head.load_state_dict(state_dict)
                logger.info(f"✅ Loaded LVEF weights from {standard_weights} (fallback)")
                return True
            except Exception as e:
                logger.warning(f"Failed to load standard LVEF weights: {e}")
        
        logger.warning("No LVEF head weights found - using untrained head")
        return False
        
        logger.info("⚠️  No pre-trained LVEF weights found - using random initialization")
    
    def predict_all(self, pooled_hidden: torch.Tensor, model_type: str) -> Dict[str, Any]:
        """
        Run all prediction heads and return formatted results.
        
        Args:
            pooled_hidden: Pooled hidden states from language model
            model_type: Type of model (for ECG quality scoring)
            
        Returns:
            Dictionary with all predictions
        """
        with torch.no_grad():
            # Survival predictions
            survival_logits = self.survival_head(pooled_hidden)
            survival_probs = torch.sigmoid(survival_logits).cpu().numpy()[0]
            
            # Risk classification
            classification_logits = self.classification_head(pooled_hidden)
            classification_probs = F.softmax(classification_logits, dim=-1)
            risk_category_idx = torch.argmax(classification_probs, dim=-1).item()
            risk_category = self.risk_categories[risk_category_idx]
            
            # LVEF binary classification
            lvef_logits = self.lvef_head(pooled_hidden)
            lvef_probs = F.softmax(lvef_logits, dim=-1).cpu().numpy()[0]
            lvef_class = torch.argmax(lvef_logits, dim=-1).item()
            
            # Confidence scores
            confidence_scores = self.confidence_head(pooled_hidden)
            confidence_vals = torch.sigmoid(confidence_scores).cpu().numpy()[0]
            
            return {
                "cardiotoxicity_risk": {
                    "immediate": float(survival_probs[0]),
                    "3_months": float(survival_probs[1]),
                    "6_months": float(survival_probs[2]),
                    "12_months": float(survival_probs[3])
                },
                "risk_category": risk_category,
                "lvef_classification": {
                    "class": lvef_class,  # 0=dysfunction, 1=normal
                    "dysfunction_prob": float(lvef_probs[0]),
                    "normal_prob": float(lvef_probs[1])
                },
                "confidence_scores": {
                    "ecg_quality": float(confidence_vals[0]) if model_type == "multimodal_with_ecg" else 0.0,
                    "prediction_confidence": float(confidence_vals[1])
                }
            }