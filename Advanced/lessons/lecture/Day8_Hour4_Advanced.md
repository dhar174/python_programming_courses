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

## Instructor-Ready Deep Dive: Running Checkpoint 4 as a Fast, Fair Milestone

This section expands the checkpoint into a full instructor script. The purpose of this hour is not to add new features. The purpose is to prove that the application has reached a stable, data-driven milestone.

### Learning Outcomes Reinforcement

**[Instructor speaks:]**

By the end of this checkpoint, you should be able to demonstrate a SQLite-backed app that performs the core workflows reliably. You should be able to create data, read it back, search it, update it, delete it, close the app, reopen it, and explain why the data survived. You should also be able to debug two very common database-app problems: schema mismatch and wrong-record updates.

I want to emphasize something: a checkpoint is not a feature race. It is a reliability test. If your app is stable, simple, and explainable, that is a stronger result than an app with three new features and one fragile persistence path.

### The Fast-Grade Mindset

**[Instructor speaks:]**

When I grade quickly, I am not trying to trick you. I am using a workflow that exposes the most important truths about your app. If the app can pass this sequence, it is very likely that your architecture is working:

1. Start from a clean launch.
2. Confirm `init_db()` runs without manual setup.
3. Create a record.
4. List records and confirm the new record appears.
5. Search for the record.
6. Close the app completely.
7. Reopen the app.
8. Confirm the record is still there.
9. Update the record by database ID.
10. Delete the record by database ID.
11. Search again and confirm the deleted record is gone.

This sequence is short, but it checks a lot: initialization, create, read, search, persistence, update, delete, ID handling, and source-of-truth discipline.

### Demo steps

Use this exact instructor demo before independent work:

1. Launch the instructor version of the app or a small reference script.
2. Say: **"I am starting from the app, not from a database editor."**
3. Create a record with a memorable title, such as `Checkpoint persistence proof`.
4. List records and point to the database ID.
5. Search for `persistence` and confirm the record appears.
6. Close the application process completely.
7. Reopen the application.
8. List or search again and confirm the record survived.
9. Update the status or priority of that same record.
10. Delete it.
11. Search for it again and confirm the app shows no result or an appropriate empty state.
12. Show the repository code briefly and point to parameterized SQL.
13. Show the startup code and point to `init_db()`.
14. Show the service constructor and point to repository injection.
15. Conclude: **"This is a stable milestone. It is not flashy, but it is real."**

### Fast-Grade Reference Script

If learners need a concrete target, show this minimal style of smoke check. Adapt names to the class project. This code assumes learners already have a service and repository with similar methods.

```python
from pathlib import Path


def run_checkpoint_smoke_test() -> None:
    repo = SQLiteTaskRepository(Path("data/checkpoint_tasks.db"))
    repo.init_db()
    service = TaskService(repo=repo)

    created = service.add_task("Checkpoint persistence proof")
    print(f"Created: {created.task_id} {created.title}")

    matches = service.search_tasks("persistence", limit=10, offset=0)
    print(f"Search matches after create: {len(matches)}")

    updated = service.mark_done(created.task_id)
    print(f"Updated: {updated.task_id} {updated.status}")

    service.delete_task(created.task_id)
    after_delete = service.search_tasks("persistence", limit=10, offset=0)
    print(f"Search matches after delete: {len(after_delete)}")


if __name__ == "__main__":
    run_checkpoint_smoke_test()
```

**[Instructor speaks:]**

This kind of script does not replace the app demo, but it is excellent for debugging. If the script fails, the GUI is probably not the first place to look. If the script passes and the GUI fails, then the issue is likely UI state, selected ID handling, or refresh logic.

## Lab prompt

**[Instructor speaks:]**

Your checkpoint work period starts now. Your job is to stabilize the milestone, not expand the product. Use this order:

1. Confirm the database initializes on startup.
2. Confirm create and list use SQLite.
3. Confirm search uses SQLite and parameterized queries.
4. Confirm update uses the database ID, not list position.
5. Confirm delete uses the database ID, not list position.
6. Confirm data survives a full application restart.
7. Confirm no common error crashes the app without a useful message.
8. Prepare a two-minute demo using the fast-grade workflow.

Do not add a second table until the core milestone is complete. Do not add authentication, themes, charts, or advanced UI polish during this hour. Those may be valuable later, but they are distractions today.

## Completion criteria

A checkpoint is considered complete when the learner can show:

- A SQLite repository with create, read/list, update, and delete behavior.
- `init_db()` runs on startup and is safe to run repeatedly.
- The app uses SQLite as the source of truth.
- Search works at a basic level and uses safe parameterized SQL.
- A record persists after closing and reopening the app.
- Update and delete target the intended database ID.
- The project organization separates model, service, repository, and interface responsibilities reasonably.
- The learner can explain how they would debug a schema mismatch.
- The learner can explain how they would debug an update/delete ID bug.

