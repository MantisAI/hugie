import os

from pydantic import BaseModel


class Settings(BaseModel):
    """Core settings."""

    base_url: str = "https://api.endpoints.huggingface.cloud"
    endpoint_url: str = f"{base_url}/endpoint"
    provider_url: str = f"{base_url}/provider"
    token: str = os.getenv("HUGGINGFACE_READ_TOKEN")
