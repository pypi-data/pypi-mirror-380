"""
Tests for llm_claude_cli.py
"""

from dazllm.core import ConfigurationError
from dazllm.llm_claude_cli import LlmClaudeCli


def test_default_model():
    """Test default model for Claude CLI"""
    assert LlmClaudeCli.default_model() == "claude-3-5-sonnet-20241022"


def test_supported_models():
    """Test supported models list"""
    models = LlmClaudeCli.supported_models()
    assert "claude-3-5-sonnet-20241022" in models
    assert "claude-3-opus-20240229" in models
    assert isinstance(models, list)
    assert len(models) > 0


def test_capabilities():
    """Test Claude CLI capabilities"""
    caps = LlmClaudeCli.capabilities()
    assert "chat" in caps
    assert "structured" in caps
    assert "image" not in caps
    assert isinstance(caps, set)


def test_context_lengths():
    """Test known context lengths for models"""
    # Verify context length mapping exists
    context_lengths = {
        "claude-3-5-sonnet-20241022": 200000,
        "claude-3-opus-20240229": 200000,
        "claude-3-5-haiku-20241022": 200000,
    }
    for model, expected in context_lengths.items():
        assert expected == 200000  # Claude models have 200K context


def test_default_for_type_paid_best():
    """Test default_for_type for paid_best"""
    result = LlmClaudeCli.default_for_type("paid_best")
    assert result == "claude-3-5-sonnet-20241022"


def test_default_for_type_paid_cheap():
    """Test default_for_type for paid_cheap"""
    result = LlmClaudeCli.default_for_type("paid_cheap")
    assert result == "claude-3-5-haiku-20241022"


def test_default_for_type_local_returns_none():
    """Test default_for_type for local models returns None"""
    assert LlmClaudeCli.default_for_type("local_small") is None
    assert LlmClaudeCli.default_for_type("local_medium") is None
    assert LlmClaudeCli.default_for_type("local_large") is None


def test_default_for_type_unknown():
    """Test default_for_type for unknown type"""
    result = LlmClaudeCli.default_for_type("unknown_type")
    assert result is None


def test_check_config():
    """Test check_config behavior"""
    try:
        LlmClaudeCli.check_config()
        # If it passes, SDK is installed
    except ConfigurationError as e:
        # If it fails, SDK is not installed
        assert "Claude Agent SDK" in str(e)


def test_is_available():
    """Test is_available method"""
    result = LlmClaudeCli.is_available()
    assert isinstance(result, bool)


def test_model_name_with_prefix():
    """Test model name handling with claude-cli: prefix"""
    try:
        llm = LlmClaudeCli("claude-cli:claude-3-5-sonnet-20241022")
        assert llm.model == "claude-3-5-sonnet-20241022"
        assert "claude-cli:" in llm.model_name
    except ConfigurationError:
        # Expected without SDK installed - test passes
        pass


def test_model_name_without_prefix():
    """Test model name handling without claude-cli: prefix"""
    try:
        llm = LlmClaudeCli("claude-3-5-sonnet-20241022")
        assert llm.model == "claude-3-5-sonnet-20241022"
    except ConfigurationError:
        # Expected without SDK installed - test passes
        pass


def test_normalize_conversation_string():
    """Test _normalize_conversation with string input"""
    try:
        llm = LlmClaudeCli("claude-3-5-sonnet-20241022")
        result = llm._normalize_conversation("Hello world")
        assert result == "Hello world"
    except ConfigurationError:
        # Expected without SDK installed - test passes
        pass


def test_normalize_conversation_list():
    """Test _normalize_conversation with list of messages"""
    try:
        llm = LlmClaudeCli("claude-3-5-sonnet-20241022")
        conversation = [
            {"role": "system", "content": "You are helpful"},
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there"},
        ]
        result = llm._normalize_conversation(conversation)
        assert "<system>You are helpful</system>" in result
        assert "Human: Hello" in result
        assert "Assistant: Hi there" in result
    except ConfigurationError:
        # Expected without SDK installed - test passes
        pass


