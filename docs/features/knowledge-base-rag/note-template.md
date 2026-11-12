---
roles: backend
levels: mid, senior
source: user
---
# Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)

## Debugging a slow endpoint in production
Probe how they found the cause before changing anything: profiling, query plans, traces. Strong: measures first, fixes the biggest cost, and says how they checked the fix worked. Weak: guesses and adds a cache straight away. Follow-up: what changes if the slow part is a third-party call?

## Rolling out a risky change
Probe how they ship a change that could break users: feature flags, staged rollout, a rollback plan, what they watch afterwards. Strong: names a concrete signal that would make them roll back. Weak: "we tested it a lot". Follow-up: how do you roll back a database migration?
