"""Integration tests for ChainGPT SDK."""

import pytest
import asyncio
from unittest.mock import AsyncMock, patch, Mock

from chaingpt.client import ChainGPTClient
from chaingpt.models.llm import (
    LLMChatRequestModel,
    ContextInjectionModel,
    TokenInformationModel,
)
from chaingpt.models.nft import GenerateImageRequestModel, ImageBufferModel
from chaingpt.types import (
    ChatHistoryMode,
    AITone,
    PresetTone,
    BlockchainNetwork,
    NFTImageModel,
    ImageEnhanceOption,
)
from chaingpt.exceptions import AuthenticationError, ChainGPTError


class TestIntegration:
    """Integration tests that test multiple components together."""

    @pytest.fixture
    def mock_http_client(self):
        """Create a mock HTTP client that properly handles API key validation."""
        mock_client = AsyncMock()

        # Create a mock response object
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": True,
            "message": "Success",
            "data": {
                "bot": "Based on your token information, TestToken (TST) is an ERC-20 token on Ethereum designed for testing purposes."
            },
        }
        mock_response.raise_for_status = Mock()  # Mock the raise_for_status method

        # Set up the mock client to return our mock response
        mock_client.post.return_value = mock_response.json()
        mock_client._request.return_value = mock_response

        return mock_client

    @pytest.mark.asyncio
    @pytest.mark.integration
    async def test_full_llm_workflow(self, api_key):
        """Test a complete LLM workflow with context injection."""
        mock_response = {
            "status": True,
            "message": "Success",
            "data": {
                "bot": "Based on your token information, TestToken (TST) is an ERC-20 token on Ethereum designed for testing purposes."
            },
        }

        with patch("chaingpt.utils.http.AsyncHTTPClient") as mock_http_class:
            mock_http_client = AsyncMock()
            mock_http_client.post.return_value = mock_response
            mock_http_class.return_value = mock_http_client

            client = ChainGPTClient(api_key=api_key)

            # Create context with token information
            token_info = TokenInformationModel(
                tokenName="TestToken",
                tokenSymbol="TST",
                blockchain=[BlockchainNetwork.ETHEREUM],
            )
            context = ContextInjectionModel(
                companyName="Test Company",
                companyDescription="A blockchain testing company",
                cryptoToken=True,
                tokenInformation=token_info,
                aiTone=AITone.PRE_SET_TONE,
                selectedTone=PresetTone.PROFESSIONAL,
            )

            # Create chat request
            request = LLMChatRequestModel(
                question="Tell me about our token",
                useCustomContext=True,
                contextInjection=context,
                chatHistory=ChatHistoryMode.ON,
                sdkUniqueId="550e8400-e29b-41d4-a716-446655440000",
            )

            # Send request
            response = await client.llm.chat(request)

            # Verify response
            assert response.status is True
            assert "token" in response.data.bot or "TST" in response.data.bot

            await client.close()

    @pytest.mark.asyncio
    @pytest.mark.integration
    async def test_full_nft_workflow(self, api_key):
        """Test a complete NFT generation workflow."""
        mock_response = {
            "status": True,
            "message": "Image generated successfully",
            "data": {"type": "Buffer", "data": [1, 2, 3, 4]},
        }

        with patch("chaingpt.utils.http.AsyncHTTPClient") as mock_http_class:
            mock_http_client = AsyncMock()
            mock_http_client.post.return_value = mock_response
            mock_http_class.return_value = mock_http_client

            client = ChainGPTClient(api_key=api_key)

            # Create image generation request
            request = GenerateImageRequestModel(
                prompt="A futuristic cityscape with neon lights",
                model=NFTImageModel.VELOGEN,
                enhance=ImageEnhanceOption.ENHANCE_1X,
                height=512,
                width=512,
            )

            # Generate image
            response = await client.nft.generate_image(request)

            # Verify response
            assert isinstance(response.data, ImageBufferModel)
            assert hasattr(response.data, "data")

            await client.close()

    @pytest.mark.asyncio
    @pytest.mark.integration
    async def test_streaming_llm_workflow(self, api_key):
        """Test streaming LLM workflow."""
        # Set up streaming response
        chunks = [b"Hello ", b"there! ", b"This is ", b"a streaming ", b"response."]

        async def mock_stream():
            for chunk in chunks:
                yield chunk

        with patch("chaingpt.utils.http.AsyncHTTPClient") as mock_http_class:
            mock_http_client = AsyncMock()
            mock_http_client.stream_post.return_value = mock_stream()
            mock_http_class.return_value = mock_http_client

            client = ChainGPTClient(api_key=api_key)

            # Create chat request
            request = LLMChatRequestModel(
                question="Tell me a story", chatHistory=ChatHistoryMode.OFF
            )

            # Collect streaming response
            received_chunks = []
            async for chunk in client.llm.stream_chat(request):
                received_chunks.append(chunk)

            # Verify streaming worked
            assert len(received_chunks) >= 10

            await client.close()

    @pytest.mark.asyncio
    @pytest.mark.integration
    async def test_multiple_service_calls(self, api_key):
        """Test making calls to multiple services in sequence."""

        # Set up different responses for different endpoints
        def mock_post_side_effect(endpoint, json_data):
            if endpoint == "/chat/stream":
                return {
                    "status": True,
                    "message": "Success",
                    "data": {"bot": "LLM response"},
                }
            elif endpoint == "/nft/generate-image":
                return {
                    "status": True,
                    "message": "Image generated",
                    "data": {"type": "Buffer", "data": [1, 2, 3, 4]},
                }
            elif endpoint == "/nft/enhancePrompt":
                return {
                    "status": True,
                    "message": "Prompt enhanced",
                    "data": {"enhancedPrompt": "Enhanced prompt text"},
                }
            else:
                return {
                    "status": False,
                    "message": "Unknown endpoint",
                }

        with patch("chaingpt.utils.http.AsyncHTTPClient") as mock_http_class:
            mock_http_client = AsyncMock()
            mock_http_client.post.side_effect = mock_post_side_effect
            mock_http_class.return_value = mock_http_client

            client = ChainGPTClient(api_key=api_key)

            # Make LLM call
            llm_request = LLMChatRequestModel(question="What is AI?")
            llm_response = await client.llm.chat(llm_request)
            assert llm_response.status is True

            # Make NFT generation call
            nft_request = GenerateImageRequestModel(
                prompt="A robot", model=NFTImageModel.VELOGEN, height=512, width=512
            )
            nft_response = await client.nft.generate_image(nft_request)
            assert isinstance(nft_response.data, ImageBufferModel)

            # Make prompt enhancement call
            from chaingpt.models.nft import EnhancePromptRequestModel

            enhance_request = EnhancePromptRequestModel(prompt="A simple robot")
            enhance_response = await client.nft.enhance_prompt(enhance_request)
            assert "Masterpiece" in enhance_response.data.enhancedPrompt

            await client.close()

    @pytest.mark.asyncio
    @pytest.mark.integration
    async def test_error_handling_across_services(self, api_key):
        """Test error handling consistency across different services."""
        # Set up error response
        error_response = {
            "status": False,
            "message": "API Error: Invalid request",
        }

        with patch("chaingpt.utils.http.AsyncHTTPClient") as mock_http_class:
            mock_http_client = AsyncMock()
            mock_http_client.post.return_value = error_response
            mock_http_class.return_value = mock_http_client

            client = ChainGPTClient(api_key=api_key)

            # Test LLM error handling
            llm_request = LLMChatRequestModel(question="Test question")
            with pytest.raises(ChainGPTError):  # Should raise ChainGPTError
                await client.llm.chat(llm_request)

            # Test NFT error handling
            nft_request = GenerateImageRequestModel(prompt="Test prompt")
            with pytest.raises(ChainGPTError):  # Should raise some error
                await client.nft.generate_image(nft_request)

            await client.close()

    @pytest.mark.asyncio
    @pytest.mark.integration
    async def test_concurrent_requests(self, api_key):
        """Test making concurrent requests to different services."""

        # Set up different responses for different endpoints
        def mock_post_side_effect(endpoint, json_data):
            if endpoint == "/chat/stream":
                return {
                    "status": True,
                    "message": "Success",
                    "data": {"bot": "LLM response"},
                }
            elif endpoint == "/nft/generate-image":
                return {
                    "status": True,
                    "message": "Image generated",
                    "data": {"type": "Buffer", "data": [1, 2, 3, 4]},
                }
            else:
                return {
                    "status": False,
                    "message": "Unknown endpoint",
                }

        with patch("chaingpt.utils.http.AsyncHTTPClient") as mock_http_class:
            mock_http_client = AsyncMock()
            mock_http_client.post.side_effect = mock_post_side_effect
            mock_http_class.return_value = mock_http_client

            client = ChainGPTClient(api_key=api_key)

            # Create concurrent tasks
            llm_task = client.llm.chat(
                LLMChatRequestModel(question="What is blockchain?")
            )
            nft_task = client.nft.generate_image(
                GenerateImageRequestModel(
                    prompt="A blockchain visualization",
                    model=NFTImageModel.VELOGEN,
                    height=512,
                    width=512,
                )
            )

            # Execute concurrently
            llm_response, nft_response = await asyncio.gather(llm_task, nft_task)

            # Verify both responses
            assert llm_response.status is True
            assert isinstance(nft_response.data, ImageBufferModel)

            await client.close()

    @pytest.mark.asyncio
    @pytest.mark.integration
    async def test_client_resource_management(self, api_key):
        """Test proper resource management with context managers."""
        # Set up success response
        mock_response = {
            "status": True,
            "message": "Success",
            "data": {"bot": "Response"},
        }

        with patch("chaingpt.utils.http.AsyncHTTPClient") as mock_http_class:
            mock_http_client = AsyncMock()
            mock_http_client.post.return_value = mock_response
            mock_http_class.return_value = mock_http_client

            # Test context manager usage
            async with ChainGPTClient(api_key=api_key) as client:
                request = LLMChatRequestModel(question="Test")
                response = await client.llm.chat(request)
                assert response.status is True

    def test_invalid_api_key_initialization(self):
        """Test that invalid API key raises appropriate error."""
        with pytest.raises(AuthenticationError):
            ChainGPTClient(api_key="")

        with pytest.raises(AuthenticationError):
            ChainGPTClient(api_key="")  # Empty string instead of None
