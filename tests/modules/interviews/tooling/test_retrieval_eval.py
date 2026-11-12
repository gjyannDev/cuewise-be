"""`run_retrieval` as a Langfuse experiment run (langfuse-experiments Step 5; AC1-AC3, AC5, AC7-AC10, EC4, EC8, EC9).

A three-note corpus is ingested into the SQLite test database with fixed vectors, so which note ranks first for each
query is decided by the test. The fake Langfuse client records the run; nothing touches the network or git.
"""

import re
from contextlib import nullcontext
from types import SimpleNamespace

import pytest
from sqlalchemy.exc import OperationalError

from app.core.ai.fake import FakeEmbedder
from app.core.ai.provider import LLMServerError
from app.core.ai.tracing import Tracer
from app.modules.interviews.constants.interviews_constants import (
    KNOWLEDGE_VECTOR_SIZE,
    RETRIEVAL_MIN_SIMILARITY,
    JobRole,
    Level,
)
from app.modules.interviews.repositories.interviews_knowledge_repository import (
    KnowledgeRepository,
)
from app.modules.interviews.services.interviews_knowledge_service import ingest_corpus
from app.modules.interviews.tooling import interviews_rag_evals as rag_module
from app.modules.interviews.tooling.interviews_eval_runs import notes_fingerprint
from app.modules.interviews.tooling.interviews_rag_evals import (
    RetrievalCase,
    run_retrieval,
)
from app.modules.interviews.utils.interviews_knowledge_utils import (
    embedding_text,
    parse_note,
)
from tests.fake_langfuse import FakeLangfuse


def vec(*head: float) -> list[float]:
    return [*head, *[0.0] * (KNOWLEDGE_VECTOR_SIZE - len(head))]


NOTES = [("api.md", "API design", vec(1, 0, 0)), ("cache.md", "Caching", vec(0, 1, 0)), ("tests.md", "Testing", vec(0, 0, 1))]
API, TESTS = "api.md#API design", "tests.md#Testing"


@pytest.fixture
def corpus(db):
    """Ingests the three notes; returns the vector each note text gets (the embedder must answer the same)."""
    vectors, chunks = {}, []
    for name, heading, direction in NOTES:
        text = f"---\nroles: backend\nlevels: mid\nsource: user\n---\n## {heading}\nWhat to probe about {heading}.\n"
        [chunk] = parse_note(name, text).chunks
        chunks.append(chunk._replace(order=len(chunks)))
        vectors[embedding_text(chunk)] = direction
    ingest_corpus(chunks, FakeEmbedder(vectors), KnowledgeRepository(db))
    return vectors


def labelled():
    """15 cases with the kinds the label rules require: most expect API design first; the last expects Testing."""
    kinds = ["synonym"] * 3 + ["vague", "role_boundary"] + ["plain"] * 10
    cases = [
        RetrievalCase(id=f"q{i}", kind=kind, role=JobRole.backend, level=Level.mid, query=f"query {i}", expected=[API])
        for i, kind in enumerate(kinds)
    ]
    cases[-1] = cases[-1].model_copy(update={"expected": [TESTS]})
    return cases


def embedder(corpus, **kwargs):
    queries = {f"query {i}": vec(0.9, 0.1, 0) for i in range(15)}
    return FakeEmbedder({**corpus, **queries}, **kwargs)


@pytest.fixture
def lf(monkeypatch):
    monkeypatch.setattr(rag_module, "git_commit", lambda: "abc1234")
    return FakeLangfuse()


def quiet(client):
    return Tracer(client, propagate=lambda **_: nullcontext())


def run(db, corpus, tracer, **kwargs):
    fields = {"tracer": tracer, "cases": labelled(), "pause": 0.0} | kwargs
    return run_retrieval(KnowledgeRepository(db), fields.pop("embedder", None) or embedder(corpus), **fields)


def test_one_run_with_one_result_per_case(db, corpus, lf):  # AC1, D1 (no repeat for retrieval)
    assert run(db, corpus, quiet(lf)) == 0

    [experiment] = lf.experiments
    assert experiment["item_ids"] == [f"retrieval:q{i}" for i in range(15)]
    stored = lf.datasets["interviews-eval/retrieval"]
    assert stored["retrieval:q0"]["input"] == {"query": "query 0", "role": "backend", "level": "mid"}
    assert stored["retrieval:q0"]["expected_output"] == {"notes": [API]}
    assert stored["retrieval:q0"]["metadata"] == {"kind": "synonym"}


def test_the_run_carries_the_embedding_setup_and_the_notes_it_ran_on(db, corpus, lf):  # AC2
    run(db, corpus, quiet(lf), note="after editing the caching note")

    [experiment] = lf.experiments
    meta = experiment["metadata"]
    hashes = [c.content_hash for c in KnowledgeRepository(db).active_chunks()]
    assert meta["task"] == "retrieval" and meta["commit"] == "abc1234"
    assert (meta["embedding_model"], meta["embedding_dimensions"]) == ("fake-embedding", "768")
    assert meta["threshold"] == str(RETRIEVAL_MIN_SIMILARITY)
    assert meta["notes_fingerprint"] == notes_fingerprint(hashes)
    assert experiment["description"] == "after editing the caching note" and meta["note"] == experiment["description"]
    fingerprint = notes_fingerprint(hashes)[:6]
    assert experiment["run_name"].startswith(f"retrieval/threshold-{RETRIEVAL_MIN_SIMILARITY}/notes-{fingerprint}/")
    assert all(isinstance(v, str) for v in meta.values())


