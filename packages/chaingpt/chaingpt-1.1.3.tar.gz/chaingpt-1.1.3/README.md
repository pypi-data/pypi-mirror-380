# ChainGPT SDK

A comprehensive Python SDK for interacting with the ChainGPT API ecosystem, providing access to AI-powered blockchain tools including LLM chat, NFT generation, smart contract development, auditing, and news services.

## Features

* **🤖 LLM Service** - AI chat with blockchain context and streaming support
* **🎨 NFT Service** - AI-powered NFT generation, minting, and metadata management
* **📝 Smart Contract Service** - AI-assisted smart contract generation with chat history
* **🔍 Auditor Service** - Automated smart contract security auditing
* **📰 News Service** - Curated blockchain and crypto news with advanced filtering
* **🔄 Streaming Support** - Real-time streaming responses for chat and generation
* **📚 Chat History** - Persistent conversation history across sessions
* **⚡ Async/Await** - Built on modern async Python for optimal performance
* **🛡️ Error Handling** - Comprehensive error mapping and retry logic
* **🔧 Easy Configuration** - Environment variables or direct parameter setup

---

## Table of Contents

1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Quick Start](#quick-start)
4. [Services](#services)
   * [LLM Service](#llm-service)
   * [NFT Service](#nft-service)
   * [Smart Contract Service](#smart-contract-service)
   * [Auditor Service](#auditor-service)
   * [News Service](#news-service)
5. [Advanced Usage](#advanced-usage)
6. [Error Handling](#error-handling)
7. [Examples](#examples)
8. [API Reference](#api-reference)
9. [Development](#development)

---

## Installation

Install via pip:

```bash
pip install chaingpt
```

Or add to your `requirements.txt`:

```bash
chaingpt>=1.1.3
```

**Dependencies:**

* `httpx` - Async HTTP client
* `pydantic` - Data validation and serialization
* `colorama` - For color logging
* `python-dotenv` - Environment variable management

---

## Configuration

Configure the SDK using environment variables or constructor parameters:

| Variable               | Default                        | Description                   |
| ---------------------- | ------------------------------ | ----------------------------- |
| `CHAINGPT_API_KEY`     | *required*                     | Your ChainGPT API key         |

### Environment Variables

Create a `.env` file:

```bash
CHAINGPT_API_KEY=your_api_key_here
```

### Direct Configuration

```python
from chaingpt.client import ChainGPTClient

client = ChainGPTClient(api_key="your_api_key_here")
```

---

## Quick Start

```python
import asyncio
import os
from chaingpt.client import ChainGPTClient
from chaingpt.models import LLMChatRequestModel
from chaingpt.types import ChatHistoryMode

async def main():
    # Initialize client
    client = ChainGPTClient(api_key=os.getenv("CHAINGPT_API_KEY"))
    
    try:
        # Simple chat
        request = LLMChatRequestModel(
            question="What is blockchain technology?",
            chatHistory=ChatHistoryMode.OFF
        )
        response = await client.llm.chat(request)
        print(f"AI: {response.data.bot}")
        
        # Streaming chat
        print("\nStreaming response:")
        async for chunk in client.llm.stream_chat(request):
            print(chunk.decode('utf-8'), end="", flush=True)
            
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Services

### LLM Service

AI-powered chat with blockchain context, custom tones, and conversation history.

```python
from chaingpt.client import ChainGPTClient
from chaingpt.models import (
    LLMChatRequestModel, 
    ContextInjectionModel, 
    TokenInformationModel,
    SocialMediaUrlModel,
)
from chaingpt.types import AITone, PresetTone, ChatHistoryMode, BlockchainNetwork

# Basic chat
request = LLMChatRequestModel(
    question="Explain DeFi protocols",
    chatHistory=ChatHistoryMode.ON,
    sdkUniqueId="550e8400-e29b-41d4-a716-446655440000",  # Example UUID
)

# Buffered response
response = await client.llm.chat(request)
print(response.data.bot)

# Streaming response
async for chunk in client.llm.stream_chat(request):
    print(chunk.decode('utf-8'), end="")
```

**Context Injection:**

```python
# Create token information
token_info = TokenInformationModel(
    tokenName="AwesomeToken",
    tokenSymbol="AWE",
    blockchain=[BlockchainNetwork.ETHEREUM, BlockchainNetwork.POLYGON],
)

# Create social media URLs
social_media = [
    SocialMediaUrlModel(name="twitter", url="https://twitter.com/awesometoken")
]

# Create context injection
context = ContextInjectionModel(
    companyName="Awesome Inc.",
    companyDescription="A company building next-gen DeFi tools.",
    cryptoToken=True,
    tokenInformation=token_info,
    socialMediaUrls=social_media,
    aiTone=AITone.PRE_SET_TONE,
    selectedTone=PresetTone.INFORMATIVE,
)

request = LLMChatRequestModel(
    question="Tell me about AwesomeToken",
    useCustomContext=True,
    contextInjection=context,
    chatHistory=ChatHistoryMode.ON,
    sdkUniqueId="550e8400-e29b-41d4-a716-446655440000",  # Example UUID
)
```

### NFT Service

Complete NFT workflow from generation to minting with AI-powered image creation, including image-to-image generation.

```python
from chaingpt.models import (
    GenerateImageRequestModel,
    GenerateNFTQueueRequestModel,
    EnhancePromptRequestModel,
    MintNFTRequestModel,
    TraitModel,
    TraitValueItemModel,
)
from chaingpt.types import NFTImageModel, ImageEnhanceOption

# 1. Enhance prompt (optional)
enhance_request = EnhancePromptRequestModel(prompt="a mystical dragon")
enhanced_response = await client.nft.enhance_prompt(enhance_request)
enhanced_prompt = enhanced_response.data.enhancedPrompt

# 2. Generate image synchronously
image_request = GenerateImageRequestModel(
    prompt=enhanced_prompt,
    model=NFTImageModel.VELOGEN,
    height=512,
    width=512,
    steps=3,
    enhance=ImageEnhanceOption.ORIGINAL,
    style="cinematic",
    traits=[
        TraitModel(
            trait_type="Background",
            value=[
                TraitValueItemModel(value="Heaven", ratio=20),
                TraitValueItemModel(value="Hell", ratio=60),
                TraitValueItemModel(value="garden", ratio=20),
            ],
        )
    ],
)
image_response = await client.nft.generate_image(image_request)

# Save the generated image
with open("generated_image.jpg", "wb") as f:
    f.write(bytes(image_response.data.data))

# 2b. Image-to-Image Generation (new feature)
# Generate variations of an existing image
image_to_image_request = GenerateImageRequestModel(
    prompt="A futuristic cyberpunk version of this character",
    model=NFTImageModel.NEBULA_FORGE_XL,
    height=1024,
    width=1024,
    image="https://example.com/reference-image.jpg",  # Valid image URL required
    isCharacterPreserve=True,  # Preserve character features
    enhance=ImageEnhanceOption.ENHANCE_1X,
)
# image_to_image_response = await client.nft.generate_image(image_to_image_request)

# 3. Queue NFT generation for minting
nft_request = GenerateNFTQueueRequestModel(
    walletAddress="0x000000000000000000000000000000000000dEaD",
    prompt="A serene alien landscape with two moons",
    model=NFTImageModel.NEBULA_FORGE_XL,
    height=1024,
    width=1024,
    steps=25,
    enhance=ImageEnhanceOption.ENHANCE_1X,
    chainId=56,  # BSC Mainnet
    amount=1,
    style="cinematic",
    traits=[
        TraitModel(
            trait_type="Background",
            value=[
                TraitValueItemModel(value="Heaven", ratio=20),
                TraitValueItemModel(value="Hell", ratio=60),
                TraitValueItemModel(value="garden", ratio=20),
            ],
        )
    ],
)
queue_response = await client.nft.generate_nft_queue(nft_request)

# 4. Track progress
progress = await client.nft.get_progress(queue_response.data.collectionId)
print(f"Generated: {progress.data.generated}, Progress: {progress.data.progress}%")

# Wait for completion
while not progress.data.generated:
    await asyncio.sleep(10)
    progress = await client.nft.get_progress(queue_response.data.collectionId)
    print(f"Generated: {progress.data.generated}, Progress: {progress.data.progress}%")

# 5. Get mint metadata (after generation completes)
if progress.data.generated:
    mint_metadata_request = MintNFTRequestModel(
        collectionId=queue_response.data.collectionId,
        name="Serene Alien Landscape #1",
        description="An AI-generated artwork of an alien world.",
        symbol="ALIEN",
        ids=[1],
    )
    mint_metadata_response = await client.nft.mint_nft_metadata(mint_metadata_request)
    print(f"Image URI: {mint_metadata_response.data.image or 'Not provided'}")

# 6. Get supported chains
chains_response = await client.nft.get_chains(test_net=True)
for chain in chains_response.data.chains:
    print(f"Chain ID: {chain.chainId}, Name: {chain.chainName}")

# 7. Get contract ABI
abi_response = await client.nft.get_abi()
print(f"Contract ABI: {abi_response.data}")
```

**New Features:**

* **Image-to-Image Generation**: Create variations of existing images by providing a reference image URL
* **Character Preservation**: Maintain character features while applying new styles or settings
* **Enhanced Traits System**: More flexible trait ratios and combinations
* **Updated Chain Support**: Support for the latest blockchain networks

### Smart Contract Service

AI-assisted smart contract generation with conversation history.

```python
from chaingpt.models import SmartContractGeneratorRequestModel
from chaingpt.types import ChatHistoryMode

request = SmartContractGeneratorRequestModel(
    question="Create an ERC20 token with burn functionality",
    chatHistory=ChatHistoryMode.ON,
    sdkUniqueId="550e8400-e29b-41d4-a716-446655440000",  # Example UUID
)

# Generate contract (buffered)
response = await client.smart_contract.generate_contract(request)
print(f"Status: {response.statusCode}")
print(f"User Prompt: {response.data.user}")
print(f"Generated Contract: {response.data.bot}")

# Generate contract (streaming)
async for chunk in client.smart_contract.stream_contract(request):
    print(chunk.decode('utf-8'), end="")

# Get chat history
history = await client.smart_contract.get_chat_history(
    limit=10,
    sort_order="desc"
)
print(f"Total entries: {history.data.count}")
for entry in history.data.rows:
    print(f"ID: {entry.id}, Question: {entry.question[:50]}...")
    print(f"Bot: {entry.chatBot.name}, User: {entry.user.email}")
    print(f"Created: {entry.createdAt}")
```

### Auditor Service

Automated smart contract security auditing with detailed vulnerability reports.

```python
from chaingpt.models import SmartContractAuditRequestModel

contract_code = """
pragma solidity ^0.8.0;
contract UnsafeBank {
    mapping(address => uint) public balances;
    
    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }
    
    function withdraw(uint amount) public {
        // Vulnerability: Reentrancy possible
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed.");
        balances[msg.sender] -= amount; // Balance updated after external call
    }
}
"""

audit_request = SmartContractAuditRequestModel(
    question=f"Please audit the following Solidity contract for security vulnerabilities:\n\n```solidity\n{contract_code}\n```",
    chatHistory=ChatHistoryMode.ON,
    sdkUniqueId="550e8400-e29b-41d4-a716-446655440000"  # Example UUID
)

# Get audit report
audit_response = await client.auditor.audit_contract(audit_request)
print(f"Status: {audit_response.status}")
print(f"Audit Report: {audit_response.data.bot}")

# Stream audit report
async for chunk in client.auditor.stream_audit(audit_request):
    print(chunk.decode('utf-8'), end="")

# Get audit history
history = await client.auditor.get_audit_history(
    sdk_unique_id="550e8400-e29b-41d4-a716-446655440000",
    limit=5
)
for entry in history.data.rows:
    print(f"Audit ID: {entry.id}, Created: {entry.createdAt}")
    print(f"Question: {entry.question[:100]}...")
```

### News Service

Access curated blockchain and cryptocurrency news with advanced filtering.

```python
# Get latest news
latest_news = await client.news.get_news(limit=10)
print(f"Found {latest_news.total} total articles")
for article in latest_news.data:
    print(f"{article.title} - {article.createdAt}")
    print(f"Category ID: {article.categoryId}, Token ID: {article.tokenId}")

# Filter by category and subcategory
# Category IDs: NFT=8, SubCategory IDs for Ethereum: 15, 39
nft_eth_news = await client.news.get_news(
    category_id=8,          # NFT category
    sub_category_id=[15, 39],  # Ethereum subcategories
    limit=5
)

# Filter by token and search query
bitcoin_news = await client.news.get_news(
    token_id=79,           # Bitcoin token ID
    search_query="halving",
    limit=5
)

# Filter by date
recent_news = await client.news.get_news(
    fetch_after="2024-01-01",
    sort_by="createdAt"
)
```

---

## Advanced Usage

### Session Management

```python
# Use consistent session IDs for conversation continuity
session_id = "550e8400-e29b-41d4-a716-446655440000"  # Example UUID

request = LLMChatRequestModel(
    question="Start a new conversation about DeFi",
    chatHistory=ChatHistoryMode.ON,
    sdkUniqueId=session_id
)

# All subsequent requests with the same session_id will maintain context
follow_up = LLMChatRequestModel(
    question="Tell me more about the previous topic",
    chatHistory=ChatHistoryMode.ON,
    sdkUniqueId=session_id  # Same session
)
```

### Error Handling with Retries

```python
from chaingpt.exceptions import ChainGPTError

try:
    response = await client.llm.chat(request)
except ChainGPTError as e:
    print(f"API Error: {e}")
    # SDK automatically retries with exponential backoff
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Custom HTTP Configuration

```python
import httpx
from chaingpt.client import ChainGPTClient

# Custom HTTP client configuration
custom_client = httpx.AsyncClient(
    timeout=60.0,
    limits=httpx.Limits(max_connections=10),
    headers={"User-Agent": "MyApp/1.0"}
)

client = ChainGPTClient(
    api_key="your_key",
    http_client=custom_client
)
```

### Logging Configuration

```python
from chaingpt.client import ChainGPTClient

# Setup debug logging
client = ChainGPTClient(api_key=API_KEY, debug=True)

```

---

## Error Handling

The SDK provides comprehensive error handling with specific exception types:

```python
from chaingpt.exceptions import (
    ChainGPTError,
    AuthenticationError,
    ValidationError,
    RateLimitError,
    ServerError,
    TimeoutError,
    StreamingError,
    ConfigurationError
)

try:
    response = await client.llm.chat(request)
except AuthenticationError as e:
    print("Authentication failed - check your API key")
except RateLimitError as e:
    print("Rate limit exceeded - please wait before retrying")
except ValidationError as e:
    print(f"Invalid request parameters: {e}")
except ServerError as e:
    print("Server error - please try again later")
except TimeoutError as e:
    print("Request timed out - please try again")
except StreamingError as e:
    print(f"Streaming error: {e}")
except ChainGPTError as e:
    print(f"API error: {e}")
```

**Common Error Codes:**

* `400` - Bad Request (invalid parameters)
* `401` - Unauthorized (invalid API key)
* `429` - Rate Limited
* `500` - Internal Server Error

---

## Examples

Complete example scripts are available in the `examples/` directory:

* `example_llm_service.py` - LLM chat with context injection
* `example_nft_service.py` - Complete NFT generation workflow
* `example_smart_contract_service.py` - Contract generation and history
* `example_auditor_service.py` - Contract auditing
* `example_news_service.py` - News filtering and retrieval

Run an example:

```bash
python examples/example_llm_service.py
```

---

## API Reference

### Core Classes

* **`ChainGPTClient`** - Main SDK client (imported from `chaingpt.client`)
* **`LLMService`** - AI chat operations
* **`NFTService`** - NFT generation and minting
* **`SmartContractService`** - Contract generation
* **`AuditorService`** - Contract auditing
* **`NewsService`** - News retrieval

### Request Models

All models are imported from `chaingpt.models`:

* **`LLMChatRequestModel`** - Chat requests
* **`GenerateImageRequestModel`** - Image generation
* **`GenerateNFTQueueRequestModel`** - NFT queue requests
* **`SmartContractGeneratorRequestModel`** - Contract generation
* **`SmartContractAuditRequestModel`** - Audit requests
* **`EnhancePromptRequestModel`** - Prompt enhancement
* **`MintNFTRequestModel`** - NFT minting
* **`ContextInjectionModel`** - Context injection for LLM
* **`TokenInformationModel`** - Token information
* **`SocialMediaUrlModel`** - Social media URLs
* **`TraitModel`** - NFT traits
* **`TraitValueItemModel`** - NFT trait values

### Enums

All enums are imported from `chaingpt.types`:

* **`ChatHistoryMode`** - `ON`, `OFF`
* **`NFTImageModel`** - `NEBULA_FORGE_XL`, `VELOGEN`
* **`ImageEnhanceOption`** - `ORIGINAL`, `ENHANCE_1X`, `ENHANCE_2X`
* **`AITone`** - `PRE_SET_TONE`, `CUSTOM_TONE`
* **`PresetTone`** - `PROFESSIONAL`, `CASUAL`, `INFORMATIVE`
* **`BlockchainNetwork`** - Various blockchain networks

---

## Requirements

* Python 3.9+
* `httpx>=0.28.1`
* `pydantic>=2.11.5`
* `colorama>=0.4.6`
* `python-dotenv>=1.1.0`

---

## Development

### Setup Development Environment

```bash
git clone https://github.com/ChainGPT-org/chaingpt-python.git
cd chaingpt-python
pip install -e ".[dev,test]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=chaingpt

# Run specific test categories
pytest -m unit
pytest -m integration
pytest -m asyncio
```

### Code Quality

```bash
# Format code
black chaingpt/ tests/ examples/

# Type checking
mypy chaingpt/

# Linting
flake8 chaingpt/ tests/
```

### Building and Publishing

```bash
# Build package
python -m build

# Check package
twine check dist/*

# Upload to PyPI (test)
twine upload --repository testpypi dist/*

# Upload to PyPI (production)
twine upload dist/*
```

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and add tests
4. Commit your changes: `git commit -m 'Add amazing feature'`
5. Push to the branch: `git push origin feature/amazing-feature`
6. Open a Pull Request

### Development Guidelines

* Follow PEP 8 style guidelines
* Add type hints to all functions
* Write comprehensive tests for new features
* Update documentation for any API changes
* Ensure all tests pass before submitting PR

---

## License

This project is licensed under the GPL-3.0-or-later License. See [LICENSE](LICENSE) for details.

---

## Support

* **Documentation**: [https://docs.chaingpt.org](https://docs.chaingpt.org)
* **API Reference**: [https://docs.chaingpt.org/dev-docs-b2b-saas-api-and-sdk/introduction-to-chaingpts-developer-tools](https://docs.chaingpt.org/dev-docs-b2b-saas-api-and-sdk/introduction-to-chaingpts-developer-tools)
* **Issues**: [GitHub Issues](https://github.com/ChainGPT-org/chaingpt-python/issues)
* **Discord**: [ChainGPT Community](https://discord.gg/chaingpt)
* **X(Twitter)**: [@ChainGPT](https://x.com/ChainGPT)

---

Built with ❤️ by the ChainGPT team
