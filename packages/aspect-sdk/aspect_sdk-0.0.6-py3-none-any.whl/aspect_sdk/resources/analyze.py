# Analyze resource - handles all analyze-related operations
from aspect_sdk._generated import (
    AnalyzeApi,
    Configuration,
    AnalyzeAskRequest,
    AnalyzeAskResponse,
    AnalyzeBoxRequest,
    AnalyzeBoxResponse,
    AnalyzePointRequest,
    AnalyzePointResponse,
    ApiClient,
)


class Analyze:
    """Analyze resource class for handling analysis operations"""
    
    def __init__(self, config: Configuration):
        api_client = ApiClient(config)
        self._api = AnalyzeApi(api_client)
    
    def ask(self, data: AnalyzeAskRequest) -> AnalyzeAskResponse:
        """
        Ask questions about video content
        
        Args:
            data: The ask analysis data
            
        Returns:
            The ask analysis response
        """
        return self._api.post_analyze_analyze_ask(
            data,
        )
    
    def box(self, data: AnalyzeBoxRequest) -> AnalyzeBoxResponse:
        """
        Analyze a box region in video
        
        Args:
            data: The box analysis data
            
        Returns:
            The box analysis response
        """
        return self._api.post_analyze_analyze_box(
            data,
        )
    
    def point(self, data: AnalyzePointRequest) -> AnalyzePointResponse:
        """
        Analyze a point in video
        
        Args:
            data: The point analysis data
            
        Returns:
            The point analysis response
        """
        return self._api.post_analyze_analyze_point(
            data,
        )
