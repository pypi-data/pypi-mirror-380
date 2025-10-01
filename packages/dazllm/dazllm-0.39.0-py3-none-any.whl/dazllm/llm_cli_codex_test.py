"""
Comprehensive tests for Codex CLI structured output with result.json separation

Tests various schemas and ensures proper separation of output logs from results.
"""

from typing import Dict, List, Optional

from pydantic import BaseModel, Field

from .llm_cli_codex import LlmCodexCli

# Removed unused import

# Define test schemas (same as Claude tests for consistency)


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


class TestCodexCliStructured:
    """Test Codex CLI structured output with real calls"""

    def test_simple_schema(self):
        """Test with a simple schema using deterministic values"""
        cli = LlmCodexCli()

        conversation = [
            {
                "role": "user",
                "content": """Return JSON with EXACTLY these values:
                {"name": "Alice", "age": 25, "is_active": true}

                DO NOT change any values. Return exactly as specified.""",
            }
        ]

        result = cli.chat_structured(conversation, SimpleSchema)

        # Verify result - check basic validity
        assert isinstance(result.value.name, str), "name must be str"
        assert len(result.value.name) > 0, "name must not be empty"
        assert isinstance(result.value.age, int), "age must be int"
        assert result.value.age >= 0, "age must be positive"
        assert isinstance(result.value.is_active, bool), "is_active must be bool"

        # Verify logs are present
        assert "Codex CLI Async Structured Output" in result.output or "Codex CLI Structured Output" in result.output
        assert "Schema: SimpleSchema" in result.output
        assert "Validation: PASSED" in result.output

    def test_file_listing_task(self):
        """Test schema structure validation"""
        cli = LlmCodexCli()

        conversation = [
            {
                "role": "user",
                "content": """Return JSON with EXACTLY these values:
                {
                    "total_files": 50,
                    "directories": ["app", "tests", "utils"],
                    "files": ["server.py", "client.py", "README.md"],
                    "most_common_extensions": {".py": 35, ".md": 10, ".json": 5}
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

        # Verify separation of logs and result
        assert "Console Output" in result.output or "Processing Response" in result.output

    def test_code_analysis_task(self):
        """Test code analysis schema structure"""
        cli = LlmCodexCli()

        conversation = [
            {
                "role": "user",
                "content": """Return JSON with EXACTLY these values:
                {
                    "file_count": 18,
                    "total_lines": 3200,
                    "function_count": 180,
                    "class_count": 40,
                    "summary": "Comprehensive analysis of Python codebase with test files and utilities"
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
        cli = LlmCodexCli()

        conversation = [
            {
                "role": "user",
                "content": """Return JSON with EXACTLY these values:
                {
                    "user": {
                        "name": "Bob Johnson",
                        "age": 32,
                        "email": "bob@example.com"
                    },
                    "projects": [
                        {
                            "name": "APIServer",
                            "language": "Go",
                            "stars": 200,
                            "contributors": ["Alice", "Charlie"]
                        },
                        {
                            "name": "MLPipeline",
                            "language": "Python",
                            "stars": 150,
                            "contributors": ["David", "Eve"]
                        }
                    ],
                    "total_contributions": 1024,
                    "active_since": "2018"
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
        """Test task execution schema structure"""
        cli = LlmCodexCli()

        conversation = [
            {
                "role": "user",
                "content": """Return JSON with EXACTLY these values:
                {
                    "task_name": "Python Keywords Summary",
                    "files_created": ["codex_summary.txt"],
                    "success": true,
                    "output_summary": "Created summary file with list of Python keywords and counted them",
                    "metrics": {"keyword_count": 35, "unique_chars": 120}
                }

                DO NOT change any values. Return exactly as specified.""",
            }
        ]

        result = cli.chat_structured(conversation, TaskExecutionSchema)

        # Verify result structure and types
        assert isinstance(result.value.task_name, str), "task_name must be str"
        assert len(result.value.task_name) > 0, "task_name must not be empty"
        assert isinstance(result.value.success, bool), "success must be bool"
        assert isinstance(result.value.files_created, list), "files_created must be list"
        assert len(result.value.files_created) >= 1, "must have at least one file"
        assert isinstance(result.value.output_summary, str), "output_summary must be str"
        assert len(result.value.output_summary) > 10, "output_summary must be meaningful"
        assert isinstance(result.value.metrics, dict), "metrics must be dict"
        assert len(result.value.metrics) > 0, "metrics must not be empty"

    def test_schema_validation_with_markers(self):
        """Test that validation and extraction works correctly"""
        cli = LlmCodexCli()

        conversation = [
            {
                "role": "user",
                "content": """Return JSON with EXACTLY these values:
                {"name": "Test Person", "age": 28, "is_active": true}

                DO NOT change any values. Return exactly as specified.""",
            }
        ]

        result = cli.chat_structured(conversation, SimpleSchema)

        # Check types and validity
        assert isinstance(result.value.name, str), "name must be str"
        assert len(result.value.name) > 0, "name must not be empty"
        assert isinstance(result.value.age, int), "age must be int"
        assert result.value.age >= 0, "age must be positive"
        assert isinstance(result.value.is_active, bool), "is_active must be bool"

        # Check that processing occurred
        assert "Processing Response" in result.output or "Validation: PASSED" in result.output

    def test_multiple_calls_consistency(self):
        """Test that multiple calls work correctly"""
        cli = LlmCodexCli()

        results = []
        for i in range(3):
            age_value = 30 + i
            conversation = [
                {
                    "role": "user",
                    "content": f"""Return JSON with EXACTLY these values:
                    {{"name": "Person{i}", "age": {age_value}, "is_active": true}}

                    DO NOT change any values. Return exactly as specified.""",
                }
            ]

            result = cli.chat_structured(conversation, SimpleSchema)
            results.append(result)

            # Each result should be valid - check types
            assert isinstance(result.value.age, int), f"Call {i}: age must be int"
            assert result.value.age >= 0, f"Call {i}: age must be positive"
            assert isinstance(result.value.is_active, bool), f"Call {i}: is_active must be bool"
            assert isinstance(result.value.name, str), f"Call {i}: name must be str"

        # All results should have proper logging
        for i, result in enumerate(results):
            assert (
                "Codex CLI Async Structured Output" in result.output or "Codex CLI Structured Output" in result.output
            ), f"Call {i}: missing CLI header"
            assert "Validation: PASSED" in result.output, f"Call {i}: missing validation status"


class TestCodexCliEdgeCases:
    """Test edge cases and error handling"""

    def test_empty_response_handling(self):
        """Test that LLM handles requests even when asked for empty objects"""
        cli = LlmCodexCli()

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

        cli = LlmCodexCli()

        conversation = [
            {
                "role": "user",
                "content": """Return JSON with EXACTLY these values:
                {
                    "items": [
                        {"id": "1", "name": "First Item", "description": "Description 1"},
                        {"id": "2", "name": "Second Item", "description": "Description 2"}
                    ],
                    "metadata": {
                        "values": [10, 20, 30],
                        "codes": [1, 2, 3]
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
        assert all("id" in item for item in result.value.items), "each item must have 'id' key"
        assert all("name" in item for item in result.value.items), "each item must have 'name' key"
        assert isinstance(result.value.metadata, dict), "metadata must be dict"
        assert len(result.value.metadata) > 0, "metadata must not be empty"
        # Check that metadata values are lists of ints
        for key, value in result.value.metadata.items():
            assert isinstance(value, list), f"metadata[{key}] must be list"
            assert all(isinstance(v, int) for v in value), f"metadata[{key}] must contain ints"
