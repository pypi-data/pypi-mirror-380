"""JWT Authentication Module for Python.

A simple and secure JWT authentication library.
"""

__version__ = "0.1.0"

# Core components
from .config import JwtConfig, JwtConfigBuilder
from .generator import JwtTokenGenerator
from .parser import JwtTokenParser
from .validator import JwtTokenValidator

# Models
from .models import JwtToken, TokenClaims, TokenType

# Exceptions
from .exceptions import (
  JwtException,
  TokenGenerationException,
  TokenInvalidException,
  TokenExpiredException,
)

# Constants
from .constants import Claims

# Convenience imports
from .config import (
  DEFAULT_ISSUER,
  DEFAULT_ACCESS_TOKEN_EXPIRATION,
  DEFAULT_REFRESH_TOKEN_EXPIRATION,
  MINIMUM_SECRET_KEY_LENGTH,
)

__all__ = [
  # Version
  "__version__",
  # Core classes
  "JwtConfig",
  "JwtConfigBuilder",
  "JwtTokenGenerator",
  "JwtTokenParser",
  "JwtTokenValidator",
  # Models
  "JwtToken",
  "TokenClaims",
  "TokenType",
  # Exceptions
  "JwtException",
  "TokenGenerationException",
  "TokenInvalidException",
  "TokenExpiredException",
  # Constants
  "Claims",
  # Config constants
  "DEFAULT_ISSUER",
  "DEFAULT_ACCESS_TOKEN_EXPIRATION",
  "DEFAULT_REFRESH_TOKEN_EXPIRATION",
  "MINIMUM_SECRET_KEY_LENGTH",
]
