"""Vector search as a LangChain retriever (U3b2).

A retriever is LangChain's "text in, relevant documents out" building block. This one is bound to a vector the
service already computed, not to a query text: the service embeds the job-description and profile queries in one
batched call, so a retriever that embedded its own query would add a second round trip. The search itself is the
repository's `nearest_chunks`, handed in by the service as a function (this folder never imports a repository).

The similarity floor, ranks and the merge stay in the service: this is search only. `nearest` is what the service
calls, so no LangChain type leaves this folder.
"""

import uuid
from collections.abc import Callable, Sequence
from typing import NamedTuple, Protocol

from langchain_core.callbacks import CallbackManagerForRetrieverRun
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever


class _Chunk(Protocol):
    @property
    def id(self) -> uuid.UUID: ...
    @property
    def competency(self) -> str: ...
    @property
    def text(self) -> str: ...


type VectorSearch = Callable[[list[float]], Sequence[tuple[_Chunk, float]]]


class Nearest(NamedTuple):
    chunk_id: uuid.UUID
    competency: str
    text: str
    score: float


class VectorRetriever(BaseRetriever):
    search: VectorSearch
    vector: list[float]

    def _get_relevant_documents(self, query: str, *, run_manager: CallbackManagerForRetrieverRun) -> list[Document]:
        # `query` is unused: the vector is the query, already embedded.
        return [
            Document(
                page_content=chunk.text,
                metadata={"chunk_id": chunk.id, "competency": chunk.competency, "score": score},
            )
            for chunk, score in self.search(self.vector)
        ]


def nearest(search: VectorSearch, vector: list[float]) -> list[Nearest]:
    """The search's chunks for `vector`, most similar first, through the retriever."""
    documents = VectorRetriever(search=search, vector=vector).invoke("")
    return [
        Nearest(d.metadata["chunk_id"], d.metadata["competency"], d.page_content, d.metadata["score"])
        for d in documents
    ]
