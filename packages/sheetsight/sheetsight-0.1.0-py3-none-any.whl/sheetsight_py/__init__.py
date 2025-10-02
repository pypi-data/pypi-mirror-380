"""
Sheetsight Python Client - Simple client for the Sheetsight search API
"""

from .client import SheetsightClient
from .types import (
    GlobalSearchOptions,
    GlobalSearchResponse,
    GlobalSearchMatch,
    PartSearchGroup,
    SearchDatasheet,
    SearchChapter,
    SearchPart,
    SearchManufacturer,
)
from .exceptions import (
    SheetsightError,
    AuthenticationError,
    APIError,
    TimeoutError,
)

__version__ = "0.1.0"
__all__ = [
    "SheetsightClient",
    "GlobalSearchOptions",
    "GlobalSearchResponse", 
    "GlobalSearchMatch",
    "PartSearchGroup",
    "SearchDatasheet",
    "SearchChapter",
    "SearchPart",
    "SearchManufacturer",
    "SheetsightError",
    "AuthenticationError",
    "APIError",
    "TimeoutError",
]


