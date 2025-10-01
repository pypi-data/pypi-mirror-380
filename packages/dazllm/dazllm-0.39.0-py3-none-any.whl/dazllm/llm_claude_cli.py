"""
Claude CLI implementation for dazllm
Uses the Claude Agent SDK for LLM interactions
"""

import json
from typing import Optional, Set, Type

from pydantic import BaseModel

from .core import ConfigurationError, Conversation, DazLlmError, Llm, LlmResponse


class LlmClaudeCli(Llm):
    """Claude CLI implementation using Claude Agent SDK"""

    def __init__(self, model: str):
        # Handle the case where model might already have "claude-cli:" prefix
        if model.startswith("claude-cli:"):
            model = model[11:]  # Remove "claude-cli:" prefix
        super().__init__(f"claude-cli:{model}")
        self.model = model if model else self.default_model()
        self.check_config()

    @staticmethod
    def default_model() -> str:
        """Default model for Claude CLI"""
        return "claude-3-5-sonnet-20241022"

    @staticmethod
    def default_for_type(model_type: str) -> Optional[str]:
        """Get default model for a given type"""
        defaults = {
            "local_small": None,  # Claude doesn't have local models
            "local_medium": None,
            "local_large": None,
            "paid_cheap": "claude-3-5-haiku-20241022",
            "paid_best": "claude-3-5-sonnet-20241022",
        }
        return defaults.get(model_type)

    @staticmethod
    def capabilities() -> Set[str]:
        """Return set of capabilities this provider supports"""
        return {"chat", "structured"}

    @staticmethod
    def supported_models() -> list[str]:
        """Return list of models this provider supports"""
        return [
            "claude-3-5-sonnet-20241022",
            "claude-3-5-haiku-20241022",
            "claude-3-opus-20240229",
            "claude-3-sonnet-20240229",
            "claude-3-haiku-20240307",
        ]

    @classmethod
    def is_available(cls) -> bool:
        """Check if Claude CLI is available"""
        try:
            cls.check_config()
            return True
        except ConfigurationError:
            return False

    @staticmethod
    def check_config():
        """Check if Claude Agent SDK is properly configured"""
        try:
            # Try to import the claude_agent_sdk
            import claude_agent_sdk  # noqa: F401
        except ImportError as e:
            raise ConfigurationError("Claude Agent SDK not installed. Run: pip install claude-agent-sdk") from e

    def _normalize_conversation(self, conversation: Conversation) -> str:
        """Convert conversation to prompt string for Claude Agent SDK"""
        if isinstance(conversation, str):
            return conversation

        # For message list, create a structured prompt
        prompt_parts = []
        for msg in conversation:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            if role == "system":
                prompt_parts.append(f"<system>{content}</system>")
            elif role == "assistant":
                prompt_parts.append(f"Assistant: {content}")
            else:
                prompt_parts.append(f"Human: {content}")

        return "\n".join(prompt_parts)

    async def chat_async(self, conversation: Conversation, force_json: bool = False) -> LlmResponse:
        """Async chat using Claude Agent SDK"""
        from claude_agent_sdk import query

        prompt = self._normalize_conversation(conversation)
        if force_json:
            prompt = f"{prompt}\n\nPlease respond with valid JSON only, no other text."

        # Collect all messages from the async iterator
        messages = []
        try:
            async for message in query(prompt=prompt):
                messages.append(str(message))
        except Exception as e:
            raise DazLlmError(f"Claude Agent SDK error: {e}") from e

        # Combine all messages into final response
        response_text = "".join(messages)
        output = f"Claude CLI completed for model: {self.model}"

        return LlmResponse(value=response_text, output=output, provider=self.provider)

    async def chat_structured_async(
        self, conversation: Conversation, schema: Type[BaseModel], context_size: int = 0
    ) -> LlmResponse:
        """Async structured chat using Claude Agent SDK"""
        from claude_agent_sdk import query

        # Add schema instruction to the prompt
        schema_json = schema.model_json_schema()
        schema_instruction = (
            f"\n\nPlease respond with valid JSON matching this schema:\n{json.dumps(schema_json, indent=2)}"
        )

        prompt = self._normalize_conversation(conversation) + schema_instruction

        # Collect all messages from the async iterator
        messages = []
        try:
            async for message in query(prompt=prompt):
                messages.append(str(message))
        except Exception as e:
            raise DazLlmError(f"Claude Agent SDK structured chat error: {e}") from e

        # Combine and parse response
        response_text = "".join(messages)

        try:
            # Extract JSON from response
            start = response_text.find("{")
            end = response_text.rfind("}") + 1
            if start >= 0 and end > start:
                data = json.loads(response_text[start:end])
            else:
                data = json.loads(response_text)
            result = schema(**data)
            output = f"Claude CLI structured chat completed for model: {self.model}"
            return LlmResponse(value=result, output=output, provider=self.provider)
        except json.JSONDecodeError as exc:
            raise DazLlmError(f"Could not parse JSON response: {response_text}") from exc
        except Exception as e:
            raise DazLlmError(f"Could not create Pydantic model: {e}") from e

    async def async_image(self, prompt: str, file_name: str, width: int = 1024, height: int = 1024) -> str:
        """Image generation not supported by Claude CLI"""
        raise DazLlmError("Claude CLI does not support image generation")

    def get_context_length(self) -> int:
        """Get the context length for Claude CLI models"""
        # Claude CLI uses the same models as the API, so use same context lengths
        context_lengths = {
            "claude-3-5-sonnet-20241022": 200000,  # 200K tokens
            "claude-3-5-sonnet-20240620": 200000,  # 200K tokens
            "claude-3-5-haiku-20241022": 200000,  # 200K tokens
            "claude-3-opus-20240229": 200000,  # 200K tokens
            "claude-3-sonnet-20240229": 200000,  # 200K tokens
            "claude-3-haiku-20240307": 200000,  # 200K tokens
            "claude-2.1": 200000,  # 200K tokens
            "claude-2.0": 100000,  # 100K tokens
            "claude-instant-1.2": 100000,  # 100K tokens
        }

        return context_lengths.get(self.model, 200000)  # Default to 200K
