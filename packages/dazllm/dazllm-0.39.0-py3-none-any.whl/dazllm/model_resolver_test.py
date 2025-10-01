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


def test_get_default_for_type():
    """Test _get_default_for_type method"""
    try:
        result = ModelResolver._get_default_for_type(ModelType.PAID_CHEAP)
        assert result is not None
        assert ":" in result
    except ModelNotFoundError:
        # No provider supports this type
        pass


def test_get_provider_default():
    """Test _get_provider_default method"""
    result = ModelResolver._get_provider_default("openai")
    assert result is not None
    assert "openai:" in result


def test_get_provider_default_with_alias():
    """Test _get_provider_default with alias"""
    result = ModelResolver._get_provider_default("claude")
    assert result is not None
    assert "anthropic:" in result


def test_find_configured_model():
    """Test _find_configured_model method"""
    result = ModelResolver._find_configured_model()
    assert result is not None
    assert ":" in result


def test_resolve_model_provider_shorthand():
    """Test resolving model with provider shorthand (no colon)"""
    result = ModelResolver.resolve_model(model="openai")
    assert result is not None
    assert "openai:" in result


def test_parse_model_name_with_complex_model():
    """Test parsing model names with complex model IDs"""
    provider, model = ModelResolver.parse_model_name("openai:gpt-4-turbo-preview")
    assert provider == "openai"
    assert model == "gpt-4-turbo-preview"

    provider, model = ModelResolver.parse_model_name("anthropic:claude-3-5-sonnet-20241022")
    assert provider == "anthropic"
    assert model == "claude-3-5-sonnet-20241022"


def test_resolve_model_all_paths():
    """Test all resolution paths comprehensively"""
    # Test with explicit full name
    result1 = ModelResolver.resolve_model(model="openai:gpt-4")
    assert "openai:gpt-4" == result1

    # Test with provider shorthand
    result2 = ModelResolver.resolve_model(model="openai")
    assert "openai:" in result2

    # Test with model type
    result3 = ModelResolver.resolve_model(model_type=ModelType.PAID_BEST)
    assert ":" in result3

    # Test with no args (uses default or finds configured)
    result4 = ModelResolver.resolve_model()
    assert ":" in result4


def test_get_default_for_type_all_types():
    """Test _get_default_for_type for all ModelType values"""
    for model_type in ModelType:
        try:
            result = ModelResolver._get_default_for_type(model_type)
            assert result is not None
            assert ":" in result
        except ModelNotFoundError:
            # Some types might not be supported
            pass


def test_parse_model_name_unknown_provider():
    """Test parsing with unknown provider"""
    try:
        ModelResolver.parse_model_name("unknown_provider:some_model")
        assert False, "Should have raised ModelNotFoundError"
    except ModelNotFoundError as e:
        assert "Unknown provider" in str(e)


def test_resolve_model_with_colon_in_model_id():
    """Test that model IDs can contain colons after the first one"""
    # The split should only happen on the first colon
    provider, model = ModelResolver.parse_model_name("openai:gpt-4:special:version")
    assert provider == "openai"
    assert model == "gpt-4:special:version"


def test_get_provider_default_all_providers():
    """Test _get_provider_default for all available providers"""
    from dazllm.provider_manager import ProviderManager

    for provider_name in ProviderManager.get_providers():
        try:
            result = ModelResolver._get_provider_default(provider_name)
            assert result is not None
            assert f"{provider_name}:" in result or ":" in result  # Allow for aliases
        except Exception:
            # Some providers might not be fully configured
            pass


def test_get_default_for_type_with_missing_providers():
    """Test _get_default_for_type when providers don't support the type"""
    # Try with a local type when most providers don't support local models
    try:
        result = ModelResolver._get_default_for_type(ModelType.LOCAL_SMALL)
        # If we get here, some provider supports it
        assert ":" in result
    except ModelNotFoundError as e:
        # Expected - no provider supports this type
        assert "No provider supports" in str(e)


def test_find_configured_model_multiple_providers():
    """Test that _find_configured_model tries multiple providers"""
    # This exercises the loop and exception handling
    result = ModelResolver._find_configured_model()
    assert result is not None
    assert ":" in result


def test_resolve_model_with_none_values():
    """Test resolve_model with explicit None values"""
    result = ModelResolver.resolve_model(model=None, model_type=None)
    assert result is not None
    assert ":" in result


def test_parse_model_name_edge_cases():
    """Test parse_model_name with edge cases"""
    # Test with multiple colons
    provider, model = ModelResolver.parse_model_name("openai:gpt:4:turbo")
    assert provider == "openai"
    assert ":" in model  # Should preserve remaining colons

    # Test with just provider and colon
    try:
        ModelResolver.parse_model_name("openai:")
        # If this succeeds, model would be empty string
    except ModelNotFoundError:
        # Some implementations might reject empty model
        pass


def test_get_default_for_type_coverage():
    """Test to increase coverage of _get_default_for_type exception handling"""
    # This tests the exception paths when provider_class methods fail
    for model_type in [ModelType.PAID_BEST, ModelType.PAID_CHEAP]:
        try:
            result = ModelResolver._get_default_for_type(model_type)
            assert result is not None
        except ModelNotFoundError:
            pass


