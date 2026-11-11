---
roles: fullstack
levels: intern, junior
source: drafted
---
# Full-stack fundamentals

## A feature from form to database
Ask them to walk a small feature end to end: the form, validation on both sides, the API call, the table it writes to, and the error the user sees. Strong answers validate on the server even when the client already does.

## Sessions and authentication basics
Probe how a logged-in user stays logged in: cookies versus tokens, what is stored where, and what happens on logout. Strong answers know a secret must never live in front-end code.

## Reading a stack trace
Give an error that appears in the browser but starts on the server. Strong answers check the network tab, then the server log for the same request, before changing code.
