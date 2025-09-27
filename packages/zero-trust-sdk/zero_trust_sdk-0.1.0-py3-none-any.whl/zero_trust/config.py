"""Configuration management for the Zero Trust SDK."""

import os
from typing import Optional
from urllib.parse import urlparse

from .types import ZeroTrustError


class Config:
    """Configuration for the Zero Trust SDK."""

    def __init__(
        self,
        api_url: str,
        token: Optional[str] = None,
        timeout: int = 30,
        max_retries: int = 3,
        user_agent: str = "zero-trust-python-sdk/0.1.0",
        verify_ssl: bool = True,
    ) -> None:
        """Initialize configuration.
        
        Args:
            api_url: API base URL
            token: Authentication token (JWT)
            timeout: Request timeout in seconds
            max_retries: Maximum retry attempts
            user_agent: User agent string
            verify_ssl: Whether to verify SSL certificates
        """
        # Validate API URL
        try:
            parsed = urlparse(api_url)
            if not parsed.scheme or not parsed.netloc:
                raise ValueError("Invalid URL")
        except Exception as e:
            raise ZeroTrustError.validation(f"Invalid API URL '{api_url}': {e}")

        self.api_url = api_url
        self.token = token
        self.timeout = timeout
        self.max_retries = max_retries
        self.user_agent = user_agent
        self.verify_ssl = verify_ssl

        self._validate()

    @classmethod
    def create(cls, api_url: str) -> "Config":
        """Create a new configuration with the given API URL."""
        return cls(api_url)

    @classmethod
    def from_env(cls) -> "Config":
        """Load configuration from environment variables.
        
        Environment variables:
        - ZEROTRUST_API_URL: API base URL
        - ZEROTRUST_TOKEN: Authentication token
        - ZEROTRUST_TIMEOUT: Request timeout in seconds
        - ZEROTRUST_MAX_RETRIES: Maximum retry attempts
        """
        api_url = os.getenv("ZEROTRUST_API_URL", "http://localhost:3000")
        token = os.getenv("ZEROTRUST_TOKEN")
        timeout = int(os.getenv("ZEROTRUST_TIMEOUT", "30"))
        max_retries = int(os.getenv("ZEROTRUST_MAX_RETRIES", "3"))

        return cls(
            api_url=api_url,
            token=token,
            timeout=timeout,
            max_retries=max_retries,
        )

    def with_token(self, token: str) -> "Config":
        """Return a new configuration with the given token."""
        return Config(
            api_url=self.api_url,
            token=token,
            timeout=self.timeout,
            max_retries=self.max_retries,
            user_agent=self.user_agent,
            verify_ssl=self.verify_ssl,
        )

    def with_timeout(self, timeout: int) -> "Config":
        """Return a new configuration with the given timeout."""
        return Config(
            api_url=self.api_url,
            token=self.token,
            timeout=timeout,
            max_retries=self.max_retries,
            user_agent=self.user_agent,
            verify_ssl=self.verify_ssl,
        )

    def with_max_retries(self, max_retries: int) -> "Config":
        """Return a new configuration with the given max retries."""
        return Config(
            api_url=self.api_url,
            token=self.token,
            timeout=self.timeout,
            max_retries=max_retries,
            user_agent=self.user_agent,
            verify_ssl=self.verify_ssl,
        )

    def with_user_agent(self, user_agent: str) -> "Config":
        """Return a new configuration with the given user agent."""
        return Config(
            api_url=self.api_url,
            token=self.token,
            timeout=self.timeout,
            max_retries=self.max_retries,
            user_agent=user_agent,
            verify_ssl=self.verify_ssl,
        )

    def disable_ssl_verification(self) -> "Config":
        """Return a new configuration with SSL verification disabled."""
        return Config(
            api_url=self.api_url,
            token=self.token,
            timeout=self.timeout,
            max_retries=self.max_retries,
            user_agent=self.user_agent,
            verify_ssl=False,
        )

    def is_authenticated(self) -> bool:
        """Check if authentication token is present."""
        return self.token is not None

    def get_base_url(self) -> str:
        """Get the base URL for API requests."""
        return self.api_url

    def _validate(self) -> None:
        """Validate the configuration."""
        if self.timeout <= 0:
            raise ZeroTrustError.validation("Timeout must be greater than 0")

        if self.max_retries < 0:
            raise ZeroTrustError.validation("Max retries must be >= 0")

        if not self.user_agent:
            raise ZeroTrustError.validation("User agent cannot be empty")