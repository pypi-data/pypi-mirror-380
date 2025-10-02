"""Tests for JWT configuration."""

import base64
import pytest

from jwt_auth.config import (
    JwtConfig,
    JwtConfigBuilder,
    DEFAULT_ISSUER,
    DEFAULT_ACCESS_TOKEN_EXPIRATION,
    DEFAULT_REFRESH_TOKEN_EXPIRATION,
    MINIMUM_SECRET_KEY_LENGTH,
)
from jwt_auth.exceptions import TokenGenerationException
from jwt_auth.models import TokenType


class TestJwtConfig:
    """Test cases for JwtConfig class."""

    def test_with_all_defaults(self):
        """Test creating config with all default values."""
        config = JwtConfig.with_all_defaults()

        assert config.issuer == DEFAULT_ISSUER
        assert config.access_token_expiration == DEFAULT_ACCESS_TOKEN_EXPIRATION
        assert config.refresh_token_expiration == DEFAULT_REFRESH_TOKEN_EXPIRATION
        assert config.secret_key is not None

    def test_with_defaults_custom_secret(self):
        """Test creating config with custom secret key."""
        custom_key = JwtConfig.generate_random_secret_key()
        config = JwtConfig.with_defaults(custom_key)

        assert config.secret_key == custom_key
        assert config.issuer == DEFAULT_ISSUER

    def test_builder_pattern(self):
        """Test builder pattern for creating config."""
        custom_key = JwtConfig.generate_random_secret_key()

        config = (
            JwtConfig.builder()
            .secret_key(custom_key)
            .issuer("test-issuer")
            .access_token_expiration(7200000)
            .refresh_token_expiration(1209600000)
            .build()
        )

        assert config.secret_key == custom_key
        assert config.issuer == "test-issuer"
        assert config.access_token_expiration == 7200000
        assert config.refresh_token_expiration == 1209600000

    def test_builder_with_seconds(self):
        """Test builder with expiration times in seconds."""
        config = (
            JwtConfig.builder()
            .access_token_expiration_seconds(3600)  # 1 hour
            .refresh_token_expiration_seconds(604800)  # 7 days
            .build()
        )

        assert config.access_token_expiration == 3600000
        assert config.refresh_token_expiration == 604800000

    def test_get_expiration_time(self):
        """Test getting expiration time by token type."""
        config = JwtConfig.with_all_defaults()

        access_exp = config.get_expiration_time(TokenType.ACCESS)
        refresh_exp = config.get_expiration_time(TokenType.REFRESH)

        assert access_exp == DEFAULT_ACCESS_TOKEN_EXPIRATION
        assert refresh_exp == DEFAULT_REFRESH_TOKEN_EXPIRATION

    def test_get_expiration_time_in_seconds(self):
        """Test getting expiration time in seconds."""
        config = JwtConfig.with_all_defaults()

        access_exp_sec = config.get_expiration_time_in_seconds(TokenType.ACCESS)
        refresh_exp_sec = config.get_expiration_time_in_seconds(TokenType.REFRESH)

        assert access_exp_sec == DEFAULT_ACCESS_TOKEN_EXPIRATION // 1000
        assert refresh_exp_sec == DEFAULT_REFRESH_TOKEN_EXPIRATION // 1000

    def test_validation_empty_secret_key(self):
        """Test validation fails with empty secret key."""
        with pytest.raises(TokenGenerationException) as exc_info:
            JwtConfig.builder().secret_key("").build()

        assert "secretKey cannot be null or empty" in str(exc_info.value)

    def test_validation_empty_issuer(self):
        """Test validation fails with empty issuer."""
        with pytest.raises(TokenGenerationException) as exc_info:
            JwtConfig.builder().issuer("").build()

        assert "issuer cannot be null or empty" in str(exc_info.value)

    def test_validation_negative_access_expiration(self):
        """Test validation fails with negative access token expiration."""
        with pytest.raises(TokenGenerationException) as exc_info:
            JwtConfig.builder().access_token_expiration(-1).build()

        assert "accessTokenExpiration must be positive" in str(exc_info.value)

    def test_validation_negative_refresh_expiration(self):
        """Test validation fails with negative refresh token expiration."""
        with pytest.raises(TokenGenerationException) as exc_info:
            JwtConfig.builder().refresh_token_expiration(-1).build()

        assert "refreshTokenExpiration must be positive" in str(exc_info.value)

    def test_validation_short_secret_key(self):
        """Test validation fails with secret key that's too short."""
        # Create a key that's too short (less than 32 bytes)
        short_key = base64.b64encode(b"short").decode('ascii')

        with pytest.raises(TokenGenerationException) as exc_info:
            JwtConfig.builder().secret_key(short_key).build()

        assert "256 bits" in str(exc_info.value)

    def test_validation_invalid_base64_secret_key(self):
        """Test validation fails with invalid base64 secret key."""
        with pytest.raises(TokenGenerationException) as exc_info:
            JwtConfig.builder().secret_key("not-valid-base64!!!").build()

        assert "Base64 encoded string" in str(exc_info.value)

    def test_generate_random_secret_key(self):
        """Test random secret key generation."""
        key1 = JwtConfig.generate_random_secret_key()
        key2 = JwtConfig.generate_random_secret_key()

        # Keys should be different
        assert key1 != key2

        # Keys should be valid base64
        decoded = base64.b64decode(key1)
        assert len(decoded) == MINIMUM_SECRET_KEY_LENGTH

        # Should be usable in config
        config = JwtConfig.with_defaults(key1)
        assert config.secret_key == key1

    def test_config_immutability(self):
        """Test that config is immutable (frozen dataclass)."""
        config = JwtConfig.with_all_defaults()

        with pytest.raises(Exception):  # FrozenInstanceError
            config.issuer = "new-issuer"