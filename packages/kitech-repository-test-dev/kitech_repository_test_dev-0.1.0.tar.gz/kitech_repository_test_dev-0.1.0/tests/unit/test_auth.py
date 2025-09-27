"""Unit tests for authentication module."""

import json
import pytest

from kitech_repository.lib.auth import AuthManager


def test_login_success(test_auth_manager, test_token, temp_config_dir):
    """Test successful login."""
    result = test_auth_manager.login(test_token)
    assert result is True

    token_file = temp_config_dir / "token.json"
    assert token_file.exists()

    data = json.loads(token_file.read_text())
    assert data["token"] == test_token


def test_login_invalid_token(test_auth_manager):
    """Test login with invalid token format."""
    with pytest.raises(ValueError, match="Invalid token format"):
        test_auth_manager.login("invalid_token")


def test_logout_success(test_auth_manager, test_token, temp_config_dir):
    """Test successful logout."""
    test_auth_manager.login(test_token)
    assert test_auth_manager.is_authenticated()

    result = test_auth_manager.logout()
    assert result is True
    assert not test_auth_manager.is_authenticated()

    token_file = temp_config_dir / "token.json"
    assert not token_file.exists()


def test_logout_when_not_logged_in(test_auth_manager):
    """Test logout when not authenticated."""
    result = test_auth_manager.logout()
    assert result is False


def test_get_token(test_auth_manager, test_token):
    """Test getting stored token."""
    assert test_auth_manager.get_token() is None

    test_auth_manager.login(test_token)
    assert test_auth_manager.get_token() == test_token


def test_is_authenticated(test_auth_manager, test_token):
    """Test authentication status check."""
    assert test_auth_manager.is_authenticated() is False

    test_auth_manager.login(test_token)
    assert test_auth_manager.is_authenticated() is True

    test_auth_manager.logout()
    assert test_auth_manager.is_authenticated() is False


def test_headers(test_auth_manager, test_token):
    """Test getting authentication headers."""
    with pytest.raises(ValueError, match="Not authenticated"):
        test_auth_manager.headers

    test_auth_manager.login(test_token)
    headers = test_auth_manager.headers

    assert headers["Authorization"] == f"Bearer {test_token}"
    assert headers["Content-Type"] == "application/json"