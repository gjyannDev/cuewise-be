# Implementation: Job URL (Slice 8b)

## Status
Ready for review (11 of 11 steps). Uncommitted; the user commits by hand. One pending item: a real-model injection eval (below).

## Completed Steps
- [x] 1. Added `trafilatura>=2.0` (installed 2.3.1, 13 packages including lxml). Smoke-tested extract.
- [x] 2. Constants (`JOB_URL_*`, `JOB_TEXT_MIN_CHARS`, messages) and errors `JobUrlUnreachableError` / `JobUrlUnreadableError` (422)
- [x] 3. `app/core/safe_fetch.py`: `SafeFetcher`, `is_public_address` (tdd, 86 tests)
- [x] 4. `interviews_job_url_utils.py`: `extract_job_text`, `truncate_on_word`, 5 fixture pages (tdd, 27 tests)
- [x] 5. `JobUrlIn` / `JobUrlOut` schemas
- [x] 6. Service, controller, dependencies (limiter + fetcher overrides), route `POST /interviews/job-url`
- [x] 7. Route tests (tdd, 46 tests)
- [x] 8. Full suite (start path unchanged); manual real-URL and TLS-pinning check
- [x] 9. ruff on touched files (4 import/style fixes), `graphify update .`, learnings.md
- [x] 10. (added 2026-11-13, AC14) Job-posting keyword check: `JOB_TERMS` (22 terms) + `JOB_TERMS_MIN_HITS = 3`, `job_term_hits` / `looks_like_job_posting` in utils, service raises `unreadable:not_a_posting` before truncation; fixtures `news_article.html`, `recipe.html` (tdd, 11 new tests)
- [x] 11. (added 2026-11-13, AC15-AC17) Paste fallback `POST /interviews/job-text`:
  - `pasted_job_text` (HTML through the extractor, else the visible text; plain text tidied).
  - The collector skips script, style, noscript and template content.
  - `JobTextIn` with the `JobTextFormat` enum, and `JobTextUnreadableError` (422 `JOB_TEXT_UNREADABLE`).
  - The service shares the `_fit` tail with the link path.
  - `limit_job_urls` is renamed `limit_job_imports`: one shared budget for links and pastes.
  - Fixture `clipboard_posting.html` (tdd, 29 new tests).

## Changes Made
New:
- `app/core/safe_fetch.py`
- `app/modules/interviews/{utils/interviews_job_url_utils.py, services/interviews_job_url_service.py, controllers/interviews_job_url_controller.py, dependencies/interviews_job_url_dependencies.py}`
- `tests/core/test_safe_fetch.py`
- `tests/modules/interviews/{routes/test_job_url.py, utils/test_job_url_utils.py, data/job_pages/*.html}`
- `docs/features/job-url/{spec,plan,task,learnings}.md`

Edited:
- `app/core/errors.py`
- `app/modules/interviews/{constants/interviews_constants.py, schemas/interviews_schema.py, routes/interviews_route.py}`
- `pyproject.toml`, `uv.lock`

No migration.

Suggested commit message:
`feat(interviews): import a job description from a posting link with an SSRF-safe fetcher (slice 8b)`

## Test Results
- Feature tests: 121 passed after step 11 (`routes/test_job_url.py`, `utils/test_job_url_utils.py`, `tests/test_layers.py`), plus 86 in `tests/core/test_safe_fetch.py`.
- Full suite after step 11: 1803 passed, 6 skipped, 2 failed. Both failures predate this slice (see Baseline Failures). Ruff and pyright are clean on the touched files.

