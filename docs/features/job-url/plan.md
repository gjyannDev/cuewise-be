# Implementation Plan: Job URL (Slice 8b)

## Overview
Add `POST /api/v1/interviews/job-url`: fetch a posting through an SSRF-safe fetcher, extract the job text, return `{text, truncated}` for the candidate to review before the unchanged start call.

## Architecture & Design
Two reusable pieces and one thin feature slice. (1) `app/core/safe_fetch.py`: a feature-agnostic, guarded HTTP GET (validate URL, resolve once, check every address, connect to the checked address, follow redirects by hand, cap time and bytes). (2) a pure extractor in `interviews_job_url_utils.py` (JSON-LD `JobPosting` first, `trafilatura.extract` as fallback, then word-boundary truncation). (3) route -> controller -> service wiring in the interviews module, with its own rate limiter. Sync end to end (sync httpx client in a sync route, which FastAPI runs in the threadpool), matching every other interviews route. No repository, no DB, no migration, no LLM call; the start path is untouched.

## Spec Requirements -> Implementation
- Endpoint, auth, response shape (AC1, AC10) -> Steps 5, 6
- URL input rules: scheme, credentials, length (AC5) -> Step 5
- Address checks, rebinding pin, redirects, ports (AC2, AC3, AC4) -> Step 3
- Time, size, content-type, status handling, error codes (AC6, AC7) -> Steps 2, 3, 6
- Extraction and truncation (AC8, AC9) -> Step 4
- No network in tests, host-only logging (AC11) -> Steps 3, 6, 7
- Injection page stays plain data; start path unchanged (AC12, AC13) -> Steps 7, 8

