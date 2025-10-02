"""Tests for JWT utility functions."""

import base64
import pytest

from jwt_auth.utils import (
    create_secret_key,
    validate_token_format,
    is_standard_claim,
    is_reserved_claim,
    verify_signature,
)
from jwt_auth.exceptions import TokenInvalidException
from jwt_auth.constants import Claims


class TestCreateSecretKey:
    """Test cases for create_secret_key function."""

    def test_create_secret_key_valid(self):
        """Test creating secret key from valid base64."""
        # Create a valid 32-byte key
        key_bytes = b"a" * 32
        base64_key = base64.b64encode(key_bytes).decode('ascii')

        result = create_secret_key(base64_key)

        assert result == key_bytes
        assert len(result) == 32

    def test_create_secret_key_invalid_base64(self):
        """Test creating secret key from invalid base64."""
        with pytest.raises(TokenInvalidException) as exc_info:
            create_secret_key("not-valid-base64!!!")

        assert "Invalid secret key format" in str(exc_info.value)
        assert exc_info.value.error_code == "INVALID_SECRET_KEY"


class TestValidateTokenFormat:
    """Test cases for validate_token_format function."""

    def test_validate_token_format_valid(self):
        """Test validating a properly formatted token."""
        valid_token = "header.payload.signature"

        # Should not raise any exception
        validate_token_format(valid_token)

    def test_validate_token_format_empty(self):
        """Test validation fails with empty token."""
        with pytest.raises(TokenInvalidException) as exc_info:
            validate_token_format("")

        assert "cannot be null or empty" in str(exc_info.value)
        assert exc_info.value.error_code == "NULL_TOKEN"

    def test_validate_token_format_none(self):
        """Test validation fails with None token."""
        with pytest.raises(TokenInvalidException):
            validate_token_format(None)

    def test_validate_token_format_whitespace(self):
        """Test validation fails with whitespace token."""
        with pytest.raises(TokenInvalidException) as exc_info:
            validate_token_format("   ")

        assert "cannot be null or empty" in str(exc_info.value)

    def test_validate_token_format_two_parts(self):
        """Test validation fails with only two parts."""
        with pytest.raises(TokenInvalidException) as exc_info:
            validate_token_format("header.payload")

        assert "3 parts" in str(exc_info.value)
        assert exc_info.value.error_code == "INVALID_FORMAT"

    def test_validate_token_format_four_parts(self):
        """Test validation fails with four parts."""
        with pytest.raises(TokenInvalidException) as exc_info:
            validate_token_format("header.payload.signature.extra")

        assert "3 parts" in str(exc_info.value)

    def test_validate_token_format_one_part(self):
        """Test validation fails with single part."""
        with pytest.raises(TokenInvalidException):
            validate_token_format("justonepart")


class TestIsStandardClaim:
    """Test cases for is_standard_claim function."""

    def test_is_standard_claim_subject(self):
        """Test that 'sub' is a standard claim."""
        assert is_standard_claim(Claims.SUBJECT) is True
        assert is_standard_claim("sub") is True

    def test_is_standard_claim_issuer(self):
        """Test that 'iss' is a standard claim."""
        assert is_standard_claim(Claims.ISSUER) is True
        assert is_standard_claim("iss") is True

    def test_is_standard_claim_expiration(self):
        """Test that 'exp' is a standard claim."""
        assert is_standard_claim(Claims.EXPIRATION) is True
        assert is_standard_claim("exp") is True

    def test_is_standard_claim_issued_at(self):
        """Test that 'iat' is a standard claim."""
        assert is_standard_claim(Claims.ISSUED_AT) is True
        assert is_standard_claim("iat") is True

    def test_is_standard_claim_all_standard(self):
        """Test all standard claims."""
        standard_claims = ["sub", "iss", "aud", "exp", "nbf", "iat", "jti"]
        for claim in standard_claims:
            assert is_standard_claim(claim) is True

    def test_is_standard_claim_custom(self):
        """Test that custom claims are not standard."""
        assert is_standard_claim("custom") is False
        assert is_standard_claim("role") is False
        assert is_standard_claim("scope") is False

    def test_is_standard_claim_token_type(self):
        """Test that token type is not a standard claim."""
        # typ is a custom claim in our implementation
        assert is_standard_claim(Claims.TOKEN_TYPE) is False
        assert is_standard_claim("typ") is False


class TestIsReservedClaim:
    """Test cases for is_reserved_claim function."""

    def test_is_reserved_claim_standard(self):
        """Test that standard claims are reserved."""
        assert is_reserved_claim("sub") is True
        assert is_reserved_claim("iss") is True
        assert is_reserved_claim("exp") is True

    def test_is_reserved_claim_token_type(self):
        """Test that token type is reserved."""
        assert is_reserved_claim(Claims.TOKEN_TYPE) is True
        assert is_reserved_claim("typ") is True

    def test_is_reserved_claim_custom(self):
        """Test that custom claims are not reserved."""
        assert is_reserved_claim("role") is False
        assert is_reserved_claim("scope") is False
        assert is_reserved_claim("custom") is False

    def test_is_reserved_claim_all_standard(self):
        """Test all standard claims are reserved."""
        standard_claims = ["sub", "iss", "aud", "exp", "nbf", "iat", "jti"]
        for claim in standard_claims:
            assert is_reserved_claim(claim) is True


class TestVerifySignature:
    """Test cases for verify_signature function."""

    def test_verify_signature_valid(self):
        """Test signature verification with valid signature."""
        import hmac
        import hashlib

        message = b"header.payload"
        secret = b"secret_key_12345678901234567890"

        # Create valid signature
        signature = hmac.new(secret, message, hashlib.sha256).digest()

        # Should return True for valid signature
        assert verify_signature(message, signature, secret) is True

    def test_verify_signature_invalid(self):
        """Test signature verification with invalid signature."""
        message = b"header.payload"
        secret = b"secret_key_12345678901234567890"
        wrong_signature = b"wrong_signature_data_here_123456"

        # Should return False for invalid signature
        assert verify_signature(message, wrong_signature, secret) is False

    def test_verify_signature_wrong_secret(self):
        """Test signature verification with wrong secret key."""
        import hmac
        import hashlib

        message = b"header.payload"
        correct_secret = b"correct_secret_key_123456789012"
        wrong_secret = b"wrong_secret_key_1234567890123"

        # Create signature with correct secret
        signature = hmac.new(correct_secret, message, hashlib.sha256).digest()

        # Verify with wrong secret should fail
        assert verify_signature(message, signature, wrong_secret) is False

    def test_verify_signature_empty_message(self):
        """Test signature verification with empty message."""
        import hmac
        import hashlib

        message = b""
        secret = b"secret_key_12345678901234567890"
        signature = hmac.new(secret, message, hashlib.sha256).digest()

        # Should work even with empty message
        assert verify_signature(message, signature, secret) is True
