#!/usr/bin/env python3
"""
Debug script to see what gpt-oss:20b is actually returning
"""

import json

try:
    from .llm_ollama import LlmOllama
except ImportError:
    from llm_ollama import LlmOllama


def debug_gpt_oss_response():
    """Debug what gpt-oss:20b is actually returning"""
    print("Debugging gpt-oss:20b response...")

    try:
        # Check if Ollama is available
        LlmOllama.check_config()
        print("✓ Ollama is available")
    except Exception as e:
        print(f"✗ Ollama not available: {e}")
        return

    try:
        # Create LLM instance
        llm = LlmOllama("ollama:gpt-oss:20b")
        print("✓ gpt-oss:20b model initialized")
        print(f"✓ Supports format parameter: {llm._supports_format}")

        # Test simple chat first
        print("\n🔄 Testing simple chat...")
        simple_conversation = [
            {"role": "user", "content": "Say hello in JSON format with a 'message' field"}
        ]

        simple_result = llm.chat(simple_conversation, force_json=True)
        print(f"Simple response: {simple_result}")

        # Test with format parameter directly
        print("\n🔄 Testing with format parameter...")

        # Build the request manually to see what's happening
        messages = llm._normalize_conversation(simple_conversation)

        # Try different format parameter formats
        formats_to_try = [
            {"type": "json"},  # Current format
            "json",            # Simple string
            {"json": True},    # Boolean flag
        ]

        import requests

        for format_param in formats_to_try:
            print(f"\n🔄 Trying format: {format_param}")
            payload = {
                "model": llm.model,
                "messages": messages,
                "format": format_param,
                "stream": False
            }

            print(f"Request payload: {json.dumps(payload, indent=2)}")

            response = requests.post(
                f"{llm.base_url}/api/chat",
                json=payload,
                headers=llm.headers,
            )

            print(f"Response status: {response.status_code}")
            print(f"Response content: {response.text}")

            if response.status_code == 200:
                response_data = response.json()
                message_content = response_data.get("message", {}).get("content", "")
                print(f"✅ SUCCESS! Message content: {message_content}")
                break
            else:
                print(f"❌ Failed with format: {format_param}")

    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    debug_gpt_oss_response()
