"""Constants used throughout the JWT authentication module.

This module provides centralized constant values for JWT operations,
following RFC 7519 standard claim names and internal configuration.
"""

from typing import Final

# Time conversion constant: milliseconds to seconds
MILLIS_TO_SECONDS: Final[int] = 1000

# Number of parts in a JWT token (header.payload.signature)
JWT_TOKEN_PARTS: Final[int] = 3


class Claims:
    """Standard JWT claim names as defined in RFC 7519.

    This class provides constants for both standard JWT claims
    and custom claims used in this authentication module.
    """

    # Standard JWT claims (RFC 7519)
    SUBJECT: Final[str] = "sub"  # Subject - identifies the principal
    ISSUER: Final[str] = "iss"  # Issuer - identifies who issued the JWT
    AUDIENCE: Final[str] = "aud"  # Audience - identifies intended recipients
    EXPIRATION: Final[str] = "exp"  # Expiration time
    NOT_BEFORE: Final[str] = "nbf"  # Not before time
    ISSUED_AT: Final[str] = "iat"  # Issued at time
    JWT_ID: Final[str] = "jti"  # JWT ID - unique identifier

    # Custom claims
    TOKEN_TYPE: Final[str] = "typ"  # Token type identification


    def __init__(self) -> None:
        """Prevent instantiation of utility class."""
        raise TypeError("Claims is a utility class and cannot be instantiated")

# Standard JWT claim names set (for validation purposes)
STANDARD_CLAIMS: Final[frozenset[str]] = frozenset({
    Claims.SUBJECT,
    Claims.ISSUER,
    Claims.AUDIENCE,
    Claims.EXPIRATION,
    Claims.NOT_BEFORE,
    Claims.ISSUED_AT,
    Claims.JWT_ID,
})

# Reserved claim names (standard claims + custom claims)
RESERVED_CLAIMS: Final[frozenset[str]] = frozenset({
    *STANDARD_CLAIMS,
    Claims.TOKEN_TYPE,
})