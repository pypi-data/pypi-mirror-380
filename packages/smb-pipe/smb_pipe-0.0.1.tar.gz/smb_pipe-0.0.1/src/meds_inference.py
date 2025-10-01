#!/usr/bin/env python3
"""
MEDS-based batch inference for multi-timepoint patient data.

Run MultiModalMedicalInference on MEDS-format parquet files.

Example (CLI)
-------------
# Basic usage (EHR-only, no file modalities in this dataset)
uv run src/meds_inference.py \
    --data s3://smb-dev-scratch/data.parquet \
    --hf-token $HF_TOKEN \
    --aws-access-key $AWS_ACCESS_KEY_ID \
    --aws-secret-key $AWS_SECRET_ACCESS_KEY \
    --language-model standardmodelbio/Qwen3-WM-0.6B \
    --encoders '{"ecg": "PKUDigitalHealth/ECGFounder"}' \
    --modality-config '{"ehr": {"include_tables": ["person", "measurement", "condition", "observation"]}}' \
    --subjects-limit 1

# Filter out noisy EHR tables (cache-dir and lookback-days are optional)
uv run src/meds_inference.py \
    --data s3://smb-dev-scratch/data.parquet \
    --hf-token $HF_TOKEN \
    --aws-access-key $AWS_ACCESS_KEY_ID \
    --aws-secret-key $AWS_SECRET_ACCESS_KEY \
    --language-model standardmodelbio/Qwen3-WM-0.6B \
    --encoders '{"ecg": "PKUDigitalHealth/ECGFounder"}' \
    --modality-config '{"ehr": {"exclude_tables": ["note", "visit_detail"]}}' \
    --subjects-limit 100

# With file modalities (when data has paths populated)
uv run src/meds_inference.py \
    --data s3://your-bucket/data-with-imaging.parquet \
    --hf-token $HF_TOKEN \
    --aws-access-key $AWS_ACCESS_KEY_ID \
    --aws-secret-key $AWS_SECRET_ACCESS_KEY \
    --language-model standardmodelbio/Qwen3-WM-0.6B \
    --encoders '{"ecg": "PKUDigitalHealth/ECGFounder"}' \
    --modality-config '{"ecg": {"path_columns": ["img_path"]}, "ct": {"path_columns": ["ct_path"]}, "ehr": {"exclude_tables": ["note"]}}' \
    --subjects-limit 100

Example (Programmatic)
----------------------
import os
from meds_inference import MEDSEmbeddingsGenerator

# Create generator (all config explicit)
generator = MEDSEmbeddingsGenerator(
    data_source="s3://smb-dev-scratch/data.parquet",
    hf_token=os.getenv("HF_TOKEN"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    language_model="standardmodelbio/Qwen3-WM-0.6B",
    encoders={"ecg": "PKUDigitalHealth/ECGFounder"},
    modality_config={
        # EHR: which MEDS tables to include in prompt
        "ehr": {
            "include_tables": ["person", "measurement", "condition", "observation"],
            "exclude_tables": ["note", "visit_detail"]
        }
        # Note: No file modalities - smb-dev-scratch data has no imaging
    },
    aws_region="us-east-2",
    cache_dir="./.cache",
    lookback_days=365  # Optional, showing default
)

# Preview prompt before running (prints formatted output automatically)
sample_prompt = generator.show_prompt()

# Generate embeddings (output defaults to ./.cache/embeddings/)
results = generator.generate_embeddings(subjects_limit=100)
"""

import argparse
import json
import os
from pathlib import Path
from typing import Dict, List, Optional

from inference_pipeline import MultiModalMedicalInference
from utils.meds_prompt_builder import MEDSPromptBuilder
from utils.meds_inference_utils import (
    MEDSDataLoader,
    MEDSModalityExtractor,
    MEDSBatchProcessor
)


