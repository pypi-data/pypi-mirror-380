"""Tests for JWT token generator."""

import pytest
import jwt as pyjwt

from jwt_auth.config import JwtConfig
from jwt_auth.generator import JwtTokenGenerator
from jwt_auth.models import TokenType, JwtToken
from jwt_auth.exceptions import TokenGenerationException


class TestJwtTokenGenerator:
    """Test cases for JwtTokenGenerator class."""

    @pytest.fixture
    def config(self):
        """Create a test configuration."""
        return JwtConfig.with_all_defaults()

    @pytest.fixture
    def generator(self, config):
        """Create a token generator."""
        return JwtTokenGenerator(config)

    def test_generator_creation(self, config):
        """Test creating a token generator."""
        generator = JwtTokenGenerator(config)

        assert generator.config == config
        assert generator._secret_key is not None

    def test_generator_creation_none_config(self):
        """Test generator creation fails with None config."""
        with pytest.raises(TokenGenerationException) as exc_info:
            JwtTokenGenerator(None)

        assert "JwtConfig cannot be null" in str(exc_info.value)

    def test_generator_create_factory(self, config):
        """Test create factory method."""
        generator = JwtTokenGenerator.create(config)

        assert isinstance(generator, JwtTokenGenerator)
        assert generator.config == config

    def test_generate_access_token(self, generator, config):
        """Test generating an access token."""
        token = generator.generate_access_token("user123")

        assert token is not None
        assert isinstance(token, str)
        assert len(token.split(".")) == 3  # JWT format

        # Decode and verify
        decoded = pyjwt.decode(
            token,
            generator._secret_key,
            algorithms=["HS256"]
        )
        assert decoded["sub"] == "user123"
        assert decoded["iss"] == config.issuer
        assert decoded["typ"] == TokenType.ACCESS.value
        assert "iat" in decoded
        assert "exp" in decoded

    def test_generate_access_token_with_claims(self, generator):
        """Test generating access token with custom claims."""
        custom_claims = {
            "role": "admin",
            "scope": "read:write"
        }

        token = generator.generate_access_token("user123", custom_claims)

        # Decode and verify custom claims
        decoded = pyjwt.decode(
            token,
            generator._secret_key,
            algorithms=["HS256"]
        )
        assert decoded["role"] == "admin"
        assert decoded["scope"] == "read:write"

    def test_generate_access_token_filters_reserved_claims(self, generator):
        """Test that reserved claims are filtered out."""
        claims_with_reserved = {
            "role": "admin",
            "sub": "hacker",  # Reserved, should be filtered
            "iss": "fake",  # Reserved, should be filtered
            "typ": "FAKE",  # Reserved, should be filtered
        }

        token = generator.generate_access_token("user123", claims_with_reserved)

        decoded = pyjwt.decode(
            token,
            generator._secret_key,
            algorithms=["HS256"]
        )
        # Should use the actual user_id, not the one in claims
        assert decoded["sub"] == "user123"
        # Should keep custom claim
        assert decoded["role"] == "admin"
        # Reserved claims should not be overridden
        assert decoded["iss"] == generator.config.issuer
        assert decoded["typ"] == TokenType.ACCESS.value

    def test_generate_refresh_token(self, generator, config):
        """Test generating a refresh token."""
        token = generator.generate_refresh_token("user123")

        assert token is not None
        assert isinstance(token, str)

        # Decode and verify
        decoded = pyjwt.decode(
            token,
            generator._secret_key,
            algorithms=["HS256"]
        )
        assert decoded["sub"] == "user123"
        assert decoded["iss"] == config.issuer
        assert decoded["typ"] == TokenType.REFRESH.value

    def test_generate_token_pair(self, generator, config):
        """Test generating a token pair."""
        token_pair = generator.generate_token_pair("user123")

        assert isinstance(token_pair, JwtToken)
        assert token_pair.access_token is not None
        assert token_pair.refresh_token is not None
        assert token_pair.expires_in > 0
        assert token_pair.token_type == "Bearer"

        # Verify both tokens
        access_decoded = pyjwt.decode(
            token_pair.access_token,
            generator._secret_key,
            algorithms=["HS256"]
        )
        refresh_decoded = pyjwt.decode(
            token_pair.refresh_token,
            generator._secret_key,
            algorithms=["HS256"]
        )

        assert access_decoded["typ"] == TokenType.ACCESS.value
        assert refresh_decoded["typ"] == TokenType.REFRESH.value
        assert access_decoded["sub"] == "user123"
        assert refresh_decoded["sub"] == "user123"

    def test_generate_token_pair_with_claims(self, generator):
        """Test generating token pair with custom claims."""
        custom_claims = {"role": "admin"}

        token_pair = generator.generate_token_pair("user123", custom_claims)

        # Access token should have custom claims
        access_decoded = pyjwt.decode(
            token_pair.access_token,
            generator._secret_key,
            algorithms=["HS256"]
        )
        assert access_decoded["role"] == "admin"

        # Refresh token should NOT have custom claims
        refresh_decoded = pyjwt.decode(
            token_pair.refresh_token,
            generator._secret_key,
            algorithms=["HS256"]
        )
        assert "role" not in refresh_decoded

    def test_generate_token_empty_user_id(self, generator):
        """Test generation fails with empty user ID."""
        with pytest.raises(TokenGenerationException) as exc_info:
            generator.generate_access_token("")

        assert "User ID cannot be null or empty" in str(exc_info.value)

    def test_generate_token_whitespace_user_id(self, generator):
        """Test generation fails with whitespace user ID."""
        with pytest.raises(TokenGenerationException):
            generator.generate_access_token("   ")

    def test_token_expiration_time(self, generator, config):
        """Test that token expiration is set correctly."""
        import time

        before = int(time.time())
        token = generator.generate_access_token("user123")
        after = int(time.time())

        decoded = pyjwt.decode(
            token,
            generator._secret_key,
            algorithms=["HS256"]
        )

        expected_exp = before + config.get_expiration_time_in_seconds(TokenType.ACCESS)
        actual_exp = decoded["exp"]

        # Should be within reasonable range
        assert expected_exp - 5 <= actual_exp <= after + config.get_expiration_time_in_seconds(TokenType.ACCESS) + 5

    def test_multiple_tokens_are_different(self, generator):
        """Test that generating multiple tokens produces different tokens."""
        import time

        token1 = generator.generate_access_token("user123")
        time.sleep(1.1)  # Ensure different iat timestamp
        token2 = generator.generate_access_token("user123")

        # Should be different due to different issued_at times
        assert token1 != token2

    def test_different_users_different_tokens(self, generator):
        """Test that different users get different tokens."""
        token1 = generator.generate_access_token("user1")
        token2 = generator.generate_access_token("user2")

        assert token1 != token2

        decoded1 = pyjwt.decode(token1, generator._secret_key, algorithms=["HS256"])
        decoded2 = pyjwt.decode(token2, generator._secret_key, algorithms=["HS256"])

        assert decoded1["sub"] == "user1"
        assert decoded2["sub"] == "user2"

    def test_token_signature_verification(self, generator):
        """Test that generated tokens have valid signatures."""
        token = generator.generate_access_token("user123")

        # Should not raise exception
        pyjwt.decode(
            token,
            generator._secret_key,
            algorithms=["HS256"]
        )

    def test_token_signature_verification_wrong_key(self, generator):
        """Test that tokens fail verification with wrong key."""
        token = generator.generate_access_token("user123")

        wrong_key = b"wrong_key_" + b"0" * 20

        with pytest.raises(pyjwt.InvalidSignatureError):
            pyjwt.decode(
                token,
                wrong_key,
                algorithms=["HS256"]
            )

    def test_custom_config_expiration(self):
        """Test token generation with custom expiration times."""
        config = (
            JwtConfig.builder()
            .access_token_expiration_seconds(7200)  # 2 hours
            .build()
        )
        generator = JwtTokenGenerator(config)

        token_pair = generator.generate_token_pair("user123")

        # expires_in should reflect custom expiration
        assert token_pair.expires_in == 7200

    def test_empty_claims_dict(self, generator):
        """Test generating token with empty claims dict."""
        token = generator.generate_access_token("user123", {})

        decoded = pyjwt.decode(
            token,
            generator._secret_key,
            algorithms=["HS256"]
        )
        assert decoded["sub"] == "user123"

    def test_none_claims(self, generator):
        """Test generating token with None claims."""
        token = generator.generate_access_token("user123", None)

        decoded = pyjwt.decode(
            token,
            generator._secret_key,
            algorithms=["HS256"]
        )
        assert decoded["sub"] == "user123"