# Users resource - handles all user-related operations
from aspect_sdk._generated import (
    UsersApi,
    Configuration,
    UserGetResponse,
    ApiClient,
)


class Users:
    """Users resource class for handling user operations"""
    
    def __init__(self, config: Configuration):
        api_client = ApiClient(config)
        self._api = UsersApi(api_client)
    
    def get_current_user(self) -> UserGetResponse:
        """
        Get current user information
        
        Returns:
            The current user schema
        """
        return self._api.get_users_users_me()
    
    def me(self) -> UserGetResponse:
        """
        Alias for get_current_user
        
        Returns:
            The current user schema
        """
        return self.get_current_user()
