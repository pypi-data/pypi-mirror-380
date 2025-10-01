#!/usr/bin/env python3
"""
MEDS conversational dataset builder with S3 streaming and multimodal support.

Optimized for performance with:
- DuckDB S3 streaming (avoid downloading entire files)
- Vectorized pandas operations (2x speedup)
- Multiprocessing for parallel subject processing
"""

import json
import multiprocessing as mp
import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

import duckdb
import pandas as pd
from tqdm import tqdm

from utils.modality_tokens import ModalityTokenGenerator
from utils.meds_prompt_builder import MEDSPromptBuilder


@dataclass
class DatasetConfig:
    """Configuration for dataset building."""
    
    data_source: str
    output_dir: Path
    subjects_per_chunk: int = 4000
    subjects_limit: int = 0
    n_last_visits: int = 5
    num_workers: Optional[int] = None
    aws_region: str = "us-east-2"
    
    # Column names to load from parquet
    columns: List[str] = None
    
    def __post_init__(self):
        if self.columns is None:
            self.columns = [
                "subject_id", "visit_id", "time", "table", "code",
                "numeric_value", "text_value", "unit",
                "img_path", "ct_path", "file_path",
            ]
        if self.num_workers is None:
            self.num_workers = max(1, mp.cpu_count())


# EventFormatter is now replaced by MEDSPromptBuilder from utils


class ModalityExtractor:
    """Extracts modality file paths and generates tokens."""
    
    # Column names that contain file paths
    PATH_COLUMNS = ("img_path", "ct_path", "file_path")
    
    def extract_paths(self, events_df: pd.DataFrame) -> List[str]:
        """Extract all file paths from events."""
        if events_df is None or events_df.empty:
            return []
        
        paths = []
        for col in self.PATH_COLUMNS:
            if col in events_df.columns:
                col_paths = events_df[col].dropna().astype(str).tolist()
                paths.extend(col_paths)
        
        # Deduplicate while preserving order
        return list(dict.fromkeys(paths))
    
    def generate_tokens(self, num_files: int) -> str:
        """
        Generate modality tokens using shared generator.
        
        Currently assumes ECG modality (m1).
        TODO: Support multiple modality types based on file paths.
        """
        if num_files <= 0:
            return ""
        
        # Use shared token generator for consistency with inference
        return ModalityTokenGenerator.generate_tokens(
            modality="ecg",
            count=num_files,
            use_pipes=True
        )


