"""Tests for custom exceptions."""

import pytest

from zenodo_sync.exceptions import (
    ZenodoSyncError,
    ZenodoAPIError,
    ZenodoAuthenticationError,
    ZenodoSyncConfigError,
    ZenodoSyncFileError,
)


class TestExceptions:
    """Test cases for custom exceptions."""

    def test_base_exception(self):
        """Test base ZenodoSyncError exception."""
        error = ZenodoSyncError("Test error message")
        assert str(error) == "Test error message"
        assert isinstance(error, Exception)

    def test_api_error_with_status_code(self):
        """Test ZenodoAPIError with status code."""
        error = ZenodoAPIError("API error", status_code=404)
        assert str(error) == "API error"
        assert error.status_code == 404
        assert isinstance(error, ZenodoSyncError)

    def test_api_error_without_status_code(self):
        """Test ZenodoAPIError without status code."""
        error = ZenodoAPIError("API error")
        assert str(error) == "API error"
        assert error.status_code is None

    def test_authentication_error(self):
        """Test ZenodoAuthenticationError."""
        error = ZenodoAuthenticationError("Authentication failed")
        assert str(error) == "Authentication failed"
        assert isinstance(error, ZenodoSyncError)

    def test_config_error(self):
        """Test ZenodoSyncConfigError."""
        error = ZenodoSyncConfigError("Configuration error")
        assert str(error) == "Configuration error"
        assert isinstance(error, ZenodoSyncError)

    def test_file_error(self):
        """Test ZenodoSyncFileError."""
        error = ZenodoSyncFileError("File operation failed")
        assert str(error) == "File operation failed"
        assert isinstance(error, ZenodoSyncError)

    def test_exception_hierarchy(self):
        """Test that all custom exceptions inherit from base exception."""
        exceptions = [
            ZenodoAPIError("test"),
            ZenodoAuthenticationError("test"),
            ZenodoSyncConfigError("test"),
            ZenodoSyncFileError("test"),
        ]
        
        for exc in exceptions:
            assert isinstance(exc, ZenodoSyncError)
            assert isinstance(exc, Exception)