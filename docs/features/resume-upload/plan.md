# Implementation Plan: Résumé upload and candidate profile (Slice 8c)

## Overview
Add a new `profile` module: upload a PDF or DOCX, read it safely in memory, scrub contact details, have the LLM fill a small validated profile, store it (one per user, replace on re-upload), and serve `GET` and `DELETE`. Nothing reads the profile yet (Slice 8d).

## Architecture & Design
- **Request flow:** route -> controller -> service -> repository, with `ai/` (prompt, extractor), `utils/` (reading, scrubbing), `models/`, `constants/` and `dependencies/` beside them. Every file is prefixed `profile_`.
- **Extraction runs as separate steps**, each pure or independently tested: read the file -> scrub -> extract (LLM) -> parse and validate -> store. The service only orders them and maps failures to errors. This is also what lets 8d add a chunk step later without touching the rest.
- **Reuse, lifted to core** (user-confirmed) so `profile` never imports `interviews`:
  - `get_llm_provider` and `get_tracer` move to `app/core/ai/dependencies.py`.
  - `load_object` and `InvalidReplyError` move to `app/core/ai/json_reply.py`.

  Interviews imports them from core, so the function and class objects stay identical and every existing test override and import keeps working.
- **Privacy in the tracer:** `TracingProvider` records the whole message list and the reply in Langfuse. A trace label (`redact`) makes the generation record a placeholder instead, so résumé content never reaches Langfuse. Only metadata (task, prompt version, model, tokens, latency) is kept.
- **Storage:** table `candidate_profiles` (UUIDv7 id, unique `user_id` with delete cascade, profile as JSON, prompt version, model, timestamps). Replace is select-then-update-or-insert in one transaction (portable to the SQLite test DB; a lost race on the unique key retries once as an update).

## Spec Requirements -> Implementation
- Endpoints, auth, permission, rate limit (AC1, AC9, AC10) -> Steps 4, 9, 10
- Content-based identification, size, page and zip-bomb limits, unreadable files (AC3, AC4, AC5) -> Step 6
- Scrub before the model (AC6) -> Steps 5, 10
- Structured extraction, retry, caps, de-duplication, provider errors (AC7, AC13) -> Steps 7, 8, 10
- Versioned prompt, input cap, prompt version stored (AC8) -> Steps 8, 9
- Replace, delete, ownership, no stored file (AC2, AC9, AC11) -> Steps 9, 10
- No content in traces or logs (AC6) -> Steps 3, 10
- Eval and baseline (AC12) -> Step 11
- Migration and layers (AC14) -> Steps 9, 12

## Implementation Steps
1. **Dependencies and parser facts.** `uv add pdfplumber python-docx` (`pdfplumber` brings `pdfminer.six`, `Pillow` and `pypdfium2`), confirm installs on Windows, then a throwaway script (scratchpad) answers the open facts:
   - how `pdfplumber` reports an encrypted PDF (and whether a hand-built PDF with an encryption entry is enough for a test, else `pypdf` is added to the **dev** group only to write that one fixture);
   - the page count without extracting text;
   - a page with no text;
   - the per-character colour in each colour model (grey, RGB, CMYK), size and position;
   - the filled shapes and images behind text (`rects`, `images`);
   - whether `python-docx` or the raw zip shows external relationships and embedded objects, and how it exposes run colour, size and hidden flags.

   Findings go in the learnings. — Test: skip
