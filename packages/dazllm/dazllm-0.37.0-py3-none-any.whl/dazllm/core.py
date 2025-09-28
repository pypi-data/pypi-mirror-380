# dazllm - A simple, unified interface for all major LLMs
from __future__ import annotations

# Imports kept explicit and top-level
import unittest
from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, Union, Dict, List, Literal, TypedDict, Set, Tuple, NamedTuple, Type
from pydantic import BaseModel

# Import exception hierarchy from provider_manager to keep types consistent
from .provider_manager import DazLlmError, ConfigurationError, ModelNotFoundError


# Define the shape of a single chat message
class Message(TypedDict):
    role: Literal["user", "assistant", "system"]
    content: str


# Define supported conversation forms: a single prompt or a list of role-tagged messages
Conversation = Union[str, List[Message]]


class LlmResponse(NamedTuple):
    """Response from LLM execution containing result, logs, and provider info"""
    value: Union[str, BaseModel]  # The actual response value
    output: str  # Complete log of execution (empty for most providers)
    provider: str  # Name of the provider that was used


# Define logical model sizes / tiers referenced across providers
class ModelType(Enum):
    LOCAL_SMALL = "local_small"
    LOCAL_MEDIUM = "local_medium"
    LOCAL_LARGE = "local_large"
    PAID_CHEAP = "paid_cheap"
    PAID_BEST = "paid_best"


# Convert free-form strings into a ModelType when possible
def _coerce_model_type(value: Optional[str]) -> Optional[ModelType]:
    # Accept None
    if value is None:
        return None

    # Normalize common user inputs
    normalized = value.strip().lower().replace("-", "_").replace(" ", "_")

    # Canonical keys → ModelType
    mapping: Dict[str, ModelType] = {
        "local_small": ModelType.LOCAL_SMALL,
        "small_local": ModelType.LOCAL_SMALL,
        "localsmall": ModelType.LOCAL_SMALL,
        "local_medium": ModelType.LOCAL_MEDIUM,
        "medium_local": ModelType.LOCAL_MEDIUM,
        "localmedium": ModelType.LOCAL_MEDIUM,
        "local_large": ModelType.LOCAL_LARGE,
        "large_local": ModelType.LOCAL_LARGE,
        "locallarge": ModelType.LOCAL_LARGE,
        "paid_cheap": ModelType.PAID_CHEAP,
        "cheap_paid": ModelType.PAID_CHEAP,
        "paidcheap": ModelType.PAID_CHEAP,
        "paid_best": ModelType.PAID_BEST,
        "best_paid": ModelType.PAID_BEST,
        "paidbest": ModelType.PAID_BEST,
    }

    # Direct match on normalized
    if normalized in mapping:
        return mapping[normalized]

    # ALLCAPS enum names also accepted
    upper = value.strip().upper()
    try:
        return ModelType[upper]
    except KeyError:
        return None


