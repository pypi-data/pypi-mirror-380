"""Tests for LLM Service and Models."""

import pytest
import json
from pydantic import ValidationError as PydanticValidationError
from unittest.mock import AsyncMock

from chaingpt.services.llm import LLMService
from chaingpt.models.llm import (
    LLMChatRequestModel,
    LLMResponseModel,
    LLMErrorResponseModel,
    ContextInjectionModel,
    TokenInformationModel,
    SocialMediaUrlModel,
)
from chaingpt.types import ChatHistoryMode, AITone, PresetTone, BlockchainNetwork
from chaingpt.exceptions import ChainGPTError


class TestLLMModels:
    """Test cases for LLM models."""

    def test_social_media_url_model_valid(self):
        """Test valid SocialMediaUrlModel creation."""
        url_model = SocialMediaUrlModel(
            name="twitter", url="https://twitter.com/chaingpt"
        )
        assert url_model.name == "twitter"
        assert str(url_model.url) == "https://twitter.com/chaingpt"

    def test_social_media_url_model_invalid_url(self):
        """Test SocialMediaUrlModel with invalid URL."""
        with pytest.raises(PydanticValidationError):
            SocialMediaUrlModel(name="twitter", url="not-a-valid-url")

    def test_token_information_model_valid(self):
        """Test valid TokenInformationModel creation."""
        token_info = TokenInformationModel(
            tokenName="TestToken",
            tokenSymbol="TST",
            tokenAddress="0x1234567890abcdef",
            blockchain=[BlockchainNetwork.ETHEREUM, BlockchainNetwork.POLYGON],
        )
        assert token_info.token_name == "TestToken"
        assert token_info.token_symbol == "TST"
        assert token_info.blockchain == [
            BlockchainNetwork.ETHEREUM,
            BlockchainNetwork.POLYGON,
        ]

    def test_token_information_model_with_urls(self):
        """Test TokenInformationModel with URL fields."""
        token_info = TokenInformationModel(
            tokenName="TestToken",
            explorerUrl="https://etherscan.io/token/0x123",
            cmcUrl="https://coinmarketcap.com/currencies/test-token/",
            coingeckoUrl="https://coingecko.com/en/coins/test-token",
        )
        assert str(token_info.explorer_url) == "https://etherscan.io/token/0x123"
        assert (
            str(token_info.cmc_url)
            == "https://coinmarketcap.com/currencies/test-token/"
        )

    def test_context_injection_model_basic(self):
        """Test basic ContextInjectionModel creation."""
        context = ContextInjectionModel(
            companyName="Test Company",
            companyDescription="A test company",
            aiTone=AITone.PRE_SET_TONE,
            selectedTone=PresetTone.PROFESSIONAL,
        )
        assert context.company_name == "Test Company"
        assert context.ai_tone == AITone.PRE_SET_TONE
        assert context.selected_tone == PresetTone.PROFESSIONAL

    def test_context_injection_model_with_token(self):
        """Test ContextInjectionModel with token information."""
        token_info = TokenInformationModel(tokenName="TestToken", tokenSymbol="TST")
        context = ContextInjectionModel(
            companyName="Test Company", cryptoToken=True, tokenInformation=token_info
        )
        assert context.crypto_token is True
        assert context.token_information.token_name == "TestToken"

    def test_context_injection_model_preset_tone_validation(self):
        """Test ContextInjectionModel preset tone validation."""
        with pytest.raises(PydanticValidationError, match="selectedTone is required"):
            ContextInjectionModel(
                companyName="Test Company",
                aiTone=AITone.PRE_SET_TONE,
                # Missing selectedTone
            )

    def test_context_injection_model_custom_tone_validation(self):
        """Test ContextInjectionModel custom tone validation."""
        with pytest.raises(PydanticValidationError, match="customTone is required"):
            ContextInjectionModel(
                companyName="Test Company",
                aiTone=AITone.CUSTOM_TONE,
                # Missing customTone
            )

    def test_context_injection_model_crypto_token_validation(self):
        """Test ContextInjectionModel crypto token validation."""
        with pytest.raises(
            PydanticValidationError, match="tokenInformation is required"
        ):
            ContextInjectionModel(
                companyName="Test Company",
                cryptoToken=True,
                # Missing tokenInformation
            )

    def test_llm_chat_request_model_basic(self):
        """Test basic LLMChatRequestModel creation."""
        request = LLMChatRequestModel(question="What is blockchain?")
        assert request.question == "What is blockchain?"
        assert request.model == "general_assistant"
        assert request.chat_history == ChatHistoryMode.OFF

    def test_llm_chat_request_model_with_context(self):
        """Test LLMChatRequestModel with context injection."""
        context = ContextInjectionModel(
            companyName="Test Company",
            aiTone=AITone.PRE_SET_TONE,
            selectedTone=PresetTone.FRIENDLY,
        )
        request = LLMChatRequestModel(
            question="Tell me about our company",
            useCustomContext=True,
            contextInjection=context,
            chatHistory=ChatHistoryMode.ON,
            sdkUniqueId="test-unique-id",
        )
        assert request.use_custom_context is True
        assert request.context_injection.company_name == "Test Company"
        assert request.chat_history == ChatHistoryMode.ON

    def test_llm_chat_request_model_invalid_question(self):
        """Test LLMChatRequestModel with invalid question."""
        with pytest.raises(PydanticValidationError):
            LLMChatRequestModel(question="")  # Empty question

        with pytest.raises(PydanticValidationError):
            LLMChatRequestModel(question="x" * 10001)  # Too long

    def test_llm_chat_request_model_invalid_model(self):
        """Test LLMChatRequestModel with invalid model."""
        with pytest.raises(
            PydanticValidationError, match="only 'general_assistant' model is supported"
        ):
            LLMChatRequestModel(question="Test question", model="invalid_model")

    def test_llm_chat_request_model_context_validation(self):
        """Test LLMChatRequestModel context validation."""
        with pytest.raises(
            PydanticValidationError, match="contextInjection is required"
        ):
            LLMChatRequestModel(
                question="Test question",
                useCustomContext=True,
                # Missing contextInjection
            )

    def test_llm_chat_request_model_to_api_dict(self):
        """Test LLMChatRequestModel to_api_dict method."""
        token_info = TokenInformationModel(
            tokenName="TestToken",
            tokenSymbol="TST",
            blockchain=[BlockchainNetwork.ETHEREUM],
        )
        social_media = [
            SocialMediaUrlModel(name="twitter", url="https://twitter.com/test")
        ]
        context = ContextInjectionModel(
            companyName="Test Company",
            cryptoToken=True,
            tokenInformation=token_info,
            socialMediaUrls=social_media,
            aiTone=AITone.PRE_SET_TONE,
            selectedTone=PresetTone.PROFESSIONAL,
        )
        request = LLMChatRequestModel(
            question="Test question",
            useCustomContext=True,
            contextInjection=context,
            chatHistory=ChatHistoryMode.ON,
            sdkUniqueId="test-id",
        )

        api_dict = request.to_api_dict()

        assert api_dict["question"] == "Test question"
        assert api_dict["useCustomContext"] is True
        assert api_dict["chatHistory"] == "on"
        assert api_dict["sdkUniqueId"] == "test-id"
        assert "contextInjection" in api_dict
        assert api_dict["contextInjection"]["companyName"] == "Test Company"
        assert "tokenInformation" in api_dict["contextInjection"]
        assert "socialMediaUrls" in api_dict["contextInjection"]

    def test_llm_response_model(self):
        """Test LLMResponseModel creation."""
        response_data = {
            "status": True,
            "message": "Success",
            "data": {"bot": "This is a test response."},
        }
        response = LLMResponseModel(**response_data)

        assert response.status is True
        assert response.message == "Success"
        assert response.data.bot == "This is a test response."

    def test_llm_error_response_model(self):
        """Test LLMErrorResponseModel creation."""
        error_data = {
            "status": False,
            "message": "API Error occurred",
            "statusCode": 400,
        }
        error_response = LLMErrorResponseModel(**error_data)

        assert error_response.status is False
        assert error_response.message == "API Error occurred"
        assert error_response.statusCode == 400


