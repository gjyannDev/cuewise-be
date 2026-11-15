# Implementation Plan: Agentic Workflow v2

## Overview
This plan adds two global skills (`debug`, `review-feature`) and edits `feature`, `create-plan` and `implement`. The goal is that each phase self-checks its dependencies, a step is done only when objective checks pass, failures get a bounded root-cause pass, and the feature ends with a traceable review. The three human gates stay unchanged.

## Architecture & Design
- **Thin wrappers over existing skills.** `debug` wraps `systematic-debugging`. `review-feature` orchestrates `code-review`, `security-review`, `llm-security` and `simplify`. Neither restates the method of the skill it wraps.
- **Contracts live in files.** Gate commands and checkpoint interval live in plan.md. Debug Log, Review and Health Check live in task.md. Phases share nothing else.
- **The health check is inline.** Each of the 5 workflow skills gets a 3-line first step plus its own Dependencies table, with no shared file that could itself go missing.
- **Two milestones** with a user checkpoint between them:
  - **Milestone A** covers reliability and recovery: health check, gated loop, debug, review-feature and the grilling fix.
  - **Milestone B** covers the techniques: problem confirmation, approaches considered, self-contained steps, checkpoints, ponytail and caveman.

## Approaches Considered
| Approach | Trade-offs | Chosen? |
|---|---|---|
| A. Thin wrapper skills plus small edits to existing phases | Few new instructions, and reuses tested skills (superpowers `systematic-debugging`, built-in `code-review`). The cost is that 2 more skills need maintaining. | **Yes.** It's the leanest option that meets every AC (ponytail), and the spec required wrapping. |
| B. Install superpowers `brainstorming`, `writing-plans` and `executing-plans` into the phases | No authoring needed, but the phases would compete, it writes to git, puts code in plans, and drops the AC/EC IDs | No. Out of scope per the spec. |
| C. Fold debug and review into implement's SKILL.md | No new skills, but implement (already about 10 KB) grows a lot, `/debug` can't run on its own (EC7), and review stops being a separate human-run step | No |

## Spec Requirements -> Implementation
- Backup before editing global skills (decided at plan time) -> Step 1
- Gated loop, plan side (gate commands) and AC/EC coverage check -> Step 2
- debug skill -> Step 3
- review-feature skill -> Step 4
- Gated loop, implement side, debug handoff and optional verification -> Step 5
- Wiring: routing file and task template -> Step 6
- Health check in feature, and the grilling fix -> Step 7 (health check in the other skills: Steps 2–5)
- Milestone A dry run -> Step 8
- Problem confirmation -> Step 9
- Approaches considered, self-contained steps and the checkpoint field -> Step 10
- ponytail every step, caveman lite and batch checkpoints -> Step 11
- Final audit and learnings.md -> Step 12

## Implementation Steps
Paths are relative to `~/.claude/skills/` unless noted. "Grep" means `Select-String` in PowerShell. Every check lists its expected result.

### Step 0 (setup)
1. **Back up the originals.** Copy `feature/`, `create-plan/` and `implement/` to `~/.claude/skills-backup/2026-11-15/`.
   - Verify: `Test-Path` on each backed-up `SKILL.md` returns True, and `(Get-ChildItem -Recurse -File).Count` matches source vs backup for each folder.
   - Test: skip (file copy).

### Milestone A: reliability and recovery
2. **create-plan: gate commands, coverage check and health check.**
   - Files: `create-plan/SKILL.md`, `create-plan/references/plan-template.md`.
   - Changes:
     - Testing Strategy must list the project's gate commands, taken from its CLAUDE.md or rules.
     - A pre-delivery check: any AC/EC without a step blocks "ready", unless it's deferred with a reason (EC14).
     - A Dependencies table (required: `plan-template.md`, `capability-routing.md`; optional: `grilling`, `ponytail`, `find-skills`) and a health-check step 0 (EC21–EC23).
   - Verify:
     - Grep `Gate commands` in plan-template.md finds 1 match or more.
     - Grep `^## Dependencies` in create-plan/SKILL.md finds 1 match.
     - Grep `uncovered` in SKILL.md finds 1 match or more.
   - Test: skip (prose); behavior is checked in Step 8.