## Tests Pending
- AC12, real-model half: run the injection job-description eval cases with the text from `injection.html` against the real interviewer and record the result in learnings §7. The unit test proves the fence holds, not the model's behavior.

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 3 | non-public address classes refused (incl. mapped, NAT64, 6to4, zone id) | spec | EC2, AC2 | pass |
| T2 | 3 | bad scheme, credentials, port, no host: refused, zero contact | spec | EC1, EC8, EC9 | pass |
| T3 | 3 | IP literal, numeric host, name resolving private: zero contact | spec | EC2, EC3, AC2 | pass |
| T4 | 3 | any private address among several refuses | spec | EC4 | pass |
| T5 | 3 | DNS failure unreachable | spec | EC24 | pass |
| T6 | 3 | connects to the validated IP; Host and SNI keep the name | spec | AC4 | pass |
| T7 | 3 | rebinding: one resolve, private never contacted | spec | EC5 | pass |
| T8 | 3 | proxy env vars ignored | inferred | risk: proxy bypass | pass |
| T9 | 3 | redirects followed with checks; private, scheme, port, credential targets never contacted | spec | EC6, EC8, AC3 | pass |
| T10 | 3 | redirect cap and loop | spec | EC7 | pass |
| T11 | 3 | 3xx without Location | code-derived | httpx 0.28 is_redirect | pass |
| T12 | 3 | non-2xx and transport errors unreachable | spec | EC10, EC11 | pass |
| T13 | 3 | one total deadline across a trickling body | spec | EC11 | pass |
| T14 | 3 | non-HTML, declared and streamed oversize unreadable; read stops at the cap | spec | EC12, EC13, AC7 | pass |
| T15 | 3 | identity encoding requested | inferred | risk: decompression past cap | pass |
| T16 | 3 | charset from header, meta, bogus fallback | spec | EC20 | pass |
| T17 | 4 | JSON-LD preferred over chrome; every JSON-LD shape; entities decoded | spec | EC15, AC9 | pass |
| T18 | 4 | broken or short JSON-LD falls back | inferred | risk: bad structured data | pass |
| T19 | 4 | main content without nav, footer, script, sidebar | spec | EC16, AC9 | pass |
| T20 | 4 | JS shell, cookie wall, tiny input give nothing | spec | EC14 | pass |
| T21 | 4 | truncation on a word boundary; exact limit; hard cut of one huge word | spec | EC17, EC18, AC8 | pass |
| T22 | 7 | 200 success, long text accepted by start | spec | AC1, AC8 | pass |
| T23 | 7 | invalid input 422, no fetch, no secret echoed | spec | AC5, EC1, EC9, EC21 | pass |
| T24 | 7 | refused targets: generic body, no details, no request | spec | AC2, AC6 | pass |
| T25 | 7 | unusable pages: generic unreadable | spec | AC6, EC12-14 | pass |
| T26 | 7 | 401, 429 with Retry-After, per user; refusals count | spec | AC10, EC22, EC23 | pass |
| T27 | 7 | log: host and outcome, no URL path, query or text; cause logged | spec | AC11 | pass |
| T28 | 7 | injection page text stays fenced in every LLM call at start | spec | AC12, EC19 | pass |
| T29 | 10 | real-posting fixtures pass the term check; news and recipe fail; margin on both sides | spec | AC14, EC25 | pass |
| T30 | 10 | a repeated term counts once | spec | EC26 | pass |
| T31 | 10 | case-insensitive, stems match | spec | EC27 | pass |
| T32 | 10 | Spanish posting not recognised (known limit) | spec | EC28 | pass |
| T33 | 10 | route: non-posting gives generic `JOB_URL_UNREADABLE`, logs `not_a_posting` | spec | AC14, EC25 | pass |
| T34 | 11 | HTML paste of a whole page: posting only, clutter dropped | spec | AC15, EC29 | pass |
| T35 | 11 | fragment the extractor skips (span, table cell) falls back to visible text | spec | EC30 | pass |
| T36 | 11 | fallback never returns script or style content | spec | EC30 | pass |
| T37 | 11 | plain-text paste tidied, otherwise kept; tag-like text kept as text | spec | EC31 | pass |
| T38 | 11 | too little text, menu only, news, recipe: `JOB_TEXT_UNREADABLE`, generic body | spec | EC32, EC33 | pass |
| T39 | 11 | long paste cut and accepted by start | spec | EC34 | pass |
| T40 | 11 | injection paste returned as plain text | spec | EC37 | pass |
| T41 | 11 | bad bodies 422; 401 without a token | spec | AC16, EC35, EC36 | pass |
| T42 | 11 | links and pastes share one 10-per-minute budget | spec | AC16, EC36 | pass |
| T43 | 11 | one paste log line with source, format, sizes, outcome; never content | spec | AC17 | pass |