2. **Lift shared helpers to core.** `app/core/ai/dependencies.py` and `app/core/ai/json_reply.py` as above; `interviews_shared_dependencies.py` and `interviews_reply.py` import them from there. Behavior-preserving. — Test: skip (the full existing suite is the safety net; run the interviews tests after).
3. **Trace redaction.** A `redact` label in `core/ai/tracing.py` constants; when set, `start_generation` records a placeholder input, and `succeed` and `fail` omit the reply text and partial text, keeping model, usage and metadata. — Test: first. Seam: `TracingProvider.complete` observed through `tests/fake_langfuse.py` (extends `tests/core/ai/test_tracing.py`; **unconfirmed**, same style as the confirmed seams). Slices: unlabelled call unchanged -> redacted input -> redacted success output -> redacted failure output -> usage and labels still recorded.
4. **Errors, permission, constants.** In `core/errors.py`: `ResumeTooLargeError` (413 `RESUME_TOO_LARGE`), `ResumeUnsupportedError` (415), `ResumeUnreadableError` (422), `ProfileExtractionFailedError` (502), `ProfileUnavailableError` (503), `ProfileNotFoundError` (404), each with a generic message ending in a next step. `Permission.profile_manage_self` granted to every signed-in role in `auth_constants.py`. `profile_constants.py`: 2 MB, 5 pages, 10 MB unzipped, minimum text, model-input cap, 20 s budget, 5 per minute, caps (20 skills, 4 roles, 3 projects, text lengths). — Test: skip (exercised by Steps 6 to 10; run the auth tests for the permission map).
5. **Contact scrub.** `profile_utils.scrub_contacts(text)`: email addresses and phone numbers removed, nothing else touched. — Test: first. Seam: `scrub_contacts` (user-confirmed). Slices: plain email -> email with plus and dots -> international phone -> phone with spaces, dashes and brackets -> several in one line -> text without any is unchanged -> a year or a four-digit number is not a phone number (EC16).
6. **Read the résumé.** `profile_utils.read_resume(data: bytes)` returns text or raises a typed refusal (too large, unsupported, unreadable); the size and page limits come from constants. Format by content, never by name. The PDF path does three things in order: drop hidden characters, find a two-column layout, read in order. — Test: first. Seam: `read_resume` (user-confirmed), tested on PDFs and DOCX files **generated in the test** (a small helper writes PDFs from a list of text runs with position, size, colour and filled rectangles, so two-column, hidden and dark-sidebar pages are explicit in the test; `python-docx` writes DOCX including hidden, white and tiny runs; `zipfile` builds the bomb and the plain zip) so there are no binary fixtures. Slices: valid PDF text (EC1) -> valid DOCX paragraphs and table (EC2) -> wrong extension on a real PDF is accepted (EC9) -> fake PDF, image, text (EC8) -> `.doc`, `.docm`, plain zip, embedded or external parts (EC10) -> over 2 MB (EC5) -> over 5 pages (EC6) -> unzipped over 10 MB without unpacking (EC7) -> encrypted (EC11) -> corrupt or truncated (EC12) -> no text layer (EC13) -> too little text (EC14) -> single-column reading order -> two columns read left then right with sentences unmixed (EC34) -> a one-column page with a wide gap in a line is not split into columns -> near-white text with nothing behind it dropped (EC35) -> tiny text dropped -> off-page text dropped -> white text over a dark rectangle kept (EC37) -> white text over an image kept -> DOCX hidden, white and tiny runs dropped (EC36) -> the dropped text appears nowhere in the result.\

