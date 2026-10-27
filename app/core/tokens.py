from datetime import UTC, datetime, timedelta
from typing import Any

import jwt

from app.core.config import settings
from app.core.errors import TokenExpiredError, TokenInvalidError

_REQUIRED_CLAIMS = ["sub", "exp", "iat", "iss", "aud"]


def create_token(user_id: int, role: str) -> str:
    # role is informational for clients; authorization always re-reads it from the DB.
    now = datetime.now(UTC)
    claims = {
        "sub": str(user_id),
        "role": role,
        "iat": now,
        "exp": now + timedelta(minutes=settings.access_token_expire_minutes),
        "iss": settings.jwt_issuer,
        "aud": settings.jwt_audience,
    }
    return jwt.encode(claims, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)


def decode_token(token: str) -> dict[str, Any]:
    try:
        return jwt.decode(
            token,
            settings.jwt_secret_key,
            # Pinned list: never trust the token's own "alg" header (blocks alg=none / key confusion).
            algorithms=[settings.jwt_algorithm],
            issuer=settings.jwt_issuer,
            audience=settings.jwt_audience,
            options={"require": _REQUIRED_CLAIMS},
        )
    except jwt.ExpiredSignatureError as exc:
        raise TokenExpiredError("Access token has expired") from exc
    except jwt.PyJWTError as exc:
        raise TokenInvalidError("Access token is invalid") from exc
