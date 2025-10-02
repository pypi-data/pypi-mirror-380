"""
Subject verification module for the Reeve Python SDK.
"""

from typing import BinaryIO, Dict, Union
import aiohttp

from .client import BaseClient


class SubjectModule:
    """Handles subject face-to-face verification with the Reeve API."""

    def __init__(self, client: BaseClient):
        """
        Initialize the Subject module.

        Args:
            client: Base HTTP client instance
        """
        self.client = client

    async def verify_faces(
        self,
        face1: Union[bytes, BinaryIO, str],
        face2: Union[bytes, BinaryIO, str]
    ) -> Dict:
        """
        Verify if two faces match.

        Args:
            face1: First face image (bytes, file-like object, or base64 string)
            face2: Second face image (bytes, file-like object, or base64 string)

        Returns:
            Verification result from the API

        Example:
            >>> async with ReeveClient(api_url="https://api.reeve.example.com",
            ...                        api_key="token") as client:
            ...     with open("face1.jpg", "rb") as f1, open("face2.jpg", "rb") as f2:
            ...         result = await client.subject.verify_faces(face1=f1, face2=f2)
        """
        form_data = aiohttp.FormData()

        # Handle face1
        if isinstance(face1, str):
            # Base64 string
            form_data.add_field("face1", face1)
        elif isinstance(face1, bytes):
            form_data.add_field("faces", face1, filename="face1.jpg", content_type="image/jpeg")
        else:
            form_data.add_field("faces", face1, filename="face1.jpg", content_type="image/jpeg")

        # Handle face2
        if isinstance(face2, str):
            # Base64 string
            form_data.add_field("face2", face2)
        elif isinstance(face2, bytes):
            form_data.add_field("faces", face2, filename="face2.jpg", content_type="image/jpeg")
        else:
            form_data.add_field("faces", face2, filename="face2.jpg", content_type="image/jpeg")

        return await self.client.post("/Subject/face/verification", data=form_data)
