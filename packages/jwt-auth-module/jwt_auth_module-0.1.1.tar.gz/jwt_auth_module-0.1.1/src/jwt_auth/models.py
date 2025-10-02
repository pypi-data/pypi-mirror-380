"""Data models for JWT authentication.

This module defines immutable data classes representing JWT tokens
and their associated claims information.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any

class TokenType(str, Enum):
    """JWT token type enumeration.

    Defines the two types of tokens used in the authentication flow:
    - ACCESS: Short-lived token for API access
    - REFRESH: Long-lived token for obtaining new access tokens
    """

    ACCESS = "ACCESS"
    REFRESH = "REFRESH"

    def __str__(self) -> str:
        """Return string representation of token type."""
        return self.value


@dataclass(frozen=True)
class JwtToken:
    """JWT token pair (Access + Refresh) DTO for client responses.

    Contains both access and refresh tokens along with metadata.
    Typically returned after successful authentication.

    Attributes:
        access_token: JWT access token string
        refresh_token: JWT refresh token string (optional)
        token_type: Token type identifier (default: "Bearer")
        expires_in: Access token expiration time in seconds
    """

    access_token: str
    refresh_token: str | None
    expires_in: int
    token_type: str = "Bearer"

    def get_authorization_header(self) -> str:
        """Return the authorization header value.

        Returns:
            Authorization header value in format: "{token_type} {access_token}"
        """
        return f"{self.token_type} {self.access_token}"

    @classmethod
    def access_only(cls, access_token: str, expires_in: int) -> "JwtToken":
        """Create a JwtToken with only access token (no refresh token).

        Useful for scenarios where only access token is needed.

        Args:
            access_token: JWT access token
            expires_in: Access token expiration time in seconds

        Returns:
            JwtToken with only access token
        """
        return cls(
            access_token=access_token,
            refresh_token=None,
            expires_in=expires_in
        )


@dataclass(frozen=True)
class TokenClaims:
    """DTO that holds the claims information parsed from a JWT token.

    Provides a structured result of token parsing with convenient
    access to standard and custom claims.

    Attributes:
        subject: The subject of the token (usually user ID)
        claims: Custom claims map
        issued_at: Token issuance time
        expiration: Token expiration time
    """

    subject: str
    claims: dict[str, Any] = field(default_factory=dict)
    issued_at: datetime | None = None
    expiration: datetime | None = None

    def get_claim(self, key: str, default: Any = None) -> Any:
        """Return a specific claim value.

        Args:
            key: Claim key
            default: Default value if key not found

        Returns:
            Claim value or default
        """
        return self.claims.get(key, default)

    def is_expired(self) -> bool:
        """Check whether the token is expired.

        Returns:
            True if expired, False otherwise (or if expiration is None)
        """
        if self.expiration is None:
            return False
        return self.expiration < datetime.now(self.expiration.tzinfo)

    def get_time_to_expiry(self) -> int:
        """Return the remaining time until token expiration (in seconds).

        Returns:
            Remaining time in seconds, 0 if expired or expiration is None
        """
        if self.expiration is None:
            return 0

        now = datetime.now(self.expiration.tzinfo)
        diff = (self.expiration - now).total_seconds()
        return max(0, int(diff))

    def __post_init__(self) -> None:
        """Validate and process fields after initialization.

        Creates defensive copies of mutable fields to ensure immutability.
        """
        # Since this is a frozen dataclass, we need to use object.__setattr__
        # to create defensive copies of mutable fields
        # Always create a copy to prevent external modification
        object.__setattr__(self, 'claims', dict(self.claims))