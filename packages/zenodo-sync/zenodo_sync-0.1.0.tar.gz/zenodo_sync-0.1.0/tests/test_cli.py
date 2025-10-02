"""Tests for CLI functionality."""

import pytest
from click.testing import CliRunner
from unittest.mock import patch, Mock

from zenodo_sync.cli import cli, main


class TestCLI:
    """Test cases for CLI commands."""

    def setup_method(self):
        """Set up test fixtures."""
        self.runner = CliRunner()

    def test_cli_version(self):
        """Test CLI version command."""
        result = self.runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert "version" in result.output.lower()

    def test_cli_help(self):
        """Test CLI help command."""
        result = self.runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "zenodo-sync" in result.output
        assert "Synchronize research data with Zenodo" in result.output

    @patch("zenodo_sync.cli.ZenodoSync")
    def test_upload_command(self, mock_zenodo_class, sample_file):
        """Test upload command."""
        mock_sync = Mock()
        mock_sync.upload_file.return_value = {"status": "success"}
        mock_zenodo_class.return_value = mock_sync

        result = self.runner.invoke(
            cli,
            ["--token", "test-token", "upload", str(sample_file)],
            catch_exceptions=False,
        )
        
        assert result.exit_code == 0
        mock_zenodo_class.assert_called_once_with(token="test-token", sandbox=True)
        mock_sync.upload_file.assert_called_once()

    @patch("zenodo_sync.cli.ZenodoSync")
    def test_download_command(self, mock_zenodo_class, temp_dir):
        """Test download command."""
        mock_sync = Mock()
        mock_sync.download_file.return_value = ["file1.txt", "file2.txt"]
        mock_zenodo_class.return_value = mock_sync

        result = self.runner.invoke(
            cli,
            ["--token", "test-token", "download", "12345", str(temp_dir)],
            catch_exceptions=False,
        )
        
        assert result.exit_code == 0
        mock_zenodo_class.assert_called_once_with(token="test-token", sandbox=True)
        mock_sync.download_file.assert_called_once()

    @patch("zenodo_sync.cli.ZenodoSync")
    def test_sync_command(self, mock_zenodo_class, temp_dir):
        """Test sync command."""
        mock_sync = Mock()
        mock_sync.sync_directory.return_value = {"status": "success"}
        mock_zenodo_class.return_value = mock_sync

        result = self.runner.invoke(
            cli,
            ["--token", "test-token", "sync", str(temp_dir)],
            catch_exceptions=False,
        )
        
        assert result.exit_code == 0
        mock_zenodo_class.assert_called_once_with(token="test-token", sandbox=True)
        mock_sync.sync_directory.assert_called_once()

    def test_main_function(self):
        """Test main entry point function."""
        with patch("zenodo_sync.cli.cli") as mock_cli:
            main()
            mock_cli.assert_called_once()