class ConversationBuilder:
    """Builds conversations from patient data."""
    
    def __init__(
        self,
        prompt_builder: MEDSPromptBuilder,
        modality_extractor: ModalityExtractor,
        n_last_visits: int = 5
    ):
        self.prompt_builder = prompt_builder
        self.modality_extractor = modality_extractor
        self.n_last_visits = n_last_visits
    
    def build_conversations(
        self,
        patient_df: pd.DataFrame
    ) -> List[Dict[str, Any]]:
        """Build all conversations for a single patient."""
        conversations = []
        emitted_windows: Set[str] = set()
        
        # Build visit-based prediction conversations
        visit_conversations = self._build_visit_predictions(
            patient_df,
            emitted_windows
        )
        conversations.extend(visit_conversations)
        
        # Build death prediction conversation if applicable
        death_conversation = self._build_death_prediction(
            patient_df,
            emitted_windows
        )
        if death_conversation:
            conversations.append(death_conversation)
        
        return conversations
    
    def _build_visit_predictions(
        self,
        patient_df: pd.DataFrame,
        emitted_windows: Set[str]
    ) -> List[Dict[str, Any]]:
        """Build conversations predicting future visits."""
        conversations = []
        
        # Get valid visits
        valid_visits = patient_df.dropna(subset=["visit_id"])
        if valid_visits.empty or len(valid_visits['visit_id'].unique()) < 2:
            return conversations
        
        # Order visits chronologically
        visit_bounds = (
            valid_visits.groupby("visit_id")["time"]
            .agg(start="min", end="max")
            .sort_values("start")
        )
        ordered_visits = visit_bounds.index.tolist()
        
        # Demographics (person table rows)
        person_rows = patient_df[patient_df["table"] == "person"]
        
        # Create conversation for each visit (predicting from prior visits)
        for i in range(1, len(ordered_visits)):
            conversation = self._build_single_visit_prediction(
                patient_df=patient_df,
                person_rows=person_rows,
                visit_bounds=visit_bounds,
                ordered_visits=ordered_visits,
                prediction_index=i,
                emitted_windows=emitted_windows
            )
            if conversation:
                conversations.append(conversation)
        
        return conversations
    
    def _build_single_visit_prediction(
        self,
        patient_df: pd.DataFrame,
        person_rows: pd.DataFrame,
        visit_bounds: pd.DataFrame,
        ordered_visits: List[Any],
        prediction_index: int,
        emitted_windows: Set[str]
    ) -> Optional[Dict[str, Any]]:
        """Build a conversation predicting a single visit."""
        prediction_visit_id = ordered_visits[prediction_index]
        prediction_start = visit_bounds.loc[prediction_visit_id, "start"]
        
        # Get context visits (last N visits before prediction)
        start_idx = (
            max(0, prediction_index - self.n_last_visits)
            if self.n_last_visits
            else 0
        )
        context_visit_ids = ordered_visits[start_idx:prediction_index]
        if not context_visit_ids:
            return None
        
        # Extract history events
        context_mask = patient_df["visit_id"].isin(context_visit_ids)
        all_context = patient_df[context_mask]
        clinical_history = all_context[
            all_context["time"] < prediction_start
        ]
        
        if clinical_history.empty:
            return None
        
        history_end = clinical_history["time"].max()
        
        # Require at least 1 day gap
        if (prediction_start - history_end) <= pd.Timedelta(days=1):
            return None
        
        # Combine demographics + clinical history
        demographics = person_rows[person_rows["time"] < prediction_start]
        history_df = pd.concat([demographics, clinical_history])
        history_df = history_df.sort_values(by="time").drop_duplicates()
        
        # Extract target events (what we're predicting)
        current_visit = patient_df[
            patient_df["visit_id"] == prediction_visit_id
        ]
        if current_visit.empty:
            return None
        
        prediction_end = current_visit["time"].max()
        target_df = patient_df[
            (patient_df["time"] > history_end) &
            (patient_df["time"] <= prediction_end)
        ]
        
        if target_df.empty:
            return None
        
        # Require both conditions and interventions in history
        if not self._has_required_events(history_df):
            return None
        
        # Check for duplicate window
        window_key = (
            f"{clinical_history['time'].min()}|{history_end}|"
            f"{prediction_start}|{prediction_end}"
        )
        if window_key in emitted_windows:
            return None
        emitted_windows.add(window_key)
        
        # Build the conversation
        return self._create_conversation(
            history_df=history_df,
            target_df=target_df,
            history_start=clinical_history["time"].min(),
            history_end=history_end,
            prediction_time=prediction_start,
            full_history_df=patient_df[
                (patient_df["time"] >= clinical_history["time"].min()) &
                (patient_df["time"] < prediction_start)
            ]
        )
    
    def _build_death_prediction(
        self,
        patient_df: pd.DataFrame,
        emitted_windows: Set[str]
    ) -> Optional[Dict[str, Any]]:
        """Build a conversation predicting patient death."""
        death_df = patient_df[patient_df["table"] == "death"]
        if death_df.empty:
            return None
        
        death_time = death_df["time"].iloc[0]
        history_df = patient_df[patient_df["time"] < death_time]
        clinical_history = history_df.dropna(subset=["visit_id"])
        
        # Limit to last N visits if configured
        if self.n_last_visits and not clinical_history.empty:
            visit_times = (
                clinical_history.groupby("visit_id")["time"]
                .min()
                .sort_values()
            )
            last_visits = visit_times.index[-self.n_last_visits:]
            clinical_history = clinical_history[
                clinical_history["visit_id"].isin(last_visits)
            ]
        
        if clinical_history.empty:
            return None
        
        history_end = clinical_history["time"].max()
        
        # Require at least 1 day gap
        if (death_time - history_end) <= pd.Timedelta(days=1):
            return None
        
        # Combine demographics + clinical history
        demographics = history_df[history_df["table"] == "person"]
        history_df = pd.concat([demographics, clinical_history])
        history_df = history_df.sort_values(by="time").drop_duplicates()
        
        # Check for duplicate window
        window_key = (
            f"{clinical_history['time'].min()}|{history_end}|"
            f"{death_time}|death"
        )
        if window_key in emitted_windows:
            return None
        emitted_windows.add(window_key)
        
        # Build the conversation
        return self._create_conversation(
            history_df=history_df,
            target_df=death_df,
            history_start=clinical_history["time"].min(),
            history_end=history_end,
            prediction_time=death_time,
            full_history_df=patient_df[
                (patient_df["time"] >= clinical_history["time"].min()) &
                (patient_df["time"] < death_time)
            ]
        )
    
    def _has_required_events(self, history_df: pd.DataFrame) -> bool:
        """Check if history has both conditions and interventions."""
        tables = set(history_df["table"].unique())
        
        condition_tables = {"condition", "measurement"}
        intervention_tables = {"drug_exposure", "procedure"}
        
        has_conditions = bool(tables & condition_tables)
        has_interventions = bool(tables & intervention_tables)
        
        return has_conditions and has_interventions
    
    def _create_conversation(
        self,
        history_df: pd.DataFrame,
        target_df: pd.DataFrame,
        history_start: Any,
        history_end: Any,
        prediction_time: Any,
        full_history_df: pd.DataFrame
    ) -> Optional[Dict[str, Any]]:
        """Create a single conversation dict."""
        # Extract modality paths
        modality_paths_list = self.modality_extractor.extract_paths(
            full_history_df
        )
        modality_paths_dict = (
            {"ecg": modality_paths_list} if modality_paths_list else None
        )
        
        # Build user prompt using MEDSPromptBuilder
        user_prompt = self.prompt_builder.build_prompt(
            events_df=history_df,
            modality_paths=modality_paths_dict,
            time_span=(history_start, history_end),
            include_time_span=True
        )
        
        if not user_prompt:
            return None
        
        # Format target events for assistant response
        assistant_content = self.prompt_builder.format_events(
            target_df,
            is_prediction_target=True
        )
        
        if not assistant_content:
            return None
        
        assistant_response = (
            f"Current time: [{prediction_time}]\n\n"
            f"{assistant_content}"
        )
        
        return {
            "messages": [
                {"role": "user", "content": user_prompt},
                {"role": "assistant", "content": assistant_response},
            ],
            "embeddings": {"m1": modality_paths_list} if modality_paths_list else {},
        }