## Implementation Steps
1. Add the `trafilatura` dependency with `uv add` and confirm the import and a tiny extract work on Windows. Say why in the summary (main-content extraction is the hard, fiddly part; stdlib would be a long tail of heuristics). — Test: skip
2. Constants and errors. In `interviews_constants.py`: per-minute limit (10), overall fetch time cap, per-hop connect/read timeouts, max body bytes (about 1 MB), redirect limit, allowed ports (80, 443), minimum extracted characters (set from the fixtures in Step 4). In `core/errors.py`: `JobUrlUnreachableError` (422, `JOB_URL_UNREACHABLE`) and `JobUrlUnreadableError` (422, `JOB_URL_UNREADABLE`) with generic messages that end in "paste the job description instead". — Test: skip (exercised by Steps 3 to 6)
3. `app/core/safe_fetch.py`, public seam `safe_fetch(url, ...)` with an injectable resolver and httpx transport. Returns a small result (final host, decoded text, content type) or raises the unreachable/unreadable error. Build in thin slices, one behavior each: scheme and port and credentials refused -> IP-literal and numeric-host forms refused (private, loopback, link-local/metadata, unique-local, reserved, multicast, IPv4-mapped IPv6; rule is "not globally routable") -> hostname resolving to a private address refused -> any one bad address among several refused -> connection goes to the validated address, never a second lookup (rebinding) -> redirects handled manually with the same checks per hop, loop and cap enforced -> non-2xx, timeout, DNS failure, connection error all become unreachable -> non-HTML and over-cap body become unreadable, read stopped at the cap -> charset decoded from header/meta with replacement, never a crash -> happy path. Test: first. Seam: `safe_fetch` (user-confirmed).
4. `interviews_job_url_utils.py`, seam `extract_job_text(html)` plus `truncate_on_word(text, limit)`. Slices: `JobPosting` JSON-LD (single object, list, `@graph`) -> fields joined into readable text; no structured data -> `trafilatura` main content without nav/footer/script text; too little text -> signals unreadable; truncation on a word boundary with the flag. Fixture pages go in `tests/modules/interviews/data/job_pages/` (JSON-LD board, plain article-style posting, JS shell, cookie wall, injection page, latin-1 page, huge page); the minimum-text threshold is tuned on them. — Test: first. Seam: `extract_job_text` (user-confirmed).
5. Schemas: `JobUrlIn` (`extra="forbid"`, stripped, bounded length, http/https only, no embedded credentials) and `JobUrlOut` (`text`, `truncated`) in `interviews_schema.py`. — Test: first (through the route seam, with Step 6)
6. Wiring: `interviews_job_url_service.py` (fetch -> extract -> truncate; logs host and outcome only, never the URL or text), `interviews_job_url_controller.py` (request to response schema), `interviews_job_url_dependencies.py` (own `RateLimiter` plus `get_job_url_limiter` for test override, `limit_job_urls`, and a `get_page_fetcher` dependency returning `safe_fetch` so tests swap it), and the route in `interviews_route.py` declared before any `/{session_id}` POST path, permission `interviews_create`, `responses=` for 401, 422, 429. Follow the transcription dependencies file exactly for the limiter pattern. — Test: first. Seam: `POST /interviews/job-url` through the existing client with the fetcher overridden (user-confirmed).
7. Route-level behavior tests: success (JSON-LD and fallback), truncation flag, both error codes with the generic body (no cause leaked), 401, 429 with `Retry-After`, validation 422s, injection page returned as plain text, log capture shows host but never the URL or page text. — Test: first (same seam as Step 6; write alongside it)
8. Verify start path unchanged: run the existing interviews suite and the injection job-description cases; do one manual check against two or three real posting URLs and one blocked site. — Test: after
9. `graphify update .`, ruff on touched paths, full `uv run pytest`; summarize and leave everything uncommitted. — Test: skip
10. (Added 2026-11-13, AC14) Job-posting check. Constants `JOB_TERMS` (English stems, lower case) and `JOB_TERMS_MIN_HITS` (3) in `interviews_constants.py`. Pure function `looks_like_job_posting(text)` in `interviews_job_url_utils.py`: count distinct terms present (case-insensitive substring, so stems match longer words), compare with the minimum. The service raises the unreadable error with reason `not_a_posting` after extraction, before truncation (judge the whole text, not the cut). New fixtures `news_article.html` and `recipe.html`. Slices: real postings pass -> non-postings fail -> distinct-not-repeated -> case and stems -> non-English fails -> route returns `JOB_URL_UNREADABLE` and logs the reason. — Test: first. Seams: `looks_like_job_posting` (pure, same kind as the confirmed `extract_job_text` seam) and the confirmed route seam.
11. (Added 2026-11-13, AC15-AC17, user-approved: HTML with plain-text fallback; clean, then cut, no LLM) Paste fallback.
    - Utils: `pasted_job_text(content, format)` returns the cleaned text or None. `html` runs `extract_job_text`, and when that is None, the HTML's visible text. The existing `_TextCollector` learns to skip script, style and noscript content. `text` runs `_tidy`. Below `JOB_TEXT_MIN_CHARS`, the result is None.
    - Constant `JOB_PASTE_MAX_CHARS = 1_000_000`; message `JOB_TEXT_UNREADABLE_MESSAGE`; error `JobTextUnreadableError` (422, `JOB_TEXT_UNREADABLE`) in `core/errors.py`.
    - Schemas `JobTextIn` (`content` stripped, 1 to max chars; `format` a `JobTextFormat` StrEnum; `extra="forbid"`). The response reuses `JobUrlOut`, the same shape; no new model.
    - Service: `import_pasted_text(user, content, format)` on `JobUrlService`. A shared private tail runs the job-term check and the cut, so both paths apply the same rules. One log line with `source=paste`, `format`, `in_chars`, `chars`, `truncated`, `outcome`; no host and no content.
    - Rate limit: `limit_job_urls` becomes `limit_job_imports` (one shared limiter for both routes, message "Too many job imports").
    - Route `POST /interviews/job-text` next to `/job-url`; controller method `import_pasted_text`.
    - Fixture `clipboard_posting.html`: a clipboard-style fragment with nav, posting and footer.
    - Test: first. Seams: `pasted_job_text` (pure) and the route. Slices: html whole page -> html fragment -> plain text -> too little -> not a posting -> long cut -> validation -> auth and shared limit -> log line.

## Affected Files & Patterns
- New: `app/core/safe_fetch.py`; `app/modules/interviews/{utils/interviews_job_url_utils.py, services/interviews_job_url_service.py, controllers/interviews_job_url_controller.py, dependencies/interviews_job_url_dependencies.py}`; tests under `tests/core/` (safe_fetch) and `tests/modules/interviews/{utils,routes}/`; fixtures dir above.
- Edited: `interviews_route.py` (one route), `interviews_schema.py` (two schemas), `interviews_constants.py`, `core/errors.py`, `pyproject.toml` and `uv.lock`.
- Patterns: transcription dependencies (limiter + overridable getter); `AppError` subclass with generic message; `responses={...: ErrorResponse}`; file prefix `interviews_`; layers checked by `tests/test_layers.py` (service may import `app.core`).
- Risks: (a) pinning the connection to the validated IP while keeping the real hostname for the Host header and TLS name check must be verified against httpx/httpcore behavior, not assumed; (b) `trafilatura` import weight and Windows install; (c) real sites may block the fetcher, which is the designed "paste instead" outcome; (d) route order, since a path param route could swallow `/job-url`.

## Testing Strategy
- Framework & command: pytest, `uv run pytest tests/core/test_safe_fetch.py tests/modules/interviews -q`, then full `uv run pytest`. Lint: `uv run --with ruff ruff check <touched paths>`.
- Doubles: recording `httpx.MockTransport` (also asserts which addresses were contacted), fake resolver returning chosen addresses (changes answer on a second call for rebinding), fixture HTML. No network.

