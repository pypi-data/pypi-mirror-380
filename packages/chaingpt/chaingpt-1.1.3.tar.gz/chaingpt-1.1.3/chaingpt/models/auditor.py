"""Pydantic models for ChainGPT Smart Contract Auditor API."""

from pydantic import BaseModel, Field
from typing_extensions import Literal

from ..types import ChatHistoryMode


# Request model for initiating a smart contract audit
class SmartContractAuditRequestModel(BaseModel):
    """Request model for auditing a smart contract."""

    model: Literal["smart_contract_auditor"] = Field(
        default="smart_contract_auditor",
        description="Model ID for smart contract auditing.",
    )
    question: str = Field(
        ...,
        min_length=1,
        description="Smart contract code and any specific instructions or questions for the auditor.",
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
