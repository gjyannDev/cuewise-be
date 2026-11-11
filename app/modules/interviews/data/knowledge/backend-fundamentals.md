---
roles: backend
levels: intern, junior
source: drafted
---
# Backend fundamentals

## HTTP and REST basics
Probe what happens between a request and a response: methods, status codes, headers, and when a 400, 401, 404 or 500 is right. Strong answers connect codes to what the client can do next. Weak answers return 200 with an error message inside.

## SQL and data modelling
Ask them to model a small domain (orders and customers) and query it. Probe joins, a missing index on a slow query, and why a foreign key helps. Strong answers explain one-to-many in plain words and spot the N+1 query problem.

## Debugging a failing request
Give a request that works locally but fails in staging. Strong answers read logs and the exact error first, reproduce it, then change one thing at a time. Weak answers guess and rewrite code.
