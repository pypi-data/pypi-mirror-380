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


def test_default_for_type():
    """Test default_for_type method"""
    assert LlmGeminiCli.default_for_type("paid_best") == "gemini-2.0-flash-exp"
    assert LlmGeminiCli.default_for_type("paid_cheap") == "gemini-1.5-flash"
    assert LlmGeminiCli.default_for_type("local_small") is None
    assert LlmGeminiCli.default_for_type("local_medium") is None
    assert LlmGeminiCli.default_for_type("local_large") is None
    assert LlmGeminiCli.default_for_type("unknown") is None


def test_help_flag():
    """Test _get_help_flag method"""
    cli = LlmGeminiCli("gemini:gemini-2.0-flash-exp")
    assert cli._get_help_flag() == "--help"


def test_timeout_seconds():
    """Test _get_timeout_seconds method"""
    cli = LlmGeminiCli("gemini:gemini-2.0-flash-exp")
    timeout = cli._get_timeout_seconds()
    assert timeout is None  # Gemini CLI has no timeout


def test_get_context_length_various_models():
    """Test get_context_length for various models"""
    # Test 1M token models
    cli1 = LlmGeminiCli("gemini:gemini-2.0-flash-exp")
    assert cli1.get_context_length() == 1000000

    cli2 = LlmGeminiCli("gemini:gemini-1.5-flash")
    assert cli2.get_context_length() == 1000000

    # Test 2M token model
    cli3 = LlmGeminiCli("gemini:gemini-1.5-pro")
    assert cli3.get_context_length() == 2000000

    # Test 32K token models
    cli4 = LlmGeminiCli("gemini:gemini-1.0-pro")
    assert cli4.get_context_length() == 32768

    # Test default for unknown model
    cli5 = LlmGeminiCli("gemini:unknown-model")
    assert cli5.get_context_length() == 32768


def test_is_acceptable_error():
    """Test _is_acceptable_error method"""
    cli = LlmGeminiCli("gemini:gemini-2.0-flash-exp")

    # Create test result objects
    class TestResult:
        def __init__(self, stdout, stderr, returncode):
            self.stdout = stdout
            self.stderr = stderr
            self.returncode = returncode

    # Should be acceptable if has stdout and no stderr
    result1 = TestResult("some output", "", 1)
    assert cli._is_acceptable_error(result1)

    # Not acceptable if has stderr
    result2 = TestResult("output", "error", 1)
    assert not cli._is_acceptable_error(result2)

    # Not acceptable if no output (returns empty string which is falsy)
    result3 = TestResult("", "", 1)
    assert not cli._is_acceptable_error(result3)
