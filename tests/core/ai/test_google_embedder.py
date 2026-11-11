"""GoogleEmbedder: Gemini's native batchEmbedContents over httpx (knowledge-base-rag Step 3; AC9, AC10, EC7, EC14)."""

import json

import httpx
import pytest

from app.core.ai.embedder import EmbeddingKind, EmbeddingSizeError
from app.core.ai.google_embedder import GoogleEmbedder
from app.core.ai.provider import (
    LLMBadResponseError,
    LLMRateLimitError,
    LLMRequestError,
    LLMServerError,
    LLMTimeoutError,
)

API_KEY = "google-embed-secret-123"
DIMS = 4


class Clock:
    def __init__(self):
        self.now = 0.0
        self.sleeps: list[float] = []

    def __call__(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)
        self.now += seconds


@pytest.fixture
def clock():
    return Clock()


@pytest.fixture
def make_embedder(clock):
    """Embedder whose HTTP layer is a scripted list of responses (or exceptions), one per attempt."""

    def _make(*script, timeout=10.0, dimensions=DIMS):
        requests: list[httpx.Request] = []
        timeouts: list[dict] = []
        steps = list(script)

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            timeouts.append(request.extensions["timeout"])
            step = steps.pop(0)
            if isinstance(step, Exception):
                raise step
            return step

        embedder = GoogleEmbedder(
            api_key=API_KEY,
            model="gemini-embedding-001",
            dimensions=dimensions,
            base_url="https://google.test/v1beta",
            timeout_seconds=timeout,
            transport=httpx.MockTransport(handler),
            sleep=clock.sleep,
            clock=clock,
        )
        return embedder, requests, timeouts

    return _make


def ok(*vectors: list[float]) -> httpx.Response:
    return httpx.Response(200, json={"embeddings": [{"values": v} for v in vectors]})


V1 = [0.1, 0.2, 0.3, 0.4]
V2 = [0.4, 0.3, 0.2, 0.1]


@pytest.mark.parametrize(
    ("kind", "task_type"),
    [(EmbeddingKind.query, "RETRIEVAL_QUERY"), (EmbeddingKind.document, "RETRIEVAL_DOCUMENT")],
)
def test_request_carries_task_type_size_and_the_key_in_a_header_only(make_embedder, kind, task_type):  # AC10
    embedder, requests, _ = make_embedder(ok(V1, V2))

    embedder.embed(["first text", "second text"], kind=kind)

    [request] = requests
    assert request.method == "POST"
    assert request.url.path == "/v1beta/models/gemini-embedding-001:batchEmbedContents"
    assert request.headers["x-goog-api-key"] == API_KEY
    assert API_KEY not in str(request.url)
    body = json.loads(request.content)
    assert API_KEY not in request.content.decode()
    assert body == {
        "requests": [
            {
                "model": "models/gemini-embedding-001",
                "content": {"parts": [{"text": text}]},
                "taskType": task_type,
                "outputDimensionality": DIMS,
            }
            for text in ("first text", "second text")
        ]
    }


def test_a_valid_response_gives_one_vector_per_text_in_order(make_embedder):
    embedder, _, _ = make_embedder(ok(V1, V2))

    result = embedder.embed(["a", "b"], kind=EmbeddingKind.document)

    assert result.vectors == [V1, V2]
    assert result.model == "gemini-embedding-001"
    assert result.attempts == 1
    # batchEmbedContents reports no usage: never guessed.
    assert result.input_tokens is None
    assert embedder.model == "gemini-embedding-001" and embedder.dimensions == DIMS


def test_a_vector_of_the_wrong_length_is_a_size_error(make_embedder):  # EC14
    embedder, requests, _ = make_embedder(ok([0.1, 0.2, 0.3]))

    with pytest.raises(EmbeddingSizeError) as caught:
        embedder.embed(["a"], kind=EmbeddingKind.query)

    assert isinstance(caught.value, LLMBadResponseError)
    assert len(requests) == 1


