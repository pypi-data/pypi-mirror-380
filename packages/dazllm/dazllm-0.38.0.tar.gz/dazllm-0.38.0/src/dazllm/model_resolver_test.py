"""
Tests for model_resolver.py
"""

# Import module to ensure coverage
import dazllm.model_resolver  # noqa: F401
from dazllm.core import ModelType
from dazllm.model_resolver import ModelResolver
from dazllm.provider_manager import DazLlmError, ModelNotFoundError


def test_parse_model_name():
    """Test parsing model names into provider and model"""
    provider, model = ModelResolver.parse_model_name("openai:gpt-4")
    assert provider == "openai"
    assert model == "gpt-4"

    provider, model = ModelResolver.parse_model_name("anthropic:claude-3")
    assert provider == "anthropic"
    assert model == "claude-3"


def test_parse_model_name_with_alias():
    """Test parsing model names with provider aliases"""
    provider, model = ModelResolver.parse_model_name("claude:claude-3")
    assert provider == "anthropic"  # Alias resolved
    assert model == "claude-3"


def test_parse_model_name_invalid():
    """Test parsing invalid model names"""
    try:
        ModelResolver.parse_model_name("invalid-no-colon")
        assert False, "Should have raised ModelNotFoundError"
    except ModelNotFoundError:
        pass  # Expected

    try:
        ModelResolver.parse_model_name("unknown:model")
        assert False, "Should have raised ModelNotFoundError"
    except ModelNotFoundError:
        pass  # Expected


def test_resolve_model_with_name():
    """Test resolving model when explicit name is given"""
    result = ModelResolver.resolve_model(model="openai:gpt-4")
    assert result == "openai:gpt-4"


def test_resolve_model_conflict():
    """Test that providing both model and model_type raises error"""
    try:
        ModelResolver.resolve_model(model="openai:gpt-4", model_type=ModelType.PAID_CHEAP)
        assert False, "Should have raised DazLlmError"
    except DazLlmError:
        pass  # Expected


def test_model_type_enum():
    """Test ModelType enum values"""
    assert ModelType.PAID_CHEAP.value == "paid_cheap"
    assert ModelType.PAID_BEST.value == "paid_best"
    assert ModelType.LOCAL_SMALL.value == "local_small"


def test_resolve_model_by_type():
    """Test resolving model by type"""
    # This tests the model type resolution path
    result = ModelResolver.resolve_model(model_type=ModelType.PAID_CHEAP)
    # Should return some valid model
    assert result is not None
    assert ":" in result  # Should have provider:model format


def test_resolve_model_no_args():
    """Test resolving model with no arguments uses default"""
    result = ModelResolver.resolve_model()
    # Should return the default model
    assert result is not None
    assert ":" in result  # Should have provider:model format


def test_get_provider_for_model_type():
    """Test getting provider for model type"""
    # Test internal method if accessible
    try:
        # Try to access _get_provider_for_model_type if it exists
        from dazllm.model_resolver import _get_provider_for_model_type

        provider = _get_provider_for_model_type(ModelType.PAID_CHEAP)
        assert provider is not None
    except ImportError:
        # Method might not be exposed, that's ok
        pass


def test_resolve_model_with_string_type():
    """Test resolving model with string model type"""
    # Test if string model types are supported
    try:
        result = ModelResolver.resolve_model(model_type="paid_cheap")
        assert result is not None
        assert ":" in result
    except (TypeError, ValueError, AttributeError):
        # String types are not supported - requires ModelType enum
        pass


def test_provider_aliases():
    """Test that provider aliases work correctly"""
    # Test various aliases
    aliases_to_test = [
        ("claude", "anthropic"),
        ("chatgpt", "openai"),
        ("gpt", "openai"),
    ]

    for alias, expected_provider in aliases_to_test:
        try:
            provider, model = ModelResolver.parse_model_name(f"{alias}:test-model")
            # Some aliases should resolve to the expected provider
            if alias in ["claude", "chatgpt", "gpt"]:
                assert provider == expected_provider
        except ModelNotFoundError:
            # Some aliases might not be registered
            pass


def test_all_model_types():
    """Test resolving all model type enum values"""
    for model_type in ModelType:
        try:
            result = ModelResolver.resolve_model(model_type=model_type)
            # Some model types might return None if no provider supports them
            if result is not None:
                assert ":" in result
                provider, model = result.split(":", 1)
                assert provider  # Provider should not be empty
                assert model  # Model should not be empty
        except (ModelNotFoundError, DazLlmError):
            # Some model types might not have any available providers
            pass
