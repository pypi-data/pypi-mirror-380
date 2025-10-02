"""JWT token parser for extracting information from JWT tokens.

This module performs parsing without validation - use JwtTokenValidator
for security validation.
"""

from datetime import datetime, timezone
from typing import Any

import jwt

from .config import JwtConfig
from .exceptions import TokenInvalidException
from .models import TokenClaims
from .utils import create_secret_key, is_standard_claim


class JwtTokenParser:
    """JWT token parser for extracting information from JWT tokens.

    Performs parsing without validation - use JwtTokenValidator for
    security validation. Thread-safe and designed to be used as a singleton.

    Attributes:
        config: JWT configuration settings
    """

    def __init__(self, config: JwtConfig) -> None:
        """Create a new JwtTokenParser with the provided configuration.

        Args:
            config: JWT configuration

        Raises:
            TokenInvalidException: If configuration is invalid
        """
        if config is None:
            raise TokenInvalidException("JwtConfig cannot be null")

        self.config = config
        self._secret_key = create_secret_key(config.secret_key)

    def parse_subject(self, token: str) -> str:
        """Parse a JWT token and extract the subject (user ID).

        Does not validate token expiration or signature.

        Args:
            token: The JWT token to parse

        Returns:
            The subject (user ID) from the token

        Raises:
            TokenInvalidException: If token cannot be parsed
        """
        try:
            claims = self._parse_claims(token)
            return claims.get("sub", "")
        except jwt.PyJWTError as e:
            raise TokenInvalidException(
                "Failed to parse subject from token",
                error_code="SUBJECT_PARSE_FAILED",
                cause=e
            ) from e
        except Exception as e:
            raise TokenInvalidException(
                "Unexpected error parsing subject from token",
                error_code="UNEXPECTED_ERROR",
                cause=e
            ) from e

    def parse_token_claims(self, token: str) -> TokenClaims:
        """Parse a JWT token and extract all claims as TokenClaims object.

        Does not validate token expiration or signature.

        Args:
            token: The JWT token to parse

        Returns:
            TokenClaims containing all parsed information

        Raises:
            TokenInvalidException: If token cannot be parsed
        """
        try:
            claims = self._parse_claims(token)

            subject = claims.get("sub", "")
            issued_at = self._convert_timestamp(claims.get("iat"))
            expiration = self._convert_timestamp(claims.get("exp"))

            # Extract custom claims (excluding standard JWT claims)
            custom_claims = self._extract_custom_claims(claims)

            return TokenClaims(
                subject=subject,
                claims=custom_claims,
                issued_at=issued_at,
                expiration=expiration
            )
        except TokenInvalidException:
            # Re-raise TokenInvalidException as-is
            raise
        except jwt.PyJWTError as e:
            raise TokenInvalidException(
                "Failed to parse token claims",
                error_code="CLAIMS_PARSE_FAILED",
                cause=e
            ) from e
        except Exception as e:
            raise TokenInvalidException(
                "Unexpected error parsing token claims",
                error_code="UNEXPECTED_ERROR",
                cause=e
            ) from e

    def parse_custom_claim(self, token: str, claim_key: str) -> Any:
        """Parse a JWT token and extract a specific custom claim.

        Args:
            token: The JWT token to parse
            claim_key: The key of the claim to extract

        Returns:
            The claim value, or None if not found

        Raises:
            TokenInvalidException: If token cannot be parsed
        """
        try:
            claims = self._parse_claims(token)
            return claims.get(claim_key)
        except jwt.PyJWTError as e:
            raise TokenInvalidException(
                f"Failed to parse custom claim '{claim_key}' from token",
                error_code="CUSTOM_CLAIM_PARSE_FAILED",
                cause=e
            ) from e
        except Exception as e:
            raise TokenInvalidException(
                f"Unexpected error parsing custom claim '{claim_key}' from token",
                error_code="UNEXPECTED_ERROR",
                cause=e
            ) from e

    def parse_expiration(self, token: str) -> datetime | None:
        """Parse a JWT token and extract the expiration date.

        Args:
            token: The JWT token to parse

        Returns:
            The expiration date, or None if not present

        Raises:
            TokenInvalidException: If token cannot be parsed
        """
        try:
            claims = self._parse_claims(token)
            return self._convert_timestamp(claims.get("exp"))
        except jwt.PyJWTError as e:
            raise TokenInvalidException(
                "Failed to parse expiration from token",
                error_code="EXPIRATION_PARSE_FAILED",
                cause=e
            ) from e
        except Exception as e:
            raise TokenInvalidException(
                "Unexpected error parsing expiration from token",
                error_code="UNEXPECTED_ERROR",
                cause=e
            ) from e

    def parse_issued_at(self, token: str) -> datetime | None:
        """Parse a JWT token and extract the issued date.

        Args:
            token: The JWT token to parse

        Returns:
            The issued date, or None if not present

        Raises:
            TokenInvalidException: If token cannot be parsed
        """
        try:
            claims = self._parse_claims(token)
            return self._convert_timestamp(claims.get("iat"))
        except jwt.PyJWTError as e:
            raise TokenInvalidException(
                "Failed to parse issued date from token",
                error_code="ISSUED_AT_PARSE_FAILED",
                cause=e
            ) from e
        except Exception as e:
            raise TokenInvalidException(
                "Unexpected error parsing issued date from token",
                error_code="UNEXPECTED_ERROR",
                cause=e
            ) from e

    def can_parse(self, token: str) -> bool:
        """Check if a token can be parsed (basic format validation).

        Does not check signature or expiration.

        Args:
            token: The JWT token to check

        Returns:
            True if token can be parsed, False otherwise
        """
        try:
            self._parse_claims(token)
            return True
        except (jwt.PyJWTError, TokenInvalidException):
            return False

    def _parse_claims(self, token: str) -> dict[str, Any]:
        """Parse the JWT token and extract all claims.

        This method handles both valid and expired tokens for parsing purposes.

        Args:
            token: The JWT token

        Returns:
            Parsed claims dictionary

        Raises:
            jwt.PyJWTError: If parsing fails
        """
        from .utils import validate_token_format

        validate_token_format(token)

        try:
            # Decode without verification for parsing purposes
            # options parameter tells PyJWT to skip all validation
            claims = jwt.decode(
                token,
                self._secret_key,
                algorithms=["HS256"],
                options={
                    "verify_signature": True,
                    "verify_exp": False,  # Don't verify expiration
                    "verify_nbf": False,
                    "verify_iat": False,
                    "verify_aud": False,
                }
            )
            return claims
        except jwt.ExpiredSignatureError:
            # For parsing purposes, we want to extract claims even from expired tokens
            # Decode without any verification
            claims = jwt.decode(
                token,
                options={"verify_signature": False},
                algorithms=["HS256"]
            )
            return claims

    @staticmethod
    def _extract_custom_claims(claims: dict[str, Any]) -> dict[str, Any]:
        """Extract custom claims from JWT claims, excluding standard JWT claims.

        Args:
            claims: The JWT claims dictionary

        Returns:
            Dictionary of custom claims
        """
        return {
            key: value
            for key, value in claims.items()
            if not is_standard_claim(key)
        }

    @staticmethod
    def _convert_timestamp(timestamp: int | float | None) -> datetime | None:
        """Convert Unix timestamp to datetime with UTC timezone.

        Args:
            timestamp: Unix timestamp (seconds since epoch)

        Returns:
            Datetime object with UTC timezone, or None if timestamp is None
        """
        if timestamp is None:
            return None
        return datetime.fromtimestamp(timestamp, tz=timezone.utc)

    @classmethod
    def create(cls, config: JwtConfig) -> "JwtTokenParser":
        """Create a JwtTokenParser with the provided configuration.

        Factory method for convenience.

        Args:
            config: JWT configuration

        Returns:
            New JwtTokenParser instance
        """
        return cls(config)