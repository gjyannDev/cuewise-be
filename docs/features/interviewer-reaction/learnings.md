# Learnings: LLM Slice 1 (Interviewer Reaction)

How to use this file (from plan.md, "Learning Log"):
- **Predict**: you write this in your own words *before* the step starts. Guesses are fine; being wrong is the point.
- **Observed**: real output from the running code (requests, token counts, log lines). Filled in while building, never invented.
- **Why**: a short explanation of the concept, drafted together.
- **Proof**: the question from `docs/ai-engineering-learning-path.md`, answered by you in your own words.

Concepts covered: 1 How a call works, 2 Context management, 3 Prompts as data, 5 Code decides, 6 Reliability, 8 Injection baseline, 9 Observability and cost.

---

## Checkpoint A: after Step 3 (provider package)
Concepts: 6 Reliability; 1 How a call works.

**Predict** (you, before Step 3)
- Which failures deserve a retry, and which should never be retried? Why?
- What does the raw request to the model look like? What do you expect to get back?
- _your answer here_

**Observed** (Step 3, `OpenRouterProvider` driven by `httpx.MockTransport`; the responses are scripted, so token numbers are illustrative, not from a real model)
- The request the code actually builds (`app/core/ai/openrouter.py`):
  ```
  POST https://openrouter.ai/api/v1/chat/completions
  Authorization: Bearer <OPENROUTER_API_KEY>
  {
    "model": "vendor/model-x",
    "messages": [
      {"role": "system",    "content": "You are a friendly interviewer for a junior backend role."},
      {"role": "assistant", "content": "Tell me about a time you disagreed with a teammate."},
      {"role": "user",      "content": "We argued about REST vs GraphQL, so I built a small prototype."}
    ],
    "max_tokens": 150
  }
  ```
- What the provider did with each kind of response (max_retries=2):
  ```
  200 OK                 -> OK attempts=1 text='A prototype is a practical way to settle it.' tokens=61/11 finish=stop
  429 then 200           -> OK attempts=2
  503 x3                 -> LLMServerError attempts=3 status=503
  timeout x3             -> LLMTimeoutError attempts=3
  401 bad key            -> LLMRequestError attempts=1 status=401
  200 but blank text     -> LLMBadResponseError attempts=1
  ```
- Mutation check: disabling the budget check made 1 test fail; retrying *every* error made 11 tests fail. The retry tests really guard the rules.

