"""JWT token generator for creating signed JWT tokens.

This module handles both access and refresh token generation with
configurable claims using the PyJWT library.
"""

from datetime import datetime, timedelta, timezone
from typing import Any

import jwt

from .config import JwtConfig
from .exceptions import TokenGenerationException
from .models import JwtToken, TokenType
from .constants import Claims, MILLIS_TO_SECONDS
from .utils import create_secret_key, is_reserved_claim


class JwtTokenGenerator:
    """JWT token generator for creating signed JWT tokens.

    Handles both access and refresh token generation with configurable claims.
    Thread-safe and designed to be used as a singleton.

    Attributes:
        config: JWT configuration settings
    """

    def __init__(self, config: JwtConfig) -> None:
        """Create a new JwtTokenGenerator with the provided configuration.

        Args:
            config: JWT configuration

        Raises:
            TokenGenerationException: If configuration is invalid
        """
        if config is None:
            raise TokenGenerationException("JwtConfig cannot be null")

        self.config = config
        try:
            self._secret_key = create_secret_key(config.secret_key)
        except Exception as e:
            raise TokenGenerationException(
                "Invalid secret key format",
                cause=e
            ) from e

    def generate_access_token(
            self,
            user_id: str,
            claims: dict[str, Any] | None = None
    ) -> str:
        """Generate an access token for the given user.

        Args:
            user_id: The user identifier
            claims: Additional claims to include in the token (optional)

        Returns:
            Access token string

        Raises:
            TokenGenerationException: If token generation fails
        """
        return self._generate_token(user_id, claims, TokenType.ACCESS)

    def generate_refresh_token(self, user_id: str) -> str:
        """Generate a refresh token for the given user.

        Args:
            user_id: The user identifier

        Returns:
            Refresh token string

        Raises:
            TokenGenerationException: If token generation fails
        """
        return self._generate_token(user_id, None, TokenType.REFRESH)

    def generate_token_pair(
            self,
            user_id: str,
            claims: dict[str, Any] | None = None
    ) -> JwtToken:
        """Generate both access and refresh tokens for the given user.

        Args:
            user_id: The user identifier
            claims: Additional claims to include in the access token (optional)

        Returns:
            JwtToken containing both access and refresh tokens

        Raises:
            TokenGenerationException: If token generation fails
        """
        try:
            access_token = self.generate_access_token(user_id, claims)
            refresh_token = self.generate_refresh_token(user_id)
            expires_in = self.config.get_expiration_time_in_seconds(TokenType.ACCESS)

            return JwtToken(
                access_token=access_token,
                refresh_token=refresh_token,
                expires_in=expires_in
            )
        except Exception as e:
            raise TokenGenerationException(
                f"Failed to generate token pair for user: {user_id}",
                cause=e
            ) from e

    def _generate_token(
            self,
            user_id: str,
            claims: dict[str, Any] | None,
            token_type: TokenType
    ) -> str:
        """Generate a token of the specified type.

        Args:
            user_id: The user identifier
            claims: Additional claims (can be None)
            token_type: The type of token to generate

        Returns:
            JWT token string

        Raises:
            TokenGenerationException: If token generation fails
        """
        self._validate_user_id(user_id)

        try:
            now = datetime.now(timezone.utc)
            expiration_ms = self.config.get_expiration_time(token_type)
            expiration = now + timedelta(milliseconds=expiration_ms)

            # Build payload with standard claims
            payload: dict[str, Any] = {
                Claims.SUBJECT: user_id,
                Claims.ISSUER: self.config.issuer,
                Claims.ISSUED_AT: now,
                Claims.EXPIRATION: expiration,
                Claims.TOKEN_TYPE: token_type.value,
            }

            # Add custom claims if provided (filter out reserved claims)
            if claims:
                for key, value in claims.items():
                    if not is_reserved_claim(key):
                        payload[key] = value

            # Generate JWT token
            token = jwt.encode(
                payload,
                self._secret_key,
                algorithm="HS256"
            )

            return token

        except jwt.PyJWTError as e:
            raise TokenGenerationException(
                f"JWT generation failed for {token_type} token, user: {user_id}",
                cause=e
            ) from e
        except Exception as e:
            raise TokenGenerationException(
                f"Unexpected error generating {token_type} token for user: {user_id}",
                cause=e
            ) from e

    @staticmethod
    def _validate_user_id(user_id: str) -> None:
        """Validate the user ID parameter.

        Args:
            user_id: The user identifier to validate

        Raises:
            TokenGenerationException: If user ID is invalid
        """
        if not user_id or not user_id.strip():
            raise TokenGenerationException("User ID cannot be null or empty")

    @classmethod
    def create(cls, config: JwtConfig) -> "JwtTokenGenerator":
        """Create a JwtTokenGenerator with the provided configuration.

        Factory method for convenience.

        Args:
            config: JWT configuration

        Returns:
            New JwtTokenGenerator instance
        """
        return cls(config)
