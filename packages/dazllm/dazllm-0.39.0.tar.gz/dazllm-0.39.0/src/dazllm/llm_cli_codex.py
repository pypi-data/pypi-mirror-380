"""
Codex CLI Provider with logging capabilities

Extends the original LlmCodexCli to implement the new LlmCli interface
with comprehensive logging capture.
"""

import asyncio
from typing import List, Optional, Set, Type

from pydantic import BaseModel

from .core import ConfigurationError, Conversation, Llm, LlmResponse
from .llm_codex_cli import LlmCodexCli as OriginalLlmCodexCli
from .memoization import memoize_llm_response_async


class LlmCodexCli(Llm):
    """Codex CLI provider with enhanced logging"""

    def __init__(self, model: str = "codex:default"):
        super().__init__(model)
        self._model = model
        self._original = None  # Lazy load

    def _get_original(self):
        """Lazy load the original CLI instance"""
        if self._original is None:
            # Must have real CLI - fail if not available
            try:
                OriginalLlmCodexCli.check_config()
                self._original = OriginalLlmCodexCli(self._model)
            except ConfigurationError as e:
                raise ConfigurationError(f"Codex CLI not available: {e}") from e
        return self._original

    def chat(self, conversation: Conversation, force_json: bool = False) -> LlmResponse:
        """Sync wrapper that blocks on async implementation"""
        import asyncio

        return asyncio.run(self.chat_async(conversation, force_json))

    def chat_structured(
        self, conversation: Conversation, schema: Type[BaseModel], context_size: int = 0
    ) -> LlmResponse:
        """Sync wrapper that blocks on async implementation"""
        import asyncio

        return asyncio.run(self.chat_structured_async(conversation, schema, context_size))

    @staticmethod
    def is_available() -> bool:
        """Check if Codex CLI is available"""
        try:
            OriginalLlmCodexCli.check_config()
            # Also check if we can actually instantiate and use it
            codex = LlmCodexCli("codex:default")
            # Try a simple test to ensure it's working
            codex.chat("test")
            return True
        except (ConfigurationError, Exception):
            return False

    @memoize_llm_response_async
    async def chat_async(self, conversation: Conversation, force_json: bool = False) -> LlmResponse:
        """Async chat with Codex CLI using async subprocess"""
        prompt = self._get_original()._normalize_conversation(conversation)

        if force_json:
            prompt = f"{prompt}\n\nPlease respond with valid JSON only, no other text."

        # Execute with async subprocess
        cmd = [self._get_original().executable, "exec", prompt]

        try:
            process = await asyncio.create_subprocess_exec(
                *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )

            stdout_bytes, stderr_bytes = await process.communicate()
            stdout = stdout_bytes.decode("utf-8") if stdout_bytes else ""
            stderr = stderr_bytes.decode("utf-8") if stderr_bytes else ""

            # Create execution log
            execution_log = []
            execution_log.append("Codex CLI Async Execution Log")
            execution_log.append(f"Command: {' '.join(cmd)}")
            execution_log.append(f"Return code: {process.returncode}")

            if stderr:
                execution_log.append(f"Stderr: {stderr}")

            execution_log.append(f"Raw stdout length: {len(stdout)}")

            if process.returncode != 0:
                execution_log.append(f"Error: Command failed with return code {process.returncode}")
                raise Exception(f"Codex CLI error: {stderr}")

            response = stdout.strip()

            if force_json:
                response = self._get_original()._extract_json_string(response)

            execution_log.append(f"Final response length: {len(response)}")
            execution_log.append(f"Response preview: {response[:100]}...")

            log_output = "\n".join(execution_log)
            return LlmResponse(value=response, output=log_output, provider=self.model)

        except Exception as e:
            error_msg = f"Codex CLI execution error: {e}"
            log_output = f"Codex CLI Async Execution Log\nCommand: {' '.join(cmd)}\nError: {error_msg}"
            raise Exception(f"{error_msg}\n\nLog:\n{log_output}")

    @memoize_llm_response_async
    async def chat_structured_async(
        self, conversation: Conversation, schema: Type[BaseModel], context_size: int = 0
    ) -> LlmResponse:
        """Async structured chat with execution logs"""
        import json

        execution_log = []
        execution_log.append("=== Codex CLI Async Structured Output ===")
        execution_log.append(f"Schema: {schema.__name__}")
        execution_log.append(f"Schema fields: {list(schema.model_fields.keys())}")

        try:
            # Build the structured prompt
            schema_json = schema.model_json_schema()
            schema_str = json.dumps(schema_json, indent=2)

            prompt = self._get_original()._normalize_conversation(conversation)
            structured_prompt = (
                f"{prompt}\n\n"
                f"IMPORTANT: You must provide a JSON response that exactly matches this schema:\n"
                f"{schema_str}\n\n"
                f"CRITICAL INSTRUCTIONS:\n"
                f"1. Start your response with any explanations, logs, or working notes\n"
                f"2. Then add the marker: === RESULT JSON START ===\n"
                f"3. Provide ONLY the valid JSON matching the schema\n"
                f"4. End with the marker: === RESULT JSON END ===\n"
                f"5. Everything between the markers must be valid JSON with no other text\n\n"
                f"Example format:\n"
                f"[Your working notes and explanations here]\n"
                f"=== RESULT JSON START ===\n"
                f'{{"field": "value"}}\n'
                f"=== RESULT JSON END ==="
            )

            execution_log.append("\n=== Schema Definition ===")
            if len(schema_str) > 200:
                execution_log.append(f"Schema JSON: {schema_str[:200]}...")
            else:
                execution_log.append(f"Schema JSON: {schema_str}")

            # Use async chat method
            # Conversation is a type alias, not a constructor - just use the list directly
            conv = [{"role": "user", "content": structured_prompt}]
            chat_result = await self.chat_async(conv, force_json=False)
            execution_log.append("\n=== Console Output ===")
            execution_log.append(chat_result.output)

            # Extract JSON from response
            response_text = chat_result.value
            execution_log.append("\n=== Processing Response ===")

            # Try to extract JSON with markers first
            parsed_json = None
            start_marker = "=== RESULT JSON START ==="
            end_marker = "=== RESULT JSON END ==="

            if start_marker in response_text and end_marker in response_text:
                # Use rfind to get the LAST occurrence (in case the prompt included examples)
                start_idx = response_text.rfind(start_marker) + len(start_marker)
                end_idx = response_text.rfind(end_marker, start_idx)  # Find end marker after start
                json_str = response_text[start_idx:end_idx].strip()
                execution_log.append("Found JSON between markers")
                if len(json_str) > 200:
                    execution_log.append(f"Extracted JSON: {json_str[:200]}...")
                else:
                    execution_log.append(f"Extracted JSON: {json_str}")

                try:
                    parsed_json = json.loads(json_str)
                except json.JSONDecodeError as e:
                    execution_log.append(f"Failed to parse marked JSON: {e}")

            # If no markers or parse failed, fall back to extraction
            if parsed_json is None:
                execution_log.append("Falling back to JSON extraction")
                parsed_json = self._get_original()._extract_json(response_text)

            # Validate against schema
            from jsonschema import validate

            validate(instance=parsed_json, schema=schema_json)

            # Create instance from schema
            # Schema should be a Pydantic model class
            result = schema(**parsed_json)

            execution_log.append("\n=== Validation: PASSED ===")
            execution_log.append(f"Result: {result.model_dump()}")

            log_output = "\n".join(execution_log)
            return LlmResponse(value=result, output=log_output, provider=self.model)

        except Exception as e:
            execution_log.append("\n=== ERROR ===")
            execution_log.append(str(e))
            log_output = "\n".join(execution_log)
            raise Exception(f"Codex CLI async structured execution error: {e}\n\nLog:\n{log_output}")

    async def async_image(self, prompt: str, file_name: str, width: int = 1024, height: int = 1024) -> str:
        """Codex doesn't support image generation"""
        raise NotImplementedError("Codex CLI doesn't support image generation")

    def get_context_length(self) -> int:
        """Get context length from original implementation"""
        return 8192  # Default context length for Codex

    @staticmethod
    def capabilities() -> Set[str]:
        """Return capabilities of Codex CLI"""
        return OriginalLlmCodexCli.capabilities()

    @staticmethod
    def supported_models() -> List[str]:
        """Return supported models"""
        return OriginalLlmCodexCli.supported_models()

    @staticmethod
    def default_model() -> str:
        """Return default model"""
        return OriginalLlmCodexCli.default_model()

    @staticmethod
    def default_for_type(model_type: str) -> Optional[str]:
        """Return default model for type"""
        return OriginalLlmCodexCli.default_for_type(model_type)

    @staticmethod
    def check_config():
        """Check configuration"""
        return OriginalLlmCodexCli.check_config()
