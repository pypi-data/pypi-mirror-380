"""Shared modality token generation for training and inference."""

from typing import Dict, List


class ModalityTokenGenerator:
    """Generates consistent modality tokens for training and inference."""
    
    # Centralized modality configuration
    MODALITY_CONFIG = {
        "ecg": {"key": "m1", "pad_token": "<m1_pad>"},
        "ct": {"key": "m2", "pad_token": "<m2_pad>"},
        "mri": {"key": "m3", "pad_token": "<m3_pad>"},
    }
    
    @staticmethod
    def generate_tokens(
        modality: str,
        count: int,
        use_pipes: bool = True
    ) -> str:
        """
        Generate modality tokens.
        
        Args:
            modality: Modality name (ecg, ct, mri)
            count: Number of files or sequence length
            use_pipes: Whether to use pipes in start/end tokens
        
        Returns:
            Token string: <|m1_start|><m1_pad>...<|m1_end|>
        """
        if count <= 0:
            return ""
        
        config = ModalityTokenGenerator.MODALITY_CONFIG.get(modality)
        if not config:
            raise ValueError(f"Unknown modality: {modality}")
        
        key = config["key"]
        pad_token = config["pad_token"]
        
        # Format start/end tokens with or without pipes
        if use_pipes:
            start = f"<|{key}_start|>"
            end = f"<|{key}_end|>"
        else:
            start = f"<{key}_start>"
            end = f"<{key}_end>"
        
        # Build token string
        pad_tokens = pad_token * count
        return f"{start}{pad_tokens}{end}"
    
    @staticmethod
    def generate_multi_modality_tokens(
        modality_info: Dict[str, int],
        use_pipes: bool = True
    ) -> str:
        """
        Generate tokens for multiple modalities.
        
        Args:
            modality_info: Dict mapping modality name to count
                          e.g., {"ecg": 128, "ct": 5}
            use_pipes: Whether to use pipes in start/end tokens
        
        Returns:
            Combined token string for all modalities
        """
        tokens = []
        
        # Process in deterministic order
        for modality in sorted(modality_info.keys()):
            count = modality_info[modality]
            if count > 0:
                token_str = ModalityTokenGenerator.generate_tokens(
                    modality=modality,
                    count=count,
                    use_pipes=use_pipes
                )
                tokens.append(token_str)
        
        return "".join(tokens)
    
    @staticmethod
    def get_modality_key(modality: str) -> str:
        """Get the key (m1, m2, m3) for a modality."""
        config = ModalityTokenGenerator.MODALITY_CONFIG.get(modality)
        if not config:
            raise ValueError(f"Unknown modality: {modality}")
        return config["key"]
