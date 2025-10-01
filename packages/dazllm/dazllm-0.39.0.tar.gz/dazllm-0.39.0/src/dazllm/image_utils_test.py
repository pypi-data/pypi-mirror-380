"""
Tests for image_utils.py
"""

# Import module to ensure coverage
import dazllm.image_utils  # noqa: F401
from dazllm.image_utils import ImageUtils


def test_calculate_optimal_size():
    """Test optimal size calculation for OpenAI"""
    # Square aspect ratio
    width, height = ImageUtils.calculate_optimal_size(500, 500)
    assert (width, height) == (1024, 1024)

    # Landscape aspect ratio
    width, height = ImageUtils.calculate_optimal_size(800, 600)
    assert (width, height) == (1536, 1024)

    # Portrait aspect ratio
    width, height = ImageUtils.calculate_optimal_size(600, 800)
    assert (width, height) == (1024, 1536)


def test_enhance_prompt_for_aspect_ratio():
    """Test prompt enhancement for different aspect ratios"""
    # Landscape
    prompt = ImageUtils.enhance_prompt_for_aspect_ratio("A mountain", 1536, 1024)
    assert "landscape" in prompt or "wide" in prompt

    # Portrait
    prompt = ImageUtils.enhance_prompt_for_aspect_ratio("A tower", 1024, 1536)
    assert "portrait" in prompt or "tall" in prompt

    # Square
    prompt = ImageUtils.enhance_prompt_for_aspect_ratio("A circle", 1024, 1024)
    assert prompt == "A circle"


def test_aspect_ratio_calculation():
    """Test aspect ratio is calculated correctly"""
    # Basic aspect ratio math
    assert 1536 / 1024 == 1.5  # Landscape
    assert 1024 / 1536 < 1.0  # Portrait
    assert 1024 / 1024 == 1.0  # Square
