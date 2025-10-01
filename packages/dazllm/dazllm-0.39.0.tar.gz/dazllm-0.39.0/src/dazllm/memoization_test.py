"""
Tests for memoization module
"""

import time
from pathlib import Path

import pytest

from .memoization import (
    _get_cache_dir,
    _hash_conversation,
    clear_memoization_cache,
    memoize_llm_response,
    memoize_llm_response_async,
)


def test_hash_conversation_string():
    """Test hashing a string conversation"""
    hash1 = _hash_conversation("Hello world")
    hash2 = _hash_conversation("Hello world")
    hash3 = _hash_conversation("Different")

    assert hash1 == hash2
    assert hash1 != hash3


def test_hash_conversation_list():
    """Test hashing a list conversation"""
    conv1 = [{"role": "user", "content": "Hello"}]
    conv2 = [{"role": "user", "content": "Hello"}]
    conv3 = [{"role": "user", "content": "Goodbye"}]

    hash1 = _hash_conversation(conv1)
    hash2 = _hash_conversation(conv2)
    hash3 = _hash_conversation(conv3)

    assert hash1 == hash2
    assert hash1 != hash3


def test_cache_dir_creation():
    """Test that cache directory is created"""
    cache_dir = _get_cache_dir()
    assert cache_dir.exists()
    assert cache_dir.is_dir()
    assert cache_dir == Path.home() / ".cache" / "dazllm" / "memoization"


def test_memoize_decorator():
    """Test that memoization works"""
    # Clear cache first
    clear_memoization_cache()

    call_count = 0

    class MockLlm:
        provider = "test"
        model = "test-model"

        @memoize_llm_response
        def chat(self, conversation):
            nonlocal call_count
            call_count += 1
            return f"Response {call_count}"

    llm = MockLlm()

    # First call should execute
    result1 = llm.chat("Hello")
    assert result1 == "Response 1"
    assert call_count == 1

    # Second call with same input should use cache
    result2 = llm.chat("Hello")
    assert result2 == "Response 1"  # Same response
    assert call_count == 1  # Not incremented

    # Different input should execute
    result3 = llm.chat("Goodbye")
    assert result3 == "Response 2"
    assert call_count == 2


@pytest.mark.asyncio
async def test_memoize_async_decorator():
    """Test that async memoization works"""
    # Clear cache first
    clear_memoization_cache()

    call_count = 0

    class MockLlm:
        provider = "test"
        model = "test-model"

        @memoize_llm_response_async
        async def chat_async(self, conversation):
            nonlocal call_count
            call_count += 1
            return f"Response {call_count}"

    llm = MockLlm()

    # First call should execute
    result1 = await llm.chat_async("Hello")
    assert result1 == "Response 1"
    assert call_count == 1

    # Second call with same input should use cache
    result2 = await llm.chat_async("Hello")
    assert result2 == "Response 1"  # Same response
    assert call_count == 1  # Not incremented

    # Different input should execute
    result3 = await llm.chat_async("Goodbye")
    assert result3 == "Response 2"
    assert call_count == 2


def test_memoize_with_schema():
    """Test that schema parameter is included in cache key"""
    # Clear cache first
    clear_memoization_cache()

    call_count = 0

    class Schema1:
        __name__ = "Schema1"

    class Schema2:
        __name__ = "Schema2"

    class MockLlm:
        provider = "test"
        model = "test-model"

        @memoize_llm_response
        def chat_structured(self, conversation, schema=None):
            nonlocal call_count
            call_count += 1
            return f"Response {call_count}"

    llm = MockLlm()

    # Same conversation, different schemas should execute separately
    result1 = llm.chat_structured("Hello", schema=Schema1)
    assert result1 == "Response 1"
    assert call_count == 1

    result2 = llm.chat_structured("Hello", schema=Schema2)
    assert result2 == "Response 2"
    assert call_count == 2

    # Same conversation and schema should use cache
    result3 = llm.chat_structured("Hello", schema=Schema1)
    assert result3 == "Response 1"  # Cached
    assert call_count == 2  # Not incremented


def test_clear_cache():
    """Test clearing the cache"""
    # Clear cache first
    clear_memoization_cache()

    call_count = 0

    class MockLlm:
        provider = "test"
        model = "test-model"

        @memoize_llm_response
        def chat(self, conversation):
            nonlocal call_count
            call_count += 1
            return f"Response {call_count}"

    llm = MockLlm()

    # Create a cached response
    result1 = llm.chat("Hello")
    assert result1 == "Response 1"
    assert call_count == 1

    # Clear cache
    clear_memoization_cache()

    # Next call should execute again
    result2 = llm.chat("Hello")
    assert result2 == "Response 2"
    assert call_count == 2


def test_corrupted_cache_handling():
    """Test that corrupted cache files are handled gracefully"""
    # Clear cache first
    clear_memoization_cache()

    call_count = 0

    class MockLlm:
        provider = "test"
        model = "test-model"

        @memoize_llm_response
        def chat(self, conversation):
            nonlocal call_count
            call_count += 1
            return f"Response {call_count}"

    llm = MockLlm()

    # First call to create cache entry
    result1 = llm.chat("Hello")
    assert result1 == "Response 1"

    # Corrupt the cache file
    cache_dir = _get_cache_dir()
    cache_files = list(cache_dir.glob("*.pkl"))
    assert len(cache_files) > 0
    with open(cache_files[0], "w") as f:
        f.write("corrupted data")

    # Should handle corrupted cache and make real call
    result2 = llm.chat("Hello")
    assert result2 == "Response 2"
    assert call_count == 2


def test_memoization_speeds_up_calls():
    """Test that memoization actually speeds things up"""
    # Clear cache first
    clear_memoization_cache()

    class MockLlm:
        provider = "test"
        model = "test-model"

        @memoize_llm_response
        def chat(self, conversation):
            # Simulate slow API call
            time.sleep(0.1)
            return "Response"

    llm = MockLlm()

    # First call should be slow
    start = time.time()
    result1 = llm.chat("Hello")
    duration1 = time.time() - start
    assert duration1 >= 0.1

    # Second call should be much faster
    start = time.time()
    result2 = llm.chat("Hello")
    duration2 = time.time() - start
    assert duration2 < 0.05  # Should be nearly instant
    assert result1 == result2
