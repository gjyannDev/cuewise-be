# Feature: Agentic Workflow v2 (debug, review-feature, gated loop)

## Problem
The feature → create-plan → implement → test workflow runs each phase once, with no structured way to recover from failures and no structured review at the end:
- When a step fails twice, `implement` stops and hands debugging back to the user. Nothing does a disciplined root-cause search first.
- "Step done" depends on the step's own tests. Lint and architecture checks (for example the layer rule) aren't part of the gate, so violations only show up later, if at all.
- No check confirms that the plan covers every spec AC/EC before implementation starts.
- There's no end-of-feature review that combines correctness, security, simplification, project rules and spec traceability. `implement`'s routing points to a `review-implementation` skill that doesn't exist.
- `feature` and `create-plan` say to invoke `/grill-me`, but `grill-me` has `disable-model-invocation: true`, so Claude can't load it. The phases silently fall back to ad hoc question rounds.
- `ponytail` and `caveman` only run in implement when Claude judges they're needed or the user turns them on, so their effect varies from run to run.
- **Skills break without anyone noticing.** A skill that can't be loaded (`grill-me`), a reference to one that doesn't exist (`review-implementation`), or one missing from the session (`caveman`) produces no warning. The phase quietly falls back to something else, so the user doesn't know what actually ran.
- Plans don't record which approaches were considered, and their steps don't always name exact files and a verification command. Large plans run with no checkpoint between the plan gate and the final diff.

## Goal
Make the workflow more agentic using reflection (critique, then revise) and tool use (real verification signals). Keep the human gates on spec, plan and final diff.
- `implement` attempts a root-cause fix on its own before escalating to the user.
- A step counts as done only when objective checks pass.
- A gap in AC/EC coverage is caught at plan time, not at finalize.
- The user can run one command after implementation and get a ranked, traceable review without anything being changed or committed without approval.

## Project Conventions
- Rule sources consulted: `cuewise-be/CLAUDE.md`, `~/.claude/CLAUDE.md`, and the existing skills `feature`, `create-plan`, `implement`, `test`, `systematic-debugging` (from obra/superpowers), `grill-me`, `grilling`, `ponytail` and `caveman` in `~/.claude/skills/`.
  - The project is a **learning project** ("favor clarity and explaining the *why*", "teach as you build"). Terse chat must never replace an explanation.
- Constraints:
  - The skills are **global and generic**. They live in `~/.claude/skills/`, read each project's `CLAUDE.md` / `.claude/rules/*.md`, and must not hardcode Cuewise commands or paths. Cuewise is only the worked example.
  - **Three-file discipline** (spec.md → plan.md → task.md, plus `learnings.md` from implement). No new per-feature files. Review findings go in `task.md`.
  - **No git writes.** No skill commits, pushes, stages, amends or resets.
  - Never loosen, skip or delete a test to get a pass. This existing rule in `implement` and `test` also binds `debug`.
  - Project rules win over skill defaults.
  - Tooling: lean-ctx for exploration, edits and commands, plus graphify when `graphify-out/` exists.

## User Flow
1. The user runs `/feature`. Every phase starts with a skill health check. feature restates the problem, the user confirms it, the grilling runs, and the user approves `spec.md` (gate 1, unchanged).
2. The user runs `/create-plan`. The plan includes the approaches considered, steps that each name files and a verification command, the gate commands, an optional checkpoint interval, and an AC/EC coverage check. The user approves `plan.md` (gate 2, unchanged).
3. The user runs `/implement`. At each checkpoint (large plans: every 3 steps) it pauses for the user. For each step:
   1. The step is written and tested as it is today.
   2. The gate commands run. The step is done only when they all pass.
   3. If attempt 2 fails, `implement` calls `debug` instead of stopping.
   4. `debug` returns `fixed` (the step continues) or `blocked` (implement stops and reports to the user).
