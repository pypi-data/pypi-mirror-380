"""
Core async HTTP client for the Reeve Python SDK.
"""

from typing import Any, Dict, Optional, Union
import aiohttp

from .exceptions import (
    APIError,
    AuthenticationError,
    NotFoundError,
    ReeveAPIError,
    ValidationError,
)


class BaseClient:
    """Base async HTTP client with authentication and error handling."""

    def __init__(self, api_url: str, api_key: Optional[str] = None):
        """
        Initialize the base client.

        Args:
            api_url: Base URL of the Reeve API
            api_key: API key for authentication (Bearer token)
        """
        self.api_url = api_url.rstrip("/")
        self.api_key = api_key
        self._session: Optional[aiohttp.ClientSession] = None

    async def __aenter__(self):
        """Async context manager entry."""
        await self._create_session()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()

    async def _create_session(self):
        """Create an aiohttp session if it doesn't exist."""
        if self._session is None or self._session.closed:
            headers = {}
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"

            self._session = aiohttp.ClientSession(
                headers=headers,
                raise_for_status=False
            )

    async def close(self):
        """Close the aiohttp session."""
        if self._session and not self._session.closed:
            await self._session.close()
            self._session = None

    def _get_headers(self, additional_headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        """
        Get request headers.

        Args:
            additional_headers: Additional headers to include

        Returns:
            Dictionary of headers
        """
        headers = {}
        if additional_headers:
            headers.update(additional_headers)
        return headers

    def _format_error_message(self, error_data: Any) -> str:
        """
        Format error message from API response.

        Args:
            error_data: Error data from API (can be string, dict, or list)

        Returns:
            Formatted error message string
        """
        if isinstance(error_data, str):
            return error_data
        elif isinstance(error_data, dict):
            # Check for common error message fields
            if "Message" in error_data:
                messages = error_data["Message"]
                if isinstance(messages, list):
                    return "; ".join(str(m) for m in messages)
                return str(messages)
            elif "message" in error_data:
                return str(error_data["message"])
            else:
                # Return string representation of the dict
                return str(error_data)
        elif isinstance(error_data, list):
            return "; ".join(str(item) for item in error_data)
        else:
            return str(error_data)

    async def _handle_response(self, response: aiohttp.ClientResponse) -> Dict[str, Any]:
        """
        Handle API response and raise appropriate exceptions.

        Args:
            response: aiohttp response object

        Returns:
            Parsed JSON response

        Raises:
            AuthenticationError: For 401 responses
            ValidationError: For 400 responses
            NotFoundError: For 404 responses
            APIError: For other error responses
        """
        try:
            data = await response.json()
        except Exception:
            data = {"error": await response.text()}

        # Check for error in response
        if response.status >= 400:
            error_data = data.get("error", f"HTTP {response.status} error")
            error_message = self._format_error_message(error_data)

            if response.status == 401:
                raise AuthenticationError(error_message, response.status, data)
            elif response.status == 400:
                raise ValidationError(error_message, response.status, data)
            elif response.status == 404:
                raise NotFoundError(error_message, response.status, data)
            else:
                raise APIError(error_message, response.status, data)

        # Check for error field in successful response
        if isinstance(data, dict) and data.get("error"):
            error_message = self._format_error_message(data["error"])
            raise ReeveAPIError(error_message, response.status, data)

        return data

    async def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        data: Optional[aiohttp.FormData] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """
        Make an HTTP request.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint path
            params: Query parameters
            json_data: JSON request body
            data: Form data (for file uploads)
            headers: Additional headers

        Returns:
            Parsed JSON response

        Raises:
            ReeveAPIError: For API errors
        """
        await self._create_session()

        url = f"{self.api_url}{endpoint}"
        request_headers = self._get_headers(headers)

        async with self._session.request(
            method=method,
            url=url,
            params=params,
            json=json_data,
            data=data,
            headers=request_headers,
        ) as response:
            return await self._handle_response(response)

    async def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """
        Make a GET request.

        Args:
            endpoint: API endpoint path
            params: Query parameters
            headers: Additional headers

        Returns:
            Parsed JSON response
        """
        return await self._request("GET", endpoint, params=params, headers=headers)

    async def post(
        self,
        endpoint: str,
        json_data: Optional[Dict[str, Any]] = None,
        data: Optional[aiohttp.FormData] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """
        Make a POST request.

        Args:
            endpoint: API endpoint path
            json_data: JSON request body
            data: Form data (for file uploads)
            params: Query parameters
            headers: Additional headers

        Returns:
            Parsed JSON response
        """
        return await self._request(
            "POST",
            endpoint,
            params=params,
            json_data=json_data,
            data=data,
            headers=headers,
        )

    async def put(
        self,
        endpoint: str,
        json_data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """
        Make a PUT request.

        Args:
            endpoint: API endpoint path
            json_data: JSON request body
            params: Query parameters
            headers: Additional headers

        Returns:
            Parsed JSON response
        """
        return await self._request("PUT", endpoint, params=params, json_data=json_data, headers=headers)

    async def delete(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """
        Make a DELETE request.

        Args:
            endpoint: API endpoint path
            params: Query parameters
            headers: Additional headers

        Returns:
            Parsed JSON response
        """
        return await self._request("DELETE", endpoint, params=params, headers=headers)
