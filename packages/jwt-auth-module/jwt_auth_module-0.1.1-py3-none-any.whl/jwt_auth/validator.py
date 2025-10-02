"""JWT token validator for verifying signed JWT tokens.

This module handles signature validation, expiration checking, and
structural verification.
"""

from datetime import datetime, timezone

import jwt

from .config import JwtConfig
from .exceptions import TokenExpiredException, TokenInvalidException
from .utils import create_secret_key, validate_token_format


class JwtTokenValidator:
    """JWT token validator for verifying signed JWT tokens.

    Handles signature validation, expiration checking, and structural
    verification. Thread-safe and designed to be used as a singleton.

    Attributes:
        config: JWT configuration settings
    """

    def __init__(self, config: JwtConfig) -> None:
        """Create a new JwtTokenValidator with the provided configuration.

        Args:
            config: JWT configuration

        Raises:
            TokenInvalidException: If configuration is invalid
        """
        if config is None:
            raise TokenInvalidException("JwtConfig cannot be null")

        self.config = config
        self._secret_key = create_secret_key(config.secret_key)

    def validate_token(self, token: str) -> bool:
        """Validate a JWT token completely.

        Checks signature, expiration, structure, and issuer.

        Args:
            token: The JWT token to validate

        Returns:
            True if token is valid

        Raises:
            TokenExpiredException: If token has expired
            TokenInvalidException: If token is invalid for any other reason
        """
        validate_token_format(token)

        try:
            claims = self._parse_and_validate_claims(token)
            self._validate_issuer(claims)
            return True
        except jwt.ExpiredSignatureError as e:
            # Extract expiration from expired token
            expired_claims = jwt.decode(
                token,
                options={"verify_signature": False},
                algorithms=["HS256"]
            )
            exp_timestamp = expired_claims.get("exp")
            expiration = (
                datetime.fromtimestamp(exp_timestamp, tz=timezone.utc)
                if exp_timestamp
                else None
            )
            raise TokenExpiredException(
                "Token has expired",
                expiration=expiration,
                cause=e
            ) from e
        except jwt.InvalidSignatureError as e:
            raise TokenInvalidException.signature_mismatch() from e
        except jwt.PyJWTError as e:
            raise TokenInvalidException(
                f"Token validation failed: {str(e)}",
                error_code="VALIDATION_FAILED",
                cause=e
            ) from e

    def is_token_valid(self, token: str) -> bool:
        """Validate a JWT token and return True if valid, False if invalid.

        Does not throw exceptions for validation failures.

        Args:
            token: The JWT token to validate

        Returns:
            True if token is valid, False otherwise
        """
        try:
            self.validate_token(token)
            return True
        except (TokenExpiredException, TokenInvalidException):
            return False

    def validate_signature(self, token: str) -> bool:
        """Validate token signature only, ignoring expiration.

        Useful for refresh token validation where expiration might be
        handled differently.

        Args:
            token: The JWT token to validate

        Returns:
            True if signature is valid

        Raises:
            TokenInvalidException: If signature is invalid
        """
        validate_token_format(token)

        try:
            # Decode with signature verification but skip expiration check
            jwt.decode(
                token,
                self._secret_key,
                algorithms=["HS256"],
                options={
                    "verify_signature": True,
                    "verify_exp": False,
                }
            )
            return True
        except jwt.ExpiredSignatureError:
            # Signature is valid but token is expired - that's OK for this method
            return True
        except jwt.InvalidSignatureError as e:
            raise TokenInvalidException.signature_mismatch() from e
        except jwt.PyJWTError as e:
            raise TokenInvalidException(
                f"Token signature validation failed: {str(e)}",
                error_code="SIGNATURE_VALIDATION_FAILED",
                cause=e
            ) from e

    def is_token_expired(self, token: str) -> bool:
        """Check if a token has expired without full validation.

        Args:
            token: The JWT token to check

        Returns:
            True if token has expired

        Raises:
            TokenInvalidException: If token format is invalid
        """
        validate_token_format(token)

        try:
            claims = self._parse_and_validate_claims(token)
            exp_timestamp = claims.get("exp")
            if exp_timestamp is None:
                return False

            expiration = datetime.fromtimestamp(exp_timestamp, tz=timezone.utc)
            return expiration < datetime.now(timezone.utc)
        except jwt.ExpiredSignatureError:
            return True
        except jwt.PyJWTError as e:
            raise TokenInvalidException(
                f"Cannot determine token expiration: {str(e)}",
                error_code="EXPIRATION_CHECK_FAILED",
                cause=e
            ) from e

    def _parse_and_validate_claims(self, token: str) -> dict:
        """Parse and validate the JWT claims.

        Args:
            token: The JWT token

        Returns:
            Parsed claims dictionary

        Raises:
            jwt.PyJWTError: If parsing or validation fails
        """
        return jwt.decode(
            token,
            self._secret_key,
            algorithms=["HS256"]
        )

    def _validate_issuer(self, claims: dict) -> None:
        """Validate the token issuer matches the expected issuer.

        Args:
            claims: The JWT claims

        Raises:
            TokenInvalidException: If issuer is invalid
        """
        token_issuer = claims.get("iss")
        expected_issuer = self.config.issuer

        if token_issuer != expected_issuer:
            raise TokenInvalidException(
                f"Invalid issuer. Expected: {expected_issuer}, Found: {token_issuer}",
                error_code="INVALID_ISSUER"
            )

    @classmethod
    def create(cls, config: JwtConfig) -> "JwtTokenValidator":
        """Create a JwtTokenValidator with the provided configuration.

        Factory method for convenience.

        Args:
            config: JWT configuration

        Returns:
            New JwtTokenValidator instance
        """
        return cls(config)
