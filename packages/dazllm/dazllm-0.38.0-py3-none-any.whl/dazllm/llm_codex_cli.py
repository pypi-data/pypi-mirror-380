"""
Codex CLI implementation for dazllm
Uses the codex command-line tool for LLM interactions
"""

import subprocess
from typing import Optional

from .cli_base import CliProviderBase
from .core import ConfigurationError, Conversation


class LlmCodexCli(CliProviderBase):
    """Codex CLI implementation"""

    def __init__(self, model: str):
        super().__init__(model, "codex")

    @staticmethod
    def default_model() -> str:
        """Default model for Codex CLI"""
        return "default"

    @staticmethod
    def default_for_type(model_type: str) -> Optional[str]:
        """Get default model for a given type"""
        # Codex CLI doesn't expose model selection, so we use "default"
        defaults = {
            "local_small": "default",
            "local_medium": "default",
            "local_large": "default",
            "paid_cheap": "default",
            "paid_best": "default",
        }
        return defaults.get(model_type)

    @staticmethod
    def capabilities() -> set[str]:
        """Return set of capabilities this provider supports"""
        return {"chat", "structured"}

    @staticmethod
    def supported_models() -> list[str]:
        """Return list of models this provider supports"""
        # Codex CLI doesn't expose available models
        return ["default"]

    @staticmethod
    def check_config():
        """Check if Codex CLI is properly configured"""
        try:
            result = subprocess.run(["codex", "--version"], capture_output=True, text=True)
            if result.returncode != 0:
                raise ConfigurationError(f"Codex CLI not accessible: {result.stderr}")
        except FileNotFoundError:
            raise ConfigurationError("Codex CLI not found. Please install codex CLI tool.")
        except Exception as e:
            raise ConfigurationError(f"Codex CLI error: {e}") from e

    def _get_help_flag(self) -> str:
        """Codex uses --version instead of --help"""
        return "--version"

    def _get_timeout_seconds(self) -> None:
        """No timeout for Codex CLI calls"""
        return None

    def _normalize_conversation(self, conversation: Conversation) -> str:
        """Convert conversation to a single prompt string for CLI"""
        if isinstance(conversation, str):
            return conversation

        # Convert message list to a formatted prompt
        prompt_parts = []
        for msg in conversation:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            if role == "system":
                prompt_parts.append(f"System: {content}")
            elif role == "assistant":
                prompt_parts.append(f"Assistant: {content}")
            else:
                prompt_parts.append(f"User: {content}")

        return "\n".join(prompt_parts)

    def _build_chat_command(self, prompt: str, force_json: bool = False) -> list[str]:
        """Build command for chat operation"""
        if force_json:
            prompt = f"{prompt}\n\nPlease respond with valid JSON only, no other text."
        return [self.executable, "exec", prompt]

    def _build_structured_command(self, prompt: str) -> list[str]:
        """Build command for structured chat operation"""
        return [self.executable, "exec", prompt]

    def get_context_length(self) -> int:
        """Get the context length for Codex CLI models"""
        # Codex CLI uses various underlying models, default to a reasonable size
        return 8192  # Conservative default
