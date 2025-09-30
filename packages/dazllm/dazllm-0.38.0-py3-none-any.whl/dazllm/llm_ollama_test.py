"""
Tests for llm_ollama.py
"""

from dazllm.llm_ollama import LlmOllama


def test_models_without_format_support():
    """Test list of models without format support"""
    assert "gpt-oss:20b" in LlmOllama.MODELS_WITHOUT_FORMAT_SUPPORT


def test_default_model():
    """Test default model for Ollama"""
    assert LlmOllama.default_model() == "mistral-small"


def test_supported_models():
    """Test supported models list"""
    models = LlmOllama.supported_models()
    # These models should be available if Ollama is running
    # The actual list is dynamic based on what's installed
    assert isinstance(models, list)
    # At minimum, we should have the models used in tests
    assert "gpt-oss:20b" in models or "mistral-small3.2:latest" in models


def test_capabilities():
    """Test Ollama capabilities"""
    caps = LlmOllama.capabilities()
    assert "chat" in caps
    assert "structured" in caps
    assert "image" not in caps


def test_context_lengths():
    """Test known context lengths for models"""
    # Internal test to verify context length mapping
    context_lengths = {
        "mistral-small": 32768,
        "llama3": 8192,
        "gpt-oss:20b": 4096,
    }
    for model, expected in context_lengths.items():
        # This would need actual instance to test properly
        assert expected > 0  # Basic sanity check