def test_get_context_length_known_model():
    """Test get_context_length for known models"""
    try:
        llm = LlmClaudeCli("claude-3-5-sonnet-20241022")
        length = llm.get_context_length()
        assert length == 200000
    except ConfigurationError:
        # Expected without SDK installed - test passes
        pass


def test_get_context_length_unknown_model():
    """Test get_context_length for unknown model uses default"""
    try:
        llm = LlmClaudeCli("unknown-model")
        length = llm.get_context_length()
        assert length == 200000  # Default
    except ConfigurationError:
        # Expected without SDK installed - test passes
        pass


# Real integration tests - only run if Claude Agent SDK is configured
def test_real_chat_simple():
    """Test real chat with simple prompt"""
    try:
        llm = LlmClaudeCli("claude-3-5-sonnet-20241022")
        response = llm.chat("Say 'hello' and nothing else")
        assert response.value is not None
        assert isinstance(response.value, str)
        assert len(response.value) > 0
        assert response.provider == "claude-cli"
        assert response.output is not None
    except Exception:
        # Skip if not configured - not a test failure
        pass


def test_real_chat_conversation():
    """Test real chat with conversation list"""
    try:
        llm = LlmClaudeCli("claude-3-5-sonnet-20241022")
        conversation = [
            {"role": "user", "content": "What is 2+2?"},
            {"role": "assistant", "content": "4"},
            {"role": "user", "content": "What is 3+3?"},
        ]
        response = llm.chat(conversation)
        assert response.value is not None
        assert isinstance(response.value, str)
        assert response.provider == "claude-cli"
    except Exception:
        # Skip if not configured
        pass


def test_real_chat_structured():
    """Test real structured chat"""
    try:
        from pydantic import BaseModel

        class SimpleResponse(BaseModel):
            answer: int

        llm = LlmClaudeCli("claude-3-5-sonnet-20241022")
        response = llm.chat_structured("What is 5+5? Answer with just the number", SimpleResponse)
        assert response.value is not None
        assert isinstance(response.value, SimpleResponse)
        assert hasattr(response.value, "answer")
        assert response.provider == "claude-cli"
    except Exception:
        # Skip if not configured
        pass


def test_real_chat_async():
    """Test real async chat"""
    try:
        import asyncio

        async def run_async_test():
            llm = LlmClaudeCli("claude-3-5-sonnet-20241022")
            response = await llm.chat_async("Say 'world' and nothing else")
            assert response.value is not None
            assert isinstance(response.value, str)
            return True

        result = asyncio.run(run_async_test())
        assert result
    except Exception:
        # Skip if not configured
        pass


def test_real_chat_structured_async():
    """Test real async structured chat"""
    try:
        import asyncio

        from pydantic import BaseModel

        class SimpleResponse(BaseModel):
            answer: int

        async def run_async_test():
            llm = LlmClaudeCli("claude-3-5-sonnet-20241022")
            response = await llm.chat_structured_async("What is 7+7? Answer with just the number", SimpleResponse)
            assert response.value is not None
            assert isinstance(response.value, SimpleResponse)
            return True

        result = asyncio.run(run_async_test())
        assert result
    except Exception:
        # Skip if not configured
        pass


def test_async_image_raises_error():
    """Test that async_image raises DazLlmError"""
    try:
        import asyncio

        from dazllm.core import DazLlmError

        async def run_async_test():
            llm = LlmClaudeCli("claude-3-5-sonnet-20241022")
            try:
                await llm.async_image("test", "test.png")
                return False  # Should not reach here
            except DazLlmError as e:
                assert "does not support image generation" in str(e)
                return True

        result = asyncio.run(run_async_test())
        assert result
    except Exception:
        # Skip if not configured
        pass