| Spec ID | Step | Test mode | Notes |
|---------|------|-----------|-------|
| AC1 | 4, 6, 7 | first | success with JSON-LD and fallback fixtures |
| AC2 | 3 | first | EC2, EC3, EC4; transport records zero contacts |
| AC3 | 3 | first | EC6, EC7, EC8 |
| AC4 | 3 | first | EC5; resolver answers differently on call two |
| AC5 | 5, 7 | first | EC1, EC9, EC21 |
| AC6 | 3, 7 | first | EC10 to EC14, EC24; body has code only |
| AC7 | 3 | first | EC13; stream read stops at cap |
| AC8 | 4 | first | EC17, EC18 |
| AC9 | 4 | first | EC15, EC16 |
| AC10 | 6, 7 | first | EC22, EC23 |
| AC11 | 3, 7 | first | no network; log capture checks |
| AC12 | 7, 8 | first + after | EC19; plain-text passthrough tested; real-LLM injection eval run is manual |
| AC13 | 8 | after | existing suite; no migration file added |
| EC11 | 3 | first | timeout via a transport that raises a timeout |
| EC20 | 3 | first | latin-1 fixture decoded without a crash |
| AC14 | 10 | first | EC25-EC28; fixtures plus one route test |
| AC15 | 11 | first | EC29-EC34, EC37; pure function plus route |
| AC16 | 11 | first | EC35, EC36 |
| AC17 | 11 | first | log capture |

- Must verify, not assume: IP pinning with correct SNI/Host/cert name (Step 3 risk a); real job sites' behavior (Step 8); `trafilatura` output on real pages vs fixtures.
- Open questions: none. The minimum-text threshold is set in Step 4 from fixtures.
- Known baseline failures: `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits` and the timing-flaky `test_turn_budget.py::test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only`.

## Blockers & Resolutions
- Minimum-text threshold -> chosen in Step 4 from fixtures.
- Real-site behavior -> manual check in Step 8, documented in the summary.
- DNS rebinding -> validated address is the connection target (Step 3).
- Numeric-host tricks (`2130706433`, `0x7f.1`) -> handled by validating resolved addresses, not by parsing the host string.

## Trade-offs & Rationale
- Preview endpoint, not a field on start -> candidate sees the text; start stays network-free.
- Own guard, not a library -> few maintained `httpx` options, and it is the SSRF lesson; kept in `core/` for reuse.
- `trafilatura` for extraction -> user-approved; JSON-LD first because it is cleaner when present.
- 422 for both errors (user-confirmed) -> user-fixable, avoids 5xx noise; the code distinguishes them.
- Sync stack -> matches the module; blocking I/O runs in the threadpool, not on the event loop.
- Cut on a word boundary, no cap raise -> no effect on prompts, evals or cost.
- Keyword check, not an LLM classifier (user-approved, 2026-11-13) -> no cost, latency or new injection surface; it's a convenience filter, and the candidate's review stays the real check. Threshold 3 distinct terms: the draft list scored real postings 7-10 and the drafted non-postings 0, so 3 starts loose; tune from `app.job_url` logs.

## Project Rules Applied
- `cuewise-be/CLAUDE.md`: route/controller/service layering and `interviews_` prefixes; structured errors with generic client messages; `response_model`, `responses=`, `extra="forbid"`; rate limiting on sensitive endpoints; no PII in logs; no dependency without saying why; tests mirror modules; no commits; `graphify update .` and ruff at the end.

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| lean-ctx | transcription dependencies/limiter pattern, route layout and ordering, error classes, config/constants locations |
| graphify | module wiring and where the start path consumes `job_description` |
| grill-me | status codes (422 both), test seams confirmed |
| security-review | SSRF surface: scheme/port/credentials, address classes, rebinding, redirects, no error oracle |
| llm-security | fetched text treated as untrusted; reuse of the existing delimited job-description path |

## Ready to Implement
- All spec requirements mapped to steps
- Every step has a Test tag; every AC and EC mapped in Testing Strategy
- Affected files identified
- Blockers resolved, edge cases handled
- Trade-offs documented
- No deviations from spec

## Deviations found during implementation (2026-11-13)
- The Step 3 seam is a `SafeFetcher` class with a `fetch(url)` method, not a `safe_fetch(url, ...)` function. Limits, resolver, transport and clock are fixed at construction, so the dependency can hand out one configured instance. The seam (one public call, observed through a recording transport) is the same.
- `safe_fetch.py` raises its own `UrlUnreachableError` / `ResponseUnreadableError` (each with a `reason`), not the HTTP `AppError`s. The service maps them to `JobUrlUnreachableError` / `JobUrlUnreadableError` and logs the reason. `core/` stays HTTP-agnostic, and the cause never reaches the error's `details`.
