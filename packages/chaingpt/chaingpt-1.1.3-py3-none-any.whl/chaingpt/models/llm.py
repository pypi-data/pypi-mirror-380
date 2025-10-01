"""Pydantic models for ChainGPT LLM API."""

from typing import List, Dict, Any
from pydantic import BaseModel, Field, field_validator, HttpUrl, model_validator

from ..types import BlockchainNetwork, ChatHistoryMode, AITone, PresetTone


class SocialMediaUrlModel(BaseModel):
    """Social media URL model."""

    name: str = Field(..., description="Name of the social media platform")
    url: HttpUrl = Field(..., description="URL to the social media profile")


class TokenInformationModel(BaseModel):
    """Token information model with validation."""

    token_name: str | None = Field(
        default=None, alias="tokenName", description="Name of the token"
    )
    token_symbol: str | None = Field(
        default=None, alias="tokenSymbol", description="Token symbol/ticker"
    )
    token_address: str | None = Field(
        default=None, alias="tokenAddress", description="Token contract address"
    )
    token_source_code: str | None = Field(
        default=None,
        alias="tokenSourceCode",
        description="Token source code or repository URL",
    )
    token_audit_url: HttpUrl | None = Field(
        default=None, alias="tokenAuditUrl", description="URL to token audit report"
    )
    explorer_url: HttpUrl | None = Field(
        default=None,
        alias="explorerUrl",
        description="Block explorer URL for the token",
    )
    cmc_url: HttpUrl | None = Field(
        default=None, alias="cmcUrl", description="CoinMarketCap URL"
    )
    coingecko_url: HttpUrl | None = Field(
        default=None, alias="coingeckoUrl", description="CoinGecko URL"
    )
    blockchain: List[BlockchainNetwork] | None = Field(
        default=None, description="List of supported blockchain networks"
    )

    model_config = {"populate_by_name": True, "use_enum_values": True}


class ContextInjectionModel(BaseModel):
    """Context injection model with comprehensive validation."""

    company_name: str | None = Field(
        default=None, alias="companyName", description="Company or project name"
    )
    company_description: str | None = Field(
        default=None,
        alias="companyDescription",
        description="Brief description of the company/project",
    )
    company_website_url: HttpUrl | None = Field(
        default=None, alias="companyWebsiteUrl", description="Company website URL"
    )
    white_paper_url: HttpUrl | None = Field(
        default=None, alias="whitePaperUrl", description="Whitepaper URL"
    )
    purpose: str | None = Field(
        default=None, description="Purpose or role of the AI chatbot"
    )
    crypto_token: bool | None = Field(
        default=None,
        alias="cryptoToken",
        description="Whether the project has a crypto token",
    )
    token_information: TokenInformationModel | None = Field(
        default=None, alias="tokenInformation", description="Token details"
    )
    social_media_urls: List[SocialMediaUrlModel] | None = Field(
        default=None, alias="socialMediaUrls", description="Social media URLs"
    )
    limitation: bool | None = Field(default=None, description="Content limitation flag")
    ai_tone: AITone | None = Field(
        default=None, alias="aiTone", description="AI tone setting"
    )
    selected_tone: PresetTone | None = Field(
        default=None, alias="selectedTone", description="Selected preset tone"
    )
    custom_tone: str | None = Field(
        default=None, alias="customTone", description="Custom tone description"
    )

    model_config = {"populate_by_name": True, "use_enum_values": True}

    @model_validator(mode="after")
    def validate_tone_consistency(self):
        """Validate tone-related fields consistency."""
        if self.ai_tone == AITone.PRE_SET_TONE and self.selected_tone is None:
            raise ValueError("selectedTone is required when aiTone is PRE_SET_TONE")

        if self.ai_tone == AITone.CUSTOM_TONE and not self.custom_tone:
            raise ValueError("customTone is required when aiTone is CUSTOM_TONE")

        return self

    @model_validator(mode="after")
    def validate_token_information_consistency(self):
        """Validate that tokenInformation is provided when cryptoToken is True."""
        if self.crypto_token is True and self.token_information is None:
            raise ValueError("tokenInformation is required when cryptoToken is True")

        return self


class LLMChatRequestModel(BaseModel):
    """LLM chat request model with validation."""

    model: str = Field(default="general_assistant", description="Model ID to use")
    question: str = Field(
        ..., min_length=1, max_length=10000, description="User's question or prompt"
    )
    chat_history: ChatHistoryMode | None = Field(
        default=ChatHistoryMode.OFF,
        alias="chatHistory",
        description="Chat history mode",
    )
    sdk_unique_id: str | None = Field(
        default=None,
        alias="sdkUniqueId",
        min_length=1,
        max_length=100,
        description="Unique session identifier",
    )
    use_custom_context: bool | None = Field(
        default=False,
        alias="useCustomContext",
        description="Whether to use custom context",
    )
    context_injection: ContextInjectionModel | None = Field(
        default=None, alias="contextInjection", description="Custom context data"
    )

    model_config = {"populate_by_name": True, "use_enum_values": True}

    @field_validator("model")
    @classmethod
    def validate_model(cls, v):
        """Validate model name."""
        if v != "general_assistant":
            raise ValueError("Currently only 'general_assistant' model is supported")
        return v

    @model_validator(mode="after")
    def validate_context_injection_consistency(self):
        """Validate that contextInjection is provided when useCustomContext is True."""
        if self.use_custom_context is True and self.context_injection is None:
            raise ValueError(
                "contextInjection is required when useCustomContext is True"
            )
        return self

    def to_api_dict(self) -> Dict[str, Any]:
        """Convert to API-compatible dictionary."""
        data = self.model_dump(by_alias=True, exclude_none=True)

        # Handle nested model serialization
        if self.context_injection:
            data["contextInjection"] = self.context_injection.model_dump(
                by_alias=True, exclude_none=True
            )

            # Handle token information serialization
            if self.context_injection.token_information:
                data["contextInjection"]["tokenInformation"] = (
                    self.context_injection.token_information.model_dump(
                        by_alias=True, exclude_none=True
                    )
                )

            # Handle social media URLs serialization
            if self.context_injection.social_media_urls:
                data["contextInjection"]["socialMediaUrls"] = [
                    {"name": url.name, "url": str(url.url)}
                    for url in self.context_injection.social_media_urls
                ]

        return data


class LLMResponseDataModel(BaseModel):
    """LLM response data model."""

    bot: str = Field(..., description="AI assistant's response")


class LLMResponseModel(BaseModel):
    """Complete LLM response model."""

    status: bool = Field(..., description="Response status")
    statusCode: int | None = Field(
        default=None, alias="statusCode", description="HTTP status code of the response"
    )
    message: str = Field(..., description="Response message")
    data: LLMResponseDataModel = Field(..., description="Response data")

    model_config = {"populate_by_name": True}


class LLMErrorResponseModel(BaseModel):
    """LLM error response model."""

    status: bool = Field(..., description="Response status (always False for errors)")
    statusCode: int | None = Field(
        default=None, alias="statusCode", description="HTTP status code of the response"
    )
    message: str = Field(..., description="Error message")

    model_config = {"extra": "allow"}  # Allow additional error fields
