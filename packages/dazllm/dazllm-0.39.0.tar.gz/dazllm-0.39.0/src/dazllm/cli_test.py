"""
Tests for cli.py
"""

import io
import sys

from dazllm.cli import create_dynamic_model, error, get_version, header, info, success, warning
from dazllm.core import ModelType


def test_get_version():
    """Test version retrieval"""
    version = get_version()
    assert version is not None
    assert isinstance(version, str)
    assert len(version) > 0


def test_create_dynamic_model():
    """Test creating dynamic model from schema"""
    schema_dict = {
        "properties": {"name": {"type": "string"}, "age": {"type": "integer"}},
        "required": ["name", "age"],
    }
    model = create_dynamic_model(schema_dict)
    assert hasattr(model, "model_fields")
    assert "name" in model.model_fields
    assert "age" in model.model_fields


def test_create_dynamic_model_empty_properties():
    """Test creating dynamic model with no properties"""
    schema_dict = {}
    model = create_dynamic_model(schema_dict)
    assert hasattr(model, "model_fields")
    assert "result" in model.model_fields


def test_create_dynamic_model_all_types():
    """Test creating dynamic model with all supported types"""
    schema_dict = {
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"},
            "score": {"type": "number"},
            "active": {"type": "boolean"},
            "tags": {"type": "array"},
            "data": {"type": "object"},
        }
    }
    model = create_dynamic_model(schema_dict)
    assert "name" in model.model_fields
    assert "age" in model.model_fields
    assert "score" in model.model_fields
    assert "active" in model.model_fields
    assert "tags" in model.model_fields
    assert "data" in model.model_fields


def test_model_type_enum():
    """Test ModelType enum for CLI"""
    assert ModelType.PAID_CHEAP.value == "paid_cheap"
    assert ModelType.PAID_BEST.value == "paid_best"
    assert ModelType.LOCAL_SMALL.value == "local_small"


def test_success_prints_message():
    """Test success function prints with green color"""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    try:
        success("Test success")
        output = captured_output.getvalue()
        assert "Test success" in output
    finally:
        sys.stdout = sys.__stdout__


def test_error_prints_message():
    """Test error function prints with red color"""
    captured_output = io.StringIO()
    sys.stderr = captured_output
    try:
        error("Test error")
        output = captured_output.getvalue()
        assert "Test error" in output
    finally:
        sys.stderr = sys.__stderr__


def test_warning_prints_message():
    """Test warning function prints with yellow color"""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    try:
        warning("Test warning")
        output = captured_output.getvalue()
        assert "Test warning" in output
    finally:
        sys.stdout = sys.__stdout__


def test_info_prints_message():
    """Test info function prints with blue color"""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    try:
        info("Test info")
        output = captured_output.getvalue()
        assert "Test info" in output
    finally:
        sys.stdout = sys.__stdout__


def test_header_prints_message():
    """Test header function prints with cyan color"""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    try:
        header("Test header")
        output = captured_output.getvalue()
        assert "Test header" in output
    finally:
        sys.stdout = sys.__stdout__
