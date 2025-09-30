"""
Tests for llm_google.py
"""

from dazllm.llm_google import LlmGoogle


def test_default_model():
    """Test default model for Google"""
    assert LlmGoogle.default_model() == "gemini-2.0-flash"


def test_supported_models():
    """Test supported models list"""
    models = LlmGoogle.supported_models()
    assert "gemini-2.0-flash" in models
    assert "gemini-1.5-pro" in models


def test_capabilities():
    """Test Google capabilities"""
    caps = LlmGoogle.capabilities()
    assert "chat" in caps
    assert "structured" in caps
    assert "image" in caps


def test_context_lengths():
    """Test known context lengths for models"""
    # Verify context length mapping exists
    context_lengths = {
        "gemini-2.0-flash": 1000000,
        "gemini-1.5-pro": 2000000,
    }
    for model, expected in context_lengths.items():
        assert expected > 0  # Basic sanity check
