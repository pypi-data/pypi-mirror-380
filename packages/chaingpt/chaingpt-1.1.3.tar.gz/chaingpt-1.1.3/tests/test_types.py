"""Tests for ChainGPT SDK types and enums."""

from chaingpt.types import (
    BlockchainNetwork,
    ChatHistoryMode,
    AITone,
    PresetTone,
    NFTImageModel,
    ImageEnhanceOption,
)


class TestBlockchainNetwork:
    """Test cases for BlockchainNetwork enum."""

    def test_blockchain_network_values(self):
        """Test BlockchainNetwork enum values."""
        assert BlockchainNetwork.ETHEREUM == "ETHEREUM"
        assert BlockchainNetwork.BSC == "BSC"
        assert BlockchainNetwork.ARBITRUM == "ARBITRUM"
        assert BlockchainNetwork.POLYGON == "POLYGON"
        assert BlockchainNetwork.AVALANCHE == "AVALANCHE"
        assert BlockchainNetwork.OPTIMISM == "OPTIMISM"

    def test_blockchain_network_membership(self):
        """Test BlockchainNetwork enum membership."""
        assert "ETHEREUM" in BlockchainNetwork
        assert "BSC" in BlockchainNetwork
        assert "INVALID_NETWORK" not in BlockchainNetwork

    def test_blockchain_network_iteration(self):
        """Test BlockchainNetwork enum iteration."""
        networks = list(BlockchainNetwork)
        assert len(networks) > 20  # Should have many networks
        assert BlockchainNetwork.ETHEREUM in networks
        assert BlockchainNetwork.POLYGON in networks

    def test_blockchain_network_string_comparison(self):
        """Test BlockchainNetwork string comparison."""
        assert BlockchainNetwork.ETHEREUM == "ETHEREUM"


class TestChatHistoryMode:
    """Test cases for ChatHistoryMode enum."""

    def test_chat_history_mode_values(self):
        """Test ChatHistoryMode enum values."""
        assert ChatHistoryMode.ON == "on"
        assert ChatHistoryMode.OFF == "off"

    def test_chat_history_mode_membership(self):
        """Test ChatHistoryMode enum membership."""
        assert "on" in ChatHistoryMode
        assert "off" in ChatHistoryMode
        assert "invalid" not in ChatHistoryMode

    def test_chat_history_mode_iteration(self):
        """Test ChatHistoryMode enum iteration."""
        modes = list(ChatHistoryMode)
        assert len(modes) == 2
        assert ChatHistoryMode.ON in modes
        assert ChatHistoryMode.OFF in modes


class TestAITone:
    """Test cases for AITone enum."""

    def test_ai_tone_values(self):
        """Test AITone enum values."""
        assert AITone.DEFAULT_TONE == "DEFAULT_TONE"
        assert AITone.CUSTOM_TONE == "CUSTOM_TONE"
        assert AITone.PRE_SET_TONE == "PRE_SET_TONE"

    def test_ai_tone_membership(self):
        """Test AITone enum membership."""
        assert "DEFAULT_TONE" in AITone
        assert "CUSTOM_TONE" in AITone
        assert "PRE_SET_TONE" in AITone
        assert "INVALID_TONE" not in AITone

    def test_ai_tone_iteration(self):
        """Test AITone enum iteration."""
        tones = list(AITone)
        assert len(tones) == 3
        assert AITone.DEFAULT_TONE in tones
        assert AITone.CUSTOM_TONE in tones
        assert AITone.PRE_SET_TONE in tones


class TestPresetTone:
    """Test cases for PresetTone enum."""

    def test_preset_tone_values(self):
        """Test PresetTone enum values."""
        assert PresetTone.PROFESSIONAL == "PROFESSIONAL"
        assert PresetTone.FRIENDLY == "FRIENDLY"
        assert PresetTone.INFORMATIVE == "INFORMATIVE"
        assert PresetTone.FORMAL == "FORMAL"
        assert PresetTone.CONVERSATIONAL == "CONVERSATIONAL"
        assert PresetTone.AUTHORITATIVE == "AUTHORITATIVE"
        assert PresetTone.PLAYFUL == "PLAYFUL"
        assert PresetTone.INSPIRATIONAL == "INSPIRATIONAL"
        assert PresetTone.CONCISE == "CONCISE"
        assert PresetTone.EMPATHETIC == "EMPATHETIC"
        assert PresetTone.ACADEMIC == "ACADEMIC"
        assert PresetTone.NEUTRAL == "NEUTRAL"
        assert PresetTone.SARCASTIC_MEME_STYLE == "SARCASTIC_MEME_STYLE"

    def test_preset_tone_membership(self):
        """Test PresetTone enum membership."""
        assert "PROFESSIONAL" in PresetTone
        assert "FRIENDLY" in PresetTone
        assert "SARCASTIC_MEME_STYLE" in PresetTone
        assert "INVALID_TONE" not in PresetTone

    def test_preset_tone_iteration(self):
        """Test PresetTone enum iteration."""
        tones = list(PresetTone)
        assert len(tones) == 13  # Should have 13 preset tones
        assert PresetTone.PROFESSIONAL in tones
        assert PresetTone.FRIENDLY in tones


