import json

import pytest

from app.core.ai.fake import FakeProvider
from app.main import app
from app.modules.interviews.interviews_constants import Level
from app.modules.interviews.interviews_dependencies import get_bank, get_clock, get_llm_provider
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


@pytest.fixture
def answer(client, auth_header):
    """POST an answer; `question_id` defaults to whatever the caller passes, body fields can be overridden."""

    def _answer(user, session_id, question_id, text="I built a prototype to compare both options.", **overrides):
        body = {"question_id": str(question_id), "answer": text} | overrides
        return client.post(f"/api/v1/interviews/{session_id}/messages", json=body, headers=auth_header(user))

    return _answer


@pytest.fixture
def llm():
    """Swap the LLM for a scripted fake: `llm.script(...)` queues replies/errors; `llm.fake.calls` records inputs.

    Once the script runs out, every call returns a new valid behavioral question (allowed for behavioral and mixed
    interviews), so a test only scripts the turns it cares about.
    """
    counter = iter(range(1, 1000))

    def unique_question() -> str:
        return _reply_json(f"Generated question number {next(counter)}?", "behavioral")

    class _LLM:
        fake = FakeProvider(default=unique_question)

        def script(self, *replies, on_call=None):
            self.fake = FakeProvider(replies, on_call=on_call, default=unique_question)
            app.dependency_overrides[get_llm_provider] = lambda: self.fake
            return self.fake

    handle = _LLM()
    app.dependency_overrides[get_llm_provider] = lambda: handle.fake
    yield handle
    app.dependency_overrides.pop(get_llm_provider, None)


def _reply_json(question="How would you design a rate limiter for a public API?", category="technical") -> str:
    return json.dumps({"question": question, "category": category})


@pytest.fixture
def reply_json():
    """Builds a reply in the exact shape the interviewer LLM must produce."""
    return _reply_json


@pytest.fixture
def clock():
    """Fake monotonic clock for the per-turn LLM budget; tests advance it (e.g. inside a fake provider's on_call)."""

    class _Clock:
        now = 1000.0

        def __call__(self) -> float:
            return self.now

        def advance(self, seconds: float) -> None:
            self.now += seconds

    fake = _Clock()
    app.dependency_overrides[get_clock] = lambda: fake
    yield fake
    app.dependency_overrides.pop(get_clock, None)
