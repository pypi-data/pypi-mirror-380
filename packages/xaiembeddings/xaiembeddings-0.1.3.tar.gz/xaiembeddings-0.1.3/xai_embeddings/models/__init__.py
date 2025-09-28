"""
Model modules for XAI Embeddings.

This module contains model implementations for generating embeddings
from transformer-based models.
"""

from .model import Model
from .BERT_model import BERT_model

__all__ = [
    "Model",
    "BERT_model",
]
