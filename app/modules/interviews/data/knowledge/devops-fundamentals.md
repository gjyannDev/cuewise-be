---
roles: devops
levels: intern, junior
source: drafted
---
# DevOps fundamentals

## Linux and shell basics
Probe how comfortable they are on a server: navigating files, permissions, processes, disk space, and a small shell script. Strong: explains how they would find what is using the disk or a port, and checks before deleting anything. Weak: copies commands without knowing what they do. Follow-up: a script works on your machine but not on the server; what do you check?

## Git and a first CI pipeline
Probe how a change moves from a branch to a merged commit, and what a simple pipeline runs on it: install, test, build. Strong: describes a pull request, a failing check and how they fixed it. Weak: pushes straight to main. Follow-up: what should happen when the pipeline fails on main?

## Containers with Docker
Probe what an image and a container are, and how they would containerise a small app. Strong: explains layers, keeping images small, and passing configuration through environment variables, not baking secrets in. Weak: treats a container like a virtual machine they log into to fix things. Follow-up: why does a container lose files when it restarts?

## Reading logs and basic monitoring
Probe how they find out why a service is failing: where the logs are, what an error line tells them, and which basic metrics (CPU, memory, errors, response time) they look at. Strong: forms a guess from the evidence and checks it. Weak: restarts the service first. Follow-up: how would you know a service is down before a user tells you?

## Cloud basics
Probe the building blocks they know: compute, storage, networking, and access control. Strong: explains why an app should run with the least access it needs and keep its data out of public storage. Weak: uses an admin key everywhere. Follow-up: how would you keep a cloud bill from growing by surprise?
