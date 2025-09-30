# Indexes resource - handles all index-related operations  
from typing import List
from aspect_sdk._generated import (
    IndexesApi,
    Configuration,
    IndexListResponse,
    IndexGetResponse,
    IndexCreateRequest,
    IndexUpdateRequest,
    IndexCreateResponse,
    IndexUpdateResponse,
    ApiClient,
)


class Indexes:
    """Indexes resource class for handling index operations"""
    
    def __init__(self, config: Configuration):
        api_client = ApiClient(config)
        self._api = IndexesApi(api_client)
    
    def get_all(self) -> List[IndexListResponse]:
        """
        Get all indexes
        
        Returns:
            List of index schemas
        """
        return self._api.get_indexes_indexes()
    
    def create(self, data: IndexCreateRequest) -> IndexCreateResponse:
        """
        Create a new index
        
        Args:
            data: The index creation data
            
        Returns:
            The created index schema
        """
        return self._api.post_indexes_indexes(data)
    
    def get(self, index_id: str) -> IndexGetResponse:
        """
        Get an index by ID
        
        Args:
            index_id: The ID of the index
            
        Returns:
            The index schema
        """
        return self._api.get_indexes_indexes_index_id(index_id)
    
    def update(
        self, 
        index_id: str, 
        data: IndexUpdateRequest
    ) -> IndexUpdateResponse:
        """
        Update an index
        
        Args:
            index_id: The ID of the index
            data: The update data
            
        Returns:
            The updated index schema
        """
        return self._api.put_indexes_indexes_index_id(
            index_id,
            data,
        )
    
    def delete(self, index_id: str) -> None:
        """
        Delete an index
        
        Args:
            index_id: The ID of the index to delete
        """
        self._api.delete_indexes_indexes_index_id(index_id)
