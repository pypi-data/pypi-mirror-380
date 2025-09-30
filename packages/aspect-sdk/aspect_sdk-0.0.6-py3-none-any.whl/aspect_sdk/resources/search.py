# Search resource - handles all search-related operations
from typing import Any
from aspect_sdk._generated import (
    SearchApi,
    Configuration,
    ApiClient,
)
from aspect_sdk._generated.models import SearchRequest, SearchResponse


class Search:
    """Search resource class for handling search operations"""
    
    def __init__(self, config: Configuration):
        api_client = ApiClient(config)
        self._api = SearchApi(api_client)
    
    def run(self, request: SearchRequest) -> SearchResponse:
        """
        Search across indexed content
        
        Args:
            parameters: The search query parameters containing index_id and query
            
        Returns:
            Search results
        """
        return self._api.post_search_search_run(request)
