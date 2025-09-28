"""Civic Interconnect package.

This package provides classes for Civic Interconnect projects.
"""

from importlib import metadata as _md

try:
    __version__: str = _md.version("civic-transparency-cwe-types")
except _md.PackageNotFoundError:  # pragma: no cover
    __version__: str = "0.0.0"

__all__ = ["__version__"]
