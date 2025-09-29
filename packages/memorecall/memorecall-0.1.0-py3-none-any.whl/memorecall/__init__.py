"""
memorecall - A memory and recall enhancement library

This is a placeholder package similar to github.com/memori
"""

__version__ = "0.1.0"
__author__ = "Hoseyn Amiri"
__email__ = "aamirihoseyn@gmail.com"

# Import main functionality
from .core import MemoryRecall

# Expose public API
__all__ = ["MemoryRecall", "hello"]


def hello() -> str:
    """Simple hello function for testing the package."""
    return "Hello from memorecall!"