4. After implement finalizes, the user runs `/review-feature`. Findings are written to the Review section of `task.md`, ranked by severity.
5. The user picks the findings to fix. `review-feature` applies only those, then re-runs the gate commands.
6. The user reviews the final diff and commits manually (gate 3, unchanged).

## Requirements

### Functional

**Gated loop (implement + create-plan)**
- `create-plan` records the project's **gate commands** (for example tests, lint and architecture checks) in plan.md's Testing Strategy.
- `implement` runs the step's tests plus the gate commands. A step is complete only when all of them pass, or a failure matches a recorded Baseline Failure.
- If plan.md lists no gate commands, `implement` falls back to the commands in the project's `CLAUDE.md`, and records the fallback in task.md.
- The existing retry limit stays: 2 attempts per step, counted once the code exists. A gate-command failure counts as a failed attempt.

**Plan coverage check (create-plan)**
- Before delivering, `create-plan` checks that every spec AC and EC maps to at least one step and a test mode. It lists any that are uncovered and doesn't report the plan as ready until each one is covered or explicitly deferred with a reason.

**debug skill (new, global)**
- Invoked by `implement` when attempt 2 of a step fails. The user can also invoke it with `/debug`.
- Input: step ID, the failing command, a short error excerpt, what has been tried, and the step's files.
- It follows `systematic-debugging`'s method (reproduce, gather evidence, one hypothesis at a time, fix the root cause). It doesn't restate that method.
- It tests at most **3 hypotheses**, one at a time.
- On success it adds a regression test that fails without the fix and passes with it, and re-runs the step's tests and gate commands.
- It returns one of these outcomes:
  - `fixed`: root cause, change made, regression test, and gate result.
  - `blocked`: hypotheses tried, evidence, best current theory, and a question for the user.
  - `blocked: plan deviation`: the root cause is in the plan, or the fix needs files outside the step's scope.
- It writes a short Debug entry in task.md for every invocation, whatever the outcome.
- `implement` continues the step on `fixed`. On `blocked` it stops and reports, as it does today. On `blocked: plan deviation` it follows its existing plan-deviation step (update plan.md, log the deviation, wait for approval).

**review-feature skill (new, global)**
- Invoked manually by the user after `implement`. It isn't called automatically.
- Scope: the working-tree diff against the main branch, plus the feature's spec.md, plan.md and task.md.
- Automated checks: it runs the plan's gate commands and any extra project-appropriate checks it can find (type checker, static security scan, dependency audit, migration up/down/up round-trip). A check that can't run is recorded as `not run: <reason>`. Nothing is installed without asking.
- Reflection pass: it runs the existing `code-review` (correctness), `security-review` (plus `llm-security` when LLM code changed) and `simplify` (report only).
- Project checklist: it checks the diff against the rules in the project's `CLAUDE.md` / `.claude/rules/*.md`.
- Traceability: it confirms every spec AC/EC has a passing test or a recorded verification.
- Output: a **Review** section in task.md listing each finding with an ID, severity (`blocker`, `should-fix` or `nit`), source (which check), file:line, and status (`open`, `fixed` or `won't fix`).
- Fixes: it applies only the findings the user selects, re-runs the gate commands afterwards, and updates their status. It never commits.

**Grilling fix (feature + create-plan)**
- `feature` and `create-plan` invoke `grilling` (which Claude can invoke) wherever they now say `/grill-me`. The rule to deliver every round through `AskUserQuestion` stays as it is.
- `implement`'s `capability-routing.md` gets the same change in its Clarification entry.

**ponytail on every implement step**
- `implement` applies `ponytail` before writing each step's code, not just when a step "looks like it's growing". The goal is the smallest code that passes the step's tests and gate commands.
- Guardrails written into implement:
  - **ponytail decides how little code, not what gets built.** It can't drop or weaken an AC, EC or plan step. If a step looks unnecessary, that's raised as a plan deviation (implement step 4).
  - **It never simplifies away** validation, security, error handling or tests.
