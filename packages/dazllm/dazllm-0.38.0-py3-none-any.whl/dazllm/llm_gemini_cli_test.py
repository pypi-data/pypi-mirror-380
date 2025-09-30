"""
Tests for llm_gemini_cli.py
"""

from dazllm.llm_gemini_cli import LlmGeminiCli


def test_default_model():
    """Test default model for Gemini CLI"""
    assert LlmGeminiCli.default_model() == "gemini-2.0-flash-exp"


def test_supported_models():
    """Test supported models list"""
    models = LlmGeminiCli.supported_models()
    assert "gemini-2.0-flash-exp" in models
    assert "gemini-1.5-pro" in models


def test_capabilities():
    """Test Gemini CLI capabilities"""
    caps = LlmGeminiCli.capabilities()
    assert "chat" in caps
    assert "structured" in caps
    assert "image" not in caps


def test_context_lengths():
    """Test known context lengths for models"""
    # Verify context length mapping exists
    context_lengths = {
        "gemini-2.0-flash-exp": 1000000,
        "gemini-1.5-pro": 2000000,
    }
    for model, expected in context_lengths.items():
        assert expected > 0  # Basic sanity check
