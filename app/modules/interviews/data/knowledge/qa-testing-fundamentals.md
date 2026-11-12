---
roles: qa
levels: intern, junior
source: posting
---
# Quality assurance basics

## Writing a reproducible bug report
Probe the last bug they reported, or would report: steps, expected versus actual result, environment and evidence. Strong: someone else can reproduce it from the text alone, with logs, a screenshot or a recording, and a stated severity. Weak: "it doesn't work" with no steps. Follow-up: what do you do when you can only reproduce it sometimes?

## Test case design techniques
Probe with a field that accepts ages 18 to 60: which inputs would they test? Strong: boundary values (17, 18, 60, 61) and equivalence groups, plus empty and non-numeric input, and says why each was picked. Weak: tries a few random values. Follow-up: how would you keep the cases reusable for the next release?

## Verifying an API and the data behind a screen
Probe how they check a screen is correct beyond what it shows: inspect the request and response with a tool like Postman, status codes, payload fields, and whether the data matches in other systems. Strong: compares expected and actual per field and spots a mismatch between the app and the back office. Weak: only looks at the UI. Follow-up: the response is correct but the screen is wrong; what next?

## Regression and cross-platform testing
Probe a small change that ships: which flows do they retest, and on which devices, OS versions, screen sizes and browsers? Strong: chooses by risk and by what the change touches, keeps a regression checklist, and names what they would automate later. Weak: retests everything, or nothing. Follow-up: how do you decide you have tested enough?

## Raising edge cases before code exists
Probe how they take part in planning and refinement: unclear acceptance criteria, unusual inputs, failure and empty states. Strong: gives a real edge case they found by asking early and what it saved. Weak: waits for the build to find problems. Follow-up: how do you handle a developer who says it is out of scope?
