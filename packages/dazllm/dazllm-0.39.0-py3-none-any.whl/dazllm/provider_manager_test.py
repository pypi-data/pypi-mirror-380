"""
Tests for provider_manager.py
"""

import pytest

from dazllm.provider_manager import (
    ConfigurationError,
    DazLlmError,
    ModelNotFoundError,
    ProviderManager,
)


def test_get_providers():
    """Test getting list of providers"""
    providers = ProviderManager.get_providers()
    assert "openai" in providers
    assert "anthropic" in providers
    assert "google" in providers
    assert "ollama" in providers


def test_resolve_provider_alias():
    """Test provider alias resolution"""
    assert ProviderManager.resolve_provider_alias("claude") == "anthropic"
    assert ProviderManager.resolve_provider_alias("gemini") == "google"
    assert ProviderManager.resolve_provider_alias("openai") == "openai"
    assert ProviderManager.resolve_provider_alias("codex") == "codex-cli"


def test_get_provider_class():
    """Test getting provider class dynamically"""
    openai_class = ProviderManager.get_provider_class("openai")
    assert openai_class.__name__ == "LlmOpenai"

    anthropic_class = ProviderManager.get_provider_class("anthropic")
    assert anthropic_class.__name__ == "LlmAnthropic"


def test_get_provider_class_invalid():
    """Test getting invalid provider class"""
    with pytest.raises(ModelNotFoundError):
        ProviderManager.get_provider_class("invalid-provider")


def test_exception_inheritance():
    """Test exception class hierarchy"""
    assert issubclass(ConfigurationError, DazLlmError)
    assert issubclass(ModelNotFoundError, DazLlmError)
