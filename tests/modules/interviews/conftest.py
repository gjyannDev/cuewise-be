import json

import pytest

from app.core.ai.fake import FakeProvider
from app.main import app
from app.modules.interviews.interviews_constants import DECISION_PROMPT_VERSION, Level, QuestionCategory
from app.modules.interviews.interviews_dependencies import (
    get_bank,
    get_clock,
    get_llm_provider,
)
from app.modules.interviews.interviews_schema import BankQuestion
from app.modules.interviews.interviews_utils import load_prompt


def _bank_question(qid, category="behavioral", roles=("general",), levels=tuple(Level)):
    return BankQuestion(
        id=qid,
        text=f"Question {qid}?",
        type=QuestionCategory(category),
        roles=list(roles),
        levels=list(levels),
    )


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
        body = {
            "role": "backend",
            "level": "junior",
            "interview_type": "behavioral",
            "question_count": 3,
        }
        body = {k: v for k, v in (body | overrides).items() if v is not None}
        return client.post("/api/v1/interviews", json=body, headers=auth_header(user))

    return _start


@pytest.fixture
def answer(client, auth_header):
    """POST an answer; `question_id` defaults to whatever the caller passes, body fields can be overridden."""

    def _answer(
        user,
        session_id,
        question_id,
        text="I built a prototype to compare both options.",
        **overrides,
    ):
        body = {"question_id": str(question_id), "answer": text} | overrides
        return client.post(
            f"/api/v1/interviews/{session_id}/messages",
            json=body,
            headers=auth_header(user),
        )

    return _answer


@pytest.fixture
def llm():
    """Swap the LLM for a scripted fake: `llm.script(...)` queues replies/errors; `llm.fake.calls` records inputs.

    Once the script runs out, every call returns a new valid behavioral question (allowed for behavioral and mixed
    interviews), so a test only scripts the turns it cares about.

    Decide calls (follow-ups) go to their own fake, `llm.decide`, scripted with `llm.script_decide(...)`; by default
    every decision is "next_question", so tests that only script questions behave as before follow-ups existed.
    """
    counter = iter(range(1, 1000))

    def unique_question() -> str:
        return _reply_json(f"Generated question number {next(counter)}?", "behavioral")

    class _LLM:
        fake = FakeProvider(default=unique_question)
        decide = FakeProvider(default=_decision_json())

        def script(self, *replies, on_call=None):
            self.fake = FakeProvider(replies, on_call=on_call, default=unique_question)
            return self.fake

        def script_decide(self, *replies, on_call=None, default=None):
            self.decide = FakeProvider(
                replies, on_call=on_call, default=default or _decision_json()
            )
            return self.decide

        # The provider the app gets: routes each call by its system prompt.
        def complete(self, messages, **kwargs):
            fake = self.decide if _DECISION_MARKER in messages[0].content else self.fake
            return fake.complete(messages, **kwargs)

        def close(self) -> None:
            pass

    handle = _LLM()
    app.dependency_overrides[get_llm_provider] = lambda: handle
    yield handle
    app.dependency_overrides.pop(get_llm_provider, None)


# A phrase only the decide prompt has (its role line, before the first placeholder), read from the prompt file.
_DECISION_MARKER = load_prompt(DECISION_PROMPT_VERSION).splitlines()[1].split("{{")[0]


def _decision_json(action="next_question", gap=None, note=None) -> str:
    return json.dumps({"action": action, "gap": gap} | ({"note": note} if note else {}))


@pytest.fixture
def decision_json():
    """Builds a reply in the exact shape the decide call must produce."""
    return _decision_json


def _reply_json(
    question="How would you design a rate limiter for a public API?",
    category="technical",
) -> str:
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
