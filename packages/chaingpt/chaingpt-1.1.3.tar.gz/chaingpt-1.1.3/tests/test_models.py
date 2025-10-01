"""Tests for ChainGPT SDK models."""

import pytest
from pydantic import ValidationError as PydanticValidationError
from chaingpt.models.llm import (
    LLMChatRequestModel,
    LLMResponseModel,
    ContextInjectionModel,
    TokenInformationModel,
    SocialMediaUrlModel,
)
from chaingpt.models.nft import (
    GenerateImageRequestModel,
    GenerateNFTQueueRequestModel,
    TraitModel,
    TraitValueItemModel,
    MintNFTRequestModel,
    EnhancePromptRequestModel,
)
from chaingpt.models.smart_contract import SmartContractGeneratorRequestModel
from chaingpt.models.auditor import SmartContractAuditRequestModel
from chaingpt.types import (
    ChatHistoryMode,
    AITone,
    PresetTone,
    BlockchainNetwork,
    NFTImageModel,
    ImageEnhanceOption,
)


class TestLLMModels:
    """Test LLM-related models."""

    def test_social_media_url_model_valid(self):
        """Test valid SocialMediaUrlModel."""
        model = SocialMediaUrlModel(name="twitter", url="https://twitter.com/chaingpt")
        assert model.name == "twitter"
        assert str(model.url) == "https://twitter.com/chaingpt"

    def test_social_media_url_model_invalid_url(self):
        """Test SocialMediaUrlModel with invalid URL."""
        with pytest.raises(PydanticValidationError):
            SocialMediaUrlModel(name="twitter", url="invalid-url")

    def test_token_information_model_comprehensive(self):
        """Test comprehensive TokenInformationModel."""
        model = TokenInformationModel(
            tokenName="ChainGPT",
            tokenSymbol="CGPT",
            tokenAddress="0x25931894a86d47441213199621f1f2994e1c39aa",
            explorerUrl="https://etherscan.io/token/0x25931894a86d47441213199621f1f2994e1c39aa",
            cmcUrl="https://coinmarketcap.com/currencies/chaingpt/",
            blockchain=[BlockchainNetwork.ETHEREUM, BlockchainNetwork.BSC],
        )
        assert model.token_name == "ChainGPT"
        assert model.token_symbol == "CGPT"
        assert len(model.blockchain) == 2

    def test_context_injection_model_with_preset_tone(self):
        """Test ContextInjectionModel with preset tone."""
        model = ContextInjectionModel(
            companyName="ChainGPT",
            companyDescription="AI-powered blockchain tools",
            aiTone=AITone.PRE_SET_TONE,
            selectedTone=PresetTone.PROFESSIONAL,
        )
        assert model.ai_tone == AITone.PRE_SET_TONE
        assert model.selected_tone == PresetTone.PROFESSIONAL

    def test_context_injection_model_with_custom_tone(self):
        """Test ContextInjectionModel with custom tone."""
        model = ContextInjectionModel(
            companyName="ChainGPT",
            aiTone=AITone.CUSTOM_TONE,
            customTone="Be technical and detailed in responses",
        )
        assert model.ai_tone == AITone.CUSTOM_TONE
        assert model.custom_tone == "Be technical and detailed in responses"

    def test_context_injection_validation_errors(self):
        """Test ContextInjectionModel validation errors."""
        # Missing selectedTone for PRE_SET_TONE
        with pytest.raises(PydanticValidationError, match="selectedTone is required"):
            ContextInjectionModel(companyName="Test", aiTone=AITone.PRE_SET_TONE)

        # Missing customTone for CUSTOM_TONE
        with pytest.raises(PydanticValidationError, match="customTone is required"):
            ContextInjectionModel(companyName="Test", aiTone=AITone.CUSTOM_TONE)

        # Missing tokenInformation when cryptoToken is True
        with pytest.raises(
            PydanticValidationError, match="tokenInformation is required"
        ):
            ContextInjectionModel(companyName="Test", cryptoToken=True)

    def test_llm_chat_request_model_basic(self):
        """Test basic LLMChatRequestModel."""
        model = LLMChatRequestModel(question="What is blockchain?")
        assert model.question == "What is blockchain?"
        assert model.model == "general_assistant"
        assert model.chat_history == ChatHistoryMode.OFF

    def test_llm_chat_request_model_with_all_fields(self):
        """Test LLMChatRequestModel with all fields."""
        context = ContextInjectionModel(
            companyName="Test",
            aiTone=AITone.PRE_SET_TONE,
            selectedTone=PresetTone.FRIENDLY,
        )
        model = LLMChatRequestModel(
            question="Tell me about our company",
            chatHistory=ChatHistoryMode.ON,
            sdkUniqueId="test-session-123",
            useCustomContext=True,
            contextInjection=context,
        )
        assert model.use_custom_context is True
        assert model.context_injection is not None

    def test_llm_chat_request_validation_errors(self):
        """Test LLMChatRequestModel validation errors."""
        # Empty question
        with pytest.raises(PydanticValidationError):
            LLMChatRequestModel(question="")

        # Invalid model
        with pytest.raises(PydanticValidationError):
            LLMChatRequestModel(question="Test", model="invalid_model")

        # useCustomContext True without contextInjection
        with pytest.raises(
            PydanticValidationError, match="contextInjection is required"
        ):
            LLMChatRequestModel(question="Test", useCustomContext=True)

    def test_llm_response_model(self):
        """Test LLMResponseModel."""
        data = {
            "status": True,
            "message": "Success",
            "data": {"bot": "This is the AI response"},
        }
        model = LLMResponseModel(**data)
        assert model.status is True
        assert model.data.bot == "This is the AI response"

    def test_token_information_model(self):
        """Test TokenInformationModel."""
        model = TokenInformationModel(
            tokenName="ChainGPT",
            tokenSymbol="CGPT",
            blockchain=[BlockchainNetwork.ETHEREUM],
        )
        assert model.token_name == "ChainGPT"
        assert model.token_symbol == "CGPT"


