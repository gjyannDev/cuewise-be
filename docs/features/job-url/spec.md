# Feature: Job URL (Slice 8b)

## Problem
A candidate who wants a job-aware interview has to copy the posting text by hand and paste it. Postings are on web pages, so pasting is friction. Fetching a user-supplied URL from our server is also a classic security hole (SSRF), and the fetched page is untrusted text that ends up near the interviewer prompt.

## Goal
Let the candidate paste a posting link and get the posting's text back, ready to review and use as the interview's job description, without the server ever being usable to reach internal addresses, and without a hostile page being able to steer the interviewer.

## Project Conventions
- Rules consulted: `cuewise-be/CLAUDE.md` (layers, security, AI guidelines), the learning path §8b.
- Constraints:
  - Layers: route -> controller -> service. No repository is needed (nothing is stored). Files prefixed `interviews_*`; the feature-agnostic safe fetcher lives in `app/core/`.
  - Pydantic input schema with `extra="forbid"` and constrained length; `response_model` on the route; `responses=` documents errors.
  - Errors are structured `AppError` subclasses in `core/errors.py` with generic client messages; details go to logs with the request ID.
  - Auth by default (default-deny); rate limiting through the existing `core/rate_limit.py` `RateLimiter`.
  - No PII in logs: log the host and outcome, never the full URL (query strings can carry tokens) and never the page text.
  - New dependency (`trafilatura`) must be justified in the summary; the project owner approved it.
  - Tests mirror `app/modules`; no network in unit tests. No migration (nothing is stored). No commits.

## User Flow
1. The candidate, on the new-interview form, pastes a posting link and asks to import it.
2. The client calls `POST /interviews/job-url` with the URL.
3. The server fetches the page, extracts the job text, and returns `{text, truncated}`.
4. The client shows the text in the job-description box. The candidate reads it, edits it, and starts the interview with the existing `POST /interviews` and its `job_description` field (unchanged).
5. If the page cannot be fetched or read, the candidate sees a message telling them to paste the text instead.

## Requirements

### Functional

- New authenticated endpoint `POST /api/v1/interviews/job-url` taking a single `url`.
- Accepts only `http` and `https` URLs, destination port 80 or 443 only, no credentials in the URL.
- Before connecting, the host is resolved and **every** resolved address must be public. The connection goes to the address that was validated, not to a second lookup.
- Redirects are followed manually, up to a small fixed limit. Each hop gets the same scheme, port and address checks as the first request.
- Limits: connect and total time caps, a maximum body size read as a stream (about 1 MB), and a content-type allowlist (`text/html`). A non-2xx final response is a failure.
- Extraction: use the page's schema.org `JobPosting` structured data when present, otherwise the page's main readable content. The HTML is downloaded by our own safe fetcher and only then parsed; the extraction library never fetches anything.
- If too little text is extracted (for example a JavaScript-only page, a login wall, a cookie wall), return the "unreadable" error telling the user to paste the text. There is no headless browser.
- If the text does not look like a job posting (fewer than a minimum number of distinct job-related terms, such as "responsibilities", "requirements", "experience", "salary", "you will"), return the same "unreadable" error. This is a convenience filter for honest wrong links (a news article, a recipe, a blog post), not a security control: a page can stuff keywords to pass, and the candidate's review of the text stays the final check. The term list and the minimum are constants, English only, tuned on the fixtures and then on real use.
- The text is trimmed to the existing `JOB_DESCRIPTION_MAX_LENGTH` (2000) on a word boundary; `truncated` says whether anything was cut.
- Nothing is stored: not the URL, not the page. The start path, summary, prompts and retrieval are unchanged and receive the text as an ordinary job description.
- Two client-visible error codes: `job_url_unreachable` (anything network-side: refused address or port, bad scheme, DNS failure, timeout, connection error, redirect limit, non-2xx) and `job_url_unreadable` (fetched but not usable: wrong content type, too large, too little text, not a job posting). The real cause is logged, not returned.
- Rate limited per user at 10 requests per minute (configurable), 429 with `Retry-After` like the other limited endpoints.

