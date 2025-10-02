"""Utility functions for JWT operations.

This module provides common utility functions for JWT token processing,
including key creation, token validation, and claim checking.
"""

import base64
import hmac
import hashlib

from .constants import JWT_TOKEN_PARTS, STANDARD_CLAIMS, RESERVED_CLAIMS
from .exceptions import TokenInvalidException


def create_secret_key(base64_secret: str) -> bytes:
    """Create a secret key from Base64 encoded string.

    Args:
        base64_secret: Base64 encoded secret key

    Returns:
        Decoded secret key bytes suitable for HMAC operations

    Raises:
        TokenInvalidException: If secret key format is invalid
    """
    try:
        key_bytes = base64.b64decode(base64_secret)
        return key_bytes
    except Exception as e:
        raise TokenInvalidException(
            "Invalid secret key format",
            error_code="INVALID_SECRET_KEY",
            cause=e
        ) from e


def validate_token_format(token: str) -> None:
    """Validate the basic format of a JWT token.

    Checks that the token is not empty and has the correct structure
    (three parts separated by dots: header.payload.signature).

    Args:
        token: JWT token string to validate

    Raises:
        TokenInvalidException: If token format is invalid
    """
    if not token or not token.strip():
        raise TokenInvalidException(
            "Token cannot be null or empty",
            error_code="NULL_TOKEN"
        )

    parts = token.split(".")
    if len(parts) != JWT_TOKEN_PARTS:
        raise TokenInvalidException.invalid_format()


def is_standard_claim(key: str) -> bool:
    """Check if a claim key is a standard JWT claim.

    Standard claims are defined in RFC 7519 (sub, iss, aud, exp, nbf, iat, jti).

    Args:
        key: Claim key to check

    Returns:
        True if the claim is a standard JWT claim
    """
    return key in STANDARD_CLAIMS


def is_reserved_claim(key: str) -> bool:
    """Check if a claim key is reserved and should not be overridden.

    Reserved claims include standard claims plus custom claims like token type
    that are managed by the library.

    Args:
        key: Claim key to check

    Returns:
        True if the claim is reserved
    """
    return key in RESERVED_CLAIMS


def verify_signature(
        message: bytes,
        signature: bytes,
        secret_key: bytes
) -> bool:
    """Verify HMAC-SHA256 signature.

    This is a helper function for signature verification during token validation.

    Args:
        message: The message that was signed (header.payload)
        signature: The signature to verify
        secret_key: The secret key used for signing

    Returns:
        True if signature is valid, False otherwise
    """
    expected_signature = hmac.new(
        secret_key,
        message,
        hashlib.sha256
    ).digest()
    return hmac.compare_digest(signature, expected_signature)