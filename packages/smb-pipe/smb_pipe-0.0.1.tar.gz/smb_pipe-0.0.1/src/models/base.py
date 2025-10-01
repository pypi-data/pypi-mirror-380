"""Base classes for models."""

import numpy as np
import torch
from abc import ABC, abstractmethod
from typing import Dict, Any, Union


class BaseECGEncoder(ABC):
    """Base class for ECG encoders."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.device = config.get("device", "cpu")
        
    @abstractmethod
    def load_weights(self, weights_path: str) -> None:
        """Load model weights."""
        pass
        
    @abstractmethod
    def preprocess(self, ecg_data: np.ndarray) -> torch.Tensor:
        """Preprocess ECG data."""
        pass
        
    @abstractmethod
    def encode(self, ecg_data: Union[np.ndarray, torch.Tensor]) -> torch.Tensor:
        """Encode ECG data to embeddings."""
        pass