class MEDSEmbeddingsGenerator:
    """
    One-step embeddings generation for MEDS-format patient data.
    
    This class encapsulates the entire pipeline from MEDS data loading
    through embeddings generation, with clean I/O and explicit configuration.
    """
    
    def __init__(
        self,
        data_source: str,
        hf_token: str,
        modality_config: Optional[Dict[str, Dict]] = None,
        aws_access_key_id: Optional[str] = None,
        aws_secret_access_key: Optional[str] = None,
        aws_region: str = "us-east-2",
        language_model: str = "standardmodelbio/Qwen3-WM-0.6B",
        encoders: Optional[Dict[str, str]] = None,
        cache_dir: str = "./.cache",
        lookback_days: int = 365,
    ):
        """
        Initialize embeddings generator.
        
        Args:
            data_source: Path to MEDS parquet (local or S3)
            hf_token: HuggingFace API token (required)
            modality_config: Dict mapping modalities to column names
                Example: {
                    "ecg": {"path_columns": ["img_path", "ecg_path"]},
                    "ct": {"path_columns": ["ct_path"]},
                    "ehr": {"columns": ["age", "gender", "impressions"]}
                }
            aws_access_key_id: AWS access key (optional, uses env if None)
            aws_secret_access_key: AWS secret key (optional, uses env if None)
            aws_region: AWS region for S3 access
            language_model: HuggingFace model ID
            encoders: Dict mapping modality to encoder model ID
            cache_dir: Base directory for caching models and embeddings
            lookback_days: Days of patient history to include
        """
        # Validate required keys
        if not hf_token:
            raise ValueError("hf_token is required")
        
        # Store configuration
        self.data_source = data_source
        self.aws_region = aws_region
        self.lookback_days = lookback_days
        
        # Set up cache directories (only for our outputs, not models)
        self.cache_dir = Path(cache_dir)
        self.embeddings_cache = self.cache_dir / "embeddings"
        self.prompts_cache = self.cache_dir / "prompts"
        
        self.embeddings_cache.mkdir(parents=True, exist_ok=True)
        self.prompts_cache.mkdir(parents=True, exist_ok=True)
        
        # Set environment variables for authentication
        os.environ["HF_TOKEN"] = hf_token
        os.environ["HUGGINGFACE_HUB_TOKEN"] = hf_token
        # Note: HF models download to ~/.cache/huggingface/ (default)
        
        if aws_access_key_id:
            os.environ["AWS_ACCESS_KEY_ID"] = aws_access_key_id
        if aws_secret_access_key:
            os.environ["AWS_SECRET_ACCESS_KEY"] = aws_secret_access_key
        if aws_region:
            os.environ["AWS_REGION"] = aws_region
        
        # Set default encoders
        if encoders is None:
            encoders = {"ecg": "PKUDigitalHealth/ECGFounder"}
        
        # Set default modality config
        if modality_config is None:
            modality_config = {
                # EHR: include all tables by default
                "ehr": {
                    "include_tables": None,  # None = all tables
                    "exclude_tables": [],     # Can exclude specific tables
                    "include_codes": None,    # None = all codes
                    "exclude_codes": []       # Can exclude specific codes
                }
                # Note: File-based modalities (ecg, ct, mri) should be
                # explicitly configured based on your data's path columns
            }
        
        # Initialize components
        self.language_model = language_model
        self.encoders = encoders
        self.modality_config = modality_config
        
        # Extract EHR config for prompt builder
        ehr_config = modality_config.get("ehr") if modality_config else None
        self.prompt_builder = MEDSPromptBuilder(ehr_config=ehr_config)
        self.pipe = None  # Lazy-loaded
        
        # Save run metadata (after all attributes are set)
        self._save_run_metadata()
    
    def _save_run_metadata(self) -> None:
        """Save metadata about the run configuration."""
        from datetime import datetime
        
        hf_cache = Path.home() / '.cache' / 'huggingface'
        
        metadata = {
            'run_timestamp': datetime.now().isoformat(),
            'data_source': self.data_source,
            'language_model': self.language_model,
            'encoders': self.encoders,
            'modality_config': self.modality_config,
            'lookback_days': self.lookback_days,
            'cache_locations': {
                'huggingface_models': str(hf_cache),
                'embeddings_output': str(self.embeddings_cache),
                'prompts_output': str(self.prompts_cache)
            },
            'model_paths': {
                'language_model': str(hf_cache / 'hub' / f'models--{self.language_model.replace("/", "--")}'),
                'encoders': {
                    name: str(hf_cache / 'hub' / f'models--{model_id.replace("/", "--")}')
                    for name, model_id in self.encoders.items()
                }
            }
        }
        
        metadata_file = self.cache_dir / 'run_metadata.json'
        with metadata_file.open('w') as f:
            json.dump(metadata, f, indent=2)
    
    def _ensure_pipeline_loaded(self) -> None:
        """Lazy-load the inference pipeline."""
        if self.pipe is None:
            # Suppress verbose model loading output
            import logging
            import warnings
            
            # Save current levels
            transformers_logger = logging.getLogger("transformers")
            old_level = transformers_logger.level
            
            # Suppress warnings about uninitialized weights
            transformers_logger.setLevel(logging.ERROR)
            warnings.filterwarnings(
                'ignore',
                message='Some weights.*were not initialized.*'
            )
            
            try:
                self.pipe = MultiModalMedicalInference(
                    language_model=self.language_model,
                    encoders=self.encoders
                )
            finally:
                # Restore logging level
                transformers_logger.setLevel(old_level)
    
    def show_prompt(
        self,
        subject_id: Optional[str] = None,
        subjects_limit: int = 1,
        print_output: bool = True,
        preview_length: int = 500
    ) -> str:
        """
        Preview the generated prompt for a sample subject.
        
        Useful for auditing and debugging prompt generation.
        
        Args:
            subject_id: Specific subject ID to preview (optional)
            subjects_limit: Number of subjects to load if not provided
            print_output: Whether to print formatted preview (default: True)
            preview_length: Number of characters to show (default: 500)
        
        Returns:
            Generated MEDS prompt string
        """
        try:
            # Load sample data
            df = MEDSDataLoader.load_meds_data(
                data_source=self.data_source,
                subject_ids=[subject_id] if subject_id else None,
                subjects_limit=subjects_limit,
                aws_region=self.aws_region
            )
            
            # Get first subject
            first_subject_id = df['subject_id'].iloc[0]
            patient_df = df[df['subject_id'] == first_subject_id]
            
            # Build window
            window_df = MEDSDataLoader.build_inference_window(
                patient_df,
                window_end_time=None,
                lookback_days=self.lookback_days
            )
            
            # Extract modality paths using config
            modality_paths = MEDSModalityExtractor.extract_modality_paths(
                window_df,
                modality_config=self.modality_config
            )
            
            # Build prompt
            time_span = (window_df['time'].min(), window_df['time'].max())
            prompt = self.prompt_builder.build_prompt(
                events_df=window_df,
                modality_paths=modality_paths if modality_paths else None,
                time_span=time_span,
                include_time_span=True
            )
            
            # Print formatted preview if requested
            if print_output:
                print(f"\n📋 Sample Prompt Preview (Subject: {first_subject_id})")
                print("=" * 60)
                
                # Show modality info
                if modality_paths:
                    print(f"Modalities found:")
                    for mod, paths in modality_paths.items():
                        print(f"  {mod}: {len(paths)} files")
                else:
                    print(f"Modalities found: None")
                
                print(f"\nPrompt (first {preview_length} chars):")
                print("-" * 60)
                print(prompt[:preview_length])
                if len(prompt) > preview_length:
                    print(f"\n... (truncated, full: {len(prompt)} chars)")
                print("=" * 60)
            
            return prompt
        
        except Exception as e:
            if print_output:
                print(f"⚠️  Could not generate sample prompt: {e}")
            raise
    
    def generate_embeddings(
        self,
        subjects_limit: Optional[int] = None,
        subject_ids: Optional[List[str]] = None,
        output_path: Optional[str] = None,
        task_prompt: Optional[str] = None,
    ) -> List[Dict]:
        """
        Generate embeddings for MEDS patient data.
        
        Args:
            subjects_limit: Limit number of subjects to process
            subject_ids: Optional list of specific subject IDs
            output_path: Optional path to save results (JSONL)
            task_prompt: Optional custom task prompt
        
        Returns:
            List of results with embeddings and predictions
        """
        # Load MEDS data
        df = MEDSDataLoader.load_meds_data(
            data_source=self.data_source,
            subject_ids=subject_ids,
            subjects_limit=subjects_limit,
            aws_region=self.aws_region
        )
        
        # Ensure pipeline is loaded
        self._ensure_pipeline_loaded()
        
        # Set default output path if not provided
        if output_path is None:
            timestamp = Path(self.data_source).stem
            output_path = str(
                self.embeddings_cache / f"embeddings_{timestamp}.jsonl"
            )
        
        # Run batch inference with modality config
        results = MEDSBatchProcessor.process_batch_inference(
            df=df,
            pipe=self.pipe,
            prompt_builder=self.prompt_builder,
            modality_config=self.modality_config,
            out_path=output_path,
            task_prompt=task_prompt,
            lookback_days=self.lookback_days
        )
        
        return results
    
    @property
    def cache_info(self) -> Dict[str, str]:
        """Get cache directory information."""
        return {
            'base': str(self.cache_dir),
            'embeddings': str(self.embeddings_cache),
            'prompts': str(self.prompts_cache),
            'hf_models': str(Path.home() / '.cache' / 'huggingface')
        }

