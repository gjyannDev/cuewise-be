import pytest
from pydantic import ValidationError
from sqlalchemy import func, select

from app.core.security import verify_password
from app.modules.auth.auth_constants import Role
from app.modules.auth.auth_model import User
from app.scripts.create_admin import main


def _no_prompt():
    raise AssertionError("password must not be asked for an existing user")


def test_unknown_email_creates_an_active_admin(db):  # AC11, EC17
    result = main("boss@example.com", db, prompt_password=lambda: "admin-pass-123")

    user = db.scalar(select(User).where(User.email == "boss@example.com"))
    assert result == "created"
    assert user.role == Role.admin
    assert user.is_active is True
    assert verify_password("admin-pass-123", user.password_hash)


def test_existing_user_is_promoted_without_touching_the_password(db, make_user):  # AC11, EC17
    user = make_user(email="ana@example.com", password="original-pass")
    original_hash = user.password_hash

    result = main("ana@example.com", db, prompt_password=_no_prompt)

    db.refresh(user)
    assert result == "promoted"
    assert user.role == Role.admin
    assert user.password_hash == original_hash


def test_running_twice_is_a_no_op(db):  # AC11, EC17
    main("boss@example.com", db, prompt_password=lambda: "admin-pass-123")

    second = main("boss@example.com", db, prompt_password=_no_prompt)

    assert second == "unchanged"
    assert db.scalar(select(func.count()).select_from(User)) == 1


def test_new_admin_password_follows_registration_rules(db):  # AC11, inferred: weak bootstrap password
    with pytest.raises(ValidationError):
        main("boss@example.com", db, prompt_password=lambda: "short")

    assert db.scalar(select(func.count()).select_from(User)) == 0


def test_invalid_email_is_rejected_before_prompting(db):  # inferred: typo in CLI arg
    with pytest.raises(ValidationError):
        main("not-an-email", db, prompt_password=_no_prompt)
