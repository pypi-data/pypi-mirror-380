"""Pydantic models for ChainGPT NFT Generator API."""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field, HttpUrl
from enum import Enum


# Enums specific to NFT generation
class NFTImageModel(str, Enum):
    """Supported AI models for NFT image generation."""

    VELOGEN = "velogen"
    NEBULA_FORGE_XL = "nebula_forge_xl"
    VISIONARY_FORGE = "VisionaryForge"
    DALE3 = "Dale3"


class ImageEnhanceOption(str, Enum):
    """Image enhancement options."""

    ORIGINAL = "original"
    ENHANCE_1X = "1x"
    ENHANCE_2X = "2x"


# Models for Traits
class TraitValueItemModel(BaseModel):
    value: str
    ratio: int


class TraitModel(BaseModel):
    trait_type: str = Field(..., alias="trait_type")
    value: List[TraitValueItemModel]


# 1. Generate Image (Synchronous)
class GenerateImageRequestModel(BaseModel):
    prompt: str
    model: NFTImageModel
    steps: Optional[int] = None
    height: int
    width: int
    enhance: Optional[ImageEnhanceOption] = ImageEnhanceOption.ORIGINAL
    style: Optional[str] = None
    traits: Optional[List[TraitModel]] = None
    image: Optional[HttpUrl | str] = None  # For image-to-image generation
    isCharacterPreserve: Optional[bool] = None  # For character preservation


class ImageBufferModel(BaseModel):
    """Model for the Buffer-style image data response."""

    type: str  # Should be "Buffer"
    data: List[int]  # Raw image bytes as a list of integers


class GenerateImageResponseModel(BaseModel):
    data: ImageBufferModel  # Updated to match actual API response structure


# 2. Generate NFT Queue (Asynchronous)
class GenerateNFTQueueRequestModel(BaseModel):
    walletAddress: str = Field(..., alias="walletAddress")
    prompt: str
    model: NFTImageModel
    steps: Optional[int] = None
    height: int
    width: int
    enhance: Optional[ImageEnhanceOption] = ImageEnhanceOption.ORIGINAL
    chainId: int = Field(..., alias="chainId")
    amount: int
    style: Optional[str] = None
    traits: Optional[List[TraitModel]] = None
    image: Optional[HttpUrl] = None  # For image-to-image generation
    isCharacterPreserve: Optional[bool] = None  # For character preservation


class GenerateNFTQueueDataModel(BaseModel):
    """Data model for the nested collectionId response."""

    collectionId: str = Field(..., alias="collectionId")


class GenerateNFTQueueResponseModel(BaseModel):
    """Model to match the actual API response structure."""

    statusCode: int = Field(..., alias="statusCode")
    message: str
    data: GenerateNFTQueueDataModel


class NFTProgressDataModel(BaseModel):
    """Data model for progress response - handles both in-progress and completed states."""

    generated: bool
    images: Optional[List[str]] = None  # Only present when generated=True
    progress: Optional[int] = None  # Progress percentage


class NFTProgressResponseModel(BaseModel):
    """Model to match the actual API response structure."""

    statusCode: int = Field(..., alias="statusCode")
    message: str
    data: NFTProgressDataModel


class MintNFTRequestModel(BaseModel):
    collectionId: str = Field(..., alias="collectionId")
    name: str
    description: str
    symbol: str
    ids: List[int]


class MintNFTDataModel(BaseModel):
    """Data model for the mint NFT response."""

    _id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    attributes: Optional[List[Dict[str, Any]]] = None
    collectionId: Optional[str] = Field(None, alias="collectionId")
    transaction: Optional[Any] = None
    __v: Optional[int] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None


class MintNFTResponseModel(BaseModel):
    """Model to match the actual API response structure."""

    statusCode: int = Field(..., alias="statusCode")
    message: str
    data: MintNFTDataModel


class EnhancePromptRequestModel(BaseModel):
    prompt: str


class EnhancePromptDataModel(BaseModel):
    """Data model for the nested enhancedPrompt response."""

    enhancedPrompt: str = Field(..., alias="enhancedPrompt")


class EnhancePromptResponseModel(BaseModel):
    """Model to match the actual API response structure."""

    statusCode: int = Field(..., alias="statusCode")
    message: str
    data: EnhancePromptDataModel


class ChainInfoModel(BaseModel):
    chainId: int = Field(..., alias="chainId")
    chainName: str = Field(..., alias="chainName")
    network: str
    networkType: str = Field(..., alias="networkType")


class GetChainsDataModel(BaseModel):
    """Data model for the chains response."""

    chains: List[ChainInfoModel]


class GetChainsResponseModel(BaseModel):
    """Model to match the actual API response structure."""

    statusCode: int = Field(..., alias="statusCode")
    message: str
    data: GetChainsDataModel


class ContractABIDataModel(BaseModel):
    """Data model for the contract ABI response."""

    abi: List[Dict[str, Any]]


class ContractABIResponseModel(BaseModel):
    """Model to match the actual API response structure."""

    statusCode: int = Field(..., alias="statusCode")
    message: str
    data: List[Dict[str, Any]]
