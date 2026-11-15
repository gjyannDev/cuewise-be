# Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)

**Concepts:** prompt chaining with human gates, verification-gated loops, evaluator-optimizer (reflection), delegation to a specialist skill, dependency health checks, and human checkpoints. **Status:** Milestones A and B built and structurally checked on 2026-11-15 (43/43 checks, all 28 edge cases mapped). Dry runs **pending**.

## 1. Why it exists
The feature → create-plan → implement workflow was a fixed chain with no feedback inside it:
- A step that failed twice simply stopped.
- "Done" meant only the step's own tests had passed.
- No end-of-feature review existed.
- Skills broke without anyone noticing. In one session we found three: `grill-me` couldn't be loaded by Claude (`disable-model-invocation: true`), the routing file pointed to a `review-implementation` skill that didn't exist, and `caveman` was missing from the skills list. None of them produced a warning.

## 2. What it is
Three agentic patterns were added to the chain, and none of the human gates were removed:
```
/feature ─[you]─> /create-plan ─[you]─> /implement ⇄ /debug ──> /review-feature ─[you]─> commit
   health check     gates + coverage      gated loop   ≤3 hypotheses   reflection pass
```
- **Tool use as a verifier:** gate commands (tests, lint, layer check) decide whether a step is done.
- **Delegation:** after the second failed attempt, a specialist skill (`debug`) takes over, with a hard cap.
- **Reflection:** `review-feature` runs several critics over the finished diff, and you pick what gets fixed.

Milestone B adds four techniques borrowed from superpowers, without installing its phase skills:
- **feature** restates the problem and waits for your confirmation before grilling (from `brainstorming`).
- **create-plan** records 2–3 Approaches Considered (from `brainstorming`), and makes every step name its files and verification command (from `writing-plans`).
- **implement** pauses at checkpoints, every 3 steps for large plans (from `executing-plans`).

implement also runs ponytail before every step, which can't cut scope, and caveman lite in chat, with full prose wherever clarity matters.

## 3. When to use it
| Do this | When | Why / limit |
|---|---|---|
| Gate commands per step | Any project with tests or lint in its CLAUDE.md | An objective pass/fail beats the agent's own judgment of "done" |
| `/debug` | Automatically on the second failure, or by hand for any bug | At most 3 hypotheses, so it can't loop forever |
| `/review-feature` | After implement finalizes | It runs only when you ask. Fixes need your selection. It never commits. |
| Health check | Start of every phase | It costs almost nothing: names are compared against the skills list, without reading any skill files |

**I'd revisit this when** the dry runs show debug returning `blocked` most of the time (the cap is too low, or the input is too thin), or review-feature's findings are mostly nits (the reviewers are too noisy).

## 4. How it works
Options considered (from plan.md):

| Option | Result |
|---|---|
| Thin wrapper skills over existing ones | **Chosen.** Reuses the tested `systematic-debugging` and `code-review` |
| Install superpowers' phase skills | Rejected: competing phases, git writes, code in plans |
| Fold debug and review into implement | Rejected: bloats implement, and `/debug` couldn't run on its own |

Walk-through of a failing step (paths under `~/.claude/skills/`):
1. `implement/SKILL.md:27`: the health check runs first, so a missing required dependency stops the run before any work.
2. `implement/SKILL.md:53`: after the step's tests, the gate commands run (from plan.md, falling back to CLAUDE.md or `gate: none found`).
3. `implement/SKILL.md:58`: attempt 2 fails, so implement invokes `/debug` with the step ID, the files, the failing command, the error excerpt and what was tried.
4. `debug/SKILL.md:35`: one hypothesis at a time, at most 3.
5. `debug/SKILL.md:38`: if the cause is in the plan, debug returns `blocked: plan deviation` without changing code.
6. Implement acts on the outcome. Later, `review-feature/SKILL.md:57` fixes only the findings you select.

Plan side: `create-plan/SKILL.md:52` requires gate commands, and `:57` blocks "ready" while any AC/EC is uncovered.

## 5. What can go wrong
| Failure | What the user sees | What the skill does | Proof |
|---|---|---|---|
| A required skill or file is missing | Phase stops immediately with the fix | Health check, step 0 | **pending** (Step 8 rename test) |
| An optional skill is missing | One `missing: X -> fallback: Y` line | Continues with the fallback | **pending** (Step 8) |
| The only way to green is changing a test | `blocked`, naming the test | debug refuses to weaken tests | grep check (instruction present). Behavior **pending**. |
| A review fix breaks a gate | Finding reopened, with a note | The fix is reverted | instruction present. Behavior **pending**. |

## 6. Try it yourself
1. Predict: if you rename `~/.claude/skills/ponytail` and run `/implement`, what is the first thing you see? Then run it.
2. Predict: does `/review-feature` on a clean branch write anything to task.md? Run it and compare (EC9 says no).
3. Write a test that fails on purpose and run `/implement`. Predict how many fix attempts happen before `/debug` takes over.

## 7. What surprised me
- `debug` and `review-feature` showed up in the available-skills list right after their files were written. The plan had assumed a new session would be needed.
- The very planning pass that wrote this plan hit the bug it fixes: `grill-me` couldn't be loaded, so the questions were asked directly.
- Structural checks: 32/32 at Milestone A, then 43/43 after Milestone B (Select-String, 2026-11-15).
- The first EC audit flagged two edge cases as missing, but the bug was in the audit, not the skills. PowerShell variable names ignore case, so a loop variable `$f` silently overwrote `$F`. It's a good reminder that a verification tool can be wrong too: check a surprising failure before "fixing" the thing under test, which is the same rule debug follows.
- Dry-run behavior: **pending**.

## 8. Check your understanding
1. Why is the gate a list of commands rather than "the agent decides it's done"?
2. When should debug *not* fix a bug it has found?
3. How does the health check tell that `grill-me` is missing when its folder exists?
4. What if the cap were removed and debug kept trying until green?

<details>
<summary>Reference answers (write yours first)</summary>

1. A command gives an objective, repeatable signal. The agent's own judgment is the very thing that tends to over-claim "done".
2. When the root cause is in the plan or outside the step's files. Then it returns `blocked: plan deviation`, because changing the design is a human decision.
3. It checks the session's available-skills list, not the disk. A skill with `disable-model-invocation: true` isn't listed, so it counts as missing.
4. Unbounded loops burn tokens and are tempted to "fix" the test instead of the code. The cap forces escalation to a human with evidence.

</details>

## 9. Go deeper / Still open
- Spec: `docs/features/agentic-workflow/spec.md`. Plan: `docs/features/agentic-workflow/plan.md`.
- **Pending:** Milestone A dry run (AC12, AC19, EC1) and Milestone B dry run (AC20–AC23). The steps are in task.md under Current Step.
- Next spec candidates: workflow metrics in task.md, hooks as guardrails, routing for bug fixes vs features.
