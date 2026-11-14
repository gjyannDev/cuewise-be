"""RetrievalService.retrieve with the candidate profile's query (resume-aware-interview Step 8; seam S3).

AC15, AC16, EC7, EC14, EC16. Reuses the vector set-up of test_retrieval_service.py: fixed directions per text, so which
note is nearest is decided by the test. Backend/mid eligible notes: API design (1,0,0), Caching (0,1,0),
Testing (0,0,1), Communication (0.5,0.5,0). The job-description query (0.9,0.1,0) ranks API, Communication, Caching,
Testing; the profile query (0,0,1) ranks Testing first.
"""


# `corpus` is a pytest fixture imported from test_retrieval_service.py: using it as a test parameter is how pytest
# injects it, not a redefinition.
# ruff: noqa: F811

import logging

from app.core.ai.embedder import EmbeddingKind
from app.core.ai.fake import EmbedCall, FakeEmbedder
from app.core.ai.provider import LLMServerError
from app.modules.interviews.constants.interviews_constants import (
    RETRIEVAL_TIME_CAP_SECONDS,
    RetrievalMode,
)
from tests.modules.interviews.services.test_retrieval_service import (
    QUERY,
    SESSION,
    Steps,
    corpus,  # noqa: F401 (a fixture)
    service,
    vec,
)

PROFILE_QUERY = "ZZPROFILE pytest, test automation, QA Engineer"


def retrieve(svc, *, query=QUERY, profile_query=PROFILE_QUERY):
    return svc.retrieve(SESSION, "backend", "mid", summary=None, job_description=query, profile_query=profile_query)


def competencies(result) -> list[str]:
    return [note.competency for note in result.notes]


def embedder_for(corpus, **kwargs) -> FakeEmbedder:
    return FakeEmbedder({**corpus, PROFILE_QUERY: vec(0, 0, 1)}, **kwargs)


def test_without_a_profile_query_the_call_is_todays(db, corpus):  # AC15, EC2
    embedder = embedder_for(corpus)

    result = retrieve(service(db, embedder, top_k=3), profile_query=None)

    assert embedder.calls == [EmbedCall((QUERY,), EmbeddingKind.query, RETRIEVAL_TIME_CAP_SECONDS)]
    assert competencies(result) == ["API design", "Communication", "Caching"]
    assert result.profile_notes == 0


def test_with_a_profile_one_batched_call_embeds_both_and_the_quota_merges(db, corpus):  # AC15
    embedder = embedder_for(corpus)

    result = retrieve(service(db, embedder, top_k=3, profile_slots=1))

    # One request for both queries (the real embedder batches them), the job description still part of it.
    assert embedder.calls == [EmbedCall((QUERY, PROFILE_QUERY), EmbeddingKind.query, RETRIEVAL_TIME_CAP_SECONDS)]
    assert result.mode == RetrievalMode.vector
    assert competencies(result) == ["API design", "Communication", "Testing"]
    assert [note.rank for note in result.notes] == [1, 2, 3]
    assert result.profile_notes == 1


def test_zero_profile_slots_gives_the_job_description_ranking(db, corpus):  # the decision rule's switch
    result = retrieve(service(db, embedder_for(corpus), top_k=3, profile_slots=0))

    assert competencies(result) == ["API design", "Communication", "Caching"]
    assert result.profile_notes == 0


def test_without_a_job_description_the_profile_ranks_alone_with_the_full_k(db, corpus):  # EC7
    embedder = embedder_for(corpus)

    result = retrieve(service(db, embedder, top_k=3), query=None)

    assert embedder.calls == [EmbedCall((PROFILE_QUERY,), EmbeddingKind.query, RETRIEVAL_TIME_CAP_SECONDS)]
    assert result.mode == RetrievalMode.vector
    assert competencies(result)[0] == "Testing" and len(result.notes) == 3
    assert result.profile_notes == 3


def test_a_job_description_below_the_threshold_falls_back_to_filter_mode(db, corpus):  # EC16
    # API design scores 0.994 against the job description, Testing exactly 1.0 against the profile.
    result = retrieve(service(db, embedder_for(corpus), min_similarity=0.999))

    assert result.mode == RetrievalMode.filter
    assert result.outcome == "retrieval_degraded:below_threshold"
    assert result.profile_notes == 0


def test_an_embedding_failure_degrades_to_filter_mode_and_the_start_goes_on(db, corpus):  # EC14
    embedder = embedder_for(corpus, errors=[LLMServerError("down")])

    result = retrieve(service(db, embedder))

    assert len(embedder.calls) == 1
    assert result.mode == RetrievalMode.filter and result.outcome == "retrieval_degraded:embedder_error"
    assert result.profile_notes == 0


def test_the_trace_and_the_log_get_counts_and_ids_never_the_query(db, corpus, app_logs):  # AC16
    steps = Steps()

    result = retrieve(service(db, embedder_for(corpus), top_k=3, profile_slots=1, tracer=steps))

    [(_, metadata, output)] = steps.recorded
    assert output["profile_notes"] == 1 and output["count"] == 3
    assert output["chunk_ids"] == [str(note.chunk_id) for note in result.notes]
    assert "ZZPROFILE" not in repr((metadata, output))
    [line] = [r.getMessage() for r in app_logs.records if r.getMessage().startswith("retrieval ")]
    assert "profile_notes=1" in line and "ZZPROFILE" not in line
    assert not [r for r in app_logs.records if "ZZPROFILE" in r.getMessage()]
    assert app_logs.records[-1].levelno <= logging.INFO
