import json
from typing import NamedTuple

import pytest

from app.core.ai.fake import FakeProvider, FakeTranscriber
from app.core.rate_limit import RateLimiter
from app.main import app
from app.modules.interviews.constants.interviews_constants import (
    DECISION_PROMPT_VERSION,
    FEEDBACK_SCORE_PROMPT_VERSION,
    FEEDBACK_WRITE_PROMPT_VERSION,
    TRANSCRIPTIONS_PER_MINUTE,
    Level,
    QuestionCategory,
)
from app.modules.interviews.dependencies.interviews_shared_dependencies import (
    get_bank,
    get_clock,
    get_llm_provider,
    get_transcriber,
)
from app.modules.interviews.dependencies.interviews_transcription_dependencies import (
    get_transcription_limiter,
)
from app.modules.interviews.schemas.interviews_schema import BankQuestion
from app.modules.interviews.utils.interviews_utils import load_prompt


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


class StreamedTurn(NamedTuple):
    status_code: int
    headers: dict[str, str]
    # (event name, parsed JSON data) in arrival order; comment lines (heartbeats) are counted, not listed.
    events: list[tuple[str, dict]]
    comments: int
    # The JSON body, for a request that failed before any stream opened.
    body: dict | None

    def names(self) -> list[str]:
        return [name for name, _ in self.events]

    def flow(self) -> list[str]:
        """Event names with each run of question.delta shown once: the shape of the stream, whatever the chunking."""
        return [name for i, name in enumerate(self.names()) if name != "question.delta" or self.names()[i - 1 : i] != [name]]

    def question(self) -> str:
        """The streamed question as the client shows it: deltas appended, a reset clearing them."""
        text = ""
        for name, data in self.events:
            text = "" if name == "reset" else text + data["text"] if name == "question.delta" else text
        return text

    def data(self, name: str) -> list[dict]:
        return [data for event, data in self.events if event == name]


def parse_sse(text: str) -> tuple[list[tuple[str, dict]], int]:
    """Split a text/event-stream body into (event, data) pairs; returns them and the number of comment frames."""
    events, comments = [], 0
    for frame in text.replace("\r\n", "\n").split("\n\n"):
        lines = [line for line in frame.split("\n") if line]
        if not lines:
            continue
        if all(line.startswith(":") for line in lines):
            comments += 1
            continue
        fields = dict(line.split(": ", 1) for line in lines if not line.startswith(":"))
        events.append((fields.get("event", "message"), json.loads(fields["data"])))
    return events, comments


@pytest.fixture
def stream_answer(client, auth_header):
    """POST an answer to the streaming endpoint and read the whole stream (or the JSON error that replaced it)."""

    def _stream(user, session_id, question_id, text="I built a prototype to compare both options.", **overrides):
        body = {"question_id": str(question_id), "answer": text} | overrides
        with client.stream(
            "POST",
            f"/api/v1/interviews/{session_id}/messages/stream",
            json=body,
            headers=auth_header(user),
        ) as response:
            raw = response.read().decode()
            headers = dict(response.headers)
            status = response.status_code
        if headers.get("content-type", "").startswith("text/event-stream"):
            events, comments = parse_sse(raw)
            return StreamedTurn(status, headers, events, comments, None)
        return StreamedTurn(status, headers, [], 0, json.loads(raw))

    return _stream


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
        fake = FakeProvider(default=unique_question, stream_format=as_v5_text)
        decide = FakeProvider(default=_decision_json())
        # End-of-interview feedback: unscripted, both reply with text that breaks their contract.
        score = FakeProvider()
        write = FakeProvider()

        def script(self, *replies, on_call=None):
            self.fake = FakeProvider(replies, on_call=on_call, default=unique_question, stream_format=as_v5_text)
            return self.fake

        def script_decide(self, *replies, on_call=None, default=None):
            self.decide = FakeProvider(
                replies, on_call=on_call, default=default or _decision_json()
            )
            return self.decide

        def script_score(self, *replies, on_call=None):
            self.score = FakeProvider(replies, on_call=on_call)
            return self.score

        def script_write(self, *replies, on_call=None):
            self.write = FakeProvider(replies, on_call=on_call)
            return self.write

        # The provider the app gets: routes each call by its system prompt.
        def complete(self, messages, **kwargs):
            system = messages[0].content
            if _SCORE_MARKER in system:
                return self.score.complete(messages, **kwargs)
            if _WRITE_MARKER in system:
                return self.write.complete(messages, **kwargs)
            fake = self.decide if _DECISION_MARKER in system else self.fake
            return fake.complete(messages, **kwargs)

        # Only write calls stream (the streamed turn's interviewer_v5); they share the write fake's script.
        def stream(self, messages, **kwargs):
            return self.fake.stream(messages, **kwargs)

        def close(self) -> None:
            pass

        async def aclose(self) -> None:
            pass

    handle = _LLM()
    app.dependency_overrides[get_llm_provider] = lambda: handle
    yield handle
    app.dependency_overrides.pop(get_llm_provider, None)


