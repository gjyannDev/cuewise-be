---
roles: devops
levels: mid, senior
source: posting
---
# Platform and DevOps practice

## CI/CD pipelines with safe rollback
Probe a pipeline they built from commit to production: build, test, package, deploy, promote between environments and roll back. Strong: names the gates that stop a bad build and a rollback that is automatic or one step. Weak: manual steps and no rollback plan. Follow-up: how do you handle a database change in the same deploy?

## Infrastructure as code in practice
Probe how they manage cloud resources as code: reusable modules, remote state, separate environments, review in Git. Strong: explains how state is protected and how a change is planned and reviewed before it is applied. Weak: edits resources by hand in the console. Follow-up: what do you do when real infrastructure drifts from the code?

## Containers and Kubernetes troubleshooting
Probe a service that keeps restarting or is unreachable: how do they find out why? Pod status and events, logs, resource limits, configuration and secrets, service and ingress. Strong: works layer by layer and checks limits and configuration before changing anything. Weak: restarts things until it works. Follow-up: how do you keep secrets out of images and repositories?

## Monitoring, alerting and observability
Probe how they know a service is unhealthy before users report it: metrics, logs, traces, dashboards and alert thresholds. Strong: alerts on user impact, avoids noisy alerts and links each alert to a runbook. Weak: collects everything and alerts on everything. Follow-up: how do you cut alert noise without missing a real incident?

## Production problems with no obvious cause
Probe a time the cause was unclear across application, network, cloud and database. Strong: narrows it step by step, mitigates first, and ends with a change that prevents a repeat. Weak: stops at the first plausible cause or blames a person. Follow-up: how do you prove the fix removed the cause?

## Cloud security, backup and recovery
Probe how they keep a cloud environment secure and recoverable: least-privilege access, network boundaries, backups, a disaster recovery plan and cost. Strong: has actually tested a restore and states a recovery time goal. Weak: has backups but never restored one. Follow-up: how do you balance cost against resilience?
