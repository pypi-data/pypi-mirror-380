"""
Gemini CLI implementation for dazllm
Uses the gemini command-line tool for LLM interactions
"""

import os
import subprocess
from typing import Optional

from .cli_base import CliProviderBase
from .core import ConfigurationError, Conversation


class LlmGeminiCli(CliProviderBase):
    """Gemini CLI implementation"""

    def __init__(self, model: str):
        super().__init__(model, "gemini")

    @staticmethod
    def default_model() -> str:
        """Default model for Gemini CLI"""
        return "gemini-2.0-flash-exp"

    @staticmethod
    def default_for_type(model_type: str) -> Optional[str]:
        """Get default model for a given type"""
        defaults = {
            "local_small": None,  # Gemini doesn't have local models
            "local_medium": None,
            "local_large": None,
            "paid_cheap": "gemini-1.5-flash",
            "paid_best": "gemini-2.0-flash-exp",
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
            "gemini-2.0-flash-exp",
            "gemini-1.5-pro",
            "gemini-1.5-flash",
            "gemini-1.5-flash-8b",
            "gemini-1.0-pro",
        ]

    @staticmethod
    def check_config():
        """Check if Gemini CLI is properly configured"""
        try:
            result = subprocess.run(["gemini", "--help"], capture_output=True, text=True)
            if result.returncode != 0:
                raise ConfigurationError(f"Gemini CLI not accessible: {result.stderr}")
        except FileNotFoundError:
            raise ConfigurationError("Gemini CLI not found. Please install gemini CLI tool.")
        except Exception as e:
            raise ConfigurationError(f"Gemini CLI error: {e}") from e

    def _normalize_conversation(self, conversation: Conversation) -> str:
        """Convert conversation to a prompt string for Gemini CLI"""
        if isinstance(conversation, str):
            return conversation

        # Convert message list to a formatted prompt
        prompt_parts = []
        for msg in conversation:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            if role == "system":
                # Gemini doesn't have explicit system messages, prepend as instruction
                prompt_parts.insert(0, f"Instructions: {content}")
            elif role == "assistant":
                prompt_parts.append(f"Assistant: {content}")
            else:
                prompt_parts.append(f"User: {content}")

        return "\n".join(prompt_parts)

    def _build_chat_command(self, prompt: str, force_json: bool = False) -> list[str]:
        """Build command for chat operation"""
        if force_json:
            prompt = f"{prompt}\n\nPlease respond with valid JSON only, no other text."

        # Use --yolo for headless operation
        # Note: --model parameter causes API errors, so we omit it and use default model
        return [self.executable, "--yolo", prompt]

    def _build_structured_command(self, prompt: str) -> list[str]:
        """Build command for structured chat operation"""
        return [self.executable, "--yolo", prompt]

    def _get_subprocess_kwargs(self) -> dict:
        """Get environment setup for Node.js paths"""
        env = os.environ.copy()
        env["GEMINI_DISABLE_SANDBOX"] = "true"

        # Ensure Node.js is in PATH for homebrew installations
        node_paths = [
            "/opt/homebrew/Cellar/node/24.5.0/bin",
            "/opt/homebrew/bin",
            "/usr/local/bin",
        ]
        for node_path in node_paths:
            if os.path.exists(node_path) and node_path not in env.get("PATH", ""):
                env["PATH"] = f"{node_path}:{env.get('PATH', '')}"

        return {"env": env, "input": ""}  # Provide empty input to avoid hanging

    def _is_acceptable_error(self, result: subprocess.CompletedProcess) -> bool:
        """Gemini CLI might return non-zero even for successful responses"""
        return result.stdout.strip() and not result.stderr

    def get_context_length(self) -> int:
        """Get the context length for Gemini CLI models"""
        # Gemini CLI uses the same models as the API, so use same context lengths
        context_lengths = {
            "gemini-2.0-flash-exp": 1000000,  # 1M tokens
            "gemini-2.0-flash": 1000000,  # 1M tokens
            "gemini-1.5-pro": 2000000,  # 2M tokens
            "gemini-1.5-flash": 1000000,  # 1M tokens
            "gemini-1.5-flash-8b": 1000000,  # 1M tokens
            "gemini-1.0-pro": 32768,  # 32K tokens
            "gemini-pro": 32768,  # 32K tokens
            "gemini-pro-vision": 32768,  # 32K tokens
        }

        return context_lengths.get(self.model, 32768)  # Default context

    def _is_acceptable_error_async(self, stdout: str, stderr: str) -> bool:
        """Gemini CLI might return non-zero even for successful responses"""
        return stdout.strip() and not stderr
