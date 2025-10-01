"""Exception hierarchy for the Incredible Python SDK."""

from __future__ import annotations


class IncredibleError(Exception):
    """Base exception for the Incredible SDK."""


class APIError(IncredibleError):
    """Raised when the API returns a non-success status code."""

    def __init__(self, status_code: int, message: str) -> None:
        self.status_code = status_code
        self.message = message
        super().__init__(f"{status_code}: {message}")


class APIConnectionError(IncredibleError):
    """Raised when the SDK cannot reach the Incredible API."""


class APITimeoutError(APIConnectionError):
    """Raised when a request to the API times out."""


class APIResponseValidationError(IncredibleError):
    """Raised when the SDK cannot parse the API response."""
