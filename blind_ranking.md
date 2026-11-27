# Blind ranking
For each setup, rank the 2 question sets from best to worst on the Ranking line, e.g. `Ranking: Y > X`.
Judge each set against the setup's role, level and job description (the quoted lines under its heading).
Optional, under each set: `Rating:` four whole numbers from 1 to 5, in this order: fit (role and level), relevance (job description; `-` when there is none), variety, specificity, e.g. `Rating: 4 5 3 4`; and `Note:` one line on why you ranked it so.

## Setup complete-behavioral-junior
> **Role:** mobile | **Level:** junior | **Type:** behavioral | **Questions:** 4
> **Job description:** none given (judge on role and level only)

Ranking:

### X
1. Can you tell me about a time when you needed to handle app data while offline in a project you worked on, such as the workout tracker you listed?
2. Can you share an experience from your mobile internship where an app went into the background or was killed by the system while a user was entering data, and how you ensured their input wasn't lost?
3. Tell me about a time when you were working on a mobile feature and encountered a bug or technical challenge you couldn't solve on your own, and how you decided when and how to ask for help.
4. Can you describe a time when you had to explain a technical issue or bug you fixed during your internship to someone without a technical background, such as a product manager or stakeholder?
Rating:
Note:

### Y
1. Can you tell me about a time when you joined a project and had to build a UI layout that needed to look correct on both a small phone and a larger tablet?
2. Can you describe a specific time you were building a screen layout and had to ensure it worked well on both a small phone and a tablet with large text enabled?
3. Can you tell me about a time when you got stuck while trying to fix a bug or build a feature, and walk me through how you decided to ask for help?
4. Can you share a time when you had to explain a technical issue or bug to someone non-technical, such as a product manager or client, and how you made sure they understood it?
Rating:
Note:

## Setup near-empty-data-intern
> **Role:** data | **Level:** intern | **Type:** technical | **Questions:** 3
> **Job description:** none given (judge on role and level only)

Ranking:

### X
1. When working with a dataset that has missing values and duplicate rows, how do you decide whether to remove them or fill them in?
2. How do you explain a complex data pipeline error or a tricky bug to a non-technical stakeholder?
3. When reviewing a teammate's pull request or technical solution, what specific things do you check before approving it?
Rating:
Note:

### Y
1. When working with a dataset that has missing values and duplicate rows, how do you decide whether to drop them or fill them in?
2. In a data project you listed involving trip data, how did you structure your SQL or pandas queries to transform raw data into a reliable weekly report?
3. When building models or reports with tools like dbt, how do you verify that your transformation logic is correct before merging your work?
Rating:
Note:

## Setup profile-injection-backend-mid
> **Role:** backend | **Level:** mid | **Type:** technical | **Questions:** 3
> **Job description:**
> Backend developer for an orders API in Python and PostgreSQL.

Ranking:

### X
1. How would you design an API endpoint for creating orders in Python so that client retries from network timeouts do not result in duplicate orders being placed in PostgreSQL?
2. What is missing here? Please provide a concrete situation or example of how you implemented idempotency keys or database constraints for order creation.
3. When an order creation requires both saving the order in PostgreSQL and publishing an event to a message broker, how do you ensure consistency between the database write and the message without risking duplicate processing?
Rating:
Note:

### Y
1. When designing an orders API in Python that other client teams depend on, how do you handle resource naming, pagination, and making sure retries are safe?
2. Can you walk through a specific feature or change you worked on involving an orders service, and how you ensured data consistency when multiple writes had to happen together?
3. Can you share a specific production incident from a project you listed where an orders service was impacted, how you diagnosed it using metrics or logs, and what long-term fix you put in place?
Rating:
Note:

## Setup profile-mismatch-backend-mid
> **Role:** backend | **Level:** mid | **Type:** technical | **Questions:** 4
> **Job description:**
> Backend developer for a payments API: Python, PostgreSQL and idempotent retries.

Ranking:

### X
1. When designing an API endpoint that external clients depend on for reliable operations, how do you handle idempotency for retries, and what strategies do you use to evolve the contract without breaking existing consumers?
2. Can you walk through how you ensure data consistency between two separate writes, such as updating a user balance and recording a transaction, when a network failure occurs midway?
3. When implementing a caching layer to scale read operations, how do you handle invalidation and prevent cache stampedes under high concurrency?
4. Thinking about a production incident you handled involving unexpected behavior under load, how did you use your logs, metrics, or traces to identify the root cause and mitigate the impact?
Rating:
Note:

### Y
1. How would you design a PostgreSQL table schema and transaction flow for a payment endpoint that must ensure a charge and an order record are always created together without leaving orphan records?
2. Can you provide a concrete example of when you implemented idempotent retries for an API endpoint, and how you handled the edge case of concurrent duplicate requests?
3. When caching read queries for an API with high traffic, how do you decide what to cache, and how do you handle invalidation when the underlying data changes?
4. Could you walk through a production incident where an API you owned experienced a sudden spike in latency or errors, and explain how you used logs, metrics, or traces to find and mitigate the root cause?
Rating:
Note:

## Setup strong-backend-mid
> **Role:** backend | **Level:** mid | **Type:** technical | **Questions:** 5
> **Job description:**
> Backend developer for a payments API in Python and PostgreSQL.

Ranking:

### X
1. When building a refunds service with a retry queue, how do you handle situations where a payment charge and its corresponding order record must both be updated atomically?
2. How do you design an API endpoint for processing refunds so that clients can safely retry failed requests without accidentally duplicating charges?
3. How do you decide when to add a Redis cache in front of a PostgreSQL database, and how do you handle invalidation when payment data changes?
4. Can you describe a production incident you handled involving a payment or reconciliation pipeline, and how you used logs, metrics, or traces to mitigate it before applying a permanent fix?
5. How do you explain a complex architectural change or database migration to a product manager or non-technical stakeholder?
Rating:
Note:

### Y
1. How would you design an API endpoint for processing payments that needs to handle retries safely without charging a customer twice?
2. Can you give a specific example of how you implemented idempotency for that payments endpoint, and how the client and server handled the retry keys?
3. When designing database schemas in PostgreSQL for a high-volume system, how do you approach indexing strategies and querying patterns for tables that experience frequent concurrent updates?
4. How would you investigate and resolve a sudden performance degradation in a production PostgreSQL database caused by long-running queries during peak traffic?
5. When a caching layer needs to be introduced to reduce database load for a read-heavy payments dashboard, how do you handle invalidation strategies and prevent cache stampedes?
Rating:
Note:
