"""The vector retriever (U3b2 Step 4, AC3): a LangChain `BaseRetriever` over the search function the service passes in."""

import uuid
from typing import NamedTuple

from app.modules.interviews.ai.interviews_retrieve import VectorRetriever, nearest

VECTOR = [0.1, 0.2, 0.3]


class Chunk(NamedTuple):
    id: uuid.UUID
    note_key: str
    competency: str
    text: str


A = Chunk(uuid.uuid7(), "a", "system_design", "Note A")
B = Chunk(uuid.uuid7(), "b", "testing", "Note B")


def recording_search(results):
    calls = []

    def search(vector):
        calls.append(vector)
        return results

    return search, calls


def test_invoke_returns_documents_in_search_order_carrying_id_competency_text_and_score():
    search, calls = recording_search([(A, 0.9), (B, 0.4)])

    documents = VectorRetriever(search=search, vector=VECTOR).invoke("")

    assert calls == [VECTOR]
    assert [(d.page_content, d.metadata) for d in documents] == [
        ("Note A", {"chunk_id": A.id, "competency": "system_design", "score": 0.9}),
        ("Note B", {"chunk_id": B.id, "competency": "testing", "score": 0.4}),
    ]


def test_nearest_returns_plain_chunks_and_applies_no_similarity_floor():
    search, _ = recording_search([(A, 0.9), (B, 0.01)])

    found = nearest(search, VECTOR)

    assert [(n.chunk_id, n.competency, n.text, n.score) for n in found] == [
        (A.id, "system_design", "Note A", 0.9),
        (B.id, "testing", "Note B", 0.01),
    ]


def test_nothing_found_is_an_empty_list():
    search, _ = recording_search([])

    assert nearest(search, VECTOR) == []
