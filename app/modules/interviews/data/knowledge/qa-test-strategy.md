---
roles: qa
levels: mid, senior
source: drafted
---
# Test strategy and quality leadership

## Risk-based test planning
Probe how they plan testing for a release with too little time: which features and changes carry the most risk, and what they test first. Strong: ranks by user impact and likelihood of breaking, states what is left untested and tells the team. Weak: tries to test everything equally and runs out of time. Follow-up: how do you explain the risk you accepted to a product manager?

## What to automate and the test pyramid
Probe how they decide between unit, API and end-to-end tests, and between automated and manual. Strong: automates stable, repeated, high-value checks at the lowest level that catches the bug, and keeps exploratory testing manual. Weak: automates every UI click and ends with slow, flaky tests. Follow-up: what do you do about a flaky end-to-end test?

## Quality gates in CI and releases
Probe which checks must pass before code merges or ships: tests, coverage of critical paths, a smoke test after deploy. Strong: keeps gates fast and meaningful, and defines what blocks a release versus what is logged. Weak: a gate everyone bypasses. Follow-up: who can override a failing gate, and when?

## Quality metrics that matter
Probe how they show quality is improving or slipping: escaped defects, defect age, test stability, time to detect. Strong: picks a few metrics tied to user impact and acts on trends. Weak: reports test counts or pass rates alone. Follow-up: how would you stop a metric from being gamed?

## Leading a release sign-off
Probe how they decide a release is ready and handle a late, serious bug. Strong: weighs severity and reach, offers options (fix, flag off, ship with a known issue) and records the decision. Weak: says yes under pressure or blocks without options. Follow-up: how do you keep developers on side when you block a release?
