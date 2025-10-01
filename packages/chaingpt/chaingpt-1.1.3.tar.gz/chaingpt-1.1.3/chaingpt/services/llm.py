"""LLM Service for ChainGPT API."""

import json
from typing import AsyncIterator

from .base import BaseService
from ..models.llm import LLMChatRequestModel, LLMResponseModel, LLMErrorResponseModel
from ..types import StreamChunk
from ..exceptions import ChainGPTError

LLM_CHAT_ENDPOINT = "/chat/stream"


class LLMService(BaseService):
    """Service for interacting with the ChainGPT LLM API."""

    async def chat(self, request_data: LLMChatRequestModel) -> LLMResponseModel:
        """
        Sends a question to the LLM and gets a complete JSON response.

        Args:
            request_data: The request data model containing the question and other parameters.

        Returns:
            The LLM's response.
        """
        if not isinstance(request_data, LLMChatRequestModel):
            raise TypeError("request_data must be an instance of LLMChatRequestModel")

        api_payload = request_data.to_api_dict()
        self._http_client.logger.debug(f"Chat request payload: {api_payload}")

        try:
            # For non-streaming requests, we need to ensure we get JSON
            # The API documentation suggests that by default it returns JSON
            # but we might need to handle cases where it doesn't
            response_json = await self._http_client.post(
                LLM_CHAT_ENDPOINT, json_data=api_payload
            )

            self._http_client.logger.debug("Chat response received successfully.")

            # Handle case where response might be None or empty
            if response_json is None:
                raise ChainGPTError("Received empty response from API")

            # Check if response has the expected structure
            if not isinstance(response_json, dict):
                raise ChainGPTError(
                    f"Expected dict response, got {type(response_json)}"
                )

            # Validate the response structure
            if response_json.get("status") is True:
                return LLMResponseModel(**response_json)
            else:
                # Handle error response
                if "message" in response_json:
                    error_model = LLMErrorResponseModel(**response_json)
                    self._http_client.logger.error(
                        f"API returned error: {error_model.message}"
                    )
                    raise ChainGPTError(f"API Error: {error_model.message}")
                else:
                    # Handle case where response doesn't match expected error format
                    self._http_client.logger.error(
                        f"Unexpected response structure: {response_json}"
                    )
                    raise ChainGPTError(f"Unexpected API response: {response_json}")

        except json.JSONDecodeError as e:
            self._http_client.logger.error(f"Failed to parse JSON response: {e}")
            raise ChainGPTError(f"Invalid JSON response from API: {e}")
        except ChainGPTError:
            # Re-raise ChainGPT specific errors
            raise
        except Exception as e:
            self._http_client.logger.error(f"Error during chat request: {e}")
            raise ChainGPTError(f"Unexpected error during chat request: {e}")

    async def stream_chat(
        self, request_data: LLMChatRequestModel
    ) -> AsyncIterator[StreamChunk]:
        """
        Sends a question to the LLM and streams the response token by token.

        Args:
            request_data: The request data model containing the question and other parameters.

        Yields:
            Stream chunks (bytes or str) as they are received from the API.
        """
        if not isinstance(request_data, LLMChatRequestModel):
            raise TypeError("request_data must be an instance of LLMChatRequestModel")

        api_payload = request_data.to_api_dict()
        self._http_client.logger.debug(
            f"Sending streaming chat request to {LLM_CHAT_ENDPOINT}"
        )

        try:
            async for chunk in self._http_client.stream_post(
                LLM_CHAT_ENDPOINT, json_data=api_payload
            ):
                yield chunk
            self._http_client.logger.debug("Chat stream finished.")
        except Exception as e:
            self._http_client.logger.error(f"Error during streaming chat request: {e}")
            raise ChainGPTError(f"Streaming chat error: {e}")
