"""
Tests for the Face module.
"""

import io
import pytest
from reeve_python_sdk import ReeveClient


@pytest.mark.asyncio
async def test_face_list(api_url, api_key, mock_aiohttp):
    """Test listing faces for a person."""
    expected_response = {
        "result": [
            {"id": 1, "personId": 1},
            {"id": 2, "personId": 1}
        ],
        "error": None
    }

    mock_aiohttp.get(
        f"{api_url}/Person/face/list/1",
        payload=expected_response
    )

    async with ReeveClient(api_url=api_url, api_key=api_key) as client:
        response = await client.face.list(person_id=1)
        assert response == expected_response
        assert len(response["result"]) == 2


@pytest.mark.asyncio
async def test_face_add(api_url, api_key, mock_aiohttp):
    """Test adding a face to a person."""
    expected_response = {
        "result": {"id": 1, "personId": 1},
        "error": None
    }

    mock_aiohttp.post(
        f"{api_url}/Person/face/add",
        payload=expected_response
    )

    # Create a fake image file
    fake_image = io.BytesIO(b"fake image data")

    async with ReeveClient(api_url=api_url, api_key=api_key) as client:
        response = await client.face.add(person_id=1, face=fake_image)
        assert response == expected_response


@pytest.mark.asyncio
async def test_face_delete(api_url, api_key, mock_aiohttp):
    """Test deleting a face."""
    expected_response = {"result": "success", "error": None}

    mock_aiohttp.post(
        f"{api_url}/Person/face/delete/1",
        payload=expected_response
    )

    async with ReeveClient(api_url=api_url, api_key=api_key) as client:
        response = await client.face.delete(face_id=1)
        assert response == expected_response


@pytest.mark.asyncio
async def test_face_recognize(api_url, api_key, mock_aiohttp):
    """Test face recognition."""
    api_response = {
        "success": True,
        "error": None,
        "result": [
            {
                "name": "John Doe",
                "thresold": 48,
                "personId": 1639555908,
                "score": 130,
                "isMatchFound": True,
                "attributes": {
                    "age": "33",
                    "gender": "Male",
                    "expression": "Unknown",
                    "blink": "False",
                    "mouthOpen": "False",
                    "glasses": "False",
                    "darkGlasses": "False",
                    "ethnicity": "Hispanic"
                }
            }
        ],
        "statusCode": 200,
        "timestamp": "1759315300"
    }

    mock_aiohttp.post(
        f"{api_url}/Person/face/recognize",
        payload=api_response
    )

    fake_image = io.BytesIO(b"fake image data")

    async with ReeveClient(api_url=api_url, api_key=api_key) as client:
        response = await client.face.recognize(face=fake_image)
        # The SDK extracts the first result from the array
        assert response["success"] is True
        assert response["result"] is not None
        assert response["result"]["personId"] == 1639555908
        assert response["result"]["isMatchFound"] is True
        assert response["result"]["name"] == "John Doe"


@pytest.mark.asyncio
async def test_face_recognize_no_match(api_url, api_key, mock_aiohttp):
    """Test face recognition with no matches."""
    api_response = {
        "success": True,
        "error": None,
        "result": None,
        "statusCode": 200,
        "timestamp": "1759315300"
    }

    mock_aiohttp.post(
        f"{api_url}/Person/face/recognize",
        payload=api_response
    )

    fake_image = io.BytesIO(b"fake image data")

    async with ReeveClient(api_url=api_url, api_key=api_key) as client:
        response = await client.face.recognize(face=fake_image)
        assert response["success"] is True
        assert response["result"] is None


@pytest.mark.asyncio
async def test_face_verify(api_url, api_key, mock_aiohttp):
    """Test face verification against a person."""
    expected_response = {
        "result": {"match": True, "confidence": 0.98},
        "error": None
    }

    mock_aiohttp.post(
        f"{api_url}/Person/face/verification",
        payload=expected_response
    )

    fake_image = io.BytesIO(b"fake image data")

    async with ReeveClient(api_url=api_url, api_key=api_key) as client:
        response = await client.face.verify(face=fake_image, person_id=1)
        assert response == expected_response
        assert response["result"]["match"] is True
