# Day 10, Hour 4: Checkpoint 5 - API Milestone Demo
**Python Programming Advanced - Session 10**

---

## Timing Overview
**Total Time:** 60 minutes  
- Frame the checkpoint and success criteria: 10 minutes  
- Show the demo checklist: 5 minutes  
- Independent stabilization and rehearsal: 35 minutes  
- Showcase, reflection, and exit ticket: 10 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Demonstrate a working Flask API backed by SQLite
2. Show consistent JSON errors and an API key gate on write operations
3. Explain how the API connects to the service and repository layers
4. Identify the most fragile part of their current API milestone
5. Evaluate the milestone against correctness, structure, persistence, and maintainability

---

## Instructor Prep Notes

- Keep the checkpoint flow focused on the runbook requirements: CRUD, SQLite, JSON errors, API key gate, optional client
- Have a fast-grade sequence ready
- Encourage learners to stabilize instead of adding new features in the middle of the checkpoint

---

## Section 1: Frame the Milestone (10 minutes)

### Opening Script

**[Instructor speaks:]**

This checkpoint validates whether your API is not only present, but trustworthy. A trustworthy API responds predictably, protects the right operations, and still uses the same stable service and persistence layers underneath.

For this milestone, I am looking for:

- Flask API with CRUD routes
- SQLite-backed persistence
- consistent JSON error responses
- API key protection on write operations
- optional Python client, if you built one

### What Counts as Success

**[Instructor speaks:]**

Success today is not a giant feature list. Success is a believable demo where the API behaves consistently and you can explain the architecture behind it.

---

## Section 2: Show the Demo Checklist (5 minutes)

### Fast-Grade Sequence

Use this quick sequence:

1. `GET /health`
2. `GET /records`
3. `POST /records` with a valid API key
4. `PUT /records/<id>` with a valid API key
5. `DELETE /records/<id>` with a valid API key
6. one missing or invalid key failure
7. one invalid input or not-found failure

Then say:

**[Instructor speaks:]**

If your API can survive that sequence with clean responses, it is in strong shape for this checkpoint.

---

## Section 3: Stabilization and Rehearsal Time (35 minutes)

### Build Goal

**[Instructor speaks:]**

Use this time to rehearse and stabilize. Remove guesswork from the demo. Confirm your commands, sample payloads, headers, and expected status codes before you are on the clock.

### Suggested Validation Checklist

```text
[ ] API starts reliably
[ ] /health returns JSON
[ ] List route works
[ ] Create route returns 201
[ ] Update route returns 200
[ ] Delete route returns 200
[ ] Invalid input returns 400 with JSON error
[ ] Missing or wrong key returns 401/403 with JSON error
[ ] Data persists in SQLite
```

### Common Failure Modes

- route returns HTML error page instead of JSON
- one write route forgot the API key check
- service exception is not caught cleanly
- test payload does not match the parser contract
- database path differs between environments

### Coaching Prompts

- Which route are you least confident about?
- Can you explain the difference between a validation failure and a missing resource?
- Where is the API key loaded?
- Where is the repository constructed?
- What evidence do you have that SQLite is the source of truth?

### Recovery Script

**[Instructor speaks:]**

If one route is unstable, do not keep guessing in the interface. Reproduce the behavior in the smallest possible test. Then work outward again. Stable demos come from narrowing uncertainty, not from clicking faster.

---

## Section 4: Showcase and Reflection (10 minutes)

### Showcase Format

Invite a few learners or groups to show:

1. health
2. one successful write
3. one protected failure
4. one explanation of architecture

Keep demos short so the energy stays up.

### Reflection Questions

- What part of your API feels strongest?
- What part still feels fragile?
- What design choice saved you time today?
- What would you improve first if you had one extra hour?

---

## Section 5: Exit Ticket and Transition (5 minutes)

### Exit Ticket

1. What made your API milestone feel maintainable, not just functional?
2. Which failure case was most useful to test?
3. What is one thing you will carry into the analytics session next?

### Transition

**[Instructor speaks:]**

Next session we pivot into data analysis and reporting. Because your application now stores structured data cleanly, you can export, summarize, visualize, and report on it in a meaningful way.

---

## Shared Day 10 Instructor Reference

Reuse the shared day-level instructor support from `Day10_Hour1_Advanced.md` for this hour's facilitation details:

- `## Instructor Coaching Appendix`
- `## Facilitation Toolkit`

This keeps the Day 10 coaching guidance in one maintained location while preserving this file's hour-specific lecture script.
