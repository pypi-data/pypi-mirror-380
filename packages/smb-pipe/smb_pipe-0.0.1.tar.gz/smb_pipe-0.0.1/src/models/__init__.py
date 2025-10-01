"""Model package init.

Keep this lightweight to avoid importing heavy submodules at package import time.
Submodules are imported lazily via strings in the ModelRegistry.
"""

__all__ = []