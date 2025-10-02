"""Custom exception classes for JWT authentication operations.

This module defines a hierarchy of exceptions used throughout the JWT
authentication module, providing clear error categorization and context.
"""

from datetime import datetime
from typing import Any

class JwtException(Exception):
    """Base exception for all JWT-related errors.

    This is the parent class for all JWT authentication exceptions,
    allowing for broad exception handling when needed.

    Attributes:
        message: Human-readable error description
        error_code: Machine-readable error identifier (optional)
        cause: Original exception that caused this error (optional)
    """

    def __init__(
            self,
            message: str,
            error_code: str | None = None,
            cause: Exception | None = None
    ) -> None:
        """Initialize JWT exception.

        Args:
            message: Error message describing what went wrong
            error_code: Optional machine-readable error code
            cause: Optional original exception
        """
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.cause = cause

        # Chain exceptions for better traceback (PEP 3134)
        if cause is not None:
            self.__cause__ = cause

    def __str__(self) -> str:
        """Return string representation of the exception."""
        if self.error_code:
            return f"[{self.error_code}] {self.message}"
        return self.message

    def __repr__(self) -> str:
        """Return detailed representation of the exception."""
        return (
            f"{self.__class__.__name__}("
            f"message={self.message!r}, "
            f"error_code={self.error_code!r})"
        )


class TokenGenerationException(JwtException):
    """Exception raised when token generation fails.

    This exception is thrown when there are issues creating JWT tokens,
    such as invalid configuration, missing required parameters, or
    cryptographic errors during signing.
    """

    def __init__(
            self,
            message: str,
            error_code: str = "TOKEN_GENERATION_FAILED",
            cause: Exception | None = None
    ) -> None:
        """Initialize token generation exception.

        Args:
            message: Error message
            error_code: Error code (defaults to TOKEN_GENERATION_FAILED)
            cause: Optional original exception
        """
        super().__init__(message, error_code, cause)

    @classmethod
    def configuration_error(cls, message: str) -> "TokenGenerationException":
        """Create exception for configuration errors.

        Args:
            message: Configuration error description

        Returns:
            TokenGenerationException with CONFIGURATION_ERROR code
        """
        return cls(message, error_code="CONFIGURATION_ERROR")

    @classmethod
    def invalid_secret_key(cls) -> "TokenGenerationException":
        """Create exception for invalid secret key.

        Returns:
            TokenGenerationException for secret key validation failure
        """
        return cls(
            "Secret key must be at least 256 bits (32 bytes) when Base64 decoded",
            error_code="INVALID_SECRET_KEY"
        )


class TokenInvalidException(JwtException):
    """Exception raised when token validation or parsing fails.

    This exception is thrown when a JWT token is malformed, has an
    invalid signature, or fails structural validation. Note that
    expiration is handled by TokenExpiredException.
    """

    def __init__(
            self,
            message: str,
            error_code: str = "TOKEN_INVALID",
            cause: Exception | None = None
    ) -> None:
        """Initialize token invalid exception.

        Args:
            message: Error message
            error_code: Error code (defaults to TOKEN_INVALID)
            cause: Optional original exception
        """
        super().__init__(message, error_code, cause)

    @classmethod
    def invalid_format(cls) -> "TokenInvalidException":
        """Create exception for invalid token format.

        Returns:
            TokenInvalidException for malformed tokens
        """
        return cls(
            "Invalid JWT token format. Expected 3 parts separated by dots",
            error_code="INVALID_FORMAT"
        )

    @classmethod
    def signature_mismatch(cls) -> "TokenInvalidException":
        """Create exception for signature verification failure.

        Returns:
            TokenInvalidException for signature mismatch
        """
        return cls(
            "Token signature verification failed",
            error_code="SIGNATURE_MISMATCH"
        )


class TokenExpiredException(JwtException):
    """Exception raised when a token has expired.

    This exception provides specific handling for expired tokens,
    including the expiration timestamp for diagnostic purposes.

    Attributes:
        expiration: The datetime when the token expired
    """

    def __init__(
            self,
            message: str,
            expiration: datetime | None = None,
            cause: Exception | None = None
    ) -> None:
        """Initialize token expired exception.

        Args:
            message: Error message
            expiration: When the token expired
            cause: Optional original exception
        """
        super().__init__(message, error_code="TOKEN_EXPIRED", cause=cause)
        self.expiration = expiration

    def __str__(self) -> str:
        """Return string representation including expiration time."""
        base_msg = super().__str__()
        if self.expiration:
            return f"{base_msg} (expired at: {self.expiration.isoformat()})"
        return base_msg

    def __repr__(self) -> str:
        """Return detailed representation of the exception."""
        return (
            f"{self.__class__.__name__}("
            f"message={self.message!r}, "
            f"expiration={self.expiration!r})"
        )