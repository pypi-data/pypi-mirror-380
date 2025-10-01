"""
tintap - AI Audio Detection & Attribution Solutions

A Python SDK for the tintap AI audio detection platform.
Detect AI-generated audio content and get detailed analysis results.

Homepage: https://tintap.ai
Documentation: https://docs.tintap.ai
"""

from .client import TintapClient, create_client
from .exceptions import TintapError, TintapAPIError, TintapConnectionError

__version__ = "0.1.0"
__author__ = "tintap"
__email__ = "contact@tintap.ai"
__homepage__ = "https://tintap.ai"

__all__ = [
    "TintapClient",
    "create_client", 
    "TintapError",
    "TintapAPIError",
    "TintapConnectionError",
]