### Paste fallback (added 2026-11-13)
Many big boards (JobStreet, often LinkedIn) refuse server fetches with a 403. The candidate's own browser can still see the page, so the fallback lets the browser do the reading: the candidate opens the posting, selects all, copies, and pastes the whole page into Cuewise. The server cleans the paste with the same rules as a fetched page.
- New authenticated endpoint `POST /api/v1/interviews/job-text` taking `content` (the paste) and `format` (`html` or `text`). The client sends the clipboard's HTML copy when it has one, else the plain-text copy. Nothing is fetched and nothing is stored.
- `html`: the same main-content extraction as a fetched page (navigation, footers, sidebars and scripts dropped). When that finds nothing (a small clipboard fragment), the visible text of the HTML is used instead, without script or style content.
- `text`: whitespace is tidied (one space between words, no blank lines); the text is otherwise kept as is. Plain text has no structure to strip menus with, which is why HTML is preferred.
- Then the same rules as the URL path: at least the minimum characters, at least the minimum distinct job terms, cut on a word boundary at 2000 with `truncated`. No LLM call.
- Response: the same `{text, truncated}` shape as `POST /interviews/job-url`.
- Failure: one generic error `job_text_unreadable` (422) asking the candidate to paste only the job description into the job description box. The cause (`too_little_text`, `not_a_posting`) is logged.
- The paste shares the job import rate limit with the URL endpoint: 10 imports per user per minute across both.
- The paste can be large: up to 1,000,000 characters (the same as the fetch byte cap), refused with 422 above that.

### Non-Functional
- **Security:** no request from this endpoint may reach loopback, private, link-local (including cloud metadata `169.254.169.254`), unique-local, multicast, reserved or unspecified addresses, in IPv4 or IPv6, including IPv4-mapped IPv6 and numeric-host forms. The refusal must not reveal which internal hosts exist.
- **Prompt injection:** fetched text is untrusted. It reaches the model only after the candidate has seen it and only through the existing job-description path, with its delimiters and injection defences. A page containing instructions must not change the interviewer's behavior.
- **Performance:** the endpoint answers or fails within a fixed overall time cap (a few seconds); it never hangs a worker.
- **Privacy:** log host, outcome and sizes only.

## UX Requirements
- Success returns text the client can drop into the job-description box, plus `truncated` so the client can say "shortened to fit; edit as needed".
- Both error messages end with a clear next step: paste the job description instead.
- Error messages are generic and identical for every cause inside a code.

## Constraints
- Python, FastAPI, `httpx` (already installed) for the fetch; `trafilatura` is the one new dependency.
- No headless browser, no JavaScript execution, no crawling beyond one page.
- `JOB_DESCRIPTION_MAX_LENGTH` is not raised; no Alembic migration.
- Unit tests use saved HTML fixtures and a fake resolver and transport. Only an opt-in live test may touch the network.

## Blockers
- The minimum-extracted-text threshold (roughly 200 characters) is chosen against the fixtures at plan time, not guessed here.
- Behavior of real job sites (bot blocking, login walls, cookie banners) is an assumption to verify manually after the build.