class MEDSDatasetBuilder:
    """Main orchestrator for building MEDS conversational datasets."""
    
    def __init__(self, config: DatasetConfig):
        self.config = config
        self.con: Optional[duckdb.DuckDBPyConnection] = None
        
        # Initialize components
        self.prompt_builder = MEDSPromptBuilder()
        self.modality_extractor = ModalityExtractor()
    
    def build(self) -> None:
        """Main build process."""
        self.config.output_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"Building dataset from: {self.config.data_source}")
        print(f"Output directory: {self.config.output_dir}")
        print(f"Subjects limit: {self.config.subjects_limit}")
        print(f"Workers: {self.config.num_workers}")
        
        start_time = time.perf_counter()
        
        # Setup DuckDB with S3 support
        self._setup_duckdb()
        
        # Get subjects to process
        subjects = self._get_subjects()
        print(f"Found {len(subjects)} subjects to process")
        
        # Process in chunks
        self._process_chunks(subjects)
        
        # Cleanup
        if self.con:
            self.con.close()
        
        elapsed = time.perf_counter() - start_time
        print(f"Total runtime: {elapsed:.2f}s ({elapsed/60:.2f} min)")
        print(f"Processed {len(subjects)} subjects")
    
    def _setup_duckdb(self) -> None:
        """Initialize DuckDB connection with S3 support."""
        print("Initializing DuckDB with S3 support...")
        self.con = duckdb.connect()
        self.con.execute("INSTALL httpfs; LOAD httpfs;")
        
        # Configure S3 authentication
        self._configure_s3_secret()
    
    def _configure_s3_secret(self) -> None:
        """Configure DuckDB S3 authentication."""
        endpoint = f"s3.{self.config.aws_region}.amazonaws.com"
        scope = self._get_s3_scope()
        
        # Try environment variables first
        key = os.getenv("AWS_ACCESS_KEY_ID")
        secret = os.getenv("AWS_SECRET_ACCESS_KEY")
        token = os.getenv("AWS_SESSION_TOKEN")
        profile = os.getenv("AWS_PROFILE")
        
        if key and secret:
            params = [key, secret, self.config.aws_region, endpoint, scope]
            if token:
                self.con.execute(
                    "CREATE OR REPLACE SECRET s3_default "
                    "(TYPE s3, PROVIDER config, KEY_ID ?, SECRET ?, "
                    "SESSION_TOKEN ?, REGION ?, ENDPOINT ?, SCOPE ?)",
                    params + [token]
                )
            else:
                self.con.execute(
                    "CREATE OR REPLACE SECRET s3_default "
                    "(TYPE s3, PROVIDER config, KEY_ID ?, SECRET ?, "
                    "REGION ?, ENDPOINT ?, SCOPE ?)",
                    params
                )
        elif profile:
            self.con.execute(
                "CREATE OR REPLACE SECRET s3_default "
                "(TYPE s3, PROVIDER credential_chain, CHAIN 'config', "
                "PROFILE ?, REGION ?, ENDPOINT ?, SCOPE ?)",
                [profile, self.config.aws_region, endpoint, scope]
            )
        else:
            # Use credential chain
            self.con.execute(
                "CREATE OR REPLACE SECRET s3_default "
                "(TYPE s3, PROVIDER credential_chain, "
                "CHAIN 'env;config;process;instance;sso', "
                "REGION ?, ENDPOINT ?, SCOPE ?)",
                [self.config.aws_region, endpoint, scope]
            )
    
    def _get_s3_scope(self) -> str:
        """Get S3 bucket scope from data source."""
        if not self.config.data_source.startswith("s3://"):
            return ""
        path = self.config.data_source[5:]  # Remove "s3://"
        bucket = path.split("/", 1)[0]
        return f"s3://{bucket}/"
    
    def _get_subjects(self) -> List[str]:
        """Query list of subject IDs to process."""
        print("Querying subject list from S3...")
        
        limit_clause = (
            f"LIMIT {self.config.subjects_limit}"
            if self.config.subjects_limit > 0
            else ""
        )
        
        query = f"""
            SELECT DISTINCT "subject_id"
            FROM read_parquet('{self.config.data_source}')
            WHERE "subject_id" IS NOT NULL
            ORDER BY "subject_id"
            {limit_clause}
        """
        
        results = self.con.execute(query).fetchall()
        return [r[0] for r in results]
    
    def _process_chunks(self, subjects: List[str]) -> None:
        """Process subjects in chunks."""
        chunk_size = self.config.subjects_per_chunk
        
        for chunk_idx, offset in enumerate(
            tqdm(
                range(0, len(subjects), chunk_size),
                desc="Saving chunks"
            )
        ):
            batch = subjects[offset:offset + chunk_size]
            
            # Load data for this batch
            df_chunk = self._load_batch_data(batch)
            
            # Build conversations
            conversations = self._build_conversations(df_chunk)
            
            # Save to file
            output_file = (
                self.config.output_dir /
                f"prediction_dataset_chunk_{chunk_idx:03d}.json"
            )
            with output_file.open("w") as f:
                json.dump(conversations, f, indent=2)
    
    def _load_batch_data(self, subjects: List[str]) -> pd.DataFrame:
        """Load data for a batch of subjects from S3."""
        # Register subjects as temp table
        subjects_df = pd.DataFrame({"subject_id": subjects})
        self.con.register("batch_subjects", subjects_df)
        
        # Determine available columns
        schema_df = self.con.execute(
            f"SELECT * FROM read_parquet('{self.config.data_source}') "
            "LIMIT 0"
        ).fetchdf()
        available_cols = set(schema_df.columns)
        
        # Build SELECT clause
        present_cols = [
            c for c in self.config.columns
            if c != "time" and c in available_cols
        ]
        select_parts = [f'"{c}"' for c in present_cols]
        
        if "time" in available_cols:
            select_parts.append('CAST("time" AS TIMESTAMP) AS time')
        
        select_clause = ", ".join(select_parts)
        order_clause = (
            'ORDER BY "subject_id", "time"'
            if "time" in available_cols
            else 'ORDER BY "subject_id"'
        )
        
        # Stream data from S3
        query = f"""
            SELECT {select_clause}
            FROM read_parquet('{self.config.data_source}')
            WHERE "subject_id" IN (SELECT subject_id FROM batch_subjects)
            {order_clause}
        """
        
        df = self.con.execute(query).fetchdf()
        
        # Ensure time is datetime
        if "time" in df.columns:
            df["time"] = pd.to_datetime(df["time"], errors="coerce")
        
        # Cleanup
        self.con.unregister("batch_subjects")
        
        return df
    
    def _build_conversations(
        self,
        df: pd.DataFrame
    ) -> List[Dict[str, Any]]:
        """Build conversations for all subjects in DataFrame."""
        # Partition by subject
        subjects = [
            patient_df
            for _, patient_df in df.groupby("subject_id", sort=True)
        ]
        
        # Build conversations in parallel or sequential
        if self.config.num_workers and self.config.num_workers > 1:
            conversations = self._build_parallel(subjects)
        else:
            conversations = self._build_sequential(subjects)
        
        return conversations
    
    def _build_sequential(
        self,
        subjects: List[pd.DataFrame]
    ) -> List[Dict[str, Any]]:
        """Build conversations sequentially."""
        builder = ConversationBuilder(
            prompt_builder=self.prompt_builder,
            modality_extractor=self.modality_extractor,
            n_last_visits=self.config.n_last_visits
        )
        
        all_conversations = []
        for patient_df in tqdm(subjects, desc="Processing subjects"):
            conversations = builder.build_conversations(patient_df)
            all_conversations.extend(conversations)
        
        return all_conversations
    
    def _build_parallel(
        self,
        subjects: List[pd.DataFrame]
    ) -> List[Dict[str, Any]]:
        """Build conversations in parallel using multiprocessing."""
        # Get multiprocessing context
        try:
            ctx = mp.get_context("fork")
        except ValueError:
            ctx = mp.get_context("spawn")
        
        workers = min(self.config.num_workers, mp.cpu_count())
        
        # Process in parallel
        with ctx.Pool(processes=workers) as pool:
            args = (
                (
                    patient_df,
                    self.config.n_last_visits,
                    self.prompt_builder,
                    self.modality_extractor
                )
                for patient_df in subjects
            )
            
            results = list(
                tqdm(
                    pool.imap_unordered(_build_subject_worker, args),
                    total=len(subjects),
                    desc="Processing subjects"
                )
            )
        
        # Flatten results
        all_conversations = []
        for conversations in results:
            all_conversations.extend(conversations)
        
        return all_conversations