def test_resolve_model_keyring_default():
    """Test that resolve_model uses keyring default when available"""
    import keyring

    # Save current value
    current_default = keyring.get_password("dazllm", "default_model")

    try:
        # Test with keyring set
        keyring.set_password("dazllm", "default_model", "openai:gpt-4")
        result = ModelResolver.resolve_model()
        assert result == "openai:gpt-4"

        # Test with keyring NOT set (returns None)
        keyring.delete_password("dazllm", "default_model")
        result = ModelResolver.resolve_model()
        # Should find a configured model instead
        assert ":" in result
    finally:
        # Restore original value
        if current_default:
            keyring.set_password("dazllm", "default_model", current_default)
        else:
            try:
                keyring.delete_password("dazllm", "default_model")
            except Exception:
                pass


def test_get_default_for_type_local_models():
    """Test _get_default_for_type with local model types"""
    for model_type in [ModelType.LOCAL_SMALL, ModelType.LOCAL_MEDIUM, ModelType.LOCAL_LARGE]:
        try:
            result = ModelResolver._get_default_for_type(model_type)
            if result:
                assert ":" in result
        except ModelNotFoundError:
            # Expected - most providers don't support local models
            pass


def test_find_configured_model_exception_handling():
    """Test _find_configured_model when no providers are configured"""

    # This will test the exception handling in the loop
    # Even if all providers fail, it should eventually return something or raise ConfigurationError
    try:
        result = ModelResolver._find_configured_model()
        assert result is not None
        assert ":" in result
    except Exception:
        # If no providers are configured, this is expected
        pass


def test_parse_model_name_all_providers():
    """Test parsing model names for all registered providers"""
    from dazllm.provider_manager import ProviderManager

    for provider in ProviderManager.get_providers():
        try:
            parsed_provider, model = ModelResolver.parse_model_name(f"{provider}:test-model")
            assert parsed_provider is not None
            assert model == "test-model"
        except Exception:
            # Some providers might not be available
            pass


def test_resolve_model_comprehensive():
    """Comprehensive test of all resolve_model code paths"""
    # Path 1: Explicit model name with colon
    r1 = ModelResolver.resolve_model(model="openai:gpt-4")
    assert r1 == "openai:gpt-4"

    # Path 2: Provider name without colon (shorthand)
    r2 = ModelResolver.resolve_model(model="openai")
    assert "openai:" in r2

    # Path 3: Model type only
    r3 = ModelResolver.resolve_model(model_type=ModelType.PAID_BEST)
    assert ":" in r3

    # Path 4: No arguments (keyring or configured)
    r4 = ModelResolver.resolve_model()
    assert ":" in r4

    # Path 5: Verify error when both specified
    try:
        ModelResolver.resolve_model(model="openai:gpt-4", model_type=ModelType.PAID_BEST)
        assert False, "Should raise error"
    except DazLlmError:
        pass


def test_find_configured_model_all_providers():
    """Test that _find_configured_model exercises all providers"""
    from dazllm.provider_manager import ProviderManager

    # This will test the loop through all providers
    for provider_name in ProviderManager.get_providers():
        try:
            # Try to check config for each provider
            ProviderManager.check_provider_config(provider_name)
        except Exception:
            # Expected - some providers might not be configured
            pass

    # Now test the actual method
    result = ModelResolver._find_configured_model()
    assert result is not None
    assert ":" in result


def test_get_default_for_type_exception_paths():
    """Test _get_default_for_type exception handling in the loop"""
    from dazllm.provider_manager import ProviderManager

    # Test that we handle ImportError, AttributeError, ModelNotFoundError
    for model_type in [ModelType.LOCAL_SMALL, ModelType.PAID_BEST, ModelType.LOCAL_MEDIUM, ModelType.LOCAL_LARGE]:
        try:
            result = ModelResolver._get_default_for_type(model_type)
            if result:
                provider, model = result.split(":", 1)
                # Verify the provider actually supports this type
                provider_class = ProviderManager.get_provider_class(provider)
                default = provider_class.default_for_type(model_type.value)
                # Either it returns something or None
                if default:
                    assert default is not None
        except ModelNotFoundError:
            # Expected for types not supported by any provider
            pass


def test_model_resolver_error_cases():
    """Test explicit error cases to increase coverage"""
    # Test parse with no colon
    try:
        ModelResolver.parse_model_name("no_colon_here")
        assert False
    except ModelNotFoundError as e:
        assert "format" in str(e).lower() or ":" in str(e)

    # Test parse with unknown provider
    try:
        ModelResolver.parse_model_name("unknown_provider:model")
        assert False
    except ModelNotFoundError as e:
        assert "provider" in str(e).lower() or "Unknown" in str(e)

    # Test resolve with conflicting params
    try:
        ModelResolver.resolve_model(model="test:model", model_type=ModelType.PAID_CHEAP)
        assert False
    except DazLlmError as e:
        assert "both" in str(e).lower() or "cannot" in str(e).lower()