## Open Questions
- None blocking. Tests changed during the build, neither loosened:
  - A shape-test sample was under the 200-character threshold, so the data was lengthened.
  - The "whole lines" truncation test asserted behavior the spec never asked for. It was replaced by "a newline counts as a word boundary".
  - Step 10: the route test's synthetic `long_posting()` matched only 2 job terms, so it gained posting wording ("We are looking for", "Requirements", "experience"). The data changed under the new rule; no assertion changed.
  - Step 11: the first script/style fallback test also asserted `<noscript>` text was dropped, which EC30 never promised. trafilatura keeps noscript text, and its tokens collided ("SCRIPT_TEXT" is inside "NOSCRIPT_TEXT"). That fragment also turned out to go through trafilatura, not the fallback, so the test was reshaped (style and script inside a table cell) until it really exercised the fallback.
  - Step 11: the first shared-budget test used two different users, so it could not test a shared per-user budget. It was rewritten with one user before any code ran.

## Baseline Failures
- `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits` (known)
- `tests/modules/interviews/ai/test_context_prompts.py::test_decide_prompt_v2_can_replace_v1_without_breaking_the_contract`: `prompts/follow_up_decision_v2.md` is not in the working tree or git history, though the handoff says it was kept as an experiment. Unrelated to this slice; the user should restore the file or drop the test.
- `test_turn_budget.py::test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only` (timing-flaky; passed this run)

## Known Issues
- The job-term check passes a job board listing page (python.org/jobs: 4 hits) and rejects non-English postings. Both are documented; the candidate's review covers the first, pasting covers the second.
- `socket.getaddrinfo` has no timeout of its own: a slow DNS resolver can exceed the 8 s budget.
- The rate limiter is per process.

## Deviations from Plan
- `SafeFetcher` class instead of a `safe_fetch` function. Core-level fetch exceptions are mapped to the HTTP errors in the service. Recorded in plan.md under "Deviations found during implementation".
- Step 10 was added after the build at the user's request (spec AC14 and EC25-EC28, plan step 10). Within it, "years of", "manager", "compensation", "team" and "role" were left out of the term list: the news fixture uses them in a non-job sense.
- Step 11 was added after the build at the user's request (spec "Paste fallback", AC15-AC17, EC29-EC37, plan step 11). The user chose HTML with a plain-text fallback, and clean-then-cut with no LLM.

Suggested commit message for steps 10-11:
`feat(interviews): reject non-posting pages and add a paste fallback for sites that block job links`

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| all | lean-ctx, graphify | lookups, tests, graph update |
| 3-7 | tdd (via implement) | red -> green at the three confirmed seams |
| 3 | security-review (plan findings) | SSRF bypass list: encodings, rebinding, redirects, proxy, oracle |

## Links
- Spec: docs/features/job-url/spec.md
- Plan: docs/features/job-url/plan.md
- Learnings: docs/features/job-url/learnings.md

---

## Validation Checklist (before PR)
- [x] All plan.md steps complete
- [x] Full test suite green apart from the listed baseline failures
- [x] Every AC met and covered by a passing test (AC12's real-model half is pending, AC13 by the full suite and no migration)
- [x] Open Questions surfaced
- [x] No skipped, deleted or loosened tests
- [x] task.md updated
- [x] learnings.md written; the pending item matches Tests Pending
- [ ] Commits: the user commits by hand
- [x] No open blockers
- [x] Project rules followed (layers, prefixes, structured errors, no PII in logs, no migration)
- [x] Plan deviations recorded
