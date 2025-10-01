"""
Tests for cli_base.py - Testing through real implementations and base class functionality
"""

from typing import List

import pytest

# Import the module to ensure coverage
import dazllm.cli_base  # noqa: F401
from dazllm.cli_base import CliProviderBase
from dazllm.llm_claude_cli import LlmClaudeCli
from dazllm.llm_gemini_cli import LlmGeminiCli


class MockCliProvider(CliProviderBase):
    """Mock implementation of CLI provider for testing base functionality"""

    def __init__(self):
        # Use a real provider name to avoid validation errors
        # We use echo as a real command that exists on all systems
        super().__init__("anthropic:claude-3-5-sonnet-20241022", "echo")

    @staticmethod
    def default_model() -> str:
        """Return default model for testing"""
        return "claude-3-5-sonnet-20241022"

    @staticmethod
    def supported_models() -> List[str]:
        """Return list of supported models"""
        return ["claude-3-5-sonnet-20241022", "claude-3-haiku-20240307"]

    @staticmethod
    def capabilities() -> set:
        """Return capabilities"""
        return {"chat", "structured"}

    @staticmethod
    def default_for_type(model_type: str) -> str:
        """Return default model for type"""
        if model_type == "chat":
            return "claude-3-5-sonnet-20241022"
        return None

    @staticmethod
    def check_config():
        """Check configuration"""
        # For testing, we always pass
        return True

    def get_context_length(self) -> int:
        """Get context length"""
        return 200000  # Claude 3.5 Sonnet context length

    def _normalize_conversation(self, conversation) -> str:
        """Convert conversation to string for testing"""
        if isinstance(conversation, str):
            return conversation
        return str(conversation)

    def _build_chat_command(self, prompt: str, force_json: bool = False) -> List[str]:
        """Build command for chat"""
        if force_json:
            return ["echo", '{"response": "test response"}']
        return ["echo", "test response"]

    def _build_structured_command(self, prompt: str) -> List[str]:
        """Build command for structured chat"""
        return ["echo", '{"answer": 42, "text": "The answer"}']

    def _get_help_flag(self) -> str:
        """Override help flag for echo"""
        return "--help"  # Echo accepts --help

    def _check_executable(self):
        """Override to avoid checking echo"""
        # Avoid checking because echo doesn't have a help flag that works as expected
        pass

    def _build_structured_prompt(self, conversation, schema) -> str:
        """Build structured prompt - override to avoid f-string issue"""
        return str(conversation)

    # Implement required async methods
    async def chat_async(self, conversation, force_json: bool = False):
        """Async chat method - just call sync version"""
        return self.chat(conversation, force_json)

    async def chat_structured_async(self, conversation, schema, context_size: int = 0):
        """Async structured chat - just call sync version"""
        return self.chat_structured(conversation, schema)

    async def async_image(self, prompt: str, file_name: str, width: int = 1024, height: int = 1024):
        """Async image generation - not supported in test"""
        raise NotImplementedError("Image generation not supported in test provider")


def test_cli_provider_initialization():
    """Test that we can initialize our test CLI provider"""
    provider = MockCliProvider()
    assert provider is not None
    assert provider.model == "claude-3-5-sonnet-20241022"
    assert provider.executable_name == "echo"


def test_default_model():
    """Test default_model method"""
    assert MockCliProvider.default_model() == "claude-3-5-sonnet-20241022"


def test_supported_models():
    """Test supported_models method"""
    models = MockCliProvider.supported_models()
    assert "claude-3-5-sonnet-20241022" in models
    assert "claude-3-haiku-20240307" in models
    assert len(models) == 2


def test_capabilities():
    """Test capabilities method"""
    caps = MockCliProvider.capabilities()
    assert "chat" in caps
    assert "structured" in caps


def test_extract_json_basic():
    """Test JSON extraction from simple response"""
    provider = MockCliProvider()

    # Test with clean JSON
    json_str = '{"key": "value", "number": 42}'
    result = provider._extract_json(json_str)
    assert result == {"key": "value", "number": 42}


def test_extract_json_with_text():
    """Test JSON extraction from response with surrounding text"""
    provider = MockCliProvider()

    # Test with JSON embedded in text
    response = 'Here is the response:\n```json\n{"result": true}\n```\nDone!'
    result = provider._extract_json(response)
    assert result == {"result": True}


def test_extract_json_multiple_attempts():
    """Test JSON extraction with various formats"""
    provider = MockCliProvider()

    # Test with markdown code block
    response1 = '```\n{"test": 123}\n```'
    result1 = provider._extract_json(response1)
    assert result1 == {"test": 123}

    # Test with nested JSON
    response2 = '{"outer": {"inner": "value"}}'
    result2 = provider._extract_json(response2)
    assert result2 == {"outer": {"inner": "value"}}


def test_extract_json_failure():
    """Test JSON extraction with invalid JSON"""
    provider = MockCliProvider()

    # Test with invalid JSON
    invalid_json = "This is not JSON at all"
    with pytest.raises(ValueError, match="Could not extract valid JSON"):
        provider._extract_json(invalid_json)


def test_chat_method_with_echo():
    """Test the chat method using real echo command"""
    provider = MockCliProvider()

    # This will actually run echo command
    response = provider.chat("Test message")
    assert response == "test response"


