from __future__ import annotations

import importlib.metadata

from .guard import Guard


#: Package version string (PEP 440).
__version__ = "0.0.0+pkgnotfound"
try:
    if __package__ is not None:
        __version__ = importlib.metadata.version(__package__)
except Exception:
    pass


__all__ = ["__version__", "Guard"]
