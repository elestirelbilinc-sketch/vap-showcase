"""
VAP Sync Client
Synchronous HTTP client for VAP API
"""

import httpx
from typing import Optional, Dict, Any
from .models import GenerateResult, HealthStatus, Balance
from .exceptions import (
    VAPError,
    VAPAuthenticationError,
    VAPInsufficientBalanceError,
    VAPRateLimitError,
    VAPValidationError,
    VAPServerError,
)


class VAPClient:
    """
    Synchronous client for VAP API.

    Usage:
        client = VAPClient(api_key="your_api_key")
        result = client.generate(prompt="A sunset over mountains")
        print(result.image_url)
    """

    DEFAULT_BASE_URL = "https://api.vapagent.com"
    DEFAULT_TIMEOUT = 60.0

    def __init__(
        self,
        api_key: str,
        base_url: str = None,
        timeout: float = None,
    ):
        """
        Initialize VAP client.

        Args:
            api_key: Your VAP API key
            base_url: API base URL (default: https://api.vapagent.com)
            timeout: Request timeout in seconds (default: 60)
        """
        self.api_key = api_key
        self.base_url = (base_url or self.DEFAULT_BASE_URL).rstrip("/")
        self.timeout = timeout or self.DEFAULT_TIMEOUT

        self._client = httpx.Client(
            base_url=self.base_url,
            timeout=self.timeout,
            headers=self._default_headers(),
        )

    def _default_headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "User-Agent": "vap-client-python/1.0.0",
        }

    def _handle_response(self, response: httpx.Response) -> dict:
        try:
            data = response.json()
        except:
            data = {"error": response.text}

        if response.status_code == 200:
            return data
        elif response.status_code == 401:
            raise VAPAuthenticationError("Authentication failed", 401, data)
        elif response.status_code == 402:
            raise VAPInsufficientBalanceError("Insufficient balance", 402, data)
        elif response.status_code == 429:
            raise VAPRateLimitError("Rate limit exceeded", 429, data)
        elif response.status_code == 400:
            raise VAPValidationError("Validation error", 400, data)
        elif response.status_code >= 500:
            raise VAPServerError("Server error", response.status_code, data)
        else:
            raise VAPError(f"Request failed: {response.status_code}", response.status_code, data)

    def _request(self, method: str, endpoint: str, json: dict = None) -> dict:
        response = self._client.request(method=method, url=endpoint, json=json)
        return self._handle_response(response)

    def close(self):
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def health(self) -> HealthStatus:
        """Check API health status."""
        data = self._request("GET", "/health")
        return HealthStatus.from_response(data)

    def generate(
        self,
        prompt: str,
        aspect_ratio: str = "1:1",
        style: Optional[str] = None,
    ) -> GenerateResult:
        """
        Generate an image from prompt.

        Args:
            prompt: Text description of the image
            aspect_ratio: Image aspect ratio (1:1, 16:9, 9:16)
            style: Optional style hints

        Returns:
            GenerateResult with image_url
        """
        payload = {"prompt": prompt, "aspect_ratio": aspect_ratio}
        if style:
            payload["style"] = style

        data = self._request("POST", "/v3/generate", json=payload)
        return GenerateResult.from_response(data)

    def get_balance(self) -> Balance:
        """Get current account balance."""
        data = self._request("GET", "/v3/balance")
        return Balance.from_response(data)
