"""
Test file for dazllm core functionality.

This file tests the main Llm class, ModelType enum, and error handling
to ensure the core dazllm functionality works as expected.
"""

import unittest

from dazllm import DazLlmError, ModelNotFoundError, ModelType
from dazllm.core import Llm, _coerce_model_type, _resolve_model_name_for_ctor

# Use OpenAI provider for consistent model validation testing (more likely to be available)
try:
    from dazllm.llm_openai import LlmOpenai as TestLlmClass

    TEST_MODEL = "openai:gpt-4o"
except ImportError:
    # Fallback to anthropic
    from dazllm.llm_anthropic import LlmAnthropic as TestLlmClass

    TEST_MODEL = "anthropic:claude-3-5-sonnet-20241022"

TEST_MODEL_INVALID = "invalid-format"


class TestLlmCore(unittest.TestCase):
    """Test cases for dazllm core functionality."""

    def test_model_name_parsing(self):
        """Test model name parsing with provider:model format."""
        try:
            llm = TestLlmClass(TEST_MODEL)
            # Extract provider and model from the TEST_MODEL
            provider, model = TEST_MODEL.split(":", 1)
            self.assertEqual(llm.provider, provider)
            self.assertEqual(llm.model, model)
        except Exception as e:
            # If the provider isn't configured, test fails
            self.fail(f"Provider {TEST_MODEL.split(':')[0]} not configured: {e}")

    def test_invalid_model_format(self):
        """Test that invalid model format raises DazLlmError."""
        with self.assertRaises(DazLlmError):
            TestLlmClass(TEST_MODEL_INVALID)

    def test_model_types(self):
        """Test that ModelType enum has expected values."""
        self.assertEqual(ModelType.PAID_BEST.value, "paid_best")
        self.assertEqual(ModelType.LOCAL_SMALL.value, "local_small")

    def test_model_type_enum_completeness(self):
        """Test that all expected model types exist."""
        expected_types = [
            ModelType.LOCAL_SMALL,
            ModelType.LOCAL_MEDIUM,
            ModelType.LOCAL_LARGE,
            ModelType.PAID_CHEAP,
            ModelType.PAID_BEST,
        ]
        # Just verify they exist without errors
        for model_type in expected_types:
            self.assertIsInstance(model_type.value, str)

    def test_llm_class_methods(self):
        """Test that Llm class has expected static methods."""
        self.assertTrue(hasattr(Llm, "get_providers"))
        self.assertTrue(hasattr(Llm, "model_named"))
        self.assertTrue(hasattr(Llm, "chat_static"))