- The YAGNI question ("does this need to exist at all?") stays with `feature` and `create-plan`, which already use ponytail for scope.

**caveman lite during implement**
- `implement` turns on `caveman` at the **lite** level when it starts, for **chat only** (step status, test summaries).
- Full prose is always used for: retry-limit failure reports, `debug` reports, security findings, irreversible actions, and any explanation of an AI concept or design trade-off.
- Files are never written in caveman: task.md, plan.md, learnings.md, code, comments and commit message suggestions.
- When implement finalizes or stops at a gate, it switches back to normal mode, so `review-feature` and later discussion aren't terse.

**Verification evidence (optional superpowers skill)**
- If `verification-before-completion` (from obra/superpowers) is installed, `implement` and `debug` follow it before claiming a step is done or a bug is fixed: show the command and its result, never "should pass".
- If it isn't installed, the gate-command rule already gives the same guarantee, and nothing fails.

**Skill health check (all workflow skills)**
- At the start of each phase (`feature`, `create-plan`, `implement`, `debug`, `review-feature`), the skill checks every skill and reference file it depends on before doing any work.
- Each workflow skill lists its dependencies in a short **Dependencies** section, each marked **required** or **optional** with its fallback. For example, implement requires `test`. debug requires `systematic-debugging`. review-feature requires `code-review`. ponytail, caveman, grilling and `verification-before-completion` are optional.
- A skill passes the check when it appears in the session's available-skills list (so it can be loaded) and every reference file the phase uses (templates, routing tables) exists.
- The check is cheap: it compares names against the available-skills list Claude already has and checks file paths exist. It doesn't read skill bodies.
- Result:
  - **All present:** nothing is reported.
  - **An optional skill is missing:** one line in chat ("missing: X → fallback: Y"), then the phase continues with the fallback.
  - **A required skill or reference file is missing:** the phase stops before doing any work and reports what's missing and how to fix it.
- implement and review-feature also write the result in task.md (a **Health Check** line under Status), so a run can be audited later.

**Problem confirmation (feature)**, borrowed from superpowers `brainstorming`
- Before the first grilling round, `feature` restates the problem in one or two sentences (who has it, what hurts, what success looks like) and asks the user to confirm or correct it through `AskUserQuestion`. Grilling starts only after it's confirmed.
- No design or approaches are proposed in feature. That stays in create-plan.

**Approaches considered (create-plan)**, borrowed from superpowers `brainstorming`
- For medium/large plans, `create-plan` lists 2–3 viable approaches with their trade-offs, the one chosen, and why (citing project rules or ponytail where they decided it). These go in a new **Approaches Considered** section of plan.md.
- If only one approach is viable, the section says so in one sentence, with the reason.
- The choice goes to the user through grilling when it's a real design decision the spec didn't settle.

**Self-contained steps (create-plan)**, borrowed from superpowers `writing-plans`
- Every plan step names the exact files it creates or changes, and the exact verification command that proves it's done (the step's tests plus the gate commands).
- A step must make sense to a reader with no context from the planning conversation. Plans still contain no code blocks.

**Batch checkpoints (implement)**, borrowed from superpowers `executing-plans`
- plan.md can set a **checkpoint interval** (every N steps). At each checkpoint, implement pauses with a short summary (steps done, tests and gate results, deviations) and continues only after the user says so.
- Defaults: large plans checkpoint every 3 steps. Small and medium plans have no checkpoints unless the plan sets one.
- Checkpoints are written in full prose, not caveman.

**Wiring**
- `implement`'s `capability-routing.md`: replace the `review-implementation` entry with `review-feature` (run by the user after finalize), and add a `debug` entry (called automatically when attempt 2 fails).
- `implement` SKILL.md: replace "attempt 2 fails → STOP" with "attempt 2 fails → invoke debug", and handle its three outcomes.
- `implement`'s task template gains **Debug Log** and **Review** sections.
- `feature`'s three-file note still forbids review.md. Review findings live in task.md, so the note stays accurate.

