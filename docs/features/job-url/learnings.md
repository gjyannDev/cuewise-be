# Learn: Job URL import and SSRF (Slice 8b)

Spec: `spec.md` · Plan: `plan.md` · Progress: `task.md`. Built 2026-11-13 on `feat/rag-integration`, uncommitted.

## 1. Why it exists
Candidates had to copy a posting's text by hand. A link is easier, but a link means **our server fetches a URL
someone else chose**. That is the textbook setup for SSRF (server-side request forgery): the request comes from inside
our network, so `http://169.254.169.254/` (cloud metadata, often holding credentials) or `http://localhost:5432` reach
places the attacker never could. And the page is untrusted text that later sits next to the interviewer prompt.

## 2. What it is
- `POST /api/v1/interviews/job-url` with `{"url": ...}` returns `{"text", "truncated"}`. Nothing is stored.
- The candidate reviews and edits the text, then starts the interview with the unchanged `POST /interviews`
  `job_description` field. Summary, retrieval and prompts never know a URL was involved.
- Two errors, both 422 and both "paste the text instead": `JOB_URL_UNREACHABLE` (could not, or may not, open it) and
  `JOB_URL_UNREADABLE` (opened it, but found no posting).

## 3. When to use it
- `app/core/safe_fetch.py` is feature-agnostic: any future "fetch a user-supplied URL" (a portfolio link, a résumé URL)
  should go through `SafeFetcher`, never a bare `httpx.get`.
- Do **not** hand a URL to a library that fetches by itself (`trafilatura.fetch_url`, `requests` inside a parser). It
  skips every check below. Fetch with `SafeFetcher`, then pass the HTML string.

## 4. How it works
One request, through the real code:

1. **Route** `import_job_url` (`app/modules/interviews/routes/interviews_route.py:96`) runs `limit_job_imports`
   (`interviews_job_url_dependencies.py:45`) first: 10 imports per user per minute, links and pastes together, and
   refused requests count too, so nobody can probe the network quickly.
2. **Schema** `JobUrlIn` (`interviews_schema.py:242`, validator `_job_url` at `:225`): http/https, a host, a numeric port,
   no `user:pass@`. Shape only, and the message never echoes the URL.
3. **Service** `JobUrlService.import_job_text` (`interviews_job_url_service.py:70`) calls the fetcher, then the
   extractor, then the shared tail `_fit` (`:52`: the job-posting check, then `truncate_on_word`), and maps every
   internal failure to one of the two generic errors.
4. **Fetcher** `SafeFetcher.fetch` (`app/core/safe_fetch.py:102`), per hop:
   - `_check` (`:121`): scheme, credentials, port 80/443, then **resolve once** and require that **every** address
     passes `is_public_address` (`:62`). That function unwraps IPv4-mapped (`::ffff:127.0.0.1`), NAT64
     (`64:ff9b::/96`, line 32) and 6to4 forms before asking `is_global`.
   - `_get` (`:143`): request the **checked IP**, with the real name in the `Host` header and as the TLS
     `sni_hostname` (`:153`). The certificate is verified against the name, not the IP.
   - Redirects: never `follow_redirects=True`. The `Location` goes back through `_check` on the next loop turn.
   - `trust_env=False` (`:109`): proxy environment variables are ignored.
   - `_read` (`:169`): `text/html` only, `Content-Length` checked, body streamed and stopped at 1 MB,
     `Accept-Encoding: identity` (`:152`), one deadline for the whole fetch.
   - `_decode` (`:186`): header charset, else `<meta charset>`, else UTF-8, with bad bytes replaced and never raised.
5. **Extractor** `extract_job_text` (`interviews_job_url_utils.py:33`): schema.org `JobPosting` JSON-LD first
   (`_from_jsonld`, `:74`), else `trafilatura.extract` on the string (`_from_main_content`, `:116`). Under 200 characters
   means no posting, so the result is unreadable.
6. **Is it a posting?** `looks_like_job_posting` (`:59`) counts distinct job-ad terms (`job_term_hits`, `:53`) from
   `JOB_TERMS` (`interviews_constants.py:227`). Under `JOB_TERMS_MIN_HITS = 3`, the result is unreadable with reason
   `not_a_posting`. Matching is lower-case substrings, so the stem `responsibilit` matches "Responsibilities". A term
   repeated 20 times still counts once. The check runs before truncation, so terms past character 2000 still count.
