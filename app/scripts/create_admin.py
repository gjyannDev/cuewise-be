"""Create the first admin, or promote an existing user to admin.

Usage: uv run python -m app.scripts.create_admin <email>
"""

import argparse
from collections.abc import Callable
from getpass import getpass

from sqlalchemy.orm import Session

from app.db import models  # noqa: F401  (registers every model before the session is used)
from app.db.session import SessionLocal
from app.modules.auth.auth_controller import AuthController
from app.modules.auth.auth_repository import AuthRepository


def main(email: str, db: Session, prompt_password: Callable[[], str]) -> str:
    return AuthController(AuthRepository(db)).ensure_admin(email, prompt_password)


def _prompt_password() -> str:
    password = getpass("Password for the new admin: ")
    if password != getpass("Repeat password: "):
        raise SystemExit("Passwords do not match.")
    return password


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create or promote an admin user.")
    parser.add_argument("email")
    args = parser.parse_args()
    with SessionLocal() as session:
        result = main(args.email, session, _prompt_password)
    print(f"{args.email}: {result}")
