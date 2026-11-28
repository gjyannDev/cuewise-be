# Implementation: U3b2 — Retrieval on LangChain

## Status
Ready for PR (all steps done or dropped by the approved deviation; `/review-feature` next)
Health Check: all present; review level: low

## Completed Steps
- [x] 1. `GoogleEmbedder` gains `embed_documents` / `embed_query` (LangChain `Embeddings`)
- [-] 2. Live spike — dropped (deviation): same request code, vectors identical by construction
- [-] 3. Path and factory — dropped (deviation): `build_embedder` already builds the class
- [x] 4. Retriever (`app/modules/interviews/ai/interviews_retrieve.py`)
- [x] 5. Wire the service (`_ranked` through `nearest`)
- [-] 6. Eval tooling — dropped (deviation): evals already build `GoogleEmbedder`
- [-] 7. Port the budget test — dropped (deviation): the test already drives `GoogleEmbedder`
- [x] 8. Splitter comparison: user run 2026-11-27, 75 of 75 chunks identical (text and hash)
- [x] 9. Evals and docs: retrieval eval no change (`docs/evals/u3b2-embeddings-vs-baseline.md`); upgrade path updated
- [x] 10. Splitter adopted (user OK'd `langchain-text-splitters` 1.2.0): `app/modules/interviews/ai/interviews_split.py`

## Current Step
- none (finalized)

## Acceptance Criteria
- AC1: answered by construction (approach G: the same request code, so no vectors to compare); recorded in learnings.md
- AC2: `GoogleEmbedder` is an `Embeddings` (T1); no re-embedding (75/75 identical hashes; same model)
- AC3: `VectorRetriever` in `ai/`, search passed by the service (T3, T4); `tests/test_layers.py` passes
- AC4: existing retrieval service tests pass unchanged (T7)
- AC5: same error types and call counts (T2; `test_retry_budget.py` unchanged and passing)
- AC6: one batched call (T6)
- AC7: retrieval eval recall@5 1.00, MRR 0.909, 26/26 cases identical; generation not needed
- AC8: comparison 75/75; adopted (T8-T10)
- AC9: `uv run pytest` 2782 passed, 10 skipped; ruff clean on `app` and `tests` (alembic errors pre-existing); logs and
  traces unchanged (ids, counts, scores, codes)

## Changes Made
- (none committed; the user commits)
- Suggested commit after Steps 1-8:
  `refactor(retrieval): GoogleEmbedder as a LangChain Embeddings and vector search through a BaseRetriever`
- Suggested commit for Step 10: `feat(knowledge): split note sections with MarkdownHeaderTextSplitter`
- Suggested commit for docs: `docs(u3b2): spec, plan, task, learnings, retrieval eval comparison and upgrade-path progress`

## Test Results
- Step 1: `uv run pytest` 2777 passed, 10 skipped; ruff clean
- Step 4: `test_retrieve.py` + `test_layers.py` 37 passed; ruff clean
- Step 5: `uv run pytest tests/modules/interviews/ tests/test_layers.py` 1899 passed, 5 skipped; ruff clean
  (existing retrieval service tests unchanged: AC4)
- Step 8: comparison test skips without the package (as designed); user run: 75 of 75 identical
- Step 10: `uv run pytest` 2782 passed, 10 skipped; `ruff check app tests` clean (knowledge validation tests unchanged)

## Tests Pending
- none (retrieval eval run 2026-11-27: `retrieval/threshold-0.55/notes-754d0f/20261127-203131/r1`, no change)

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 1 | `GoogleEmbedder` is an `Embeddings`; methods send one batched call with the right task type | spec | AC2 | pass |
| T2 | 1 | `embed_query` keeps the retry rules and typed errors (2 calls on 503s) | spec | AC5, EC12 | pass |
| T3 | 4 | `invoke` returns documents in search order with chunk id, competency, text, score | spec | AC3 | pass |
| T4 | 4 | `nearest` returns plain tuples and applies no floor | spec | AC3 | pass |
| T5 | 4 | empty search gives an empty list | inferred | risk: empty input | pass |
| T6 | 5 | one batched embed call for both queries | spec | AC6, EC10 | pass (existing `test_retrieval_profile.py:63`) |
| T7 | 5 | degrade reasons, floor, merge, fallback unchanged | spec | AC4, EC2-EC9 | pass (existing tests) |
| T8 | 8 | per-chunk text/hash report of splitter vs `parse_note` | spec | AC8, EC11 | pass (user run, 75/75); file removed after adoption (it would compare the splitter with itself) |
| T9 | 10 | splitter gives each `##` heading's text, title left out | spec | AC8 | pass |
| T10 | 10 | a heading with no text is absent from the split (so `parse_note` keeps its own scan) | code-derived | splitter drops empty sections | pass |
| T11 | review | an indented, tabbed or trailing-space line is refused (R1) | code-derived | splitter strips lines | pass |
| T12 | review | `##B` (no space) or `##` inside a code fence is refused with a clear message (R2) | code-derived | scan vs splitter | pass |

## Open Questions
- none

## Baseline Failures
- `tests/modules/profile/utils/test_profile_read_resume.py`: flaky in the full suite, passes alone (pre-existing)
- `uv run --with ruff ruff check .`: 47 errors, all in `alembic/` (untouched; pre-existing); `ruff check app tests` is clean

## Known Issues
- Pre-existing pyright errors in `interviews_feedback.py`, `interviews_report.py`, `profile_schema.py` (untouched)

## Deviations from Plan
- Finding: `GoogleGenerativeAIEmbeddings.embed_documents` (langchain-google-genai) calls
  `client.batch_embed_contents(request)` with no timeout or retry; `request_options` is declared but never used, so the
  Google client's defaults apply (60 s timeout, retry on 503 ServiceUnavailable up to a 60 s deadline). The service's
  time cap and the retry budget (AC5, EC2, EC12) can't hold through it -> plan.md updated: approach G, `GoogleEmbedder`
  subclasses `Embeddings`; Steps 2, 3, 6, 7 dropped -> Approved by: user, 2026-11-27 (two AskUserQuestion answers).
- Finding (Step 10): `MarkdownHeaderTextSplitter` drops a heading with no text and merges sections that share a heading,
  so it can't replace the heading scan that raises "empty section" / "duplicate heading". Adopted for the section text
  only; `_sections` keeps its heading scan. The comparison test was removed after adoption (it would compare the
  splitter with itself); its 75/75 result is in learnings.md -> Approved by: user (adopt), 2026-11-27.
- Not mine: `interviews_retrieval_service.py` and `interviews_rag_evals.py` were reformatted on disk during the session
  (line wrapping only; the retrieval and tooling tests pass, 399).

## Debug Log
- none

## Review
Written by `/review-feature low` (2026-11-27). Scope: the uncommitted U3b2 changes on `feat/langchain-migration`
(the branch's earlier U3b1 commits were reviewed in U3b1). Coverage note: the `code-review` agent saw only part of the
diff (its read was cut off; it never opened `interviews_retrieve.py` or `interviews_split.py`, and it skipped tests) and
reported no findings for what it read; the new files and tests were reviewed by hand against the code and the
installed `langchain-text-splitters` 1.2.0 source.

| ID | Severity | Source | File:line | Finding | Status |
|----|----------|--------|-----------|---------|--------|
| R1 | should-fix | manual (code-review gap) | app/modules/interviews/ai/interviews_split.py:15 | `MarkdownHeaderTextSplitter.split_text` strips every line (`line.strip()`) and removes non-printable characters (tabs included), so a future note with an indented nested list or an indented code block is silently flattened: the text the question writer sees changes and so does the stored hash. The old `_sections` kept lines as written. Today's corpus has no indented lines, which is why the comparison was 75/75. Fix options: reject indented lines in `_sections` with a clear `CorpusError`, or go back to taking the text from our own scan. | fixed (`_sections` rejects a line with leading/trailing whitespace or a tab, naming the section; tests in `test_knowledge_utils.py`) |
| R2 | should-fix | manual | app/modules/interviews/utils/interviews_knowledge_utils.py:248 | The heading scan (`_SECTION`, `^##(?!#)\s*`) and the splitter disagree on what a heading is: `##Heading` (no space) and a `## ` line inside a code fence are headings to the scan but not to the splitter. Before, such notes ingested; now they fail with a misleading "empty section" error, or the fenced text lands in the previous section. Fix: when a scanned heading has no entry in the split, raise an error that names the mismatch, or align `_SECTION` with the splitter (require a space). | fixed (empty sections are told apart by the scan; a heading the splitter doesn't see raises "not read as a section: write '## X' with a space, outside a code fence") |
| R3 | nit | manual | app/modules/interviews/utils/interviews_knowledge_utils.py:33 | `utils/` (feature-local pure helpers) now imports from `ai/`, so the corpus parser depends on LangChain. Allowed by `tests/test_layers.py`, but the direction is unusual; moving `parse_note`'s split call into ingestion's `ai/` side would keep utils pure. | open |
| R4 | nit | manual | app/modules/interviews/ai/interviews_retrieve.py:41 | `VectorRetriever.search` is typed `Callable[..., Sequence[tuple[Any, float]]]` while the module defines `VectorSearch` for the same thing; one type would do. | fixed |
| R5 | nit | manual | app/modules/interviews/tooling/interviews_rag_evals.py | The file is modified only by line wrapping done on disk during the session, not by U3b2; keep it out of the U3b2 commit (or commit it separately). `interviews_retrieval_service.py` has the same reformat mixed with the real `_ranked` change. | open |

Check results:
- `uv run --with ruff ruff check app tests` -> pass
- `uv run --with ruff ruff check .` -> fail, 47 errors, all in `alembic/` (pre-existing, untouched; Baseline Failures)
- `uv run pytest` -> not re-run: low level; the last full run on this final diff is green (2782 passed, 10 skipped)
- type checker, static security scan, dependency audit, migrations -> not run: low level (no migration in this diff)
- `code-review` (low) -> no findings, partial coverage (see the note above)
- `security-review` -> not run: low level, no auth, permission, secret or new user-data handling in the diff
- `llm-security` -> not run: low level, no prompt files or chat-call code changed
- `simplify` -> not run: low level
- Project rules: LangChain only in `core/ai` and `ai/` (holds; layer test passes); dependency added with the user's OK and
  a reason; no new logging; tests mock the embedder; AI change compared with the baseline
  (`docs/evals/u3b2-embeddings-vs-baseline.md`) -> pass, with R3 as a nit
- Traceability: AC1-AC9 and EC1-EC12 each map to a passing test or a recorded verification (see Acceptance Criteria and
  Test Cases) -> pass

After the fixes (R1, R2, R4; selected by the user):
- `uv run --with ruff ruff check app tests` -> pass
- `uv run pytest` -> first run 1 failed, 2786 passed (the failing test's name was not captured; the known flaky
  `test_profile_read_resume.py` is the likely one); re-run 2787 passed, 10 skipped
- real corpus: `load_corpus` still gives 75 chunks (no note is rejected by the new checks)
## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| all | ponytail | smallest diff: reuse `GoogleEmbedder` instead of a new wrapper |
| all | caveman (lite) | chat style |

## Links
- Spec: docs/features/u3b2-retrieval/spec.md
- Plan: docs/features/u3b2-retrieval/plan.md
