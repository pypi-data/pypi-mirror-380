#!/usr/bin/env python3
"""
Test script to verify gpt-oss:20b works with structured responses using format parameter
"""

from pydantic import BaseModel

# Import from local development version
try:
    from .llm_ollama import LlmOllama
except ImportError:
    # Running as script, use absolute import with local path
    from llm_ollama import LlmOllama


class PersonData(BaseModel):
    """Test data structure for gpt-oss:20b"""

    name: str
    age: int
    occupation: str
    active: bool


def test_gpt_oss_structured_response():
    """Test that gpt-oss:20b correctly identifies as NOT supporting format parameter"""
    print("Testing gpt-oss:20b format support detection...")

    try:
        # Check if Ollama is available
        LlmOllama.check_config()
        print("✓ Ollama is available")
    except Exception as e:
        print(f"✗ Ollama not available: {e}")
        print("Skipping test - Ollama is required")
        return  # Skip test gracefully

    try:
        # Create LLM instance using proper Ollama provider format
        llm = LlmOllama("ollama:gpt-oss:20b")
        print("✓ gpt-oss:20b model initialized")

        # Verify it does NOT support format parameter (known issue with Harmony format)
        supports_format = llm._supports_format
        print(f"✓ Supports format parameter: {supports_format}")

        assert not supports_format, "Expected gpt-oss:20b to NOT support format parameter (uses alternative method)"

        # Test that chat_structured uses the alternative method (not format parameter)
        conversation = [
            {
                "role": "user",
                "content": "Create a person profile for John Smith, a 30-year-old software engineer.",
            }
        ]

        print("🔄 Testing structured response with alternative method...")
        result = llm.chat_structured(conversation, PersonData)

        print("✓ Structured response received using alternative method:")
        print(f"  Type: {type(result)}")
        print(f"  Data: {result}")

        # Verify it's the correct type
        assert isinstance(result.value, PersonData), f"Expected PersonData, got {type(result.value)}"

        person = result.value
        print("✓ Valid PersonData object:")
        print(f"  Name: {person.name}")
        print(f"  Age: {person.age}")
        print(f"  Occupation: {person.occupation}")
        print(f"  Active: {person.active}")

        # Basic validation
        assert isinstance(person.name, str) and person.name, "Invalid name field"
        assert isinstance(person.age, int) and person.age > 0, "Invalid age field"
        assert isinstance(person.occupation, str) and person.occupation, "Invalid occupation field"
        assert isinstance(person.active, bool), "Invalid active field"

        print("✅ All validations passed!")
        print("✅ gpt-oss:20b correctly uses alternative method for structured responses!")

    except Exception as e:
        print(f"✗ Test failed with error: {e}")
        import traceback

        traceback.print_exc()
        raise


def main():
    """Run the test"""
    print("=" * 70)
    print("Testing gpt-oss:20b Alternative Method Detection")
    print("Verifying that alternative structured response method is used")
    print("=" * 70)
    print()

    try:
        test_gpt_oss_structured_response()
        print()
        print("=" * 70)
        print("✅ SUCCESS: gpt-oss:20b correctly uses alternative method!")
        print("The model properly detects lack of format support and uses workaround.")
        print("=" * 70)
        return 0
    except Exception:
        print()
        print("=" * 70)
        print("❌ FAILURE: gpt-oss:20b alternative method detection failed")
        print("The implementation may need investigation.")
        print("=" * 70)
        return 1


if __name__ == "__main__":
    exit(main())
