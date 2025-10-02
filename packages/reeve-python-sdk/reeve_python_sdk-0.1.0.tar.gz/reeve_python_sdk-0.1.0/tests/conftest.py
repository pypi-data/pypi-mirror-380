"""
Test configuration and fixtures for reeve_python_sdk.
"""

import pytest
from aioresponses import aioresponses


@pytest.fixture
def mock_aiohttp():
    """Fixture to mock aiohttp responses."""
    with aioresponses() as m:
        yield m


@pytest.fixture
def api_url():
    """Fixture for API URL."""
    return "https://api.reeve.example.com"


@pytest.fixture
def api_key():
    """Fixture for API key."""
    return "test-api-key-12345"
