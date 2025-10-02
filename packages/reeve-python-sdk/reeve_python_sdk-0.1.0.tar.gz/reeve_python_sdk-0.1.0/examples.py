"""
Usage examples for the Reeve Python SDK.

This file demonstrates the two core functionalities:
1. Face Enrollment - Register faces for a person
2. Face Recognition - Identify unknown faces
"""

import asyncio
from reeve_python_sdk import ReeveClient
from reeve_python_sdk.exceptions import ReeveAPIError


async def example_face_enrollment():
    """Example: Enroll faces for a person."""
    async with ReeveClient(
        api_url="https://api.reeve.example.com",
        api_key="your-api-key"
    ) as client:
        try:
            # Create a person
            person = await client.person.add(firstname="John", lastname="Doe")
            person_id = person["result"]["id"]
            print(f"Created person with ID: {person_id}")

            # Add face images
            with open("face1.jpg", "rb") as f:
                result1 = await client.face.add(person_id=person_id, face=f)
                print(f"Added face 1: {result1}")

            with open("face2.jpg", "rb") as f:
                result2 = await client.face.add(person_id=person_id, face=f)
                print(f"Added face 2: {result2}")

            # List all faces for the person
            faces = await client.face.list(person_id=person_id)
            print(f"Person has {len(faces['result'])} faces enrolled")
        except ReeveAPIError as e:
            print(f"Enrollment error: {e}")


async def example_face_recognition():
    """Example: Recognize an unknown face."""
    async with ReeveClient(
        api_url="https://api.reeve.example.com",
        api_key="your-api-key"
    ) as client:
        try:
            # Recognize a face
            with open("face3.jpg", "rb") as f:
                result = await client.face.recognize(face=f)

            if result.get("result"):
                match = result["result"]
                print(f"Recognized person ID: {match.get('personId')}")
                print(f"Name: {match.get('name')}")
                print(f"Score: {match.get('score')}")
                print(f"Match found: {match.get('isMatchFound')}")

                # Demographics and attributes
                attrs = match.get("attributes", {})
                print(f"Age: {attrs.get('age')}, Gender: {attrs.get('gender')}")
                print(f"Ethnicity: {attrs.get('ethnicity')}")
            else:
                print("No match found")
        except ReeveAPIError as e:
            print(f"Recognition error: {e}")


# Run examples
if __name__ == "__main__":
    print("=== Face Enrollment Example ===")
    # asyncio.run(example_face_enrollment())

    print("\n=== Face Recognition Example ===")
    asyncio.run(example_face_recognition())
