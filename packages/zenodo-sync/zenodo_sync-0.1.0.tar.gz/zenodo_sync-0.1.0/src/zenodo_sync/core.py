"""Core functionality for zenodo-sync."""

from typing import Dict, List, Optional, Any
import os
from pathlib import Path

from .exceptions import ZenodoSyncError, ZenodoSyncConfigError


class ZenodoSync:
    """Main class for synchronizing data with Zenodo."""

    def __init__(
        self,
        token: Optional[str] = None,
        sandbox: bool = True,
        base_url: Optional[str] = None,
    ) -> None:
        """
        Initialize ZenodoSync.

        Args:
            token: Zenodo API token. If None, will try to get from environment.
            sandbox: Whether to use Zenodo sandbox (default: True for safety).
            base_url: Custom base URL for Zenodo API.
        """
        self.token = token or os.getenv("ZENODO_TOKEN")
        self.sandbox = sandbox
        
        if base_url:
            self.base_url = base_url
        elif sandbox:
            self.base_url = "https://sandbox.zenodo.org/api"
        else:
            self.base_url = "https://zenodo.org/api"
        
        if not self.token:
            raise ZenodoSyncConfigError(
                "Zenodo API token is required. Set ZENODO_TOKEN environment variable "
                "or pass token parameter."
            )

    def upload_file(self, file_path: Path, deposition_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Upload a file to Zenodo.

        Args:
            file_path: Path to the file to upload.
            deposition_id: Zenodo deposition ID. If None, creates a new deposition.

        Returns:
            Dictionary containing upload information.

        Raises:
            ZenodoSyncError: If upload fails.
        """
        # Placeholder implementation
        raise NotImplementedError("File upload functionality coming soon")

    def download_file(self, record_id: str, output_dir: Path) -> List[Path]:
        """
        Download files from a Zenodo record.

        Args:
            record_id: Zenodo record ID.
            output_dir: Directory to save downloaded files.

        Returns:
            List of paths to downloaded files.

        Raises:
            ZenodoSyncError: If download fails.
        """
        # Placeholder implementation
        raise NotImplementedError("File download functionality coming soon")

    def sync_directory(
        self,
        local_dir: Path,
        record_id: Optional[str] = None,
        exclude_patterns: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """
        Synchronize a local directory with Zenodo.

        Args:
            local_dir: Path to local directory to sync.
            record_id: Existing Zenodo record ID. If None, creates new record.
            exclude_patterns: Glob patterns for files to exclude.

        Returns:
            Dictionary containing sync results.

        Raises:
            ZenodoSyncError: If sync fails.
        """
        # Placeholder implementation
        raise NotImplementedError("Directory sync functionality coming soon")

    def get_version(self) -> str:
        """Get the current version of zenodo-sync."""
        from . import __version__
        return __version__