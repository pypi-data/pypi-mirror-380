"""
MEDS inference utilities for multi-timepoint patient data processing.

This module provides the backend logic for MEDS-based inference,
including data loading, windowing, and batch processing.
"""

from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd
import duckdb
from loguru import logger
from tqdm import tqdm

from .meds_prompt_builder import MEDSPromptBuilder


class MEDSDataLoader:
    """Handles loading MEDS-format data from parquet files."""
    
    @staticmethod
    def _configure_s3_secret(
        con: duckdb.DuckDBPyConnection,
        data_source: str,
        region: str = "us-east-2"
    ) -> None:
        """Configure DuckDB S3 authentication."""
        import os
        
        # Get S3 scope from data source
        if not data_source.startswith("s3://"):
            return
        
        path = data_source[5:]  # Remove "s3://"
        bucket = path.split("/", 1)[0]
        scope = f"s3://{bucket}/"
        
        endpoint = f"s3.{region}.amazonaws.com"
        
        # Try environment variables first
        key = os.getenv("AWS_ACCESS_KEY_ID")
        secret = os.getenv("AWS_SECRET_ACCESS_KEY")
        token = os.getenv("AWS_SESSION_TOKEN")
        profile = os.getenv("AWS_PROFILE")
        
        if key and secret:
            params = [key, secret, region, endpoint, scope]
            if token:
                con.execute(
                    "CREATE OR REPLACE SECRET s3_default "
                    "(TYPE s3, PROVIDER config, KEY_ID ?, SECRET ?, "
                    "SESSION_TOKEN ?, REGION ?, ENDPOINT ?, SCOPE ?)",
                    params + [token]
                )
            else:
                con.execute(
                    "CREATE OR REPLACE SECRET s3_default "
                    "(TYPE s3, PROVIDER config, KEY_ID ?, SECRET ?, "
                    "REGION ?, ENDPOINT ?, SCOPE ?)",
                    params
                )
        elif profile:
            con.execute(
                "CREATE OR REPLACE SECRET s3_default "
                "(TYPE s3, PROVIDER credential_chain, CHAIN 'config', "
                "PROFILE ?, REGION ?, ENDPOINT ?, SCOPE ?)",
                [profile, region, endpoint, scope]
            )
        else:
            # Use credential chain
            con.execute(
                "CREATE OR REPLACE SECRET s3_default "
                "(TYPE s3, PROVIDER credential_chain, "
                "CHAIN 'env;config;process;instance;sso', "
                "REGION ?, ENDPOINT ?, SCOPE ?)",
                [region, endpoint, scope]
            )
    
    @staticmethod
    def load_meds_data(
        data_source: str,
        subject_ids: Optional[List[str]] = None,
        subjects_limit: Optional[int] = None,
        aws_region: str = "us-east-2"
    ) -> pd.DataFrame:
        """
        Load MEDS data from parquet file.
        
        Args:
            data_source: Path to parquet file (local or S3)
            subject_ids: Optional list of specific subject IDs to load
            subjects_limit: Optional limit on number of subjects
            aws_region: AWS region for S3 access
        
        Returns:
            DataFrame with MEDS format data
        """
        con = duckdb.connect()
        
        # Configure S3 if needed
        if data_source.startswith("s3://"):
            con.execute("INSTALL httpfs; LOAD httpfs;")
            MEDSDataLoader._configure_s3_secret(con, data_source, aws_region)
        
        # Build query with filters
        where_clauses = []
        if subject_ids:
            ids_str = "', '".join(subject_ids)
            where_clauses.append(f"subject_id IN ('{ids_str}')")
        
        where_sql = (
            f"WHERE {' AND '.join(where_clauses)}"
            if where_clauses
            else ""
        )
        
        # Get subjects
        subject_query = f"""
            SELECT DISTINCT subject_id
            FROM read_parquet('{data_source}')
            {where_sql}
            ORDER BY subject_id
        """
        
        if subjects_limit:
            subject_query += f" LIMIT {subjects_limit}"
        
        subjects = con.execute(subject_query).fetchdf()
        subject_list = subjects['subject_id'].tolist()
        
        logger.info(
            f"Loading {len(subject_list)} subjects from {data_source}"
        )
        
        # Load full data for these subjects
        con.register(
            'subjects_list',
            pd.DataFrame({'subject_id': subject_list})
        )
        
        data_query = f"""
            SELECT *
            FROM read_parquet('{data_source}')
            WHERE subject_id IN (SELECT subject_id FROM subjects_list)
            ORDER BY subject_id, time
        """
        
        df = con.execute(data_query).fetchdf()
        
        # Ensure time is datetime
        if 'time' in df.columns:
            df['time'] = pd.to_datetime(df['time'], errors='coerce')
        
        con.close()
        
        logger.info(
            f"Loaded {len(df)} events for {len(subject_list)} subjects"
        )
        return df
    
    @staticmethod
    def build_inference_window(
        patient_df: pd.DataFrame,
        window_end_time: Optional[pd.Timestamp] = None,
        lookback_days: Optional[int] = 365
    ) -> pd.DataFrame:
        """
        Build inference window for a patient.
        
        Args:
            patient_df: All events for a patient
            window_end_time: End time for window (default: latest event)
            lookback_days: How many days of history to include
        
        Returns:
            DataFrame with events in the inference window
        """
        if window_end_time is None:
            window_end_time = patient_df['time'].max()
        
        if lookback_days:
            window_start = window_end_time - pd.Timedelta(days=lookback_days)
            window_df = patient_df[
                (patient_df['time'] >= window_start) &
                (patient_df['time'] <= window_end_time)
            ]
        else:
            window_df = patient_df[patient_df['time'] <= window_end_time]
        
        return window_df


