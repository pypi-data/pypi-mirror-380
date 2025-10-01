"""Model loading and initialization manager."""

import os
import torch
from typing import Dict, List, Optional, Any, Tuple
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModel
from loguru import logger

# Local utility imports
# ECG encoder classes live in models.ecg_encoder; we load them lazily to avoid
# pulling heavy deps unless the encoder is actually requested.
from .ecg_processing import ECGDataLoader


class ModelManager:
    """Manages loading and initialization of different model types."""
    
    # Whitelists for accepted model IDs
    ALLOWED_ECG_ENCODERS: List[str] = [
        "PKUDigitalHealth/ECGFounder",
        "Edoardo-BS/hubert-ecg-base",
    ]
    
    ALLOWED_LANGUAGE_MODELS: List[str] = [
        "standardmodelbio/Qwen3-WM-0.6B",
        "standardmodelbio/MACE-0.6B-base",
        "standardmodelbio/smb-mntp-llama-3.1-8b"
    ]
    
    # Mapping of ECG encoder IDs to their encoder class implementations
    ECG_ENCODER_CLASS_MAP: Dict[str, str] = {
        "PKUDigitalHealth/ECGFounder": "ECGFounderEncoder",  # Uses vendored code
        "Edoardo-BS/hubert-ecg-base": "HuggingFaceECGEncoder",  # Standard HF format
    }
    
    def __init__(
        self, 
        language_model: str, 
        encoders: Optional[Dict[str, str]] = None,
        device: str = "cuda" if torch.cuda.is_available() else "cpu"
    ):
        """
        Initialize model manager.
        
        Args:
            language_model: Language model ID
            ecg_encoder: ECG encoder model ID (optional)
            device: Device to run on ("cuda" or "cpu")
        """
        self.language_model_id = language_model
        self.device = device
        # Generalized encoders mapping (e.g., {"ecg": "...", "ct": "..."}).
        self.encoders: Dict[str, str] = dict(encoders or {})
        self.hf_token = os.getenv("HF_TOKEN")
        
        # Validate models
        self._validate_models()
        
        # Determine model type and dtype
        self.model_type = self.determine_model_type()
        self.model_dtype = torch.float16 if self.device == "cuda" else torch.float32
        
        # Initialize components
        self.model = None
        self.tokenizer = None
        self.ecg_loader = None
        self.ecg_encoder = None
        
    def _validate_models(self) -> None:
        """Validate model IDs against whitelists."""
        if self.language_model_id not in self.ALLOWED_LANGUAGE_MODELS:
            raise ValueError(
                f"Unsupported language model '{self.language_model_id}'.\n"
                f"Allowed models: {self.ALLOWED_LANGUAGE_MODELS}"
            )

        ecg_id = self.encoders.get("ecg")
        if ecg_id and ecg_id not in self.ALLOWED_ECG_ENCODERS:
            raise ValueError(
                f"Unsupported ECG encoder '{ecg_id}'.\n"
                f"Allowed encoders: {self.ALLOWED_ECG_ENCODERS}"
            )
    
    def determine_model_type(self) -> str:
        """Determine pipeline type based on provided models."""
        if self.encoders.get("ecg"):
            return "multimodal_with_ecg"
        else:
            return "standard_llm"
    
    def load_all_models(self) -> Tuple[Any, Any, Optional[Any], Optional[Any]]:
        """
        Load all models based on model type.
        
        Returns:
            Tuple of (model, tokenizer, ecg_loader, ecg_encoder)
        """
        logger.info(f"Loading {self.model_type} pipeline...")
        
        if self.model_type == "multimodal_with_ecg":
            return self._load_multimodal_models()
        else:
            return self._load_standard_models()
    
    def _load_multimodal_models(self) -> Tuple[Any, Any, Any, Any]:
        """Load multimodal pipeline components."""
        # Initialize ECG components
        self.ecg_loader = ECGDataLoader()
        
        # ------------------------------------------------------------------
        # Initialize ECG encoder (logic inlined from former model_loader.py)
        # ------------------------------------------------------------------
        encoder_class_name = self.ECG_ENCODER_CLASS_MAP[self.encoders["ecg"]]

        ecg_config = {
            "class": encoder_class_name,
            "model_id": self.encoders["ecg"],
            "device": self.device,
        }

        self.ecg_encoder = self.create_ecg_encoder(ecg_config)
        
        logger.info(f"Loading multimodal model: {self.language_model_id}")
        
        # Load language model with trust_remote_code for custom architecture
        self.model = AutoModelForCausalLM.from_pretrained(
            self.language_model_id,
            torch_dtype=self.model_dtype,
            trust_remote_code=True,
            token=self.hf_token,
        )
        
        self.tokenizer = self._load_tokenizer(trust_remote_code=True)

        # Register modality placeholder tokens once per load. Currently only ECG.
        self._register_modality_tokens()
        self.model.to(self.device)
        self.model.eval()
        
        return self.model, self.tokenizer, self.ecg_loader, self.ecg_encoder

    # ------------------------------------------------------------------
    # Static helpers
    # ------------------------------------------------------------------

    @staticmethod
    def create_ecg_encoder(ecg_config: Dict[str, Any]):
        """Instantiate an ECG encoder given its config dict.

        This logic was previously located in utils/model_loader.py but has
        been moved here to avoid a dedicated one‐function module.
        """
        encoder_class = ecg_config["class"]

        if encoder_class == "ECGFounderEncoder":
            from models.ecg_encoder import ECGFounderEncoder as _Encoder
        elif encoder_class == "HuggingFaceECGEncoder":
            from models.ecg_encoder import HuggingFaceECGEncoder as _Encoder
        else:
            raise ValueError(
                f"Unknown encoder class: {encoder_class}. "
                f"Expected one of: ECGFounderEncoder, HuggingFaceECGEncoder"
            )

        return _Encoder(ecg_config)

    # ---------------------------------------------------------------------
    # Private helpers
    # ---------------------------------------------------------------------

    def _register_modality_tokens(self) -> None:
        """Ensure special modality tokens exist in tokenizer and model config.

        This allows the model to splice external modality embeddings at the
        correct placeholder positions. Registers placeholder tokens per modality.
        """
        special_tokens = {"additional_special_tokens": [
            "<m1_pad>", "<m2_pad>",
            "<m1_start>", "<m1_end>",
            "<m2_start>", "<m2_end>",
        ]}

        # add_special_tokens returns the number of tokens added; 0 if present
        added_count = self.tokenizer.add_special_tokens(special_tokens)

        if added_count:
            # Resize token embeddings so new indices are valid.
            self.model.resize_token_embeddings(len(self.tokenizer))

        # Store token ids on config for easy access downstream.
        self.model.config.m1_token_id = self.tokenizer.convert_tokens_to_ids("<m1_pad>")
        self.model.config.m2_token_id = self.tokenizer.convert_tokens_to_ids("<m2_pad>")
        self.model.config.m1_start_id = self.tokenizer.convert_tokens_to_ids("<m1_start>")
        self.model.config.m1_end_id = self.tokenizer.convert_tokens_to_ids("<m1_end>")
        self.model.config.m2_start_id = self.tokenizer.convert_tokens_to_ids("<m2_start>")
        self.model.config.m2_end_id = self.tokenizer.convert_tokens_to_ids("<m2_end>")
    
    def _load_standard_models(self) -> Tuple[Any, Any, None, None]:
        """Load standard LLM pipeline components."""
        logger.info(f"Loading standard LLM: {self.language_model_id}")
        
        # Load as standard causal LM
        self.model = AutoModelForCausalLM.from_pretrained(
            self.language_model_id,
            torch_dtype=self.model_dtype,
            trust_remote_code=True,
            token=self.hf_token,
        )
        
        self.tokenizer = self._load_tokenizer(trust_remote_code=True)
        self.model.to(self.device)
        self.model.eval()
        
        return self.model, self.tokenizer, None, None
    
    def _load_tokenizer(self, trust_remote_code=False):
        """Load tokenizer with proper configuration."""
        try:
            tokenizer = AutoTokenizer.from_pretrained(
                self.language_model_id,
                trust_remote_code=trust_remote_code,
                token=self.hf_token,
            )
        except Exception as e:
            logger.warning(f"Fast tokenizer failed, trying slow tokenizer: {e}")
            tokenizer = AutoTokenizer.from_pretrained(
                self.language_model_id,
                trust_remote_code=trust_remote_code,
                token=self.hf_token,
                use_fast=False,
            )
        
        # Set padding token if needed
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

        return tokenizer