"""COB AI - Python client for COB SharePoint search."""

from .client import COB
from .models import (
    SearchResponse, SearchResult, NENTagResponse,
    SyncStatusResponse, FailedDocumentInfo, SyncStartResponse
)

__version__ = "0.1.5"
__all__ = [
    "COB", "SearchResponse", "SearchResult", "NENTagResponse",
    "SyncStatusResponse", "FailedDocumentInfo", "SyncStartResponse"
]