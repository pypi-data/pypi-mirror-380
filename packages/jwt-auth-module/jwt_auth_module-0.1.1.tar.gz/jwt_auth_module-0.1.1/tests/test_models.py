"""Tests for JWT models."""

from datetime import datetime, timezone, timedelta
import pytest

from jwt_auth.models import JwtToken, TokenClaims, TokenType


class TestTokenType:
    """Test cases for TokenType enum."""

    def test_token_type_values(self):
        """Test token type enum values."""
        assert TokenType.ACCESS.value == "ACCESS"
        assert TokenType.REFRESH.value == "REFRESH"

    def test_token_type_string_conversion(self):
        """Test token type string conversion."""
        assert str(TokenType.ACCESS) == "ACCESS"
        assert str(TokenType.REFRESH) == "REFRESH"


class TestJwtToken:
    """Test cases for JwtToken class."""

    def test_jwt_token_creation(self):
        """Test creating a JWT token with all fields."""
        token = JwtToken(
            access_token="access123",
            refresh_token="refresh456",
            expires_in=3600
        )

        assert token.access_token == "access123"
        assert token.refresh_token == "refresh456"
        assert token.expires_in == 3600
        assert token.token_type == "Bearer"

    def test_jwt_token_custom_type(self):
        """Test creating a JWT token with custom token type."""
        token = JwtToken(
            access_token="access123",
            refresh_token="refresh456",
            expires_in=3600,
            token_type="Custom"
        )

        assert token.token_type == "Custom"

    def test_jwt_token_access_only(self):
        """Test creating access-only JWT token."""
        token = JwtToken.access_only("access123", 3600)

        assert token.access_token == "access123"
        assert token.refresh_token is None
        assert token.expires_in == 3600
        assert token.token_type == "Bearer"

    def test_get_authorization_header(self):
        """Test getting authorization header value."""
        token = JwtToken(
            access_token="access123",
            refresh_token="refresh456",
            expires_in=3600
        )

        header = token.get_authorization_header()
        assert header == "Bearer access123"

    def test_get_authorization_header_custom_type(self):
        """Test authorization header with custom token type."""
        token = JwtToken(
            access_token="access123",
            refresh_token="refresh456",
            expires_in=3600,
            token_type="Custom"
        )

        header = token.get_authorization_header()
        assert header == "Custom access123"

    def test_jwt_token_immutability(self):
        """Test that JwtToken is immutable."""
        token = JwtToken(
            access_token="access123",
            refresh_token="refresh456",
            expires_in=3600
        )

        with pytest.raises(Exception):  # FrozenInstanceError
            token.access_token = "new_token"


class TestTokenClaims:
    """Test cases for TokenClaims class."""

    def test_token_claims_creation(self):
        """Test creating token claims with all fields."""
        now = datetime.now(timezone.utc)
        exp = now + timedelta(hours=1)
        claims_dict = {"role": "admin", "scope": "read"}

        claims = TokenClaims(
            subject="user123",
            claims=claims_dict,
            issued_at=now,
            expiration=exp
        )

        assert claims.subject == "user123"
        assert claims.claims == claims_dict
        assert claims.issued_at == now
        assert claims.expiration == exp

    def test_token_claims_defaults(self):
        """Test creating token claims with default values."""
        claims = TokenClaims(subject="user123")

        assert claims.subject == "user123"
        assert claims.claims == {}
        assert claims.issued_at is None
        assert claims.expiration is None

    def test_get_claim(self):
        """Test getting specific claim value."""
        claims = TokenClaims(
            subject="user123",
            claims={"role": "admin", "scope": "read"}
        )

        assert claims.get_claim("role") == "admin"
        assert claims.get_claim("scope") == "read"
        assert claims.get_claim("nonexistent") is None

    def test_get_claim_with_default(self):
        """Test getting claim with default value."""
        claims = TokenClaims(
            subject="user123",
            claims={"role": "admin"}
        )

        assert claims.get_claim("nonexistent", "default") == "default"

    def test_is_expired_false(self):
        """Test is_expired returns False for valid token."""
        now = datetime.now(timezone.utc)
        exp = now + timedelta(hours=1)

        claims = TokenClaims(
            subject="user123",
            expiration=exp
        )

        assert claims.is_expired() is False

    def test_is_expired_true(self):
        """Test is_expired returns True for expired token."""
        now = datetime.now(timezone.utc)
        exp = now - timedelta(hours=1)

        claims = TokenClaims(
            subject="user123",
            expiration=exp
        )

        assert claims.is_expired() is True

    def test_is_expired_no_expiration(self):
        """Test is_expired returns False when no expiration set."""
        claims = TokenClaims(subject="user123")

        assert claims.is_expired() is False

    def test_get_time_to_expiry(self):
        """Test getting time to expiry in seconds."""
        now = datetime.now(timezone.utc)
        exp = now + timedelta(hours=1)

        claims = TokenClaims(
            subject="user123",
            expiration=exp
        )

        time_left = claims.get_time_to_expiry()
        # Should be approximately 3600 seconds (1 hour)
        assert 3595 <= time_left <= 3600

    def test_get_time_to_expiry_expired(self):
        """Test time to expiry returns 0 for expired token."""
        now = datetime.now(timezone.utc)
        exp = now - timedelta(hours=1)

        claims = TokenClaims(
            subject="user123",
            expiration=exp
        )

        assert claims.get_time_to_expiry() == 0

    def test_get_time_to_expiry_no_expiration(self):
        """Test time to expiry returns 0 when no expiration."""
        claims = TokenClaims(subject="user123")

        assert claims.get_time_to_expiry() == 0

    def test_token_claims_immutability(self):
        """Test that TokenClaims is immutable."""
        claims = TokenClaims(
            subject="user123",
            claims={"role": "admin"}
        )

        with pytest.raises(Exception):  # FrozenInstanceError
            claims.subject = "new_user"

    def test_claims_dict_is_copy(self):
        """Test that claims dict is a defensive copy."""
        original_claims = {"role": "admin"}
        claims = TokenClaims(
            subject="user123",
            claims=original_claims
        )

        # Modifying original should not affect TokenClaims
        original_claims["role"] = "user"
        assert claims.get_claim("role") == "admin"