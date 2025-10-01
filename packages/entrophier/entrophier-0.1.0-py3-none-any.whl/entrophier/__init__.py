"""
High-Entropy String Redaction Tool

A configurable Python tool for detecting and redacting sensitive data in text using
entropy analysis and pattern matching. Designed for processing log files, user input,
and any text containing potentially sensitive information.
"""

from .core import (
    redact_sensitive_data,
    redact_high_entropy_tokens,
    redact_high_entropy_strings,
    calculate_entropy,
    is_high_entropy_segment,
)
from .config import load_config

__version__ = "0.1.0"

__all__ = [
    "redact_sensitive_data",
    "redact_high_entropy_tokens",
    "redact_high_entropy_strings",
    "calculate_entropy",
    "is_high_entropy_segment",
    "load_config",
]
