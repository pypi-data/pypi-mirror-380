"""
Tests for cli.py
"""

from dazllm.cli import create_dynamic_model, get_version
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


def test_model_type_enum():
    """Test ModelType enum for CLI"""
    assert ModelType.PAID_CHEAP.value == "paid_cheap"
    assert ModelType.PAID_BEST.value == "paid_best"
    assert ModelType.LOCAL_SMALL.value == "local_small"
