from datetime import UTC, datetime, timedelta
from uuid import uuid7

import jwt
import pytest

from app.core.config import settings
from app.core.errors import TokenExpiredError, TokenInvalidError
from app.core.tokens import create_token, decode_token


def _sign(key=None, alg=None, **overrides):
    now = datetime.now(UTC)
    claims = {
        "sub": "1",
        "role": "user",
        "iat": now,
        "exp": now + timedelta(minutes=5),
        "iss": settings.jwt_issuer,
        "aud": settings.jwt_audience,
    } | overrides
    return jwt.encode(claims, key or settings.jwt_secret_key, algorithm=alg or settings.jwt_algorithm)


def test_token_round_trips_all_claims():  # AC2, R3
    user_id = uuid7()

    claims = decode_token(create_token(user_id, "admin"))

    assert claims["sub"] == str(user_id)
    assert claims["role"] == "admin"
    assert claims["iss"] == settings.jwt_issuer
    assert claims["aud"] == settings.jwt_audience
    assert claims["exp"] - claims["iat"] == settings.access_token_expire_minutes * 60


def test_expired_token_is_rejected_as_expired():  # EC3
    past = datetime.now(UTC) - timedelta(hours=2)
    token = _sign(iat=past, exp=past + timedelta(minutes=1))

    with pytest.raises(TokenExpiredError):
        decode_token(token)


def test_tampered_payload_is_invalid():  # EC4
    header, _payload, signature = create_token(uuid7(), "user").split(".")
    forged_payload = jwt.utils.base64url_encode(b'{"sub":"1","role":"admin"}').decode()

    with pytest.raises(TokenInvalidError):
        decode_token(f"{header}.{forged_payload}.{signature}")


def test_token_signed_with_other_secret_is_invalid():  # EC4
    token = _sign(key="another-secret-key-that-is-at-least-32-characters")

    with pytest.raises(TokenInvalidError):
        decode_token(token)


def test_unsigned_alg_none_token_is_invalid():  # EC5
    now = datetime.now(UTC)
    claims = {
        "sub": "1",
        "role": "admin",
        "iat": now,
        "exp": now + timedelta(minutes=5),
        "iss": settings.jwt_issuer,
        "aud": settings.jwt_audience,
    }
    token = jwt.encode(claims, None, algorithm="none")  # pyright: ignore[reportArgumentType]

    with pytest.raises(TokenInvalidError):
        decode_token(token)


def test_token_signed_with_unpinned_algorithm_is_invalid():  # EC5
    with pytest.raises(TokenInvalidError):
        decode_token(_sign(alg="HS512"))


@pytest.mark.parametrize("claim", ["iss", "aud"])
def test_wrong_issuer_or_audience_is_invalid(claim):  # EC6
    with pytest.raises(TokenInvalidError):
        decode_token(_sign(**{claim: "someone-else"}))


@pytest.mark.parametrize("missing", ["sub", "exp", "iat", "iss", "aud"])
def test_token_missing_required_claim_is_invalid(missing):  # EC7, inferred: incomplete token
    now = datetime.now(UTC)
    claims = {
        "sub": "1",
        "iat": now,
        "exp": now + timedelta(minutes=5),
        "iss": settings.jwt_issuer,
        "aud": settings.jwt_audience,
    }
    del claims[missing]
    token = jwt.encode(claims, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)

    with pytest.raises(TokenInvalidError):
        decode_token(token)


def test_garbage_string_is_invalid():  # EC4, inferred: not a JWT at all
    with pytest.raises(TokenInvalidError):
        decode_token("not-a-jwt")
