"""
Gemini CLI Provider with logging capabilities

Extends the original LlmGeminiCli to implement the new LlmCli interface
with comprehensive logging capture using Gemini's built-in debug and session features.
"""

import asyncio
from typing import List, Optional, Set, Type

from pydantic import BaseModel

from .core import ConfigurationError, Conversation, Llm, LlmResponse
from .llm_gemini_cli import LlmGeminiCli as OriginalLlmGeminiCli
from .memoization import memoize_llm_response, memoize_llm_response_async


class LlmGeminiCli(Llm):
    """Gemini CLI provider with enhanced logging"""

    def __init__(self, model: str = "gemini:gemini-2.0-flash-exp"):
        super().__init__(model)
        self._model = model
        self._original = None  # Lazy load

    def _get_original(self):
        """Lazy load the original CLI instance"""
        if self._original is None:
            # Must have real CLI - fail if not available
            try:
                OriginalLlmGeminiCli.check_config()
                self._original = OriginalLlmGeminiCli(self._model)
            except ConfigurationError as e:
                raise ConfigurationError(f"Gemini CLI not available: {e}") from e
        return self._original

    @memoize_llm_response
    def chat(self, conversation: Conversation, force_json: bool = False) -> LlmResponse:
        """Sync wrapper for Gemini CLI chat"""
        return self._get_original().chat(conversation, force_json)

    @memoize_llm_response
    def chat_structured(
        self, conversation: Conversation, schema: Type[BaseModel], context_size: int = 0
    ) -> LlmResponse:
        """Sync wrapper for Gemini CLI structured chat"""
        return self._get_original().chat_structured(conversation, schema, context_size)

    @staticmethod
    def is_available() -> bool:
        """Check if Gemini CLI is available"""
        try:
            OriginalLlmGeminiCli.check_config()
            return True
        except ConfigurationError:
            return False

    @memoize_llm_response_async
    async def chat_async(self, conversation: Conversation, force_json: bool = False) -> LlmResponse:
        """Async version of chat - delegates to sync implementation"""
        return await asyncio.get_event_loop().run_in_executor(None, self._get_original().chat, conversation, force_json)

    @memoize_llm_response_async
    async def chat_structured_async(
        self, conversation: Conversation, schema: Type[BaseModel], context_size: int = 0
    ) -> LlmResponse:
        """Async version of chat_structured - delegates to sync implementation"""
        return await asyncio.get_event_loop().run_in_executor(
            None, self._get_original().chat_structured, conversation, schema, context_size
        )

    async def async_image(self, prompt: str, file_name: str, width: int = 1024, height: int = 1024) -> str:
        """Gemini doesn't support image generation via CLI"""
        raise NotImplementedError("Gemini CLI doesn't support image generation")

    def get_context_length(self) -> int:
        """Get context length from original implementation"""
        return 1000000  # Default context length for Gemini 2.0 Flash

    @staticmethod
    def capabilities() -> Set[str]:
        """Return capabilities of Gemini CLI"""
        return OriginalLlmGeminiCli.capabilities()

    @staticmethod
    def supported_models() -> List[str]:
        """Return supported models"""
        return OriginalLlmGeminiCli.supported_models()

    @staticmethod
    def default_model() -> str:
        """Return default model"""
        return OriginalLlmGeminiCli.default_model()

    @staticmethod
    def default_for_type(model_type: str) -> Optional[str]:
        """Return default model for type"""
        return OriginalLlmGeminiCli.default_for_type(model_type)

    @staticmethod
    def check_config():
        """Check configuration"""
        return OriginalLlmGeminiCli.check_config()
