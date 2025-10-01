#!/usr/bin/env python3
"""
Multimodal Medical Inference Pipeline with Multi-Head Predictions

Uses Qwen3-WM with multiple prediction heads for structured outputs:
- Survival head for time-based risk predictions
- Classification head for risk categories
- Regression head for confidence scores
- Text generation for clinical reports and recommendations
"""

import os
from typing import Dict, List, Optional, Any
from datetime import datetime

# ---------------------------------------------------------------------------
# Flash-Attention: try to import but fallback gracefully if not available
# ---------------------------------------------------------------------------
try:
    import flash_attn  # noqa: F401
    FLASH_ATTN_AVAILABLE = True
except Exception:
    FLASH_ATTN_AVAILABLE = False
    import warnings
    warnings.warn(
        "Flash-Attention not available. Models will use standard attention mechanisms. "
        "For better performance, install flash-attn compatible with your PyTorch version."
    )

import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModel
from loguru import logger

# Import components
from utils.results_formatter import ResultsFormatter
from models.prediction_heads import CardiotoxicityPredictionHeads
from utils.model_manager import ModelManager
from utils import logging_utils

# Import modality token generator for backward compatibility
from utils.modality_tokens import ModalityTokenGenerator


class MultiModalMedicalInference:
    """Multi-head inference pipeline supporting both multimodal and text-only models."""
    
    # Modality key mappings for embedding processing
    MODALITY_NAME_TO_KEY = {
        "ecg": "m1",
        "ct": "m2",  # Example for future modality key used by the model
    }

    def __init__(
        self,
        language_model: str = "standardmodelbio/Qwen3-WM-0.6B",
        encoders: Optional[Dict[str, str]] = None,
        device: str = "cuda" if torch.cuda.is_available() else "cpu",
    ):
        """
        Initialize the multimodal inference pipeline.
        
        Args:
            ecg_encoder: ECG encoder model ID (optional, required for multimodal models)
            language_model: Language model ID (multimodal or text-only)
            device: Device to run on ("cuda" or "cpu")
        """
        # Initialize model manager with a general encoders mapping.
        encoders_map: Dict[str, str] = {}
        if encoders is not None:
            try:
                encoders_map = dict(encoders)
            except Exception:
                encoders_map = {}

        self.model_manager = ModelManager(
            language_model=language_model,
            encoders=encoders_map,
            device=device
        )
        
        # Set attributes from model manager
        self.device = device
        self.language_model_id = language_model
        # Expose core attributes from the model manager.
        self.model_type = self.model_manager.model_type
        self.model_dtype = self.model_manager.model_dtype
        self.encoders: Dict[str, Optional[str]] = dict(
            getattr(self.model_manager, "encoders", {})
        )
        
        logger.info(f"Pipeline type: {self.model_type}")
        
        # Load all models through model manager
        (self.model, self.tokenizer,
         self.ecg_loader, self.ecg_encoder) = self.model_manager.load_all_models()
        
        # Initialize prediction heads manager
        self.prediction_heads = CardiotoxicityPredictionHeads(
            hidden_size=self.model.config.hidden_size,
            device=self.device
        )
        
        # Initialize utility classes
        self.results_formatter = ResultsFormatter()
        
    def predict(
        self,
        clinical_notes: str = "",
        task_prompt: str = "Provide a clinical assessment with detailed findings and recommendations.",
        modalities_inputs: Optional[Dict[str, Any]] = None,
        use_modalities: Optional[Dict[str, bool]] = None,
        skip_prompt_building: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Generate predictions using multiple heads and text generation.
        
        Args:
            clinical_notes: Clinical text or pre-built MEDS prompt
            task_prompt: Task instruction for the model
            modalities_inputs: Dict with modality file paths
            use_modalities: Dict controlling which modalities to use
            skip_prompt_building: If True, use clinical_notes as-is (for MEDS)
            **kwargs: Additional metadata to include in prompt
        
        Supports both multimodal (ECG + text) and text-only models.
        Returns the same structured output format regardless of model type.
        """
        start_time = datetime.now()
        
        # Resolve whether to use ECG (ablation-friendly) from generic inputs
        modalities_inputs = modalities_inputs or {}
        use_modalities = use_modalities or {}
        if self.model_type == "multimodal_with_ecg":
            ecg_spec = modalities_inputs.get("ecg", {}) or {}
            ecg_files = ecg_spec.get("files")
            requested = use_modalities.get("ecg") if "ecg" in use_modalities else None
            effective_use_ecg = bool(ecg_files) if requested is None else bool(requested)
            ecg_data_dir = ecg_spec.get("data_dir", "")
        else:
            effective_use_ecg = False
            ecg_files = None
            ecg_data_dir = ""

        # Track which modalities we're using for logging/formatting (simplified)
        # Note: Actual modality info is now generated in text_processor

        # Get embeddings and generate text based on model type
        if self.model_type == "multimodal_with_ecg":
            pooled_hidden, generated_text = self._process_multimodal(
                modalities_inputs=modalities_inputs,
                clinical_notes=clinical_notes,
                task_prompt=task_prompt,
                use_modalities={"ecg": effective_use_ecg},
                skip_prompt_building=skip_prompt_building,
                **kwargs
            )
        else:
            # Standard text-only processing (fallback)
            pooled_hidden, generated_text = self._process_standard(
                clinical_notes,
                task_prompt=task_prompt,
                skip_prompt_building=skip_prompt_building,
                **kwargs
            )
        
        # Run all prediction heads
        head_predictions = self.prediction_heads.predict_all(pooled_hidden, self.model_type)
        
        # Parse generated text for reports and recommendations
        clinical_reports, recommendations = self.results_formatter.parse_generated_text(generated_text)
        
        # Build structured output
        inference_time = (datetime.now() - start_time).total_seconds()
        
        # Build per-modality usage summary
        modalities_summary = {}
        if self.model_type == "multimodal_with_ecg":
            modalities_summary["ecg"] = {
                "used": bool(effective_use_ecg),
                "files": len(ecg_files) if ecg_files else 0,
            }

        predictions = self.results_formatter.format_predictions(
            head_predictions=head_predictions,
            clinical_reports=clinical_reports,
            recommendations=recommendations,
            generated_text=generated_text,
            model_type=self.model_type,
            inference_time=inference_time,
            language_model_id=self.language_model_id,
            encoders=self.encoders,
            modalities=modalities_summary,
        )
        
        return predictions
    
    def _process_multimodal(
        self,
        modalities_inputs,
        clinical_notes,
        task_prompt,
        skip_prompt_building=False,
        **kwargs
    ):
        """Process multimodal inputs (ECG + text) and return embeddings + text.

        Accepts ablation via kwargs: use_ecg: bool
        - If True: ECG must be present and successfully processed. Raises if missing.
        - If False: ECG is ignored even if files are provided (true ablation).
        """
        use_modalities = dict(kwargs.pop("use_modalities", {}) or {})
        use_ecg = bool(use_modalities.get("ecg", False))

        embeddings_by_name = {}
        modalities = ()

        if use_ecg:
            ecg_spec = modalities_inputs.get("ecg", {}) if modalities_inputs else {}
            ecg_files = ecg_spec.get("files")
            ecg_data_dir = ecg_spec.get("data_dir", "")
            if not ecg_files:
                raise FileNotFoundError("use_ecg=True but no ecg files were provided")

            if not (self.ecg_loader and self.ecg_encoder):
                raise RuntimeError("ECG components not initialized")

            ecg_embeddings = []
            for ecg_file in ecg_files:
                path = os.path.join(ecg_data_dir, ecg_file) if ecg_data_dir else ecg_file

                # Load and process ECG
                ecg_data = self.ecg_loader.load_ecg_file(path)
                ecg_data = self.ecg_loader.preprocess_ecg(ecg_data, normalize=True)

                # Generate sequence embeddings so placeholder count matches
                embedding = self.ecg_encoder.encode(ecg_data, return_sequence=True)
                ecg_embeddings.append(embedding)

            if not ecg_embeddings:
                raise RuntimeError("use_ecg=True but no ECG embeddings were produced")

            # Average multiple ECGs if provided
            ecg_tensor = torch.stack(ecg_embeddings).mean(dim=0, keepdim=True)
            embeddings_by_name["ecg"] = ecg_tensor.to(dtype=self.model_dtype, device=self.device)
            embeddings_dict, modality_info = self._prepare_modalities(embeddings_by_name)
        else:
            embeddings_dict = None
            modality_info = None

        # Build prompt (skip if already built externally, e.g., MEDS)
        if skip_prompt_building:
            prompt = clinical_notes
        else:
            # Legacy: Use text processor for CSV-based prompts
            # NOTE: This path is deprecated and will be removed
            # when TextProcessor is restored or fully migrated
            prompt = (
                f"{clinical_notes}\n\n{task_prompt}"
                if clinical_notes
                else task_prompt
            )

        # Log the prepared prompt for debugging/tracking 
        modality_names = tuple(modality_info.keys()) if modality_info else ()
        self._log_input_prompt(prompt, modality_names, kwargs.get('row_idx'))
        
        return self._run_generation(prompt, embeddings_dict)
    
    def _process_standard(self, clinical_notes, skip_prompt_building=False, **kwargs):
        """Process with standard LLM (text-only)."""
        task_prompt = kwargs.pop("task_prompt", "Provide a clinical assessment with detailed findings and recommendations.")
        
        # Build prompt (skip if already built externally)
        if skip_prompt_building:
            prompt = clinical_notes
        else:
            prompt = (
                f"{clinical_notes}\n\n{task_prompt}"
                if clinical_notes
                else task_prompt
            )
        
        # Log the prepared prompt for debugging/tracking
        self._log_input_prompt(prompt, (), kwargs.get('row_idx'))
        
        return self._run_generation(prompt)

    # ------------------------------------------------------------------
    # Shared helper for tokenization, forward, pooling, generation
    # ------------------------------------------------------------------
    def _prepare_modalities(self, modality_embeddings: Dict[str, torch.Tensor]):
        """Prepare embeddings and metadata for multimodal processing.

        Args:
            modality_embeddings: Dict mapping modality name (e.g., "ecg")
                                  to its embedding tensor.

        Returns:
            Tuple of (embeddings_dict_for_model, modality_metadata_for_text_processor)
        """
        embeddings_dict: Dict[str, torch.Tensor] = {}
        modality_info: Dict[str, Dict[str, Any]] = {}

        for name, tensor in modality_embeddings.items():
            key = self.MODALITY_NAME_TO_KEY.get(name)
            if not key:
                continue

            # Normalize embedding tensor to shape (seq_len, hidden)
            embedding_matrix = tensor
            if embedding_matrix is None:
                continue
            if embedding_matrix.dim() == 1:
                embedding_matrix = embedding_matrix.unsqueeze(0)
            elif embedding_matrix.dim() == 3:
                # Collapse batch dimension if present: (batch, seq, hidden) -> (seq, hidden)
                embedding_matrix = embedding_matrix.mean(dim=0)

            # Ensure 2D
            if embedding_matrix.dim() != 2:
                # Best effort: flatten to (seq, hidden)
                embedding_matrix = embedding_matrix.view(embedding_matrix.size(0), -1)

            seq_len = int(embedding_matrix.size(0))

            # Store embeddings for model
            embeddings_dict[key] = embedding_matrix.to(dtype=self.model_dtype, device=self.device)
            
            # Store metadata for text processor
            modality_info[name] = {"seq_len": seq_len}

        return (embeddings_dict if embeddings_dict else None), (modality_info if modality_info else None)

    def _run_generation(self, prompt: str, embeddings_dict: Optional[dict] = None):
        """Tokenize prompt, run model, pool, generate, and decode.

        Returns:
            Tuple[torch.Tensor, str]: (pooled_hidden, generated_text)
        """
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512
        )
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        model_kwargs = {
            "input_ids": inputs["input_ids"],
            "output_hidden_states": True,
            "return_dict": True,
        }
        if embeddings_dict is not None:
            model_kwargs["embeddings"] = embeddings_dict

        with torch.no_grad():
            outputs = self.model(**model_kwargs)

            pooled_hidden = self.mean_pooling(
                outputs.hidden_states[-1],
                inputs.get("attention_mask")
            )

            generate_kwargs = {
                "input_ids": inputs["input_ids"],
                "max_new_tokens": 200,
                "temperature": 0.7,
                "do_sample": True,
                "pad_token_id": self.tokenizer.pad_token_id,
                "eos_token_id": self.tokenizer.eos_token_id,
            }
            if embeddings_dict is not None:
                generate_kwargs["embeddings"] = embeddings_dict

            generation_outputs = self.model.generate(**generate_kwargs)

            # Strip the prompt tokens from the output
            input_length = inputs["input_ids"].shape[1]
            generated_ids = generation_outputs[0][input_length:]
            generated_text = self.tokenizer.decode(
                generated_ids, skip_special_tokens=True
            )

        return pooled_hidden, generated_text

    def mean_pooling(self, hidden_states: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
        """Apply mean pooling to hidden states."""
        # Expand attention mask for hidden size
        attention_mask_expanded = attention_mask.unsqueeze(-1).expand(hidden_states.size()).float()
        
        # Apply mask and compute mean
        sum_embeddings = torch.sum(hidden_states * attention_mask_expanded, 1)
        sum_mask = torch.clamp(attention_mask_expanded.sum(1), min=1e-9)
        
        return sum_embeddings / sum_mask

    def _log_input_prompt(self, prompt: str, modalities: tuple = (), row_idx: int = None) -> None:
        """Log input prompt for debugging and tracking."""
        # Check if we should show prompts in console (even with --quiet)
        show_full_prompt = getattr(self, 'show_prompts', False)
        
        # Log to local logs
        logging_utils.log_input_prompt(prompt, modalities, row_idx, show_full_prompt)
        
        # External trackers can hook here if desired.