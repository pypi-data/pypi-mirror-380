"""
Data models for the Reeve Python SDK.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional

from dateutil import parser


@dataclass
class Person:
    """Represents a person in the Reeve system."""

    id: int
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data: dict) -> "Person":
        """Create a Person instance from a dictionary."""
        return cls(
            id=data.get("id"),
            firstname=data.get("firstname"),
            lastname=data.get("lastname"),
            created_at=parser.parse(data["createdAt"]) if data.get("createdAt") else None,
            updated_at=parser.parse(data["updatedAt"]) if data.get("updatedAt") else None,
        )

    def to_dict(self) -> dict:
        """Convert Person instance to a dictionary."""
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "createdAt": self.created_at.isoformat() if self.created_at else None,
            "updatedAt": self.updated_at.isoformat() if self.updated_at else None,
        }


@dataclass
class APIResponse:
    """Wrapper for API responses from Reeve."""

    success: bool
    result: Any = None
    error: Optional[str] = None
    data: Optional[dict] = None

    @classmethod
    def from_dict(cls, data: dict) -> "APIResponse":
        """Create an APIResponse instance from a dictionary."""
        # Handle different response formats
        if "error" in data and data["error"]:
            return cls(success=False, error=data.get("error"), data=data)

        return cls(
            success=True,
            result=data.get("result"),
            data=data
        )

    def is_success(self) -> bool:
        """Check if the API call was successful."""
        return self.success and not self.error
