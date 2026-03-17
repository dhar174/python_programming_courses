# Day 8, Hour 4: Checkpoint 4 - Data-Driven App Milestone
**Python Programming Advanced - Session 8**

---

## Timing Overview
**Total Time:** 60 minutes  
- Frame the checkpoint and rubric: 10 minutes  
- Demo the fast-grade workflow: 5 minutes  
- Independent build and validation time: 35 minutes  
- Showcase, reflection, and exit ticket: 10 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Demonstrate a SQLite-backed application that persists data across restarts
2. Show clean CRUD behavior using the database as the source of truth
3. Explain where search logic and initialization logic live in the project
4. Identify and fix common milestone bugs such as schema mismatches and incorrect IDs
5. Evaluate their own work against a checkpoint rubric focused on correctness, architecture, persistence, and professional habits

---

## Instructor Prep Notes

- Have the checkpoint rubric visible before learners start building
- Prepare a short "fast grade" demo: create, close, reopen, search, update, delete
- Encourage learners to aim for a stable milestone rather than extra features
- Expect several learners to discover hidden bugs only when they restart the app; build time for that

---

## Section 1: Framing the Milestone (10 minutes)

### Opening Script

**[Instructor speaks:]**

This hour is not a brand-new lesson. It is a proving hour. We are validating that the architecture from the last several sessions can survive contact with reality. A data-driven app milestone means the application is no longer pretending to have persistence. It actually has it.

Today I am looking for four things:

1. SQLite is truly the source of truth
2. CRUD operations work reliably
3. Search works at a practical level
4. The code organization still makes sense under pressure

If your app is a little plain but stable, that is better than a flashy app that crashes. Stability is the priority.

### Clarify the Deliverables

**[Instructor speaks:]**

For this checkpoint, the required deliverables are:

- a SQLite repository with CRUD
- database initialization on startup
- an app that uses the database as the true source of truth
- a working basic search feature
- a short demo that proves persistence across restarts

The stretch goal is a second table or a join, but that is absolutely not required for success today.

### Connect to the Rubric

Display or read the checkpoint criteria in plain language:

- Correctness: do the workflows behave as expected?
- Architecture and clarity: is the code reasonably organized?
- Error handling: do failures behave cleanly?
- Persistence and integration: does data survive restarts?
- Professional habits: did you use sensible naming, logging, and incremental testing?

Then say:

**[Instructor speaks:]**

Notice that I am not grading you only on whether one happy-path demo works one time. I am looking for reliability and design judgment.

---

## Section 2: Show the Fast-Grade Workflow (5 minutes)

### Instructor Demonstration

**[Instructor speaks:]**

Before you work independently, I want to show you the quickest honest way to prove this milestone.

Use a short demo flow:

1. Launch the app
2. Create a record
3. Search for that record
4. Close the app completely
5. Reopen the app
6. Confirm the record still exists
7. Update the record
8. Delete the record

Narrate the reasoning:

**[Instructor speaks:]**

If you can do that sequence reliably, you have already demonstrated most of the milestone. If you cannot do it, the sequence tells you exactly where to look next: initialization, add flow, search path, restart persistence, update logic, or delete logic.

### What the Demo Should Not Depend On

**[Instructor speaks:]**

Your milestone demo should not depend on:

- hand-editing the database file
- remembering hidden setup steps that are not documented
- a previous run's leftover state that you cannot explain
- hard-coded values that only work on your machine

If the app only works because of luck, it is not ready.

---

## Section 3: Independent Build and Validation Time (35 minutes)

### Build Goal

**[Instructor speaks:]**

Use this work period to stabilize, not to chase novelty. If you are halfway through adding a fancy feature, pause it. Finish the milestone requirements first.

### Recommended Work Sequence

Guide learners to work in this order:

1. Confirm database initialization
2. Confirm create and list
3. Confirm search
4. Confirm update and delete
5. Confirm restart persistence
6. Confirm error handling and logs

This order helps isolate the failures that matter most.

### Validation Checklist for Learners

