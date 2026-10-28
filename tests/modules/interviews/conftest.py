import pytest

from app.main import app
from app.modules.interviews.interviews_constants import Level
from app.modules.interviews.interviews_dependencies import get_bank
from app.modules.interviews.interviews_schema import BankQuestion


def _bank_question(qid, category="behavioral", roles=("general",), levels=tuple(Level)):
    return BankQuestion(id=qid, text=f"Question {qid}?", type=category, roles=list(roles), levels=list(levels))


@pytest.fixture
def make_bank_question():
    return _bank_question


@pytest.fixture
def bank():
    """Small fixture bank wired into the app instead of the shipped mock file; mutable for snapshot tests."""
    questions = (
        [_bank_question(f"b{i}") for i in range(5)]
        + [_bank_question(f"t{i}", "technical") for i in range(5)]
        + [_bank_question("frontend-only", "technical", roles=["frontend"])]
    )
    app.dependency_overrides[get_bank] = lambda: questions
    yield questions
    app.dependency_overrides.pop(get_bank, None)


@pytest.fixture
def start_interview(client, auth_header, bank):
    """POST a setup for `user`; any field can be overridden, or dropped by passing None."""

    def _start(user, **overrides):
        body = {"role": "backend", "level": "junior", "interview_type": "behavioral", "question_count": 3}
        body = {k: v for k, v in (body | overrides).items() if v is not None}
        return client.post("/api/v1/interviews", json=body, headers=auth_header(user))

    return _start
