"""Tests for JWT exceptions."""

from datetime import datetime, timezone
import pytest

from jwt_auth.exceptions import (
    JwtException,
    TokenGenerationException,
    TokenInvalidException,
    TokenExpiredException,
)


class TestJwtException:
    """Test cases for JwtException base class."""

    def test_jwt_exception_basic(self):
        """Test creating basic JWT exception."""
        exc = JwtException("Test error")

        assert str(exc) == "Test error"
        assert exc.message == "Test error"
        assert exc.error_code is None
        assert exc.cause is None

    def test_jwt_exception_with_error_code(self):
        """Test JWT exception with error code."""
        exc = JwtException("Test error", error_code="TEST_ERROR")

        assert str(exc) == "[TEST_ERROR] Test error"
        assert exc.error_code == "TEST_ERROR"

    def test_jwt_exception_with_cause(self):
        """Test JWT exception with cause."""
        original = ValueError("Original error")
        exc = JwtException("Test error", cause=original)

        assert exc.cause is original
        assert exc.__cause__ is original

    def test_jwt_exception_repr(self):
        """Test JWT exception repr."""
        exc = JwtException("Test error", error_code="TEST_ERROR")

        repr_str = repr(exc)
        assert "JwtException" in repr_str
        assert "Test error" in repr_str
        assert "TEST_ERROR" in repr_str


class TestTokenGenerationException:
    """Test cases for TokenGenerationException."""

    def test_token_generation_exception_basic(self):
        """Test creating basic token generation exception."""
        exc = TokenGenerationException("Generation failed")

        assert str(exc) == "[TOKEN_GENERATION_FAILED] Generation failed"
        assert exc.error_code == "TOKEN_GENERATION_FAILED"

    def test_token_generation_exception_custom_code(self):
        """Test token generation exception with custom code."""
        exc = TokenGenerationException("Error", error_code="CUSTOM_ERROR")

        assert exc.error_code == "CUSTOM_ERROR"
        assert "[CUSTOM_ERROR]" in str(exc)

    def test_configuration_error_factory(self):
        """Test configuration_error factory method."""
        exc = TokenGenerationException.configuration_error("Invalid config")

        assert "Invalid config" in str(exc)
        assert exc.error_code == "CONFIGURATION_ERROR"

    def test_invalid_secret_key_factory(self):
        """Test invalid_secret_key factory method."""
        exc = TokenGenerationException.invalid_secret_key()

        assert "256 bits" in str(exc)
        assert "32 bytes" in str(exc)
        assert exc.error_code == "INVALID_SECRET_KEY"


class TestTokenInvalidException:
    """Test cases for TokenInvalidException."""

    def test_token_invalid_exception_basic(self):
        """Test creating basic token invalid exception."""
        exc = TokenInvalidException("Invalid token")

        assert str(exc) == "[TOKEN_INVALID] Invalid token"
        assert exc.error_code == "TOKEN_INVALID"

    def test_token_invalid_exception_custom_code(self):
        """Test token invalid exception with custom code."""
        exc = TokenInvalidException("Error", error_code="CUSTOM_ERROR")

        assert exc.error_code == "CUSTOM_ERROR"

    def test_invalid_format_factory(self):
        """Test invalid_format factory method."""
        exc = TokenInvalidException.invalid_format()

        assert "3 parts" in str(exc)
        assert "dots" in str(exc)
        assert exc.error_code == "INVALID_FORMAT"

    def test_signature_mismatch_factory(self):
        """Test signature_mismatch factory method."""
        exc = TokenInvalidException.signature_mismatch()

        assert "signature" in str(exc).lower()
        assert exc.error_code == "SIGNATURE_MISMATCH"


class TestTokenExpiredException:
    """Test cases for TokenExpiredException."""

    def test_token_expired_exception_basic(self):
        """Test creating basic token expired exception."""
        exc = TokenExpiredException("Token expired")

        assert "Token expired" in str(exc)
        assert exc.error_code == "TOKEN_EXPIRED"
        assert exc.expiration is None

    def test_token_expired_exception_with_expiration(self):
        """Test token expired exception with expiration time."""
        exp_time = datetime(2024, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        exc = TokenExpiredException("Token expired", expiration=exp_time)

        assert exc.expiration == exp_time
        assert "2024-01-01" in str(exc)
        assert "12:00:00" in str(exc)

    def test_token_expired_exception_repr(self):
        """Test token expired exception repr."""
        exp_time = datetime(2024, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        exc = TokenExpiredException("Token expired", expiration=exp_time)

        repr_str = repr(exc)
        assert "TokenExpiredException" in repr_str
        assert "Token expired" in repr_str

    def test_token_expired_exception_with_cause(self):
        """Test token expired exception with cause."""
        original = ValueError("Original error")
        exp_time = datetime(2024, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        exc = TokenExpiredException(
            "Token expired",
            expiration=exp_time,
            cause=original
        )

        assert exc.cause is original
        assert exc.__cause__ is original


class TestExceptionHierarchy:
    """Test exception hierarchy and inheritance."""

    def test_exception_inheritance(self):
        """Test that all exceptions inherit from JwtException."""
        assert issubclass(TokenGenerationException, JwtException)
        assert issubclass(TokenInvalidException, JwtException)
        assert issubclass(TokenExpiredException, JwtException)

    def test_exception_catching_generation(self):
        """Test TokenGenerationException is catchable as JwtException."""
        with pytest.raises(JwtException):
            raise TokenGenerationException("Error")

    def test_exception_catching_invalid(self):
        """Test TokenInvalidException is catchable as JwtException."""
        with pytest.raises(JwtException):
            raise TokenInvalidException("Error")

    def test_exception_catching_expired(self):
        """Test TokenExpiredException is catchable as JwtException."""
        with pytest.raises(JwtException):
            raise TokenExpiredException("Error")

    def test_specific_exception_catching_generation(self):
        """Test catching TokenGenerationException specifically."""
        with pytest.raises(TokenGenerationException):
            raise TokenGenerationException("Error")

    def test_specific_exception_catching_invalid(self):
        """Test catching TokenInvalidException specifically."""
        with pytest.raises(TokenInvalidException):
            raise TokenInvalidException("Error")

    def test_specific_exception_catching_expired(self):
        """Test catching TokenExpiredException specifically."""
        with pytest.raises(TokenExpiredException):
            raise TokenExpiredException("Error")