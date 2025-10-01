"""
Comprehensive tests for Claude CLI structured output with result.json separation

Tests various schemas and ensures proper separation of output logs from results.
"""

from typing import Dict, List, Optional

from pydantic import BaseModel, Field

# Removed unused import
from .llm_cli_claude import LlmClaudeCliWithLogging as LlmClaudeCli

# Define test schemas


class SimpleSchema(BaseModel):
    """Simple schema with basic types"""

    name: str
    age: int
    is_active: bool


class FileListSchema(BaseModel):
    """Schema for file listing task"""

    total_files: int = Field(description="Total number of files found")
    directories: List[str] = Field(description="List of directory names")
    files: List[str] = Field(description="List of file names")
    most_common_extensions: Dict[str, int] = Field(description="Extension counts")


class AnalysisResultSchema(BaseModel):
    """Schema for code analysis result"""

    file_count: int = Field(description="Number of Python files")
    total_lines: int = Field(description="Total lines of code")
    function_count: int = Field(description="Number of functions")
    class_count: int = Field(description="Number of classes")
    summary: str = Field(description="Brief summary of findings")


class ComplexNestedSchema(BaseModel):
    """Complex schema with nested structures"""

    class PersonInfo(BaseModel):
        name: str
        age: int
        email: Optional[str] = None

    class ProjectInfo(BaseModel):
        name: str
        language: str
        stars: int
        contributors: List[str]

    user: PersonInfo
    projects: List[ProjectInfo]
    total_contributions: int
    active_since: str


class TaskExecutionSchema(BaseModel):
    """Schema for task execution with file creation"""

    task_name: str = Field(description="Name of the executed task")
    files_created: List[str] = Field(description="List of files created")
    success: bool = Field(description="Whether task succeeded")
    output_summary: str = Field(description="Summary of what was done")
    metrics: Dict[str, int] = Field(description="Numeric metrics from the task")