def _build_subject_worker(args) -> List[Dict[str, Any]]:
    """Worker function for multiprocessing."""
    patient_df, n_last_visits, prompt_builder, modality_extractor = args
    
    builder = ConversationBuilder(
        prompt_builder=prompt_builder,
        modality_extractor=modality_extractor,
        n_last_visits=n_last_visits
    )
    
    return builder.build_conversations(patient_df)


def main():
    """CLI entry point."""
    config = DatasetConfig(
        data_source=os.getenv(
            "DATA_SOURCE",
            "s3://smb-dev-scratch/data.parquet"
        ),
        output_dir=Path(
            os.getenv("OUT_DIR", "data/mmeds/prediction_dataset_chunks")
        ),
        subjects_per_chunk=int(os.getenv("SUBJECTS_PER_CHUNK", "4000")),
        subjects_limit=int(os.getenv("SUBJECTS_LIMIT", "0")),
        n_last_visits=int(os.getenv("N_LAST_VISITS", "5")),
        num_workers=int(
            os.getenv("NUM_WORKERS", str(max(1, mp.cpu_count())))
        ),
        aws_region=(
            os.getenv("AWS_REGION") or
            os.getenv("AWS_DEFAULT_REGION") or
            "us-east-2"
        ),
    )
    
    builder = MEDSDatasetBuilder(config)
    builder.build()


if __name__ == "__main__":
    main()
