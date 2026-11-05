# Learn: Calling an LLM safely (Slice 1, interviewer reaction)

**Concepts:** 1 How a call works, 2 Context management, 3 Prompts as data, 5 Code decides, 6 Reliability,
8 Injection baseline, 9 Observability and cost. See `docs/ai-engineering-learning-path.md`.

> **Note on history.** This slice was built first, when the LLM wrote a short *reaction* to each answer
> (`reaction_v1`, `OpenRouterProvider`). Since then the provider became vendor-neutral
> (`OpenAICompatibleProvider`) and reactions became predefined lines (see `llm-interviewer/learnings.md`, section 7).
> The measurements below are from the original build and are kept as recorded. The code locations in section 4 are the
> current ones.

---

## 1. Why it exists

The app needed its first real LLM call, and an interview must never break because of it. A model call is not like a
database query:

- It is **slow** (seconds) and **sometimes fails** (timeout, 429, 5xx, a bad key).
- It has **no memory**: the model only knows what you send in that one request.
- It **costs money per token**, so a longer conversation costs more every turn.
- Its output is **untrusted text**, and the candidate's answer is untrusted input going into it.

Slice 1 is the plumbing that makes one call safe: a provider with timeouts and retries, a way to rebuild the
conversation, a code-owned state machine, a fallback, and one log line per call.

## 2. What it is

- **A call is an HTTPS POST with JSON.** The `messages` list *is* the whole conversation the model sees. There is no
  hidden session. Every turn, the app rebuilds the list from the database (**stateless**).
- **Failures split in two.** *Transient* ones (timeout, 429, 5xx, dropped connection) may succeed on retry, so they are
  retried with growing waits and random jitter. *Permanent* ones (401 bad key, 400 bad request, a 200 with an unusable
  body) fail the same way again, so retrying only wastes time and money.
- **A total time budget** caps everything: no retry starts if it would push the wait past about 30 s.
- **The code owns progress.** The model only writes a sentence. A state machine in code decides which question is
  current, so nothing the model says can skip or repeat a question ("the LLM decides, the code enforces").
- **A fallback is a value, not an error.** If the LLM fails, the reaction is simply `null`.

## 3. When to use it

| Do this | When | Why / the limit |
|---|---|---|
| Retry | Timeout, 429, 5xx, dropped connection | Might succeed next time. Cap with attempts **and** the time budget |
| Never retry | 401, 400, 200 with an unusable body | Fails identically; costs time and money |
| Resend the full history every call | Short conversations (about 10 questions) | Simple and fine, but input cost grows every turn |
| Put candidate text only in `user` turns | Always | Reduces injection risk. It does not remove it |
| Keep the DB transaction closed during the call | Always | A slow LLM must not hold locks or lose the answer |
| Return `null` on any LLM failure | Whenever the LLM part is optional | The interview continues; only a DB failure is a real 500 |

**I'd revisit this when** input tokens or hidden reasoning start to dominate the bill. That happened: it led to the
context-management slice (`context-management/learnings.md`).

## 4. How it works

**The options** (the main decisions):

| Decision | Chosen | Alternative | Why |
|---|---|---|---|
| Where progress lives | Code (state machine, compare-and-swap) | Let the model say when to move on | Models don't reliably follow rules; code does |
| When to call the LLM | After saving the answer (commit), with no transaction open, then save the reaction | Hold one transaction around the call | A slow or failing LLM can't lose the answer or hold locks for 30 s |
| Transcript vs model input | Two views built from the same rows | One shared structure | Lets the model input change (trim history, add a summary) without changing what the user sees |
| What to log | Metadata only, one line per call | Log the text | Answers and replies are personal data |

**The flow** (current code):

```
POST /interviews/{id}/messages
  controller   interviews_controller.py:264   answer / prepare_answer:283 / finish_answer:370
  provider     openai_compatible.py:73   complete(): the request, retries inside the time budget
               openai_compatible.py:175  _attempt(): one HTTP call -> LLMResult or a typed LLMError
  retry rules  retry.py:21   retry_delay(): which errors wait and try again, and for how long
  save         interviews_repository.py:163   record_turn(): conditional UPDATE + inserts in one commit
  log          interviews_turn.py:646   log_llm_call(): one metadata line per call
```

**The request the code builds** (Slice 1 build, `OpenRouterProvider` driven by `httpx.MockTransport`; responses are
scripted, so token numbers are illustrative):