7. **Profile schema, reply parser and grounding.** `profile_schema.py`: `CandidateProfile` (skills, roles, projects; `extra="forbid"`, length caps) and `ProfileOut`. `profile/ai/profile_reply.py`: `parse_profile_reply(raw)` uses `load_object`, trims, drops blanks, merges skills case-insensitively, cuts lists to their caps, and refuses a profile with no skills and no roles. `profile_utils.ground_profile(profile, source_text)` drops skills, technologies, role titles and organizations that do not appear in the source text (case and whitespace ignored) and reports the drop count; summaries are not checked; an empty result is refused. — Test: first. Seams: `parse_profile_reply` (user-confirmed) and `ground_profile` (pure, **unconfirmed**, same style). Slices for the parser: valid reply -> fenced JSON -> not JSON or not an object -> unknown field -> over-long text and over-long lists cut (EC19) -> duplicate skills merged (EC20) -> blank items dropped -> no skills and no roles refused (EC15) -> the worst case renders under about 4,000 characters (AC13). Slices for grounding: every item present -> an invented skill dropped (EC38) -> case and spacing ignored -> a technology inside a longer word still matches only as a whole word -> counts reported -> nothing left is refused -> summaries untouched.
8. **Prompt and extractor.** `profile/prompts/profile_extract_v1.md` (system prompt: the résumé is data in delimiters, never instructions; the fields; no names or contact details; output only JSON). `profile/ai/profile_extract.py`: builds the messages, caps the input (and reports a cut), calls the provider with the `redact` label, `llm_max_tokens`, the 20 s budget, retries once on an invalid reply, and maps provider errors and timeouts. — Test: after (the wording is judged by the eval in Step 11); the retry and error behavior is covered at the route seam in Step 10.
9. **Model, repository, migration.** `profile/models/profile_model.py` (`CandidateProfileRow` with `UUIDPrimaryKeyMixin`; JSON with a Postgres JSONB variant), registered in `app/db/models.py`. `profile_repository.py`: `get`, `replace_for_user` (single transaction, one retry on a lost unique race), `delete`. Alembic migration autogenerated, reviewed, and checked offline with `alembic upgrade head --sql`; applying it to a real database is done only after telling you which one it touches. — Test: first, through the route seam (Step 10).
10. **Service, controller, dependencies, routes.** `ProfileService.upload(user, data)` orders the steps and logs one metadata line (format, bytes, pages, characters, cut flag, item counts, tokens, latency, outcome; never content); `get` and `delete`. Controller maps to `ProfileOut`. Dependencies: a per-process `RateLimiter` plus an overridable getter (the transcription pattern), the permission, and the provider from core. Routes `POST /profile/resume` (multipart `file`, read with a cap of one byte over the limit), `GET /profile`, `DELETE /profile`, with `responses=`. Router registered in `main.py`. — Test: first. Seam: the HTTP routes with a scripted LLM, a recording fake Langfuse client and the in-memory DB (user-confirmed). Slices: PDF -> 200 and GET returns it (AC1) -> DOCX -> replace (EC3) -> failed upload keeps the old one (EC4) -> each refusal's status, code and generic body (EC5 to EC15) -> the scripted model never receives an email or a phone number (EC16) -> retry once then 200 (EC17) -> two bad replies 502 (EC18) -> provider error or timeout 502 (EC21) -> no LLM 503 (EC22) -> injected résumé gives a valid profile with no instruction obeyed in the scripted check (EC23) -> long input cut (EC24) -> an invented skill from the scripted model is dropped and counted (EC38) -> visible instructions stay fenced and cannot enter the profile (EC39) -> hidden text from a generated PDF and DOCX never appears in the scripted model's input (EC35, EC36) -> GET 404 (EC25) -> DELETE and idempotent DELETE (EC26) -> user B cannot see user A's (EC27) -> 401 (EC28) -> 429 with `Retry-After` and no model call (EC29) -> missing file, empty file, extra fields 422 (EC30) -> the log line has counts only (EC32) -> traces hold metadata only (EC33).
11. **Eval.** `profile/data/profile_eval_cases.json`: about 5 synthetic résumés as text (no real people; one with hidden injected instructions, one laid out in two columns) with expected skills, role count and titles. `profile/tooling/profile_evals.py` follows the interviews eval pattern (`run_experiment` helpers, a console summary), and it runs the same read, scrub, extract, parse and ground steps the service does, so the numbers describe the real pipeline. A pure `score_profile(profile, expected)` gives skills precision and recall, role-count match and title matches. — Test: first for `score_profile` (**unconfirmed**, same style as `recall_at_k`); the real-model run is a pending gate for you, with the baseline written into the learnings.
12. **Verify and finish.** `uv run pytest`, `uv run --with ruff ruff check` on touched paths, `graphify update .`, `task.md` and `learnings.md`. — Test: skip

## Affected Files & Patterns
- New:
  - `app/modules/profile/{routes,controllers,services,repositories,schemas,utils,ai,models,constants,dependencies,prompts,data,tooling}/profile_*`
  - `app/core/ai/dependencies.py`
  - `app/core/ai/json_reply.py`
  - one Alembic migration
  - `tests/modules/profile/` mirroring the layers
  - `tests/helpers` for generated PDFs and DOCX files
- Edited:
  - `app/core/ai/tracing.py`, `app/core/errors.py`
  - `app/modules/auth/constants/auth_constants.py`
  - `app/modules/interviews/dependencies/interviews_shared_dependencies.py`, `app/modules/interviews/ai/interviews_reply.py` (imports only)
  - `app/db/models.py`, `app/main.py`
  - `pyproject.toml`, `uv.lock`
