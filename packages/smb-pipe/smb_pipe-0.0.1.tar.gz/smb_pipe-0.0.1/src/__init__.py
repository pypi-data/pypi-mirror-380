"""
Isolated inference endpoint for multimodal medical AI model.
This module provides inference capabilities without any UI dependencies.
"""

from .inference_pipeline import MultiModalMedicalInference

__all__ = ["MultiModalMedicalInference"]