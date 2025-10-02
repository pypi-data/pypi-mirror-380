"""Tests for the core ZenodoSync functionality."""

import os
import pytest
from unittest.mock import patch

from zenodo_sync import ZenodoSync, ZenodoSyncError
from zenodo_sync.exceptions import ZenodoSyncConfigError


class TestZenodoSync:
    """Test cases for ZenodoSync class."""

    def test_init_with_token(self, sample_token):
        """Test initialization with explicit token."""
        sync = ZenodoSync(token=sample_token, sandbox=True)
        assert sync.token == sample_token
        assert sync.sandbox is True
        assert "sandbox" in sync.base_url

    def test_init_with_production(self, sample_token):
        """Test initialization with production mode."""
        sync = ZenodoSync(token=sample_token, sandbox=False)
        assert sync.sandbox is False
        assert "sandbox" not in sync.base_url
        assert sync.base_url == "https://zenodo.org/api"

    @patch.dict(os.environ, {"ZENODO_TOKEN": "env-token-123"})
    def test_init_with_env_token(self):
        """Test initialization with token from environment."""
        sync = ZenodoSync(sandbox=True)
        assert sync.token == "env-token-123"

    def test_init_no_token_raises_error(self):
        """Test initialization without token raises error."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ZenodoSyncConfigError, match="Zenodo API token is required"):
                ZenodoSync(sandbox=True)

    def test_custom_base_url(self, sample_token):
        """Test initialization with custom base URL."""
        custom_url = "https://custom.zenodo.org/api"
        sync = ZenodoSync(token=sample_token, base_url=custom_url)
        assert sync.base_url == custom_url

    def test_get_version(self, mock_zenodo_sync):
        """Test getting version."""
        version = mock_zenodo_sync.get_version()
        assert isinstance(version, str)
        assert "." in version  # Should be in semver format

    def test_upload_file_not_implemented(self, mock_zenodo_sync, sample_file):
        """Test that upload_file raises NotImplementedError."""
        with pytest.raises(NotImplementedError, match="File upload functionality coming soon"):
            mock_zenodo_sync.upload_file(sample_file)

    def test_download_file_not_implemented(self, mock_zenodo_sync, temp_dir):
        """Test that download_file raises NotImplementedError."""
        with pytest.raises(NotImplementedError, match="File download functionality coming soon"):
            mock_zenodo_sync.download_file("12345", temp_dir)

    def test_sync_directory_not_implemented(self, mock_zenodo_sync, temp_dir):
        """Test that sync_directory raises NotImplementedError."""
        with pytest.raises(NotImplementedError, match="Directory sync functionality coming soon"):
            mock_zenodo_sync.sync_directory(temp_dir)