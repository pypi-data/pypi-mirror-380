# errors.py
"""
Custom exceptions for the MFDev SDK.

Use these classes to signal specific errors:
- Configuration and preconditions (ConfigurationError)
- HTTP requests (RequestError, HTTPStatusError, MaxRetriesExceeded, InvalidResponseError)
- Data validation (DataValidationError, MissingFieldError, NotADictError)
- File operations (FileIOError, CSVWriteError, ExcelWriteError)
"""

from typing import Optional


class MFDevError(Exception):
    """Base exception for all MFDev SDK errors."""
    pass


# --- Configuration / Preconditions --------------------------------------------------

class ConfigurationError(MFDevError):
    """Raised when an invalid configuration or missing parameter is detected."""
    pass


# --- Requests / Networking ----------------------------------------------------------

class RequestError(MFDevError):
    """Generic request error (network, timeouts, TLS, etc.)."""
    def __init__(self, message: str, url: Optional[str] = None):
        self.url = url
        super().__init__(message)


class HTTPStatusError(RequestError):
    """Raised when the server responds with a non-accepted HTTP status code."""
    def __init__(self, status_code: int, message: Optional[str] = None, url: Optional[str] = None):
        self.status_code = status_code
        msg = message or f"HTTP status not accepted: {status_code}"
        super().__init__(msg, url=url)


class MaxRetriesExceeded(RequestError):
    """Raised when the maximum number of retries has been exceeded."""
    def __init__(self, retries: int, url: Optional[str] = None):
        self.retries = retries
        super().__init__(f"Maximum retries reached ({retries}).", url=url)


class InvalidResponseError(RequestError):
    """Raised when the response does not meet the expected format or conditions."""
    pass


# --- Data Validation ---------------------------------------------------------------

class DataValidationError(MFDevError):
    """Generic error for data validation failures."""
    pass


class MissingFieldError(DataValidationError):
    """Raised when a required field is missing in a record."""
    def __init__(self, field: str, index: Optional[int] = None):
        self.field = field
        self.index = index
        msg = f"Missing required field '{field}'"
        if index is not None:
            msg += f" at position {index}"
        super().__init__(msg)


class NotADictError(DataValidationError):
    """Raised when a dictionary was expected but another type was provided."""
    def __init__(self, index: Optional[int] = None):
        self.index = index
        msg = "Item is not a dictionary"
        if index is not None:
            msg += f" (at position {index})"
        super().__init__(msg)


# --- File Operations / Export -------------------------------------------------------

class FileIOError(MFDevError):
    """Generic file input/output error."""
    pass


class CSVWriteError(FileIOError):
    """Raised when writing a CSV file fails."""
    def __init__(self, path: str, reason: Optional[str] = None):
        self.path = path
        msg = f"Failed to write CSV file at: {path}"
        if reason:
            msg += f". Reason: {reason}"
        super().__init__(msg)


class ExcelWriteError(FileIOError):
    """Raised when writing an Excel file fails."""
    def __init__(self, path: str, reason: Optional[str] = None):
        self.path = path
        msg = f"Failed to write Excel file at: {path}"
        if reason:
            msg += f". Reason: {reason}"
        super().__init__(msg)


__all__ = [
    "MFDevError",
    "ConfigurationError",
    "RequestError",
    "HTTPStatusError",
    "MaxRetriesExceeded",
    "InvalidResponseError",
    "DataValidationError",
    "MissingFieldError",
    "NotADictError",
    "FileIOError",
    "CSVWriteError",
    "ExcelWriteError",
]