# A phrase only the decide prompt has (its role line, before the first placeholder), read from the prompt file.
_DECISION_MARKER = load_prompt(DECISION_PROMPT_VERSION).splitlines()[1].split("{{")[0]
_SCORE_MARKER = load_prompt(FEEDBACK_SCORE_PROMPT_VERSION).splitlines()[1].split("{{")[0]
_WRITE_MARKER = load_prompt(FEEDBACK_WRITE_PROMPT_VERSION).splitlines()[1].split("{{")[0]


def as_v5_text(reply: str) -> str:
    """A write reply scripted in v4's JSON, as interviewer_v5 streams it (a CATEGORY line for main questions, then the
    text). Anything else (broken JSON, plain text) streams unchanged, so an invalid script stays invalid."""
    try:
        data = json.loads(reply)
    except ValueError:
        return reply
    if not isinstance(data, dict) or not isinstance(data.get("question"), str) or set(data) - {"question", "category"}:
        return reply
    return f"CATEGORY: {data['category']}\n{data['question']}" if "category" in data else data["question"]


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


@pytest.fixture
def anyio_backend():
    """Async tests (`pytest.mark.anyio`, anyio's own pytest plugin) run on asyncio only, like the app."""
    return "asyncio"


WEBM_AUDIO = b"\x1a\x45\xdf\xa3" + b"\x00" * 256


class _Stt:
    """The speech-to-text seam of a test: a scripted transcriber and a fresh per-test rate limiter."""

    def __init__(self):
        self.fake: FakeTranscriber | None = FakeTranscriber()
        self.limiter = RateLimiter(limit=TRANSCRIPTIONS_PER_MINUTE, window_seconds=60)

    def script(self, *replies, duration: float | None = 12.5) -> None:
        self.fake = FakeTranscriber(replies, duration=duration)

    def disable(self) -> None:
        """No transcriber configured (DEEPGRAM_API_KEY blank)."""
        self.fake = None


@pytest.fixture
def stt():
    state = _Stt()
    app.dependency_overrides[get_transcriber] = lambda: state.fake
    app.dependency_overrides[get_transcription_limiter] = lambda: state.limiter
    yield state
    app.dependency_overrides.pop(get_transcriber, None)
    app.dependency_overrides.pop(get_transcription_limiter, None)


@pytest.fixture
def transcribe(client, auth_header, stt):
    """POST a recording to the transcription endpoint; `audio=None` sends no file part at all."""

    def _transcribe(user, session_id, audio=WEBM_AUDIO, content_type="audio/webm;codecs=opus", headers=None):
        files = None if audio is None else {"audio": ("answer.webm", audio, content_type)}
        return client.post(
            f"/api/v1/interviews/{session_id}/transcriptions",
            files=files,
            headers=auth_header(user) if headers is None else headers,
        )

    return _transcribe
