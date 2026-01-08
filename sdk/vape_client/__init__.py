"""
VAP Python SDK
Official Python client for VAP AI Generation API
"""

__version__ = "1.0.0"
__author__ = "VAP Team"

from .client import VAPClient
from .models import GenerateResult, HealthStatus, Balance
from .exceptions import (
    VAPError,
    VAPAuthenticationError,
    VAPInsufficientBalanceError,
    VAPRateLimitError,
    VAPValidationError,
    VAPServerError,
)

__all__ = [
    "__version__",
    "VAPClient",
    "GenerateResult",
    "HealthStatus",
    "Balance",
    "VAPError",
    "VAPAuthenticationError",
    "VAPInsufficientBalanceError",
    "VAPRateLimitError",
    "VAPValidationError",
    "VAPServerError",
]
