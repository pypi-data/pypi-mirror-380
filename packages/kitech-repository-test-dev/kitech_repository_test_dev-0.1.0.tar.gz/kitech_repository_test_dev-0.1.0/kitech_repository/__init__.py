"""KITECH Manufacturing Data Repository Library and CLI."""

__version__ = "0.1.0"
__author__ = "KITECH Repository Team"

from kitech_repository.lib.client import KitechClient
from kitech_repository.lib.auth import AuthManager
from kitech_repository.lib.config import Config

# Convenience functions for library usage
def download(repository_id: int, path: str = "", output_dir: str = None, token: str = None):
    """Download a file or directory from repository.

    Args:
        repository_id: The repository ID
        path: Path within repository (empty string for root)
        output_dir: Local output directory (None for default)
        token: API token (None to use stored token)

    Returns:
        Path: Path to downloaded file/directory
    """
    with KitechClient(token=token) as client:
        return client.download_file(
            repository_id=repository_id,
            path=path if path else None,
            output_dir=output_dir,
            show_progress=True
        )

def upload(repository_id: int, file_path: str, remote_path: str = "", token: str = None):
    """Upload a file to repository.

    Args:
        repository_id: The repository ID
        file_path: Local file path to upload
        remote_path: Remote path within repository (empty string for root)
        token: API token (None to use stored token)

    Returns:
        dict: Upload response data
    """
    from pathlib import Path
    with KitechClient(token=token) as client:
        return client.upload_file(
            repository_id=repository_id,
            file_path=Path(file_path),
            remote_path=remote_path,
            show_progress=True
        )

def list_repositories(token: str = None):
    """List available repositories.

    Args:
        token: API token (None to use stored token)

    Returns:
        list: List of Repository objects
    """
    with KitechClient(token=token) as client:
        result = client.list_repositories()
        return result["repositories"]

def list_files(repository_id: int, path: str = "", token: str = None, page: int = 0, limit: int = 100):
    """List files in repository.

    Args:
        repository_id: The repository ID
        path: Path within repository (empty string for root)
        token: API token (None to use stored token)
        page: Page number (default: 0)
        limit: Number of files per page (default: 100)

    Returns:
        dict: Dictionary containing 'files' list and pagination metadata
    """
    with KitechClient(token=token) as client:
        return client.list_files(repository_id, prefix=path if path else "", page=page, limit=limit)

# Export main classes and functions
__all__ = [
    "KitechClient",
    "AuthManager",
    "Config",
    "download",
    "upload",
    "list_repositories",
    "list_files"
]