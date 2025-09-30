# Assets resource - handles all asset-related operations
import os
from pathlib import Path
from typing import List
from typing import IO, Optional, Union
from pydantic.main import BaseModel

from aspect_sdk._generated import (
    AssetsApi,
    Configuration,
    AssetGetResponse,
    AssetCreateResponse,
    AssetDownloadGetResponse,
    AssetUpdateRequest,
    AssetUpdateResponse,
    AssetListResponse,
    ApiClient,
    CoreFeatureType,
)


FileInput = Union[str, os.PathLike[str], bytes]


# Asset create request
class AssetCreateRequest(BaseModel):
    index_id: str
    save_original: bool
    id: Optional[str] = None
    features: Optional[List[CoreFeatureType]] = None
    asset_file: Optional[FileInput] = None
    asset_url: Optional[str] = None
    name: str


class Assets:
    """Assets resource class for handling asset operations"""
    
    def __init__(self, config: Configuration):
        api_client = ApiClient(config)
        self._api = AssetsApi(api_client)
    
    def get_all(self, index_id: str) -> List[AssetListResponse]:
        """
        Get all assets for an index
        
        Args:
            index_id: The ID of the index
            
        Returns:
            List of asset schemas
        """
        return self._api.get_assets_assets(
            index_id=index_id,
        )
    
    def get(self, asset_id: str) -> AssetGetResponse:
        """
        Get a specific asset by ID
        
        Args:
            asset_id: The ID of the asset
            
        Returns:
            The asset schema
        """
        return self._api.get_assets_assets_asset_id(
            asset_id=asset_id,
        )

    def create(self, data: AssetCreateRequest) -> AssetCreateResponse:
        """
        Create an asset
        
        Args:
            data: The asset creation data
            
        Returns:
            The created asset schema
        """
        processed_asset_file = None
        if data.asset_file:
            processed_asset_file = self._read_file(data.asset_file)
        
        return self._api.post_assets_assets(
            index_id=data.index_id,
            save_original=data.save_original,
            name=data.name,
            id=data.id,
            features=data.features,
            asset_file=processed_asset_file,
            asset_url=data.asset_url,
        )
    
    def update(
        self,
        asset_id: str,
        update_data: AssetUpdateRequest,
    ) -> AssetUpdateResponse:
        """
        Update an asset
        
        Args:
            asset_id: The ID of the asset
            update_data: The update data
            
        Returns:
            The updated asset schema
        """
        return self._api.put_assets_assets_asset_id(
            asset_id,
            update_data,
        )
    
    def delete(self, asset_id: str) -> None:
        """
        Delete an asset
        
        Args:
            asset_id: The ID of the asset to delete
        """
        self._api.delete_assets_assets_asset_id(
            asset_id,
        )
    
    def get_download_data(
        self,
        asset_id: str,
    ) -> AssetDownloadGetResponse:
        """
        Get download data for an asset
        
        Args:
            asset_id: The ID of the asset
            storage_entity_type: The type of storage entity
            
        Returns:
            The asset download data
        """
        return self._api.get_assets_assets_asset_id_download(
            asset_id,
        )

    def _read_file(self, file: FileInput) -> bytes:
        """
        Read a file from various input types
        
        Args:
            file: The file input - can be path string, pathlib.Path, bytes, bytearray, or file-like object

        Returns:
            The file content as bytes
        """
        if isinstance(file, (str, os.PathLike)):
            # Handle file paths - read and return content
            file_path = Path(file)
            with file_path.open("rb") as file_handle:
                return file_handle.read()
        elif isinstance(file, (bytes, bytearray)):
            # Handle raw bytes - return as-is
            return bytes(file)
        elif hasattr(file, "read"):
            # Handle file-like objects - read content but don't close (caller owns it)
            if hasattr(file, "seek"):
                file.seek(0)  # Reset to beginning if seekable
            return file.read()
        else:
            raise TypeError(
                f"Unsupported file input type: {type(file).__name__}. "
                "file must be a file path (str or pathlib.Path), bytes/bytearray, or a binary file-like object"
            )