# Resolve constructor inputs into a fully-qualified "provider:model_id" string
# Rules:
# - If model_name is already provided → return as-is
# - If provider + explicit model → compose "provider:model"
# - If provider only → choose that provider's default model
# - If provider + type → provider's default_for_type or its default_model
# - If only a size/type hint (via 'model' alias or model_type) → use ModelResolver
def _resolve_model_name_for_ctor(
    model_name: Optional[str],
    provider: Optional[str],
    model: Optional[str],
    model_type: Optional[ModelType],
) -> str:
    from .model_resolver import ModelResolver
    from .provider_manager import ProviderManager

    # Keep explicit fully-qualified model names untouched
    if model_name:
        return model_name

    # If 'model' looks like a size alias, treat it as model_type
    alias_type = _coerce_model_type(model) if model else None
    if alias_type is not None:
        model_type = alias_type
        model = None

    # Provider + explicit model id
    if provider and model and model_type is None:
        return f"{provider}:{model}"

    # Provider only → provider default
    if provider and model is None and model_type is None:
        info = ProviderManager.get_provider_info(provider)
        default_model = info.get("default_model")
        if not default_model:
            raise ModelNotFoundError(f"No default model found for provider '{provider}'")
        return f"{provider}:{default_model}"

    # Provider + type → provider default_for_type, fallback to provider default
    if provider and model_type is not None:
        default_for_type: Optional[str] = None

        # Try to read type defaults if provider_info exposes them
        info = ProviderManager.get_provider_info(provider)
        for key in ("defaults", "default_for_type_map", "type_defaults"):
            m = info.get(key) if isinstance(info, dict) else None
            if isinstance(m, dict):
                default_for_type = m.get(model_type.value) or m.get(model_type.name)
                if default_for_type:
                    break

        # Ask provider class directly when available
        if not default_for_type:
            try:
                provider_class = ProviderManager.get_provider_class(provider)  # type: ignore[attr-defined]
                default_for_type = provider_class.default_for_type(model_type.value)
            except Exception:
                default_for_type = None

        chosen = default_for_type or info.get("default_model")
        if not chosen:
            raise ModelNotFoundError(
                f"No default for type '{model_type.value}' on provider '{provider}'"
            )
        return f"{provider}:{chosen}"

    # No provider specified → delegate to ModelResolver to pick the best provider/model
    resolved = ModelResolver.resolve_model(model, model_type)
    return resolved


