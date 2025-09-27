"""Pytest configuration and fixtures."""

import pytest
from pathlib import Path
import tempfile
import json
from unittest.mock import MagicMock, patch

from kitech_repository.lib.config import Config
from kitech_repository.lib.auth import AuthManager
from kitech_repository.lib.client import KitechClient


@pytest.fixture
def temp_config_dir():
    """Create a temporary config directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def test_config(temp_config_dir):
    """Create a test configuration."""
    config = Config(
        api_base_url="https://test.api.com/v1",
        config_dir=temp_config_dir,
        download_dir=temp_config_dir / "downloads",
        timeout=10,
    )
    return config


@pytest.fixture
def test_auth_manager(test_config):
    """Create a test auth manager."""
    return AuthManager(config=test_config)


@pytest.fixture
def test_token():
    """Provide a test token."""
    return "kt_test_token_1234567890abcdef"


@pytest.fixture
def mock_client():
    """Create a mock KITECH client."""
    with patch("kitech_repository.lib.client.httpx.Client") as mock_httpx:
        client = KitechClient()
        client.client = MagicMock()
        yield client


@pytest.fixture
def sample_repository():
    """Provide sample repository data."""
    return {
        "id": 123,
        "name": "test-repo",
        "description": "Test repository",
        "isPublic": True,
        "ownerId": "user-123",
        "ownerName": "Test User",
        "createdAt": "2024-01-01T00:00:00",
        "updatedAt": "2024-01-01T00:00:00",
    }


@pytest.fixture
def sample_file():
    """Provide sample file data."""
    return {
        "name": "test.csv",
        "path": "/data/test.csv",
        "size": 1024,
        "isDirectory": False,
        "lastModified": "2024-01-01T00:00:00",
    }