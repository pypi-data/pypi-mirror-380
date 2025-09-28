"""
XAI Embeddings - A Python package for explainable AI embeddings analysis.

This package provides various explanation methods for transformer-based models,
including attention-based, combination subsets, leave-one-out, and other explanation techniques.
"""

__version__ = "0.1.1"
__author__ = "Bartosz Rybiński"
__email__ = "bartoszrybinski@proton.me"

from . import explainers
from . import models
from . import distances

__all__ = [
    "explainers",
    "models",
    "distances",
]
