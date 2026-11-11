"""The embedding contract features code against, separate from the chat `LLMProvider`.

An embedding turns a text into a list of numbers (a vector) such that texts with similar meaning get vectors that
point in similar directions. Comparing two vectors (cosine similarity: 1 = same direction, 0 = unrelated) then
measures how close two texts are in meaning, even when they share no words ("REST API design" vs "designing HTTP
endpoints"). Retrieval embeds every note once (as a *document*) and the job description at interview start (as a
*query*); models trained for retrieval embed the two kinds slightly differently so that a short question lands near
the long passage that answers it.

Failures raise the `LLMError` subclasses from `provider.py`, like the transcriber, so one set of retry rules applies.
"""

from collections.abc import Sequence
from enum import StrEnum
from typing import Protocol

from pydantic import BaseModel

from .provider import LLMBadResponseError


class EmbeddingKind(StrEnum):
    query = "query"
    document = "document"


class EmbeddingResult(BaseModel):
    # One vector per input text, in input order.
    vectors: list[list[float]]
    model: str
    # None when the vendor doesn't report usage; never guessed.
    input_tokens: int | None
    latency_ms: int
    attempts: int


class EmbeddingSizeError(LLMBadResponseError):
    """A vector of another length than configured. Vectors of different sizes can't be compared, and the database
    column has a fixed size, so this is never retried or stored."""


class Embedder(Protocol):
    @property
    def model(self) -> str: ...

    @property
    def dimensions(self) -> int: ...

    def embed(
        self,
        texts: Sequence[str],
        *,
        kind: EmbeddingKind,
        # The caller's whole time budget for this call, retries included; None = one attempt's timeout.
        budget_seconds: float | None = None,
    ) -> EmbeddingResult: ...

    def close(self) -> None: ...
