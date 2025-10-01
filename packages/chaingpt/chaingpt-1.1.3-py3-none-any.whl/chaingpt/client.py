"""Main client for interacting with the ChainGPT API."""

from .services.llm import LLMService
from .services.nft import NFTService
from .services.smart_contract import SmartContractService
from .services.auditor import AuditorService
from .services.news import NewsService
from .utils.http import AsyncHTTPClient, DEFAULT_TIMEOUT, DEFAULT_STREAM_TIMEOUT
from .types import HTTPTimeout


class ChainGPTClient:
    """
    Asynchronous client for the ChainGPT API.
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.chaingpt.org",
        timeout: HTTPTimeout = DEFAULT_TIMEOUT,
        stream_timeout: HTTPTimeout = DEFAULT_STREAM_TIMEOUT,
        debug: bool = False,
    ):
        """
        Initializes the ChainGPTClient.

        Args:
            api_key: Your ChainGPT API key.
            base_url: The base URL for the ChainGPT API.
            timeout: Default timeout for regular requests in seconds.
            stream_timeout: Default timeout for streaming requests in seconds.
            debug: If True, enables debug logging.
        """
        self._http_client = AsyncHTTPClient(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            stream_timeout=stream_timeout,
            debug=debug,
        )
        self.llm = LLMService(self._http_client)
        self.nft = NFTService(self._http_client)
        self.smart_contract = SmartContractService(self._http_client)
        self.auditor = AuditorService(self._http_client)
        self.news = NewsService(self._http_client)

        self._http_client.logger.debug("ChainGPTClient initialized.")

    async def close(self) -> None:
        """Closes the underlying HTTP client session."""
        await self._http_client.close()
        self._http_client.logger.debug("ChainGPTClient closed.")

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