class MEDSModalityExtractor:
    """Extracts modality file paths from MEDS events."""
    
    @staticmethod
    def extract_modality_paths(
        events_df: pd.DataFrame,
        modality_config: Optional[Dict[str, Dict]] = None,
        validate_columns: bool = True
    ) -> Dict[str, List[str]]:
        """
        Extract modality file paths from events using config.
        
        Args:
            events_df: DataFrame with MEDS events
            modality_config: Dict mapping modalities to column specs
                Example: {
                    "ecg": {"path_columns": ["img_path", "ecg_path"]},
                    "ct": {"path_columns": ["ct_path"]}
                }
            validate_columns: If True, error if specified columns don't exist
        
        Returns:
            Dict mapping modality names to file paths
        """
        if modality_config is None:
            # Default config
            modality_config = {
                "ecg": {"path_columns": ["img_path", "ecg_path", "file_path"]},
                "ct": {"path_columns": ["ct_path"]}
            }
        
        modality_paths = {}
        available_cols = set(events_df.columns)
        
        # Extract paths for each configured modality
        for modality, config in modality_config.items():
            path_columns = config.get("path_columns", [])
            if not path_columns:
                continue
            
            # Validate columns exist if requested
            if validate_columns:
                missing_cols = [c for c in path_columns if c not in available_cols]
                if missing_cols:
                    raise ValueError(
                        f"Modality '{modality}' specifies columns that don't exist: "
                        f"{missing_cols}. Available columns: {sorted(available_cols)}"
                    )
            
            # Collect paths from all specified columns
            all_paths = []
            for col in path_columns:
                if col in events_df.columns:
                    paths = events_df[col].dropna().astype(str).tolist()
                    all_paths.extend(paths)
            
            if all_paths:
                # Deduplicate while preserving order
                modality_paths[modality] = list(dict.fromkeys(all_paths))
        
        return modality_paths
    
    @staticmethod
    def prepare_modalities_inputs(
        modality_paths: Dict[str, List[str]]
    ) -> Dict[str, Dict[str, any]]:
        """
        Convert modality paths to inference pipeline format.
        
        Args:
            modality_paths: Dict mapping modality to file paths
        
        Returns:
            Dict formatted for inference pipeline
        """
        modalities_inputs = {}
        
        if 'ecg' in modality_paths and modality_paths['ecg']:
            first_path = Path(modality_paths['ecg'][0])
            modalities_inputs['ecg'] = {
                'files': [Path(p).name for p in modality_paths['ecg']],
                'data_dir': str(first_path.parent)
            }
        
        # TODO: Add CT, MRI support
        
        return modalities_inputs