3. **Create `debug/SKILL.md`.**
   - Frontmatter: `name: debug`, plus a description naming both triggers (implement's attempt 2 fails, and the user runs `/debug`).
   - Sections:
     - Dependencies (required: `systematic-debugging`; optional: `verification-before-completion`) and health check.
     - Input contract (step ID, failing command, error excerpt, what was tried, step files).
     - Method: delegate to systematic-debugging, one hypothesis at a time, at most 3.
     - Regression test that fails without the fix.
     - Never weaken tests (EC4).
     - Outcomes `fixed`, `blocked` and `blocked: plan deviation` with their fields (EC2, EC3).
     - Debug Log entry on every invocation.
     - Standalone mode with no task.md, reporting in chat (EC7).
     - Optional verification evidence (EC17).
     - Must be generic, with no project names.
   - Verify:
     - The first line is `---`, and `name: debug` is present.
     - Grep finds `blocked: plan deviation`, `3 hypotheses`, `regression test` and `^## Dependencies` (each 1 match or more).
     - Grep `(?i)cuewise` finds 0 matches.
   - Test: skip (prose); checked in Step 8.
4. **Create `review-feature/SKILL.md`.**
   - Frontmatter: `name: review-feature`, plus a description saying the user runs it after implement and that it never commits.
   - Sections:
     - Dependencies (required: `code-review`; optional: `security-review`, `llm-security`, `simplify`, `verification-before-completion`) and health check.
     - Inputs: the diff against the main branch, plus spec, plan and task. With no diff it stops (EC9). With missing docs it reviews the diff only (EC10).
     - Automated checks: the plan's gate commands plus the type checker, security scan, dependency audit and migration round-trip where they apply. A check that can't run is recorded as `not run: <reason>`, and nothing is installed without asking (EC8).
     - Reflection pass, with duplicate findings merged (EC11).
     - Project-rules checklist.
     - AC/EC traceability.
     - The Review section format in task.md (ID, severity, source, file:line, status) and the Health Check line.
     - Fix only the findings the user selects, then re-run the gates. A fix that breaks a gate is reverted and its finding reopened (EC12).
     - Re-runs append new IDs and keep existing statuses (EC13).
     - No commits.
   - Verify:
     - Frontmatter is valid.
     - Grep finds `not run:`, `blocker`, `should-fix`, `nit`, `never commit` and `^## Dependencies` (each 1 match or more).
     - Grep `(?i)cuewise` finds 0 matches.
   - Test: skip; checked in Step 8.
5. **implement/SKILL.md: gated loop, debug handoff and health check.**
   - Changes:
     - Step 0: health check, plus a Dependencies table (required: `test`, `task-template.md`, `capability-routing.md`, `learnings-template.md`; optional: `debug`, `tdd`, `ponytail`, `caveman`, `verification-before-completion`, `code-review`, `simplify`, `security-review`).
     - "Step done" means the step's tests plus the gate commands pass. If plan.md has no gate commands, use CLAUDE.md, and record `gate: none found` if neither has any (EC6). A gate failure counts as an attempt, and a Baseline Failure doesn't (EC5).
     - Replace "Attempt 2 fails -> STOP" with "invoke debug", and handle each of the three outcomes (EC1–EC3).
     - Optional verification evidence (AC16).
     - Rewrite the matching Notes bullets ("Test retry limit", "Early exit") so the rest of the file doesn't contradict the new rule.
   - Verify:
     - Grep `invoke.*debug` finds 1 match or more.
     - Grep `STOP immediately` finds 0 matches.
     - Grep `gate: none found` finds 1 match.
     - Grep `^## Dependencies` finds 1 match.
   - Test: skip; checked in Step 8.
6. **implement references: routing file and task template.**
   - Files: `implement/references/capability-routing.md`, `implement/references/task-template.md`.
   - Changes:
     - Routing: remove `review-implementation`, add `debug` (automatic, on the second failed attempt) and `review-feature` (the user runs it after finalize), and swap `grill-me` for `grilling` in Clarification.
     - Template: a `Health Check:` line under Status, a `## Debug Log` section, and a `## Review` section (a finding table plus check results, including `not run` rows). Add matching Validation Checklist items.
   - Verify:
     - Grep `review-implementation` finds 0 matches.
     - Grep `grill-me` finds 0 matches.
     - Grep `review-feature` and `debug` each find 1 match or more.
     - Grep `^## Debug Log`, `^## Review` and `Health Check:` in task-template.md each find 1 match.
   - Test: skip.
7. **feature: health check and the grilling fix (also covers the grilling fix in create-plan).**
   - Files: `feature/SKILL.md`, `create-plan/SKILL.md`, `create-plan/references/capability-routing.md`, `create-plan/references/plan-template.md` (the Skills Consulted row).
   - Changes:
     - feature gets a Dependencies table (required: `references/spec-template.md`; optional: `grilling`, `ponytail`, `find-skills`) and a health-check step 0.
     - Every `grill-me` reference becomes `grilling`, and the AskUserQuestion delivery rule stays. If `grilling` is missing, ask directly (EC18).
   - Verify:
     - Grep `grill-me` across `feature/`, `create-plan/` and `implement/` finds 0 matches.
     - Grep `AskUserQuestion` in feature/ and create-plan/ SKILL.md still finds 1 match or more each.
   - Test: skip.
8. **Milestone A check and dry run.**
   - Run every grep check from Steps 2–7, plus `(?i)cuewise` over all 5 skills, which must find 0 matches (AC11).
   - Start a **new session** so `debug` and `review-feature` appear in the available-skills list, and confirm both are listed (AC1, AC3).
   - Dry run:
     - On a small Cuewise feature the user picks, run `/implement` for at least one step with the gate commands (AC12).
     - Force one failing step to see the debug handoff.
     - Run `/review-feature` and confirm the Review section is written and no code changes before selection (AC12).
     - Hide an optional skill (rename its folder temporarily) to see the one-line warning, and rename a required reference file to see the phase stop (AC19). Restore both afterwards.
   - Record the results in task.md.
   - Test: after (real behavior).
   - **Checkpoint: the user decides whether to continue to Milestone B.**

### Milestone B: techniques
9. **feature: problem confirmation.**
   - File: `feature/SKILL.md`.
   - Changes: before the first grilling round, restate the problem (who has it, what hurts, what success looks like) and confirm it through AskUserQuestion. If the user corrects it, restate again (EC24). Propose no design.
   - Verify: grep `restate` finds 1 match or more.
   - Test: skip.
10. **create-plan: approaches, self-contained steps and the checkpoint field.**
    - Files: `create-plan/SKILL.md`, `create-plan/references/plan-template.md`.
    - Changes:
      - An `## Approaches Considered` section (2–3 approaches, trade-offs, the chosen one and why; one sentence if only one is viable; cite the spec when it settled the approach, EC25).
      - Every step names exact files and an exact verification command. A `skip` step names related tests or gates, and "none" isn't allowed (EC26). Still no code blocks.
      - A `Checkpoint interval:` field (large → 3 by default).
    - Verify: grep `Approaches Considered`, `Checkpoint interval` and `verification command` in both files each find 1 match or more.
    - Test: skip.
11. **implement: ponytail every step, caveman lite and checkpoints.**
    - Files: `implement/SKILL.md`, `implement/references/capability-routing.md`.
    - Changes:
      - ponytail runs before every step's code, with its two guardrails (EC16). Update the Tools table and the routing ponytail entry so ponytail is no longer conditional.
      - Replace the Chat Style section: caveman lite turned on at start, chat only, with the full-prose exceptions listed (failure, debug, security, irreversible actions, AI-concept and trade-off explanations). Switch back to normal mode at finalize and at any stop (EC20). The user's own caveman choice wins (EC19), and if caveman is missing, continue normally (EC15).
      - Checkpoints: pause at each interval with a full-prose summary. Use the size default when the plan doesn't set one, and skip a checkpoint that lands on finalize or a stop (EC27). Older plans continue with their gaps noted in task.md (EC28).
    - Verify: grep `caveman lite`, `normal mode`, `checkpoint` and `ponytail` in implement/SKILL.md each find 1 match or more.
    - Test: skip.
12. **Final audit and learnings.**
    - Re-run every grep check from Steps 2–11.
    - Check AC10 by hand: for each of EC1–EC28, write the skill file and the phrase that covers it into task.md.
    - Dry run B on a small feature: problem confirmation, Approaches Considered in the plan, and caveman lite in chat (AC20–AC23).
    - Write `docs/features/agentic-workflow/learnings.md`.
    - Test: after.

## Affected Files & Patterns
- New: `debug/SKILL.md`, `review-feature/SKILL.md`.
- Edited:
  - `feature/SKILL.md`
  - `create-plan/SKILL.md`, `create-plan/references/plan-template.md`, `create-plan/references/capability-routing.md`
  - `implement/SKILL.md`, `implement/references/capability-routing.md`, `implement/references/task-template.md`
- Backup: `~/.claude/skills-backup/2026-11-15/`.
- In this repo: only `docs/features/agentic-workflow/` (`task.md` and `learnings.md`, written by implement). No Cuewise source changes.
- Patterns to follow:
  - The existing skills' structure (frontmatter, numbered Workflow steps that end in **Done when:**, a Tools & Token Budget table, Notes).
  - The `AskUserQuestion` delivery rule already in feature and create-plan.
- Risks:
  - New skills may not appear until a new session (handled in Step 8).
  - Editing implement while it's executing this plan. Step 5 changes the rules implement itself follows, so the agent must keep following the version it loaded at start.
  - Long skill files dilute instructions. Keep each new section short, and don't restate wrapped skills.

## Testing Strategy
- **Framework:** no test runner applies, since these are prose skill files.
- **Gate commands** for this feature are the grep checks listed in each step. The full set is re-run in Steps 8 and 12.
- **Behavior** is verified by dry runs on real Cuewise features. The gate commands in those dry runs come from Cuewise's CLAUDE.md: `uv run pytest` (which includes `tests/test_layers.py`) and `uv run --with ruff ruff check .`.
- **Checkpoint interval:** at the milestone boundary (after Step 8), the user decides.
- **Coverage map:**

| Spec ID | Step | Test mode | Notes |
|---|---|---|---|
| AC1, AC2 | 3, 8 | skip / after | listed in a new session |
| AC3, AC4 | 4, 8 | skip / after | |
| AC5, AC6 | 5 | skip | dry run in Step 8 |
| AC7 | 2 | skip | |
| AC8, AC9 | 6 | skip | |
| AC10 | 12 | after | EC→phrase audit in task.md |
| AC11 | 8, 12 | skip | `(?i)cuewise` finds 0 matches |
| AC12 | 8 | after | real feature dry run |
| AC13 | 7 | skip | moved into Milestone A (see Trade-offs) |
| AC14, AC15 | 11 | skip | dry run in Step 12 |
| AC16 | 3, 5 | skip | |
| AC17 | 2, 3, 4, 5, 7 | skip | |
| AC18 | 4, 6 | skip | |
| AC19 | 8 | after | hide-skill / rename-file test |
| AC20 | 9, 12 | skip / after | |
| AC21, AC22 | 10, 12 | skip / after | |
| AC23 | 10, 11, 12 | skip / after | |
| EC1, EC2, EC3 | 3, 5 | skip | forced failure in Step 8 |
| EC4, EC7 | 3 | skip | |
| EC5, EC6 | 5 | skip | |
| EC8–EC13 | 4 | skip | EC8 and EC9 seen in the Step 8 dry run |
| EC14 | 2 | skip | |
| EC15, EC16, EC19, EC20 | 11 | skip | |
| EC17 | 3, 5 | skip | verification-before-completion not installed now, so it's the default path |
| EC18 | 7 | skip | |
| EC21, EC22, EC23 | 2, 3, 4, 5, 7 | skip / after | Step 8 hide/rename test |
| EC24 | 9 | skip | |
| EC25, EC26 | 10 | skip | |
| EC27, EC28 | 11 | skip | EC28: this plan predates the field |

- **Must verify, not assume:**
  - A new skill shows up in the available-skills list (it may need a new session).
  - Renaming a skill folder actually hides it.
  - `caveman` loads (the spec's open verification).
- **Open questions:** none. Every EC has an outcome.
- **Known baseline failures:** n/a. Cuewise's baseline for the dry runs is recorded when they start.

## Blockers & Resolutions
- `~/.claude/skills` isn't under git → dated backup copy (Step 1). Rollback is a copy back.
- `grill-me` can't be loaded by Claude (the problem this spec fixes) → this planning pass asked its questions directly through AskUserQuestion.
- Implement edits its own rules mid-run → it follows the loaded version, and the new rules are first exercised in Step 8.

## Trade-offs & Rationale
- **The grilling fix moved from Part B to Milestone A (Step 7).** The health check marks `grill-me` as missing (EC23), so without the fix every feature and create-plan run in Milestone A would warn.
- **Inline health check, not a shared file.** Each skill's Dependencies table is different anyway, and a shared file would be one more required dependency that could go missing.
- **Grep checks instead of a reusable script.** These are one-off structural checks (ponytail). A script would be one more file to maintain. Revisit if the workflow skills keep growing.
- **Checkpoint only at the milestone boundary for this plan.** Step 8 is a natural review point, and the large-plan default (every 3 steps) would split Milestone A unnaturally.
- **Most steps are `skip`, with behavior checked in dry runs.** Prose has no unit-test seam, and real runs are the only meaningful behavior signal.

## Project Rules Applied
- `cuewise-be/CLAUDE.md`:
  - No git writes, so the backup is a file copy, not a git repo.
  - Learning project, so the caveman exceptions cover explanations and learnings.md is written.
  - Lean-ctx and graphify are used for project work.
- `feature` three-file discipline: review findings go in task.md, not review.md.
- Global skills stay generic: no Cuewise strings (AC11, checked by grep).

## Skills Consulted
| Skill | Contribution |
|---|---|
| grill-me → asked directly | Could not be loaded (`disable-model-invocation: true`), so 4 decisions were asked through AskUserQuestion: milestones, backup, inline check, grep verification |
| ponytail (principles) | Thin wrappers, no check script, no shared file |
| lean-ctx / native Read | Read the current SKILL.md files, templates and routing files (outside the repo root, so native Read was used) |
| graphify | Not used, because no Cuewise code is affected |
| security-review | Not needed, because there's no auth, data or untrusted input. The no-commit and no-install rules are carried into review-feature. |

## Ready to Implement
- [x] All spec requirements mapped to steps
- [x] Every step has a Test tag, and every AC/EC is mapped
- [x] Affected files identified
- [x] Blockers resolved, and every edge case has an owner
- [x] Trade-offs documented
- [x] Deviation from spec: AC13 moved into Milestone A (see Trade-offs)
