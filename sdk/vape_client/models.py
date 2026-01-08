"""
VAP SDK Models
Data models for API responses
"""

from typing import Optional, Dict, Any
from dataclasses import dataclass


@dataclass
class GenerateResult:
    """Result of image generation."""
    success: bool
    image_url: Optional[str] = None
    task_id: Optional[str] = None
    error: Optional[str] = None

    @classmethod
    def from_response(cls, data: dict) -> "GenerateResult":
        return cls(
            success=data.get("success", False),
            image_url=data.get("image_url"),
            task_id=data.get("task_id"),
            error=data.get("error"),
        )


@dataclass
class HealthStatus:
    """API health status."""
    status: str
    version: Optional[str] = None

    @classmethod
    def from_response(cls, data: dict) -> "HealthStatus":
        return cls(
            status=data.get("status", "unknown"),
            version=data.get("version"),
        )


@dataclass
class Balance:
    """Account balance."""
    balance: float
    currency: str = "USD"

    @classmethod
    def from_response(cls, data: dict) -> "Balance":
        return cls(
            balance=float(data.get("balance", 0)),
            currency=data.get("currency", "USD"),
        )
