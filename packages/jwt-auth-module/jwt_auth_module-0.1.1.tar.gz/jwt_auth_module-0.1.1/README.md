# JWT Auth Modules - Python

A simple and secure JWT (JSON Web Token) authentication library for Python applications.

## Features

- 🔐 Generate and validate JWT access tokens
- 🔄 Refresh token support
- ⚙️ Configurable token expiration
- 🛡️ Signature verification
- 📝 Custom claims support
- 🎯 Type-safe with full type hints
- ✅ Comprehensive test coverage

## Installation

```bash
pip install jwt-auth-module
```

## Quick Start

```python
from jwt_auth import JwtConfig, JwtTokenGenerator, JwtTokenValidator

# Create configuration with your own secret key
config = (
    JwtConfig.builder()
    .secret_key("your-base64-encoded-secret-key")
    .issuer("your-app-name")
    .build()
)

# Generate tokens
generator = JwtTokenGenerator(config)
access_token = generator.generate_access_token("user123")
refresh_token = generator.generate_refresh_token("user123")

# Validate tokens
validator = JwtTokenValidator(config)
is_valid = validator.validate_token(access_token)

# Parse token claims
from jwt_auth import JwtTokenParser
parser = JwtTokenParser(config)
claims = parser.parse_token(access_token)
user_id = claims.get_subject()
```

## Configuration

```python
from jwt_auth import JwtConfig

# Using builder pattern (recommended)
config = (
    JwtConfig.builder()
    .secret_key("your-base64-encoded-secret-key")
    .issuer("your-app-name")
    .access_token_expiration_seconds(3600)  # 1 hour
    .refresh_token_expiration_seconds(604800)  # 7 days
    .build()
)

# Using defaults (for testing only)
config = JwtConfig.with_all_defaults()
```

**⚠️ Security Warning:** Never use the default secret key in production. Always provide your own secure secret key.

## Custom Claims

```python
# Add custom claims to tokens
custom_claims = {
    "role": "admin",
    "scope": "read:write",
    "department": "engineering"
}

token = generator.generate_access_token("user123", custom_claims)

# Parse and access custom claims
claims = parser.parse_token(token)
role = claims.get_claim("role")
```

## Requirements

- Python 3.9+
- PyJWT >= 2.8.0

## License

MIT License

## Related Projects

- [JWT Auth Modules - Java](https://github.com/cubedm/jwt-auth-modules/tree/main/jwt-java)

## Contributing

Contributions are welcome! Please visit the [GitHub repository](https://github.com/cubedm/jwt-auth-modules).