class TestLLMService:
    """Test cases for LLMService."""

    @pytest.fixture
    def llm_service(self, mock_http_client):
        """Create LLMService instance for testing."""
        return LLMService(mock_http_client)

    @pytest.mark.asyncio
    async def test_chat_success(self, llm_service, mock_http_client, mock_llm_response):
        """Test successful chat request."""
        request = LLMChatRequestModel(question="What is blockchain?")
        mock_http_client.post.return_value = mock_llm_response

        response = await llm_service.chat(request)

        assert isinstance(response, LLMResponseModel)
        assert response.status is True
        assert response.data.bot == "This is a test response from the AI assistant."
        mock_http_client.post.assert_called_once()

    @pytest.mark.asyncio
    async def test_chat_invalid_request_type(self, llm_service):
        """Test chat with invalid request type."""
        with pytest.raises(
            TypeError, match="must be an instance of LLMChatRequestModel"
        ):
            await llm_service.chat({"question": "test"})

    @pytest.mark.asyncio
    async def test_chat_empty_response(self, llm_service, mock_http_client):
        """Test chat with empty response."""
        request = LLMChatRequestModel(question="What is blockchain?")
        mock_http_client.post.return_value = None

        with pytest.raises(ChainGPTError, match="Received empty response"):
            await llm_service.chat(request)

    @pytest.mark.asyncio
    async def test_chat_non_dict_response(self, llm_service, mock_http_client):
        """Test chat with non-dict response."""
        request = LLMChatRequestModel(question="What is blockchain?")
        mock_http_client.post.return_value = "not a dict"

        with pytest.raises(ChainGPTError, match="Expected dict response"):
            await llm_service.chat(request)

    @pytest.mark.asyncio
    async def test_chat_error_response(
        self, llm_service, mock_http_client, mock_error_response
    ):
        """Test chat with error response."""
        request = LLMChatRequestModel(question="What is blockchain?")
        mock_http_client.post.return_value = mock_error_response

        with pytest.raises(ChainGPTError, match="API Error occurred"):
            await llm_service.chat(request)

    @pytest.mark.asyncio
    async def test_chat_unexpected_response_structure(
        self, llm_service, mock_http_client
    ):
        """Test chat with unexpected response structure."""
        request = LLMChatRequestModel(question="What is blockchain?")
        mock_http_client.post = AsyncMock(return_value={"unexpected": "structure"})

        with pytest.raises(ChainGPTError, match="Unexpected API response"):
            await llm_service.chat(request)

    @pytest.mark.asyncio
    async def test_chat_json_decode_error(self, llm_service, mock_http_client):
        """Test chat with JSON decode error."""
        request = LLMChatRequestModel(question="What is blockchain?")
        mock_http_client.post.side_effect = json.JSONDecodeError("Invalid JSON", "", 0)

        with pytest.raises(ChainGPTError, match="Invalid JSON response"):
            await llm_service.chat(request)

    @pytest.mark.asyncio
    async def test_chat_unexpected_exception(self, llm_service, mock_http_client):
        """Test chat with unexpected exception."""
        request = LLMChatRequestModel(question="What is blockchain?")
        mock_http_client.post.side_effect = Exception("Unexpected error")

        with pytest.raises(ChainGPTError, match="Unexpected error during chat request"):
            await llm_service.chat(request)

    @pytest.mark.asyncio
    async def test_stream_chat_success(self, llm_service, mock_http_client):
        """Test successful streaming chat."""
        request = LLMChatRequestModel(question="What is blockchain?")

        async def mock_stream_response():
            yield b"chunk1"
            yield b"chunk2"
            yield b"chunk3"

        mock_http_client.stream_post.return_value = mock_stream_response()

        chunks = []
        async for chunk in llm_service.stream_chat(request):
            chunks.append(chunk)

        assert chunks == [b"chunk1", b"chunk2", b"chunk3"]
        mock_http_client.stream_post.assert_called_once()

    @pytest.mark.asyncio
    async def test_stream_chat_invalid_request_type(self, llm_service):
        """Test streaming chat with invalid request type."""
        with pytest.raises(
            TypeError, match="must be an instance of LLMChatRequestModel"
        ):
            async for chunk in llm_service.stream_chat({"question": "test"}):
                pass

    @pytest.mark.asyncio
    async def test_stream_chat_exception(self, llm_service, mock_http_client):
        """Test streaming chat with exception."""
        request = LLMChatRequestModel(question="What is blockchain?")
        mock_http_client.stream_post.side_effect = Exception("Stream error")

        with pytest.raises(ChainGPTError, match="Streaming chat error"):
            async for chunk in llm_service.stream_chat(request):
                pass

    @pytest.mark.asyncio
    async def test_chat_with_context_injection(
        self, llm_service, mock_http_client, mock_llm_response
    ):
        """Test chat with context injection."""
        context = ContextInjectionModel(
            companyName="Test Company",
            aiTone=AITone.PRE_SET_TONE,
            selectedTone=PresetTone.PROFESSIONAL,
        )
        request = LLMChatRequestModel(
            question="Tell me about our company",
            useCustomContext=True,
            contextInjection=context,
        )
        mock_http_client.post.return_value = mock_llm_response

        response = await llm_service.chat(request)

        assert isinstance(response, LLMResponseModel)
        # Check that the request was properly serialized
        call_args = mock_http_client.post.call_args
        assert call_args[1]["json_data"]["useCustomContext"] is True
        assert "contextInjection" in call_args[1]["json_data"]

    @pytest.mark.asyncio
    async def test_chat_with_all_parameters(
        self, llm_service, mock_http_client, mock_llm_response
    ):
        """Test chat with all parameters."""
        token_info = TokenInformationModel(
            tokenName="TestToken",
            tokenSymbol="TST",
            blockchain=[BlockchainNetwork.ETHEREUM],
        )
        social_media = [
            SocialMediaUrlModel(name="twitter", url="https://twitter.com/test")
        ]
        context = ContextInjectionModel(
            companyName="Test Company",
            companyDescription="A test company",
            cryptoToken=True,
            tokenInformation=token_info,
            socialMediaUrls=social_media,
            aiTone=AITone.CUSTOM_TONE,
            customTone="Be very technical and detailed",
        )
        request = LLMChatRequestModel(
            question="Explain our tokenomics",
            useCustomContext=True,
            contextInjection=context,
            chatHistory=ChatHistoryMode.ON,
            sdkUniqueId="test-session-123",
        )
        mock_http_client.post.return_value = mock_llm_response

        response = await llm_service.chat(request)

        assert isinstance(response, LLMResponseModel)
        # Verify the API call was made with correct parameters
        call_args = mock_http_client.post.call_args
        api_data = call_args[1]["json_data"]

        assert api_data["question"] == "Explain our tokenomics"
        assert api_data["useCustomContext"] is True
        assert api_data["chatHistory"] == "on"
        assert api_data["sdkUniqueId"] == "test-session-123"
        assert "contextInjection" in api_data
        assert api_data["contextInjection"]["companyName"] == "Test Company"