class MEDSBatchProcessor:
    """Processes batches of MEDS data for inference."""
    
    @staticmethod
    def process_batch_inference(
        df: pd.DataFrame,
        pipe: any,  # MultiModalMedicalInference instance
        prompt_builder: MEDSPromptBuilder,
        modality_config: Optional[Dict[str, Dict]] = None,
        out_path: Optional[str] = None,
        task_prompt: Optional[str] = None,
        lookback_days: int = 365
    ) -> List[Dict]:
        """
        Run inference on all subjects in MEDS DataFrame.
        
        Args:
            df: MEDS-format DataFrame
            pipe: Inference pipeline instance
            prompt_builder: MEDS prompt builder
            modality_config: Dict mapping modalities to column names
            out_path: Optional path to save results (JSONL)
            task_prompt: Optional custom task prompt
            lookback_days: Days of history to include in window
        
        Returns:
            List of prediction results
        """
        results = []
        subjects = df.groupby('subject_id')
        
        logger.info(f"Running inference on {len(subjects)} subjects")
        
        for subject_id, patient_df in tqdm(
            subjects,
            desc="Processing subjects"
        ):
            result = MEDSBatchProcessor._process_single_subject(
                subject_id=str(subject_id),
                patient_df=patient_df,
                pipe=pipe,
                prompt_builder=prompt_builder,
                modality_config=modality_config,
                task_prompt=task_prompt,
                lookback_days=lookback_days
            )
            results.append(result)
            
            # Save incrementally if output path provided
            if out_path:
                output_path = Path(out_path)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                with output_path.open('a') as f:
                    import json
                    f.write(json.dumps(result, default=str) + '\n')
        
        # Summary stats
        successful = sum(1 for r in results if r['status'] == 'success')
        logger.info(
            f"Inference complete: {successful}/{len(results)} successful"
        )
        
        return results
    
    @staticmethod
    def _process_single_subject(
        subject_id: str,
        patient_df: pd.DataFrame,
        pipe: any,
        prompt_builder: MEDSPromptBuilder,
        modality_config: Optional[Dict[str, Dict]],
        task_prompt: Optional[str],
        lookback_days: int
    ) -> Dict:
        """Process a single subject and return predictions."""
        # Build inference window
        window_df = MEDSDataLoader.build_inference_window(
            patient_df,
            window_end_time=None,
            lookback_days=lookback_days
        )
        
        if window_df.empty:
            logger.warning(f"No data in window for subject {subject_id}")
            return {
                'subject_id': subject_id,
                'status': 'no_data',
                'predictions': None
            }
        
        # Extract modality paths using config
        modality_paths = MEDSModalityExtractor.extract_modality_paths(
            window_df,
            modality_config=modality_config
        )
        
        # Build prompt
        time_span = (window_df['time'].min(), window_df['time'].max())
        prompt = prompt_builder.build_prompt(
            events_df=window_df,
            modality_paths=modality_paths if modality_paths else None,
            time_span=time_span,
            include_time_span=True
        )
        
        if not prompt:
            logger.warning(f"Failed to build prompt for {subject_id}")
            return {
                'subject_id': subject_id,
                'status': 'prompt_failed',
                'predictions': None
            }
        
        # Prepare modalities inputs
        modalities_inputs = MEDSModalityExtractor.prepare_modalities_inputs(
            modality_paths
        )
        
        # Run inference (skip prompt building since we already built it)
        try:
            preds = pipe.predict(
                clinical_notes=prompt,
                modalities_inputs=modalities_inputs,
                task_prompt=task_prompt,
                use_modalities={'ecg': bool(modality_paths.get('ecg'))},
                skip_prompt_building=True  # We already built MEDS prompt
            )
            
            return {
                'subject_id': subject_id,
                'status': 'success',
                'time_span': {
                    'start': str(time_span[0]),
                    'end': str(time_span[1])
                },
                'modalities': list(modality_paths.keys()),
                'predictions': preds.get('predictions', {}),
                'prompt_length': len(prompt)
            }
        
        except Exception as e:
            logger.error(f"Inference failed for {subject_id}: {e}")
            return {
                'subject_id': subject_id,
                'status': 'inference_failed',
                'error': str(e),
                'predictions': None
            }
