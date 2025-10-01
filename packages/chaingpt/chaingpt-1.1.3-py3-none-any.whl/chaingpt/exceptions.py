"""Custom exceptions for ChainGPT SDK."""

from typing import Dict, Any
import httpx


class ChainGPTError(Exception):
    """Base exception for all ChainGPT SDK errors."""

    def __init__(self, message: str, details: Dict[str, Any] | None = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def __str__(self) -> str:
        if self.details:
            return f"{self.message} - Details: {self.details}"
        return self.message


class APIError(ChainGPTError):
    """Raised when the API returns an error response."""

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        response: httpx.Response | None = None,
        details: Dict[str, Any] | None = None,
    ):
        super().__init__(message, details)
        self.status_code = status_code
        self.response = response

    @classmethod
    def from_response(cls, response: httpx.Response) -> "APIError":
        """Create APIError from HTTP response."""
        try:
            error_data = response.json()
            message = error_data.get("message", f"HTTP {response.status_code}")
            details = {k: v for k, v in error_data.items() if k != "message"}
        except Exception:
            message = f"HTTP {response.status_code}: {response.text}"
            details = {}

        return cls(
            message=message,
            status_code=response.status_code,
            response=response,
            details=details,
        )


class AuthenticationError(ChainGPTError):
    """Raised when authentication fails (401 Unauthorized)."""

    def __init__(self, message: str = "Invalid API key or authentication failed"):
        super().__init__(message)


class ValidationError(ChainGPTError):
    """Raised when request validation fails (400 Bad Request)."""

    def __init__(self, message: str, field: str | None = None):
        super().__init__(message)
        self.field = field

    @classmethod
    def from_response(cls, response: httpx.Response) -> "ValidationError":
        """Create ValidationError from HTTP response."""
        try:
            error_data = response.json()
            message = error_data.get(
                "message", f"Validation failed: HTTP {response.status_code}"
            )
            # Try to extract field information if available
            field = error_data.get("field") or error_data.get("parameter")
        except Exception:
            message = (
                f"Validation failed: HTTP {response.status_code} - {response.text}"
            )
            field = None

        return cls(message=message, field=field)


class InsufficientCreditsError(ChainGPTError):
    """Raised when account has insufficient credits (402/403)."""

    def __init__(self, message: str = "Insufficient credits in your account"):
        super().__init__(message)


class RateLimitError(ChainGPTError):
    """Raised when rate limit is exceeded (429 Too Many Requests)."""

    def __init__(
        self, message: str = "Rate limit exceeded", retry_after: int | None = None
    ):
        super().__init__(message)
        self.retry_after = retry_after

    @classmethod
    def from_response(cls, response: httpx.Response) -> "RateLimitError":
        """Create RateLimitError from HTTP response."""
        retry_after = None
        if "retry-after" in response.headers:
            try:
                retry_after = int(response.headers["retry-after"])
            except ValueError:
                pass

        try:
            error_data = response.json()
            message = error_data.get("message", "Rate limit exceeded")
        except Exception:
            message = "Rate limit exceeded"

        return cls(message=message, retry_after=retry_after)


class NotFoundError(ChainGPTError):
    """Raised when endpoint is not found (404 Not Found)."""

    def __init__(self, message: str = "Endpoint not found"):
        super().__init__(message)


class ServerError(ChainGPTError):
    """Raised when server returns 5xx error."""

    def __init__(self, message: str, status_code: int | None = None):
        super().__init__(message)
        self.status_code = status_code


class TimeoutError(ChainGPTError):
    """Raised when request times out."""

    def __init__(self, message: str = "Request timed out"):
        super().__init__(message)


class StreamingError(ChainGPTError):
    """Raised when streaming encounters an error."""

    def __init__(self, message: str):
        super().__init__(message)


class ConfigurationError(ChainGPTError):
    """Raised when SDK configuration is invalid."""

    def __init__(self, message: str):
        super().__init__(message)


def handle_http_error(response: httpx.Response) -> None:
    """Handle HTTP errors and raise appropriate exceptions."""
    if response.status_code == 400:
        raise ValidationError.from_response(response)
    elif response.status_code == 401:
        raise AuthenticationError()
    elif response.status_code in (402, 403):
        raise InsufficientCreditsError()
    elif response.status_code == 404:
        raise NotFoundError()
    elif response.status_code == 422:
        raise ValidationError.from_response(response)
    elif response.status_code == 429:
        raise RateLimitError.from_response(response)
    elif response.status_code >= 500:
        raise ServerError(
            f"Server error: {response.status_code}", status_code=response.status_code
        )
    else:
        raise APIError.from_response(response)
