"""Tests for JWT token validator."""

import pytest
from datetime import datetime, timezone, timedelta

from jwt_auth.config import JwtConfig
from jwt_auth.generator import JwtTokenGenerator
from jwt_auth.validator import JwtTokenValidator
from jwt_auth.exceptions import TokenInvalidException, TokenExpiredException


class TestJwtTokenValidator:
    """Test cases for JwtTokenValidator class."""

    @pytest.fixture
    def config(self):
        """Create a test configuration."""
        return JwtConfig.with_all_defaults()

    @pytest.fixture
    def generator(self, config):
        """Create a token generator."""
        return JwtTokenGenerator(config)

    @pytest.fixture
    def validator(self, config):
        """Create a token validator."""
        return JwtTokenValidator(config)

    def test_validator_creation(self, config):
        """Test creating a token validator."""
        validator = JwtTokenValidator(config)

        assert validator.config == config
        assert validator._secret_key is not None

    def test_validator_creation_none_config(self):
        """Test validator creation fails with None config."""
        with pytest.raises(TokenInvalidException) as exc_info:
            JwtTokenValidator(None)

        assert "JwtConfig cannot be null" in str(exc_info.value)

    def test_validator_create_factory(self, config):
        """Test create factory method."""
        validator = JwtTokenValidator.create(config)

        assert isinstance(validator, JwtTokenValidator)
        assert validator.config == config

    def test_validate_token_valid(self, generator, validator):
        """Test validating a valid token."""
        token = generator.generate_access_token("user123")

        result = validator.validate_token(token)
        assert result is True

    def test_validate_token_expired(self, config):
        """Test validating an expired token raises TokenExpiredException."""
        # Create a config with very short expiration
        short_config = (
            JwtConfig.builder()
            .secret_key(config.secret_key)
            .access_token_expiration_seconds(1)
            .build()
        )
        generator = JwtTokenGenerator(short_config)
        validator = JwtTokenValidator(short_config)

        token = generator.generate_access_token("user123")

        # Wait for token to expire
        import time
        time.sleep(2)

        with pytest.raises(TokenExpiredException) as exc_info:
            validator.validate_token(token)

        assert "expired" in str(exc_info.value).lower()
        assert exc_info.value.expiration is not None

    def test_validate_token_invalid_signature(self, generator, config):
        """Test validating token with invalid signature."""
        token = generator.generate_access_token("user123")

        # Create validator with different secret
        import base64
        wrong_secret = base64.b64encode(b"z" * 32).decode('ascii')
        wrong_config = (
            JwtConfig.builder()
            .secret_key(wrong_secret)
            .build()
        )
        validator = JwtTokenValidator(wrong_config)

        with pytest.raises(TokenInvalidException) as exc_info:
            validator.validate_token(token)

        assert exc_info.value.error_code == "SIGNATURE_MISMATCH"

    def test_validate_token_invalid_format(self, validator):
        """Test validating token with invalid format."""
        with pytest.raises(TokenInvalidException) as exc_info:
            validator.validate_token("invalid.token")

        assert exc_info.value.error_code == "INVALID_FORMAT"

    def test_validate_token_empty(self, validator):
        """Test validating empty token."""
        with pytest.raises(TokenInvalidException) as exc_info:
            validator.validate_token("")

        assert exc_info.value.error_code == "NULL_TOKEN"

    def test_validate_token_none(self, validator):
        """Test validating None token."""
        with pytest.raises(TokenInvalidException):
            validator.validate_token(None)

    def test_validate_token_invalid_issuer(self, generator, config):
        """Test validating token with wrong issuer."""
        token = generator.generate_access_token("user123")

        # Create validator with different issuer
        wrong_config = (
            JwtConfig.builder()
            .secret_key(config.secret_key)
            .issuer("different-issuer")
            .build()
        )
        validator = JwtTokenValidator(wrong_config)

        with pytest.raises(TokenInvalidException) as exc_info:
            validator.validate_token(token)

        assert exc_info.value.error_code == "INVALID_ISSUER"
        assert "issuer" in str(exc_info.value).lower()

    def test_is_token_valid_true(self, generator, validator):
        """Test is_token_valid returns True for valid token."""
        token = generator.generate_access_token("user123")

        assert validator.is_token_valid(token) is True

    def test_is_token_valid_false_expired(self, config):
        """Test is_token_valid returns False for expired token."""
        short_config = (
            JwtConfig.builder()
            .secret_key(config.secret_key)
            .access_token_expiration_seconds(1)
            .build()
        )
        generator = JwtTokenGenerator(short_config)
        validator = JwtTokenValidator(short_config)

        token = generator.generate_access_token("user123")

        import time
        time.sleep(2)

        assert validator.is_token_valid(token) is False

    def test_is_token_valid_false_invalid_signature(self, generator, config):
        """Test is_token_valid returns False for invalid signature."""
        token = generator.generate_access_token("user123")

        import base64
        wrong_secret = base64.b64encode(b"w" * 32).decode('ascii')
        wrong_config = (
            JwtConfig.builder()
            .secret_key(wrong_secret)
            .build()
        )
        validator = JwtTokenValidator(wrong_config)

        assert validator.is_token_valid(token) is False

    def test_is_token_valid_false_invalid_format(self, validator):
        """Test is_token_valid returns False for invalid format."""
        assert validator.is_token_valid("invalid.token") is False
        assert validator.is_token_valid("") is False
        assert validator.is_token_valid(None) is False

    def test_validate_signature_valid(self, generator, validator):
        """Test validating signature of valid token."""
        token = generator.generate_access_token("user123")

        result = validator.validate_signature(token)
        assert result is True

    def test_validate_signature_expired_token(self, config):
        """Test validate_signature returns True for expired token (only checks signature)."""
        short_config = (
            JwtConfig.builder()
            .secret_key(config.secret_key)
            .access_token_expiration_seconds(1)
            .build()
        )
        generator = JwtTokenGenerator(short_config)
        validator = JwtTokenValidator(short_config)

        token = generator.generate_access_token("user123")

        import time
        time.sleep(2)

        # Should still validate signature even though expired
        result = validator.validate_signature(token)
        assert result is True

    def test_validate_signature_invalid(self, generator, config):
        """Test validate_signature raises exception for invalid signature."""
        token = generator.generate_access_token("user123")

        import base64
        wrong_secret = base64.b64encode(b"v" * 32).decode('ascii')
        wrong_config = (
            JwtConfig.builder()
            .secret_key(wrong_secret)
            .build()
        )
        validator = JwtTokenValidator(wrong_config)

        with pytest.raises(TokenInvalidException) as exc_info:
            validator.validate_signature(token)

        assert exc_info.value.error_code == "SIGNATURE_MISMATCH"

    def test_validate_signature_invalid_format(self, validator):
        """Test validate_signature fails with invalid format."""
        with pytest.raises(TokenInvalidException):
            validator.validate_signature("invalid.token")

    def test_is_token_expired_false(self, generator, validator):
        """Test is_token_expired returns False for valid token."""
        token = generator.generate_access_token("user123")

        assert validator.is_token_expired(token) is False

    def test_is_token_expired_true(self, config):
        """Test is_token_expired returns True for expired token."""
        short_config = (
            JwtConfig.builder()
            .secret_key(config.secret_key)
            .access_token_expiration_seconds(1)
            .build()
        )
        generator = JwtTokenGenerator(short_config)
        validator = JwtTokenValidator(short_config)

        token = generator.generate_access_token("user123")

        import time
        time.sleep(2)

        assert validator.is_token_expired(token) is True

    def test_is_token_expired_invalid_format(self, validator):
        """Test is_token_expired fails with invalid format."""
        with pytest.raises(TokenInvalidException):
            validator.is_token_expired("invalid.token")

    def test_validate_refresh_token(self, generator, validator):
        """Test validating a refresh token."""
        token = generator.generate_refresh_token("user123")

        result = validator.validate_token(token)
        assert result is True

    def test_validate_token_with_custom_claims(self, generator, validator):
        """Test validating token with custom claims."""
        custom_claims = {"role": "admin", "scope": "read:write"}
        token = generator.generate_access_token("user123", custom_claims)

        result = validator.validate_token(token)
        assert result is True

    def test_validator_does_not_accept_different_issuer(self, generator, config):
        """Test that validator rejects tokens from different issuer."""
        # Generate token with issuer1
        config1 = (
            JwtConfig.builder()
            .issuer("issuer1")
            .build()
        )
        generator = JwtTokenGenerator(config1)
        token = generator.generate_access_token("user123")

        # Validate with issuer2 - should fail
        config2 = (
            JwtConfig.builder()
            .secret_key(config1.secret_key)
            .issuer("issuer2")
            .build()
        )
        validator = JwtTokenValidator(config2)

        with pytest.raises(TokenInvalidException) as exc_info:
            validator.validate_token(token)

        assert exc_info.value.error_code == "INVALID_ISSUER"

    def test_validator_accepts_same_issuer(self, generator, validator, config):
        """Test that validator accepts tokens with same issuer."""
        token = generator.generate_access_token("user123")

        # Should validate successfully with same issuer
        result = validator.validate_token(token)
        assert result is True

    def test_multiple_validations_same_token(self, generator, validator):
        """Test validating same token multiple times."""
        token = generator.generate_access_token("user123")

        # Should succeed multiple times
        assert validator.validate_token(token) is True
        assert validator.validate_token(token) is True
        assert validator.validate_token(token) is True

    def test_validate_different_tokens(self, generator, validator):
        """Test validating different tokens."""
        token1 = generator.generate_access_token("user1")
        token2 = generator.generate_access_token("user2")

        assert validator.validate_token(token1) is True
        assert validator.validate_token(token2) is True