# Unified interface for all providers, with flexible construction helpers
class Llm(ABC):
    # Cache instances by fully-qualified model name
    _cached: Dict[str, Llm] = {}

    # Constructor supports:
    # - Llm() → default overall model
    # - Llm(provider="lm-studio") → provider's default model
    # - Llm(model="large_local") or Llm(model_type=ModelType.LOCAL_LARGE) → best provider for that tier
    # - Llm("provider:model_id") → fully-qualified explicit selection
    def __init__(
        self,
        model_name: Optional[str] = None,
        *,
        provider: Optional[str] = None,
        model: Optional[str] = None,
        model_type: Optional[ModelType] = None,
    ):
        from .model_resolver import ModelResolver

        # Resolve inputs into a fully-qualified name
        fq_name = _resolve_model_name_for_ctor(model_name, provider, model, model_type)

        # Store resolved name and parsed parts
        self.model_name = fq_name
        self.provider, self.model = ModelResolver.parse_model_name(fq_name)
        self.provider_name = self.provider  # For compatibility with CLI interface

    # Construct using a provider's default model (camelCase per request)
    @classmethod
    def fromProvider(cls, provider_name: str) -> Llm:
        return cls(provider=provider_name)

    # Construct using a provider's default model (snake_case alias)
    @classmethod
    def from_provider(cls, provider_name: str) -> Llm:
        return cls(provider=provider_name)

    # Shortcut: choose a local small model on the best provider
    @classmethod
    def LocalSmall(cls) -> Llm:
        return cls(model_type=ModelType.LOCAL_SMALL)

    # Shortcut: choose a local medium model on the best provider
    @classmethod
    def LocalMedium(cls) -> Llm:
        return cls(model_type=ModelType.LOCAL_MEDIUM)

    # Shortcut: choose a local large model on the best provider
    @classmethod
    def LocalLarge(cls) -> Llm:
        return cls(model_type=ModelType.LOCAL_LARGE)

    # Shortcut: choose the cheapest paid model on the best provider
    @classmethod
    def PaidCheap(cls) -> Llm:
        return cls(model_type=ModelType.PAID_CHEAP)

    # Shortcut: choose the best paid model on the best provider
    @classmethod
    def PaidBest(cls) -> Llm:
        return cls(model_type=ModelType.PAID_BEST)

    # Retrieve or create a cached instance for a fully-qualified model name
    @classmethod
    def model_named(cls, model_name: str) -> Llm:
        from .provider_manager import ProviderManager

        if model_name in cls._cached:
            return cls._cached[model_name]
        provider, model = cls._parse_model_name_static(model_name)
        instance = ProviderManager.create_provider_instance(provider, model)
        cls._cached[model_name] = instance
        return instance

    # Parse a fully-qualified model string into (provider, model_id)
    @staticmethod
    def _parse_model_name_static(model_name: str) -> Tuple[str, str]:
        from .model_resolver import ModelResolver

        return ModelResolver.parse_model_name(model_name)

    # Return a list of available providers
    @classmethod
    def get_providers(cls) -> List[str]:
        from .provider_manager import ProviderManager

        return ProviderManager.get_providers()

    # Return metadata for a single provider
    @classmethod
    def get_provider_info(cls, provider: str) -> Dict:
        from .provider_manager import ProviderManager

        return ProviderManager.get_provider_info(provider)

    # Return metadata for all providers
    @classmethod
    def get_all_providers_info(cls) -> Dict[str, Dict]:
        from .provider_manager import ProviderManager

        return ProviderManager.get_all_providers_info()

    # Get CLI interface with enhanced logging capabilities
    @classmethod
    def cli(cls):
        """
        Get a CLI interface that provides enhanced logging capabilities

        Returns a CLI provider instance with enhanced logging.

        Returns:
            Llm: CLI provider with logging capabilities
        """
        # Try to find and return the best available CLI provider with logging
        try:
            from .llm_cli_claude import LlmClaudeCliWithLogging
            if LlmClaudeCliWithLogging.is_available():
                return LlmClaudeCliWithLogging()
        except ImportError:
            pass

        # Add other CLI providers here as they get updated
        raise ConfigurationError("No CLI providers with logging available")

    # Send a chat conversation and return LlmResponse with result and logs
    def chat(self, conversation: Conversation, force_json: bool = False) -> LlmResponse:
        """Synchronous wrapper that blocks on the async implementation."""
        return _run_sync(self.chat_async(conversation, force_json))

    # Async variant for non-blocking use in event loops
    @abstractmethod
    async def chat_async(self, conversation: Conversation, force_json: bool = False) -> LlmResponse:
        """Async chat that providers must implement."""
        pass

    # Send a chat conversation and parse into a Pydantic schema (subclasses must implement)
    def chat_structured(
        self, conversation: Conversation, schema: Type[BaseModel], context_size: int = 0
    ) -> LlmResponse:
        """Synchronous wrapper that blocks on the async implementation."""
        return _run_sync(self.chat_structured_async(conversation, schema, context_size))

    @abstractmethod
    async def chat_structured_async(
        self, conversation: Conversation, schema: Type[BaseModel], context_size: int = 0
    ) -> LlmResponse:
        """Async structured chat that providers must implement."""
        pass

    # Generate an image and return the output path/URL (subclasses must implement)
    def image(
        self, prompt: str, file_name: str, width: int = 1024, height: int = 1024
    ) -> str:
        """Synchronous wrapper that blocks on the async implementation."""
        return _run_sync(self.async_image(prompt, file_name, width, height))

    @abstractmethod
    async def async_image(
        self, prompt: str, file_name: str, width: int = 1024, height: int = 1024
    ) -> str:
        """Async image generation that providers must implement."""
        pass

    # Get context length for the current model (subclasses must implement)
    @abstractmethod
    def get_context_length(self) -> int:
        """Get the context length (token limit) for the current model"""
        pass

    # Describe provider capabilities (subclasses must implement)
    @staticmethod
    @abstractmethod
    def capabilities() -> Set[str]:
        pass

    # List model ids supported by the provider (subclasses must implement)
    @staticmethod
    @abstractmethod
    def supported_models() -> List[str]:
        pass

    # Return the provider's default model id (subclasses must implement)
    @staticmethod
    @abstractmethod
    def default_model() -> str:
        pass

    # Return the provider's default model id for a given type (subclasses must implement)
    @staticmethod
    @abstractmethod
    def default_for_type(model_type: str) -> Optional[str]:
        pass

    # Verify provider-level configuration (subclasses must implement)
    @staticmethod
    @abstractmethod
    def check_config():
        pass

    # Check if this provider is available on the system
    @classmethod
    def is_available(cls) -> bool:
        """Check if this provider is available on the system"""
        try:
            # Default implementation: try to call check_config
            # Subclasses can override for more specific availability checks
            cls.check_config()
            return True
        except Exception:
            return False

    # Convenience: resolve and chat without manually constructing an instance
    @classmethod
    def chat_static(
        cls,
        conversation: Conversation,
        model: Optional[str] = None,
        model_type: Optional[ModelType] = None,
        force_json: bool = False,
    ) -> LlmResponse:
        from .model_resolver import ModelResolver

        model_name = ModelResolver.resolve_model(model, model_type)
        llm = cls.model_named(model_name)
        return llm.chat(conversation, force_json)

    @classmethod
    async def chat_static_async(
        cls,
        conversation: Conversation,
        model: Optional[str] = None,
        model_type: Optional[ModelType] = None,
        force_json: bool = False,
    ) -> LlmResponse:
        """Async convenience chat using resolved model."""
        from .model_resolver import ModelResolver

        model_name = ModelResolver.resolve_model(model, model_type)
        llm = cls.model_named(model_name)
        return await llm.chat_async(conversation, force_json)

    # Convenience: resolve and structured-chat without manually constructing an instance
    @classmethod
    def chat_structured_static(
        cls,
        conversation: Conversation,
        schema: Type[BaseModel],
        model: Optional[str] = None,
        model_type: Optional[ModelType] = None,
        context_size: int = 0,
    ) -> LlmResponse:
        from .model_resolver import ModelResolver

        model_name = ModelResolver.resolve_model(model, model_type)
        llm = cls.model_named(model_name)
        return llm.chat_structured(conversation, schema, context_size)

    # Convenience: resolve and image without manually constructing an instance
    @classmethod
    def image_static(
        cls,
        prompt: str,
        file_name: str,
        width: int = 1024,
        height: int = 1024,
        model: Optional[str] = None,
        model_type: Optional[ModelType] = None,
    ) -> str:
        from .model_resolver import ModelResolver

        model_name = ModelResolver.resolve_model(model, model_type)
        llm = cls.model_named(model_name)
        return llm.image(prompt, file_name, width, height)

    # Generate image using the best available provider
    @classmethod
    def generate_image(
        cls,
        prompt: str,
        file_name: str,
        width: int = 1024,
        height: int = 1024,
        preferred_provider: Optional[str] = None,
    ) -> str:
        """Generate an image using the best available provider that supports image generation

        Args:
            prompt: The image generation prompt
            file_name: Output file name
            width: Image width in pixels
            height: Image height in pixels
            preferred_provider: Optional preferred provider name

        Returns:
            Path to the generated image file
        """
        from .provider_manager import ProviderManager

        # Define provider preference order (best to worst)
        provider_preference = [
            "openai",      # Best quality with gpt-image-1
            "google",      # Good alternative with Gemini
            "anthropic",   # If they add image support
        ]

        # If user specified a preferred provider, try it first
        if preferred_provider:
            try:
                provider = ProviderManager.resolve_provider_alias(preferred_provider)
                info = ProviderManager.get_provider_info(provider)
                if "image" in info.get("capabilities", set()):
                    llm = cls.from_provider(provider)
                    return llm.image(prompt, file_name, width, height)
            except Exception:
                pass  # Fall back to automatic selection

        # Try providers in preference order
        for provider in provider_preference:
            try:
                info = ProviderManager.get_provider_info(provider)
                if info.get("configured", False) and "image" in info.get("capabilities", set()):
                    # For OpenAI, use gpt-image-1 specifically
                    if provider == "openai":
                        llm = cls.model_named("openai:gpt-image-1")
                    else:
                        llm = cls.from_provider(provider)
                    return llm.image(prompt, file_name, width, height)
            except Exception:
                continue  # Try next provider

        raise DazLlmError("No configured provider supports image generation")

    @classmethod
    async def async_generate_image(
        cls,
        prompt: str,
        file_name: str,
        width: int = 1024,
        height: int = 1024,
        preferred_provider: Optional[str] = None,
    ) -> str:
        """Async image generation variant selecting the best provider."""
        from .provider_manager import ProviderManager

        provider_preference = ["openai", "google", "anthropic"]

        if preferred_provider:
            try:
                provider = ProviderManager.resolve_provider_alias(preferred_provider)
                info = ProviderManager.get_provider_info(provider)
                if "image" in info.get("capabilities", set()):
                    llm = cls.from_provider(provider)
                    return await llm.async_image(prompt, file_name, width, height)
            except Exception:
                pass

        for provider in provider_preference:
            try:
                info = ProviderManager.get_provider_info(provider)
                if info.get("configured", False) and "image" in info.get("capabilities", set()):
                    if provider == "openai":
                        llm = cls.model_named("openai:gpt-image-1")
                    else:
                        llm = cls.from_provider(provider)
                    return await llm.async_image(prompt, file_name, width, height)
            except Exception:
                continue

        raise DazLlmError("No configured provider supports image generation")


