---
roles: backend
levels: mid, senior
source: drafted
---
# Backend design and operations

## API design and versioning
Probe how they design an endpoint other teams depend on: resource naming, pagination, idempotency for retries, and how they change it without breaking old clients. Strong answers mention deprecation windows and contract tests.

## Data consistency and transactions
Ask about two writes that must both happen (charge and order). Probe transactions, isolation surprises, and what changes when a message queue or another service is involved. Strong answers mention retries with idempotency keys or an outbox.

## Caching and scaling reads
Probe when a cache helps and when it hurts: invalidation, stale data the business can accept, and a cache stampede. Strong answers measure first and name what they would watch after adding it.

## Observability and incidents
Ask about a production incident they handled: how they noticed, which logs, metrics or traces helped, how they mitigated before fixing, and what the follow-up changed. Strong answers describe a blameless review and a lasting fix.
