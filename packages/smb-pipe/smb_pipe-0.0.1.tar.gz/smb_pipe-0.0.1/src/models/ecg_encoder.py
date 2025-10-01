"""ECG encoder implementations using HuggingFace models.

This module loads pre-trained ECG encoders from HuggingFace or local checkpoints.
"""

import os
import sys
import numpy as np
import torch
from typing import Dict, Any, Union, Optional
from transformers import AutoModel, AutoFeatureExtractor

from .base import BaseECGEncoder

try:
    from huggingface_hub import hf_hub_download
except ImportError:
    hf_hub_download = None

try:
    from vendor.ecgfounder.model import (
        ft_12lead_ECGFounder,
        ft_1lead_ECGFounder,
    )
except ImportError:
    ft_12lead_ECGFounder = None
    ft_1lead_ECGFounder = None


class HuggingFaceECGEncoder(BaseECGEncoder):
    """Generic ECG encoder that loads from HuggingFace."""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        
        # Model ID or path
        model_id = config.get("model_id", config.get("weights"))
        if not model_id:
            raise ValueError("Either 'model_id' or 'weights' must be specified in config")
            
        # Get HuggingFace token from environment
        hf_token = os.getenv("HF_TOKEN")
        
        # Load model and (optionally) processor
        load_kwargs = dict(
            trust_remote_code=True,
            torch_dtype=torch.float16 if config.get("dtype") == "float16" else torch.float32,
            token=hf_token,
        )
        try:
            self.model = AutoModel.from_pretrained(model_id, **load_kwargs)
        except Exception as e:
            # Retry with common subfolders used by repos that store checkpoints in a directory
            last_err = e
            for subfolder in ("checkpoint", "checkpoints", "weights"):
                try:
                    self.model = AutoModel.from_pretrained(model_id, subfolder=subfolder, **load_kwargs)
                    break
                except Exception as e2:
                    last_err = e2
                    self.model = None
            if self.model is None:
                raise ValueError(f"Failed to load model from {model_id}: {last_err}")
        self.model.to(self.device)
        self.model.eval()

        # Try to load a feature extractor if one exists; continue without if not
        self.feature_extractor = None
        try:
            self.feature_extractor = AutoFeatureExtractor.from_pretrained(model_id, token=hf_token)
        except Exception:
            # Try with the same subfolder candidates
            self.feature_extractor = None
            for subfolder in ("checkpoint", "checkpoints", "weights"):
                try:
                    self.feature_extractor = AutoFeatureExtractor.from_pretrained(
                        model_id, subfolder=subfolder, token=hf_token
                    )
                    break
                except Exception:
                    self.feature_extractor = None
            
        # Get expected input shape from config
        self.expected_channels = config.get("input_channels", 12)
        self.expected_length = config.get("signal_length", 5000)
        
    def load_weights(self, weights_path: str) -> None:
        """Load weights - already handled in __init__ for HF models."""
        pass
        
    def preprocess(self, ecg_data: np.ndarray) -> torch.Tensor:
        """Preprocess ECG data for the model."""
        # Ensure correct shape (channels, length)
        if ecg_data.ndim == 1:
            ecg_data = ecg_data.reshape(1, -1)
        elif ecg_data.shape[0] > ecg_data.shape[1]:
            ecg_data = ecg_data.T
            
        # Validate channels
        if ecg_data.shape[0] != self.expected_channels:
            raise ValueError(
                f"Expected {self.expected_channels} channels, got {ecg_data.shape[0]}"
            )
            
        # Resample/pad to expected length if needed
        current_length = ecg_data.shape[1]
        if current_length != self.expected_length:
            if current_length < self.expected_length:
                # Pad
                pad_width = self.expected_length - current_length
                ecg_data = np.pad(ecg_data, ((0, 0), (0, pad_width)), mode='constant')
            else:
                # Crop
                ecg_data = ecg_data[:, :self.expected_length]
                
        # Use feature extractor if available, but handle ECG-specific cases
        if self.feature_extractor:
            # For HuBERT-based ECG models, flatten multi-lead ECG to 1D
            if "hubert" in self.config.get("model_id", "").lower():
                # Flatten 12-lead ECG to 1D by concatenating leads
                ecg_1d = ecg_data.flatten()  # Shape: (12*5000,) = (60000,)
                inputs = self.feature_extractor(ecg_1d, return_tensors="pt", sampling_rate=500)
            else:
                # Standard feature extraction for other models
                inputs = self.feature_extractor(ecg_data, return_tensors="pt")
                
            # Common keys across extractors
            if "input_values" in inputs:
                tensor = inputs["input_values"]
            elif "values" in inputs:
                tensor = inputs["values"]
            else:
                # Fallback to first tensor value
                first_key = next(iter(inputs))
                tensor = inputs[first_key]
            return tensor.to(self.device)
        else:
            # Fallback when no feature extractor is available
            if "hubert" in self.config.get("model_id", "").lower():
                # HuBERT expects 1D input: flatten multi-lead ECG
                ecg_1d = ecg_data.flatten()  # Shape: (12*5000,) = (60000,)
                ecg_tensor = torch.FloatTensor(ecg_1d).unsqueeze(0)  # Add batch: (1, 60000)
            elif "videomae" in self.config.get("model_id", "").lower() or "vision" in self.config.get("model_id", "").lower():
                # VideoMAE expects (batch, frames, channels, height, width)
                ecg_tensor = torch.FloatTensor(ecg_data).unsqueeze(0)  # Add batch dimension
                batch_size, num_channels, length = ecg_tensor.shape
                
                # Create a 2D representation: split signal into segments
                height = 16  # Fixed height for video representation
                width = length // height
                if width * height < length:
                    width += 1
                    # Pad to fit
                    pad_length = width * height - length
                    ecg_tensor = torch.nn.functional.pad(ecg_tensor, (0, pad_length))
                
                # Reshape to 2D grid
                ecg_tensor = ecg_tensor.reshape(batch_size, num_channels, height, width)
                # Add channel dimension and treat ECG channels as frames
                ecg_tensor = ecg_tensor.unsqueeze(2)  # (batch, frames, 1, height, width)
                # Expand to 3 channels (RGB)
                ecg_tensor = ecg_tensor.expand(-1, -1, 3, -1, -1)
            else:
                # Standard transformer input: (batch, channels, length)
                ecg_tensor = torch.FloatTensor(ecg_data).unsqueeze(0)  # Add batch dimension
                
            return ecg_tensor.to(self.device)
            
    def encode(self, ecg_data: Union[np.ndarray, torch.Tensor], return_sequence: bool = False) -> torch.Tensor:
        """Encode ECG data into embeddings."""
        # Preprocess if needed
        if isinstance(ecg_data, np.ndarray):
            ecg_tensor = self.preprocess(ecg_data)
        else:
            ecg_tensor = ecg_data.to(self.device)
            
        # Generate embeddings
        with torch.no_grad():
            outputs = self.model(ecg_tensor)
            
            # Extract embeddings based on model output structure
            if hasattr(outputs, "last_hidden_state"):
                # Transformer models
                if return_sequence:
                    # Remove batch dimension -> (seq, hidden)
                    embeddings = outputs.last_hidden_state.squeeze(0)
                else:
                    embeddings = outputs.last_hidden_state.mean(dim=1)
            elif hasattr(outputs, "pooler_output"):
                # Models with pooler
                embeddings = outputs.pooler_output
            elif isinstance(outputs, tuple):
                # Some models return tuple (logits, features)
                embeddings = outputs[-1] if len(outputs) > 1 else outputs[0]
            else:
                # Direct tensor output
                embeddings = outputs
                
            # Ensure 2D output
            if not return_sequence:
                # Expect (batch, features)
                if embeddings.dim() > 2:
                    embeddings = embeddings.mean(dim=1)
            else:
                # Expect (seq, features)
                if embeddings.dim() == 2 and embeddings.size(0) == 1:
                    embeddings = embeddings.squeeze(0)
                elif embeddings.dim() == 3:
                    embeddings = embeddings.squeeze(0)
            
            # Project to expected connector dimension if needed (for Qwen3-WM compatibility)
            if embeddings.size(-1) != 1024:
                if not hasattr(self, 'projection'):
                    # Create projection layer on-demand
                    self.projection = torch.nn.Linear(embeddings.size(-1), 1024, bias=False).to(self.device)
                # Support (batch, hidden) or (seq, hidden)
                embeddings = self.projection(embeddings)
                
        return embeddings