### Rubric Language for Instructor Use

Use this plain-language rubric while circulating:

- **Meets expectations:** Core CRUD works, restart persistence is proven, search works, SQL values are parameterized, and the learner can explain the architecture.
- **Approaching expectations:** Some workflows work, but restart proof, search, or ID handling is unreliable.
- **Needs revision:** The app still relies on in-memory or JSON state as live storage, does not initialize the database, or crashes during core workflows.
- **Exceeds expectations:** The core milestone is stable, the learner has a small smoke test or clear demo script, and any extension remains safely separated from the core architecture.

## Common pitfalls

### Pitfall 1: "It worked until I restarted"

Likely causes:

- The app stored data in memory but never wrote to SQLite.
- The write happened, but the connection was not committed.
- The app wrote to one database path and reopened another.
- Startup initialization dropped and recreated the table.

**[Instructor speaks:]**

Let's prove the path first. Then let's prove the write. Then let's prove the restart reads from the same database. We are not guessing; we are following the evidence.

### Pitfall 2: Schema mismatch

Symptoms include errors such as "no such column," missing values in model objects, or row conversion failures.

Likely causes:

- The model has a new field that the table does not contain.
- The SQL query selects columns in a shape the mapper does not expect.
- An older database file remains from a previous version of the schema.
- The learner changed `CREATE TABLE` but did not recreate or migrate the existing database.

**[Instructor speaks:]**

Schema mismatch is not a personal failure. It is one of the most normal database bugs. The fix starts by writing down the expected schema and comparing it to what the app is actually opening.

For the course milestone, the safest recovery is often:

1. Stop the app.
2. Confirm there is no valuable data in the practice database.
3. Rename or remove the old practice database file if appropriate.
4. Run startup again so `init_db()` creates the current schema.
5. Re-test create, list, search, update, and delete.

Only do that with practice data. In real systems, schema migrations must preserve production data.

### Pitfall 3: Update or delete affects the wrong record

Likely causes:

- The UI uses table row index instead of database ID.
- Search or pagination changes visible order, but the app still assumes row 0 means ID 1.
- The selected ID is stale after refresh.
- The SQL `WHERE` clause uses the wrong value.

**[Instructor speaks:]**

Once search and pagination exist, list position is not identity. The database ID is identity. Print the ID you are about to update or delete, then compare it to the visible record and the repository call.

### Pitfall 4: Unsafe search SQL

Likely causes:

- The learner used string concatenation or an f-string with raw user text.
- The wildcard was pasted around the placeholder incorrectly.
- Filters were added by trusting arbitrary column names.

Recovery language:

**[Instructor speaks:]**

Keep the SQL structure controlled by your program. Put user-provided values in parameters. For search, build the wildcard value in Python and pass it as the parameter.

## Optional Extension

Only offer these after the checkpoint is stable:

- Add a second table and demonstrate one small `JOIN`, such as tasks and categories.
- Add a count query for search results.
- Add CSV export that reads from SQLite but does not replace SQLite as the source of truth.
- Add a smoke-test script that runs the fast-grade workflow automatically on a practice database.

Keep repeating: the extension must not destabilize the milestone. If an extension breaks CRUD or restart persistence, pause the extension and restore the checkpoint.

## Quick Check

Ask learners to answer:

1. What proved that SQLite was the source of truth?
2. Why is `init_db()` part of the checkpoint rather than an optional setup detail?
3. What is the difference between database ID and list position?
4. What is one symptom of schema mismatch?
5. What is the first thing you should check if data disappears after restart?
6. Why is a stable milestone more valuable today than a new feature?

Expected answer themes: restart proof demonstrates persistence; `init_db()` makes startup reliable; database ID is stable identity while list position changes; schema mismatch appears as missing columns or row mapping errors; disappearing data requires checking path, commit, and source of truth; stability proves the architecture is ready for the next session.

## Instructor Conference Guide

Use short, targeted conferences rather than long debugging takeovers. Ask each learner or pair:

- "Show me where your database is initialized."
- "Show me the repository method that creates a record."
- "Show me the line that passes the repository into the service."
- "Show me how you know this record survived restart."
- "Show me which ID will be updated or deleted."
- "Show me where user input is passed as SQL parameters."

If they cannot show an answer, that is the next work item. If they can show an answer, ask them to run the fast-grade sequence.

### Stable Milestone Closing Script

**[Instructor speaks:]**

Today is the point where your project starts to look like a real application. Real applications have to remember things. They have to find things. They have to update the intended record rather than whichever row happens to be visible. They have to recover from restart. They have to keep user input separate from SQL structure.