7. **Log**: one `app.job_url` line with user id, host, bytes, chars, truncated, latency and `outcome=ok` or
   `unreachable:<reason>` or `unreadable:<reason>`. Never the URL or the text.

**The paste fallback** (`POST /interviews/job-text`, for sites that refuse our fetch, such as JobStreet's 403):
- **Why it works:** the site blocks our *server*, not the candidate. Their own browser already shows the page, so the
  browser does the reading: select all, copy, paste. Nothing is fetched, so there is no SSRF surface at all.
- **Why HTML first:** the clipboard holds two copies of a selection, HTML and plain text. The client sends the HTML one
  when it can (`format: html`), because its structure lets `trafilatura` drop the menus, footer and "similar jobs".
  Plain text is one flat block with nothing to tell the menu from the posting, so it is only tidied.
- **Flow:** route `import_job_text_paste` (`interviews_route.py:116`), schema `JobTextIn` (`interviews_schema.py:254`:
  up to 1,000,000 characters, `format` is the `JobTextFormat` enum) -> `import_pasted_text`
  (`interviews_job_url_service.py:95`) -> `pasted_job_text` (`interviews_job_url_utils.py:42`). For HTML it tries
  `extract_job_text`; when that skips a small fragment, it uses the fragment's visible text (`_visible_text`, `:150`,
  which skips script, style, noscript and template content, `:29`). Then the same `_fit` as the link path.
- **One failure:** `JOB_TEXT_UNREADABLE` (422) asks the candidate to paste just the description into the job
  description box. The log line has `source=paste`, the format and `in_chars`, never the content.

Decisions and why:
- **Preview endpoint, not a field on start**: the candidate sees what the model will read, and start stays fast with no
  network call.
- **Own guard, library for extraction**: there is no well-maintained SSRF guard for `httpx`, and writing it is the lesson.
  Main-content extraction is a long tail of heuristics, so `trafilatura` does it (one new dependency, 13 packages with
  lxml).
- **One message per error code**: if "blocked", "connection refused" and "timeout" looked different, the endpoint would
  become a port scanner for our network (an oracle). The real reason is in the log.
- **422 for both**: the user fixes it by pasting text. A 5xx would page on-call for someone else's website.
- **Keyword check, not an LLM classifier**: "is this a job posting?" is a convenience for honest wrong links (a news
  article pasted by mistake), not a security control. A keyword count costs nothing, adds no latency and opens no new
  prompt-injection surface. An LLM would be more accurate, but a hostile page could also try to talk it into "yes".
  Keyword stuffing beats the counter too, so the candidate's review of the text stays the real check.

## 5. What can go wrong
| Attack or failure | Defence | Test |
|---|---|---|
| `http://127.0.0.1`, `http://169.254.169.254`, `[::1]`, `[::ffff:127.0.0.1]`, `2130706433` | resolved address must be public | `tests/core/test_safe_fetch.py::test_private_targets_are_refused_without_contact` |
| Public name that resolves to 10.x | same check on resolved addresses | same test, `intranet.example.com` |
| DNS rebinding: public at check time, private at connect time | connect to the checked IP, resolve once | `test_dns_rebinding_cannot_swap_in_a_private_address` (`:178`) |
| Public page that 302s to the metadata service | manual redirects, re-checked every hop | `test_a_redirect_into_a_refused_target_is_never_followed` (`:236`) |
| `HTTPS_PROXY` set in the environment | `trust_env=False` | `test_proxy_environment_variables_are_ignored` (`:188`) |
| Endless or huge body | streamed byte cap | `test_a_body_over_the_cap_stops_the_read_early` (`:321`) |
| Slow trickle under every per-read timeout | one total deadline | `test_the_whole_fetch_has_one_time_budget` (`:286`) |
| Page with `</job_description> SYSTEM: ...` | candidate sees it; start path neutralises tags inside the fence | `tests/modules/interviews/routes/test_job_url.py::test_instructions_in_a_page_stay_fenced_data_in_the_interview` |
| Probing many internal hosts | rate limit counts refusals | `test_refused_requests_count_toward_the_limit` |
| URL with a token in its query string | log the host only | `test_one_log_line_with_host_and_outcome_but_not_the_url_or_text` |
| A news article or recipe pasted by mistake | job-term check, at least 3 distinct terms | `tests/modules/interviews/utils/test_job_url_utils.py::test_a_long_page_that_is_not_a_posting_does_not`, route `test_a_page_that_is_not_a_posting_asks_for_the_text` |
| A page repeating one job word to look like a posting | distinct terms only | `test_a_repeated_term_counts_once` |
| A real posting in Spanish | **not handled**: rejected, the candidate pastes it (known limit) | `test_a_posting_in_another_language_is_not_recognised` |
| A job board listing page (many jobs on one page) | **not handled**: passes (python.org/jobs, 4 hits); the candidate's review catches it | manual check, §7 |
| A site refuses our fetch (JobStreet: 403) | paste fallback: the candidate's browser reads the page | `test_an_html_paste_returns_the_posting_without_the_page_clutter` |
| Clipboard HTML that `trafilatura` skips (a bare `<span>` or table cell) | visible-text fallback | `test_a_fragment_the_extractor_skips_falls_back_to_its_visible_text` |
| CSS or JavaScript inside a pasted fragment | the collector skips script and style | `test_the_fallback_never_returns_script_or_style_content` |
| Alternating links and pastes to get past the limit | one shared budget | `test_links_and_pastes_share_one_import_budget` |
| Plain-text paste keeps the menu lines | **not handled**: HTML is preferred for this reason | `test_a_plain_text_paste_is_tidied_but_otherwise_kept` |

