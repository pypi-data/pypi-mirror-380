"""
Person management module for the Reeve Python SDK.
"""

from typing import Dict, List, Optional

from .client import BaseClient
from .models import Person


class PersonModule:
    """Handles person management operations with the Reeve API."""

    def __init__(self, client: BaseClient):
        """
        Initialize the Person module.

        Args:
            client: Base HTTP client instance
        """
        self.client = client

    async def list(self, page: Optional[int] = None, amount: Optional[int] = None) -> Dict:
        """
        List all persons with optional pagination.

        Args:
            page: Page number for pagination
            amount: Number of persons per page

        Returns:
            List of persons from the API

        Example:
            >>> async with ReeveClient(api_url="https://api.reeve.example.com",
            ...                        api_key="token") as client:
            ...     persons = await client.person.list(page=1, amount=10)
        """
        params = {}
        if page is not None:
            params["Page"] = page
        if amount is not None:
            params["Amount"] = amount

        return await self.client.get("/Person/list", params=params)

    async def add(self, firstname: Optional[str] = None, lastname: Optional[str] = None) -> Dict:
        """
        Create a new person.

        Args:
            firstname: Person's first name
            lastname: Person's last name

        Returns:
            Created person data from the API

        Example:
            >>> async with ReeveClient(api_url="https://api.reeve.example.com",
            ...                        api_key="token") as client:
            ...     person = await client.person.add(firstname="John", lastname="Doe")
        """
        data = {}
        if firstname is not None:
            data["firstname"] = firstname
        if lastname is not None:
            data["lastname"] = lastname

        return await self.client.post("/Person/add", json_data=data)

    async def edit(self, person_id: int, firstname: Optional[str] = None,
                   lastname: Optional[str] = None) -> Dict:
        """
        Edit an existing person.

        Args:
            person_id: ID of the person to edit
            firstname: Updated first name
            lastname: Updated last name

        Returns:
            Updated person data from the API

        Example:
            >>> async with ReeveClient(api_url="https://api.reeve.example.com",
            ...                        api_key="token") as client:
            ...     person = await client.person.edit(1, firstname="Jane", lastname="Smith")
        """
        data = {"id": person_id}
        if firstname is not None:
            data["firstname"] = firstname
        if lastname is not None:
            data["lastname"] = lastname

        return await self.client.put(f"/Person/edit/{person_id}", json_data=data)

    async def delete(self, person_id: int) -> Dict:
        """
        Delete a person by ID.

        Args:
            person_id: ID of the person to delete

        Returns:
            Deletion response from the API

        Example:
            >>> async with ReeveClient(api_url="https://api.reeve.example.com",
            ...                        api_key="token") as client:
            ...     result = await client.person.delete(1)
        """
        return await self.client.post(f"/Person/delete/{person_id}")
