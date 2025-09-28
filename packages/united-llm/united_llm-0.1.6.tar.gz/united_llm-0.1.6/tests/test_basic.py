#!/usr/bin/env python3
"""
Basic tests for United LLM

These are simple tests that verify the package can be imported and basic functionality works.
"""

import pytest
from pathlib import Path
from pydantic import BaseModel
from typing import List


def test_import():
    """Test that the package can be imported"""
    from united_llm import LLMClient
    from united_llm.utils.image_input import ImageInput
    
    assert LLMClient is not None
    assert ImageInput is not None


def test_client_creation():
    """Test that LLMClient can be created with config"""
    from united_llm import LLMClient
    
    config = {
        "api_keys": {
            "openrouter": "test-key",
            "ollama": None
        },
        "base_urls": {
            "openrouter": "https://openrouter.ai/api/v1",
            "ollama": "http://localhost:11434/v1"
        },
        "log_dir": "logs/llm_calls"
    }
    
    client = LLMClient(config_dict=config)
    assert client is not None
    assert client.config == config


def test_provider_detection():
    """Test provider detection logic"""
    from united_llm import LLMClient
    
    config = {
        "api_keys": {"openrouter": "test", "ollama": None},
        "base_urls": {"openrouter": "https://openrouter.ai/api/v1", "ollama": "http://localhost:11434/v1"},
        "log_dir": "logs"
    }
    
    client = LLMClient(config_dict=config)
    
    # Test valid provider detection
    provider, model = client._detect_provider("ollama:qwen3:8b")
    assert provider == "ollama"
    assert model == "qwen3:8b"
    
    provider, model = client._detect_provider("openrouter:google/gemini-2.5-flash-lite")
    assert provider == "openrouter"
    assert model == "google/gemini-2.5-flash-lite"
    
    # Test invalid format
    with pytest.raises(ValueError, match="Model must include provider prefix"):
        client._detect_provider("invalid-format")


def test_vision_capability_detection():
    """Test vision capability detection"""
    from united_llm import LLMClient
    
    config = {
        "api_keys": {"openrouter": "test", "ollama": None},
        "base_urls": {"openrouter": "https://openrouter.ai/api/v1", "ollama": "http://localhost:11434/v1"},
        "log_dir": "logs"
    }
    
    client = LLMClient(config_dict=config)
    
    # Test vision-capable models
    assert client.is_vision_capable("openrouter:google/gemini-2.5-flash-lite") == True
    assert client.is_vision_capable("openrouter:anthropic/claude-3-5-sonnet") == True
    
    # Test non-vision models
    assert client.is_vision_capable("ollama:qwen3:8b") == False


def test_image_input_creation():
    """Test ImageInput creation with valid base64 data"""
    from united_llm.utils.image_input import ImageInput
    
    # Valid base64 data (1x1 pixel PNG)
    test_b64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/PchI7wAAAABJRU5ErkJggg=="
    
    img = ImageInput(test_b64, name="test_image")
    assert img.name == "test_image"
    assert img._original_data == test_b64
    assert img.base64_data == test_b64
    assert img.mime_type == "image/jpeg"  # Default fallback


def test_pydantic_models():
    """Test that Pydantic models work correctly"""
    from pydantic import BaseModel
    
    class TestModel(BaseModel):
        name: str
        age: int
        active: bool = True
    
    # Test model creation
    model = TestModel(name="Test", age=25)
    assert model.name == "Test"
    assert model.age == 25
    assert model.active == True
    
    # Test model validation
    with pytest.raises(Exception):  # Should raise validation error
        TestModel(name="Test", age="invalid")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