## Edge Cases
- **EC1:** URL scheme is not http/https (`file:`, `ftp:`, `gopher:`, `javascript:`) -> 422 validation error, no fetch.
- **EC2:** URL host is an IP literal in a private, loopback, link-local or metadata range (`127.0.0.1`, `10.0.0.5`, `169.254.169.254`, `[::1]`, `[::ffff:127.0.0.1]`) -> `job_url_unreachable`, no connection made.
- **EC3:** Public hostname that resolves to a private address -> `job_url_unreachable`, no connection made.
- **EC4:** Hostname resolves to several addresses and any one is private -> `job_url_unreachable`.
- **EC5:** DNS rebinding: a name resolves public at check time and private on a second lookup -> the connection uses only the validated address, so the private one is never contacted.
- **EC6:** Public URL redirects (301/302/307/308) to a private address or a non-http scheme -> `job_url_unreachable`; the second hop is never contacted.
- **EC7:** More redirects than the limit, or a redirect loop -> `job_url_unreachable`.
- **EC8:** URL with an explicit port other than 80 or 443 (including on a redirect) -> `job_url_unreachable`.
- **EC9:** URL contains credentials (`https://user:pass@host/`) -> 422 validation error.
- **EC10:** Server returns 4xx or 5xx (including 403 from bot blocking) -> `job_url_unreachable`.
- **EC11:** Server is slow or never answers -> `job_url_unreachable` within the overall time cap.
- **EC12:** Response is not `text/html` (PDF, image, JSON) -> `job_url_unreadable`.
- **EC13:** Body exceeds the size cap -> reading stops at the cap and the result is `job_url_unreadable`; the full body is never held in memory.
- **EC14:** Page is a JavaScript shell, login wall or cookie wall with almost no text -> `job_url_unreadable`.
- **EC15:** Page has `JobPosting` JSON-LD -> the structured fields are used and the result is the posting text, not the page chrome.
- **EC16:** Page has no structured data -> the main readable content is returned without navigation, footer and script text.
- **EC17:** Extracted text is longer than 2000 characters -> cut on a word boundary at or under 2000, `truncated: true`.
- **EC18:** Extracted text fits in 2000 characters -> returned whole, `truncated: false`.
- **EC19:** Page text contains instructions to the model ("ignore previous rules", fake closing tags like `</job_description>`) -> returned as plain text for the candidate to see; if used as the job description, the interviewer's behavior is unchanged (covered by the existing injection eval path).
- **EC20:** Page is declared in a non-UTF-8 charset -> decoded using the declared or detected charset; no crash, no garbled-byte output.
- **EC21:** Invalid or oversized `url` input (empty, over the length limit, malformed) -> 422 validation error.
- **EC22:** Unauthenticated request -> 401, no fetch.
- **EC23:** More than 10 requests in a minute by one user -> 429 with `Retry-After`, no fetch.
- **EC24:** Hostname fails to resolve -> `job_url_unreachable`.
- **EC25:** Page has plenty of text but is not a job posting (news article, recipe, blog post) -> `job_url_unreadable`; the log says `unreadable:not_a_posting`.
- **EC26:** A term repeated many times counts once (a page saying "team" twenty times is not a posting) -> only distinct terms count toward the minimum.
- **EC27:** Terms are matched case-insensitively and inside longer words where they are stems ("Responsibilities", "RESPONSIBILITY") -> counted.
- **EC28:** Posting written in a language other than English -> `job_url_unreadable` (known limitation, documented; the candidate pastes the text).
- **EC29:** HTML paste of a whole posting page with navigation, footer and "similar jobs" -> the posting text without them.
- **EC30:** HTML paste the main-content extractor can't use (a small fragment) -> the fragment's visible text, with no script or style content.
- **EC31:** Plain-text paste -> returned with whitespace tidied, otherwise unchanged (menu lines stay; known limitation of plain text).
- **EC32:** Paste with too little text (an empty selection, a few words) -> `job_text_unreadable`; log `too_little_text`.
- **EC33:** Paste that is not a posting (an article) -> `job_text_unreadable`; log `not_a_posting`.
- **EC34:** Paste longer than 2000 characters after cleaning -> cut on a word boundary, `truncated: true`.
- **EC35:** Empty content, content over 1,000,000 characters, a `format` other than `html` or `text`, or an extra field -> 422 validation error.
- **EC36:** Unauthenticated -> 401. URL imports and pastes together over 10 a minute -> 429 with `Retry-After`.
- **EC37:** Paste containing instructions to the model -> returned as plain text, like EC19.

