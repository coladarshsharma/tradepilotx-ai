from app.core.security import create_access_token, create_refresh_token, decode_token, hash_password, verify_password


def test_password_hash_round_trip() -> None:
    password = "A-strong-test-password"
    assert verify_password(password, hash_password(password))


def test_access_token_contains_expected_claims() -> None:
    token = create_access_token("user-123", "trader")
    claims = decode_token(token, "access")
    assert claims["sub"] == "user-123"
    assert claims["role"] == "trader"


def test_refresh_token_contains_unique_identifier() -> None:
    token, token_id, _ = create_refresh_token("user-123")
    claims = decode_token(token, "refresh")
    assert claims["jti"] == token_id
