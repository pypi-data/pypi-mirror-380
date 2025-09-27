"""
Rune: Zero-configuration, OS-independent asset management for Python.

This package provides a single, intuitive entry point (`assets`) for accessing
project assets without needing to manage relative paths or complex configurations.
"""

__version__ = "0.1.0"

from .exceptions import AssetNotFoundError, ConfigurationError, RuneError, ProjectRootNotFoundError
from .loader import RuneLoader

# The primary public API for the Rune library.
# Users can import this object directly to access their assets.
# Example:
#   from rune import assets
#   image_path = assets.images / "player.png"
assets = RuneLoader()

__all__ = [
    "assets",
    "RuneError",
    "AssetNotFoundError",
    "ProjectRootNotFoundError",
    "ConfigurationError",
]