@pytest.mark.parametrize(
    "response",
    [
        httpx.Response(200, content=b"not json"),
        httpx.Response(200, json={}),
        httpx.Response(200, json={"embeddings": [{"values": V1}]}),  # 2 texts, 1 vector
        httpx.Response(200, json={"embeddings": [{"values": V1}, {"values": ["x", 1, 2, 3]}]}),
    ],
)
def test_an_unusable_200_is_a_bad_response_and_not_retried(make_embedder, response):
    embedder, requests, _ = make_embedder(response)

    with pytest.raises(LLMBadResponseError):
        embedder.embed(["a", "b"], kind=EmbeddingKind.document)

    assert len(requests) == 1


@pytest.mark.parametrize(
    ("status", "error"),
    [(429, LLMRateLimitError), (500, LLMServerError), (503, LLMServerError)],
)
def test_429_and_5xx_are_retried_once_inside_the_budget(make_embedder, clock, status, error):  # EC7
    embedder, requests, _ = make_embedder(httpx.Response(status), ok(V1))

    result = embedder.embed(["a"], kind=EmbeddingKind.query, budget_seconds=5)

    assert len(requests) == 2 and result.attempts == 2
    assert len(clock.sleeps) == 1


@pytest.mark.parametrize(
    ("status", "error"),
    [(429, LLMRateLimitError), (503, LLMServerError)],
)
def test_only_one_retry_then_the_typed_error(make_embedder, status, error):
    embedder, requests, _ = make_embedder(httpx.Response(status), httpx.Response(status), ok(V1))

    with pytest.raises(error) as caught:
        embedder.embed(["a"], kind=EmbeddingKind.query, budget_seconds=5)

    assert len(requests) == 2 and caught.value.attempts == 2


def test_no_retry_starts_past_the_budget(make_embedder, clock):  # AC19: the start-time cap holds
    embedder, requests, _ = make_embedder(httpx.Response(503), ok(V1))

    with pytest.raises(LLMServerError):
        embedder.embed(["a"], kind=EmbeddingKind.query, budget_seconds=0.4)

    assert len(requests) == 1 and clock.sleeps == []


def test_each_attempt_waits_no_longer_than_the_budget_or_the_timeout(make_embedder):  # AC19
    embedder, _, timeouts = make_embedder(ok(V1), ok(V1), timeout=10.0)

    embedder.embed(["a"], kind=EmbeddingKind.query, budget_seconds=5)
    embedder.embed(["a"], kind=EmbeddingKind.document)

    assert timeouts[0]["read"] == 5
    assert timeouts[1]["read"] == 10


def test_a_timeout_maps_to_a_timeout_error(make_embedder):  # EC7
    embedder, requests, _ = make_embedder(httpx.ReadTimeout("slow"), httpx.ReadTimeout("slow"))

    with pytest.raises(LLMTimeoutError):
        embedder.embed(["a"], kind=EmbeddingKind.query, budget_seconds=5)

    assert len(requests) == 2


def test_a_dropped_connection_is_a_server_error(make_embedder):
    embedder, _, _ = make_embedder(httpx.ConnectError("refused"), httpx.ConnectError("refused"))

    with pytest.raises(LLMServerError):
        embedder.embed(["a"], kind=EmbeddingKind.query, budget_seconds=5)


@pytest.mark.parametrize("status", [400, 401, 403])
def test_other_4xx_are_not_retried(make_embedder, status):  # a bad key sends the same broken request again
    embedder, requests, _ = make_embedder(httpx.Response(status))

    with pytest.raises(LLMRequestError):
        embedder.embed(["a"], kind=EmbeddingKind.query)

    assert len(requests) == 1


def test_errors_never_carry_the_key_or_the_text(make_embedder):  # AC20
    embedder, _, _ = make_embedder(httpx.Response(400), ok([0.1]))

    with pytest.raises(LLMRequestError) as rejected:
        embedder.embed(["a private job description"], kind=EmbeddingKind.query)
    with pytest.raises(EmbeddingSizeError) as wrong_size:
        embedder.embed(["a private job description"], kind=EmbeddingKind.query)

    for exc in (rejected.value, wrong_size.value):
        assert API_KEY not in str(exc) and "private" not in str(exc)