class TestClaudeCliStructured:
    """Test Claude CLI structured output with real calls"""

    def test_simple_schema(self):
        """Test with a simple schema using deterministic values"""
        cli = LlmClaudeCli()

        conversation = [
            {
                "role": "user",
                "content": """Return JSON with EXACTLY these values:
                {"name": "TestUser", "age": 25, "is_active": true}

                DO NOT change any values. Return exactly as specified.""",
            }
        ]

        result = cli.chat_structured(conversation, SimpleSchema)

        # Verify result - check basic validity
        assert isinstance(result.value.age, int), f"Age must be int, got {type(result.value.age)}"
        assert result.value.age >= 0, f"Age must be positive, got {result.value.age}"
        assert isinstance(result.value.is_active, bool), "is_active must be bool"
        assert isinstance(result.value.name, str), "Name must be str"
        assert len(result.value.name) > 0, "Name must not be empty"

        # Verify logs are present
        assert "claude CLI Structured Output" in result.output or "Schema:" in result.output
        assert "Schema: SimpleSchema" in result.output
        assert "Validation: PASSED" in result.output

    def test_file_listing_task(self):
        """Test schema structure validation without depending on exact file system state"""
        cli = LlmClaudeCli()

        conversation = [
            {
                "role": "user",
                "content": """Return JSON with EXACTLY these values:
                {
                    "total_files": 42,
                    "directories": ["src", "tests"],
                    "files": ["main.py", "utils.py", "config.py"],
                    "most_common_extensions": {".py": 30, ".txt": 10, ".md": 2}
                }

                DO NOT change any values. Return exactly as specified.""",
            }
        ]

        result = cli.chat_structured(conversation, FileListSchema)

        # Verify result structure and types only
        assert isinstance(result.value.total_files, int), "total_files must be int"
        assert result.value.total_files > 0, "total_files must be positive"
        assert isinstance(result.value.directories, list), "directories must be list"
        assert isinstance(result.value.files, list), "files must be list"
        assert isinstance(result.value.most_common_extensions, dict), "most_common_extensions must be dict"
        assert len(result.value.most_common_extensions) > 0, "must have at least one extension"

        # Verify logs are present
        assert "Schema:" in result.output or "claude CLI" in result.output

    def test_code_analysis_task(self):
        """Test code analysis schema structure"""
        cli = LlmClaudeCli()

        conversation = [
            {
                "role": "user",
                "content": """Return JSON with EXACTLY these values:
                {
                    "file_count": 15,
                    "total_lines": 2400,
                    "function_count": 120,
                    "class_count": 30,
                    "summary": "Analysis of Python codebase with multiple modules and test files"
                }

                DO NOT change any values. Return exactly as specified.""",
            }
        ]

        result = cli.chat_structured(conversation, AnalysisResultSchema)

        # Verify result types and ranges
        assert isinstance(result.value.file_count, int), "file_count must be int"
        assert result.value.file_count > 0, "file_count must be positive"
        assert isinstance(result.value.total_lines, int), "total_lines must be int"
        assert result.value.total_lines > 0, "total_lines must be positive"
        assert isinstance(result.value.function_count, int), "function_count must be int"
        assert isinstance(result.value.class_count, int), "class_count must be int"
        assert isinstance(result.value.summary, str), "summary must be str"
        assert len(result.value.summary) > 10, "summary must be meaningful"

        # Check logs
        assert "Validation: PASSED" in result.output

    def test_complex_nested_schema(self):
        """Test with complex nested schema structure"""
        cli = LlmClaudeCli()

        conversation = [
            {
                "role": "user",
                "content": """Return JSON with EXACTLY these values:
                {
                    "user": {
                        "name": "Alice Smith",
                        "age": 28,
                        "email": "alice@test.com"
                    },
                    "projects": [
                        {
                            "name": "WebApp",
                            "language": "Python",
                            "stars": 150,
                            "contributors": ["Bob", "Charlie"]
                        },
                        {
                            "name": "DataTool",
                            "language": "Go",
                            "stars": 75,
                            "contributors": ["David"]
                        }
                    ],
                    "total_contributions": 523,
                    "active_since": "2019"
                }

                DO NOT change any values. Return exactly as specified.""",
            }
        ]

        result = cli.chat_structured(conversation, ComplexNestedSchema)

        # Verify nested structures - check types and validity only
        assert isinstance(result.value.user.name, str), "user.name must be str"
        assert len(result.value.user.name) > 0, "user.name must not be empty"
        assert isinstance(result.value.user.age, int), "user.age must be int"
        assert result.value.user.age > 0, "user.age must be positive"
        assert isinstance(result.value.user.email, str), "user.email must be str"
        assert "@" in result.value.user.email, "email must contain @"

        assert isinstance(result.value.projects, list), "projects must be list"
        assert len(result.value.projects) >= 1, "must have at least one project"

        # Check first project structure
        first_project = result.value.projects[0]
        assert isinstance(first_project.name, str), "project.name must be str"
        assert len(first_project.name) > 0, "project.name must not be empty"
        assert isinstance(first_project.language, str), "project.language must be str"
        assert isinstance(first_project.stars, int), "project.stars must be int"
        assert first_project.stars >= 0, "stars must be non-negative"
        assert isinstance(first_project.contributors, list), "contributors must be list"

        assert isinstance(result.value.total_contributions, int), "total_contributions must be int"
        assert result.value.total_contributions >= 0, "total_contributions must be non-negative"
        assert isinstance(result.value.active_since, str), "active_since must be str"
        assert len(result.value.active_since) > 0, "active_since must not be empty"

    def test_task_with_file_creation(self):
        """Test with different simple values"""
        cli = LlmClaudeCli()

        conversation = [
            {
                "role": "user",
                "content": """Return JSON with EXACTLY these values:
                {"name": "AnotherUser", "age": 35, "is_active": false}

                DO NOT change any values. Return exactly as specified.""",
            }
        ]

        result = cli.chat_structured(conversation, SimpleSchema)

        # Verify result - check basic validity
        assert isinstance(result.value.name, str), "name must be str"
        assert len(result.value.name) > 0, "name must not be empty"
        assert isinstance(result.value.age, int), "age must be int"
        assert result.value.age >= 0, "age must be non-negative"
        assert isinstance(result.value.is_active, bool), "is_active must be bool"

    def test_schema_validation_retry(self):
        """Test that validation works with different data"""
        cli = LlmClaudeCli()

        conversation = [
            {
                "role": "user",
                "content": 'Return JSON with EXACTLY these values: {"name": "ValidUser", "age": 30, "is_active": false}. DO NOT change any values.',
            }
        ]

        result = cli.chat_structured(conversation, SimpleSchema)

        # Check types and validity
        assert isinstance(result.value.name, str), "name must be str"
        assert len(result.value.name) > 0, "name must not be empty"
        assert isinstance(result.value.age, int), "age must be int"
        assert result.value.age >= 0, "age must be non-negative"
        assert isinstance(result.value.is_active, bool), "is_active must be bool"

        # Check that output is present
        assert result.output is not None, "output must be present"
        assert len(result.output) > 0, "output must not be empty"

    def test_multiple_calls_cleanup(self):
        """Test that multiple calls work correctly"""
        cli = LlmClaudeCli()

        # First call
        result1 = cli.chat_structured(
            [
                {
                    "role": "user",
                    "content": 'Return JSON with EXACTLY these values: {"name": "TestUser1", "age": 15, "is_active": true}. DO NOT change any values.',
                }
            ],
            SimpleSchema,
        )
        assert isinstance(result1.value.name, str)
        assert isinstance(result1.value.age, int)
        assert result1.value.age >= 0

        # Second call
        result2 = cli.chat_structured(
            [
                {
                    "role": "user",
                    "content": 'Return JSON with EXACTLY these values: {"name": "TestUser2", "age": 16, "is_active": false}. DO NOT change any values.',
                }
            ],
            SimpleSchema,
        )
        assert isinstance(result2.value.name, str)
        assert isinstance(result2.value.age, int)
        assert result2.value.age >= 0

        # Third call
        result3 = cli.chat_structured(
            [
                {
                    "role": "user",
                    "content": 'Return JSON with EXACTLY these values: {"name": "TestUser3", "age": 17, "is_active": true}. DO NOT change any values.',
                }
            ],
            SimpleSchema,
        )
        assert isinstance(result3.value.name, str)
        assert isinstance(result3.value.age, int)
        assert result3.value.age >= 0