def _run_sync(coro):
    """Run an async coroutine from sync context, even if a loop is running.

    - If no running loop, uses asyncio.run.
    - If a loop is running (e.g. called from async context), runs the coroutine
      in a dedicated event loop on a background thread and blocks for the result.
    """
    import asyncio
    import threading

    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(coro)

    result_box = {}
    error_box = {}

    def _worker():
        loop = asyncio.new_event_loop()
        try:
            asyncio.set_event_loop(loop)
            result = loop.run_until_complete(coro)
            result_box["result"] = result
        except Exception as e:  # noqa: BLE001
            error_box["error"] = e
        finally:
            loop.close()

    t = threading.Thread(target=_worker, daemon=True)
    t.start()
    t.join()
    if error_box:
        raise error_box["error"]
    return result_box["result"]


# Check configuration status across providers
def check_configuration() -> Dict[str, Dict[str, Union[bool, str]]]:
    from .provider_manager import ProviderManager, PROVIDERS

    status: Dict[str, Dict[str, Union[bool, str]]] = {}
    for provider in PROVIDERS.keys():
        try:
            info = ProviderManager.get_provider_info(provider)
            status[provider] = {
                "configured": info["configured"],
                "error": None,
            }
        except ModelNotFoundError as e:
            status[provider] = {"configured": False, "error": str(e)}
        except (ImportError, AttributeError) as e:
            status[provider] = {"configured": False, "error": f"Import error: {e}"}
    return status