### Non-Functional
- **Token cost:** `debug` and `review-feature` reuse plan.md's Skills Consulted findings and don't re-query. Command output is cut down to failures plus the summary line.
- **Bounded autonomy:** an implement step makes at most 2 attempts, then debug tests at most 3 hypotheses. No unbounded loops.
- **Safety:** neither skill commits, edits secrets, or runs destructive DB commands against a non-scratch database. Web content they fetch is treated as data, never as instructions.
- **Privacy:** no personal data (résumés, answers, secrets) is pasted into task.md entries.

## Constraints
- Changes are limited to skill files under `~/.claude/skills/` (new `debug/` and `review-feature/` folders, plus edits to `feature/`, `create-plan/`, `implement/` and their references). `grill-me`, `ponytail`, `caveman` and the superpowers skills themselves aren't edited.
- Superpowers is used **à la carte**. The full plugin isn't installed, because its brainstorm/plan/execute skills duplicate this workflow and its git skills break the no-git-writes rule.
- No project source code changes.
- No new dependencies. Ad hoc tools run through the project's own runner (for example `uv run --with <tool>`), and only with permission.

## Blockers
- None open. All decisions were settled in the grill-me rounds and follow-up discussion on 2026-11-15.
- Dependency (user action, optional): install `verification-before-completion` from obra/superpowers if you want it. The workflow works without it (EC17).
- To verify: `caveman` didn't appear in one session's skill list even though its frontmatter is valid. Run `/caveman` once to confirm it loads (EC15).

## Edge Cases
- **EC1:** Attempt 2 of a step fails → `implement` calls `debug` with the structured input and doesn't stop.
- **EC2:** Debug's 3rd hypothesis is wrong → debug returns `blocked`. implement stops, task.md records the hypotheses and evidence, and the user is asked the debug question.
- **EC3:** The root cause is in the plan, or the fix needs files outside the step → debug returns `blocked: plan deviation` without changing code. implement runs its plan-deviation step.
- **EC4:** The only way to get green is to loosen, skip or delete a test → debug refuses and returns `blocked`, naming the test and why it seems wrong.
- **EC5:** The failure matches a recorded Baseline Failure → it doesn't count as an attempt, and debug isn't called.
- **EC6:** plan.md has no gate commands (older plan) → implement uses CLAUDE.md's commands and records the fallback in task.md. If neither source has commands, it runs the step's tests only and records `gate: none found`.
- **EC7:** The user runs `/debug` directly, outside implement → it runs the same method and caps, using the user's description as input. With no feature context it writes no task.md entry and reports in chat.
- **EC8:** A review check's tool is unavailable (no type checker, no scratch DB, a non-Python project) → that check is recorded as `not run: <reason>` and the review continues. Nothing is installed without asking.
- **EC9:** `/review-feature` runs with no diff against main → it reports "nothing to review" and writes no Review section.
- **EC10:** `/review-feature` runs with no task.md or spec.md for the feature → it reviews the diff only, skips traceability, and states which inputs were missing.
- **EC11:** Two reviewers report the same issue → it's recorded once, with both sources.
- **EC12:** A selected fix makes a gate command fail → the fix is reverted, its finding is marked `open` with a note, and the user is told.
- **EC13:** `review-feature` runs a second time on the same feature → new findings are appended with new IDs. Existing IDs keep their status. Findings that no longer reproduce are marked `fixed`.
- **EC14:** A plan AC/EC has no step → create-plan lists it as uncovered and doesn't report the plan as ready until it's mapped or deferred with a reason.
- **EC15:** `caveman` can't be loaded in the session → implement continues in normal chat, mentions it once, and doesn't fail.
- **EC16:** ponytail's leanest version would drop or weaken an AC, EC or plan step, or remove validation, security, error handling or a test → that version is rejected. If the step really looks unnecessary, it's raised as a plan deviation and nothing is cut.
- **EC17:** `verification-before-completion` isn't installed → implement and debug rely on the gate-command rule only. No error and no install prompt.
- **EC18:** `grilling` can't be loaded → feature and create-plan run the question rounds directly through `AskUserQuestion` (today's behavior) and mention it once.
- **EC19:** The user has explicitly picked another caveman level (or turned caveman off) in the session → the user's choice wins over implement's lite default.
- **EC20:** implement stops early (retry limit, `blocked`, or a plan deviation) → it still switches back to normal mode before the stop report, so the report is in full prose.
- **EC21:** A required skill or reference file is missing at phase start → the phase stops before doing any work, names the missing item, and says how to fix it (install it, or restore the file).
- **EC22:** An optional skill is missing at phase start → one line in chat ("missing: X → fallback: Y"), then the phase continues with the fallback. In implement and review-feature it's also recorded in task.md's Health Check line.
- **EC23:** A skill exists on disk but isn't in the available-skills list (for example `disable-model-invocation: true`, as with `grill-me`) → it counts as missing and gets the same required/optional handling.
- **EC24:** The user corrects the problem restatement in feature → feature restates it again with the correction and asks again. Grilling starts only after a confirmation.
- **EC25:** A spec already settles the approach → create-plan's Approaches Considered names that approach, cites the spec, and doesn't re-ask.
- **EC26:** A plan step can't name an exact verification command (for example config or copy with `Test: skip`) → the step names the existing related tests or the gate commands it must still pass. "None" isn't allowed.
- **EC27:** A checkpoint falls on the last step, or right after a `blocked` stop → there's no separate checkpoint. The finalize or stop report replaces it.
- **EC28:** An older plan.md has no checkpoint interval, Approaches Considered section or file/command per step → implement uses the size-based checkpoint default and works with what the plan has. It notes the missing parts in task.md and doesn't stop.

