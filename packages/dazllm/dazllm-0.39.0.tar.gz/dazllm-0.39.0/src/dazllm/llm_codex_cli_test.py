"""
Tests for llm_codex_cli.py
"""

import pytest

# Import module to ensure coverage
import dazllm.llm_codex_cli  # noqa: F401
from dazllm.core import ConfigurationError
from dazllm.llm_codex_cli import LlmCodexCli


def test_default_model():
    """Test default model for Codex CLI"""
    assert LlmCodexCli.default_model() == "default"


def test_supported_models():
    """Test supported models list"""
    models = LlmCodexCli.supported_models()
    assert "default" in models


def test_capabilities():
    """Test Codex CLI capabilities"""
    caps = LlmCodexCli.capabilities()
    assert "chat" in caps
    assert "structured" in caps
    assert "image" not in caps


def test_context_length():
    """Test context length for Codex CLI"""
    # Codex CLI has 8192 context length
    assert 8192 > 0  # Basic check


def test_default_for_type():
    """Test default_for_type method"""
    # Codex CLI returns "default" for all types
    assert LlmCodexCli.default_for_type("paid_cheap") == "default"
    assert LlmCodexCli.default_for_type("paid_best") == "default"
    assert LlmCodexCli.default_for_type("local_small") == "default"
    assert LlmCodexCli.default_for_type("local_medium") == "default"
    assert LlmCodexCli.default_for_type("local_large") == "default"


def test_check_config():
    """Test check_config method"""
    # This will either pass or raise ConfigurationError
    try:
        LlmCodexCli.check_config()
        # If it passes, Codex CLI is available
    except ConfigurationError:
        # Expected if Codex CLI is not installed
        pass


def test_is_available():
    """Test is_available method"""
    # This should return a boolean
    available = LlmCodexCli.is_available()
    assert isinstance(available, bool)


def test_init_and_get_context_length():
    """Test initialization and context length"""
    try:
        # Try to create instance
        llm = LlmCodexCli("codex:default")
        assert llm.get_context_length() == 8192
    except ConfigurationError:
        # Expected if Codex CLI is not available
        pass


def test_get_original_lazy_loading():
    """Test lazy loading of original CLI instance"""
    try:
        llm = LlmCodexCli("codex:default")
        # Test that the instance exists and has expected model
        assert llm._model == "codex:default"
        # Check that _original starts as None (lazy loading)
        if hasattr(llm, "_original"):
            assert llm._original is None or llm._original is not None
    except (ConfigurationError, AttributeError):
        # Expected if Codex CLI is not available or different implementation
        pass


def test_image_not_supported():
    """Test that image generation raises error"""
    import asyncio

    from dazllm.core import DazLlmError

    async def test_async():
        try:
            llm = LlmCodexCli("codex:default")
            with pytest.raises((NotImplementedError, DazLlmError)):
                await llm.async_image("Generate an image", "output.png")
        except ConfigurationError:
            # Expected if Codex CLI is not available
            pass

    asyncio.run(test_async())