```
POST https://openrouter.ai/api/v1/chat/completions
Authorization: Bearer [REDACTED:Authorization header]
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

**Messages grow by 2 every turn** (a 3-question mixed interview, real run with the fake LLM):

```
turn 1: 3 messages, 1057 chars, roles = S A U
turn 2: 5 messages, 1279 chars, roles = S A U A U
turn 3: 7 messages, 1515 chars, roles = S A U A U A U
```

Each earlier reaction is merged with the next question into one assistant turn. The system prompt is
`prompts/reaction_v1.md` (versioned file), filled with only `role` and `level`, and every stored reaction row records
its `prompt_version`.

Errors are **typed** (`LLMTimeoutError`, `LLMRequestError`, ... in `provider.py`) and carry `attempts`, so the caller
can log what happened without knowing anything about HTTP.

## 5. What can go wrong

| Failure | What the user sees | What the code does | Proof |
|---|---|---|---|
| `429` then `200` | A reaction, a little slower | Retries: `OK attempts=2` | provider tests |
| `503` x3 / timeout x3 | No reaction line; next question appears | `LLMServerError` / `LLMTimeoutError` after 3 attempts, reaction `null` | provider tests |
| `401` bad key | No reaction line | `LLMRequestError attempts=1`, no retry, `ERROR` log | provider tests |
| `200` with blank text | No reaction line | `LLMBadResponseError attempts=1`, no retry | provider tests |
| Double-click on submit | Second click gets a `409` | `QUESTION_NOT_CURRENT`; a conditional `UPDATE ... WHERE current_position = :expected AND status = 'in_progress'` matches zero rows, so nothing is saved | tests; removing either guard made 2 extra tests fail |
| Server dies mid-call | Nothing saved; resubmit works | The answer is saved before the call, the reaction after (short write, slow call, short write) | test: no DB transaction open while the LLM runs |
| A log line leaks personal text | n/a | Only metadata is logged | test asserts no log line contains the answer, reaction, job description or key |

Mutation checks: disabling the time-budget check made 1 test fail; retrying *every* error made 11 tests fail.

## 6. Try it yourself

Write your prediction first, then check.

1. **Retry rules.** Predict which failures deserve a retry and which never should. Then read
   `retry_delay` in `app/core/ai/retry.py:21` and compare.
2. **Stateless.** Predict how many messages are sent when the candidate answers question 3 (answer: look at the
   table in section 4), and why the candidate's text is not put in the system prompt.
3. **Double-click.** Predict who decides the interview moves on (the model or the code), and what a second submit
   gets. Find the conditional `UPDATE` in `record_turn` (`interviews_repository.py:163`).
4. **Cost.** Predict how many more prompt tokens turn 3 sends than turn 1, then run:
   ```sql
   SELECT session_id, SUM(prompt_tokens + completion_tokens) AS tokens
   FROM interview_messages WHERE role = 'interviewer' GROUP BY session_id;
   ```
5. **Logs.** Predict what one log line about an LLM call should tell you, and what must never be in it. Then read
   `log_llm_call` (`interviews_turn.py:646`) and a few lines of `logs/app.log`.

## 7. What surprised me

**Checkpoint A: what the provider did with each response** (`max_retries=2`, scripted responses):

```
200 OK                 -> OK attempts=1 text='A prototype is a practical way to settle it.' tokens=61/11 finish=stop
429 then 200           -> OK attempts=2
503 x3                 -> LLMServerError attempts=3 status=503
timeout x3             -> LLMTimeoutError attempts=3
401 bad key            -> LLMRequestError attempts=1 status=401
200 but blank text     -> LLMBadResponseError attempts=1
```

Backoff is 0.5 s, about 1 s, plus jitter so many clients don't retry at the same instant.

**Checkpoint B: turn 3 as actually sent** (truncated):

```
[system]    You are a friendly, professional interviewer running a mock job interview. The candidate is practicing for a j...
[assistant] Describe a time you disagreed with a teammate. How did you resolve it?
[user]      We argued about REST vs GraphQL for a new service, so I built two tiny prototypes...
[assistant] Building a prototype to compare both is a practical way to settle it.\n\nHow would you debug a bug that only hap...
[user]      I once shipped a bad migration; I rolled it back within ten minutes and wrote the postmortem.
[assistant] Owning the rollback and writing the postmortem shows real accountability.\n\nTell me about a mistake you made at...
[user]      I would add the column as nullable, backfill in batches, then add the constraint.
```

**Checkpoint C: the double-click.** Submitting question 1 a second time, right after it was answered:

```
409 {"code": "QUESTION_NOT_CURRENT", "message": "This is not the current question of the interview", ...}
app.errors: QUESTION_NOT_CURRENT: ... (app/modules/interviews/interviews_controller.py:125 answer)
```

The rule lives in code, twice: the controller checks `question_id == current question`, and the repository only advances
with a conditional `UPDATE`. The model's reply is never used to decide the next step.

**Checkpoint D: input cost and the LLM being down** (fake LLM; its token numbers are estimates = characters / 4).
Prompt tokens per reaction, read from the stored rows: `264 -> 319 -> 378`. Turn 3 sends about 43% more input than turn 1
for a reply of the same size (about 17 tokens). With a 401 bad key on a fresh interview:

```
201  reaction = None  | next position = 2
ERROR app.llm: llm_call session=... model=- prompt_version=reaction_v1 prompt_tokens=- completion_tokens=- latency_ms=0 attempts=1 finish=- outcome=LLMRequestError
```

The candidate only notices there is no reaction line; the answer is saved and the next question appears. A test proves
no database transaction is open while the LLM call runs; moving the message-building after the commit makes it fail.

**Checkpoint E: one log line per call** (real lines from `logs/app.log`, with the HTTP request id in brackets):

```
INFO  [a8ddd64a...] app.llm: llm_call session=01a185bd-... model=fake-model prompt_version=reaction_v1 prompt_tokens=264 completion_tokens=17 latency_ms=0 attempts=1 finish=stop outcome=ok
INFO  [36f01bb7...] app.llm: llm_call session=01a185bd-... model=fake-model prompt_version=reaction_v1 prompt_tokens=319 completion_tokens=18 latency_ms=0 attempts=1 finish=stop outcome=ok
ERROR [28e2788d...] app.llm: llm_call session=01a185bd-... model=- prompt_version=reaction_v1 prompt_tokens=- completion_tokens=- latency_ms=0 attempts=1 finish=- outcome=LLMRequestError
```

Levels carry meaning: `INFO` = fine, `WARNING` = transient (timeout, 429, 5xx), `ERROR` = needs a human (bad key,
broken reply). Cost of the 3-question interview, read from the database: 1012 tokens (fake estimates).

**Checkpoint F: the transcript is not what the model receives.** `GET /api/v1/interviews/{id}/messages`:

```
1 interviewer question Describe a time you disagreed with a teammate. How did you resolve it?
1 candidate   answer   We argued about REST vs GraphQL for a new service, so I built two tiny
1 interviewer reaction Building a prototype to compare both is a practical way to settle it.
2 interviewer question How would you debug a bug that only happens in production?
...
3 interviewer reaction Splitting the migration into small reversible steps keeps risk low.
```

Compare with what the model received on turn 3: a system prompt the user never sees, and reaction + next question glued
into one assistant turn. Both views come from the same stored rows.

## 8. Check your understanding

1. **(Proof, concept 6)** You simulate a timeout. Describe exactly what the user sees.
2. **(Proof, concept 1)** Why does turn 10 cost more than turn 1?
3. **(Proof, concept 3)** Can you point to the exact prompt version that produced a reply?
4. **(Proof, concept 5)** Can a reply from the model ever skip or repeat a question? Why not?
5. **(Proof, concept 2)** Which context strategy does this slice use, and what does it cost?
6. **(Proof, concept 9)** How would you answer "how much does one interview cost?" with a number?
7. **(Why)** Why is a `401` never retried but a `503` is?
8. **(When)** When is "resend the full history" a fine choice, and what tells you to stop?
9. **(How)** How does the code stop two submits of the same answer from both winning?
10. **(What if)** What if the app held one DB transaction open around the LLM call?

<details>
<summary>Reference answers (write yours first)</summary>

1. The provider retries with growing waits until the attempts or the time budget run out, then raises
   `LLMTimeoutError`. The controller turns any LLM failure into `reaction: null`. The answer was already saved, so the
   candidate sees no reaction line, and the next question appears. An `ERROR`/`WARNING` log line records it.
2. The API remembers nothing, so every call resends the whole history. Input tokens (and cost) grow by one turn per
   question: prompt tokens went `264 -> 319 -> 378`, about 43% more at turn 3 than turn 1.
3. Yes. Every stored reaction row has `prompt_version` (`reaction_v1`), and the `llm_call` log line carries it.
4. No. Progress is a state machine in code. Nothing the model returns decides the next step, the controller checks
   `question_id == current question`, and the repository's conditional `UPDATE ... WHERE current_position = :expected`
   advances only once.
5. Full history: everything so far is sent each time. Fine for about 10 questions, but input grows every turn. This is
   what Checkpoint G / the context-management slice measures.
6. Sum `prompt_tokens + completion_tokens` per session (the SQL in section 6), then multiply by the model's price per
   token. Example from the fake run: 1012 estimated tokens for 3 questions.
7. A `401` is permanent: the same key fails identically, so retrying wastes time and money. A `503` is transient and may
   succeed next time.
8. When the conversation is short and the cost is acceptable. Stop when input or hidden reasoning start to dominate the
   bill or hit the limit (which is what happened, and led to the context-management slice).
9. A conditional `UPDATE` matches zero rows for the loser, so nothing is saved, and the loser gets `409
   QUESTION_NOT_CURRENT`. No locks needed.
10. A slow or failing call would hold the transaction and its locks for up to 30 s, and a failure could lose the
    already-valid answer. Short write, slow call, short write avoids both.

</details>

## 9. Go deeper / Still open

- Spec and plan: `docs/features/interviewer-reaction/spec.md`, `plan.md`.
- Next concept this unlocks: prompts as data and injection (`llm-interviewer/learnings.md`), then context management.

**Still open** (needs a real API key; was never filled in):

- Checkpoint G: prompt tokens on turn 1 vs the last turn; the same answer 5 times at temperature 0 vs 1; a very small
  `max_tokens` and its `finish_reason`; a wrong key / tiny timeout (what the user saw, what the log said); the token
  total and cost of one full interview. Later real-model numbers exist in `llm-interviewer/learnings.md` (section 7).
