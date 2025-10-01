"""Typed schemas and lightweight validation for CLI/runtime configs."""

from typing import List, Optional, Dict

# Support both Pydantic v1 and v2
try:  # v2 path
    from pydantic import BaseModel, model_validator  # type: ignore
    try:
        # RootModel is available only in v2.
        from pydantic import RootModel  # type: ignore
    except Exception:
        RootModel = None  # type: ignore
    _PYDANTIC_V2 = True
except Exception:
    try:  # v1 fallback
        from pydantic import BaseModel, root_validator  # type: ignore
        _PYDANTIC_V2 = False
    except Exception as e:  # pragma: no cover - explicit error to guide install
        raise ImportError(
            "pydantic is required for --modalities validation. Install via `uv add pydantic`."
        ) from e


class ECGConfig(BaseModel):
    """Configuration for ECG modality sourced from a CSV column."""

    path_column: str


class EHRConfig(BaseModel):
    """Configuration for EHR text fields folded into the prompt."""

    columns: List[str] = []


class CTConfig(BaseModel):
    """Configuration for CT modality (reserved for future use)."""

    path_column: Optional[str] = None


class ModalitiesConfig(BaseModel):
    """Top-level modalities mapping for batch inference.

    Example JSON:
        {
          "ecg": {"path_column": "local_dat_path"},
          "ehr": {"columns": ["age", "gender", "diagnosis"]}
        }
    """

    ecg: Optional[ECGConfig] = None
    ehr: Optional[EHRConfig] = None
    ct: Optional[CTConfig] = None

    # Cross-version validation: ensure at least one modality is provided
    if _PYDANTIC_V2:
        @model_validator(mode="after")  # type: ignore[misc]
        def _at_least_one_modality_v2(self):  # type: ignore[no-untyped-def]
            if not any([self.ecg, self.ehr, self.ct]):
                raise ValueError("At least one modality (ecg/ehr/ct) must be specified")
            return self
    else:
        @root_validator(pre=False, skip_on_failure=True)  # type: ignore[misc]
        def _at_least_one_modality_v1(cls, values):  # type: ignore[no-untyped-def]
            if not any(values.get(k) is not None for k in ("ecg", "ehr", "ct")):
                raise ValueError("At least one modality (ecg/ehr/ct) must be specified")
            return values

    @classmethod
    def from_json(cls, json_str: str) -> "ModalitiesConfig":
        """Parse a JSON string into a typed config, with validation."""
        # v2 uses model_validate_json; v1 uses parse_raw
        if hasattr(cls, "model_validate_json"):
            return cls.model_validate_json(json_str)  # type: ignore[attr-defined]
        return cls.parse_raw(json_str)


# ---------------------------------------------------------------------------
# Encoders mapping config (JSON object of modality->encoder_id)
# ---------------------------------------------------------------------------
if _PYDANTIC_V2 and 'RootModel' in globals() and RootModel is not None:  # type: ignore
    class EncodersConfig(RootModel[Dict[str, str]]):  # type: ignore
        """Top-level mapping of modality name to encoder identifier."""

        @classmethod
        def from_json(cls, json_str: str) -> "EncodersConfig":
            return cls.model_validate_json(json_str)  # type: ignore[attr-defined]

        def mapping(self) -> Dict[str, str]:  # type: ignore[override]
            return dict(self.root)
else:
    class EncodersConfig(BaseModel):
        """Top-level mapping of modality name to encoder identifier (v1 style)."""

        __root__: Dict[str, str]

        @classmethod
        def from_json(cls, json_str: str) -> "EncodersConfig":
            return cls.parse_raw(json_str)

        def mapping(self) -> Dict[str, str]:
            return dict(self.__root__)