class TestCoerceModelType(unittest.TestCase):
    """Test cases for _coerce_model_type function."""

    def test_coerce_none(self):
        """Test that None returns None."""
        self.assertIsNone(_coerce_model_type(None))

    def test_coerce_local_small_variants(self):
        """Test various ways of specifying local_small."""
        self.assertEqual(_coerce_model_type("local_small"), ModelType.LOCAL_SMALL)
        self.assertEqual(_coerce_model_type("local-small"), ModelType.LOCAL_SMALL)
        self.assertEqual(_coerce_model_type("local small"), ModelType.LOCAL_SMALL)
        self.assertEqual(_coerce_model_type("small_local"), ModelType.LOCAL_SMALL)
        self.assertEqual(_coerce_model_type("localsmall"), ModelType.LOCAL_SMALL)
        self.assertEqual(_coerce_model_type("LOCAL_SMALL"), ModelType.LOCAL_SMALL)
        self.assertEqual(_coerce_model_type("  local_small  "), ModelType.LOCAL_SMALL)

    def test_coerce_local_medium_variants(self):
        """Test various ways of specifying local_medium."""
        self.assertEqual(_coerce_model_type("local_medium"), ModelType.LOCAL_MEDIUM)
        self.assertEqual(_coerce_model_type("local-medium"), ModelType.LOCAL_MEDIUM)
        self.assertEqual(_coerce_model_type("medium_local"), ModelType.LOCAL_MEDIUM)
        self.assertEqual(_coerce_model_type("localmedium"), ModelType.LOCAL_MEDIUM)
        self.assertEqual(_coerce_model_type("LOCAL_MEDIUM"), ModelType.LOCAL_MEDIUM)

    def test_coerce_local_large_variants(self):
        """Test various ways of specifying local_large."""
        self.assertEqual(_coerce_model_type("local_large"), ModelType.LOCAL_LARGE)
        self.assertEqual(_coerce_model_type("local-large"), ModelType.LOCAL_LARGE)
        self.assertEqual(_coerce_model_type("large_local"), ModelType.LOCAL_LARGE)
        self.assertEqual(_coerce_model_type("locallarge"), ModelType.LOCAL_LARGE)
        self.assertEqual(_coerce_model_type("LOCAL_LARGE"), ModelType.LOCAL_LARGE)

    def test_coerce_paid_cheap_variants(self):
        """Test various ways of specifying paid_cheap."""
        self.assertEqual(_coerce_model_type("paid_cheap"), ModelType.PAID_CHEAP)
        self.assertEqual(_coerce_model_type("paid-cheap"), ModelType.PAID_CHEAP)
        self.assertEqual(_coerce_model_type("cheap_paid"), ModelType.PAID_CHEAP)
        self.assertEqual(_coerce_model_type("paidcheap"), ModelType.PAID_CHEAP)
        self.assertEqual(_coerce_model_type("PAID_CHEAP"), ModelType.PAID_CHEAP)

    def test_coerce_paid_best_variants(self):
        """Test various ways of specifying paid_best."""
        self.assertEqual(_coerce_model_type("paid_best"), ModelType.PAID_BEST)
        self.assertEqual(_coerce_model_type("paid-best"), ModelType.PAID_BEST)
        self.assertEqual(_coerce_model_type("best_paid"), ModelType.PAID_BEST)
        self.assertEqual(_coerce_model_type("paidbest"), ModelType.PAID_BEST)
        self.assertEqual(_coerce_model_type("PAID_BEST"), ModelType.PAID_BEST)

    def test_coerce_invalid_returns_none(self):
        """Test that invalid model types return None."""
        self.assertIsNone(_coerce_model_type("invalid"))
        self.assertIsNone(_coerce_model_type("unknown_type"))
        self.assertIsNone(_coerce_model_type(""))
        self.assertIsNone(_coerce_model_type("123"))


class TestResolveModelNameForCtor(unittest.TestCase):
    """Test cases for _resolve_model_name_for_ctor function."""

    def test_resolve_explicit_model_name(self):
        """Test that explicit model_name is returned unchanged."""
        result = _resolve_model_name_for_ctor("provider:model", None, None, None)
        self.assertEqual(result, "provider:model")

        result = _resolve_model_name_for_ctor("openai:gpt-4", None, None, None)
        self.assertEqual(result, "openai:gpt-4")

    def test_resolve_provider_and_model(self):
        """Test provider + explicit model composition."""
        result = _resolve_model_name_for_ctor(None, "openai", "gpt-4", None)
        self.assertEqual(result, "openai:gpt-4")

    def test_resolve_provider_only(self):
        """Test provider without model gets provider default."""
        result = _resolve_model_name_for_ctor(None, "openai", None, None)
        self.assertIn("openai:", result)

    def test_resolve_provider_with_model_type(self):
        """Test provider + model_type gets type-specific default."""
        result = _resolve_model_name_for_ctor(None, "openai", None, ModelType.PAID_BEST)
        self.assertIn("openai:", result)

    def test_resolve_model_alias_to_type(self):
        """Test that model alias is converted to model_type."""
        result = _resolve_model_name_for_ctor(None, "openai", "paid_best", None)
        self.assertIn("openai:", result)

    def test_resolve_no_provider_uses_resolver(self):
        """Test that no provider delegates to ModelResolver."""
        result = _resolve_model_name_for_ctor(None, None, None, ModelType.PAID_BEST)
        self.assertIsInstance(result, str)
        self.assertIn(":", result)

    def test_resolve_invalid_provider_raises_error(self):
        """Test that invalid provider raises ModelNotFoundError."""
        with self.assertRaises(ModelNotFoundError):
            _resolve_model_name_for_ctor(None, "nonexistent_provider", None, None)