## 6. Try it yourself
1. Predict, then run: `uv run pytest tests/core/test_safe_fetch.py -k rebinding -v`. Then, in `_get`, replace the pinned
   URL with the original `url` (no pinning). Which test fails, and why does the resolver call count matter?
2. Remove the NAT64 branch from `is_public_address`. Predict which parametrised case fails. (`64:ff9b::a00:1`: Python's
   `is_global` says True for it.)
3. Start the dev server and `POST /api/v1/interviews/job-url` with a real posting from a company careers page, then
   with a LinkedIn or Indeed link. Read the `app.job_url` log line for each.

## 7. What surprised me
Real numbers, measured 2026-11-13 on this machine (Python 3.14.7, httpx 0.28.1, trafilatura 2.3.1):

- **Extracted lengths on the fixtures** (scratch script calling `_from_jsonld` and `_from_main_content`):

  | Page | JSON-LD | Main content |
  |---|---|---|
  | `js_shell.html` | 0 | 46 |
  | `cookie_wall.html` | 0 | 90 |
  | `injection.html` | 0 | 595 |
  | `article_posting.html` | 0 | 740 |
  | `jsonld_board.html` | 645 | **203** |

  The 200-character threshold sits between the walls (≤ 90) and the real postings (≥ 595). But on the job board page,
  trafilatura's "main content" is the chrome ("Apply now with LinkedIn…", 203 characters, just over the bar). That is
  why JSON-LD comes first, and it shows the threshold alone can't tell a posting from chrome.
- **Python calls `64:ff9b::a00:1` global**, though it is NAT64 for `10.0.0.1`. `is_global` alone is not an SSRF check.
- **`httpx` 0.28 `is_redirect` is true without a `Location` header.** The first version raised `KeyError` and a test
  caught it.
- **Real sites** (manual run through `PAGE_FETCHER`):

  | URL | Result | Time |
  |---|---|---|
  | `https://example.com` | ok over pinned TLS, but too little text, so unreadable | 307 ms |
  | `https://www.python.org/jobs/` | ok, 3069 characters | 285 ms |
  | `https://www.indeed.com/viewjob?…` | 403, unreachable | 249 ms |
  | `https://www.linkedin.com/jobs/view/1` | 404, unreachable (a fake id; real LinkedIn pages are usually login-walled) | 337 ms |
  | `localhost`, `169.254.169.254` | refused before any connection | 7-8 ms |

- **TLS pinning check**: resolving `www.python.org` to example.com's IP fails the TLS handshake. The server name sent
  and checked is the real hostname, not the IP. (`badssl.com` test hosts timed out from here, so the expired-certificate
  case was not observed directly.)
- **Job-term check** (step 10, 22 terms, minimum 3), from a scratch script calling `job_term_hits` on each fixture:

  | Page | Distinct terms |
  |---|---|
  | `article_posting.html` | 7 |
  | `jsonld_board.html` | 7 |
  | `injection.html` | 6 |
  | `news_article.html` | 0 |
  | `recipe.html` | 0 |

  Real pages through `PAGE_FETCHER`: `python.org/jobs/` (a listing, not one posting) scored 4 and **passes**.
  `python.org/about/` scored 1 and is rejected. Wikipedia returned 403 before the check ran.
