"""
Tests for llm_ollama.py
"""

from dazllm import DazLlmError
from dazllm.llm_ollama import LlmOllama


def test_models_without_format_support():
    """Test list of models without format support"""
    assert "gpt-oss:20b" in LlmOllama.MODELS_WITHOUT_FORMAT_SUPPORT


def test_default_model():
    """Test default model for Ollama"""
    assert LlmOllama.default_model() == "mistral-small"


def test_default_for_type():
    """Test default_for_type method"""
    assert LlmOllama.default_for_type("local_small") == "phi3"
    assert LlmOllama.default_for_type("local_medium") == "mistral-small"
    assert LlmOllama.default_for_type("local_large") == "qwen3:32b"
    assert LlmOllama.default_for_type("paid_cheap") is None
    assert LlmOllama.default_for_type("paid_best") is None
    assert LlmOllama.default_for_type("unknown") is None


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


def test_get_base_url_static():
    """Test _get_base_url_static method"""
    url = LlmOllama._get_base_url_static()
    assert isinstance(url, str)
    assert url.startswith("http")


def test_check_config():
    """Test check_config method"""
    # This will raise if Ollama is not running
    LlmOllama.check_config()


def test_check_format_support():
    """Test _check_format_support for different models"""
    # Model with format support - use actually installed model
    ollama1 = LlmOllama("ollama:phi3")
    assert ollama1._check_format_support()

    # Model without format support
    ollama2 = LlmOllama("ollama:gpt-oss:20b")
    assert not ollama2._check_format_support()


def test_normalize_conversation_string():
    """Test _normalize_conversation with string input"""
    ollama = LlmOllama("ollama:phi3")
    result = ollama._normalize_conversation("Hello world")
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["role"] == "user"
    assert result[0]["content"] == "Hello world"


def test_normalize_conversation_list():
    """Test _normalize_conversation with list input"""
    ollama = LlmOllama("ollama:phi3")
    conversation = [{"role": "user", "content": "Hello"}]
    result = ollama._normalize_conversation(conversation)
    assert result == conversation


def test_find_json_with_markdown():
    """Test _find_json with markdown code blocks"""
    ollama = LlmOllama("ollama:phi3")
    text = '```json\n{"name": "test", "value": 42}\n```'
    result = ollama._find_json(text)
    assert result == {"name": "test", "value": 42}


def test_find_json_without_markdown():
    """Test _find_json without markdown"""
    ollama = LlmOllama("ollama:phi3")
    text = '{"name": "test", "value": 42}'
    result = ollama._find_json(text)
    assert result == {"name": "test", "value": 42}


def test_parse_json_with_multiple_strategies_markdown():
    """Test _parse_json_with_multiple_strategies with markdown"""
    ollama = LlmOllama("ollama:phi3")
    text = '```json\n{"key": "value"}\n```'
    result = ollama._parse_json_with_multiple_strategies(text)
    assert result == {"key": "value"}


def test_parse_json_with_multiple_strategies_plain():
    """Test _parse_json_with_multiple_strategies with plain JSON"""
    ollama = LlmOllama("ollama:phi3")
    text = '{"key": "value"}'
    result = ollama._parse_json_with_multiple_strategies(text)
    assert result == {"key": "value"}


def test_parse_json_with_multiple_strategies_with_prefix():
    """Test _parse_json_with_multiple_strategies with prefix"""
    ollama = LlmOllama("ollama:phi3")
    text = 'Here is the JSON: {"key": "value"}'
    result = ollama._parse_json_with_multiple_strategies(text)
    assert result == {"key": "value"}


def test_parse_json_with_multiple_strategies_embedded():
    """Test _parse_json_with_multiple_strategies with embedded JSON"""
    ollama = LlmOllama("ollama:phi3")
    text = 'Some text before {"key": "value"} some text after'
    result = ollama._parse_json_with_multiple_strategies(text)
    assert result == {"key": "value"}


def test_get_context_length_known_models():
    """Test get_context_length for known models"""
    # Llama3
    ollama2 = LlmOllama("ollama:llama3")
    assert ollama2.get_context_length() == 8192

    # GPT-OSS
    ollama3 = LlmOllama("ollama:gpt-oss:20b")
    assert ollama3.get_context_length() == 4096


def test_image_not_supported():
    """Test that image generation raises error"""
    ollama = LlmOllama("ollama:phi3")
    try:
        ollama.image("test prompt", "output.png")
        assert False, "Should have raised DazLlmError"
    except DazLlmError as e:
        assert "not supported" in str(e).lower()


def test_parse_json_with_multiple_strategies_with_trailing_punctuation():
    """Test _parse_json_with_multiple_strategies with trailing punctuation"""
    ollama = LlmOllama("ollama:phi3")
    text = '{"key": "value"}.'
    result = ollama._parse_json_with_multiple_strategies(text)
    assert result == {"key": "value"}


def test_parse_json_with_multiple_strategies_with_output_prefix():
    """Test _parse_json_with_multiple_strategies with Output prefix"""
    ollama = LlmOllama("ollama:phi3")
    text = 'Output: {"key": "value"}'
    result = ollama._parse_json_with_multiple_strategies(text)
    assert result == {"key": "value"}


def test_parse_json_with_multiple_strategies_with_result_prefix():
    """Test _parse_json_with_multiple_strategies with Result prefix"""
    ollama = LlmOllama("ollama:phi3")
    text = 'Result: {"key": "value"}'
    result = ollama._parse_json_with_multiple_strategies(text)
    assert result == {"key": "value"}


def test_get_context_length_phi3():
    """Test get_context_length for phi3 model"""
    ollama = LlmOllama("ollama:phi3")
    assert ollama.get_context_length() == 4096


def test_get_context_length_pattern_matching():
    """Test get_context_length pattern matching for model families"""
    # Use installed llama3
    ollama = LlmOllama("ollama:llama3")
    # Should match llama3 pattern
    assert ollama.get_context_length() == 8192


def test_get_base_url():
    """Test _get_base_url instance method"""
    ollama = LlmOllama("ollama:phi3")
    url = ollama._get_base_url()
    assert isinstance(url, str)
    assert url.startswith("http")


def test_is_model_available():
    """Test _is_model_available method"""
    ollama = LlmOllama("ollama:phi3")
    # Should be True since phi3 is installed
    assert ollama._is_model_available()


def test_parse_json_failure():
    """Test _parse_json_with_multiple_strategies with invalid JSON"""
    ollama = LlmOllama("ollama:phi3")
    try:
        ollama._parse_json_with_multiple_strategies("This is not JSON at all")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Could not parse JSON" in str(e)


def test_simple_chat():
    """Test simple chat functionality"""
    ollama = LlmOllama("ollama:phi3")
    response = ollama.chat("What is 10 + 15? Answer with just the number.")
    assert isinstance(response.value, str)
    assert "25" in response.value


def test_find_json_error():
    """Test _find_json with invalid markdown JSON"""
    ollama = LlmOllama("ollama:phi3")
    try:
        ollama._find_json("```json\ninvalid json here\n```")
        assert False, "Should have raised exception"
    except Exception:
        pass  # Expected


def test_parse_json_with_json_prefix():
    """Test _parse_json_with_multiple_strategies with JSON prefix"""
    ollama = LlmOllama("ollama:phi3")
    text = 'JSON: {"key": "value"}'
    result = ollama._parse_json_with_multiple_strategies(text)
    assert result == {"key": "value"}
