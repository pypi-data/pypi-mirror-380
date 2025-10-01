"""
Unified MEDS prompt builder for training and inference.

This module provides the core prompt generation logic for MEDS-format data.
Used by both training dataset creation and live inference.
"""

from typing import Any, Dict, List, Optional
import pandas as pd

from .modality_tokens import ModalityTokenGenerator


class MEDSPromptBuilder:
    """
    Builds prompts from MEDS-format data for the fusion model.
    
    Handles:
    - Multi-timepoint patient histories
    - Multiple modalities (ECG, CT, MRI, etc.)
    - Structured event formatting
    - Modality token generation
    """
    
    # Table name to semantic tag mapping
    CATEGORY_MAPPING = {
        "person": "demographics",
        "condition": "conditions",
        "measurement": "measurements",
        "observation": "observations",
        "note": "notes",
        "drug_exposure": "drugs",
        "procedure": "procedures",
        "death": "death",
    }
    
    def __init__(
        self,
        excluded_tags: Optional[set] = None,
        ehr_config: Optional[Dict] = None
    ):
        """
        Initialize prompt builder.
        
        Args:
            excluded_tags: Set of tags to exclude from prompts
            ehr_config: Configuration for EHR data filtering
                {
                    "include_tables": ["person", "measurement"],
                    "exclude_tables": ["note"],
                    "include_codes": ["LOINC/8867-4"],
                    "exclude_codes": ["SNOMED/noise_123"]
                }
        """
        self.excluded_tags = excluded_tags or set()
        self.ehr_config = ehr_config or {}
    
    def format_events(
        self,
        events_df: pd.DataFrame,
        is_prediction_target: bool = False
    ) -> str:
        """
        Convert MEDS events DataFrame to structured text.
        
        Args:
            events_df: DataFrame with MEDS format events
            is_prediction_target: If True, only include prediction-relevant tags
        
        Returns:
            Formatted text with tagged sections
        """
        if events_df is None or events_df.empty:
            return ""
        
        # Apply EHR config filters first (if configured)
        if self.ehr_config:
            # Filter by tables
            include_tables = self.ehr_config.get("include_tables")
            exclude_tables = self.ehr_config.get("exclude_tables", [])
            
            if include_tables is not None:
                events_df = events_df[events_df['table'].isin(include_tables)]
            if exclude_tables:
                events_df = events_df[~events_df['table'].isin(exclude_tables)]
            
            # Filter by codes
            include_codes = self.ehr_config.get("include_codes")
            exclude_codes = self.ehr_config.get("exclude_codes", [])
            
            if include_codes is not None:
                events_df = events_df[events_df['code'].isin(include_codes)]
            if exclude_codes:
                events_df = events_df[~events_df['code'].isin(exclude_codes)]
        
        # Map table names to semantic tags
        events_df = events_df.copy()
        events_df['tag'] = events_df['table'].map(self.CATEGORY_MAPPING)
        
        # Filter to relevant tags
        if is_prediction_target:
            allowed_tags = ["conditions", "measurements", "death"]
        else:
            allowed_tags = [
                t for t in self.CATEGORY_MAPPING.values()
                if t not in self.excluded_tags
            ]
        
        events_df = events_df[events_df['tag'].isin(allowed_tags)]
        if events_df.empty:
            return ""
        
        output_parts: Dict[str, str] = {}
        
        # Process each tag separately
        for tag in events_df['tag'].unique():
            if pd.isna(tag):
                continue
            
            tag_events = events_df[events_df['tag'] == tag]
            formatted_lines = self._format_tag_events(tag, tag_events)
            
            if formatted_lines:
                output_parts[tag] = (
                    f"<{tag}>\n" +
                    "\n".join(formatted_lines) +
                    f"\n</{tag}>"
                )
        
        return "\n".join(output_parts.values())
    
    def _format_tag_events(
        self,
        tag: str,
        tag_events: pd.DataFrame
    ) -> List[str]:
        """Format events for a specific tag."""
        if tag_events.empty:
            return []
        
        # Observations: just show unique codes
        if tag == "observations":
            unique_codes = tag_events['code'].dropna().unique()
            return list(unique_codes.astype(str))
        
        # Other tags: format with values
        return self._format_valued_events(tag, tag_events)
    
    def _format_valued_events(
        self,
        tag: str,
        events: pd.DataFrame
    ) -> List[str]:
        """Format events that have numeric or text values."""
        # Vectorized value formatting
        formatted_values = pd.Series('', index=events.index)
        
        # Format numeric values
        numeric_mask = events['numeric_value'].notna()
        if numeric_mask.any():
            nums = events.loc[numeric_mask, 'numeric_value']
            formatted_values.loc[numeric_mask] = nums.round(2).astype(str)
        
        # Format text values (where no numeric)
        text_mask = events['text_value'].notna()
        if text_mask.any():
            text_only = text_mask & ~numeric_mask
            if text_only.any():
                texts = events.loc[text_only, 'text_value']
                formatted_values.loc[text_only] = texts.astype(str)
        
        # Keep only events with values
        has_value = formatted_values != ''
        if not has_value.any():
            return []
        
        valid_events = events[has_value].copy()
        valid_events['formatted_value'] = formatted_values[has_value]
        
        # Group by code and format
        lines = []
        for code in valid_events['code'].unique():
            if pd.isna(code):
                continue
            
            code_events = valid_events[valid_events['code'] == code]
            line = self._format_code_events(tag, code, code_events)
            if line:
                lines.append(line)
        
        # Deduplicate while preserving order
        return list(dict.fromkeys(lines))
    
    def _format_code_events(
        self,
        tag: str,
        code: str,
        events: pd.DataFrame
    ) -> str:
        """Format all events for a specific code."""
        # Special case: birth date
        if code == "MEDS_BIRTH" and tag == "demographics":
            birth_date = events['time'].iloc[0].strftime("%Y-%m-%d")
            return f"Birth: {birth_date}"
        
        # Get last 5 values (chronological order)
        values = events['formatted_value'].tail(5).tolist()
        if not values:
            return str(code)
        
        # Add unit if available
        units = events['unit'].dropna()
        unit_str = f" ({units.iloc[-1]})" if len(units) > 0 else ""
        
        return f"{code}{unit_str}: {', '.join(values)}"
    
    def build_prompt(
        self,
        events_df: pd.DataFrame,
        modality_paths: Optional[Dict[str, List[str]]] = None,
        time_span: Optional[tuple] = None,
        include_time_span: bool = True
    ) -> str:
        """
        Build a complete prompt from MEDS events.
        
        Args:
            events_df: DataFrame with MEDS format events
            modality_paths: Dict mapping modality names to file paths
                           e.g., {"ecg": ["path1.h5", "path2.h5"]}
            time_span: Optional (start, end) timestamps for time span header
            include_time_span: Whether to include time span in prompt
        
        Returns:
            Complete prompt string with modality tokens and formatted events
        """
        # Format clinical events
        clinical_content = self.format_events(
            events_df,
            is_prediction_target=False
        )
        
        if not clinical_content:
            return ""
        
        prompt_parts = []
        
        # Add modality tokens if paths provided
        if modality_paths:
            for modality, paths in sorted(modality_paths.items()):
                if paths:
                    tokens = ModalityTokenGenerator.generate_tokens(
                        modality=modality,
                        count=len(paths),
                        use_pipes=True
                    )
                    prompt_parts.append(tokens)
        
        # Add time span if available
        if include_time_span and time_span:
            start, end = time_span
            prompt_parts.append(f"Time span: [{start} - {end}]")
        
        # Add clinical content
        prompt_parts.append(clinical_content)
        
        return "\n\n".join(prompt_parts)