class TestLlmConstructors(unittest.TestCase):
    """Test cases for Llm constructor and class methods."""

    def test_from_provider_method(self):
        """Test from_provider class method."""
        # Use model_named which properly creates instances
        llm = Llm.model_named(TEST_MODEL)
        provider, _ = TEST_MODEL.split(":", 1)
        self.assertEqual(llm.provider, provider)

    def test_fromProvider_method_creates_with_default(self):
        """Test that we can construct with provider-default pattern."""
        # Test the resolution logic
        from dazllm.core import _resolve_model_name_for_ctor

        result = _resolve_model_name_for_ctor(None, "claude-cli", None, None)
        self.assertIn("claude-cli:", result)

    def test_local_small_shortcut(self):
        """Test LocalSmall shortcut creates proper model string."""
        # Test the resolution via model_named
        from dazllm.model_resolver import ModelResolver

        result = ModelResolver.resolve_model(None, ModelType.LOCAL_SMALL)
        self.assertIsInstance(result, str)
        self.assertIn(":", result)

    def test_local_medium_shortcut(self):
        """Test LocalMedium shortcut creates proper model string."""
        from dazllm.model_resolver import ModelResolver

        result = ModelResolver.resolve_model(None, ModelType.LOCAL_MEDIUM)
        self.assertIsInstance(result, str)
        self.assertIn(":", result)

    def test_local_large_shortcut(self):
        """Test LocalLarge shortcut creates proper model string."""
        from dazllm.model_resolver import ModelResolver

        result = ModelResolver.resolve_model(None, ModelType.LOCAL_LARGE)
        self.assertIsInstance(result, str)
        self.assertIn(":", result)

    def test_paid_cheap_shortcut(self):
        """Test PaidCheap shortcut creates proper model string."""
        from dazllm.model_resolver import ModelResolver

        result = ModelResolver.resolve_model(None, ModelType.PAID_CHEAP)
        self.assertIsInstance(result, str)
        self.assertIn(":", result)

    def test_paid_best_shortcut(self):
        """Test PaidBest shortcut creates proper model string."""
        from dazllm.model_resolver import ModelResolver

        result = ModelResolver.resolve_model(None, ModelType.PAID_BEST)
        self.assertIsInstance(result, str)
        self.assertIn(":", result)

    def test_model_named_caching(self):
        """Test that model_named caches instances."""
        llm1 = Llm.model_named(TEST_MODEL)
        llm2 = Llm.model_named(TEST_MODEL)
        # Should return same instance due to caching
        self.assertIs(llm1, llm2)

    def test_get_provider_info(self):
        """Test get_provider_info class method."""
        info = Llm.get_provider_info("claude-cli")
        self.assertIsInstance(info, dict)
        self.assertIn("configured", info)

    def test_get_all_providers_info(self):
        """Test get_all_providers_info class method."""
        all_info = Llm.get_all_providers_info()
        self.assertIsInstance(all_info, dict)
        self.assertGreater(len(all_info), 0)


class TestLlmResponse(unittest.TestCase):
    """Test cases for LlmResponse NamedTuple."""

    def test_llm_response_structure(self):
        """Test LlmResponse has correct fields."""
        from dazllm.core import LlmResponse

        response = LlmResponse(value="test", output="", provider="test-provider")
        self.assertEqual(response.value, "test")
        self.assertEqual(response.output, "")
        self.assertEqual(response.provider, "test-provider")

    def test_llm_response_with_basemodel(self):
        """Test LlmResponse can hold BaseModel value."""
        from pydantic import BaseModel

        from dazllm.core import LlmResponse

        class TestModel(BaseModel):
            field: str

        model = TestModel(field="value")
        response = LlmResponse(value=model, output="", provider="test-provider")
        self.assertIsInstance(response.value, BaseModel)


class TestCheckConfiguration(unittest.TestCase):
    """Test cases for check_configuration function."""

    def test_check_configuration_returns_dict(self):
        """Test that check_configuration returns a dictionary."""
        from dazllm.core import check_configuration

        status = check_configuration()
        self.assertIsInstance(status, dict)

    def test_check_configuration_has_provider_entries(self):
        """Test that check_configuration includes provider entries."""
        from dazllm.core import check_configuration

        status = check_configuration()
        self.assertGreater(len(status), 0)
        for provider_name, provider_status in status.items():
            self.assertIsInstance(provider_status, dict)
            self.assertIn("configured", provider_status)
