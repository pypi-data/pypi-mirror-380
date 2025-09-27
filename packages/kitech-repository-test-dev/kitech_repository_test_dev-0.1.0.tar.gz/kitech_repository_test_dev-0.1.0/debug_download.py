#!/usr/bin/env python3
"""Debug script to test file download directly."""

import sys
from pathlib import Path
from kitech_repository.lib.client import KitechClient

def test_download():
    """Test downloading the problematic file."""
    try:
        with KitechClient() as client:
            # Test connection first
            print("Testing connection...")
            result = client.test_connection()
            print(f"Connection test result: {result}")

            # List repositories to find one to test with
            print("Listing repositories...")
            repos = client.list_repositories(limit=5)
            if not repos["repositories"]:
                print("No repositories found")
                return

            repo = repos["repositories"][0]
            print(f"Using repository: {repo.name} (ID: {repo.id})")

            # List files in the repository
            print("Listing files...")
            files = client.list_files(repo.id, prefix="", include_hash=False)
            if not files["files"]:
                print("No files found in repository")
                return

            # Find the problematic JPEG file or use first file
            target_file = None
            for file in files["files"]:
                if "360_F_92535664_IvFsQeHjBzfE6sD4VHdO8u5OHUSc6yHF.jpg" in file.path:
                    target_file = file
                    break

            if not target_file:
                target_file = files["files"][0]  # Use first file if JPEG not found

            print(f"Downloading file: {target_file.path}")
            print(f"File size: {target_file.size} bytes")

            # Get download URL first to see what type it is
            download_url = client.get_download_url(repo.id, target_file.path)
            print(f"Download URL: {download_url}")
            print(f"Is presigned URL: {'X-Amz-Algorithm' in download_url}")

            # Download the file
            output_dir = Path("./debug_downloads")
            downloaded_path = client.download_file(
                repository_id=repo.id,
                path=target_file.path,
                output_dir=output_dir,
                show_progress=True
            )

            print(f"Downloaded to: {downloaded_path}")

            if downloaded_path.exists():
                actual_size = downloaded_path.stat().st_size
                print(f"Downloaded file size: {actual_size} bytes")
                print(f"Expected size: {target_file.size} bytes")
                print(f"Size match: {actual_size == target_file.size}")

                # Check file type
                import subprocess
                try:
                    result = subprocess.run(['file', str(downloaded_path)], capture_output=True, text=True)
                    print(f"File type: {result.stdout.strip()}")
                except:
                    print("Could not determine file type")

                # Check first few bytes
                with open(downloaded_path, 'rb') as f:
                    first_bytes = f.read(20)
                    print(f"First 20 bytes (hex): {first_bytes.hex()}")
                    print(f"First 20 bytes (repr): {repr(first_bytes)}")
            else:
                print("Downloaded file does not exist!")

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_download()