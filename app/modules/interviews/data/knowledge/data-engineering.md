---
roles: data
levels: mid, senior
source: drafted
---
# Data engineering

## Pipelines and orchestration
Probe a pipeline they built or ran: scheduling, retries, backfills, and what happens when an upstream source arrives late. Strong answers make each step idempotent so a rerun is safe.

## Data quality and contracts
Ask how bad data was caught before it reached a dashboard: tests on the data, schema changes from producers, and alerting. Strong answers name a contract with the team that produces the data.

## Modelling for analytics
Probe how they shape raw tables for analysts: facts and dimensions, slowly changing attributes, and partitioning for cost. Strong answers trade query speed against freshness on purpose.
