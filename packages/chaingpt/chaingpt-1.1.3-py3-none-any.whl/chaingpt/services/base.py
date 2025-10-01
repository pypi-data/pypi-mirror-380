"""Base service class for ChainGPT API services."""

from ..utils.http import AsyncHTTPClient
from ..utils.logger import setup_logger

logger = setup_logger(__name__)


class BaseService:
    """Base class for all API services."""

    def __init__(self, http_client: AsyncHTTPClient):
        self._http_client = http_client
        self._logger = logger
