"""Centralized logging configuration utilities."""
from __future__ import annotations

import sys
import warnings
from pathlib import Path
from datetime import datetime
from typing import Optional

from loguru import logger


def configure_run_logging(
    csv_path: str,
    quiet: bool = False,
    log_file: Optional[str] = None,
    enable_hf_warning_filter: bool = True,
):
    """Configure file and console logging for batch runs.

    - Writes INFO logs to outputs/logs/batch_<csvstem>_<ts>.log (or provided path)
    - Console: INFO by default; WARNING if quiet=True
    - Optionally filters noisy warnings
    - Sets Transformers logging verbosity accordingly when available
    """
    logs_dir = Path("outputs/logs")
    logs_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    default_log = logs_dir / f"batch_{Path(csv_path).stem}_{ts}.log"
    log_path = Path(log_file) if log_file else default_log

    # Reset existing handlers
    logger.remove()

    # File sink
    logger.add(
        str(log_path),
        rotation="50 MB",
        level="INFO",
        enqueue=True,
        backtrace=False,
        diagnose=False,
    )

    # Console sink
    if quiet:
        logger.add(sys.stderr, level="WARNING", enqueue=True, backtrace=False, diagnose=False)
        # Reduce HF verbosity if available
        try:
            from transformers.utils import logging as hf_logging  # type: ignore
            hf_logging.set_verbosity_error()
        except Exception:
            pass
        warnings.filterwarnings("ignore")
    else:
        logger.add(sys.stderr, level="INFO", enqueue=True, backtrace=False, diagnose=False)
        try:
            from transformers.utils import logging as hf_logging  # type: ignore
            hf_logging.set_verbosity_warning()
        except Exception:
            pass
        if enable_hf_warning_filter:
            warnings.filterwarnings("ignore", message="Flash-Attention not available.*")

    logger.info(f"Detailed logs written to: {str(log_path)}")
    return str(log_path)


def log_wandb_status(use_wandb: bool, project: str = "", run_name: str = "") -> None:
    """Deprecated: W&B integration removed; this is a no-op."""
    return


def log_input_prompt(prompt: str, modalities: tuple = (), row_idx: int = None, show_full_prompt: bool = False) -> None:
    """Log the input prompt for debugging and tracking.
    
    Args:
        prompt: The full input prompt text
        modalities: Modality tokens used (e.g., ('<m1_pad>',))
        row_idx: Optional row index for batch processing context
        show_full_prompt: If True, shows full prompt even in quiet mode
    """
    modality_info = f" [modalities: {', '.join(modalities)}]" if modalities else " [text-only]"
    row_info = f" [row {row_idx}]" if row_idx is not None else ""
    
    # Always log the summary (this will appear in file logs)
    logger.info(f"Input prompt prepared{modality_info}{row_info}")
    
    # Full prompt: use WARNING level if show_full_prompt=True (visible even with --quiet)
    if show_full_prompt:
        logger.warning(f"Input prompt preview (first 200 chars):\n{prompt[:200]}{'...' if len(prompt) > 200 else ''}")
    else:
        logger.debug(f"Full prompt text:\n{'-'*50}\n{prompt}\n{'-'*50}")