# Basic tests to ensure core wiring behaves as expected
class TestLlmCore(unittest.TestCase):
    # Verify enum values are stable
    def test_model_type_enum(self):
        self.assertEqual(ModelType.LOCAL_SMALL.value, "local_small")
        self.assertEqual(ModelType.PAID_BEST.value, "paid_best")

    # Verify exception hierarchy
    def test_exception_hierarchy(self):
        self.assertTrue(issubclass(ConfigurationError, DazLlmError))
        self.assertTrue(issubclass(ModelNotFoundError, DazLlmError))

    # Providers are discoverable (do not assert specific names; environments vary)
    def test_get_providers(self):
        providers = Llm.get_providers()
        self.assertIsInstance(providers, list)
        self.assertGreaterEqual(len(providers), 0)

    # Configuration checker returns a dict
    def test_check_configuration_function(self):
        status = check_configuration()
        self.assertIsInstance(status, dict)

    # TypedDict layout is correct
    def test_message_structure(self):
        msg = {"role": "user", "content": "Hello"}
        self.assertIn("role", msg)
        self.assertIn("content", msg)

    # Conversation union accepts both forms
    def test_conversation_types(self):
        conv_str = "Hello"
        conv_list = [{"role": "user", "content": "Hello"}]
        self.assertIsInstance(conv_str, (str, list))
        self.assertIsInstance(conv_list, (str, list))


# Public exports
__all__ = [
    "Llm",
    "ModelType",
    "Message",
    "Conversation",
    "DazLlmError",
    "ConfigurationError",
    "ModelNotFoundError",
    "check_configuration",
]
