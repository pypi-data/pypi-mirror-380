"""Pydantic models for ChainGPT Chat History API with transformation layer."""

from typing import List, Any, Dict
from pydantic import BaseModel, Field, field_validator, model_validator

from .base import ChatBotModel, UserModel


class ChatHistoryEntryModel(BaseModel):
    """Represents a single entry in the chat history."""

    id: str = Field(..., alias="id")
    question: str = Field(..., alias="question")
    answer: str = Field(..., alias="answer")
    createdAt: str = Field(..., alias="createdAt")
    promptId: str | None = Field(None, alias="promptId")
    type: str = Field(..., alias="type")
    chartData: Any | None = Field(None, alias="chartData")
    chartType: str | None = Field(None, alias="chartType")
    chartInterval: str | None = Field(None, alias="chartInterval")
    trend: str | None = Field(None, alias="trend")
    chainId: str | None = Field(None, alias="chainId")
    auditType: str | None = Field(None, alias="auditType")
    auditMethod: str | None = Field(None, alias="auditMethod")
    contractAddress: str | None = Field(None, alias="contractAddress")
    chatBot: ChatBotModel = Field(..., alias="chatBot")
    user: UserModel = Field(..., alias="user")
    chatFeedbacks: List[Any] = Field(default_factory=list, alias="chatFeedbacks")
    sdkUniqueId: str | None = Field(None, alias="sdkUniqueId")

    @field_validator("id", mode="before")
    @classmethod
    def convert_id_to_string(cls, v):
        """Convert integer id to string."""
        return str(v) if isinstance(v, int) else v

    model_config = {"populate_by_name": True}


class ChatHistoryDataModel(BaseModel):
    """Data model for the list of chat history entries and count."""

    rows: List[ChatHistoryEntryModel]
    count: int

    model_config = {"populate_by_name": True}


class GetChatHistoryResponseModel(BaseModel):
    """Response model for retrieving chat history."""

    status: bool | None = Field(
        None, alias="status", description="Indicates if the request was successful"
    )
    statusCode: int | None = Field(
        None, alias="statusCode", description="HTTP status code of the response"
    )
    message: str
    data: ChatHistoryDataModel

    @model_validator(mode="before")
    @classmethod
    def transform_status_code(cls, values):
        """Transform statusCode to status boolean."""
        if isinstance(values, dict) and "statusCode" in values:
            values["status"] = values["statusCode"] == 200
        return values


def transform_api_response(api_response: Dict[str, Any]) -> Dict[str, Any]:
    """Transform raw API response to match expected model structure."""
    transformed = {
        "status": api_response.get("status", True),
        "statusCode": api_response.get("statusCode", 200),
        "message": api_response.get("message", ""),
        "data": {"count": api_response.get("data", {}).get("count", 0), "rows": []},
    }

    for row in api_response.get("data", {}).get("rows", []):
        transformed_row = {
            "id": str(row.get("id", "")),
            "question": row.get("question", ""),
            "answer": row.get("answer", ""),
            "createdAt": row.get("createdAt", ""),
            "promptId": row.get("promptId"),
            "type": row.get("type", "text"),
            "chartData": row.get("chartData"),
            "chartType": row.get("chartType"),
            "chartInterval": row.get("chartInterval"),
            "trend": row.get("trend"),
            "chainId": row.get("chainId"),
            "auditType": row.get("auditType"),
            "auditMethod": row.get("auditMethod"),
            "contractAddress": row.get("contractAddress"),
            "chatBot": row.get("chatBot"),
            "user": row.get("user"),
            "chatFeedbacks": row.get("chatFeedbacks", []),
            "sdkUniqueId": row.get("sdkUniqueId"),
        }
        transformed["data"]["rows"].append(transformed_row)

    return transformed
