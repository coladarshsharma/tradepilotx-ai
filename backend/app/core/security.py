from datetime import datetime, timedelta, timezone
from typing import Any
from uuid import uuid4

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import get_settings

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    return password_context.verify(password, password_hash)


def create_token(subject: str, token_type: str, expires_delta: timedelta, extra: dict[str, Any] | None = None) -> tuple[str, str, datetime]:
    settings = get_settings()
    now = datetime.now(timezone.utc)
    expires_at = now + expires_delta
    token_id = str(uuid4())
    payload: dict[str, Any] = {
        "sub": subject,
        "typ": token_type,
        "jti": token_id,
        "iat": now,
        "exp": expires_at,
    }
    if extra:
        payload.update(extra)
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm), token_id, expires_at


def create_access_token(user_id: str, role: str) -> str:
    settings = get_settings()
    token, _, _ = create_token(user_id, "access", timedelta(minutes=settings.access_token_expire_minutes), {"role": role})
    return token


def create_refresh_token(user_id: str) -> tuple[str, str, datetime]:
    settings = get_settings()
    return create_token(user_id, "refresh", timedelta(days=settings.refresh_token_expire_days))


def create_action_token(user_id: str, token_type: str, expires_delta: timedelta) -> str:
    token, _, _ = create_token(user_id, token_type, expires_delta)
    return token


def decode_token(token: str, expected_type: str | None = None) -> dict[str, Any]:
    settings = get_settings()
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
    except JWTError as exc:
        raise ValueError("Invalid or expired token") from exc
    if expected_type and payload.get("typ") != expected_type:
        raise ValueError("Unexpected token type")
    if not payload.get("sub") or not payload.get("jti"):
        raise ValueError("Malformed token")
    return payload
