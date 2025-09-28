#!/usr/bin/env python3
"""
Demo of the new LlmCli interface with enhanced logging capabilities

This example shows how to use the new Llm.cli() interface to get both
responses and comprehensive execution logs from CLI providers.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pydantic import BaseModel
from dazllm.core import Llm
from colorama import init, Fore, Style

# Initialize colorama for pretty output
init(autoreset=True)


class TaskResult(BaseModel):
    """Example schema for structured output"""
    task_name: str
    complexity: int  # 1-10 scale
    estimated_time_hours: float
    priority: str  # "low", "medium", "high"


def demo_basic_cli_logging():
    """Demonstrate basic CLI usage with logging"""
    print(f"{Fore.CYAN}{Style.BRIGHT}🔧 Basic CLI with Logging Demo")
    print("=" * 50)

    # Get the CLI interface
    cli = Llm.cli()

    print(f"Available providers: {Fore.GREEN}{cli.get_available_providers()}")
    print(f"Capabilities: {Fore.GREEN}{cli.capabilities()}")

    # Basic chat with logging
    print(f"\n{Fore.YELLOW}📝 Testing basic chat...")
    response = cli.chat("What is the capital of Japan? Answer briefly.")

    print(f"{Fore.GREEN}✓ Response: {response.value}")
    print(f"{Fore.BLUE}📋 Execution log ({len(response.output)} chars):")
    print(f"{Fore.CYAN}{response.output}")


def demo_structured_output_with_logging():
    """Demonstrate structured output with detailed logging"""
    print(f"\n{Fore.MAGENTA}{Style.BRIGHT}🏗️ Structured Output with Logging Demo")
    print("=" * 50)

    cli = Llm.cli()

    prompt = """Analyze this software development task and return structured data:

    Task: "Implement user authentication system with JWT tokens"

    Return JSON with:
    - task_name: string description
    - complexity: number 1-10 (where 10 is most complex)
    - estimated_time_hours: decimal hours
    - priority: "low", "medium", or "high"

    Example format:
    {
        "task_name": "Implement user authentication system with JWT tokens",
        "complexity": 7,
        "estimated_time_hours": 16.5,
        "priority": "high"
    }"""

    print(f"{Fore.YELLOW}📝 Testing structured output...")
    response = cli.chat_structured(prompt, TaskResult)

    print(f"{Fore.GREEN}✓ Structured Result:")
    print(f"  Task: {response.value.task_name}")
    print(f"  Complexity: {response.value.complexity}/10")
    print(f"  Time Estimate: {response.value.estimated_time_hours} hours")
    print(f"  Priority: {response.value.priority}")

    print(f"\n{Fore.BLUE}📋 Detailed execution log:")
    print(f"{Fore.CYAN}{response.output}")


def demo_conversation_with_logging():
    """Demonstrate conversation format with logging"""
    print(f"\n{Fore.RED}{Style.BRIGHT}💬 Conversation with Logging Demo")
    print("=" * 50)

    cli = Llm.cli()

    conversation = [
        {"role": "system", "content": "You are a helpful coding assistant. Be concise."},
        {"role": "user", "content": "What's the difference between Python lists and tuples?"},
        {"role": "assistant", "content": "Lists are mutable (can be changed), tuples are immutable (cannot be changed)."},
        {"role": "user", "content": "Which is faster for accessing elements?"}
    ]

    print(f"{Fore.YELLOW}📝 Testing conversation format...")
    response = cli.chat(conversation)

    print(f"{Fore.GREEN}✓ Response: {response.value}")

    # Show interesting parts of the log
    log_lines = response.output.split('\n')
    print(f"\n{Fore.BLUE}📋 Key log sections:")
    for line in log_lines:
        if any(keyword in line for keyword in ['Command:', 'Return code:', 'succeeded', 'Conversation']):
            print(f"{Fore.CYAN}  {line}")


def demo_error_handling_and_logging():
    """Demonstrate error handling with comprehensive logging"""
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}🚨 Error Handling and Logging Demo")
    print("=" * 50)

    cli = Llm.cli()

    try:
        # This should work but let's see the logs
        response = cli.chat("Explain quantum computing in exactly 10 words.")

        print(f"{Fore.GREEN}✓ Response: {response.value}")

        # Look for any warnings or issues in the logs
        log_lines = response.output.split('\n')
        issues = [line for line in log_lines if any(word in line.lower() for word in
                 ['error', 'warning', 'failed', 'timeout', 'retry'])]

        if issues:
            print(f"{Fore.YELLOW}⚠️ Issues found in logs:")
            for issue in issues:
                print(f"  {issue}")
        else:
            print(f"{Fore.GREEN}✓ Clean execution - no issues found")

    except Exception as e:
        print(f"{Fore.RED}❌ Exception caught: {e}")
        # The exception should include detailed logs
        if "Log:" in str(e):
            print(f"{Fore.BLUE}📋 Exception includes detailed logs as expected!")


def main():
    """Run all CLI logging demos"""
    print(f"{Fore.WHITE}{Style.BRIGHT}🚀 LlmCli Enhanced Logging Demo")
    print("=" * 60)
    print("This demo shows the new CLI interface that captures both")
    print("responses AND comprehensive execution logs from CLI tools.")
    print("=" * 60)

    try:
        demo_basic_cli_logging()
        demo_structured_output_with_logging()
        demo_conversation_with_logging()
        demo_error_handling_and_logging()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}🎉 All CLI logging demos completed successfully!")
        print("=" * 60)
        print("Key features demonstrated:")
        print("✓ Basic chat with execution logging")
        print("✓ Structured output with schema validation logging")
        print("✓ Conversation format with detailed logs")
        print("✓ Error handling with comprehensive log capture")
        print("✓ Meta-provider that tries all available CLI tools")
        print("✓ Real CLI execution logs (not simulated)")

    except Exception as e:
        print(f"\n{Fore.RED}❌ Demo failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()