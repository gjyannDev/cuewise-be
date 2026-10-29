import pytest

from app.core.ai.fake import FakeProvider
from app.main import app
from app.modules.interviews.interviews_constants import Level
from app.modules.interviews.interviews_dependencies import get_bank, get_llm_provider
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
    """Swap the LLM for a scripted fake: `llm.script(...)` queues replies/errors; `llm.fake.calls` records inputs."""

    class _LLM:
        fake = FakeProvider()

        def script(self, *replies, on_call=None):
            self.fake = FakeProvider(replies, on_call=on_call)
            app.dependency_overrides[get_llm_provider] = lambda: self.fake
            return self.fake

    handle = _LLM()
    app.dependency_overrides[get_llm_provider] = lambda: handle.fake
    yield handle
    app.dependency_overrides.pop(get_llm_provider, None)