Ask learners to keep this checklist beside them:

```text
[ ] Database file exists in the expected path
[ ] init_db runs safely on startup
[ ] Add creates a new record in SQLite
[ ] List reads from SQLite, not stale in-memory data
[ ] Search returns expected results
[ ] Update targets the correct record ID
[ ] Delete removes the intended record
[ ] Restart proves persistence
[ ] Common errors do not crash the app
```

### Coaching Notes for Common Failure Modes

#### Failure Mode 1: Data Appears Until Restart, Then Disappears

Likely causes:

- no commit after write operations
- writing to one database file and reading from another
- still using in-memory data for display

What to say:

**[Instructor speaks:]**

Let's verify the database path first. Then let's verify commit behavior. Then let's confirm your list view is actually reloading from SQLite rather than showing cached objects.

#### Failure Mode 2: Update or Delete Affects the Wrong Record

Likely causes:

- using list index instead of a stable ID
- wrong `WHERE` clause
- stale selected ID in the UI

What to say:

**[Instructor speaks:]**

Print the ID you think you are updating. Then inspect the SQL or repository call. Stable IDs matter more than list position once data can be searched and paginated.

#### Failure Mode 3: Search Returns Strange Results

Likely causes:

- wildcard placement errors
- forgetting to normalize case
- stale UI rows not cleared
- SQL assembled incorrectly

What to say:

**[Instructor speaks:]**

Test the repository method by itself first. Once the query is correct, reconnect it to the interface.

#### Failure Mode 4: Schema Mismatch

Likely causes:

- code expects a column that the table does not have
- learner changed the model but not the schema
- old database file remains from earlier experiments

What to say:

**[Instructor speaks:]**

This is a real-world bug category. The database schema and the application model must evolve together. For the course, keep the schema small and explicit so you can reason about it.

### Mini-Conferences During Build Time

As you circulate, do 30-second architecture checks:

- Ask one learner to point to the repository
- Ask another to explain where validation lives
- Ask another to explain how restart persistence is proven
- Ask another to explain why JSON is not the live source of truth anymore

These micro-conversations reveal understanding faster than staring at code silently.

### Encourage Professional Habits

**[Instructor speaks:]**

If you change something significant and it works, commit it. This is a perfect time for small, truthful commits such as:

- `feat: wire sqlite repo into tracker service`
- `fix: use stable record id for update and delete`
- `feat: add search query to sqlite repository`

Small commits make it easier to recover from mistakes.

---

## Section 4: Showcase and Reflection (10 minutes)

### Demo Format

Invite a few learners or pairs to show their milestone quickly:

1. Show the app running
2. Create a record
3. Search for it
4. Restart and prove persistence
5. Explain one design decision

Keep each showcase short so the pace stays high.

### Reflection Prompts

Ask:

- What bug cost you the most time today?
- What design choice saved you time today?
- What feels stable now that did not feel stable yesterday?
- If a teammate joined your project tonight, what would confuse them first?

### Instructor Close

**[Instructor speaks:]**

Checkpoint hours are valuable because they show you the difference between understanding a concept and operationalizing a concept. You now have a much more honest picture of your project. That is progress, even if today exposed a few bugs.

---

## Section 5: Exit Ticket and Transition (5 minutes)

### Exit Ticket

Ask learners to answer briefly:

1. What was the most common database bug you hit today?
2. What proved to you that SQLite is now your source of truth?
3. What part of your architecture are you most likely to refine next?

### Transition Forward

**[Instructor speaks:]**

Next session we move up a level and expose our application through a REST API using Flask. Because you stabilized your repository and service layer today, that next step will be dramatically easier than it would have been a week ago.

---

## Shared Day 8 Instructor Reference

Reuse the shared day-level instructor support from `Day8_Hour1_Advanced.md` for this hour's facilitation details:

- `## Instructor Coaching Appendix`
- `## Facilitation Toolkit`

This keeps the Day 8 coaching guidance in one maintained location while preserving this file's hour-specific lecture script.
