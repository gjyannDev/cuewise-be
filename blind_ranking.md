# Blind ranking
For each setup, rank the 5 question sets from best to worst on the Ranking line, e.g. `Ranking: W > V > Z > Y > X`.
Judge each set against the setup's role, level and job description (the quoted lines under its heading).
Optional, under each set: `Rating:` four whole numbers from 1 to 5, in this order: fit (role and level), relevance (job description; `-` when there is none), variety, specificity, e.g. `Rating: 4 5 3 4`; and `Note:` one line on why you ranked it so.

## Setup complete-behavioral-junior
> **Role:** mobile | **Level:** junior | **Type:** behavioral | **Questions:** 4
> **Job description:** none given (judge on role and level only)

Ranking:

### X
1. Can you tell me about a time when you were working on a workout tracker project you listed and had to handle multiple urgent tasks competing for your attention?
2. Could you describe a specific moment in your internship when you got stuck on a bug and decided to ask a teammate for help?
3. Can you tell me about a time when you had to adapt a mobile screen layout to work across different device sizes?
4. Can you tell me about a time when you needed to explain a technical bug or its fix to someone on your team who was not a developer?
Rating:
Note:

### Y
1. Can you tell me about a time you had to fix a bug in a mobile app when you weren't entirely sure what was causing it?
2. Tell me about a time you received constructive feedback on a pull request for a mobile feature and how you handled it.
3. Can you describe a situation where you had to collaborate with a designer or a backend developer to implement a new screen or feature on mobile?
4. Tell me about a time you had to learn a new tool, library, or language quickly to complete a mobile development task.
Rating:
Note:

### Z
1. Can you tell me about your part in a project you worked on with others, and how you split up the work between team members?
2. When you were building the workout tracker project you listed, how did you decide what to try on your own before asking for help when you got stuck?
3. Thinking about the internship experience you listed, can you tell me about a time you received feedback on your code that was difficult to hear, and how you handled it?
4. Can you describe a time when you had to explain a technical issue or design decision from your work to someone outside of engineering, and how you made sure they understood it?
Rating:
Note:

### V
1. Can you tell me about a time when you got stuck on a bug in your mobile app, and walk me through how you decided when and how to ask a more experienced teammate for help?
2. Can you tell me about a time when your mobile app had to handle going into the background or being killed by the system while the user was in the middle of a task?
3. Tell me about a time you had to build or adjust a mobile screen so that it looked correct on both a small phone and a larger tablet, including any challenges with text sizing or layout constraints.
4. Can you tell me about a time when you had to explain a complex mobile bug or technical issue to someone outside of engineering, like a product manager or support team member?
Rating:
Note:

### W
1. Can you tell me about a time when you got stuck on a bug in a mobile app, what you tried on your own first, and how you decided when and how to ask for help?
2. Tell me about a time when an app you worked on had to handle going into the background or getting killed by the system while the user was in the middle of an action.
3. Can you share an example of a screen you built that needed to work across different screen sizes and with large text enabled?
4. Tell me about a time when you had to explain a technical issue or bug to someone outside of engineering, like a product manager or a client.
Rating:
Note:

## Setup long-job-description-frontend-junior
> **Role:** frontend | **Level:** junior | **Type:** technical | **Questions:** 5
> **Job description:**
> About us: we are a small team building a booking platform for independent fitness studios. Thousands of studios use us to manage classes, memberships and payments, and their members book through our web app and our white-label mobile web pages. The role: you will join the customer-facing web team of six engineers and one designer. You will build and maintain booking flows, the member account area and the studio dashboard. Our stack is TypeScript, React, Next.js, React Query and Tailwind, with Playwright for end-to-end tests and Storybook for components. Accessibility matters to us: many members book on older phones, so performance on slow networks is part of every feature. What we expect: one to two years of professional experience with React and TypeScript, comfort writing tests, curiosity about how the API works behind the screens, and clear written communication, because we work across three time zones. Nice to have: experience with payment forms, internationalisation or design systems. We offer remote work, a learning budget and four weeks of holiday.