## Acceptance Criteria
- [ ] **AC1:** `POST /api/v1/interviews/job-url` with a valid public URL whose page is a saved job posting returns 200 with `text` (non-empty) and `truncated`. (EC15, EC16, EC18)
- [ ] **AC2:** Requests to private, loopback, link-local, metadata and mapped-IPv6 addresses, by IP literal or by hostname, are refused with `job_url_unreachable` and the fake transport records zero connections to them. (EC2, EC3, EC4)
- [ ] **AC3:** A redirect into a private address, to a non-http scheme, to a disallowed port, or past the redirect limit is refused and the later hop is never contacted. (EC6, EC7, EC8)
- [ ] **AC4:** The connection is made to the address that passed validation; a resolver that returns a different address on a second call has no effect. (EC5)
- [ ] **AC5:** Non-http(s) schemes, credentials in the URL, and invalid input are rejected with 422 before any fetch. (EC1, EC9, EC21)
- [ ] **AC6:** Non-2xx responses, timeouts, resolution failures and connection errors return `job_url_unreachable`; non-HTML, oversize and near-empty pages return `job_url_unreadable`. Neither response reveals the cause beyond its code. (EC10-EC14, EC24)
- [ ] **AC7:** The size cap stops the read at the limit and the fetch fails without buffering the rest. (EC13)
- [ ] **AC8:** Text over 2000 characters is cut on a word boundary with `truncated: true`; shorter text is untouched with `truncated: false`. (EC17, EC18)
- [ ] **AC9:** Extraction prefers `JobPosting` JSON-LD and falls back to main content; navigation and script text are absent from the fallback output on the fixture pages. (EC15, EC16)
- [ ] **AC10:** The endpoint requires authentication and is rate limited at 10 per minute per user with `Retry-After`. (EC22, EC23)
- [ ] **AC11:** No test in the default suite touches the network; logs contain host and outcome but never the full URL or page text.
- [ ] **AC12:** An injection fixture page is returned as plain text, and the existing injection job-description eval cases still pass unchanged when its text is used as `job_description`. (EC19)
- [ ] **AC13:** `POST /interviews`, its schema, the summary, prompts and retrieval are unchanged, and the existing test suite still passes (the two known baseline failures aside). No migration is added.

- [ ] **AC14:** Every real-posting fixture clears the job-term minimum and every non-posting fixture (news article, recipe) falls below it; a non-posting page through the route returns `job_url_unreadable` with the generic message and logs `unreadable:not_a_posting`. (EC25-EC28)
- [ ] **AC15:** `POST /api/v1/interviews/job-text` returns `{text, truncated}` for an HTML paste (clutter removed), an HTML fragment and a plain-text paste of a posting; too-little-text and non-posting pastes return `job_text_unreadable` with one generic message. (EC29-EC34, EC37)
- [ ] **AC16:** Invalid paste bodies are 422; the endpoint requires authentication; URL and paste imports share one 10-per-minute budget. (EC35, EC36)
- [ ] **AC17:** One `app.job_url` log line per paste with `source=paste`, the format, the input size, the outcome and the output size, and never the pasted content.

## Out of Scope
- An LLM classifier for "is this a job posting": adds cost, latency and another injection surface for a convenience check.
- Detecting postings in languages other than English.
- Getting past a site's bot blocking (a fake browser identity, a headless browser, proxies, scraping services): against the sites' terms. The paste fallback is the answer to blocked sites.
- LLM condensing of long pastes: cost, latency and an injection surface before the candidate has reviewed the text. Clean, then cut.
- A browser extension or bookmarklet ("Send to Cuewise"): a later client project; it could reuse the paste endpoint.
- Storing the URL or the page (no provenance, no migration): YAGNI, and less data held.
- A `job_url` field on the start request: the preview endpoint covers it and keeps start free of network calls.
- Headless browser or JavaScript rendering, and per-site scrapers or APIs: out of scope by decision; blocked pages fall back to paste.
- PDF or other non-HTML postings.
- Robots.txt handling, caching, or crawling more than one page.
- Raising the 2000-character job-description cap.
- Résumé upload (8c), résumé-aware prompts (8d), feedback grounding (8e).
