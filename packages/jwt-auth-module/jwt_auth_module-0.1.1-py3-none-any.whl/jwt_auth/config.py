"""JWT configuration management.

This module provides immutable configuration for JWT token operations
using dataclass with validation.
"""

import base64
import secrets
from dataclasses import dataclass
from typing import Final

from .constants import MILLIS_TO_SECONDS
from .exceptions import TokenGenerationException
from .models import TokenType

# Default configuration constants
DEFAULT_ISSUER: Final[str] = "cubedm-jwt-auth-module"
DEFAULT_ACCESS_TOKEN_EXPIRATION: Final[int] = 3600000  # 1 hour in milliseconds
DEFAULT_REFRESH_TOKEN_EXPIRATION: Final[int] = 604800000  # 7 days in milliseconds
MINIMUM_SECRET_KEY_LENGTH: Final[int] = 32  # 256 bits
DEFAULT_SECRET_KEY: Final[str] = "XkCTgf51URZ9MuwhbX+UnlbJQDw2efUHaZCZJ4d6BT8="


@dataclass(frozen=True)
class JwtConfig:
    """Immutable JWT configuration with validation.

    Contains all necessary settings for JWT token generation and validation.
    Thread-safe and designed to be shared across multiple JWT operations.

    Attributes:
        secret_key: Base64 encoded secret key for JWT signing
        issuer: JWT issuer name
        access_token_expiration: Access token expiration time in milliseconds
        refresh_token_expiration: Refresh token expiration time in milliseconds
    """

    secret_key: str = DEFAULT_SECRET_KEY
    issuer: str = DEFAULT_ISSUER
    access_token_expiration: int = DEFAULT_ACCESS_TOKEN_EXPIRATION
    refresh_token_expiration: int = DEFAULT_REFRESH_TOKEN_EXPIRATION

    def __post_init__(self) -> None:
        """Validate configuration after initialization.

        Raises:
            TokenGenerationException: If configuration is invalid
        """
        self._validate_configuration()

    def _validate_configuration(self) -> None:
        """Validate all configuration parameters.

        Raises:
            TokenGenerationException: If any parameter is invalid
        """
        if not self.secret_key or not self.secret_key.strip():
            raise TokenGenerationException.configuration_error(
                "secretKey cannot be null or empty"
            )

        if not self.issuer or not self.issuer.strip():
            raise TokenGenerationException.configuration_error(
                "issuer cannot be null or empty"
            )

        if self.access_token_expiration <= 0:
            raise TokenGenerationException.configuration_error(
                "accessTokenExpiration must be positive"
            )

        if self.refresh_token_expiration <= 0:
            raise TokenGenerationException.configuration_error(
                "refreshTokenExpiration must be positive"
            )

        self._validate_secret_key_length()

    def _validate_secret_key_length(self) -> None:
        """Validate that secret key meets minimum security requirements.

        Raises:
            TokenGenerationException: If secret key is too short
        """
        try:
            key_bytes = base64.b64decode(self.secret_key)
            if len(key_bytes) < MINIMUM_SECRET_KEY_LENGTH:
                raise TokenGenerationException.invalid_secret_key()
        except (ValueError, TypeError) as e:
            raise TokenGenerationException(
                "Secret key must be a valid Base64 encoded string",
                cause=e
            ) from e

    def get_expiration_time(self, token_type: TokenType) -> int:
        """Return expiration time for the given token type.

        Args:
            token_type: The token type

        Returns:
            Expiration time in milliseconds
        """
        if token_type == TokenType.ACCESS:
            return self.access_token_expiration
        elif token_type == TokenType.REFRESH:
            return self.refresh_token_expiration
        else:
            raise ValueError(f"Unknown token type: {token_type}")

    def get_expiration_time_in_seconds(self, token_type: TokenType) -> int:
        """Return expiration time in seconds for the given token type.

        Args:
            token_type: The token type

        Returns:
            Expiration time in seconds
        """
        return self.get_expiration_time(token_type) // MILLIS_TO_SECONDS

    @classmethod
    def with_defaults(cls, secret_key: str) -> "JwtConfig":
        """Create a JwtConfig with default settings and provided secret key.

        Args:
            secret_key: Base64 encoded secret key

        Returns:
            JwtConfig with default settings
        """
        return cls(secret_key=secret_key)

    @classmethod
    def with_all_defaults(cls) -> "JwtConfig":
        """Create a JwtConfig with all default settings.

        This is convenient for quick setup but it's recommended to provide
        your own secret key for production.

        Returns:
            JwtConfig with all defaults including default secret key
        """
        return cls()

    @classmethod
    def builder(cls) -> "JwtConfigBuilder":
        """Create a new builder instance for fluent configuration.

        Returns:
            New JwtConfigBuilder instance
        """
        return JwtConfigBuilder()

    @staticmethod
    def generate_random_secret_key() -> str:
        """Generate a random Base64 encoded secret key.

        WARNING: Only use this for development, not in production!

        Returns:
            Randomly generated Base64 encoded secret key
        """
        key_bytes = secrets.token_bytes(MINIMUM_SECRET_KEY_LENGTH)
        return base64.b64encode(key_bytes).decode('ascii')


