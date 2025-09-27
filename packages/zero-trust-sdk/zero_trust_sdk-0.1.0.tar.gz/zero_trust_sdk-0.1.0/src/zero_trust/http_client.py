"""HTTP client for API communication."""

import asyncio
import json
from typing import Any, Dict, Optional, Union
from urllib.parse import urljoin

import aiohttp
import requests

from .config import Config
from .types import ZeroTrustError


class HttpClient:
    """HTTP client for Zero Trust API communication."""

    def __init__(self, config: Config) -> None:
        """Initialize HTTP client.
        
        Args:
            config: Client configuration
        """
        self.config = config
        self._session: Optional[aiohttp.ClientSession] = None

    def _get_session(self) -> aiohttp.ClientSession:
        """Get or create async session."""
        if self._session is None or self._session.closed:
            timeout = aiohttp.ClientTimeout(total=self.config.timeout)
            self._session = aiohttp.ClientSession(
                timeout=timeout,
                connector=aiohttp.TCPConnector(verify_ssl=self.config.verify_ssl),
                headers=self._get_headers(),
            )
        return self._session

    def _get_headers(self) -> Dict[str, str]:
        """Get default headers for requests."""
        headers = {
            "Content-Type": "application/json",
            "User-Agent": self.config.user_agent,
        }
        
        if self.config.token:
            headers["Authorization"] = f"Bearer {self.config.token}"
            
        return headers

    def _get_url(self, path: str) -> str:
        """Get full URL for API path."""
        return urljoin(self.config.api_url, path)

    def _handle_response_error(self, status: int, response_data: Any) -> None:
        """Handle HTTP error responses."""
        if status == 401:
            raise ZeroTrustError.auth("Authentication failed")
        elif status == 403:
            raise ZeroTrustError.permission_denied("Access denied")
        elif status == 404:
            raise ZeroTrustError.not_found("Resource not found")
        elif status == 429:
            # Extract retry-after if available
            retry_after = 60  # Default
            if isinstance(response_data, dict) and "retry_after" in response_data:
                retry_after = response_data["retry_after"]
            raise ZeroTrustError.rate_limit(retry_after)
        elif 400 <= status < 500:
            message = "Client error"
            if isinstance(response_data, dict) and "message" in response_data:
                message = response_data["message"]
            elif isinstance(response_data, str):
                message = response_data
            raise ZeroTrustError.client_error(status, message)
        elif status >= 500:
            message = "Server error"
            if isinstance(response_data, dict) and "message" in response_data:
                message = response_data["message"]
            elif isinstance(response_data, str):
                message = response_data
            raise ZeroTrustError.server_error(status, message)

    async def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """Make GET request.
        
        Args:
            path: API endpoint path
            params: Query parameters
            
        Returns:
            Response data
            
        Raises:
            ZeroTrustError: If request fails
        """
        return await self._request("GET", path, params=params)

    async def post(self, path: str, data: Optional[Dict[str, Any]] = None) -> Any:
        """Make POST request.
        
        Args:
            path: API endpoint path
            data: Request body data
            
        Returns:
            Response data
            
        Raises:
            ZeroTrustError: If request fails
        """
        return await self._request("POST", path, data=data)

    async def put(self, path: str, data: Optional[Dict[str, Any]] = None) -> Any:
        """Make PUT request.
        
        Args:
            path: API endpoint path
            data: Request body data
            
        Returns:
            Response data
            
        Raises:
            ZeroTrustError: If request fails
        """
        return await self._request("PUT", path, data=data)

    async def delete(self, path: str) -> Any:
        """Make DELETE request.
        
        Args:
            path: API endpoint path
            
        Returns:
            Response data
            
        Raises:
            ZeroTrustError: If request fails
        """
        return await self._request("DELETE", path)

    async def _request(
        self,
        method: str,
        path: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """Make HTTP request with retries.
        
        Args:
            method: HTTP method
            path: API endpoint path
            data: Request body data
            params: Query parameters
            
        Returns:
            Response data
            
        Raises:
            ZeroTrustError: If request fails
        """
        url = self._get_url(path)
        session = self._get_session()
        
        for attempt in range(self.config.max_retries + 1):
            try:
                async with session.request(
                    method,
                    url,
                    json=data,
                    params=params,
                ) as response:
                    # Get response data
                    try:
                        if response.content_type == "application/json":
                            response_data = await response.json()
                        else:
                            response_data = await response.text()
                    except Exception:
                        response_data = None

                    # Handle successful responses
                    if 200 <= response.status < 300:
                        return response_data

                    # Handle error responses
                    self._handle_response_error(response.status, response_data)

            except aiohttp.ClientError as e:
                if attempt == self.config.max_retries:
                    raise ZeroTrustError.network(str(e))
                # Exponential backoff
                await asyncio.sleep(2 ** attempt)
            except asyncio.TimeoutError:
                if attempt == self.config.max_retries:
                    raise ZeroTrustError.timeout()
                await asyncio.sleep(2 ** attempt)

    def set_token(self, token: str) -> None:
        """Update authentication token.
        
        Args:
            token: New authentication token
        """
        self.config = self.config.with_token(token)
        # Close existing session to update headers
        if self._session and not self._session.closed:
            asyncio.create_task(self._session.close())
            self._session = None

    async def test_connection(self) -> bool:
        """Test connection to the API.
        
        Returns:
            True if connection successful, False otherwise
        """
        try:
            await self.get("/health")
            return True
        except ZeroTrustError:
            return False
        except Exception:
            return False

    async def close(self) -> None:
        """Close the HTTP session."""
        if self._session and not self._session.closed:
            await self._session.close()

    async def __aenter__(self) -> "HttpClient":
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Async context manager exit."""
        await self.close()


class SyncHttpClient:
    """Synchronous HTTP client for blocking operations."""

    def __init__(self, config: Config) -> None:
        """Initialize sync HTTP client.
        
        Args:
            config: Client configuration
        """
        self.config = config
        self.session = requests.Session()
        self.session.headers.update(self._get_headers())

    def _get_headers(self) -> Dict[str, str]:
        """Get default headers for requests."""
        headers = {
            "Content-Type": "application/json",
            "User-Agent": self.config.user_agent,
        }
        
        if self.config.token:
            headers["Authorization"] = f"Bearer {self.config.token}"
            
        return headers

    def _get_url(self, path: str) -> str:
        """Get full URL for API path."""
        return urljoin(self.config.api_url, path)

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """Make synchronous GET request.
        
        Args:
            path: API endpoint path
            params: Query parameters
            
        Returns:
            Response data
            
        Raises:
            ZeroTrustError: If request fails
        """
        return self._request("GET", path, params=params)

    def post(self, path: str, data: Optional[Dict[str, Any]] = None) -> Any:
        """Make synchronous POST request.
        
        Args:
            path: API endpoint path
            data: Request body data
            
        Returns:
            Response data
            
        Raises:
            ZeroTrustError: If request fails
        """
        return self._request("POST", path, data=data)

    def _request(
        self,
        method: str,
        path: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """Make HTTP request.
        
        Args:
            method: HTTP method
            path: API endpoint path
            data: Request body data
            params: Query parameters
            
        Returns:
            Response data
            
        Raises:
            ZeroTrustError: If request fails
        """
        url = self._get_url(path)
        
        try:
            response = self.session.request(
                method,
                url,
                json=data,
                params=params,
                timeout=self.config.timeout,
                verify=self.config.verify_ssl,
            )
            
            # Get response data
            try:
                if response.headers.get("content-type", "").startswith("application/json"):
                    response_data = response.json()
                else:
                    response_data = response.text
            except Exception:
                response_data = None

            # Handle successful responses
            if 200 <= response.status_code < 300:
                return response_data

            # Handle error responses
            if response.status_code == 401:
                raise ZeroTrustError.auth("Authentication failed")
            elif response.status_code == 403:
                raise ZeroTrustError.permission_denied("Access denied")
            elif response.status_code == 404:
                raise ZeroTrustError.not_found("Resource not found")
            elif 400 <= response.status_code < 500:
                message = "Client error"
                if isinstance(response_data, dict) and "message" in response_data:
                    message = response_data["message"]
                raise ZeroTrustError.client_error(response.status_code, message)
            elif response.status_code >= 500:
                message = "Server error"
                if isinstance(response_data, dict) and "message" in response_data:
                    message = response_data["message"]
                raise ZeroTrustError.server_error(response.status_code, message)

        except requests.exceptions.RequestException as e:
            raise ZeroTrustError.network(str(e))

    def set_token(self, token: str) -> None:
        """Update authentication token.
        
        Args:
            token: New authentication token
        """
        self.config = self.config.with_token(token)
        self.session.headers["Authorization"] = f"Bearer {token}"