class TestNFTImageModel:
    """Test cases for NFTImageModel enum."""

    def test_nft_image_model_values(self):
        """Test NFTImageModel enum values."""
        assert NFTImageModel.VELOGEN == "velogen"
        assert NFTImageModel.NEBULA_FORGE_XL == "nebula_forge_xl"
        assert NFTImageModel.VISIONARY_FORGE == "VisionaryForge"
        assert NFTImageModel.DALE3 == "Dale3"

    def test_nft_image_model_membership(self):
        """Test NFTImageModel enum membership."""
        assert "velogen" in NFTImageModel
        assert "nebula_forge_xl" in NFTImageModel
        assert "VisionaryForge" in NFTImageModel
        assert "Dale3" in NFTImageModel
        assert "invalid_model" not in NFTImageModel

    def test_nft_image_model_iteration(self):
        """Test NFTImageModel enum iteration."""
        models = list(NFTImageModel)
        assert len(models) == 4
        assert NFTImageModel.VELOGEN in models
        assert NFTImageModel.NEBULA_FORGE_XL in models


class TestImageEnhanceOption:
    """Test cases for ImageEnhanceOption enum."""

    def test_image_enhance_option_values(self):
        """Test ImageEnhanceOption enum values."""
        assert ImageEnhanceOption.ORIGINAL == "original"
        assert ImageEnhanceOption.ENHANCE_1X == "1x"
        assert ImageEnhanceOption.ENHANCE_2X == "2x"

    def test_image_enhance_option_membership(self):
        """Test ImageEnhanceOption enum membership."""
        assert "original" in ImageEnhanceOption
        assert "1x" in ImageEnhanceOption
        assert "2x" in ImageEnhanceOption
        assert "4x" not in ImageEnhanceOption

    def test_image_enhance_option_iteration(self):
        """Test ImageEnhanceOption enum iteration."""
        options = list(ImageEnhanceOption)
        assert len(options) == 3
        assert ImageEnhanceOption.ORIGINAL in options
        assert ImageEnhanceOption.ENHANCE_1X in options
        assert ImageEnhanceOption.ENHANCE_2X in options


class TestEnumStringBehavior:
    """Test that enums behave correctly as strings."""

    def test_enum_string_equality(self):
        """Test that enums compare equal to their string values."""
        assert BlockchainNetwork.ETHEREUM == "ETHEREUM"
        assert ChatHistoryMode.ON == "on"
        assert AITone.CUSTOM_TONE == "CUSTOM_TONE"
        assert PresetTone.PROFESSIONAL == "PROFESSIONAL"

    def test_enum_in_list_of_strings(self):
        """Test that enums work in lists with strings."""
        blockchain_list = ["ETHEREUM", "BSC", BlockchainNetwork.POLYGON]
        assert "ETHEREUM" in blockchain_list
        assert BlockchainNetwork.ETHEREUM in blockchain_list
        assert BlockchainNetwork.POLYGON in blockchain_list

    def test_enum_json_serialization_behavior(self):
        """Test enum behavior for JSON serialization."""
        # These enums should serialize to their string values
        assert BlockchainNetwork.ETHEREUM.value == "ETHEREUM"
        assert ChatHistoryMode.ON.value == "on"
        assert AITone.PRE_SET_TONE.value == "PRE_SET_TONE"
        assert PresetTone.FRIENDLY.value == "FRIENDLY"
        assert NFTImageModel.VELOGEN.value == "velogen"
        assert ImageEnhanceOption.ORIGINAL.value == "original"
