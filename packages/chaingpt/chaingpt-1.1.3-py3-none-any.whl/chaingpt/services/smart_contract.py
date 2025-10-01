"""Smart Contract Service for ChainGPT API."""

from typing import AsyncIterator, Dict, Any

from .base import BaseService
from ..models.smart_contract import (
    SmartContractGeneratorRequestModel,
    SmartContractGeneratorResponseModel,
)
from ..models.chat_history import GetChatHistoryResponseModel
from ..types import StreamChunk

# Smart Contract Endpoints
SMART_CONTRACT_GENERATOR_ENDPOINT = "/chat/stream"  # Same as LLM but different model
CHAT_HISTORY_ENDPOINT = "/chat/chatHistory"  # As per documentation


class SmartContractService(BaseService):
    """Service for interacting with the ChainGPT Smart Contract Generator API."""

    async def generate_contract(
        self, request_data: SmartContractGeneratorRequestModel
    ) -> SmartContractGeneratorResponseModel:
        """
        Generates a smart contract and returns the complete JSON response.
        The 'model' field in request_data must be 'smart_contract_generator'.
        """
        if not isinstance(request_data, SmartContractGeneratorRequestModel):
            raise TypeError(
                "request_data must be an instance of SmartContractGeneratorRequestModel"
            )
        if request_data.model != "smart_contract_generator":
            raise ValueError(
                "Model for SmartContractService must be 'smart_contract_generator'"
            )

        api_payload = request_data.model_dump(by_alias=True, exclude_none=True)
        self._http_client.logger.debug(
            f"Sending smart contract generation request to {SMART_CONTRACT_GENERATOR_ENDPOINT}"
        )
        self._http_client.logger.debug(f"Smart contract request payload: {api_payload}")

        response_json = await self._http_client.post(
            SMART_CONTRACT_GENERATOR_ENDPOINT, json_data=api_payload
        )
        self._http_client.logger.debug("Smart contract response received successfully.")
        return SmartContractGeneratorResponseModel(**response_json)

    async def stream_contract(
        self, request_data: SmartContractGeneratorRequestModel
    ) -> AsyncIterator[StreamChunk]:
        """
        Generates a smart contract and streams the response.
        The 'model' field in request_data must be 'smart_contract_generator'.
        Yields raw chunks of the contract code.
        """
        if not isinstance(request_data, SmartContractGeneratorRequestModel):
            raise TypeError(
                "request_data must be an instance of SmartContractGeneratorRequestModel"
            )
        if request_data.model != "smart_contract_generator":
            raise ValueError(
                "Model for SmartContractService must be 'smart_contract_generator'"
            )

        api_payload = request_data.model_dump(by_alias=True, exclude_none=True)
        self._http_client.logger.debug(
            f"Sending streaming smart contract request to {SMART_CONTRACT_GENERATOR_ENDPOINT}"
        )

        async for chunk in self._http_client.stream_post(
            SMART_CONTRACT_GENERATOR_ENDPOINT, json_data=api_payload
        ):
            yield chunk
        self._http_client.logger.debug("Smart contract stream finished.")

    async def get_chat_history(
        self,
        limit: int | None = 10,
        offset: int | None = 0,
        sort_by: str | None = "createdAt",
        sort_order: str | None = "desc",
    ) -> GetChatHistoryResponseModel:
        """
        Retrieves chat history for the smart contract generator.
        The API doc mentions using apiclient.get("/", {params...}), suggesting params are for the base URL
        of the history feature or a specific endpoint.
        Using CHAT_HISTORY_ENDPOINT = "/chat/chatHistory".
        """
        params: Dict[str, Any] = {
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "sortOrder": sort_order,
        }

        self._http_client.logger.debug(
            f"Sending get chat history request to {CHAT_HISTORY_ENDPOINT} with params: {params}"
        )

        # Using _request for GET and to get the raw httpx.Response
        http_response = await self._http_client._request(
            "GET", CHAT_HISTORY_ENDPOINT, params=params
        )
        response_json = http_response.json()

        return GetChatHistoryResponseModel(**response_json)
