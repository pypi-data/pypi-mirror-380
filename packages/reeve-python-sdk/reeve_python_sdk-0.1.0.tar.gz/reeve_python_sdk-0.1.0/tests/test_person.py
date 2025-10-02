"""
Tests for the Person module.
"""

import pytest
from reeve_python_sdk import ReeveClient


@pytest.mark.asyncio
async def test_person_list(api_url, api_key, mock_aiohttp):
    """Test listing persons."""
    expected_response = {
        "result": [
            {"id": 1, "firstname": "John", "lastname": "Doe"},
            {"id": 2, "firstname": "Jane", "lastname": "Smith"}
        ],
        "error": None
    }

    mock_aiohttp.get(
        f"{api_url}/Person/list?Page=1&Amount=10",
        payload=expected_response
    )

    async with ReeveClient(api_url=api_url, api_key=api_key) as client:
        response = await client.person.list(page=1, amount=10)
        assert response == expected_response
        assert len(response["result"]) == 2


@pytest.mark.asyncio
async def test_person_add(api_url, api_key, mock_aiohttp):
    """Test adding a person."""
    expected_response = {
        "result": {"id": 1, "firstname": "John", "lastname": "Doe"},
        "error": None
    }

    mock_aiohttp.post(
        f"{api_url}/Person/add",
        payload=expected_response
    )

    async with ReeveClient(api_url=api_url, api_key=api_key) as client:
        response = await client.person.add(firstname="John", lastname="Doe")
        assert response == expected_response
        assert response["result"]["firstname"] == "John"


@pytest.mark.asyncio
async def test_person_edit(api_url, api_key, mock_aiohttp):
    """Test editing a person."""
    expected_response = {
        "result": {"id": 1, "firstname": "Jane", "lastname": "Doe"},
        "error": None
    }

    mock_aiohttp.put(
        f"{api_url}/Person/edit/1",
        payload=expected_response
    )

    async with ReeveClient(api_url=api_url, api_key=api_key) as client:
        response = await client.person.edit(person_id=1, firstname="Jane")
        assert response == expected_response
        assert response["result"]["firstname"] == "Jane"


@pytest.mark.asyncio
async def test_person_delete(api_url, api_key, mock_aiohttp):
    """Test deleting a person."""
    expected_response = {"result": "success", "error": None}

    mock_aiohttp.post(
        f"{api_url}/Person/delete/1",
        payload=expected_response
    )

    async with ReeveClient(api_url=api_url, api_key=api_key) as client:
        response = await client.person.delete(person_id=1)
        assert response == expected_response
