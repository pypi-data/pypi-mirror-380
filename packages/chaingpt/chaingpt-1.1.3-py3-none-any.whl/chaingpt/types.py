"""Type definitions for ChainGPT SDK."""

from enum import Enum
from typing import Dict, List, Union, Any, AsyncIterator, Iterator
from typing_extensions import Literal, TypedDict


class BlockchainNetwork(str, Enum):
    """Supported blockchain networks."""

    ETHEREUM = "ETHEREUM"
    BSC = "BSC"
    ARBITRUM = "ARBITRUM"
    BASE = "BASE"
    BLAST = "BLAST"
    AVALANCHE = "AVALANCHE"
    POLYGON = "POLYGON"
    SCROLL = "SCROLL"
    OPTIMISM = "OPTIMISM"
    LINEA = "LINEA"
    ZKSYNC = "ZKSYNC"
    POLYGON_ZKEVM = "POLYGON_ZKEVM"
    GNOSIS = "GNOSIS"
    FANTOM = "FANTOM"
    MOONRIVER = "MOONRIVER"
    MOONBEAM = "MOONBEAM"
    BOBA = "BOBA"
    METIS = "METIS"
    LISK = "LISK"
    AURORA = "AURORA"
    SEI = "SEI"
    IMMUTABLE_ZK = "IMMUTABLE_ZK"
    GRAVITY = "GRAVITY"
    TAIKO = "TAIKO"
    CRONOS = "CRONOS"
    FRAXTAL = "FRAXTAL"
    ABSTRACT = "ABSTRACT"
    WORLD_CHAIN = "WORLD_CHAIN"
    MANTLE = "MANTLE"
    MODE = "MODE"
    CELO = "CELO"
    BERACHAIN = "BERACHAIN"


class ChatHistoryMode(str, Enum):
    """Chat history modes."""

    ON = "on"
    OFF = "off"


class AITone(str, Enum):
    """AI tone options."""

    DEFAULT_TONE = "DEFAULT_TONE"
    CUSTOM_TONE = "CUSTOM_TONE"
    PRE_SET_TONE = "PRE_SET_TONE"


class PresetTone(str, Enum):
    """Preset tone options."""

    PROFESSIONAL = "PROFESSIONAL"
    FRIENDLY = "FRIENDLY"
    INFORMATIVE = "INFORMATIVE"
    FORMAL = "FORMAL"
    CONVERSATIONAL = "CONVERSATIONAL"
    AUTHORITATIVE = "AUTHORITATIVE"
    PLAYFUL = "PLAYFUL"
    INSPIRATIONAL = "INSPIRATIONAL"
    CONCISE = "CONCISE"
    EMPATHETIC = "EMPATHETIC"
    ACADEMIC = "ACADEMIC"
    NEUTRAL = "NEUTRAL"
    SARCASTIC_MEME_STYLE = "SARCASTIC_MEME_STYLE"


class SocialMediaUrl(TypedDict):
    """Social media URL structure."""

    name: str
    url: str


class TokenInformation(TypedDict, total=False):
    """Token information structure."""

    tokenName: str | None
    tokenSymbol: str | None
    tokenAddress: str | None
    tokenSourceCode: str | None
    tokenAuditUrl: str | None
    explorerUrl: str | None
    cmcUrl: str | None
    coingeckoUrl: str | None
    blockchain: List[BlockchainNetwork] | None


class ContextInjection(TypedDict, total=False):
    """Context injection structure for customizing AI responses."""

    companyName: str | None
    companyDescription: str | None
    companyWebsiteUrl: str | None
    whitePaperUrl: str | None
    purpose: str | None
    cryptoToken: bool | None
    tokenInformation: TokenInformation | None
    socialMediaUrls: List[SocialMediaUrl] | None
    limitation: bool | None
    aiTone: AITone | None
    selectedTone: PresetTone | None
    customTone: str | None


# Response types
class LLMResponseData(TypedDict):
    """LLM response data structure."""

    bot: str


class LLMResponse(TypedDict):
    """Complete LLM response structure."""

    status: bool
    message: str
    data: LLMResponseData


class ErrorResponse(TypedDict):
    """Error response structure."""

    status: bool
    message: str


# Request types
class LLMChatRequest(TypedDict):
    """LLM chat request structure."""

    model: Literal["general_assistant"]
    question: str
    chatHistory: ChatHistoryMode | None
    sdkUniqueId: str | None
    useCustomContext: bool | None
    contextInjection: ContextInjection | None


# Stream types
StreamChunk = Union[str, bytes]
SyncStreamIterator = Iterator[StreamChunk]
AsyncStreamIterator = AsyncIterator[StreamChunk]

# HTTP types
HTTPHeaders = Dict[str, str]
HTTPParams = Dict[str, Any]
HTTPTimeout = Union[float, int, None]


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


# NFT Trait types
class TraitValueItem(TypedDict):
    """Trait value item structure."""

    value: str
    ratio: int


class Trait(TypedDict):
    """Trait structure."""

    trait_type: str
    value: List[TraitValueItem]


# NFT Request types
class GenerateImageRequest(TypedDict, total=False):
    """Generate image request structure."""

    prompt: str
    model: str
    steps: int | None
    height: int
    width: int
    enhance: str | None
    style: str | None
    traits: List[Trait] | None
    image: str | None
    isCharacterPreserve: bool | None


class GenerateNFTQueueRequest(TypedDict, total=False):
    """Generate NFT queue request structure."""

    walletAddress: str
    prompt: str
    model: str
    steps: int | None
    height: int
    width: int
    enhance: str | None
    chainId: int
    amount: int
    style: str | None
    traits: List[Trait] | None
    image: str | None
    isCharacterPreserve: bool | None


class MintNFTRequest(TypedDict):
    """Mint NFT request structure."""

    collectionId: str
    name: str
    description: str
    symbol: str
    ids: List[int]


class EnhancePromptRequest(TypedDict):
    """Enhance prompt request structure."""

    prompt: str


# NFT Response types
class ImageBuffer(TypedDict):
    """Image buffer structure."""

    type: str
    data: List[int]


class GenerateImageResponse(TypedDict):
    """Generate image response structure."""

    data: ImageBuffer


class GenerateNFTQueueResponse(TypedDict):
    """Generate NFT queue response structure."""

    collectionId: str
    status: str


class NFTProgressResponse(TypedDict, total=False):
    """NFT progress response structure."""

    collectionId: str | None
    status: str
    progress: int | None
    images: List[str] | None
    generated: bool | None


class MintNFTResponse(TypedDict, total=False):
    """Mint NFT response structure."""

    name: str
    description: str
    image: str
    attributes: List[Dict[str, Any]] | None
    collectionId: str
    transaction: Any | None


class EnhancePromptResponse(TypedDict):
    """Enhance prompt response structure."""

    enhancedPrompt: str


class ChainInfo(TypedDict):
    """Chain info structure."""

    chainId: int
    chainName: str
    network: str
    networkType: str


class GetChainsResponse(TypedDict):
    """Get chains response structure."""

    chains: List[ChainInfo]


class ContractABIResponse(TypedDict):
    """Contract ABI response structure."""

    abi: List[Dict[str, Any]]
