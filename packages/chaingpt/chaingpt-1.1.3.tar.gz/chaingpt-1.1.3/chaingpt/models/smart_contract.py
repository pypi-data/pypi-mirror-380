"""Pydantic models for ChainGPT Smart Contract Generator API."""

from pydantic import BaseModel, Field
from typing_extensions import Literal

from ..types import ChatHistoryMode


class SmartContractGeneratorRequestModel(BaseModel):
    """Request model for generating a smart contract."""

    model: Literal["smart_contract_generator"] = Field(
        default="smart_contract_generator",
        description="Model ID for smart contract generation.",
    )
    question: str = Field(
        ..., min_length=1, description="Prompt describing the smart contract."
    )
    chatHistory: ChatHistoryMode | None = Field(
        default=ChatHistoryMode.OFF,
        alias="chatHistory",
        description="Chat history mode.",
    )
    sdkUniqueId: str | None = Field(
        default=None,
        alias="sdkUniqueId",
        min_length=1,
        max_length=100,
        description="Unique session identifier for chat history.",
    )

    model_config = {"populate_by_name": True, "use_enum_values": True}


class SmartContractDataModel(BaseModel):
    """Nested data model within the smart contract generator response."""

    user: str | None = Field(default=None, description="The user's prompt.")
    bot: str | None = Field(
        default=None, description="The generated Solidity smart contract code."
    )


class SmartContractGeneratorResponseModel(BaseModel):
    """Response model for a successful smart contract generation."""

    status: bool
    statusCode: int | None = Field(default=None, alias="statusCode")
    message: str | None = None
    data: SmartContractDataModel
