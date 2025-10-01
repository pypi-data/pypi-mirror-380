"""Tests for NFT Service."""

import pytest
from unittest.mock import Mock

from chaingpt.services.nft import NFTService
from chaingpt.models.nft import (
    GenerateImageRequestModel,
    GenerateImageResponseModel,
    GenerateNFTQueueRequestModel,
    GenerateNFTQueueResponseModel,
    NFTProgressResponseModel,
    MintNFTRequestModel,
    MintNFTResponseModel,
    EnhancePromptRequestModel,
    EnhancePromptResponseModel,
    GetChainsResponseModel,
    ContractABIResponseModel,
    TraitModel,
    TraitValueItemModel,
    ImageBufferModel,
)
from chaingpt.types import NFTImageModel, ImageEnhanceOption


class TestNFTService:
    """Test cases for NFTService."""

    @pytest.fixture
    def nft_service(self, mock_http_client):
        """Create NFTService instance for testing."""
        return NFTService(mock_http_client)

    @pytest.mark.asyncio
    async def test_generate_image_success(self, nft_service, mock_http_client):
        """Test successful image generation."""
        request = GenerateImageRequestModel(
            prompt="A beautiful landscape",
            model=NFTImageModel.VELOGEN,
            enhance=ImageEnhanceOption.ORIGINAL,
            height=512,
            width=512,
        )

        mock_response = {
            "data": {"type": "Buffer", "data": [1, 2, 3, 4]},  # Mock image data
        }
        mock_http_client.post.return_value = mock_response

        response = await nft_service.generate_image(request)

        assert isinstance(response, GenerateImageResponseModel)
        assert isinstance(response.data, ImageBufferModel)
        mock_http_client.post.assert_called_once_with(
            "/nft/generate-image",
            json_data=request.model_dump(by_alias=True, exclude_none=True),
        )

    @pytest.mark.asyncio
    async def test_generate_image_with_image_to_image(
        self, nft_service, mock_http_client
    ):
        """Test image generation with image-to-image features."""
        request = GenerateImageRequestModel(
            prompt="A futuristic version of this character",
            model=NFTImageModel.NEBULA_FORGE_XL,
            height=1024,
            width=1024,
            image="https://example.com/reference-image.jpg",
            isCharacterPreserve=True,
        )

        mock_response = {
            "data": {"type": "Buffer", "data": [1, 2, 3, 4]},
        }
        mock_http_client.post.return_value = mock_response

        response = await nft_service.generate_image(request)

        assert isinstance(response, GenerateImageResponseModel)
        mock_http_client.post.assert_called_once_with(
            "/nft/generate-image",
            json_data=request.model_dump(by_alias=True, exclude_none=True),
        )

    @pytest.mark.asyncio
    async def test_generate_image_invalid_request_type(self, nft_service):
        """Test generate image with invalid request type."""
        with pytest.raises(
            TypeError, match="must be an instance of GenerateImageRequestModel"
        ):
            await nft_service.generate_image({"prompt": "test"})

    @pytest.mark.asyncio
    async def test_generate_nft_queue_success(self, nft_service, mock_http_client):
        """Test successful NFT queue generation."""
        traits = [
            TraitModel(
                trait_type="Background",
                value=[
                    TraitValueItemModel(value="Blue", ratio=50),
                    TraitValueItemModel(value="Red", ratio=30),
                ],
            )
        ]

        request = GenerateNFTQueueRequestModel(
            prompt="A collection of cool NFTs",
            model=NFTImageModel.NEBULA_FORGE_XL,
            traits=traits,
            walletAddress="0x1234567890abcdef1234567890abcdef12345678",
            chainId=1,
            amount=10,
            height=512,
            width=512,
        )

        mock_response = {
            "statusCode": 201,
            "message": "NFT generation queued successfully",
            "data": {"collectionId": "collection_123"},
        }
        mock_http_client.post.return_value = mock_response

        response = await nft_service.generate_nft_queue(request)

        assert isinstance(response, GenerateNFTQueueResponseModel)
        assert response.data.collectionId == "collection_123"
        assert response.statusCode == 201
        mock_http_client.post.assert_called_once_with(
            "/nft/generate-nft-queue",
            json_data=request.model_dump(by_alias=True, exclude_none=True),
        )

    @pytest.mark.asyncio
    async def test_get_progress_success(self, nft_service, mock_http_client):
        """Test successful progress check."""
        collection_id = "collection_123"

        mock_response = Mock()
        mock_response.json.return_value = {
            "statusCode": 200,
            "message": "Progress retrieved successfully",
            "data": {"generated": False, "progress": 50},
        }
        mock_http_client._request.return_value = mock_response

        response = await nft_service.get_progress(collection_id)

        assert isinstance(response, NFTProgressResponseModel)
        assert response.data.generated is False
        assert response.data.progress == 50
        mock_http_client._request.assert_called_once_with(
            "GET", f"/nft/progress/{collection_id}"
        )

    @pytest.mark.asyncio
    async def test_get_progress_completed(self, nft_service, mock_http_client):
        """Test progress check when generation is completed."""
        collection_id = "collection_123"

        mock_response = Mock()
        mock_response.json.return_value = {
            "statusCode": 200,
            "message": "Request Successful",
            "data": {
                "images": ["https://ipfs.io/ipfs/Qm...1.png"],
                "generated": True,
            },
        }
        mock_http_client._request.return_value = mock_response

        response = await nft_service.get_progress(collection_id)

        assert isinstance(response, NFTProgressResponseModel)
        assert response.data.generated is True
        assert response.data.images == ["https://ipfs.io/ipfs/Qm...1.png"]
        mock_http_client._request.assert_called_once_with(
            "GET", f"/nft/progress/{collection_id}"
        )

    @pytest.mark.asyncio
    async def test_enhance_prompt_success(self, nft_service, mock_http_client):
        """Test successful prompt enhancement."""
        request = EnhancePromptRequestModel(prompt="A simple landscape")

        mock_response = {
            "statusCode": 200,
            "message": "Prompt enhanced successfully",
            "data": {
                "enhancedPrompt": "A breathtaking, detailed landscape with rolling hills and vibrant colors"
            },
        }
        mock_http_client.post.return_value = mock_response

        response = await nft_service.enhance_prompt(request)

        assert isinstance(response, EnhancePromptResponseModel)
        assert (
            response.data.enhancedPrompt
            == "A breathtaking, detailed landscape with rolling hills and vibrant colors"
        )
        mock_http_client.post.assert_called_once_with(
            "/nft/enhancePrompt",
            json_data=request.model_dump(by_alias=True, exclude_none=True),
        )

    @pytest.mark.asyncio
    async def test_get_chains_success(self, nft_service, mock_http_client):
        """Test successful chains retrieval."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "statusCode": 200,
            "message": "Chains retrieved successfully",
            "data": {
                "chains": [
                    {
                        "chainId": 1,
                        "chainName": "Ethereum",
                        "network": "ethereum",
                        "networkType": "Mainnet",
                    },
                    {
                        "chainId": 137,
                        "chainName": "Polygon",
                        "network": "matic",
                        "networkType": "Mainnet",
                    },
                ]
            },
        }
        mock_http_client._request.return_value = mock_response

        response = await nft_service.get_chains()

        assert isinstance(response, GetChainsResponseModel)
        assert len(response.data.chains) == 2
        assert response.data.chains[0].chainId == 1
        assert response.data.chains[0].chainName == "Ethereum"
        mock_http_client._request.assert_called_once_with(
            "GET", "/nft/get-chains", params=None
        )

    @pytest.mark.asyncio
    async def test_get_chains_with_testnet(self, nft_service, mock_http_client):
        """Test chains retrieval with testnet parameter."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "statusCode": 200,
            "message": "Chains retrieved successfully",
            "data": {
                "chains": [
                    {
                        "chainId": 97,
                        "chainName": "BSC Testnet",
                        "network": "bsc-testnet",
                        "networkType": "Testnet",
                    }
                ]
            },
        }
        mock_http_client._request.return_value = mock_response

        response = await nft_service.get_chains(test_net=True)

        assert isinstance(response, GetChainsResponseModel)
        mock_http_client._request.assert_called_once_with(
            "GET", "/nft/get-chains", params={"testNet": True}
        )

    @pytest.mark.asyncio
    async def test_get_abi_success(self, nft_service, mock_http_client):
        """Test successful contract ABI retrieval."""
        mock_response = {
            "statusCode": 200,
            "message": "ABI retrieved successfully",
            "data": [{"type": "function", "name": "mint", "inputs": []}],
        }
        mock_http_client._request.return_value = mock_response

        response = await nft_service.get_abi()

        assert isinstance(response, ContractABIResponseModel)
        assert len(response.data) == 1
        assert response.data[0]["type"] == "function"
        assert response.data[0]["name"] == "mint"
        mock_http_client._request.assert_called_once_with("GET", "/nft/abi")

    @pytest.mark.asyncio
    async def test_mint_nft_metadata_success(self, nft_service, mock_http_client):
        """Test successful NFT mint metadata retrieval."""
        request = MintNFTRequestModel(
            collectionId="collection_123",
            name="Test NFT",
            description="A test NFT",
            symbol="TEST",
            ids=[1],
        )

        mock_response = {
            "statusCode": 201,
            "message": "NFT metadata created successfully",
            "data": {
                "_id": "68a6b5e60153a6ed12345678",
                "name": "Test NFT",
                "description": "A test NFT",
                "image": "ipfs://Qm...",
                "attributes": [],
                "collectionId": "collection_123",
                "transaction": None,
                "__v": 0,
                "createdAt": "2024-01-15T10:30:00.000Z",
                "updatedAt": "2024-01-15T10:30:00.000Z",
            },
        }
        mock_http_client.post.return_value = mock_response

        response = await nft_service.mint_nft_metadata(request)

        assert isinstance(response, MintNFTResponseModel)
        assert response.data._id == "68a6b5e60153a6ed12345678"
        assert response.data.name == "Test NFT"
        assert response.data.description == "A test NFT"
        assert response.data.image == "ipfs://Qm..."
        mock_http_client.post.assert_called_once_with(
            "/nft/mint-nft",
            json_data=request.model_dump(by_alias=True, exclude_none=True),
        )


