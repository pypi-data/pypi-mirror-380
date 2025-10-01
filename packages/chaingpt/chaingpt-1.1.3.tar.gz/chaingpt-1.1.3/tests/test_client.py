"""Tests for ChainGPTClient."""

import pytest
from unittest.mock import patch, AsyncMock

from chaingpt.client import ChainGPTClient
from chaingpt.exceptions import AuthenticationError, ConfigurationError
from chaingpt.services import (
    LLMService,
    NFTService,
    SmartContractService,
    AuditorService,
    NewsService,
)


class TestChainGPTClient:
    """Test cases for ChainGPTClient."""

    def test_client_initialization(self, api_key):
        """Test client initialization with valid parameters."""
        client = ChainGPTClient(api_key=api_key)

        assert client._http_client is not None
        assert isinstance(client.llm, LLMService)
        assert isinstance(client.nft, NFTService)
        assert isinstance(client.smart_contract, SmartContractService)
        assert isinstance(client.auditor, AuditorService)
        assert isinstance(client.news, NewsService)

    def test_client_initialization_with_custom_params(self, api_key):
        """Test client initialization with custom parameters."""
        base_url = "https://custom.api.url"
        timeout = 60.0
        stream_timeout = 120.0

        client = ChainGPTClient(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            stream_timeout=stream_timeout,
        )

        assert client._http_client.base_url == base_url

    def test_client_initialization_without_api_key(self):
        """Test client initialization without API key raises error."""
        with pytest.raises(AuthenticationError):
            ChainGPTClient(api_key="")

    @pytest.mark.asyncio
    async def test_client_close(self, api_key):
        """Test client close method."""
        client = ChainGPTClient(api_key=api_key)

        with patch.object(
            client._http_client, "close", new_callable=AsyncMock
        ) as mock_close:
            await client.close()
            mock_close.assert_called_once()

    @pytest.mark.asyncio
    async def test_client_context_manager(self, api_key):
        """Test client as async context manager."""
        with patch(
            "chaingpt.utils.http.AsyncHTTPClient.close", new_callable=AsyncMock
        ) as mock_close:
            async with ChainGPTClient(api_key=api_key) as client:
                assert isinstance(client, ChainGPTClient)

            mock_close.assert_called_once()

    def test_client_services_initialization(self, api_key):
        """Test that all services are properly initialized."""
        client = ChainGPTClient(api_key=api_key)

        # Check that all services share the same HTTP client
        assert client.llm._http_client is client._http_client
        assert client.nft._http_client is client._http_client
        assert client.smart_contract._http_client is client._http_client
        assert client.auditor._http_client is client._http_client
        assert client.news._http_client is client._http_client

    @pytest.mark.asyncio
    async def test_multiple_client_instances(self, api_key):
        """Test creating multiple client instances."""
        client1 = ChainGPTClient(api_key=api_key)
        client2 = ChainGPTClient(api_key=api_key + "_2")

        assert client1._http_client is not client2._http_client

        await client1.close()
        await client2.close()

    def test_client_default_values(self, api_key):
        """Test client uses correct default values."""
        client = ChainGPTClient(api_key=api_key)

        assert client._http_client.base_url == "https://api.chaingpt.org"
        # Note: timeout values are stored in the AsyncHTTPClient instance

    @pytest.mark.asyncio
    async def test_client_aenter_aexit(self, api_key):
        """Test client async enter and exit methods."""
        client = ChainGPTClient(api_key=api_key)

        # Test __aenter__
        entered_client = await client.__aenter__()
        assert entered_client is client

        # Test __aexit__
        with patch.object(client, "close", new_callable=AsyncMock) as mock_close:
            await client.__aexit__(None, None, None)
            mock_close.assert_called_once()
