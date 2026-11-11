---
roles: frontend
levels: mid, senior
source: drafted
---
# Frontend architecture

## State management at scale
Probe how they split server state (fetched data and its cache) from client state, and how they keep many screens consistent. Strong answers name the trade-offs of a global store versus a query cache and when each goes wrong.

## Performance and Core Web Vitals
Ask how they would find and fix a slow page: what they measure first, bundle size, rendering work, images and hydration. Strong answers start from a real metric and a profile, not from a list of tricks.

## Testing user interfaces
Probe what they cover with component tests, what with end-to-end tests, and how they keep tests from breaking on every markup change. Strong answers test behaviour the user sees and keep end-to-end tests few.
