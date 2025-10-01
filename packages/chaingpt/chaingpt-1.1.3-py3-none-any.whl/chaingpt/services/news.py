"""News Service for ChainGPT AI News API."""

from typing import List, Union, Dict, Any

from ..exceptions import ValidationError

from .base import BaseService
from ..models.news import GetNewsResponseModel

NEWS_ENDPOINT = "/news"


class NewsService(BaseService):
    """Service for interacting with the ChainGPT AI News Generator API."""

    """Updated News Service method to handle the API response structure."""

    async def get_news(
        self,
        category_id: Union[int, List[int]] | None = None,
        sub_category_id: Union[int, List[int]] | None = None,
        token_id: Union[int, List[int]] | None = None,
        search_query: str | None = None,
        fetch_after: str | None = None,  # Date string, e.g., "YYYY-MM-DD"
        limit: int | None = 10,
        offset: int | None = 0,
        sort_by: str | None = "createdAt",  # Default based on API doc
    ) -> GetNewsResponseModel:
        """
        Retrieves AI-generated news articles with optional filtering and pagination.

        Args:
            category_id: Filter by one or more category IDs.
            sub_category_id: Filter by one or more sub-category IDs.
            token_id: Filter by one or more specific token IDs.
            search_query: Keyword search term for news title or description.
            fetch_after: Only return news published after this date (e.g., "YYYY-MM-DD").
            limit: Maximum number of news articles to return.
            offset: Number of items to skip for pagination.
            sort_by: Field to sort results by (currently "createdAt").

        Returns:
            An object containing the list of news articles and pagination info.
        """
        params: Dict[str, Any] = {}
        if category_id is not None:
            params["categoryId"] = category_id
        if sub_category_id is not None:
            params["subCategoryId"] = sub_category_id
        if token_id is not None:
            params["tokenId"] = token_id
        if search_query is not None:
            params["searchQuery"] = search_query
        if fetch_after is not None:
            params["fetchAfter"] = fetch_after
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        if sort_by is not None:
            params["sortBy"] = sort_by

        self._http_client.logger.debug(
            f"Sending get news request to {NEWS_ENDPOINT} with params: {params}"
        )

        http_response = await self._http_client._request(
            "GET", NEWS_ENDPOINT, params=params
        )
        response_json = http_response.json()

        self._http_client.logger.debug(f"Get news response JSON: {response_json}")

        try:
            return GetNewsResponseModel(**response_json)
        except ValidationError as e:
            self._http_client.logger.error(f"Validation error in news response: {e}")
            self._http_client.logger.debug(
                f"Raw response that failed validation: {response_json}"
            )
            raise
