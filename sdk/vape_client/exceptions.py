"""
VAP SDK Exceptions
"""


class VAPError(Exception):
    """Base exception for VAP errors."""

    def __init__(self, message: str, status_code: int = None, response: dict = None):
        self.message = message
        self.status_code = status_code
        self.response = response or {}
        super().__init__(self.message)


class VAPAuthenticationError(VAPError):
    """Authentication failed (401)."""
    pass


class VAPInsufficientBalanceError(VAPError):
    """Insufficient balance (402)."""
    pass


class VAPRateLimitError(VAPError):
    """Rate limit exceeded (429)."""
    pass


class VAPValidationError(VAPError):
    """Validation error (400)."""
    pass


class VAPServerError(VAPError):
    """Server error (5xx)."""
    pass