Ranking:

### X
1. When building a web app that needs to work offline like the flashcard app you listed, how do you decide what data to store locally and how do you handle data synchronization when the connection returns?
2. How would you style a complex component using CSS so it adapts cleanly to both wide desktop screens and narrow mobile viewports?
3. When building a form component, how do you decide whether state should live locally inside the component or be lifted up to a parent, and how does that choice affect re-renders?
4. When reviewing a pull request from a teammate where you spot a bug or a risk, how do you phrase your feedback so they understand the reasoning and feel supported?
5. When explaining a complex technical change or a tricky bug fix to someone outside your team, such as a product manager or support staff, how do you structure your explanation?
Rating:
Note:

### Y
1. When building a React component that fetches data from an API, how do you handle loading, error, and empty states so the interface remains clear to the user?
2. When you are writing unit or component tests with React, how do you decide which edge cases to cover beyond the basic happy path?
3. How do you ensure semantic HTML and accessibility standards like keyboard navigation and screen-reader support are met when building a new component?
4. When reviewing a teammate's pull request on a React and TypeScript project, what specific things do you look for before approving it?
5. Could you walk me through a specific situation where you had to explain a technical problem or solution to someone outside of engineering, such as a product manager or designer?
Rating:
Note:

### Z
1. When building the settings pages you mentioned in your experience, how did you structure the CSS layouts and ensure they worked well for keyboard users?
2. Could you walk me through a specific layout you built with flexbox or grid in that project, and how you decided which one to use?
3. When reviewing a teammate's code or a technical solution, how do you decide what feedback to leave, and how do you phrase your requests for change?
4. When you are preparing to ship a change in a project you listed, how do you decide which test cases to cover and what to leave to manual checks?
5. When you needed to explain a technical problem or design decision to someone outside of engineering, how did you decide what details to include and structure your explanation?
Rating:
Note:

### V
1. When building a feature in React that fetches data from an API, how do you decide what state to keep in local component state versus a library like React Query?
2. When writing tests for a React component using Playwright or another testing tool, how do you determine what user interactions and assertions are necessary to ensure the feature works reliably?
3. When you join an existing codebase and need to fix a bug in a component you did not write, what steps do you take to understand how it works and verify your fix?
4. When building a user-facing feature with Tailwind CSS and React, how do you approach styling to ensure it is accessible to keyboard users and works well on smaller screens?
5. When you notice that a web application feels sluggish or takes too long to load initial content on a slower mobile device, how do you investigate and identify the performance bottleneck?
Rating:
Note:

### W
1. When building a multi-step booking form in React, how do you decide whether state should live locally within a component or be lifted up to a parent?
2. When fetching and caching data with React Query for a studio dashboard that updates frequently, how do you handle loading states and stale data to ensure the UI stays responsive?
3. When writing a component that needs to be accessible to screen reader and keyboard users, how do you verify its keyboard navigation and semantic structure?
4. When writing automated end-to-end tests with Playwright for a critical booking flow, how do you decide which edge cases and failure states to cover versus leaving to manual checks?
5. When building a Next.js web application for users on older phones and slow networks, how do you measure and optimize page performance for your components?
Rating:
Note:

## Setup near-empty-data-intern
> **Role:** data | **Level:** intern | **Type:** technical | **Questions:** 3
> **Job description:** none given (judge on role and level only)

Ranking:

### X
1. When you are working with a dataset that contains missing values and incorrect data types, how do you decide whether to drop those rows, fill them with estimated values, or flag them for further investigation?
2. When reviewing a teammate's code or technical solution before it gets merged, what specific criteria do you use to evaluate it, and how do you decide what feedback to leave?
3. When you need to explain a technical design, a bug, or an infrastructure change to someone outside your field, such as a product manager or a support team, how do you structure your explanation?
Rating:
Note:

