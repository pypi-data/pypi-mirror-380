"""
Anthropic implementation for dazllm
"""

import keyring
import json
from typing import Type
from pydantic import BaseModel

from .core import Llm, Conversation, ConfigurationError, DazLlmError, _run_sync, LlmResponse


class LlmAnthropic(Llm):
    """Anthropic implementation"""

    def __init__(self, model: str):
        super().__init__(model)
        self.check_config()

        # Import Anthropic client
        try:
            import anthropic

            self.client = anthropic.Anthropic(api_key=self._get_api_key())
        except ImportError as exc:
            raise ConfigurationError(
                "Anthropic library not installed. Run: pip install anthropic"
            ) from exc

    @staticmethod
    def default_model() -> str:
        """Default model for Anthropic"""
        return "claude-3-5-sonnet-20241022"

    @staticmethod
    def default_for_type(model_type: str) -> str:
        """Get default model for a given type"""
        defaults = {
            "local_small": None,  # Anthropic doesn't have local models
            "local_medium": None,
            "local_large": None,
            "paid_cheap": "claude-3-haiku-20240307",
            "paid_best": "claude-3-5-sonnet-20241022",
        }
        return defaults.get(model_type)

    @staticmethod
    def capabilities() -> set[str]:
        """Return set of capabilities this provider supports"""
        return {"chat", "structured"}

    @staticmethod
    def supported_models() -> list[str]:
        """Return list of models this provider supports"""
        return [
            "claude-3-5-sonnet-20241022",
            "claude-3-5-sonnet-20240620",
            "claude-3-opus-20240229",
            "claude-3-sonnet-20240229",
            "claude-3-haiku-20240307",
        ]

    @staticmethod
    def check_config():
        """Check if Anthropic is properly configured"""
        api_key = keyring.get_password("dazllm", "anthropic_api_key")
        if not api_key:
            raise ConfigurationError(
                "Anthropic API key not found in keyring. Set with: keyring set dazllm anthropic_api_key"
            )

    def _get_api_key(self) -> str:
        """Get Anthropic API key from keyring"""
        api_key = keyring.get_password("dazllm", "anthropic_api_key")
        if not api_key:
            raise ConfigurationError("Anthropic API key not found in keyring")
        return api_key

    def _normalize_conversation(self, conversation: Conversation) -> tuple[str, list]:
        """Convert conversation to Anthropic message format"""
        if isinstance(conversation, str):
            messages = [{"role": "user", "content": conversation}]
        else:
            messages = conversation.copy()

        # Extract system message if present
        system_message = ""
        filtered_messages = []

        for msg in messages:
            if msg["role"] == "system":
                system_message = msg["content"]
            else:
                filtered_messages.append(msg)

        return system_message, filtered_messages

    def chat(self, conversation: Conversation, force_json: bool = False) -> LlmResponse:
        """Sync wrapper; blocks on chat_async."""
        return _run_sync(self.chat_async(conversation, force_json))

    async def chat_async(self, conversation: Conversation, force_json: bool = False) -> LlmResponse:
        import asyncio
        system_message, messages = self._normalize_conversation(conversation)
        kwargs = {"model": self.model, "max_tokens": 4000, "messages": messages}
        if system_message:
            kwargs["system"] = system_message

        try:
            from anthropic import AsyncAnthropic  # type: ignore
            client = AsyncAnthropic(api_key=self._get_api_key())
            response = await client.messages.create(**kwargs)  # type: ignore[arg-type]
            content = response.content[0].text
            return LlmResponse(value=content, output="", provider=self.provider_name)
        except Exception:
            def _call_sync():
                try:
                    return self.client.messages.create(**kwargs)
                except Exception as e:  # noqa: BLE001
                    raise DazLlmError(f"Anthropic API error: {e}") from e
            resp = await asyncio.to_thread(_call_sync)
            content = resp.content[0].text
            return LlmResponse(value=content, output="", provider=self.provider_name)

    def chat_structured(
        self, conversation: Conversation, schema: Type[BaseModel], context_size: int = 0
    ) -> LlmResponse:
        """Sync wrapper; blocks on chat_structured_async."""
        return _run_sync(self.chat_structured_async(conversation, schema, context_size))

    async def chat_structured_async(
        self, conversation: Conversation, schema: Type[BaseModel], context_size: int = 0
    ) -> LlmResponse:
        import asyncio
        system_message, messages = self._normalize_conversation(conversation)
        schema_json = schema.model_json_schema()
        schema_instruction = (
            "\n\nPlease respond with valid JSON matching this schema:\n"
            f"{json.dumps(schema_json, indent=2)}"
        )
        if system_message:
            system_message += schema_instruction
        else:
            system_message = f"You are a helpful assistant.{schema_instruction}"
        kwargs = {"model": self.model, "max_tokens": 4000, "messages": messages, "system": system_message}

        async def _call_async():
            try:
                from anthropic import AsyncAnthropic  # type: ignore
                client = AsyncAnthropic(api_key=self._get_api_key())
                return await client.messages.create(**kwargs)  # type: ignore[arg-type]
            except Exception:
                def _call_sync():
                    return self.client.messages.create(**kwargs)
                return await asyncio.to_thread(_call_sync)

        response = await _call_async()
        content = response.content[0].text
        try:
            start = content.find("{")
            end = content.rfind("}") + 1
            data = json.loads(content[start:end] if start >= 0 and end > start else content)
            result = schema(**data)
            return LlmResponse(value=result, output="", provider=self.provider_name)
        except json.JSONDecodeError as exc:  # noqa: PERF203
            raise DazLlmError(f"Could not parse JSON response: {content}") from exc
        except Exception as e:  # noqa: BLE001
            raise DazLlmError(f"Could not create Pydantic model: {e}") from e

    def image(
        self, prompt: str, file_name: str, width: int = 1024, height: int = 1024
    ) -> str:
        """Sync wrapper; blocks on async_image."""
        return _run_sync(self.async_image(prompt, file_name, width, height))

    async def async_image(
        self, prompt: str, file_name: str, width: int = 1024, height: int = 1024
    ) -> str:
        raise DazLlmError(
            (
                "Image generation not supported by Anthropic. "
                "Use OpenAI or other providers for image generation."
            )
        )

    def get_context_length(self) -> int:
        """Get the context length for the current Claude model"""
        # Known context lengths for Claude models
        context_lengths = {
            "claude-3-5-sonnet-20241022": 200000,    # 200K tokens
            "claude-3-5-sonnet-20240620": 200000,    # 200K tokens
            "claude-3-5-haiku-20241022": 200000,     # 200K tokens
            "claude-3-opus-20240229": 200000,        # 200K tokens
            "claude-3-sonnet-20240229": 200000,      # 200K tokens
            "claude-3-haiku-20240307": 200000,       # 200K tokens
            "claude-2.1": 200000,                    # 200K tokens
            "claude-2.0": 100000,                    # 100K tokens
            "claude-instant-1.2": 100000,            # 100K tokens
        }

        return context_lengths.get(self.model, 200000)  # Default to 200K


import unittest  # noqa: E402


class TestLlmAnthropic(unittest.TestCase):
    """Test cases for LlmAnthropic"""

    def test_default_model(self):
        """Test default model"""
        self.assertEqual(LlmAnthropic.default_model(), "claude-3-5-sonnet-20241022")

    def test_default_for_type(self):
        """Test default for type"""
        self.assertEqual(LlmAnthropic.default_for_type("paid_best"), "claude-3-5-sonnet-20241022")
        self.assertIsNone(LlmAnthropic.default_for_type("local_small"))

    def test_capabilities(self):
        """Test capabilities"""
        caps = LlmAnthropic.capabilities()
        self.assertIn("chat", caps)
        self.assertIn("structured", caps)

    def test_supported_models(self):
        """Test supported models"""
        models = LlmAnthropic.supported_models()
        self.assertIn("claude-3-5-sonnet-20241022", models)
        self.assertIsInstance(models, list)

    def test_image_not_supported(self):
        """Test image generation raises error"""
        try:
            llm = LlmAnthropic("anthropic:claude-3-haiku-20240307")
            with self.assertRaises(DazLlmError):
                llm.image("test", "test.jpg")
        except ConfigurationError:
            pass  # Expected without API key