**Why**
- An LLM API is just an HTTPS POST with JSON. There is no hidden session: the `messages` list *is* the whole conversation the model sees.
- Failures split into two groups. **Transient** ones (timeout, 429, 5xx, dropped connection) may succeed if you wait and try again, so they are retried with growing waits (0.5 s, ~1 s, plus random jitter so many clients don't retry at the same instant). **Permanent** ones (401 bad key, 400 bad request, a 200 with an unusable body) will fail exactly the same way again, so retrying only wastes time and money.
- A total time budget caps the whole thing: no retry starts if it would push the wait past ~30 s, and even a single attempt never waits longer than the budget that is left. A slow fallback is worse for the user than a fast one.
- Errors are typed (`LLMTimeoutError`, `LLMRequestError`, ...) and carry `attempts`, so the caller can log what happened without knowing anything about HTTP.

**Proof** (you)
- Concept 6: You can simulate a timeout and describe exactly what the user sees.
- _your answer here_

---

## Checkpoint B: after Step 5 (prompt and message building)
Concepts: 1 Stateless calls; 2 Context; 3 Prompts as data; 8 Injection baseline.

**Predict** (you)
- How many messages are sent to the model when the candidate answers question 3?
- Where does the candidate's text go in that list, and why not into the system prompt?
- _your answer here_

**Observed** (Step 5 + a real in-process run of the app with the fake LLM; a 3-question mixed interview)
- Messages sent on each call. The list grows by 2 every turn, because the model has no memory:
  ```
  turn 1: 3 messages, 1057 chars, roles = S A U
  turn 2: 5 messages, 1279 chars, roles = S A U A U
  turn 3: 7 messages, 1515 chars, roles = S A U A U A U
  ```
- Turn 3 as actually sent (truncated). Note how each earlier reaction is merged with the next question into one assistant turn:
  ```
  [system]    You are a friendly, professional interviewer running a mock job interview. The candidate is practicing for a j...
  [assistant] Describe a time you disagreed with a teammate. How did you resolve it?
  [user]      We argued about REST vs GraphQL for a new service, so I built two tiny prototypes...
  [assistant] Building a prototype to compare both is a practical way to settle it.\n\nHow would you debug a bug that only hap...
  [user]      I once shipped a bad migration; I rolled it back within ten minutes and wrote the postmortem.
  [assistant] Owning the rollback and writing the postmortem shows real accountability.\n\nTell me about a mistake you made at...
  [user]      I would add the column as nullable, backfill in batches, then add the constraint.
  ```
- The system prompt is `app/modules/interviews/prompts/reaction_v1.md`, filled with only `role` and `level`. Every stored reaction row has `prompt_version = reaction_v1`.

**Why**
- **Stateless (concept 1):** the API remembers nothing between calls. "The conversation" is just the list we rebuild from the database every time (`history_turns` + `build_llm_messages`).
- **Context (concept 2):** we send *everything* so far. Simple and fine for 10 questions, but input size (and cost) grows every turn. That is the trade-off you will measure with real tokens in Checkpoint G.
- **Prompts as data (concept 3):** the prompt lives in a versioned file, and each reply records which version wrote it. A changed prompt becomes `reaction_v2.md`, never an edit of v1.
- **Injection baseline (concept 8):** the candidate's text only ever goes into `user` turns, never into the system prompt, and the system prompt tells the model to treat user turns as answers, not instructions. That *reduces* the risk; it does not remove it. Slice 2 measures it.

**Proof** (you)
- Concept 1: Why does turn 10 cost more than turn 1?
- Concept 3: Can you point to the exact prompt version that produced a reply?
- _your answer here_

---

## Checkpoint C: after Steps 6-7 (answer state machine and guards)
Concepts: 5 The LLM decides (later), the code enforces.

**Predict** (you)
- What happens when the candidate double-clicks "submit"?
- Who decides that the interview moves to the next question: the model or the code?
- _your answer here_

**Observed** (Steps 6-7)
- Submitting question 1 a second time, right after it was answered:
  ```
  409 {"code": "QUESTION_NOT_CURRENT", "message": "This is not the current question of the interview", ...}
  app.errors: QUESTION_NOT_CURRENT: ... (app/modules/interviews/interviews_controller.py:125 answer)
  ```
- The rule lives in code, twice: the controller checks `question_id == current question`, and the repository's `record_answer` only advances with a conditional `UPDATE ... WHERE current_position = :expected AND status = 'in_progress'`. Zero rows updated = someone else got there first = nothing saved.
- Mutation check: removing either guard made 2 extra tests fail.

**Why**
- Progress through the interview is a **state machine owned by the code**: position 1 -> 2 -> ... -> completed. The LLM in this slice only writes a sentence; it cannot move, skip or repeat a question, because nothing it returns is used to decide the next step.
- The compare-and-swap makes double-clicks and retries safe without locks: whichever request commits first wins; the other one matches zero rows and gets a clean 409.
- This is the "LLM decides, code enforces" pattern in its simplest form. In Slice 3 the model will *suggest* "follow up or move on", and this same code will still decide whether that is allowed.

**Proof** (you)
- Concept 5: Can a reply from the model ever skip or repeat a question? Why not?
- _your answer here_

---

## Checkpoint D: after Step 8 (LLM in the answer flow)
Concepts: 1, 2 Context cost; 6 Fallback.

**Predict** (you)
- Will the candidate notice when the LLM is down? What will they see?
- How many more prompt tokens will turn 3 send than turn 1?
- _your answer here_

**Observed** (Step 8, fake LLM; its token numbers are *estimates* = characters / 4, real ones come in Checkpoint G)
- Prompt tokens per reaction, read from the stored rows: `264 -> 319 -> 378`. Turn 3 sends ~43% more input than turn 1 for a reply of the same size (~17 tokens).
- LLM "down" (a 401 bad key) on a fresh interview:
  ```
  201  reaction = None  | next position = 2
  ERROR app.llm: llm_call session=... model=- prompt_version=reaction_v1 prompt_tokens=- completion_tokens=- latency_ms=0 attempts=1 finish=- outcome=LLMRequestError
  ```
  The candidate only notices that there is no reaction line; the answer is saved and the next question appears.
- A test proves no database transaction is open while the LLM call runs; moving the message-building after the commit makes that test fail.

**Why**
- Input cost grows every turn because the whole history is resent (concept 2). Output cost stays flat because `max_tokens` caps it.
- **Short write, slow call, short write:** save the answer and advance (commit), then call the LLM with no transaction open, then save the reaction (commit). A slow or failing LLM can never lose the answer or hold database locks for 30 seconds.
- **The fallback is a value, not an error:** any LLM failure becomes `reaction: null`. Only a database failure is a real 500.

**Proof** (you)
- Concept 2: Which context strategy does this slice use, and what does it cost?
- _your answer here_

---

## Checkpoint E: after Step 9 (usage logging)
Concepts: 9 Observability and cost.

**Predict** (you)
- What should one log line about an LLM call tell you? What must never be in it?
- _your answer here_

**Observed** (Step 9, real log lines from `logs/app.log`; one line per LLM call, with the HTTP request id in brackets)
```
INFO  [a8ddd64a...] app.llm: llm_call session=01a185bd-... model=fake-model prompt_version=reaction_v1 prompt_tokens=264 completion_tokens=17 latency_ms=0 attempts=1 finish=stop outcome=ok
INFO  [36f01bb7...] app.llm: llm_call session=01a185bd-... model=fake-model prompt_version=reaction_v1 prompt_tokens=319 completion_tokens=18 latency_ms=0 attempts=1 finish=stop outcome=ok
ERROR [28e2788d...] app.llm: llm_call session=01a185bd-... model=- prompt_version=reaction_v1 prompt_tokens=- completion_tokens=- latency_ms=0 attempts=1 finish=- outcome=LLMRequestError
```
- Cost of one interview from the database (same numbers, no log parsing):
  ```sql
  SELECT session_id, SUM(prompt_tokens + completion_tokens) AS tokens
  FROM interview_messages WHERE role = 'interviewer' GROUP BY session_id;
  -- 1012 tokens for the 3-question interview above (fake estimates)
  ```
- A test asserts that no log line contains the answer, the reaction, the job description or the key.

**Why**
- One line per call answers "what happened, how slow, how big, which model and prompt" without ever writing personal text. Answers and replies are personal data, so only metadata is logged.
- Levels carry meaning: `INFO` = fine, `WARNING` = transient (timeout, 429, 5xx: expected now and then), `ERROR` = needs a human (bad key, broken reply).
- Storing usage on the reaction row turns cost into a SQL query. Multiply tokens by your model's price per token to get money.

**Proof** (you)
- Concept 9: How would you answer "how much does one interview cost?" with a number?
- _your answer here_

---

## Checkpoint F: after Step 10 (transcript endpoint)
Concepts: 2 Context vs what the user sees.

**Predict** (you)
- Is the transcript the user sees the same as what the model receives? What differs?
- _your answer here_

**Observed** (Step 10, `GET /api/v1/interviews/{id}/messages` for the same interview as Checkpoint B)
```
1 interviewer question Describe a time you disagreed with a teammate. How did you resolve it?
1 candidate   answer   We argued about REST vs GraphQL for a new service, so I built two tiny
1 interviewer reaction Building a prototype to compare both is a practical way to settle it.
2 interviewer question How would you debug a bug that only happens in production?
...
3 interviewer reaction Splitting the migration into small reversible steps keeps risk low.
```
Compare with what the model received on turn 3 (Checkpoint B): a system prompt the user never sees, and reaction + next question glued into one assistant turn.

**Why**
- Both views come from the same stored rows. The **transcript** is for people: one item per thing shown, in order, nothing hidden or merged. The **model input** is for the LLM: a system prompt, strict role alternation, and only what the model needs.
- Keeping these two views separate is what later lets you change the model input (trim history, add a summary, add the job description) without changing what the user sees.

---

## Checkpoint G: after Step 11 (real API, Proof round)
Concepts: 1, 2, 6, 9.

**Predict** (you)
- Your estimate of the token total and cost of one full 5-question interview.
- _your answer here_

**Observed** (real OpenRouter runs; needs a key)
- Prompt tokens on turn 1 vs the last turn: _
- Same answer 5 times at temperature 0 vs 1: _
- `max_tokens` very small: the cut-off reply and its `finish_reason`: _
- Wrong key / tiny timeout: what the user saw, what the log said: _
- Token total and cost for one full interview: _

**Proof** (you)
- Concepts 1, 2, 6, 9, answered with the numbers above.
- _your answer here_
