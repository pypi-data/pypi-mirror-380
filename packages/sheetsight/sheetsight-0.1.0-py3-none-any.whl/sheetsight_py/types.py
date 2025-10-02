"""
Type definitions for Sheetsight API responses and requests
"""

from typing import Dict, List, Optional, TypedDict


class SearchChapter(TypedDict):
    """Chapter information for search results"""
    id: str
    title: str
    startPage: int
    endPage: int


class SearchDatasheet(TypedDict):
    """Datasheet information for search results"""
    id: str
    filename: str
    description: str
    pdfUrl: str
    status: str
    numPages: Optional[int]
    manufacturerId: str


class SearchPart(TypedDict):
    """Part information for search results"""
    id: str
    partNumber: str
    manufacturerId: str
    partTypeId: Optional[str]
    description: Optional[str]
    productPage: Optional[str]
    status: str


class SearchManufacturer(TypedDict):
    """Manufacturer information for search results"""
    id: str
    displayName: str
    website: Optional[str]
    approvedDomains: Optional[List[str]]


class GlobalSearchMatch(TypedDict):
    """Individual search match result"""
    id: str
    score: float
    datasheet_id: Optional[str]
    page_number: Optional[int]
    chunk_index: Optional[int]
    content: str
    char_count: Optional[int]
    search_method: str
    relevance_score: float
    chapter: Optional[SearchChapter]
    datasheet: Optional[SearchDatasheet]


class PartSearchGroup(TypedDict):
    """Group of search results for a specific part"""
    part: SearchPart
    manufacturer: SearchManufacturer
    matches: List[GlobalSearchMatch]
    totalRelevanceScore: float
    bestMatch: Optional[GlobalSearchMatch]
    matchCount: int


class GlobalSearchMetadata(TypedDict):
    """Metadata about the search operation"""
    vector_search_results: int
    parts_with_matches: int
    avg_matches_per_part: float


class GlobalSearchResponse(TypedDict):
    """Complete response from the global search API"""
    query: str
    total_results: int
    total_parts: int
    processing_time_ms: int
    grouped_results: List[PartSearchGroup]
    metadata: GlobalSearchMetadata


class GlobalSearchOptions(TypedDict, total=False):
    """Options for global search requests"""
    maxResults: int
    maxMatchesPerPart: int
    includePartInfo: bool
    groupByPart: bool