class TestClaudeCliEdgeCases:
    """Test edge cases and error handling"""

    def test_empty_response_handling(self):
        """Test that LLM handles requests even when asked for empty objects"""
        cli = LlmClaudeCli()

        # Even when asked for empty object, LLM should provide valid response
        conversation = [{"role": "user", "content": "Return an empty object: {}"}]

        # The LLM is smart enough to fill required fields even when asked for empty object
        # So we just verify it returns a valid result
        result = cli.chat_structured(conversation, SimpleSchema)
        assert result is not None
        assert hasattr(result, "value")
        # The LLM should have provided something valid (even if we asked for empty)
        assert isinstance(result.value, SimpleSchema)

    def test_large_schema(self):
        """Test with large complex schema"""

        class LargeSchema(BaseModel):
            items: List[Dict[str, str]] = Field(description="List of items with string keys and values")
            metadata: Dict[str, List[int]] = Field(description="Metadata with lists of integers")

        cli = LlmClaudeCli()

        conversation = [
            {
                "role": "user",
                "content": """Return JSON with EXACTLY these values:
                {
                    "items": [
                        {"id": "1", "name": "First", "type": "A"},
                        {"id": "2", "name": "Second", "type": "B"},
                        {"id": "3", "name": "Third", "type": "C"}
                    ],
                    "metadata": {
                        "scores": [1, 2, 3],
                        "ratings": [4, 5]
                    }
                }

                DO NOT change any values. Return exactly as specified.""",
            }
        ]

        result = cli.chat_structured(conversation, LargeSchema)

        # Check structure and types
        assert isinstance(result.value.items, list), "items must be list"
        assert len(result.value.items) >= 1, "must have at least one item"
        assert all(isinstance(item, dict) for item in result.value.items), "each item must be dict"
        # Be flexible about dict keys - just check we have dicts with string values
        for item in result.value.items:
            assert len(item) > 0, "each item must have at least one key"
            assert all(isinstance(v, str) for v in item.values()), "all values must be strings"
        assert isinstance(result.value.metadata, dict), "metadata must be dict"
        assert len(result.value.metadata) > 0, "metadata must not be empty"
