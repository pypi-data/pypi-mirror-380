"""HTTP client for interacting with the ChainGPT API."""

from typing import Any, Dict, AsyncIterator

import httpx

from ..exceptions import (
    APIError,
    TimeoutError as SDKTimeoutError,
    handle_http_error,
    AuthenticationError,
)
from ..types import HTTPHeaders, HTTPParams, HTTPTimeout, StreamChunk
from .logger import setup_logger

DEFAULT_TIMEOUT: HTTPTimeout = 120.0  # Default timeout in seconds
DEFAULT_STREAM_TIMEOUT: HTTPTimeout = 300.0  # Default timeout for stream requests


class AsyncHTTPClient:
    """Asynchronous HTTP client for ChainGPT API."""

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.chaingpt.org",
        timeout: HTTPTimeout = DEFAULT_TIMEOUT,
        stream_timeout: HTTPTimeout = DEFAULT_STREAM_TIMEOUT,
        debug: bool = False,
    ):
        if not api_key:
            raise AuthenticationError("API key is required.")

        self.base_url = base_url
        self._api_key = api_key
        self._timeout = timeout
        self._stream_timeout = stream_timeout
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers=self._get_default_headers(),
            timeout=self._timeout,
        )
        if debug:
            self.logger = setup_logger(__name__, level=10)  # DEBUG level
        else:
            self.logger = setup_logger(__name__)

    def _get_default_headers(self) -> HTTPHeaders:
        """Returns default headers for API requests."""
        return {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    async def close(self) -> None:
        """Closes the HTTP client."""
        await self._client.aclose()

    async def _request(
        self,
        method: str,
        endpoint: str,
        json_data: Dict[str, Any] | None = None,
        params: HTTPParams | None = None,
        custom_headers: HTTPHeaders | None = None,
        timeout: HTTPTimeout | None = None,
    ) -> httpx.Response:
        """Makes an HTTP request and returns the response."""
        headers = self._get_default_headers()
        if custom_headers:
            headers.update(custom_headers)

        request_url = f"{self.base_url}{endpoint}"
        self.logger.debug(
            f"Sending {method} request to {request_url} with data: {json_data}"
        )

        try:
            response = await self._client.request(
                method,
                endpoint,  # httpx.AsyncClient prepends base_url
                json=json_data,
                params=params,
                headers=headers,
                timeout=timeout or self._timeout,
            )
            response.raise_for_status()  # Raise HTTPStatusError for 4xx/5xx responses
        except httpx.TimeoutException as e:
            self.logger.error(f"Request timed out: {e}")
            raise SDKTimeoutError(f"Request to {request_url} timed out.")
        except httpx.HTTPStatusError as e:
            self.logger.error(
                f"HTTP error occurred: {e.response.status_code} - {e.response.text}"
            )
            handle_http_error(e.response)  # This will raise a specific SDK exception
            # Fallback if handle_http_error doesn't raise for some reason (it should)
            raise APIError(
                f"HTTP {e.response.status_code} error",
                status_code=e.response.status_code,
            )
        except httpx.RequestError as e:
            self.logger.error(f"An error occurred while requesting {request_url}: {e}")
            raise APIError(f"Request error to {request_url}: {e}")

        self.logger.debug(f"Received response: {response.status_code}")
        return response

    async def post(
        self,
        endpoint: str,
        json_data: Dict[str, Any],
        params: HTTPParams | None = None,
        custom_headers: HTTPHeaders | None = None,
        timeout: HTTPTimeout | None = None,
    ) -> Dict[str, Any]:
        """Sends a POST request and returns the JSON response."""
        response = await self._request(
            "POST",
            endpoint,
            json_data=json_data,
            params=params,
            custom_headers=custom_headers,
            timeout=timeout,
        )

        # Handle both JSON and plain text responses
        content_type = response.headers.get("content-type", "").lower()

        # First, try to parse as JSON if content-type suggests it or if parsing succeeds
        if "application/json" in content_type:
            try:
                return response.json()
            except Exception as e:
                self.logger.warning(
                    f"Content-Type indicates JSON but parsing failed: {e}"
                )
                # Fall through to text handling
        else:
            # Try JSON parsing anyway, some APIs don't set proper content-type
            try:
                return response.json()
            except Exception:
                # JSON parsing failed, this is expected for text responses
                pass

        # Handle plain text response
        text_content = response.text.strip()
        if text_content:
            self.logger.debug(f"Received plain text response: {text_content[:100]}...")
            return {
                "status": True,
                "message": "Success",
                "data": {"bot": text_content},
            }

        # Only raise exception if we have neither JSON nor meaningful text content
        raise APIError(f"API returned empty response with content-type: {content_type}")

    async def stream_post(
        self,
        endpoint: str,
        json_data: Dict[str, Any],
        params: HTTPParams | None = None,
        custom_headers: HTTPHeaders | None = None,
        timeout: HTTPTimeout | None = None,
    ) -> AsyncIterator[StreamChunk]:
        """Sends a POST request and streams the response."""
        headers = self._get_default_headers()
        if custom_headers:
            headers.update(custom_headers)
        headers["Accept"] = "text/event-stream"  # Or as required by API for streaming

        request_url = f"{self.base_url}{endpoint}"
        self.logger.debug(
            f"Streaming POST request to {request_url} with data: {json_data}"
        )

        try:
            async with self._client.stream(
                "POST",
                endpoint,  # httpx.AsyncClient prepends base_url
                json=json_data,
                params=params,
                headers=headers,
                timeout=timeout or self._stream_timeout,
            ) as response:
                # Check for initial error before streaming
                if response.status_code not in [200, 201]:
                    # Attempt to read error body if not 200/201 OK
                    error_body = await response.aread()
                    temp_response = httpx.Response(
                        status_code=response.status_code,
                        headers=response.headers,
                        content=error_body,
                        request=response.request,
                    )
                    handle_http_error(temp_response)
                    # Fallback if handle_http_error doesn't raise
                    raise APIError(
                        f"Streaming failed with status {response.status_code}",
                        status_code=response.status_code,
                    )

                async for (
                    chunk
                ) in response.aiter_bytes():  # Use aiter_bytes for raw bytes
                    if chunk:  # Only yield non-empty chunks
                        self.logger.debug(
                            f"Received stream chunk: {chunk[:100]}..."
                        )  # Log first 100 bytes
                        yield chunk
        except httpx.TimeoutException as e:
            self.logger.error(f"Stream request timed out: {e}")
            raise SDKTimeoutError(f"Stream request to {request_url} timed out.")
        except (
            httpx.HTTPStatusError
        ) as e:  # Should be caught by the check inside stream if status != 200
            self.logger.error(
                f"HTTP error during stream setup: {e.response.status_code} - {e.response.text}"
            )
            handle_http_error(e.response)
            raise APIError(
                f"HTTP {e.response.status_code} error",
                status_code=e.response.status_code,
            )  # Fallback
        except httpx.RequestError as e:
            self.logger.error(f"An error occurred while streaming {request_url}: {e}")
            raise APIError(f"Stream request error to {request_url}: {e}")

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