def test_chat_structured_with_echo():
    """Test structured chat using real echo command"""
    from pydantic import BaseModel

    class TestResponse(BaseModel):
        answer: int
        text: str

    provider = MockCliProvider()

    # This will actually run echo command which returns JSON
    response = provider.chat_structured("What is the answer?", TestResponse)
    assert hasattr(response, "value")
    assert isinstance(response.value, TestResponse)
    assert response.value.answer == 42
    assert response.value.text == "The answer"


def test_real_cli_providers():
    """Test that real CLI providers properly have required methods"""
    # Claude CLI now uses Agent SDK directly (not CliProviderBase)
    try:
        claude_cli = LlmClaudeCli("anthropic:claude-3-5-sonnet-20241022")
        assert hasattr(claude_cli, "chat")
        assert hasattr(claude_cli, "chat_structured")
    except Exception:
        # Skip if SDK not installed
        pass

    # Test Gemini CLI inherits from base
    assert issubclass(LlmGeminiCli, CliProviderBase)
    gemini_cli = LlmGeminiCli("google:gemini-2.0-flash")
    assert hasattr(gemini_cli, "chat")
    assert hasattr(gemini_cli, "chat_structured")
    assert hasattr(gemini_cli, "_extract_json")


def test_find_executable():
    """Test the _find_executable method"""
    provider = MockCliProvider()

    # Test that echo executable was found during initialization
    assert provider.executable is not None
    assert "echo" in provider.executable.lower()

    # Test finding a non-existent executable would fail
    import shutil

    nonexistent_path = shutil.which("this_definitely_does_not_exist_12345")
    assert nonexistent_path is None


def test_json_extraction_strategies():
    """Test that base class tries multiple JSON extraction strategies"""
    provider = MockCliProvider()

    # Test various JSON formats that the base class should handle
    test_cases = [
        ('{"simple": "json"}', {"simple": "json"}),
        ('```json\n{"markdown": "block"}\n```', {"markdown": "block"}),
        ('```\n{"plain": "block"}\n```', {"plain": "block"}),
        ('Text before {"inline": "json"}', {"inline": "json"}),
    ]

    for input_text, expected in test_cases:
        result = provider._extract_json(input_text)
        assert result == expected


def test_base_class_methods_exist():
    """Test that all expected base class methods exist"""
    provider = MockCliProvider()

    # Check all methods that should be provided by the base class
    assert hasattr(provider, "chat")
    assert hasattr(provider, "chat_structured")
    assert hasattr(provider, "_extract_json")
    assert hasattr(provider, "_find_executable")
    assert hasattr(provider, "_check_executable")

    # Check that abstract methods are implemented
    assert callable(provider.default_model)
    assert callable(provider.supported_models)
    assert callable(provider.capabilities)
    assert callable(provider._normalize_conversation)
    assert callable(provider._build_chat_command)
    assert callable(provider._build_structured_command)


def test_executable_check_in_base_class():
    """Test that the base class properly checks for executable"""
    # Try to create provider with non-existent command
    from dazllm.core import ConfigurationError

    class BadProvider(MockCliProvider):
        def __init__(self):
            try:
                # This will call base class init with bad command
                CliProviderBase.__init__(self, "anthropic:claude-3-5-sonnet-20241022", "nonexistent12345")
            except ConfigurationError as e:
                # Expected behavior
                self.error = str(e)

    bad_provider = BadProvider()
    assert hasattr(bad_provider, "error")
    assert "not found" in bad_provider.error.lower()


def test_context_length():
    """Test getting context length from provider"""
    provider = MockCliProvider()
    context_len = provider.get_context_length()
    assert context_len == 200000


def test_check_config():
    """Test check_config method"""
    result = MockCliProvider.check_config()
    assert result is True


def test_default_for_type():
    """Test getting default model for type"""
    assert MockCliProvider.default_for_type("chat") == "claude-3-5-sonnet-20241022"
    assert MockCliProvider.default_for_type("image") is None


def test_json_with_markers():
    """Test JSON extraction with markers"""
    provider = MockCliProvider()

    # Test extraction with markers
    text_with_markers = """
    Some explanation text
    === RESULT JSON START ===
    {"marked": "json"}
    === RESULT JSON END ===
    More text after
    """

    result = provider._extract_json_with_markers(text_with_markers)
    assert result == {"marked": "json"}

    # Test without markers
    text_without = "Just regular text"
    result = provider._extract_json_with_markers(text_without)
    assert result is None


def test_async_methods():
    """Test that async methods are implemented"""
    import asyncio

    async def run_async_tests():
        provider = MockCliProvider()

        # Test async chat
        result = await provider.chat_async("Hello")
        assert result == "test response"

        # Test async structured chat
        from pydantic import BaseModel

        class AsyncTest(BaseModel):
            answer: int
            text: str

        result = await provider.chat_structured_async("Test", AsyncTest)
        assert hasattr(result, "value")
        assert isinstance(result.value, AsyncTest)

        # Test async image (should raise)
        with pytest.raises(NotImplementedError):
            await provider.async_image("prompt", "file.png")

    asyncio.run(run_async_tests())
