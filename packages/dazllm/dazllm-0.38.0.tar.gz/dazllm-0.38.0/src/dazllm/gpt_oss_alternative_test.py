#!/usr/bin/env python3
"""
Test script to verify gpt-oss:20b works with alternative structured responses
(using manual schema injection instead of format parameter)
"""

from pydantic import BaseModel

try:
    from .llm_ollama import LlmOllama
except ImportError:
    from llm_ollama import LlmOllama


class SimpleProfile(BaseModel):
    """Simple test data structure for gpt-oss:20b alternative testing"""

    name: str
    age: int
    city: str
    is_student: bool


def test_gpt_oss_alternative_method():
    """Test that gpt-oss:20b works with alternative structured responses"""
    print("Testing gpt-oss:20b with alternative method (manual schema injection)...")

    try:
        # Check if Ollama is available
        LlmOllama.check_config()
        print("✓ Ollama is available")
    except Exception as e:
        print(f"✗ Ollama not available: {e}")
        print("Skipping test - Ollama is required")
        return  # Skip test gracefully

    try:
        # Create LLM instance
        llm = LlmOllama("ollama:gpt-oss:20b")
        print("✓ gpt-oss:20b model initialized")

        # Verify it does NOT support format parameter (should use alternative)
        supports_format = llm._supports_format
        print(f"✓ Supports format parameter: {supports_format}")

        if supports_format:
            print("⚠️  Expected gpt-oss:20b to NOT support format parameter")
            print("   This test is specifically for the alternative method")

        # Test structured response using alternative method
        conversation = [
            {
                "role": "user",
                "content": "Create a profile for Alice Johnson, a 25-year-old student living in Boston.",
            }
        ]

        print("🔄 Testing structured response with alternative method...")
        result = llm.chat_structured(conversation, SimpleProfile)

        print("✓ Structured response received using alternative:")
        print(f"  Type: {type(result)}")
        print(f"  Data: {result}")

        # Verify it's the correct type
        assert isinstance(result.value, SimpleProfile), f"Expected SimpleProfile, got {type(result.value)}"

        profile = result.value
        print("✓ Valid SimpleProfile object:")
        print(f"  Name: {profile.name}")
        print(f"  Age: {profile.age}")
        print(f"  City: {profile.city}")
        print(f"  Is Student: {profile.is_student}")

        # Basic validation
        assert isinstance(profile.name, str) and profile.name, "Invalid name field"
        assert isinstance(profile.age, int) and profile.age > 0, "Invalid age field"
        assert isinstance(profile.city, str) and profile.city, "Invalid city field"
        assert isinstance(profile.is_student, bool), "Invalid is_student field"

        print("✅ All validations passed!")
        print("✅ gpt-oss:20b works correctly with alternative method!")

    except Exception as e:
        print(f"✗ Test failed with error: {e}")
        import traceback

        traceback.print_exc()
        raise


def main():
    """Run the test"""
    print("=" * 80)
    print("Testing gpt-oss:20b Alternative Structured Response Support")
    print("Verifying that the manual schema injection method works")
    print("(Research shows gpt-oss:20b has issues with 'format' parameter due to Harmony response format)")
    print("=" * 80)
    print()

    success = test_gpt_oss_alternative_method()

    print()
    print("=" * 80)
    if success:
        print("✅ SUCCESS: gpt-oss:20b works with alternative structured responses!")
        print("The original hack was correct - manual schema injection works around")
        print("the known issues with gpt-oss:20b's Harmony response format.")
    else:
        print("❌ FAILURE: gpt-oss:20b alternative method not working")
        print("This indicates a deeper issue with the model or implementation.")
    print("=" * 80)

    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