class ECGFounderEncoder(BaseECGEncoder):
    """ECGFounder encoder loaded from a .pth checkpoint (Hugging Face or local).

    Produces a 1024-d embedding by mean-pooling the temporal feature map.
    """

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)

        # Ensure vendored ECGFounder modules are available
        if ft_12lead_ECGFounder is None or ft_1lead_ECGFounder is None:
            raise ImportError("Failed to load vendored ECGFounder model code.")

        self.mode = config.get("mode", "12lead")
        self.expected_channels = 12 if self.mode == "12lead" else 1
        self.expected_length = int(config.get("signal_length", 5000))

        # Resolve checkpoint path
        weights_path = config.get("weights")
        model_id = config.get("model_id")
        if (not weights_path) and model_id:
            # Download the appropriate checkpoint from HF hub (use HF_TOKEN if provided)
            try:
                if hf_hub_download is None:
                    raise ImportError("huggingface_hub not available")
                filename = (
                    "12_lead_ECGFounder.pth" if self.mode == "12lead" else "1_lead_ECGFounder.pth"
                )
                hf_token = os.getenv("HF_TOKEN")
                weights_path = hf_hub_download(
                    repo_id=model_id,
                    filename=filename,
                    token=hf_token,
                )
            except Exception as e:
                raise ValueError(f"Failed to download ECGFounder weights from {model_id}: {e}")
        if not weights_path or not os.path.exists(weights_path):
            raise ValueError("ECGFounderEncoder requires a valid 'weights' path or 'model_id' to download from.")

        # Instantiate model
        if self.mode == "12lead":
            self.model = ft_12lead_ECGFounder(
                device=self.device, pth=weights_path, n_classes=1, linear_prob=False
            )
        else:
            self.model = ft_1lead_ECGFounder(
                device=self.device, pth=weights_path, n_classes=1, linear_prob=False
            )
        self.model.eval()

    def load_weights(self, weights_path: str) -> None:
        # Weights are loaded during initialization for ECGFounderEncoder
        return None

    def preprocess(self, ecg_data: np.ndarray) -> torch.Tensor:
        # Ensure (channels, length)
        if ecg_data.ndim == 1:
            ecg_data = ecg_data.reshape(1, -1)
        elif ecg_data.shape[0] > ecg_data.shape[1]:
            ecg_data = ecg_data.T

        # Adjust channel count
        if ecg_data.shape[0] != self.expected_channels:
            if ecg_data.shape[0] < self.expected_channels:
                repeats = self.expected_channels // ecg_data.shape[0] + 1
                ecg_data = np.tile(ecg_data, (repeats, 1))[: self.expected_channels]
            else:
                ecg_data = ecg_data[: self.expected_channels]

        # Adjust length
        current_length = ecg_data.shape[1]
        if current_length != self.expected_length:
            if current_length < self.expected_length:
                pad_width = self.expected_length - current_length
                ecg_data = np.pad(ecg_data, ((0, 0), (0, pad_width)), mode="constant")
            else:
                ecg_data = ecg_data[:, : self.expected_length]

        return torch.FloatTensor(ecg_data).unsqueeze(0).to(self.device)

    def encode(self, ecg_data: Union[np.ndarray, torch.Tensor], return_sequence: bool = False) -> torch.Tensor:
        if isinstance(ecg_data, np.ndarray):
            ecg_tensor = self.preprocess(ecg_data)
        else:
            ecg_tensor = ecg_data.to(self.device)

        with torch.no_grad():
            outputs, features = self.model(ecg_tensor)
            # features shape: (batch, T, C)
            if return_sequence:
                embedding = features.squeeze(0)  # (T, C)
            else:
                # Mean over time -> (batch, C)
                embedding = features.mean(dim=1)
        return embedding