"""
Memoization utilities for LLM responses

Provides caching of LLM responses based on conversation content.
This speeds up repeated calls with identical prompts (common in tests)
while still making real calls the first time.
"""

import functools
import hashlib
import json
import pickle
from pathlib import Path
from typing import Any, Callable


def _hash_conversation(conversation: Any) -> str:
    """Create a stable hash of a conversation for cache key"""
    # Normalize conversation to string form
    if isinstance(conversation, str):
        content = conversation
    elif isinstance(conversation, list):
        # Sort dict keys for stable hashing
        content = json.dumps(conversation, sort_keys=True)
    else:
        content = str(conversation)

    return hashlib.sha256(content.encode()).hexdigest()


def _get_cache_dir() -> Path:
    """Get or create the cache directory for memoized responses"""
    cache_dir = Path.home() / ".cache" / "dazllm" / "memoization"
    cache_dir.mkdir(parents=True, exist_ok=True)
    return cache_dir


def memoize_llm_response(method: Callable) -> Callable:
    """
    Decorator that memoizes LLM responses based on conversation content.

    The first call with a given conversation will make a real API call.
    Subsequent calls with the same conversation will return the cached response.

    This is particularly useful for tests that repeatedly use the same prompts,
    and can also speed up production code with repeated patterns.
    """

    @functools.wraps(method)
    def wrapper(self, conversation: Any, *args, **kwargs) -> Any:
        # Create cache key from method name, provider, model, and conversation
        provider = getattr(self, "provider", "unknown")
        model = getattr(self, "model", "unknown")
        conv_hash = _hash_conversation(conversation)

        # Include schema in cache key if present (for structured calls)
        schema_name = ""
        if "schema" in kwargs:
            schema_name = f"_{kwargs['schema'].__name__}"

        cache_key = f"{provider}_{model}_{method.__name__}{schema_name}_{conv_hash}"
        cache_file = _get_cache_dir() / f"{cache_key}.pkl"

        # Try to load from cache
        if cache_file.exists():
            try:
                with open(cache_file, "rb") as f:
                    return pickle.load(f)
            except Exception:
                # If cache is corrupted, ignore and proceed with real call
                pass

        # Make real call
        result = method(self, conversation, *args, **kwargs)

        # Cache the result
        try:
            with open(cache_file, "wb") as f:
                pickle.dump(result, f)
        except Exception:
            # If caching fails, that's ok - we still have the result
            pass

        return result

    return wrapper


def memoize_llm_response_async(method: Callable) -> Callable:
    """
    Async version of memoize_llm_response decorator.

    Provides the same caching behavior for async methods.
    """

    @functools.wraps(method)
    async def wrapper(self, conversation: Any, *args, **kwargs) -> Any:
        # Create cache key from method name, provider, model, and conversation
        provider = getattr(self, "provider", "unknown")
        model = getattr(self, "model", "unknown")
        conv_hash = _hash_conversation(conversation)

        # Include schema in cache key if present (for structured calls)
        schema_name = ""
        if "schema" in kwargs:
            schema_name = f"_{kwargs['schema'].__name__}"

        cache_key = f"{provider}_{model}_{method.__name__}{schema_name}_{conv_hash}"
        cache_file = _get_cache_dir() / f"{cache_key}.pkl"

        # Try to load from cache
        if cache_file.exists():
            try:
                with open(cache_file, "rb") as f:
                    return pickle.load(f)
            except Exception:
                # If cache is corrupted, ignore and proceed with real call
                pass

        # Make real call
        result = await method(self, conversation, *args, **kwargs)

        # Cache the result
        try:
            with open(cache_file, "wb") as f:
                pickle.dump(result, f)
        except Exception:
            # If caching fails, that's ok - we still have the result
            pass

        return result

    return wrapper


def clear_memoization_cache():
    """Clear all memoized responses"""
    cache_dir = _get_cache_dir()
    for cache_file in cache_dir.glob("*.pkl"):
        cache_file.unlink()
