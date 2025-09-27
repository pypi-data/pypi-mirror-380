"""Unit tests for configuration module."""

import json
from pathlib import Path

import pytest

from kitech_repository.lib.config import Config, get_config


def test_config_defaults():
    """Test configuration with default values."""
    config = Config()

    assert config.api_base_url == "https://kitech-manufacturing-api.wimcorp.dev/v1"
    assert config.api_token is None
    assert config.config_dir == Path.home() / ".kitech"
    assert config.download_dir == Path.cwd() / "downloads"
    assert config.timeout == 30
    assert config.max_retries == 3
    assert config.chunk_size == 8192


def test_config_custom_values():
    """Test configuration with custom values."""
    config = Config(
        api_base_url="https://custom.api.com",
        api_token="kt_custom_token",
        timeout=60,
        max_retries=5,
    )

    assert config.api_base_url == "https://custom.api.com"
    assert config.api_token == "kt_custom_token"
    assert config.timeout == 60
    assert config.max_retries == 5


def test_config_save_and_load(temp_config_dir):
    """Test saving and loading configuration."""
    config = Config(
        api_base_url="https://test.api.com",
        api_token="kt_test_token",
        config_dir=temp_config_dir,
    )

    config.save()
    config_file = temp_config_dir / "config.json"
    assert config_file.exists()

    data = json.loads(config_file.read_text())
    assert data["api_base_url"] == "https://test.api.com"
    assert data["api_token"] == "kt_test_token"


def test_config_load_from_file(temp_config_dir, monkeypatch):
    """Test loading configuration from existing file."""
    config_data = {
        "api_base_url": "https://loaded.api.com",
        "api_token": "kt_loaded_token",
        "timeout": 45,
    }

    config_file = temp_config_dir / "config.json"
    config_file.write_text(json.dumps(config_data))

    monkeypatch.setattr(Path, "home", lambda: temp_config_dir.parent)

    loaded_config = Config.load()
    assert loaded_config.api_base_url == "https://loaded.api.com"
    assert loaded_config.api_token == "kt_loaded_token"
    assert loaded_config.timeout == 45


def test_get_config(monkeypatch, temp_config_dir):
    """Test get_config utility function."""
    monkeypatch.setattr(Path, "home", lambda: temp_config_dir.parent)

    config = get_config()
    assert isinstance(config, Config)
    assert config.api_base_url == "https://kitech-manufacturing-api.wimcorp.dev/v1"