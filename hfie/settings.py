import os

from pydantic import BaseModel


class Settings(BaseModel):
    """Core settings."""

    base_url = "https://api.endpoints.huggingface.cloud"
    endpoint_url = f"{base_url}/endpoint"
    provider_url = f"{base_url}/provider"
    token = os.getenv("TOKEN")
