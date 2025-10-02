"""
Tests for the base HTTP client.
"""

import pytest
from reeve_python_sdk import ReeveClient
from reeve_python_sdk.exceptions import AuthenticationError, ValidationError, NotFoundError


@pytest.mark.asyncio
async def test_client_initialization(api_url, api_key):
    """Test client initialization."""
    client = ReeveClient(api_url=api_url, api_key=api_key)
    assert client.api_url == api_url
    assert client.api_key == api_key
    assert client.auth is not None
    assert client.person is not None
    assert client.face is not None
    assert client.subject is not None


@pytest.mark.asyncio
async def test_client_context_manager(api_url, api_key, mock_aiohttp):
    """Test client as async context manager."""
    mock_aiohttp.get(
        f"{api_url}/Person/list",
        payload={"result": [], "error": None}
    )

    async with ReeveClient(api_url=api_url, api_key=api_key) as client:
        assert client._session is not None
        response = await client.person.list()
        assert response is not None

    # Session should be closed after exiting context
    assert client._session is None or client._session.closed


@pytest.mark.asyncio
async def test_authentication_error(api_url, api_key, mock_aiohttp):
    """Test authentication error handling."""
    mock_aiohttp.get(
        f"{api_url}/Person/list",
        status=401,
        payload={"error": "Unauthorized"}
    )

    async with ReeveClient(api_url=api_url, api_key=api_key) as client:
        with pytest.raises(AuthenticationError) as exc_info:
            await client.person.list()
        assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_validation_error(api_url, api_key, mock_aiohttp):
    """Test validation error handling."""
    mock_aiohttp.post(
        f"{api_url}/Person/add",
        status=400,
        payload={"error": "Invalid data"}
    )

    async with ReeveClient(api_url=api_url, api_key=api_key) as client:
        with pytest.raises(ValidationError) as exc_info:
            await client.person.add()
        assert exc_info.value.status_code == 400


@pytest.mark.asyncio
async def test_not_found_error(api_url, api_key, mock_aiohttp):
    """Test not found error handling."""
    mock_aiohttp.get(
        f"{api_url}/Person/face/list/999",
        status=404,
        payload={"error": "Person not found"}
    )

    async with ReeveClient(api_url=api_url, api_key=api_key) as client:
        with pytest.raises(NotFoundError) as exc_info:
            await client.face.list(person_id=999)
        assert exc_info.value.status_code == 404