### Y
1. When designing a database table to store user profile information that might change over time, how would you decide whether to use a relational database or a NoSQL database?
2. When writing a SQL query that joins multiple large tables together, what steps would you take to investigate and improve its performance if it takes too long to execute?
3. If an ETL pipeline you built fails partway through loading data into a destination warehouse, how would you design it to recover safely without duplicating records?
Rating:
Note:

### Z
1. When cleaning a dataset with missing values, how do you decide whether to drop those rows or impute the missing data, and what impact does that choice have on your analysis?
2. In one of your data projects using Python and pandas, how did you handle duplicate rows or incorrect data types, and what effect did those steps have on your final output?
3. When developing a data model in dbt, how do you approach writing tests for data quality, and how do you handle models that fail those checks?
Rating:
Note:

### V
1. When cleaning a messy dataset for analysis, how do you decide whether to drop rows with missing values, fill them in, or flag them, and what effect does that choice have on your final result?
2. When you were working on the data analysis project you listed, how did you write your SQL queries to handle tables or joins that might duplicate rows by mistake?
3. When presenting the findings from a data analysis project to an audience, how do you structure your presentation, and what caveats do you make sure to highlight?
Rating:
Note:

### W
1. When working with a dataset that has missing values and duplicate rows, how do you decide whether to remove them or fill them in, and how do those choices affect your analysis?
2. What specific steps would you take to clean a dataset containing columns with incorrect data types before performing any analysis on it?
3. When reviewing a teammate's code or technical solution before it gets merged, what specific aspects do you look at to decide whether to approve it or request changes?
Rating:
Note:

## Setup profile-injection-backend-mid
> **Role:** backend | **Level:** mid | **Type:** technical | **Questions:** 3
> **Job description:**
> Backend developer for an orders API in Python and PostgreSQL.

Ranking:

### X
1. When designing a RESTful API endpoint for creating orders in PostgreSQL, how do you handle concurrent requests that might try to insert duplicate order numbers or oversell inventory?
2. When working with a PostgreSQL database under high write volume, what strategies do you use to manage connection pooling and prevent the database from becoming a bottleneck?
3. When an orders API needs to integrate with a flaky external payment gateway, what architectural patterns do you use to ensure data consistency and prevent dropped orders?
Rating:
Note:

### Y
1. When building an API endpoint for creating orders that other internal teams depend on, how do you handle client retries safely to avoid duplicate orders, and how would you structure the resource naming and pagination for fetching the order history?
2. When two database writes must both succeed—such as creating an order record and processing a payment—how do you ensure consistency, and what changes if the payment processing happens via an external third-party service?
3. Can you walk through a specific production incident involving slow database queries or high latency that you investigated, how you identified the bottleneck using metrics or logs, and what steps you took to mitigate and prevent it from happening again?
Rating:
Note:

### Z
1. When designing a public API endpoint for creating orders that other teams depend on, how do you handle retries safely without risking duplicate orders, and how do you approach versioning the endpoint when you need to make a breaking change?
2. Can you walk me through a concrete example where you implemented that approach, including the specific idempotency mechanism and how you handled potential race conditions between concurrent requests with the same key?
3. When an order creation workflow requires writing to both the PostgreSQL database and an external payment gateway, how do you ensure data consistency between them if the payment succeeds but the database write fails, and what specific transaction or architectural patterns do you use to handle that?
Rating:
Note:

### V
1. When building an API endpoint in FastAPI that other services depend on, how do you handle versioning and breaking changes without disrupting existing clients?
2. When working with Python and PostgreSQL on an orders service you listed, how do you ensure data consistency across multiple database writes when part of the operation fails?
3. Can you walk through how you would investigate and resolve a performance issue in a production orders service where specific read queries have slowed down over time?
Rating:
Note:

### W
1. When building an endpoint for a service that other teams depend on, how do you handle versioning and breaking changes without disrupting existing clients?
2. When you need to ensure that two related writes, such as updating an order and recording a payment, both succeed reliably in a Python and PostgreSQL backend, how do you handle failures and data consistency?
3. When an endpoint handling order data experiences high traffic and slow response times in production, how would you go about identifying the root cause and addressing it?
Rating:
Note:
