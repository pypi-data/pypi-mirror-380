"""Tests for AsyncHTTPClient."""

import pytest
from unittest.mock import AsyncMock, Mock, patch
import httpx

from chaingpt.utils.http import AsyncHTTPClient, DEFAULT_TIMEOUT, DEFAULT_STREAM_TIMEOUT
from chaingpt.exceptions import (
    APIError,
    AuthenticationError,
    TimeoutError as SDKTimeoutError,
    ValidationError,
)


class TestAsyncHTTPClient:
    """Test cases for AsyncHTTPClient."""

    def test_client_initialization(self, api_key):
        """Test client initialization."""
        client = AsyncHTTPClient(api_key=api_key)

        assert client.base_url == "https://api.chaingpt.org"
        assert client._api_key == api_key
        assert client._timeout == DEFAULT_TIMEOUT
        assert client._stream_timeout == DEFAULT_STREAM_TIMEOUT

    def test_client_initialization_with_custom_params(self, api_key):
        """Test client initialization with custom parameters."""
        base_url = "https://custom.api.url"
        timeout = 60.0
        stream_timeout = 120.0

        client = AsyncHTTPClient(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            stream_timeout=stream_timeout,
        )

        assert client.base_url == base_url
        assert client._timeout == timeout
        assert client._stream_timeout == stream_timeout

    def test_client_initialization_without_api_key(self):
        """Test client initialization without API key raises error."""
        with pytest.raises(AuthenticationError):
            AsyncHTTPClient(api_key="")

    def test_get_default_headers(self, api_key):
        """Test default headers generation."""
        client = AsyncHTTPClient(api_key=api_key)
        headers = client._get_default_headers()

        assert headers["Authorization"] == f"Bearer {api_key}"
        assert headers["Content-Type"] == "application/json"
        assert headers["Accept"] == "application/json"

    @pytest.mark.asyncio
    async def test_close(self, api_key):
        """Test client close method."""
        client = AsyncHTTPClient(api_key=api_key)

        with patch.object(
            client._client, "aclose", new_callable=AsyncMock
        ) as mock_close:
            await client.close()
            mock_close.assert_called_once()

    @pytest.mark.asyncio
    async def test_context_manager(self, api_key):
        """Test client as async context manager."""
        async with AsyncHTTPClient(api_key=api_key) as client:
            assert isinstance(client, AsyncHTTPClient)

    @pytest.mark.asyncio
    async def test_post_json_response(self, api_key):
        """Test POST request with JSON response."""
        client = AsyncHTTPClient(api_key=api_key)

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {"content-type": "application/json"}
        mock_response.json.return_value = {
            "status": True,
            "data": {"result": "success"},
        }
        mock_response.raise_for_status.return_value = None

        with patch.object(
            client._client,
            "request",
            new_callable=AsyncMock,
            return_value=mock_response,
        ):
            result = await client.post("/test", {"data": "test"})

            assert result == {"status": True, "data": {"result": "success"}}

    @pytest.mark.asyncio
    async def test_post_text_response(self, api_key):
        """Test POST request with text response."""
        client = AsyncHTTPClient(api_key=api_key)

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {"content-type": "text/plain"}
        mock_response.json.side_effect = Exception("Not JSON")
        mock_response.text = "This is a text response"
        mock_response.raise_for_status.return_value = None

        with patch.object(
            client._client,
            "request",
            new_callable=AsyncMock,
            return_value=mock_response,
        ):
            result = await client.post("/test", {"data": "test"})

            expected = {
                "status": True,
                "message": "Success",
                "data": {"bot": "This is a text response"},
            }
            assert result == expected

    @pytest.mark.asyncio
    async def test_post_empty_response(self, api_key):
        """Test POST request with empty response."""
        client = AsyncHTTPClient(api_key=api_key)

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {"content-type": "text/plain"}
        mock_response.json.side_effect = Exception("Not JSON")
        mock_response.text = ""
        mock_response.raise_for_status.return_value = None

        with patch.object(
            client._client,
            "request",
            new_callable=AsyncMock,
            return_value=mock_response,
        ):
            with pytest.raises(APIError, match="empty response"):
                await client.post("/test", {"data": "test"})

    @pytest.mark.asyncio
    async def test_request_timeout_error(self, api_key):
        """Test request timeout handling."""
        client = AsyncHTTPClient(api_key=api_key)

        with patch.object(
            client._client,
            "request",
            new_callable=AsyncMock,
            side_effect=httpx.TimeoutException("Timeout"),
        ):
            with pytest.raises(SDKTimeoutError):
                await client.post("/test", {"data": "test"})

    @pytest.mark.asyncio
    async def test_request_http_status_error(self, api_key):
        """Test HTTP status error handling."""
        client = AsyncHTTPClient(api_key=api_key)

        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"

        http_error = httpx.HTTPStatusError(
            "Bad Request", request=Mock(), response=mock_response
        )

        with patch.object(
            client._client, "request", new_callable=AsyncMock, side_effect=http_error
        ):
            with patch(
                "chaingpt.utils.http.handle_http_error",
                side_effect=ValidationError("Bad Request"),
            ):
                with pytest.raises(ValidationError):
                    await client.post("/test", {"data": "test"})

    @pytest.mark.asyncio
    async def test_request_generic_error(self, api_key):
        """Test generic request error handling."""
        client = AsyncHTTPClient(api_key=api_key)

        request_error = httpx.RequestError("Connection failed")

        with patch.object(
            client._client, "request", new_callable=AsyncMock, side_effect=request_error
        ):
            with pytest.raises(APIError, match="Request error"):
                await client.post("/test", {"data": "test"})

    @pytest.mark.asyncio
    async def test_stream_post_success(self, api_key):
        """Test successful streaming POST request."""
        client = AsyncHTTPClient(api_key=api_key)

        # Mock stream response
        async def mock_aiter_bytes():
            yield b"chunk1"
            yield b"chunk2"
            yield b"chunk3"

        mock_response = AsyncMock()
        mock_response.status_code = 200
        mock_response.aiter_bytes = mock_aiter_bytes

        mock_stream_context = AsyncMock()
        mock_stream_context.__aenter__.return_value = mock_response
        mock_stream_context.__aexit__.return_value = None

        with patch.object(client._client, "stream", return_value=mock_stream_context):
            chunks = []
            async for chunk in client.stream_post("/test", {"data": "test"}):
                chunks.append(chunk)

            assert chunks == [b"chunk1", b"chunk2", b"chunk3"]

    @pytest.mark.asyncio
    async def test_stream_post_error_response(self, api_key):
        """Test streaming POST request with error response."""
        client = AsyncHTTPClient(api_key=api_key)

        mock_response = AsyncMock()
        mock_response.status_code = 400
        mock_response.headers = {}
        mock_response.request = Mock()
        mock_response.aread.return_value = b"Bad Request"

        mock_stream_context = AsyncMock()
        mock_stream_context.__aenter__.return_value = mock_response
        mock_stream_context.__aexit__.return_value = None

        with patch.object(client._client, "stream", return_value=mock_stream_context):
            with patch(
                "chaingpt.utils.http.handle_http_error",
                side_effect=ValidationError("Bad Request"),
            ):
                with pytest.raises(ValidationError):
                    async for chunk in client.stream_post("/test", {"data": "test"}):
                        pass

    @pytest.mark.asyncio
    async def test_stream_post_timeout(self, api_key):
        """Test streaming POST request timeout."""
        client = AsyncHTTPClient(api_key=api_key)

        with patch.object(
            client._client, "stream", side_effect=httpx.TimeoutException("Timeout")
        ):
            with pytest.raises(SDKTimeoutError):
                async for chunk in client.stream_post("/test", {"data": "test"}):
                    pass

    @pytest.mark.asyncio
    async def test_custom_headers(self, api_key):
        """Test request with custom headers."""
        client = AsyncHTTPClient(api_key=api_key)

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {"content-type": "application/json"}
        mock_response.json.return_value = {"success": True}
        mock_response.raise_for_status.return_value = None

        custom_headers = {"X-Custom-Header": "test-value"}

        with patch.object(
            client._client,
            "request",
            new_callable=AsyncMock,
            return_value=mock_response,
        ) as mock_request:
            await client.post("/test", {"data": "test"}, custom_headers=custom_headers)

            # Check that custom headers were included
            call_kwargs = mock_request.call_args[1]
            headers = call_kwargs["headers"]
            assert headers["X-Custom-Header"] == "test-value"
            assert headers["Authorization"] == f"Bearer {api_key}"

    @pytest.mark.asyncio
    async def test_custom_timeout(self, api_key):
        """Test request with custom timeout."""
        client = AsyncHTTPClient(api_key=api_key)

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {"content-type": "application/json"}
        mock_response.json.return_value = {"success": True}
        mock_response.raise_for_status.return_value = None

        custom_timeout = 120.0

        with patch.object(
            client._client,
            "request",
            new_callable=AsyncMock,
            return_value=mock_response,
        ) as mock_request:
            await client.post("/test", {"data": "test"}, timeout=custom_timeout)

            # Check that custom timeout was used
            call_kwargs = mock_request.call_args[1]
            assert call_kwargs["timeout"] == custom_timeout

    @pytest.mark.asyncio
    async def test_request_with_params(self, api_key):
        """Test request with query parameters."""
        client = AsyncHTTPClient(api_key=api_key)

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {"content-type": "application/json"}
        mock_response.json.return_value = {"success": True}
        mock_response.raise_for_status.return_value = None

        params = {"param1": "value1", "param2": "value2"}

        with patch.object(
            client._client,
            "request",
            new_callable=AsyncMock,
            return_value=mock_response,
        ) as mock_request:
            await client.post("/test", {"data": "test"}, params=params)

            # Check that params were included
            call_kwargs = mock_request.call_args[1]
            assert call_kwargs["params"] == params
