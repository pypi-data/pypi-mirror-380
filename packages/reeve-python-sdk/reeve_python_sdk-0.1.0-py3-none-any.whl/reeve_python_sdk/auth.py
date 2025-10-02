"""
Authentication module for the Reeve Python SDK.
"""

from typing import Dict

from .client import BaseClient


class AuthModule:
    """Handles authentication operations with the Reeve API."""

    def __init__(self, client: BaseClient):
        """
        Initialize the Auth module.

        Args:
            client: Base HTTP client instance
        """
        self.client = client

    async def get_token(self) -> Dict:
        """
        Get authentication token.

        Returns:
            Token response from the API

        Example:
            >>> async with ReeveClient(api_url="https://api.reeve.example.com") as client:
            ...     token = await client.auth.get_token()
        """
        return await self.client.get("/Auth/token")
