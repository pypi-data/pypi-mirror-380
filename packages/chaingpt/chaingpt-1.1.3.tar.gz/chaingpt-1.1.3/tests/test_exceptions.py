"""Tests for ChainGPT SDK exceptions."""

import pytest
from unittest.mock import Mock
import httpx

from chaingpt.exceptions import (
    ChainGPTError,
    APIError,
    AuthenticationError,
    ValidationError,
    InsufficientCreditsError,
    RateLimitError,
    NotFoundError,
    ServerError,
    TimeoutError,
    StreamingError,
    ConfigurationError,
    handle_http_error,
)


class TestChainGPTError:
    """Test cases for ChainGPTError base class."""

    def test_basic_exception(self):
        """Test basic exception creation."""
        error = ChainGPTError("Test error")
        assert str(error) == "Test error"
        assert error.message == "Test error"
        assert error.details == {}

    def test_exception_with_details(self):
        """Test exception with details."""
        details = {"code": "TEST_ERROR", "field": "test_field"}
        error = ChainGPTError("Test error", details)

        assert error.message == "Test error"
        assert error.details == details
        assert "Details:" in str(error)


class TestAPIError:
    """Test cases for APIError."""

    def test_api_error_creation(self):
        """Test APIError creation."""
        error = APIError("API error", status_code=400)
        assert error.message == "API error"
        assert error.status_code == 400

    def test_api_error_from_response(self):
        """Test creating APIError from HTTP response."""
        # Mock response with JSON error
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 400
        mock_response.json.return_value = {
            "message": "Bad request",
            "code": "INVALID_INPUT",
        }

        error = APIError.from_response(mock_response)
        assert error.message == "Bad request"
        assert error.status_code == 400
        assert error.details == {"code": "INVALID_INPUT"}

    def test_api_error_from_response_no_json(self):
        """Test creating APIError from response without JSON."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 500
        mock_response.json.side_effect = Exception("Not JSON")
        mock_response.text = "Internal Server Error"

        error = APIError.from_response(mock_response)
        assert "HTTP 500" in error.message
        assert error.status_code == 500


class TestValidationError:
    """Test cases for ValidationError."""

    def test_validation_error_basic(self):
        """Test basic ValidationError."""
        error = ValidationError("Invalid input")
        assert error.message == "Invalid input"
        assert error.field is None

    def test_validation_error_with_field(self):
        """Test ValidationError with field."""
        error = ValidationError("Invalid input", field="email")
        assert error.message == "Invalid input"
        assert error.field == "email"

    def test_validation_error_from_response(self):
        """Test creating ValidationError from response."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 400
        mock_response.json.return_value = {
            "message": "Validation failed",
            "field": "api_key",
        }

        error = ValidationError.from_response(mock_response)
        assert error.message == "Validation failed"
        assert error.field == "api_key"

    def test_validation_error_from_response_no_json(self):
        """Test ValidationError from response without JSON."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 400
        mock_response.json.side_effect = Exception("Not JSON")
        mock_response.text = "Bad Request"

        error = ValidationError.from_response(mock_response)
        assert "Validation failed" in error.message
        assert error.field is None


class TestRateLimitError:
    """Test cases for RateLimitError."""

    def test_rate_limit_error_basic(self):
        """Test basic RateLimitError."""
        error = RateLimitError()
        assert "Rate limit exceeded" in error.message
        assert error.retry_after is None

    def test_rate_limit_error_with_retry_after(self):
        """Test RateLimitError with retry_after."""
        error = RateLimitError("Rate limited", retry_after=60)
        assert error.message == "Rate limited"
        assert error.retry_after == 60

    def test_rate_limit_error_from_response(self):
        """Test creating RateLimitError from response."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {"retry-after": "120"}
        mock_response.json.return_value = {"message": "Too many requests"}

        error = RateLimitError.from_response(mock_response)
        assert error.message == "Too many requests"
        assert error.retry_after == 120

    def test_rate_limit_error_invalid_retry_after(self):
        """Test RateLimitError with invalid retry-after header."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {"retry-after": "invalid"}
        mock_response.json.return_value = {"message": "Too many requests"}

        error = RateLimitError.from_response(mock_response)
        assert error.retry_after is None


class TestServerError:
    """Test cases for ServerError."""

    def test_server_error_basic(self):
        """Test basic ServerError."""
        error = ServerError("Server error")
        assert error.message == "Server error"
        assert error.status_code is None

    def test_server_error_with_status_code(self):
        """Test ServerError with status code."""
        error = ServerError("Internal error", status_code=500)
        assert error.message == "Internal error"
        assert error.status_code == 500


class TestOtherExceptions:
    """Test cases for other specific exceptions."""

    def test_authentication_error(self):
        """Test AuthenticationError."""
        error = AuthenticationError()
        assert "authentication failed" in error.message.lower()

    def test_insufficient_credits_error(self):
        """Test InsufficientCreditsError."""
        error = InsufficientCreditsError()
        assert "insufficient credits" in error.message.lower()

    def test_not_found_error(self):
        """Test NotFoundError."""
        error = NotFoundError()
        assert "not found" in error.message.lower()

    def test_timeout_error(self):
        """Test TimeoutError."""
        error = TimeoutError()
        assert "timed out" in error.message.lower()

    def test_streaming_error(self):
        """Test StreamingError."""
        error = StreamingError("Stream failed")
        assert error.message == "Stream failed"

    def test_configuration_error(self):
        """Test ConfigurationError."""
        error = ConfigurationError("Invalid config")
        assert error.message == "Invalid config"


class TestHandleHttpError:
    """Test cases for handle_http_error function."""

    def test_handle_400_error(self):
        """Test handling 400 Bad Request."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 400
        mock_response.json.return_value = {"message": "Bad request"}

        with pytest.raises(ValidationError):
            handle_http_error(mock_response)

    def test_handle_401_error(self):
        """Test handling 401 Unauthorized."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 401

        with pytest.raises(AuthenticationError):
            handle_http_error(mock_response)

    def test_handle_402_error(self):
        """Test handling 402 Payment Required."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 402

        with pytest.raises(InsufficientCreditsError):
            handle_http_error(mock_response)

    def test_handle_403_error(self):
        """Test handling 403 Forbidden."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 403

        with pytest.raises(InsufficientCreditsError):
            handle_http_error(mock_response)

    def test_handle_404_error(self):
        """Test handling 404 Not Found."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 404

        with pytest.raises(NotFoundError):
            handle_http_error(mock_response)

    def test_handle_422_error(self):
        """Test handling 422 Unprocessable Entity."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 422
        mock_response.json.return_value = {"message": "Validation error"}

        with pytest.raises(ValidationError):
            handle_http_error(mock_response)

    def test_handle_429_error(self):
        """Test handling 429 Too Many Requests."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 429
        mock_response.headers = {}
        mock_response.json.return_value = {"message": "Rate limited"}

        with pytest.raises(RateLimitError):
            handle_http_error(mock_response)

    def test_handle_500_error(self):
        """Test handling 500 Internal Server Error."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 500

        with pytest.raises(ServerError) as exc_info:
            handle_http_error(mock_response)

        assert exc_info.value.status_code == 500

    def test_handle_other_error(self):
        """Test handling other HTTP errors."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 418  # I'm a teapot
        mock_response.json.return_value = {"message": "Teapot error"}

        with pytest.raises(APIError):
            handle_http_error(mock_response)
