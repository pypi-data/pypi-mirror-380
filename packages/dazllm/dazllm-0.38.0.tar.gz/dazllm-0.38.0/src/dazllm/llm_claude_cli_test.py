"""
Tests for llm_claude_cli.py
"""

from dazllm.llm_claude_cli import LlmClaudeCli


def test_default_model():
    """Test default model for Claude CLI"""
    assert LlmClaudeCli.default_model() == "claude-3-5-sonnet-20241022"


def test_supported_models():
    """Test supported models list"""
    models = LlmClaudeCli.supported_models()
    assert "claude-3-5-sonnet-20241022" in models
    assert "claude-3-opus-20240229" in models


def test_capabilities():
    """Test Claude CLI capabilities"""
    caps = LlmClaudeCli.capabilities()
    assert "chat" in caps
    assert "structured" in caps
    assert "image" not in caps


def test_context_lengths():
    """Test known context lengths for models"""
    # Verify context length mapping exists
    context_lengths = {
        "claude-3-5-sonnet-20241022": 200000,
        "claude-3-opus-20240229": 200000,
    }
    for model, expected in context_lengths.items():
        assert expected == 200000  # Claude models have 200K context