class JwtConfigBuilder:
    """Builder for creating JwtConfig instances with fluent API.

    Provides a convenient way to construct JwtConfig with custom settings.
    """

    def __init__(self) -> None:
        """Initialize builder with default values."""
        self._secret_key = DEFAULT_SECRET_KEY
        self._issuer = DEFAULT_ISSUER
        self._access_token_expiration = DEFAULT_ACCESS_TOKEN_EXPIRATION
        self._refresh_token_expiration = DEFAULT_REFRESH_TOKEN_EXPIRATION

    def secret_key(self, secret_key: str) -> "JwtConfigBuilder":
        """Set the secret key for JWT signing.

        Must be Base64 encoded and at least 256 bits (32 bytes).

        Args:
            secret_key: Base64 encoded secret key

        Returns:
            This builder instance
        """
        self._secret_key = secret_key
        return self

    def issuer(self, issuer: str) -> "JwtConfigBuilder":
        """Set the JWT issuer.

        Args:
            issuer: Issuer name

        Returns:
            This builder instance
        """
        self._issuer = issuer
        return self

    def access_token_expiration(self, expiration_ms: int) -> "JwtConfigBuilder":
        """Set the access token expiration time in milliseconds.

        Args:
            expiration_ms: Expiration time in milliseconds

        Returns:
            This builder instance
        """
        self._access_token_expiration = expiration_ms
        return self

    def access_token_expiration_seconds(self, expiration_seconds: int) -> "JwtConfigBuilder":
        """Set the access token expiration time in seconds.

        Args:
            expiration_seconds: Expiration time in seconds

        Returns:
            This builder instance
        """
        self._access_token_expiration = expiration_seconds * MILLIS_TO_SECONDS
        return self

    def refresh_token_expiration(self, expiration_ms: int) -> "JwtConfigBuilder":
        """Set the refresh token expiration time in milliseconds.

        Args:
            expiration_ms: Expiration time in milliseconds

        Returns:
            This builder instance
        """
        self._refresh_token_expiration = expiration_ms
        return self

    def refresh_token_expiration_seconds(self, expiration_seconds: int) -> "JwtConfigBuilder":
        """Set the refresh token expiration time in seconds.

        Args:
            expiration_seconds: Expiration time in seconds

        Returns:
            This builder instance
        """
        self._refresh_token_expiration = expiration_seconds * MILLIS_TO_SECONDS
        return self

    def build(self) -> JwtConfig:
        """Build the JwtConfig instance.

        Returns:
            Immutable JwtConfig instance

        Raises:
            TokenGenerationException: If configuration is invalid
        """
        return JwtConfig(
            secret_key=self._secret_key,
            issuer=self._issuer,
            access_token_expiration=self._access_token_expiration,
            refresh_token_expiration=self._refresh_token_expiration
        )