def parse_args():
    """Parse command line arguments."""
    p = argparse.ArgumentParser(
        description="MEDS-based batch inference",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic (all required params)
  uv run src/meds_inference.py \\
      --data s3://smb-dev-scratch/data.parquet \\
      --hf-token $HF_TOKEN \\
      --aws-access-key $AWS_ACCESS_KEY_ID \\
      --aws-secret-key $AWS_SECRET_ACCESS_KEY \\
      --language-model standardmodelbio/Qwen3-WM-0.6B \\
      --encoders '{"ecg": "PKUDigitalHealth/ECGFounder"}' \\
      --modality-config '{"ehr": {"include_tables": ["person", "measurement", "condition", "observation"]}}' \\
      --subjects-limit 1
  
  # With imaging and custom optional params
  uv run src/meds_inference.py \\
      --data s3://your-bucket/data-with-imaging.parquet \\
      --hf-token $HF_TOKEN \\
      --aws-access-key $AWS_ACCESS_KEY_ID \\
      --aws-secret-key $AWS_SECRET_ACCESS_KEY \\
      --language-model standardmodelbio/Qwen3-WM-0.6B \\
      --encoders '{"ecg": "PKUDigitalHealth/ECGFounder"}' \\
      --modality-config '{"ecg": {"path_columns": ["img_path"]}, "ehr": {"exclude_tables": ["note"]}}' \\
      --cache-dir ./my-cache \\
      --lookback-days 180 \\
      --subjects-limit 100

Cache locations:
  - Run outputs: ./.cache/ (in current directory where command runs)
    - ./.cache/embeddings/ (generated embeddings)
    - ./.cache/prompts/ (saved prompts for inspection)
  - HF Models: ~/.cache/huggingface/ (global, shared across projects)
        """
    )
    
    # Required arguments
    p.add_argument(
        '--data',
        required=True,
        help='Path to MEDS parquet file (local or S3)'
    )
    p.add_argument(
        '--hf-token',
        required=True,
        help='HuggingFace API token'
    )
    
    # Optional AWS credentials (uses env vars if not provided)
    p.add_argument(
        '--aws-access-key',
        help='AWS access key ID (optional, uses env if not provided)'
    )
    p.add_argument(
        '--aws-secret-key',
        help='AWS secret access key (optional, uses env if not provided)'
    )
    p.add_argument(
        '--aws-region',
        default='us-east-2',
        help='AWS region (default: us-east-2)'
    )
    
    # Data selection
    p.add_argument(
        '--subject-ids',
        help='Comma-separated list of specific subject IDs to process'
    )
    p.add_argument(
        '--subjects-limit',
        type=int,
        help='Limit number of subjects to process'
    )
    
    # Output (optional, defaults to cache directory)
    p.add_argument(
        '--output',
        help='Output JSONL file (default: <cache-dir>/embeddings/<source>.jsonl)'
    )
    
    # Model configuration (required)
    p.add_argument(
        '--language-model',
        required=True,
        help='HuggingFace model ID for language model (e.g., standardmodelbio/Qwen3-WM-0.6B)'
    )
    p.add_argument(
        '--encoders',
        required=True,
        help='JSON dict mapping modality to encoder model ID (e.g., \'{"ecg": "PKUDigitalHealth/ECGFounder"}\')'
    )
    p.add_argument(
        '--modality-config',
        required=True,
        help='JSON dict mapping modalities to configuration. '
             'For files: \'{"ecg": {"path_columns": ["img_path"]}}\' '
             'For EHR: \'{"ehr": {"include_tables": ["measurement", "condition"]}}\''
    )
    
    # Cache configuration
    p.add_argument(
        '--cache-dir',
        default='./.cache',
        help='Cache directory for embeddings and prompts (default: ./.cache in current dir; models use ~/.cache/huggingface/)'
    )
    
    # Inference configuration
    p.add_argument(
        '--task-prompt',
        help='Custom task prompt for inference'
    )
    p.add_argument(
        '--lookback-days',
        type=int,
        default=365,
        help='Days of patient history to include (default: 365)'
    )
    
    return p.parse_args()


def main():
    """CLI entry point."""
    args = parse_args()
    
    # Parse JSON arguments
    encoders = json.loads(args.encoders)
    
    modality_config = None
    if args.modality_config:
        modality_config = json.loads(args.modality_config)
    
    # Parse subject IDs if provided
    subject_ids = None
    if args.subject_ids:
        subject_ids = [s.strip() for s in args.subject_ids.split(',')]
    
    # Initialize embeddings generator
    generator = MEDSEmbeddingsGenerator(
        data_source=args.data,
        hf_token=args.hf_token,
        modality_config=modality_config,
        aws_access_key_id=args.aws_access_key,
        aws_secret_access_key=args.aws_secret_key,
        aws_region=args.aws_region,
        language_model=args.language_model,
        encoders=encoders,
        cache_dir=args.cache_dir,
        lookback_days=args.lookback_days
    )
    
    # Show configuration and sample prompt
    generator.show_prompt()
    
    # Generate embeddings
    results = generator.generate_embeddings(
        subjects_limit=args.subjects_limit,
        subject_ids=subject_ids,
        output_path=args.output,
        task_prompt=args.task_prompt
    )


if __name__ == '__main__':
    main()

