"""
zenodo-sync: A lightweight CLI and Python library to synchronise local research data,
results and analysis artifacts with Zenodo.

Designed for reproducible science.
"""

__version__ = "0.1.0"
__author__ = "CausalIQ"
__email__ = "info@causaliq.com"

# Package metadata
__title__ = "zenodo-sync"
__description__ = "A lightweight CLI and Python library to synchronise local research data, results and analysis artifacts with Zenodo"
__url__ = "https://github.com/causaliq/zenodo-sync"
__license__ = "MIT"

# Version tuple for programmatic access
VERSION = tuple(map(int, __version__.split(".")))

# Import main classes and functions for easy access
from .core import ZenodoSync
from .exceptions import ZenodoSyncError

__all__ = [
    "__version__",
    "__author__",
    "__email__",
    "VERSION",
    "ZenodoSync",
    "ZenodoSyncError",
]