## Acceptance Criteria
- [ ] **AC1:** `~/.claude/skills/debug/SKILL.md` exists with valid frontmatter (name, and a description that says when implement calls it and when to use `/debug`), and is listed as an available skill.
- [ ] **AC2:** The debug skill documents the structured input, the 3-hypothesis cap, the regression-test requirement, the never-weaken-tests rule, and the three outcomes (`fixed`, `blocked`, `blocked: plan deviation`) with the fields each one returns.
- [ ] **AC3:** `~/.claude/skills/review-feature/SKILL.md` exists with valid frontmatter, and is listed as an available skill.
- [ ] **AC4:** The review-feature skill documents the scope, automated checks with the `not run: <reason>` rule, the reflection pass (code-review, security-review, llm-security when LLM code changed, simplify), the project checklist, AC/EC traceability, the task.md Review section format (ID, severity, source, file:line, status), and fix-only-on-selection with no commits.
- [ ] **AC5:** implement's SKILL.md calls debug when attempt 2 fails, and defines what implement does for each of the three outcomes.
- [ ] **AC6:** implement's SKILL.md defines "step done" as the step's tests plus the gate commands passing, with the CLAUDE.md fallback and the `gate: none found` case.
- [ ] **AC7:** create-plan's SKILL.md and plan template require gate commands in Testing Strategy and an AC/EC coverage check before delivery.
- [ ] **AC8:** implement's `capability-routing.md` has no `review-implementation` entry, and has entries for `debug` and `review-feature`.
- [ ] **AC9:** implement's `task-template.md` has a Debug Log section and a Review section (the finding table plus a check-results list including `not run` rows).
- [ ] **AC10:** Every edge case EC1–EC28 is covered by an explicit instruction in the skill that owns it.
- [ ] **AC11:** No skill text hardcodes Cuewise-specific commands, paths or rules. Cuewise appears only as an example, if at all.
- [ ] **AC12:** A dry run on one small Cuewise feature shows the gate commands running, and `/review-feature` writing a Review section to task.md without changing code until the user selects fixes. The results are recorded in this feature's learnings.md.
- [ ] **AC13:** `feature`, `create-plan` and implement's `capability-routing.md` reference `grilling` instead of `grill-me`, and keep the `AskUserQuestion` delivery rule.
- [ ] **AC14:** implement's SKILL.md applies ponytail before every step's code, with both guardrails (it can't cut scope, and never removes validation, security, error handling or tests). Its Tools table and `capability-routing.md` no longer describe ponytail as conditional.
- [ ] **AC15:** implement's SKILL.md turns on caveman lite at start for chat only, lists the full-prose exceptions (failure, debug, security, irreversible actions, AI-concept and trade-off explanations), keeps files in normal prose, and switches back to normal mode at finalize or at any stop.
- [ ] **AC16:** implement's and debug's SKILL.md reference `verification-before-completion` as optional, and work unchanged when it's absent.
- [ ] **AC17:** `feature`, `create-plan`, `implement`, `debug` and `review-feature` each have a Dependencies section (each entry marked required or optional, with its fallback), and a first workflow step that runs the health check with the stop/warn/silent outcomes.
- [ ] **AC18:** implement's `task-template.md` has a Health Check line under Status, and review-feature writes the same line.
- [ ] **AC19:** A dry run with an optional skill hidden shows the one-line warning and the fallback. A dry run with a required reference file renamed shows the phase stopping before it does any work.
- [ ] **AC20:** feature's SKILL.md requires a confirmed problem restatement before the first grilling round, and proposes no design.
- [ ] **AC21:** create-plan's SKILL.md and plan template have an Approaches Considered section (2–3 approaches with trade-offs, the one chosen and why, or a one-sentence single-approach reason).
- [ ] **AC22:** create-plan's SKILL.md and plan template require every step to name exact files and an exact verification command, with no code blocks.
- [ ] **AC23:** create-plan's plan template has a checkpoint interval field. implement's SKILL.md pauses at each checkpoint with a full-prose summary, applies the size-based default (large → every 3 steps) when the plan doesn't set one, and skips a checkpoint that coincides with finalize or a stop.

## Out of Scope
- **Stage 2–3 patterns:** critic pass and grilling before approvals, routing (bug vs feature vs tiny), lessons-learned capture, re-planning beyond the existing deviation step. Deferred so the effect of this change can be measured on its own.
- **Workflow metrics in task.md** (retries, leaked findings, plan corrections). Next spec, once there's a baseline.
- **Hooks and guardrails** and permission tiers in `settings.json`. Separate config work.
- **New tool integrations** (browser automation, schemathesis, the Artifact dashboard). Added per phase later.
- **Parallel subagents, orchestrator-workers, voting.** They add cost the project doesn't need yet.
- **Auto-running review-feature** at the end of implement. The user runs it manually, which keeps the final gate human.
- **The full superpowers plugin**, and its `brainstorming`, `writing-plans`, `executing-plans`, `test-driven-development`, `using-git-worktrees` and `finishing-a-development-branch` skills. They duplicate this workflow or write to git. Their best techniques (problem confirmation, approaches considered, self-contained steps, batch checkpoints) are adopted into the existing skills instead.
- **A health check for skills outside the workflow** (for example a global audit of every skill in `~/.claude/skills/`). This spec only checks what each phase depends on.
- **`receiving-code-review` / `requesting-code-review`** in review-feature. A possible later fit, once review-feature has been run on a few features.
- **ponytail or caveman in other phases.** feature and create-plan already use ponytail for scope, and caveman stays out of spec and plan discussions, where clarity matters most.
- **Editing `grill-me`** (removing its `disable-model-invocation` flag). Pointing to `grilling` fixes the problem without changing a third-party skill.
