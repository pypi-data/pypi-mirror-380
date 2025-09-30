# __init__.py
"""
MFDev SDK

A lightweight scraping and data processing toolkit with:
- Robust HTTP request handling
- Custom error management
- Data cleaning utilities
- CSV/Excel export helpers
"""

__version__ = "0.1.6"
__author__ = "Miguel Fernandez"
__license__ = "MIT"

# Expose main classes
from .library import MFDevScraper

# Expose custom errors at top-level
from .errors import (
    MFDevError,
    ConfigurationError,
    RequestError,
    HTTPStatusError,
    MaxRetriesExceeded,
    InvalidResponseError,
    DataValidationError,
    MissingFieldError,
    NotADictError,
    FileIOError,
    CSVWriteError,
    ExcelWriteError,
)

__all__ = [
    "MFDevScraper",
    # Errors
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