If your app passed the fast-grade workflow, you have earned a meaningful milestone. If it did not pass yet, you now have a precise map of what to fix. Either way, the checkpoint has done its job: it made the invisible parts of your architecture visible.

## Additional Instructor Script: Keeping the Checkpoint Focused

Use this block during the work period when learners are drifting into new features.

**[Instructor speaks:]**

I am going to be very direct about scope. The checkpoint is not asking you to build the most impressive app you can imagine. It is asking you to prove that the foundation is stable. A foundation is not exciting in the same way a new visual feature is exciting, but every later feature depends on it.

If you have 20 minutes left and CRUD is unreliable, do not add a chart. If search is unsafe, do not add a theme. If restart persistence is unproven, do not start a second table. Stabilize the milestone first.

### The Checkpoint Evidence Board

Write these headings on the board or display them:

```text
Initialization | Create | Read/List | Search | Update | Delete | Restart Proof | Safe SQL
```

Ask learners to mark each heading as green, yellow, or red:

- Green means "I can demonstrate it now."
- Yellow means "It partially works or needs verification."
- Red means "It is missing or broken."

**[Instructor speaks:]**

Your next task is not the most interesting green item. Your next task is the highest-risk red or yellow item. This is how professional debugging often works: identify the risk, reduce the risk, then move on.

### A Two-Minute Demo Template

Give learners this exact structure for their final demonstration:

1. "Here is my app starting up."
2. "Here is where `init_db()` runs."
3. "I create a record named `Checkpoint demo item`."
4. "I search for `demo` and find it."
5. "I close and reopen the app."
6. "The record is still present, proving persistence."
7. "I update the record using its database ID."
8. "I delete the record using its database ID."
9. "Here is one repository method showing parameterized SQL."
10. "One issue I fixed was..."

This template keeps showcase time fair and prevents rambling. It also trains learners to present evidence, not just claims.

### Instructor Triage Language

When a learner says, "Nothing works," respond with a narrowing question:

**[Instructor speaks:]**

Let's find the first failing link. Does startup run? Does the table exist? Can the repository create one record from a script? Can the service call that repository method? Can the interface call the service? We only need the first failing link right now.

When a learner says, "Search is broken," ask:

**[Instructor speaks:]**

Does the repository search method work when called directly with a known term? If yes, the issue is probably service wiring or interface state. If no, the issue is probably query logic, data, or parameters.

When a learner says, "Delete deletes the wrong thing," ask:

**[Instructor speaks:]**

Show me the ID being passed to delete. Is it the database ID or the row number in the current display? After search and pagination, row number is not a stable identity.

### Milestone Debugging Examples

Give these as short "debug stories" to normalize mistakes:

**Story 1: The vanishing record.** A learner created records successfully, but they disappeared after restart. The problem was not the insert statement. The app was opening `data/tasks.db` when launched from one folder and `tasks.db` in the project root when launched from another. The fix was to use a clear `Path` relative to the project or application data directory and print the resolved path during development.

**Story 2: The invisible schema change.** A learner added a `priority` field to the model and query, but the existing table did not have a `priority` column. The `CREATE TABLE IF NOT EXISTS` statement did not modify the old table because the table already existed. For the course practice database, the learner recreated the practice database after confirming no important data was inside. The teaching point is that schema and model evolve together.

**Story 3: The list index bug.** A learner searched for open tasks, selected the first visible row, and clicked delete. The app deleted ID 1 instead of the selected task because it used the table row number. The fix was to store the selected database ID with the displayed row and pass that ID into the service.

### Professional Habits to Praise

During showcase, explicitly praise habits that may otherwise go unnoticed:

- The learner can explain the source of truth.
- The learner uses a small smoke test before opening the GUI.
- The learner prints or logs the database path while debugging.
- The learner uses parameterized queries consistently.
- The learner keeps the service interface stable.
- The learner chooses a stable milestone over a risky extension.
- The learner describes a bug and the evidence used to fix it.

**[Instructor speaks:]**

These habits are part of engineering skill. They are not secondary to code. They are how code becomes reliable.

### Preparing for the Next Session

Close the day by connecting the checkpoint to the upcoming Flask/API work:

**[Instructor speaks:]**

Next session, when we expose behavior through HTTP routes, we do not want route functions full of SQL. The work you did today makes that possible. A route can call the service. The service can call the repository. SQLite remains behind the repository boundary. That is why this checkpoint matters beyond today's grade.

If your checkpoint is green, you are ready to build outward. If your checkpoint still has red or yellow items, your best homework is not a new feature. Your best homework is to make the fast-grade workflow boringly reliable. Boring reliability is a compliment in software.
