"""
Base class for CLI providers to eliminate duplication
Provides common functionality for subprocess execution, JSON extraction, and error handling
"""

import asyncio
import json
import re
import subprocess
from typing import Dict, Optional, Type

from jsonschema import ValidationError, validate
from pydantic import BaseModel

from .core import ConfigurationError, Conversation, DazLlmError, Llm, LlmResponse


class CliProviderBase(Llm):
    """Base class for CLI providers that eliminates common code duplication"""

    def __init__(self, model: str, executable_name: str):
        super().__init__(model)
        self.executable_name = executable_name
        self.executable = self._find_executable()
        self._check_executable()

    def _find_executable(self) -> str:
        """Find the CLI executable"""
        import shutil

        executable = shutil.which(self.executable_name)
        if not executable:
            raise ConfigurationError(f"{self.executable_name} CLI not found in PATH")
        return executable

    def _check_executable(self):
        """Ensure the executable is available and working"""
        try:
            result = subprocess.run([self.executable, self._get_help_flag()], capture_output=True, text=True)
            if result.returncode != 0:
                raise ConfigurationError(f"{self.executable_name} CLI check failed: {result.stderr}")
        except Exception as e:
            raise ConfigurationError(f"Cannot run {self.executable_name} CLI: {e}") from e

    def _get_help_flag(self) -> str:
        """Get the help flag for this CLI tool"""
        return "--help"

    def _get_timeout_seconds(self) -> None:
        """Get timeout in seconds for CLI calls - None means unlimited"""
        return None

    def _extract_json_with_markers(self, text: str) -> Optional[dict]:
        """Extract JSON between specific markers"""
        start_marker = "=== RESULT JSON START ==="
        end_marker = "=== RESULT JSON END ==="

        if start_marker in text and end_marker in text:
            start_idx = text.find(start_marker) + len(start_marker)
            end_idx = text.find(end_marker)
            json_str = text[start_idx:end_idx].strip()

            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                pass

        return None

    def _extract_json(self, text: str) -> dict:
        """Extract JSON from text with multiple strategies"""
        # Strategy 1: Look for markdown code blocks
        if "```json" in text:
            match = re.search(r"```json\s*(.*?)\s*```", text, re.DOTALL)
            if match:
                try:
                    return json.loads(match.group(1))
                except json.JSONDecodeError:
                    pass

        # Strategy 2: Look for any code blocks
        if "```" in text:
            match = re.search(r"```\s*(.*?)\s*```", text, re.DOTALL)
            if match:
                try:
                    return json.loads(match.group(1))
                except json.JSONDecodeError:
                    pass

        # Strategy 3: Try to parse the entire text
        try:
            return json.loads(text.strip())
        except json.JSONDecodeError:
            pass

        # Strategy 4: Look for JSON-like structures
        json_patterns = [
            r"\{[^{}]*\}",  # Simple JSON object
            r"\{.*?\}(?=\s*$|\s*\n)",  # JSON object at end of line
            r"\{.*\}",  # Any JSON object
            r"\[.*\]",  # JSON array
        ]

        for pattern in json_patterns:
            matches = re.findall(pattern, text, re.DOTALL | re.MULTILINE)
            for match in matches:
                try:
                    parsed = json.loads(match)
                    if isinstance(parsed, dict):
                        return parsed
                except json.JSONDecodeError:
                    continue

        # Strategy 5: Clean common prefixes and try again
        cleaned = text.strip()
        prefixes = [
            "Here is the JSON:",
            "JSON:",
            "Output:",
            "Result:",
            "Response:",
            "Here's the JSON:",
        ]
        for prefix in prefixes:
            if cleaned.startswith(prefix):
                cleaned = cleaned[len(prefix) :].strip()
                break

        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            raise ValueError(f"Could not extract valid JSON from response: {text[:200]}...")

    def _extract_json_string(self, text: str) -> str:
        """Extract JSON string from text (for force_json mode)"""
        try:
            parsed = self._extract_json(text)
            return json.dumps(parsed)
        except (json.JSONDecodeError, ValueError):
            return text  # Return original if can't parse

    def _build_structured_prompt(self, conversation: Conversation, schema: Type[BaseModel]) -> str:
        """Build structured prompt with schema instructions"""
        schema_json = schema.model_json_schema()
        schema_str = json.dumps(schema_json, indent=2)

        prompt = self._normalize_conversation(conversation)
        return (
            f"{prompt}\n\n"
            f"IMPORTANT: You must provide a JSON response that exactly matches this schema:\n"
            f"{schema_str}\n\n"
            f"CRITICAL INSTRUCTIONS:\n"
            f"1. If the user has specified exact JSON values to return, use those values\n"
            f"2. Otherwise, generate appropriate values based on the user's request\n"
            f"3. Start your response with any explanations, logs, or working notes (optional)\n"
            f"4. Then add the marker: === RESULT JSON START ===\n"
            f"5. Provide ONLY the valid JSON matching the schema\n"
            f"6. End with the marker: === RESULT JSON END ===\n"
            f"7. Everything between the markers must be valid JSON with no other text\n\n"
            f"Example format:\n"
            f"[Your working notes and explanations here - optional]\n"
            f"=== RESULT JSON START ===\n"
            '{"field": "value"}\n'
            f"=== RESULT JSON END ==="
        )

    async def _async_subprocess_call(self, cmd: list[str], input_text: str = "") -> tuple[str, str, int]:
        """Execute subprocess call asynchronously"""
        try:
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                stdin=asyncio.subprocess.PIPE if input_text else None,
            )

            stdout_bytes, stderr_bytes = await process.communicate(
                input=input_text.encode("utf-8") if input_text else None
            )

            stdout = stdout_bytes.decode("utf-8") if stdout_bytes else ""
            stderr = stderr_bytes.decode("utf-8") if stderr_bytes else ""

            return stdout, stderr, process.returncode

        except Exception as e:
            raise DazLlmError(f"{self.executable_name} CLI async execution error: {e}") from e

    def chat_structured(
        self, conversation: Conversation, schema: Type[BaseModel], context_size: int = 0
    ) -> LlmResponse:
        """Chat with structured output using common retry logic"""
        structured_prompt = self._build_structured_prompt(conversation, schema)
        schema_json = schema.model_json_schema()

        attempts = 10
        last_error = None
        current_prompt = structured_prompt
        execution_log = []

        while attempts > 0:
            try:
                cmd = self._build_structured_command(current_prompt)

                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=self._get_timeout_seconds(),
                    **self._get_subprocess_kwargs(),
                )

                if result.returncode != 0 and not self._is_acceptable_error(result):
                    raise DazLlmError(f"{self.executable_name} CLI error: {result.stderr}")

                response = result.stdout.strip()
                if not response:
                    raise DazLlmError(f"Empty response from {self.executable_name} CLI")

                execution_log.append(f"=== {self.executable_name} CLI Structured Output ===")
                execution_log.append(f"Schema: {schema.__name__}")
                execution_log.append(f"Response length: {len(response)}")

                # Try to extract JSON with markers first
                parsed_json = self._extract_json_with_markers(response)
                if parsed_json is None:
                    parsed_json = self._extract_json(response)

                # Validate against schema
                validate(instance=parsed_json, schema=schema_json)
                result_obj = schema(**parsed_json)

                execution_log.append("Validation: PASSED")
                log_output = "\n".join(execution_log)
                return LlmResponse(value=result_obj, output=log_output, provider=self.executable_name)

            except (json.JSONDecodeError, ValueError) as e:
                last_error = e
                current_prompt = self._build_retry_prompt(structured_prompt, f"not valid JSON. Error: {e}")
            except ValidationError as e:
                last_error = e
                current_prompt = self._build_retry_prompt(structured_prompt, f"JSON didn't match schema. Error: {e}")
            except Exception as e:
                raise DazLlmError(f"{self.executable_name} CLI execution error: {e}") from e

            attempts -= 1

        raise DazLlmError(f"Failed to get valid structured response after multiple attempts. Last error: {last_error}")

    def _build_retry_prompt(self, original_prompt: str, error_msg: str) -> str:
        """Build retry prompt with error feedback"""
        return (
            f"{original_prompt}\n\n"
            f"PREVIOUS ATTEMPT FAILED:\n"
            f"The response was {error_msg}\n"
            f"Please provide valid JSON between the markers matching the schema exactly."
        )

    def _is_acceptable_error(self, result: subprocess.CompletedProcess) -> bool:
        """Check if subprocess error is acceptable (e.g., has output despite non-zero return)"""
        return result.stdout.strip() and not result.stderr

    def _get_subprocess_kwargs(self) -> Dict:
        """Get additional kwargs for subprocess calls"""
        return {}

    def chat(self, conversation: Conversation, force_json: bool = False) -> str:
        """Chat using CLI with common implementation"""
        prompt = self._normalize_conversation(conversation)
        cmd = self._build_chat_command(prompt, force_json)

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=self._get_timeout_seconds(),
                **self._get_subprocess_kwargs(),
            )

            if result.returncode != 0 and not self._is_acceptable_error(result):
                raise DazLlmError(f"{self.executable_name} CLI error: {result.stderr}")

            response = result.stdout.strip()

            if force_json:
                response = self._extract_json_string(response)

            return response

        except Exception as e:
            raise DazLlmError(f"{self.executable_name} CLI execution error: {e}") from e

    async def chat_async(self, conversation: Conversation, force_json: bool = False) -> LlmResponse:
        """Async chat using proper subprocess"""
        prompt = self._normalize_conversation(conversation)
        cmd = self._build_chat_command(prompt, force_json)

        stdout, stderr, returncode = await self._async_subprocess_call(cmd)

        if returncode != 0 and not self._is_acceptable_error_async(stdout, stderr):
            raise DazLlmError(f"{self.executable_name} CLI error: {stderr}")

        response = stdout.strip()
        if force_json:
            response = self._extract_json_string(response)

        return LlmResponse(
            value=response,
            output=f"{self.executable_name} CLI async execution completed",
            provider=self.model,
        )

    async def chat_structured_async(self, conversation: Conversation, schema, context_size: int = 0) -> LlmResponse:
        """Async structured chat using proper subprocess"""
        structured_prompt = self._build_structured_prompt(conversation, schema)
        cmd = self._build_structured_command(structured_prompt)

        stdout, stderr, returncode = await self._async_subprocess_call(cmd)

        if returncode != 0 and not self._is_acceptable_error_async(stdout, stderr):
            raise DazLlmError(f"{self.executable_name} CLI structured error: {stderr}")

        response_text = stdout.strip()

        # Extract and validate JSON
        parsed_json = self._extract_json(response_text)
        from jsonschema import validate

        schema_json = schema.model_json_schema()
        validate(instance=parsed_json, schema=schema_json)
        result = schema(**parsed_json)

        return LlmResponse(
            value=result,
            output=f"{self.executable_name} CLI async structured execution completed",
            provider=self.model,
        )

    def _is_acceptable_error_async(self, stdout: str, stderr: str) -> bool:
        """Check if async subprocess error is acceptable"""
        return stdout.strip() and not stderr

    # Abstract methods that subclasses must implement
    def _normalize_conversation(self, conversation: Conversation) -> str:
        """Convert conversation to CLI-specific format"""
        raise NotImplementedError

    def _build_chat_command(self, prompt: str, force_json: bool = False) -> list[str]:
        """Build command for chat operation"""
        raise NotImplementedError

    def _build_structured_command(self, prompt: str) -> list[str]:
        """Build command for structured chat operation"""
        raise NotImplementedError

    def image(self, prompt: str, file_name: str, width: int = 1024, height: int = 1024) -> str:
        """Generate image (not supported by CLI providers)"""
        raise DazLlmError(f"Image generation not supported by {self.executable_name} CLI")

    async def async_image(self, prompt: str, file_name: str, width: int = 1024, height: int = 1024) -> str:
        """Async image generation (not supported by CLI providers)"""
        raise DazLlmError(f"Image generation not supported by {self.executable_name} CLI")
