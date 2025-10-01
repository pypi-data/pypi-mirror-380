"""Pydantic models for ChainGPT AI News Generator API."""

from typing import List, Any
from pydantic import BaseModel, Field


class CategoryModel(BaseModel):
    """Model for category information."""

    id: int
    name: str
    isBlockchain: bool
    isToken: bool
    createdAt: str
    updatedAt: str
    deletedAt: str | None = None


class SubCategoryModel(BaseModel):
    """Model for sub-category information."""

    id: int
    name: str
    isBlockchain: bool
    isToken: bool
    createdAt: str
    updatedAt: str
    deletedAt: str | None = None


class TokenModel(BaseModel):
    """Model for token information."""

    id: int
    name: str
    isBlockchain: bool
    isToken: bool
    createdAt: str
    updatedAt: str
    deletedAt: str | None = None


class MediaModel(BaseModel):
    """Model for media information."""

    id: int
    fileName: str
    fileDescriptor: str
    mimeType: str
    fileSize: int
    createdAt: str | None = None
    updatedAt: str | None = None
    deletedAt: str | None = None


class NewsArticleModel(BaseModel):
    """Represents a single news article."""

    id: int
    title: str
    description: str
    pubDate: str
    isPublished: bool
    author: str
    userId: int | None = None
    isFeatured: int
    categoryId: int | None = None  # Changed to Optional since API can return None
    subCategoryId: int | None = None
    tokenId: int | None = None
    isTopStory: int
    viewsCount: int
    imageUrl: str
    mediaId: int
    createdAt: str
    updatedAt: str
    deletedAt: str | None = None

    # Related objects
    category: CategoryModel | None = None  # Can be None as seen in API response
    subCategory: SubCategoryModel | None = None
    token: TokenModel | None = None
    newsTags: List[Any] = []
    media: MediaModel | None = None

    model_config = {"populate_by_name": True}


class GetNewsResponseModel(BaseModel):
    """Response model for the GET /news endpoint."""

    statusCode: int | None = Field(
        ..., alias="statusCode", description="HTTP status code of the response"
    )
    message: str | None = None
    data: List[NewsArticleModel]
    limit: int | None = None  # As per example, these are part of the response
    offset: int | None = None
    total: int | None = None

    model_config = {"populate_by_name": True}
