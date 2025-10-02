"""Custom exceptions for zenodo-sync."""


class ZenodoSyncError(Exception):
    """Base exception class for zenodo-sync."""

    pass


class ZenodoAPIError(ZenodoSyncError):
    """Exception raised when Zenodo API returns an error."""

    def __init__(self, message: str, status_code: int = None) -> None:
        super().__init__(message)
        self.status_code = status_code


class ZenodoAuthenticationError(ZenodoSyncError):
    """Exception raised when authentication with Zenodo fails."""

    pass


class ZenodoSyncConfigError(ZenodoSyncError):
    """Exception raised when configuration is invalid."""

    pass


class ZenodoSyncFileError(ZenodoSyncError):
    """Exception raised when file operations fail."""

    pass