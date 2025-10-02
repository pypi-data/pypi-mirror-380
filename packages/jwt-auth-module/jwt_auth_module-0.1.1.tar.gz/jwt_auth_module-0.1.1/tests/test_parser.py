"""Tests for JWT token parser."""

import pytest
import jwt as pyjwt
from datetime import datetime, timezone, timedelta

from jwt_auth.config import JwtConfig
from jwt_auth.generator import JwtTokenGenerator
from jwt_auth.parser import JwtTokenParser
from jwt_auth.models import TokenType
from jwt_auth.exceptions import TokenInvalidException


class TestJwtTokenParser:
    """Test cases for JwtTokenParser class."""

    @pytest.fixture
    def config(self):
        """Create a test configuration."""
        return JwtConfig.with_all_defaults()

    @pytest.fixture
    def generator(self, config):
        """Create a token generator."""
        return JwtTokenGenerator(config)

    @pytest.fixture
    def parser(self, config):
        """Create a token parser."""
        return JwtTokenParser(config)

    def test_parser_creation(self, config):
        """Test creating a token parser."""
        parser = JwtTokenParser(config)

        assert parser.config == config
        assert parser._secret_key is not None

    def test_parser_creation_none_config(self):
        """Test parser creation fails with None config."""
        with pytest.raises(TokenInvalidException) as exc_info:
            JwtTokenParser(None)

        assert "JwtConfig cannot be null" in str(exc_info.value)

    def test_parser_create_factory(self, config):
        """Test create factory method."""
        parser = JwtTokenParser.create(config)

        assert isinstance(parser, JwtTokenParser)
        assert parser.config == config

    def test_parse_token_valid(self, generator, parser):
        """Test parsing a valid token."""
        token = generator.generate_access_token("user123")

        claims = parser.parse_token_claims(token)

        assert claims.subject == "user123"
        assert claims.issued_at is not None
        assert claims.expiration is not None

    def test_parse_token_with_custom_claims(self, generator, parser):
        """Test parsing token with custom claims."""
        custom_claims = {
            "role": "admin",
            "scope": "read:write"
        }
        token = generator.generate_access_token("user123", custom_claims)

        claims = parser.parse_token_claims(token)

        assert claims.subject == "user123"
        assert claims.get_claim("role") == "admin"
        assert claims.get_claim("scope") == "read:write"

    def test_parse_expired_token(self, config):
        """Test parsing an expired token (parser should still parse it)."""
        # Create a config with very short expiration
        short_config = (
            JwtConfig.builder()
            .secret_key(config.secret_key)
            .access_token_expiration_seconds(1)  # 1 second
            .build()
        )
        generator = JwtTokenGenerator(short_config)
        parser = JwtTokenParser(short_config)

        token = generator.generate_access_token("user123")

        # Wait for token to expire
        import time
        time.sleep(2)

        # Parser should still parse expired token
        claims = parser.parse_token_claims(token)
        assert claims.subject == "user123"
        assert claims.is_expired() is True

    def test_parse_token_empty(self, parser):
        """Test parsing fails with empty token."""
        with pytest.raises(TokenInvalidException) as exc_info:
            parser.parse_token_claims("")

        assert "cannot be null or empty" in str(exc_info.value)
        assert exc_info.value.error_code == "NULL_TOKEN"

    def test_parse_token_none(self, parser):
        """Test parsing fails with None token."""
        with pytest.raises(TokenInvalidException):
            parser.parse_token_claims(None)

    def test_parse_token_invalid_format(self, parser):
        """Test parsing fails with invalid format."""
        with pytest.raises(TokenInvalidException) as exc_info:
            parser.parse_token_claims("invalid.token")

        assert "3 parts" in str(exc_info.value)
        assert exc_info.value.error_code == "INVALID_FORMAT"

    def test_parse_token_invalid_signature(self, generator, config):
        """Test parsing fails with invalid signature."""
        token = generator.generate_access_token("user123")

        # Create parser with different secret (valid 32-byte base64 encoded)
        import base64
        wrong_secret = base64.b64encode(b"x" * 32).decode('ascii')  # 32 bytes
        wrong_config = (
            JwtConfig.builder()
            .secret_key(wrong_secret)
            .build()
        )
        parser = JwtTokenParser(wrong_config)

        with pytest.raises(TokenInvalidException):
            parser.parse_token_claims(token)

    def test_parse_subject(self, generator, parser):
        """Test parsing subject from token."""
        token = generator.generate_access_token("user123")

        subject = parser.parse_subject(token)
        assert subject == "user123"

    def test_parse_subject_different_users(self, generator, parser):
        """Test parsing subjects for different users."""
        token1 = generator.generate_access_token("user1")
        token2 = generator.generate_access_token("user2")

        assert parser.parse_subject(token1) == "user1"
        assert parser.parse_subject(token2) == "user2"

    def test_parse_expiration(self, generator, parser, config):
        """Test parsing expiration from token."""
        token = generator.generate_access_token("user123")

        expiration = parser.parse_expiration(token)

        assert expiration is not None
        assert isinstance(expiration, datetime)
        assert expiration.tzinfo is not None

    def test_parse_issued_at(self, generator, parser):
        """Test parsing issued_at from token."""
        token = generator.generate_access_token("user123")

        issued_at = parser.parse_issued_at(token)

        assert issued_at is not None
        assert isinstance(issued_at, datetime)
        assert issued_at.tzinfo is not None

    def test_parse_claim(self, generator, parser):
        """Test parsing specific claim from token."""
        custom_claims = {"role": "admin"}
        token = generator.generate_access_token("user123", custom_claims)

        role = parser.parse_custom_claim(token, "role")
        assert role == "admin"

    def test_parse_claim_nonexistent(self, generator, parser):
        """Test parsing nonexistent claim returns None."""
        token = generator.generate_access_token("user123")

        result = parser.parse_custom_claim(token, "nonexistent")
        assert result is None

    def test_parse_claim_with_claims_object(self, generator, parser):
        """Test parsing claims and accessing via TokenClaims object."""
        custom_claims = {"role": "admin", "age": 30}
        token = generator.generate_access_token("user123", custom_claims)

        claims = parser.parse_token_claims(token)

        assert claims.get_claim("role") == "admin"
        assert claims.get_claim("age") == 30

    def test_parse_custom_claim_multiple_types(self, generator, parser):
        """Test parsing custom claims of different types."""
        custom_claims = {"role": "admin", "level": 5, "active": True}
        token = generator.generate_access_token("user123", custom_claims)

        role = parser.parse_custom_claim(token, "role")
        level = parser.parse_custom_claim(token, "level")
        active = parser.parse_custom_claim(token, "active")

        assert role == "admin"
        assert level == 5
        assert active is True

    def test_can_parse_valid_token(self, generator, parser):
        """Test can_parse returns True for valid token."""
        token = generator.generate_access_token("user123")

        assert parser.can_parse(token) is True

    def test_can_parse_invalid_format(self, parser):
        """Test can_parse returns False for invalid format."""
        assert parser.can_parse("invalid.token") is False
        assert parser.can_parse("") is False
        assert parser.can_parse(None) is False

    def test_can_parse_invalid_signature(self, generator, config):
        """Test can_parse returns False for invalid signature."""
        token = generator.generate_access_token("user123")

        # Create parser with different secret (valid 32-byte base64 encoded)
        import base64
        wrong_secret = base64.b64encode(b"y" * 32).decode('ascii')  # 32 bytes
        wrong_config = (
            JwtConfig.builder()
            .secret_key(wrong_secret)
            .build()
        )
        parser = JwtTokenParser(wrong_config)

        assert parser.can_parse(token) is False

    def test_can_parse_expired_token(self, config):
        """Test can_parse returns True for expired token (parser can still parse)."""
        # Create a config with very short expiration
        short_config = (
            JwtConfig.builder()
            .secret_key(config.secret_key)
            .access_token_expiration_seconds(1)
            .build()
        )
        generator = JwtTokenGenerator(short_config)
        parser = JwtTokenParser(short_config)

        token = generator.generate_access_token("user123")

        # Wait for token to expire
        import time
        time.sleep(2)

        # Parser can still parse expired tokens
        assert parser.can_parse(token) is True

    def test_parse_refresh_token(self, generator, parser):
        """Test parsing a refresh token."""
        token = generator.generate_refresh_token("user123")

        claims = parser.parse_token_claims(token)

        assert claims.subject == "user123"
        assert claims.get_claim("typ") == TokenType.REFRESH.value

    def test_parse_preserves_all_claims(self, generator, parser):
        """Test that parsing preserves all custom claims."""
        custom_claims = {
            "role": "admin",
            "scope": "read:write",
            "department": "engineering",
            "level": 5
        }
        token = generator.generate_access_token("user123", custom_claims)

        claims = parser.parse_token_claims(token)

        assert claims.get_claim("role") == "admin"
        assert claims.get_claim("scope") == "read:write"
        assert claims.get_claim("department") == "engineering"
        assert claims.get_claim("level") == 5

    def test_parse_token_issued_at_before_expiration(self, generator, parser):
        """Test that issued_at is before expiration."""
        token = generator.generate_access_token("user123")

        claims = parser.parse_token_claims(token)

        assert claims.issued_at < claims.expiration

    def test_multiple_parses_same_result(self, generator, parser):
        """Test that parsing same token multiple times gives same result."""
        token = generator.generate_access_token("user123")

        claims1 = parser.parse_token_claims(token)
        claims2 = parser.parse_token_claims(token)

        assert claims1.subject == claims2.subject
        assert claims1.issued_at == claims2.issued_at
        assert claims1.expiration == claims2.expiration

    def test_parser_does_not_validate_issuer(self, config):
        """Test that parser does not validate issuer (that's validator's job)."""
        # Create token with one issuer
        config1 = (
            JwtConfig.builder()
            .issuer("issuer1")
            .build()
        )
        generator = JwtTokenGenerator(config1)
        token = generator.generate_access_token("user123")

        # Parse with different issuer - should succeed
        config2 = (
            JwtConfig.builder()
            .secret_key(config1.secret_key)
            .issuer("issuer2")
            .build()
        )
        parser = JwtTokenParser(config2)

        # Should parse successfully (parser doesn't validate issuer)
        claims = parser.parse_token_claims(token)
        assert claims.subject == "user123"