- Patterns to follow:
  - transcription (multipart read with a cap, limiter plus overridable getter, metadata-only log line);
  - the job-url service (generic errors, cause in the log);
  - `interviews_reply` and `interviews_feedback` (JSON reply, validate, retry once);
  - `interviews_eval_runs` (experiment helpers);
  - `tests/fake_langfuse.py`, `tests/test_layers.py`.
- Risks:
  - **Parser surface:** `pdfplumber` and `pdfminer.six` behavior on malformed input is learned in Step 1 and pinned by tests.
  - **Column detection is our own rule:** `pdfplumber` joins words across columns on its own, so a wrong gap threshold could split a one-column page or merge a two-column one. Both directions have tests, and a failure to detect falls back to a single column.
  - **Hidden-text rules can drop real text:** white text on a dark shape is legitimate, so near-white text is dropped only when nothing dark or no image is behind it; thresholds come from the generated pages, and a wrong call costs a missing line, not a wrong profile.
  - **Heavier dependency:** `pdfplumber` brings `Pillow` and `pypdfium2`; parsing is slower than a plain extractor but stays well inside the 5-page limit.
  - **Zip bomb:** the unzipped size must be read from the zip directory, not by unpacking.
  - **Tracing change touches core:** every existing trace test must stay green.
  - **Lifting helpers:** a missed import breaks interviews, so the full suite runs right after Step 2.
  - **Free-text fields** can still hold a name (documented).

## Testing Strategy
- Framework and command: pytest. `uv run pytest tests/modules/profile tests/core -q` per step, then `uv run pytest` at the end. Lint: `uv run --with ruff ruff check <paths>`. Doubles: scripted `FakeProvider`, `fake_langfuse`, in-memory SQLite, a limiter swapped per test, generated files. No network, no real model in the default suite.

| Spec ID | Step | Test mode | Notes |
|---------|------|-----------|-------|
| AC1 | 10 | first | EC1, EC2 |
| AC2 | 9, 10 | first | EC3, EC4 |
| AC3 | 6, 10 | first | EC8, EC9, EC10 |
| AC4 | 6, 10 | first | EC5, EC6, EC7 |
| AC5 | 6, 7, 10 | first | EC11 to EC15 |
| AC6 | 3, 5, 10 | first | EC16, EC33 |
| AC7 | 7, 10 | first | EC17 to EC22 |
| AC8 | 8, 9, 10 | after + first | prompt wording is judged by the eval; EC24 cut and stored version at the route |
| AC9 | 10 | first | EC25 to EC27 |
| AC10 | 10 | first | EC28 to EC30 |
| AC11 | 9, 10 | first | the table has no file or text column; nothing written to disk |
| AC12 | 11 | first + after | `score_profile` first; the real-model run is a pending gate (EC23 is judged there too) |
| AC13 | 7 | first | worst-case profile size |
| AC15 | 6, 10 | first | EC34 to EC37; the reader at its seam, and the model input at the route |
| AC16 | 7, 10 | first | EC38 (grounding at its seam, the scripted drop at the route); EC39 at the route |
| AC14 | 9, 12 | first + after | migration checked offline; layer test and full suite |
| EC31 | 8, 11 | after | non-English: documented, not guaranteed; one eval case if time allows |
| EC32 | 10 | first | log content |

- Must verify, not assume:
  - How `pdfplumber` reports encrypted, scanned and malformed PDFs, the page count without a full parse, and per-character colour in each colour model (Step 1).
  - That `python-docx` or the zip shows external relationships and embedded objects (Step 1).
  - That `redact` also holds inside the experiment runner.
  - The real-model profile quality and the injection result (your run).
  - The provider's data terms before real use.
- Open questions: none.
- Known baseline failures: `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits`, plus the timing-flaky `test_turn_budget.py` test. (The `follow_up_decision_v2` contract test was removed on 2026-11-14: v2 lost its experiment and its file was never committed.)

