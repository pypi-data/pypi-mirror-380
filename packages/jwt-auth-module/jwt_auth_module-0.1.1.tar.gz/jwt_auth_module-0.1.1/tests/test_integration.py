"""Integration tests for JWT authentication module.

Tests the complete flow of token generation, parsing, and validation.
"""

import pytest
from datetime import datetime, timezone

from jwt_auth.config import JwtConfig
from jwt_auth.generator import JwtTokenGenerator
from jwt_auth.parser import JwtTokenParser
from jwt_auth.validator import JwtTokenValidator
from jwt_auth.models import TokenType
from jwt_auth.exceptions import TokenExpiredException, TokenInvalidException


class TestJwtIntegration:
    """Integration tests for complete JWT workflows."""

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

    @pytest.fixture
    def validator(self, config):
        """Create a token validator."""
        return JwtTokenValidator(config)

    def test_generate_parse_validate_flow(self, generator, parser, validator):
        """Test complete flow: generate -> parse -> validate."""
        # Generate token
        token = generator.generate_access_token("user123")

        # Parse token
        claims = parser.parse_token_claims(token)
        assert claims.subject == "user123"
        assert claims.expiration is not None

        # Validate token
        assert validator.validate_token(token) is True

    def test_generate_token_pair_and_validate(self, generator, validator):
        """Test generating token pair and validating both tokens."""
        # Generate token pair
        token_pair = generator.generate_token_pair("user123")

        # Validate access token
        assert validator.validate_token(token_pair.access_token) is True

        # Validate refresh token
        assert validator.validate_token(token_pair.refresh_token) is True

    def test_custom_claims_through_full_flow(self, generator, parser, validator):
        """Test custom claims through generate -> parse -> validate."""
        custom_claims = {
            "role": "admin",
            "permissions": ["read", "write", "delete"],
            "department": "engineering"
        }

        # Generate with custom claims
        token = generator.generate_access_token("user123", custom_claims)

        # Validate token
        assert validator.validate_token(token) is True

        # Parse and verify custom claims
        claims = parser.parse_token_claims(token)
        assert claims.get_claim("role") == "admin"
        assert claims.get_claim("permissions") == ["read", "write", "delete"]
        assert claims.get_claim("department") == "engineering"

    def test_expired_token_flow(self, config):
        """Test expired token through validation and parsing."""
        # Create config with short expiration
        short_config = (
            JwtConfig.builder()
            .secret_key(config.secret_key)
            .access_token_expiration_seconds(1)
            .build()
        )

        generator = JwtTokenGenerator(short_config)
        parser = JwtTokenParser(short_config)
        validator = JwtTokenValidator(short_config)

        # Generate token
        token = generator.generate_access_token("user123")

        # Token should be valid initially
        assert validator.validate_token(token) is True

        # Wait for expiration
        import time
        time.sleep(2)

        # Validation should fail
        with pytest.raises(TokenExpiredException):
            validator.validate_token(token)

        # But parsing should still work
        claims = parser.parse_token_claims(token)
        assert claims.subject == "user123"
        assert claims.is_expired() is True

    def test_different_configs_incompatible(self):
        """Test that tokens from different configs can't be validated."""
        # Create two different configs
        config1 = JwtConfig.builder().issuer("issuer1").build()
        config2 = JwtConfig.builder().issuer("issuer2").build()

        generator1 = JwtTokenGenerator(config1)
        validator2 = JwtTokenValidator(config2)

        # Generate with config1
        token = generator1.generate_access_token("user123")

        # Should fail validation with config2 (different issuer)
        with pytest.raises(TokenInvalidException) as exc_info:
            validator2.validate_token(token)

        assert exc_info.value.error_code == "INVALID_ISSUER"

    def test_same_secret_different_issuer(self):
        """Test that same secret but different issuer fails validation."""
        secret = JwtConfig.generate_random_secret_key()

        config1 = (
            JwtConfig.builder()
            .secret_key(secret)
            .issuer("issuer1")
            .build()
        )
        config2 = (
            JwtConfig.builder()
            .secret_key(secret)
            .issuer("issuer2")
            .build()
        )

        generator = JwtTokenGenerator(config1)
        validator = JwtTokenValidator(config2)

        token = generator.generate_access_token("user123")

        # Should fail because issuer is different
        with pytest.raises(TokenInvalidException):
            validator.validate_token(token)

    def test_refresh_token_lifecycle(self, generator, parser, validator):
        """Test refresh token generation and validation."""
        # Generate refresh token
        refresh_token = generator.generate_refresh_token("user123")

        # Validate refresh token
        assert validator.validate_token(refresh_token) is True

        # Parse refresh token
        claims = parser.parse_token_claims(refresh_token)
        assert claims.subject == "user123"
        assert claims.get_claim("typ") == TokenType.REFRESH.value

    def test_token_pair_different_expirations(self, config, parser):
        """Test that access and refresh tokens have different expirations."""
        generator = JwtTokenGenerator(config)

        token_pair = generator.generate_token_pair("user123")

        # Parse both tokens
        access_claims = parser.parse_token_claims(token_pair.access_token)
        refresh_claims = parser.parse_token_claims(token_pair.refresh_token)

        # Refresh token should expire later than access token
        assert refresh_claims.expiration > access_claims.expiration

    def test_multiple_users_isolation(self, generator, parser, validator):
        """Test that different users have isolated tokens."""
        # Generate tokens for different users
        token1 = generator.generate_access_token("user1")
        token2 = generator.generate_access_token("user2")
        token3 = generator.generate_access_token("user3")

        # All should be valid
        assert validator.validate_token(token1) is True
        assert validator.validate_token(token2) is True
        assert validator.validate_token(token3) is True

        # Parse and verify subjects
        claims1 = parser.parse_token_claims(token1)
        claims2 = parser.parse_token_claims(token2)
        claims3 = parser.parse_token_claims(token3)

        assert claims1.subject == "user1"
        assert claims2.subject == "user2"
        assert claims3.subject == "user3"

    def test_signature_validation_only(self, config, generator):
        """Test signature validation ignores expiration."""
        # Create config with short expiration
        short_config = (
            JwtConfig.builder()
            .secret_key(config.secret_key)
            .access_token_expiration_seconds(1)
            .build()
        )

        generator = JwtTokenGenerator(short_config)
        validator = JwtTokenValidator(short_config)

        token = generator.generate_access_token("user123")

        # Wait for expiration
        import time
        time.sleep(2)

        # Full validation should fail
        with pytest.raises(TokenExpiredException):
            validator.validate_token(token)

        # But signature validation should pass
        assert validator.validate_signature(token) is True

    def test_can_parse_vs_is_valid(self, config):
        """Test difference between can_parse and is_token_valid."""
        # Create expired token
        short_config = (
            JwtConfig.builder()
            .secret_key(config.secret_key)
            .access_token_expiration_seconds(1)
            .build()
        )

        generator = JwtTokenGenerator(short_config)
        parser = JwtTokenParser(short_config)
        validator = JwtTokenValidator(short_config)

        token = generator.generate_access_token("user123")

        import time
        time.sleep(2)

        # Parser can parse expired tokens
        assert parser.can_parse(token) is True

        # But validator considers them invalid
        assert validator.is_token_valid(token) is False

    def test_reserved_claims_filtered(self, generator, parser):
        """Test that reserved claims are filtered during generation."""
        # Try to override reserved claims
        malicious_claims = {
            "sub": "hacker",  # Reserved
            "iss": "fake-issuer",  # Reserved
            "typ": "FAKE",  # Reserved
            "role": "admin"  # Custom, should be kept
        }

        token = generator.generate_access_token("user123", malicious_claims)

        # Parse and verify
        claims = parser.parse_token_claims(token)

        # Reserved claims should not be overridden
        assert claims.subject == "user123"  # Not "hacker"
        assert claims.get_claim("typ") == TokenType.ACCESS.value  # Not "FAKE"

        # Custom claim should be preserved
        assert claims.get_claim("role") == "admin"

    def test_authorization_header_format(self, generator):
        """Test authorization header format."""
        token_pair = generator.generate_token_pair("user123")

        header = token_pair.get_authorization_header()

        assert header.startswith("Bearer ")
        assert header == f"Bearer {token_pair.access_token}"

    def test_custom_expiration_config(self):
        """Test custom expiration configuration."""
        # Create config with custom expiration times
        custom_config = (
            JwtConfig.builder()
            .access_token_expiration_seconds(7200)  # 2 hours
            .refresh_token_expiration_seconds(2592000)  # 30 days
            .build()
        )

        generator = JwtTokenGenerator(custom_config)
        parser = JwtTokenParser(custom_config)

        token_pair = generator.generate_token_pair("user123")

        # Check expires_in matches config
        assert token_pair.expires_in == 7200

        # Parse and check expiration times
        access_claims = parser.parse_token_claims(token_pair.access_token)
        refresh_claims = parser.parse_token_claims(token_pair.refresh_token)

        # Calculate expected expiration difference
        access_to_refresh_diff = (
            refresh_claims.expiration - access_claims.expiration
        ).total_seconds()

        # Should be approximately 30 days - 2 hours = 2,584,800 seconds
        expected_diff = 2592000 - 7200
        assert abs(access_to_refresh_diff - expected_diff) < 5

    def test_time_to_expiry(self, generator, parser):
        """Test time_to_expiry calculation."""
        token = generator.generate_access_token("user123")

        claims = parser.parse_token_claims(token)

        # Should have approximately 1 hour (3600 seconds) left
        time_left = claims.get_time_to_expiry()
        assert 3595 <= time_left <= 3600

    def test_access_only_token(self, generator, validator):
        """Test generating access-only token (no refresh token)."""
        from jwt_auth.models import JwtToken

        access_token = generator.generate_access_token("user123")

        token_obj = JwtToken.access_only(access_token, 3600)

        assert token_obj.access_token == access_token
        assert token_obj.refresh_token is None
        assert token_obj.expires_in == 3600

        # Validate access token
        assert validator.validate_token(access_token) is True

    def test_multiple_token_generations_unique(self, generator):
        """Test that multiple token generations produce unique tokens."""
        import time

        tokens = []
        for _ in range(5):
            tokens.append(generator.generate_access_token("user123"))
            time.sleep(1.1)  # Sleep for over 1 second to ensure different iat timestamps

        # All tokens should be different (due to different iat)
        assert len(set(tokens)) == 5

    def test_parser_validator_consistency(self, generator, parser, validator, config):
        """Test that parser and validator are consistent."""
        token = generator.generate_access_token("user123")

        # If validator says it's valid
        assert validator.validate_token(token) is True

        # Then parser should be able to parse it
        assert parser.can_parse(token) is True

        # And parsing should succeed
        claims = parser.parse_token_claims(token)
        assert claims.subject == "user123"

    def test_issuer_validation_enforced(self, config):
        """Test that issuer validation is properly enforced."""
        token_config = (
            JwtConfig.builder()
            .issuer("token-issuer")
            .build()
        )
        validator_config = (
            JwtConfig.builder()
            .secret_key(token_config.secret_key)
            .issuer("validator-issuer")
            .build()
        )

        generator = JwtTokenGenerator(token_config)
        validator = JwtTokenValidator(validator_config)

        token = generator.generate_access_token("user123")

        # Should fail with wrong issuer
        with pytest.raises(TokenInvalidException) as exc_info:
            validator.validate_token(token)

        assert "issuer" in str(exc_info.value).lower()
        assert "token-issuer" in str(exc_info.value)
        assert "validator-issuer" in str(exc_info.value)