"""Authentication manager for the Zero Trust SDK."""

from typing import Optional

from .http_client import HttpClient
from .types import AuthResponse, User, ZeroTrustError


class AuthManager:
    """Authentication manager for Zero Trust API."""

    def __init__(self, http_client: HttpClient) -> None:
        """Initialize authentication manager.
        
        Args:
            http_client: HTTP client instance
        """
        self.http_client = http_client

    async def register(
        self,
        email: str,
        password: str,
        wallet_address: Optional[str] = None,
    ) -> AuthResponse:
        """Register a new user.
        
        Args:
            email: User email address
            password: User password
            wallet_address: Optional wallet address for Web3 authentication
            
        Returns:
            Authentication response with token and user info
            
        Raises:
            ZeroTrustError: If registration fails
        """
        if not email or not password:
            raise ZeroTrustError.validation("Email and password are required")

        payload = {
            "email": email,
            "password": password,
        }
        
        if wallet_address:
            payload["wallet_address"] = wallet_address

        try:
            response = await self.http_client.post("/api/v1/auth/register", payload)
            
            # Parse response
            user_data = response.get("user", {})
            user = User(
                id=user_data.get("id"),
                email=user_data.get("email"),
                role=user_data.get("role", "user"),
                created_at=user_data.get("created_at"),
                wallet_address=user_data.get("wallet_address"),
            )
            
            return AuthResponse(
                token=response.get("token"),
                user=user,
                expires_at=response.get("expires_at"),
            )
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Registration failed: {e}", "REGISTRATION_ERROR")

    async def login(self, email: str, password: str) -> AuthResponse:
        """Login with email and password.
        
        Args:
            email: User email address
            password: User password
            
        Returns:
            Authentication response with token and user info
            
        Raises:
            ZeroTrustError: If login fails
        """
        if not email or not password:
            raise ZeroTrustError.validation("Email and password are required")

        payload = {
            "email": email,
            "password": password,
        }

        try:
            response = await self.http_client.post("/api/v1/auth/login", payload)
            
            # Parse response
            user_data = response.get("user", {})
            user = User(
                id=user_data.get("id"),
                email=user_data.get("email"),
                role=user_data.get("role", "user"),
                created_at=user_data.get("created_at"),
                wallet_address=user_data.get("wallet_address"),
            )
            
            auth_response = AuthResponse(
                token=response.get("token"),
                user=user,
                expires_at=response.get("expires_at"),
            )
            
            # Update client token
            self.http_client.set_token(auth_response.token)
            
            return auth_response
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Login failed: {e}", "LOGIN_ERROR")

    async def wallet_auth(
        self,
        wallet_address: str,
        signature: str,
        message: str,
    ) -> AuthResponse:
        """Authenticate using Web3 wallet signature.
        
        Args:
            wallet_address: Ethereum wallet address
            signature: Signed message signature
            message: Original message that was signed
            
        Returns:
            Authentication response with token and user info
            
        Raises:
            ZeroTrustError: If wallet authentication fails
        """
        if not wallet_address or not signature or not message:
            raise ZeroTrustError.validation(
                "Wallet address, signature, and message are required"
            )

        payload = {
            "wallet_address": wallet_address,
            "signature": signature,
            "message": message,
        }

        try:
            response = await self.http_client.post("/api/v1/auth/wallet", payload)
            
            # Parse response
            user_data = response.get("user", {})
            user = User(
                id=user_data.get("id"),
                email=user_data.get("email"),
                role=user_data.get("role", "user"),
                created_at=user_data.get("created_at"),
                wallet_address=user_data.get("wallet_address"),
            )
            
            auth_response = AuthResponse(
                token=response.get("token"),
                user=user,
                expires_at=response.get("expires_at"),
            )
            
            # Update client token
            self.http_client.set_token(auth_response.token)
            
            return auth_response
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Wallet authentication failed: {e}", "WALLET_AUTH_ERROR")

    async def refresh_token(self, refresh_token: str) -> AuthResponse:
        """Refresh authentication token.
        
        Args:
            refresh_token: Refresh token
            
        Returns:
            New authentication response
            
        Raises:
            ZeroTrustError: If token refresh fails
        """
        if not refresh_token:
            raise ZeroTrustError.validation("Refresh token is required")

        payload = {"refresh_token": refresh_token}

        try:
            response = await self.http_client.post("/api/v1/auth/refresh", payload)
            
            # Parse response
            user_data = response.get("user", {})
            user = User(
                id=user_data.get("id"),
                email=user_data.get("email"),
                role=user_data.get("role", "user"),
                created_at=user_data.get("created_at"),
                wallet_address=user_data.get("wallet_address"),
            )
            
            auth_response = AuthResponse(
                token=response.get("token"),
                user=user,
                expires_at=response.get("expires_at"),
            )
            
            # Update client token
            self.http_client.set_token(auth_response.token)
            
            return auth_response
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Token refresh failed: {e}", "REFRESH_ERROR")

    async def logout(self) -> bool:
        """Logout current user.
        
        Returns:
            True if logout successful
            
        Raises:
            ZeroTrustError: If logout fails
        """
        try:
            await self.http_client.post("/api/v1/auth/logout")
            
            # Clear token from client
            self.http_client.set_token("")
            
            return True
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Logout failed: {e}", "LOGOUT_ERROR")

    async def get_current_user(self) -> User:
        """Get current authenticated user information.
        
        Returns:
            Current user information
            
        Raises:
            ZeroTrustError: If user info request fails
        """
        try:
            response = await self.http_client.get("/api/v1/auth/me")
            
            return User(
                id=response.get("id"),
                email=response.get("email"),
                role=response.get("role", "user"),
                created_at=response.get("created_at"),
                wallet_address=response.get("wallet_address"),
            )
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to get user info: {e}", "USER_INFO_ERROR")

    async def change_password(
        self,
        current_password: str,
        new_password: str,
    ) -> bool:
        """Change user password.
        
        Args:
            current_password: Current password
            new_password: New password
            
        Returns:
            True if password change successful
            
        Raises:
            ZeroTrustError: If password change fails
        """
        if not current_password or not new_password:
            raise ZeroTrustError.validation("Current and new passwords are required")

        payload = {
            "current_password": current_password,
            "new_password": new_password,
        }

        try:
            await self.http_client.post("/api/v1/auth/change-password", payload)
            return True
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Password change failed: {e}", "PASSWORD_CHANGE_ERROR")

    async def reset_password(self, email: str) -> bool:
        """Request password reset.
        
        Args:
            email: User email address
            
        Returns:
            True if reset request successful
            
        Raises:
            ZeroTrustError: If password reset request fails
        """
        if not email:
            raise ZeroTrustError.validation("Email is required")

        payload = {"email": email}

        try:
            await self.http_client.post("/api/v1/auth/reset-password", payload)
            return True
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Password reset failed: {e}", "PASSWORD_RESET_ERROR")

    async def verify_token(self, token: str) -> bool:
        """Verify if a token is valid.
        
        Args:
            token: JWT token to verify
            
        Returns:
            True if token is valid
            
        Raises:
            ZeroTrustError: If token verification fails
        """
        if not token:
            raise ZeroTrustError.validation("Token is required")

        # Temporarily set token for verification
        original_token = self.http_client.config.token
        self.http_client.set_token(token)
        
        try:
            await self.http_client.get("/api/v1/auth/verify")
            return True
        except ZeroTrustError as e:
            if e.code == "AUTH_ERROR":
                return False
            raise
        except Exception as e:
            raise ZeroTrustError(f"Token verification failed: {e}", "TOKEN_VERIFICATION_ERROR")
        finally:
            # Restore original token
            if original_token:
                self.http_client.set_token(original_token)