def summary_numbers(out):
    vector = re.search(r"vector: recall@5=([\d.]+) MRR=([\d.]+)", out)
    flt = re.search(r"filter: recall@5=([\d.]+) MRR=([\d.]+)", out)
    return [float(vector[1]), float(vector[2]), float(flt[1]), float(flt[2])]


def test_case_and_run_scores_equal_the_console_numbers(db, corpus, lf, capsys):  # AC3, AC5
    run(db, corpus, quiet(lf))

    out = capsys.readouterr().out
    run_name = lf.experiments[0]["run_name"]
    names = ["vector_recall_at_5", "vector_mrr", "filter_recall_at_5", "filter_mrr"]
    posted = [lf.run_score(run_name, name)["value"] for name in names]
    assert posted == pytest.approx(summary_numbers(out), abs=5e-4)
    assert lf.run_score(run_name, "errored_count")["value"] == 0.0
    last = {s["name"]: s for s in lf.item_scores(run_name) if s["trace_id"].endswith("retrieval:q14")}
    assert set(last) == {"vector_recall_at_5", "vector_reciprocal_rank", "filter_recall_at_5", "filter_reciprocal_rank", "errored"}
    assert (last["vector_recall_at_5"]["value"], last["errored"]["value"]) == (0.0, 0.0)  # Testing scores under 0.55


def test_the_result_shows_the_top_notes_and_what_was_expected(db, corpus, lf):  # readable results
    run(db, corpus, quiet(lf))

    output = lf.outputs[f"trace-{lf.experiments[0]['run_name']}-retrieval:q0"]
    assert output["expected"] == [API]
    assert output["top_notes"][0]["note"] == API and output["top_notes"][0]["score"] > 0.9


def test_an_embedder_error_is_a_failed_errored_case_and_the_run_goes_on(db, corpus, lf, capsys):  # EC4
    assert run(db, corpus, quiet(lf), embedder=embedder(corpus, errors=[LLMServerError("503")])) == 0

    run_name = lf.experiments[0]["run_name"]
    first = {s["name"]: s for s in lf.item_scores(run_name) if s["trace_id"].endswith("retrieval:q0")}
    assert (first["errored"]["value"], first["errored"]["comment"]) == (1.0, "LLMServerError")
    assert first["vector_recall_at_5"]["value"] == 0.0
    assert lf.run_score(run_name, "errored_count")["value"] == 1.0
    assert lf.experiments[0]["item_ids"] == [f"retrieval:q{i}" for i in range(15)]
    assert "q0" in capsys.readouterr().out


def test_without_keys_the_console_is_the_same_except_the_last_line(db, corpus, lf, capsys):  # AC7, AC8
    assert run(db, corpus, Tracer(None)) == 0
    keyless = capsys.readouterr().out
    run(db, corpus, quiet(lf))
    keyed = capsys.readouterr().out

    assert keyless.rstrip("\n").splitlines()[:-1] == keyed.rstrip("\n").splitlines()[:-1]
    assert keyless.rstrip("\n").splitlines()[-1] == "Langfuse: not recorded (no LANGFUSE keys set)."
    assert keyed.rstrip("\n").splitlines()[-1].startswith("Langfuse runs: retrieval/")


def test_no_notes_ingested_stops_before_any_call_or_run(db, lf, capsys):  # AC10, EC8
    calls = FakeEmbedder()

    assert run(db, {}, quiet(lf), embedder=calls) == 1

    assert "ingest" in capsys.readouterr().out.lower()
    assert calls.calls == [] and lf.experiments == [] and lf.datasets == {}


def test_notes_embedded_with_another_model_stop_before_any_call_or_run(db, corpus, lf, capsys):  # AC10, EC8
    other = embedder(corpus, model="another-model")

    assert run(db, corpus, quiet(lf), embedder=other) == 1

    assert "another-model" in capsys.readouterr().out and other.calls == [] and lf.experiments == []


def test_an_unreachable_database_stops_with_how_to_start_it(lf, capsys):  # AC10, EC8
    class Down:
        def active_chunks(self):
            raise OperationalError("SELECT 1", {}, Exception("connection refused"))

    calls = FakeEmbedder()

    assert run_retrieval(Down(), calls, tracer=quiet(lf), cases=labelled(), pause=0.0) == 1

    out = capsys.readouterr().out
    assert "docker compose up -d" in out and "connection refused" not in out
    assert calls.calls == [] and lf.experiments == []


def test_a_case_set_that_breaks_the_label_rules_is_still_refused(db, corpus, lf, capsys):  # EC9
    assert run(db, corpus, quiet(lf), cases=labelled()[:2]) == 1

    assert "label set:" in capsys.readouterr().out and lf.experiments == []


def test_run_rag_task_passes_the_note_and_ignores_repeat_for_retrieval(db, corpus, lf, monkeypatch):  # D1, AC21
    seen = {}

    def fake_run_retrieval(repo, embedder, **kwargs):
        seen.update(kwargs)
        return 0

    monkeypatch.setattr(rag_module, "run_retrieval", fake_run_retrieval)
    monkeypatch.setattr(rag_module, "_session", lambda: nullcontext(db))
    settings = SimpleNamespace(llm_provider_configs=[], embedding_configured=True)
    monkeypatch.setattr("app.core.ai.factory.build_embedder", lambda _settings: embedder(corpus))
    args = SimpleNamespace(task="retrieval", model=None, repeat=3, note="why", pause_seconds=0.0)

    assert rag_module.run_rag_task(args, None, settings, quiet(lf)) == 0

    assert seen["note"] == "why" and "repeat" not in seen
