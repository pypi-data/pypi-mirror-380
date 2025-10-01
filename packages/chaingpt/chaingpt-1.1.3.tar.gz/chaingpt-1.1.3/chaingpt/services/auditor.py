"""Smart Contract Auditor Service for ChainGPT API."""

from typing import AsyncIterator, Dict, Any

from .base import BaseService
from ..models.auditor import SmartContractAuditRequestModel
from ..models.llm import LLMResponseModel
from ..models.chat_history import GetChatHistoryResponseModel, transform_api_response
from ..types import StreamChunk

# Endpoints (shared with other services but used with specific models/logic here)
AUDIT_ENDPOINT = "/chat/stream"
HISTORY_ENDPOINT = "/chat/chatHistory"


class AuditorService(BaseService):
    """Service for interacting with the ChainGPT Smart Contract Auditor API."""

    async def audit_contract(
        self, request_data: SmartContractAuditRequestModel
    ) -> LLMResponseModel:
        """
        Submits a smart contract for audit and returns the complete JSON response.
        The 'model' field in request_data must be 'smart_contract_auditor'.
        """
        if not isinstance(request_data, SmartContractAuditRequestModel):
            raise TypeError(
                "request_data must be an instance of SmartContractAuditRequestModel"
            )
        if request_data.model != "smart_contract_auditor":  # Ensure correct model
            raise ValueError(
                "Model for AuditorService must be 'smart_contract_auditor'"
            )

        api_payload = request_data.model_dump(by_alias=True, exclude_none=True)
        self._http_client.logger.debug(f"Audit request payload: {api_payload}")

        response_json = await self._http_client.post(
            AUDIT_ENDPOINT, json_data=api_payload
        )
        self._http_client.logger.debug("Audit response received successfully.")
        return LLMResponseModel(
            **response_json
        )  # Uses the general LLM response structure

    async def stream_audit(
        self, request_data: SmartContractAuditRequestModel
    ) -> AsyncIterator[StreamChunk]:
        """
        Submits a smart contract for audit and streams the response.
        The 'model' field in request_data must be 'smart_contract_auditor'.
        Yields raw chunks of the audit report.
        """
        if not isinstance(request_data, SmartContractAuditRequestModel):
            raise TypeError(
                "request_data must be an instance of SmartContractAuditRequestModel"
            )
        if request_data.model != "smart_contract_auditor":  # Ensure correct model
            raise ValueError(
                "Model for AuditorService must be 'smart_contract_auditor'"
            )

        api_payload = request_data.model_dump(by_alias=True, exclude_none=True)
        self._http_client.logger.debug(
            f"Sending streaming audit request to {AUDIT_ENDPOINT}"
        )

        async for chunk in self._http_client.stream_post(
            AUDIT_ENDPOINT, json_data=api_payload
        ):
            yield chunk
        self._http_client.logger.info("Audit stream finished.")

    async def get_audit_history(
        self,
        limit: int | None = 10,
        offset: int | None = 0,
        sort_by: str | None = "createdAt",
        sort_order: str | None = "desc",
        sdk_unique_id: str | None = None,
    ) -> GetChatHistoryResponseModel:
        """
        Retrieves chat history for the smart contract auditor.
        """
        params: Dict[str, Any] = {
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "sortOrder": sort_order,
        }
        if sdk_unique_id:
            params["sdkUniqueId"] = sdk_unique_id

        self._http_client.logger.debug(
            f"Sending get audit history request to {HISTORY_ENDPOINT} with params: {params}"
        )

        http_response = await self._http_client._request(
            "GET", HISTORY_ENDPOINT, params=params
        )
        response_json = http_response.json()

        self._http_client.logger.debug(
            f"Get audit history response JSON: {response_json}"
        )

        # Option 1: Use the transformation function
        transformed_response = transform_api_response(response_json)
        return GetChatHistoryResponseModel(**transformed_response)
