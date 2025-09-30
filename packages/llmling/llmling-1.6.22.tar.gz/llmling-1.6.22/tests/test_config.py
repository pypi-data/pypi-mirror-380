"""Tests for configuration handling in LLMling."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import pydantic
import pytest
from upath import UPath
import yamling

from llmling import config, config_resources
from llmling.config.models import Config
from llmling.processors.base import ProcessorConfig


if TYPE_CHECKING:
    import os


MINIMAL_CONFIG = """
version: "1.0"
global_settings:
  timeout: 30
  max_retries: 3
resources:
  test-context:
    type: text
    content: test content
    description: test description
context_processors: {}
resource_groups: {}
"""


@pytest.fixture
def valid_config_dict() -> dict[str, Any]:
    """Create a valid configuration dictionary for testing."""
    return yamling.load_yaml_file(config_resources.TEST_CONFIG)


@pytest.fixture
def minimal_config_dict() -> dict[str, Any]:
    """Create a minimal valid configuration dictionary."""
    return yamling.load_yaml(MINIMAL_CONFIG)


def test_load_valid_config(valid_config_dict: dict[str, Any]) -> None:
    """Test loading a valid configuration."""
    cfg = config.Config.model_validate(valid_config_dict)
    assert cfg.version == "1.0"
    assert isinstance(cfg.global_settings, config.GlobalSettings)


def test_load_minimal_config(minimal_config_dict: dict[str, Any]) -> None:
    """Test loading a minimal valid configuration."""
    cfg = config.Config.model_validate(minimal_config_dict)
    assert cfg.version == "1.0"
    assert len(cfg.resources) == 1


def test_processor_config_structure() -> None:
    """Test processor config structural validation."""
    # Test invalid type
    with pytest.raises(pydantic.ValidationError):
        ProcessorConfig(type="invalid")  # type: ignore

    # Test valid types with empty strings (now allowed)
    proc = ProcessorConfig(import_path="test")
    assert proc.import_path == "test"

    # Test setting values
    proc = ProcessorConfig(import_path="test.func", async_execution=True)
    assert proc.import_path == "test.func"
    assert proc.async_execution


def test_processor_config_defaults() -> None:
    """Test processor config default values."""
    proc = ProcessorConfig(import_path="test")
    assert proc.name is None
    assert proc.description is None
    assert proc.import_path == "test"
    assert not proc.async_execution
    assert proc.metadata == {}


def test_validate_source_context() -> None:
    """Test validation of source context configurations."""
    invalid = {"type": "source", "import_path": "invalid.1path", "description": "test"}
    with pytest.raises(pydantic.ValidationError) as exc_info:
        config.SourceResource.model_validate(invalid)
    assert "Invalid import path" in str(exc_info.value)

    valid = {"type": "source", "import_path": "valid.path", "description": "test"}
    ctx = config.SourceResource.model_validate(valid)
    assert ctx.import_path == "valid.path"


def test_validate_callable_context() -> None:
    """Test validation of callable context configurations."""
    invalid = {"type": "callable", "import_path": "invalid.1path", "description": "test"}
    with pytest.raises(pydantic.ValidationError) as exc_info:
        config.CallableResource.model_validate(invalid)
    assert "Invalid import path" in str(exc_info.value)

    valid = {"type": "callable", "import_path": "valid.path", "description": "test"}
    ctx = config.CallableResource.model_validate(valid)
    assert ctx.import_path == "valid.path"


def test_load_config_from_file(tmp_path: os.PathLike[str]) -> None:
    """Test loading configuration from a file."""
    config_path = UPath(tmp_path) / "test_config.yml"
    config_path.write_text(MINIMAL_CONFIG)

    cfg = config.Config.from_file(config_path)
    assert isinstance(cfg, config.Config)
    assert cfg.version == "1.0"
    assert "test-context" in cfg.resources


def test_schema_generation():
    """Test that JSON schema can be generated from config models."""
    try:
        _schema = Config.model_json_schema()
    except Exception as exc:  # noqa: BLE001
        pytest.fail(f"Failed to generate schema: {exc}")


if __name__ == "__main__":
    pytest.main([__file__])