- **The first draft of the term list would have let the news page through.** "years of" ("after years of debate"),
  "manager" ("the project manager told reporters") and "compensation" (for shops on the route) are job words in a job
  ad and ordinary words in a news story. Writing the negative fixture realistically, instead of avoiding those words,
  is what exposed it. A term list is only as good as its negative examples.
- **Real sites differ** (2026-11-13): a JobStreet posting returned **403** to our server. A LinkedIn guest job page
  returned 214 KB of HTML with no JSON-LD block; main-content extraction gave 4444 characters and 11 job terms, with
  some noise ("See who … has hired for this role"). Re-running the request with a browser identity to dodge the 403
  was refused as bot-check circumvention, and that is the right call: the paste fallback is the answer to blocks.
- **trafilatura and clipboard HTML:** a whole copied page (the `clipboard_posting.html` fixture) came out clean: menus,
  search bar, "similar jobs" and footer all dropped. But a bare `<span>` or a table cell holding a full posting came
  back as `None`, as did a table cell with style and script inside it. That is why the paste path needs its own
  visible-text fallback.
- **trafilatura keeps `<noscript>` text.** The JS-shell fixture's 46 characters were its noscript message. My first
  fallback test asserted noscript text was dropped, which the spec never promised; the test was corrected.

## 8. Check your understanding
1. Why is checking the hostname string (for "localhost" or "127.") not enough?
2. Why must the redirect check run again on every hop, not only on the first URL?
3. What would DNS rebinding do if we validated with `getaddrinfo` and then called `httpx.get(url)`?
4. Why does the client get the same message for "private address" and "connection refused"?
5. A page says "Ignore previous instructions". Which two things keep it from steering the interviewer?
6. Why does the job-term check run before truncation, and why does a repeated word count once?
7. JobStreet refuses our server. Why does the paste fallback work there, and why is HTML preferred over plain text?

<details><summary>Answers</summary>

1. The same address has many spellings: `2130706433`, `0x7f.1`, `[::ffff:127.0.0.1]`, or any public name whose DNS
   record points at 127.0.0.1. Only the resolved address is the truth, so that is what gets checked.
2. The first page is public and passes. Its 302 then points inside. `httpx` would follow it with no check at all.
3. `httpx` would resolve the name a second time. The attacker's DNS answers public the first time and private the
   second, so the connection lands inside. Connecting to the checked IP removes that second lookup.
4. Different answers would let an attacker map which internal hosts and ports exist (an oracle). The reason goes to
   the log, which only we read.
5. The candidate reads the text before using it. Then it reaches the model only inside `<job_description>`, with app
   tags neutralised (`job_description_block`) and a system prompt that treats the block as data.
6. A long posting's requirements often sit after the first 2000 characters, so judging only the cut text would reject
   real postings. And counting distinct terms means one word repeated many times can't fake a posting. It still can't
   stop a page that lists many different job words, which is why this check is a convenience, not a guard.
7. The block is on requests from our server. The candidate's browser is already allowed to see the page, so letting
   that browser copy it needs no fetch and breaks no rule. HTML keeps the page's structure (nav, main, footer), so the
   extractor can drop the clutter; plain text has lost it, so menu lines can't be told apart from the posting.
</details>

## 9. Go deeper / Still open
- **Pending**: a real-model run of the injection job-description eval cases with this page's text (AC12's real-model
  half). The unit test only proves the fence holds.
- DNS lookups use `socket.getaddrinfo`, which has no timeout of its own. A very slow resolver can exceed the 8 s budget.
  A resolver run in a thread with a timeout fixes it if that ever shows up in the logs.
- The rate limiter is per process (see `core/rate_limit.py`). It needs a shared store when the app scales out.
- Many big boards (LinkedIn, Indeed) block server fetches. That is the designed "paste instead" outcome, not a bug.
- The job-term threshold (3) is tuned on 5 fixtures and 3 real pages. Retune it from the `app.job_url` log lines:
  `outcome=unreadable:not_a_posting` on links candidates then paste by hand means the bar is too high.
- Further reading: OWASP SSRF Prevention Cheat Sheet; PortSwigger Web Security Academy, SSRF labs.