## Deviations found during implementation (2026-11-14)
- **External hyperlinks in DOCX are allowed**; every other external relationship is refused (Step 1: résumés nearly always link LinkedIn or GitHub, and nothing here follows links).
- **The reader lives in `profile_resume_utils.py`**, not `profile_utils.py` (size; follows `interviews_job_url_utils.py`). The test file generator is `tests/resume_files.py` (no `tests/helpers` package exists).
- **Column rule:** each side needs at least 3 lines, not a share of the words (a skills sidebar holds about a tenth of the words).
- **Profile JSON is plain `JSON`**, like `interview_feedback.result`, not a JSONB variant: it is read and replaced whole, never queried.
- **The migration was written by hand** (autogenerate connects to the database); checked offline with `--sql`.
- **The PDF/DOCX builders live in `app/modules/profile/tooling/profile_resume_files.py`** (the eval builds real files too); `tests/resume_files.py` re-exports them.
- **The eval runner imports `interviews_eval_runs`** (dev tooling, not app code); lifting those helpers to core is a later refactor.
- **Caps tightened** (skill 30, title 60, organization 60, period 20, summary 220, project name 60, description 220, technology 30) so the worst case stays under 4,000 characters of JSON (AC13); the first caps added up to about 4,600.
- **Extraction temperature 0** for repeatable extraction and comparable eval runs.

## Blockers & Resolutions
- Tracing would leak résumé text -> `redact` label (Step 3), tested.
- Cross-feature imports -> lift to core (Step 2, user-confirmed).
- Text thresholds (minimum characters, model-input cap) -> set from the generated fixtures in Steps 6 and 8.
- Upsert on the SQLite test DB -> portable select-then-write, not a Postgres-only statement.
- Applying the migration to a real database -> offline SQL first; the real run only after telling you which database it touches.
- Provider data terms -> documented open item for you; not a code task.

## Trade-offs & Rationale
- **Item ids:** the earlier suggestion of stable ids on each role and project is dropped for now. With replace-only storage, array position is enough; 8d can derive an id if it ever needs one. The separate-steps requirement is kept.
- **`pdfplumber` instead of a plain extractor** (user decision): it reports each character's colour, size and position, which is what hidden-text filtering and column reading need. Columns are our own gap-based rule because `pdfplumber` does not separate them.
- **Grounding check instead of trusting the model:** deterministic, free of model calls, and it bounds both invented skills and injected ones.
- **Generated test files** instead of committed binaries: no unknown content in the repo, every refusal and layout case is explicit in the test, and the PDF helper is a few dozen lines.
- **`redact` label** instead of bypassing the tracing wrapper: one switch in one place, and metadata stays visible.
- **Select-then-write replace** instead of a Postgres upsert: the whole suite runs on SQLite; the unique key still guarantees one row, and the lost-race retry is tiny.
- **Profile in JSON** instead of normalized tables: it is read and replaced as a whole, never queried by field.
- **Skills dedup in the parser, not the prompt:** deterministic and testable.

## Project Rules Applied
- `cuewise-be/CLAUDE.md`: layered module with `profile_` prefixes; UUIDv7 keys; migration through Alembic only; Pydantic with `extra="forbid"`; structured errors with generic messages; rate limiting; the provider behind its interface; prompts as versioned files; validated LLM output with a retry and safe failure; mocked LLM in tests; no content in logs; an eval for the AI feature; new dependencies justified; no commits.
- `docs/features/job-url/`: untrusted-input handling, generic errors, causes only in logs.

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| lean-ctx / graphify | transcription route and service, tracing internals, reply parsing, migration style, test DB setup, eval helpers |
| grill-me | helper location (lift to core) and test seams, both confirmed |
| security-review (plan-level) | parser attack surface, zip bomb, trace leak, ownership, no stored file |
| llm-security | résumé as an injection path; hidden-text filtering, the schema and caps, and the grounding check bound what the model can emit |
| sqlalchemy-alembic-expert-best-practices-code-review | unique key, delete cascade, JSON variant, offline migration check |

## Ready to Implement
- All spec requirements mapped to steps
- Every step has a Test tag; every AC and EC mapped
- Affected files identified
- Blockers resolved, edge cases handled
- Trade-offs documented
- One deviation from my earlier suggestion (item ids dropped), none from the spec