class TestNFTModels:
    """Test NFT-related models."""

    def test_trait_value_item_model(self):
        """Test TraitValueItemModel."""
        model = TraitValueItemModel(value="Blue", ratio=50)
        assert model.value == "Blue"
        assert model.ratio == 50

    def test_trait_model(self):
        """Test TraitModel."""
        values = [
            TraitValueItemModel(value="Blue", ratio=50),
            TraitValueItemModel(value="Red", ratio=30),
        ]
        model = TraitModel(trait_type="Background", value=values)
        assert model.trait_type == "Background"
        assert len(model.value) == 2

    def test_generate_image_request_model(self):
        """Test GenerateImageRequestModel."""
        model = GenerateImageRequestModel(
            prompt="A beautiful landscape",
            model=NFTImageModel.VELOGEN,
            enhance=ImageEnhanceOption.ENHANCE_1X,
            height=512,
            width=512,
        )
        assert model.prompt == "A beautiful landscape"
        assert model.model == NFTImageModel.VELOGEN

    def test_generate_nft_queue_request_model(self):
        """Test GenerateNFTQueueRequestModel."""
        traits = [
            TraitModel(
                trait_type="Background",
                value=[TraitValueItemModel(value="Blue", ratio=50)],
            )
        ]
        model = GenerateNFTQueueRequestModel(
            prompt="NFT Collection",
            model=NFTImageModel.NEBULA_FORGE_XL,
            traits=traits,
            height=512,
            width=512,
            walletAddress="0x1234567890abcdef",
            chainId=1,
            amount=1,
        )
        assert len(model.traits) == 1

    def test_mint_nft_request_model(self):
        """Test MintNFTRequestModel."""
        model = MintNFTRequestModel(
            name="Test NFT",
            description="This is a test NFT",
            ids=[1, 2],
            collectionId="col_123",
            symbol=BlockchainNetwork.ETHEREUM,
        )
        assert model.collectionId == "col_123"
        assert model.symbol == BlockchainNetwork.ETHEREUM

    def test_enhance_prompt_request_model(self):
        """Test EnhancePromptRequestModel."""
        model = EnhancePromptRequestModel(prompt="Simple prompt")
        assert model.prompt == "Simple prompt"


class TestSmartContractModels:
    """Test Smart Contract-related models."""

    def test_smart_contract_generator_request_model(self):
        """Test SmartContractGeneratorRequestModel."""
        model = SmartContractGeneratorRequestModel(question="Create an ERC20 token")
        assert model.question == "Create an ERC20 token"


class TestAuditorModels:
    """Test Auditor-related models."""

    def test_smart_contract_audit_request_model(self):
        """Test SmartContractAuditRequestModel."""
        contract_code = """
        pragma solidity ^0.8.0;
        contract SimpleToken {
            mapping(address => uint256) public balances;
        }
        """
        model = SmartContractAuditRequestModel(
            question=f"Is this contract secure? {contract_code}",
        )
        assert model.model == "smart_contract_auditor"


class TestModelSerialization:
    """Test model serialization and deserialization."""

    def test_llm_request_to_api_dict(self):
        """Test LLMChatRequestModel to_api_dict method."""
        token_info = TokenInformationModel(
            tokenName="TestToken",
            tokenSymbol="TST",
            blockchain=[BlockchainNetwork.ETHEREUM],
        )
        context = ContextInjectionModel(
            companyName="Test Company",
            cryptoToken=True,
            tokenInformation=token_info,
            aiTone=AITone.PRE_SET_TONE,
            selectedTone=PresetTone.PROFESSIONAL,
        )
        model = LLMChatRequestModel(
            question="Test question",
            useCustomContext=True,
            contextInjection=context,
            chatHistory=ChatHistoryMode.ON,
        )

        api_dict = model.to_api_dict()

        assert api_dict["question"] == "Test question"
        assert api_dict["useCustomContext"] is True
        assert api_dict["chatHistory"] == "on"
        assert "contextInjection" in api_dict
        assert api_dict["contextInjection"]["companyName"] == "Test Company"

    def test_nft_model_serialization(self):
        """Test NFT model serialization."""
        model = GenerateImageRequestModel(
            prompt="Test image",
            model=NFTImageModel.VELOGEN,
            enhance=ImageEnhanceOption.ORIGINAL,
            height=512,
            width=512,
        )

        serialized = model.model_dump(by_alias=True, exclude_none=True)

        assert serialized["prompt"] == "Test image"
        assert serialized["model"] == "velogen"
        assert serialized["enhance"] == "original"

    def test_model_with_aliases(self):
        """Test models with field aliases."""
        model = TokenInformationModel(
            tokenName="Test",  # alias for token_name
            tokenSymbol="TST",  # alias for token_symbol
        )

        # Test both attribute access and alias access
        assert model.token_name == "Test"
        assert model.token_symbol == "TST"

        # Test serialization with aliases
        serialized = model.model_dump(by_alias=True)
        assert "tokenName" in serialized
        assert "tokenSymbol" in serialized
