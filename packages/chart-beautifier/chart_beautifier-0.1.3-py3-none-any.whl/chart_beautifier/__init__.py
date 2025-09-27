"""
Chart Beautifier SDK

A Python SDK for creating beautiful and interactive charts.
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .client import ChartBeautifierClient
from .exceptions import ChartBeautifierError, ValidationError, APIError

__all__ = [
    "ChartBeautifierClient",
    "ChartBeautifierError", 
    "ValidationError",
    "APIError"
]
