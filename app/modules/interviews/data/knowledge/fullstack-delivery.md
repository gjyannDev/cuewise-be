---
roles: fullstack
levels: mid, senior
source: drafted
---
# Full-stack delivery

## API contracts between client and server
Probe how they keep client and server in step: shared types or a schema, versioning, and rolling out a breaking change when old app versions still call the API. Strong answers release the server change first and remove old fields later.

## End-to-end feature ownership
Ask about a feature they owned across the stack: where they spent the most time, what they would split differently, and how they tested the whole path. Strong answers mention feature flags or a gradual rollout.

## Security across the stack
Probe authorization (who may see this record) as well as authentication, input handling against injection, and cross-site scripting in rendered content. Strong answers check ownership on the server for every request.
