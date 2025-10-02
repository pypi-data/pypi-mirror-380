"""
Face management module for the Reeve Python SDK.
"""

from typing import BinaryIO, Dict, Union
import aiohttp

from .client import BaseClient


class FaceModule:
    """Handles face operations with the Reeve API."""

    def __init__(self, client: BaseClient):
        """
        Initialize the Face module.

        Args:
            client: Base HTTP client instance
        """
        self.client = client

    async def list(self, person_id: int) -> Dict:
        """
        List all faces for a specific person.

        Args:
            person_id: ID of the person

        Returns:
            List of faces from the API

        Example:
            >>> async with ReeveClient(api_url="https://api.reeve.example.com",
            ...                        api_key="token") as client:
            ...     faces = await client.face.list(person_id=1)
        """
        return await self.client.get(f"/Person/face/list/{person_id}")

    async def add(self, person_id: int, face: Union[bytes, BinaryIO]) -> Dict:
        """
        Add a face image to a person.

        Args:
            person_id: ID of the person
            face: Face image as bytes or file-like object (JPG format)

        Returns:
            Response from the API

        Example:
            >>> async with ReeveClient(api_url="https://api.reeve.example.com",
            ...                        api_key="token") as client:
            ...     with open("face.jpg", "rb") as f:
            ...         result = await client.face.add(person_id=1, face=f)
        """
        form_data = aiohttp.FormData()
        form_data.add_field("personId", str(person_id))

        if isinstance(face, bytes):
            form_data.add_field("face", face, filename="face.jpg", content_type="image/jpeg")
        else:
            form_data.add_field("face", face, filename="face.jpg", content_type="image/jpeg")

        return await self.client.post("/Person/face/add", data=form_data)

    async def delete(self, face_id: int) -> Dict:
        """
        Delete a face by ID.

        Args:
            face_id: ID of the face to delete

        Returns:
            Deletion response from the API

        Example:
            >>> async with ReeveClient(api_url="https://api.reeve.example.com",
            ...                        api_key="token") as client:
            ...     result = await client.face.delete(face_id=123)
        """
        return await self.client.post(f"/Person/face/delete/{face_id}")

    async def recognize(self, face: Union[bytes, BinaryIO]) -> Dict:
        """
        Recognize a face against all enrolled persons.

        Args:
            face: Face image as bytes or file-like object (JPG format)

        Returns:
            Recognition result from the API (first match or null if no matches)

        Example:
            >>> async with ReeveClient(api_url="https://api.reeve.example.com",
            ...                        api_key="token") as client:
            ...     with open("unknown_face.jpg", "rb") as f:
            ...         result = await client.face.recognize(face=f)
            ...         # result["result"] will be the first match or None
        """
        form_data = aiohttp.FormData()

        if isinstance(face, bytes):
            form_data.add_field("face", face, filename="face.jpg", content_type="image/jpeg")
        else:
            form_data.add_field("face", face, filename="face.jpg", content_type="image/jpeg")

        response = await self.client.post("/Person/face/recognize", data=form_data)

        # Extract first result if available, otherwise return null
        if response.get("result") and isinstance(response["result"], list) and len(response["result"]) > 0:
            response["result"] = response["result"][0]
        else:
            response["result"] = None

        return response

    async def verify(self, face: Union[bytes, BinaryIO], person_id: int) -> Dict:
        """
        Verify a face against a specific person.

        Args:
            face: Face image as bytes or file-like object (JPG format)
            person_id: ID of the person to verify against

        Returns:
            Verification result from the API

        Example:
            >>> async with ReeveClient(api_url="https://api.reeve.example.com",
            ...                        api_key="token") as client:
            ...     with open("face.jpg", "rb") as f:
            ...         result = await client.face.verify(face=f, person_id=1)
        """
        form_data = aiohttp.FormData()
        form_data.add_field("personId", str(person_id))

        if isinstance(face, bytes):
            form_data.add_field("face", face, filename="face.jpg", content_type="image/jpeg")
        else:
            form_data.add_field("face", face, filename="face.jpg", content_type="image/jpeg")

        return await self.client.post("/Person/face/verification", data=form_data)
