"""
Claude CLI implementation for dazllm
Uses the claude command-line tool for LLM interactions
"""

import subprocess
from typing import Optional

from .core import Conversation, ConfigurationError
from .cli_base import CliProviderBase


class LlmClaudeCli(CliProviderBase):
    """Claude CLI implementation"""

    def __init__(self, model: str):
        super().__init__(model, "claude")

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
    def capabilities() -> set[str]:
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
        """Check if Claude CLI is properly configured"""
        try:
            result = subprocess.run(
                ["claude", "--help"],
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                raise ConfigurationError(f"Claude CLI not accessible: {result.stderr}")
        except FileNotFoundError:
            raise ConfigurationError("Claude CLI not found. Please install claude CLI tool.")
        except Exception as e:
            raise ConfigurationError(f"Claude CLI error: {e}") from e

    def _normalize_conversation(self, conversation: Conversation) -> str:
        """Convert conversation to arguments for Claude CLI"""
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

    def _build_chat_command(self, prompt: str, force_json: bool = False) -> list[str]:
        """Build command for chat operation"""
        if force_json:
            prompt = f"{prompt}\n\nPlease respond with valid JSON only, no other text."

        return [
            self.executable,
            "--print",
            "--output-format", "text",
            "--dangerously-skip-permissions",  # For headless operation
            prompt
        ]

    def _build_structured_command(self, prompt: str) -> list[str]:
        """Build command for structured chat operation"""
        return [
            self.executable,
            "--print",
            "--output-format", "text",
            "--dangerously-skip-permissions",  # For headless operation
            prompt
        ]

    def get_context_length(self) -> int:
        """Get the context length for Claude CLI models"""
        # Claude CLI uses the same models as the API, so use same context lengths
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
