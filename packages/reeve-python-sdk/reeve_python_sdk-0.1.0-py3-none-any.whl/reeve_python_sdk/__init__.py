"""
Reeve Python SDK - A facial recognition API client.
"""

import sys

if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

from typing import Optional

from .client import BaseClient
from .auth import AuthModule
from .person import PersonModule
from .face import FaceModule
from .subject import SubjectModule
from .exceptions import (
    ReeveAPIError,
    AuthenticationError,
    ValidationError,
    NotFoundError,
    APIError,
)
from .models import Person, APIResponse

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "reeve_python_sdk"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError


class ReeveClient(BaseClient):
    """
    Main client for interacting with the Reeve API.

    This client provides access to all Reeve API functionality including
    person management, face management, recognition, and verification.

    Example:
        >>> import asyncio
        >>> from reeve_python_sdk import ReeveClient
        >>>
        >>> async def main():
        ...     async with ReeveClient(
        ...         api_url="https://api.reeve.example.com",
        ...         api_key="your-api-key"
        ...     ) as client:
        ...         # Create a person
        ...         person = await client.person.add(firstname="John", lastname="Doe")
        ...         print(person)
        >>>
        >>> asyncio.run(main())
    """

    def __init__(self, api_url: str, api_key: Optional[str] = None):
        """
        Initialize the Reeve client.

        Args:
            api_url: Base URL of the Reeve API
            api_key: API key for authentication (Bearer token)
        """
        super().__init__(api_url, api_key)

        # Initialize modules
        self.auth = AuthModule(self)
        self.person = PersonModule(self)
        self.face = FaceModule(self)
        self.subject = SubjectModule(self)


__all__ = [
    "ReeveClient",
    "ReeveAPIError",
    "AuthenticationError",
    "ValidationError",
    "NotFoundError",
    "APIError",
    "Person",
    "APIResponse",
    "__version__",
]
