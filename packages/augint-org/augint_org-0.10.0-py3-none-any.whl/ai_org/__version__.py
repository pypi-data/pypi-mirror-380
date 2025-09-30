"""Version information for augint-org."""

import importlib.metadata

try:
    # Get version from installed package metadata
    __version__ = importlib.metadata.version("augint-org")
except importlib.metadata.PackageNotFoundError:
    # Fallback for development
    __version__ = "0.0.0-dev"