class TestNFTModels:
    """Test cases for NFT models."""

    def test_trait_value_item_model(self):
        """Test TraitValueItemModel creation."""
        trait_value = TraitValueItemModel(value="Blue", ratio=50)
        assert trait_value.value == "Blue"
        assert trait_value.ratio == 50

    def test_trait_model(self):
        """Test TraitModel creation."""
        values = [
            TraitValueItemModel(value="Blue", ratio=50),
            TraitValueItemModel(value="Red", ratio=30),
        ]
        trait = TraitModel(trait_type="Background", value=values)
        assert trait.trait_type == "Background"
        assert len(trait.value) == 2
        assert trait.value[0].value == "Blue"

    def test_generate_image_request_model(self):
        """Test GenerateImageRequestModel creation."""
        request = GenerateImageRequestModel(
            prompt="A beautiful landscape",
            model=NFTImageModel.VELOGEN,
            enhance=ImageEnhanceOption.ENHANCE_1X,
            height=512,
            width=512,
        )
        assert request.prompt == "A beautiful landscape"
        assert request.model == NFTImageModel.VELOGEN
        assert request.enhance == ImageEnhanceOption.ENHANCE_1X

    def test_generate_image_request_model_with_image_to_image(self):
        """Test GenerateImageRequestModel with image-to-image features."""
        request = GenerateImageRequestModel(
            prompt="A futuristic version",
            model=NFTImageModel.NEBULA_FORGE_XL,
            height=1024,
            width=1024,
            image="https://example.com/image.jpg",
            isCharacterPreserve=True,
        )
        assert request.prompt == "A futuristic version"
        assert str(request.image) == "https://example.com/image.jpg"
        assert request.isCharacterPreserve is True

    def test_generate_nft_queue_request_model(self):
        """Test GenerateNFTQueueRequestModel creation."""
        traits = [
            TraitModel(
                trait_type="Background",
                value=[TraitValueItemModel(value="Blue", ratio=50)],
            )
        ]
        request = GenerateNFTQueueRequestModel(
            prompt="A collection of NFTs",
            model=NFTImageModel.NEBULA_FORGE_XL,
            traits=traits,
            walletAddress="0x1234567890abcdef1234567890abcdef12345678",
            chainId=1,
            amount=10,
            height=512,
            width=512,
        )
        assert request.prompt == "A collection of NFTs"
        assert request.model == NFTImageModel.NEBULA_FORGE_XL
        assert len(request.traits) == 1

    def test_mint_nft_request_model(self):
        """Test MintNFTRequestModel creation."""
        request = MintNFTRequestModel(
            collectionId="collection_123",
            name="My NFT",
            description="A unique NFT",
            ids=[1, 2],
            symbol="MNFT",
        )
        assert request.collectionId == "collection_123"

    def test_enhance_prompt_request_model(self):
        """Test EnhancePromptRequestModel creation."""
        request = EnhancePromptRequestModel(prompt="A simple landscape")
        assert request.prompt == "A simple landscape"
