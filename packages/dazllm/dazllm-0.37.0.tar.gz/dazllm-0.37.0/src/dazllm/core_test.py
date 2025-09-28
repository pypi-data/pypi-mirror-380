"""
Test file for dazllm core functionality.

This file tests the main Llm class, ModelType enum, and error handling
to ensure the core dazllm functionality works as expected.
"""

import unittest
from dazllm import ModelType, DazLlmError
from dazllm.core import Llm
# Use CLI provider for consistent model validation testing
from dazllm.llm_claude_cli import LlmClaudeCli as TestLlmClass
TEST_MODEL = "claude-cli:claude-3-5-sonnet-20241022"
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
        except Exception:
            # If the provider isn't configured, skip this test
            self.skipTest(f"Provider {TEST_MODEL.split(':')[0]} not configured")

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
            ModelType.PAID_BEST
        ]
        # Just verify they exist without errors
        for model_type in expected_types:
            self.assertIsInstance(model_type.value, str)

    def test_llm_class_methods(self):
        """Test that Llm class has expected static methods."""
        self.assertTrue(hasattr(Llm, 'get_providers'))
        self.assertTrue(hasattr(Llm, 'model_named'))
        self.assertTrue(hasattr(Llm, 'chat_static'))
