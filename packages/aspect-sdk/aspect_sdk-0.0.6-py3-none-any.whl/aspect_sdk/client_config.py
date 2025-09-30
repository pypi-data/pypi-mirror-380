# Types for the user-facing SDK
from typing import Optional
from pydantic import BaseModel, Field


class AspectConfig(BaseModel):
    """Configuration for the Aspect Media Engine SDK client"""
    
    api_key: str = Field(..., description="API key for authentication")
    base_url: Optional[str] = Field(
        default="https://api.aspect.inc",
        description="Base URL for the Aspect API"
    )
    timeout: Optional[float] = Field(
        default=30.0,
        description="Request timeout in seconds"
    )