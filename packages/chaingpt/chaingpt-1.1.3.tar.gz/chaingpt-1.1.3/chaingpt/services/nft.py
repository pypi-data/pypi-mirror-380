"""NFT Service for ChainGPT API."""

from chaingpt.exceptions import ChainGPTError
from .base import BaseService
from ..models.nft import (
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
)

# NFT Endpoints
GENERATE_IMAGE_ENDPOINT = "/nft/generate-image"
GENERATE_NFT_QUEUE_ENDPOINT = "/nft/generate-nft-queue"
PROGRESS_ENDPOINT_TEMPLATE = "/nft/progress/{collectionId}"
MINT_NFT_ENDPOINT = "/nft/mint-nft"
ENHANCE_PROMPT_ENDPOINT = "/nft/enhancePrompt"
GET_CHAINS_ENDPOINT = "/nft/get-chains"
GET_ABI_ENDPOINT = "/nft/abi"


class NFTService(BaseService):
    """Service for interacting with the ChainGPT NFT Generator API."""

    async def generate_image(
        self, request_data: GenerateImageRequestModel
    ) -> GenerateImageResponseModel:
        """Generates an image synchronously based on the given prompt and model."""
        try:
            if not isinstance(request_data, GenerateImageRequestModel):
                raise TypeError(
                    "request_data must be an instance of GenerateImageRequestModel"
                )

            api_payload = request_data.model_dump(by_alias=True, exclude_none=True)

            response_json = await self._http_client.post(
                GENERATE_IMAGE_ENDPOINT, json_data=api_payload
            )
            return GenerateImageResponseModel(**response_json)
        except ChainGPTError as e:
            self._http_client.logger.error(f"ChainGPT API error in generate_image: {e}")
            raise
        except Exception as e:
            self._http_client.logger.error(f"Error generating image: {e}")
            raise

    async def generate_nft_queue(
        self, request_data: GenerateNFTQueueRequestModel
    ) -> GenerateNFTQueueResponseModel:
        """Initiates an NFT image generation job."""
        if not isinstance(request_data, GenerateNFTQueueRequestModel):
            raise TypeError(
                "request_data must be an instance of GenerateNFTQueueRequestModel"
            )

        api_payload = request_data.model_dump(by_alias=True, exclude_none=True)
        self._http_client.logger.debug(
            f"Sending generate NFT queue request to {GENERATE_NFT_QUEUE_ENDPOINT}"
        )

        response_json = await self._http_client.post(
            GENERATE_NFT_QUEUE_ENDPOINT, json_data=api_payload
        )
        return GenerateNFTQueueResponseModel(**response_json)

    async def get_progress(self, collection_id: str) -> NFTProgressResponseModel:
        """Checks the status and progress of a queued NFT generation job."""
        endpoint = PROGRESS_ENDPOINT_TEMPLATE.format(collectionId=collection_id)
        self._http_client.logger.debug(f"Sending get progress request to {endpoint}")

        response_json = await self._http_client._request("GET", endpoint)
        return NFTProgressResponseModel(**response_json.json())

    async def mint_nft_metadata(
        self, request_data: MintNFTRequestModel
    ) -> MintNFTResponseModel:
        """Finalizes NFT creation by generating metadata for minting."""
        if not isinstance(request_data, MintNFTRequestModel):
            raise TypeError("request_data must be an instance of MintNFTRequestModel")

        api_payload = request_data.model_dump(by_alias=True, exclude_none=True)
        self._http_client.logger.debug(
            f"Sending mint NFT metadata request to {MINT_NFT_ENDPOINT}"
        )

        response_json = await self._http_client.post(
            MINT_NFT_ENDPOINT, json_data=api_payload
        )
        return MintNFTResponseModel(**response_json)

    async def enhance_prompt(
        self, request_data: EnhancePromptRequestModel
    ) -> EnhancePromptResponseModel:
        """Enhances or refines a text prompt for better image generation results."""
        if not isinstance(request_data, EnhancePromptRequestModel):
            raise TypeError(
                "request_data must be an instance of EnhancePromptRequestModel"
            )

        api_payload = request_data.model_dump(by_alias=True, exclude_none=True)
        self._http_client.logger.debug(
            f"Sending enhance prompt request to {ENHANCE_PROMPT_ENDPOINT}"
        )

        response_json = await self._http_client.post(
            ENHANCE_PROMPT_ENDPOINT, json_data=api_payload
        )
        return EnhancePromptResponseModel(**response_json)

    async def get_chains(self, test_net: bool | None = None) -> GetChainsResponseModel:
        """Retrieves the list of supported blockchain networks."""
        params = {}
        if test_net is not None:
            params["testNet"] = test_net

        self._http_client.logger.debug(
            f"Sending get chains request to {GET_CHAINS_ENDPOINT} with params: {params}"
        )
        response_json = await self._http_client._request(
            "GET", GET_CHAINS_ENDPOINT, params=params if params else None
        )
        return GetChainsResponseModel(**response_json.json())

    async def get_abi(self) -> ContractABIResponseModel:
        """Provides the ABI of the ChainGPT NFT smart contract."""
        self._http_client.logger.debug(f"Sending get ABI request to {GET_ABI_ENDPOINT}")
        response_json = await self._http_client._request("GET", GET_ABI_ENDPOINT)
        return ContractABIResponseModel(**response_json.json())
