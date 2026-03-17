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

## Instructor Coaching Appendix

### Whiteboard Plan for Day 8

Use this appendix to slow the class down and make the database-to-application relationship visible. Draw three boxes on the board labeled `service`, `repository`, and `database`. Under the service box, list the verbs the learner cares about: add, list, get, update, delete, search. Under the repository box, list the translation work: SQL statements, parameter binding, row mapping, commits, initialization. Under the database box, list the tables and constraints that make the information durable. Then say out loud that the whole day is about keeping those responsibilities separate so the application stays understandable.

After drawing the three boxes, add arrows in both directions. Explain that reads flow from the database into rows, from rows into objects, and then into the service layer for the rest of the application. Writes flow the other way. This visual helps students stop imagining the database as magic storage and start imagining it as one layer in a system.

When you reach Hour 29, add a note beside the repository box that says `raw SQL or ORM abstraction`. Explain that this is the day's controlled fork. The application still needs a stable service layer either way. In Hour 30, emphasize the arrow from the application entry point into the service constructor. In Hour 31, add `search, filter, limit, offset` near the repository box. In Hour 32, circle the entire diagram and say that the checkpoint is evaluating whether all three boxes cooperate cleanly.

### Listen-Fors During Guided Practice

As learners work today, listen less for jargon and more for evidence that they understand the architectural consequences of their decisions. Strong signs include statements like these:

- "I kept the route or callback simple and let the service call the repository."
- "I moved the query into the repository because the GUI should not know SQL."
- "I reset the offset when the search term changes."
- "I proved persistence by restarting the app."
- "I picked the SQL path because it fit the lab and the project better."

Worry signs include comments like these:

- "I copied the JSON save here just in case."
- "I think it updates the right record because it usually lines up with the list index."
- "I added an ORM and now I need to rewrite the whole project."
- "I built the query with string formatting because it was faster."
- "The app still shows the record after delete, so I guess it worked."

When you hear a worry sign, do not immediately solve the code for the learner. Ask a clarifying question first. Good examples are:

- "What is your source of truth now?"
- "Where would a teammate look for that logic?"
- "What ID is actually being passed into the update or delete call?"
- "How could you prove the query is correct outside the interface?"
- "If you restart the app, what result should you see?"

These questions reinforce design reasoning rather than just patching symptoms.

### Common Misconceptions to Correct Immediately

One common misconception is that a database-backed app is automatically well designed. It is not. A poorly structured project can still use SQLite. The value comes from clear boundaries, safe queries, and predictable behavior. Say this directly so students do not confuse the presence of a `.db` file with architectural quality.

A second misconception is that an ORM is the "advanced" choice and raw SQL is somehow a beginner fallback. That framing is misleading. In small and medium-sized applications, raw SQL can be the clearer and more honest option. Emphasize that abstraction is a tradeoff, not a badge of seniority.

A third misconception is that search is mostly a UI feature. Search is partly a UI feature, but the real correctness lives lower down. If the repository does not return the right rows, the prettiest search box in the world does not matter. Keep pushing students to validate the data access layer before blaming the interface.

A fourth misconception is that pagination is just a performance trick. In reality, it is also a usability pattern. It limits cognitive load, keeps result sets manageable, and supports predictable navigation. Even if students never implement sophisticated pagination professionally, understanding why `LIMIT` and `OFFSET` exist will help them reason about data-heavy interfaces.

### Suggested Mini-Conferences for Each Hour

For Hour 29, ask students to explain the benefit and cost of the path they chose. If they chose the ORM slice, ask what the ORM is saving them from writing manually. If they chose deeper SQL, ask what direct SQL makes easier to understand or debug.

For Hour 30, ask students to point to the exact line where the repository is injected into the service. Then ask what stayed the same above that line when the storage implementation changed. This quickly reveals whether they understand the point of the repository pattern.

For Hour 31, ask students to state the search behavior they expect before they run it. A student who can say, "an empty term should show all rows, a term should search title and category, and a new search should reset to page one" usually has a much stronger implementation plan.

For Hour 32, ask students to narrate their milestone demo before they give it. If their explanation is confused, the demo is often confused too. Coaching the narrative helps surface missing initialization steps, unclear sources of truth, and hidden assumptions.

### Pacing Adjustments

If the cohort is behind schedule, treat Hour 29 as a SQL deepening hour only. Do not force the ORM branch. Students gain more from one clear summary query and a stable architecture than from a rushed package experiment that creates confusion.

If Hour 30 runs long because many students are still unwinding older JSON persistence, pause feature work and explicitly direct them to remove or disable the second source of truth. That cleanup is worth more than squeezing in extra polish.

If students struggle with Hour 31, narrow the success condition. Search first, then filter, then pagination. In a mixed-ability cohort, requiring all three at once can bury the learning objective.

If the checkpoint hour reveals widespread instability, reduce the public demo requirement and spend more time on guided debugging. The milestone is still valuable if it turns into a structured bug-fix session, as long as learners connect the bugs back to architecture and data access practices.

### Evidence of Mastery for Day 8

A student has met the spirit of Day 8 when they can do more than show a working interface. Look for these evidence points:

- They can explain why the database is now the system of record.
- They can point to a repository method and explain what it returns.
- They can prove persistence across restart instead of merely claiming it.
- They can describe at least one safe SQL practice they used.
- They can separate a UI concern from a repository concern.
- They can describe one tradeoff in the ORM versus raw SQL discussion.

A particularly strong student can also explain what they intentionally did not build yet. That shows scope control, which is a professional skill.

### End-of-Day Instructor Wrap Script

Use this if you want a clean close to the session:

**[Instructor speaks:]**

Today was about moving from a project that merely stores some information to a project that behaves like a real data-driven application. You made choices about abstraction, storage, integration, search, and reliability. Those choices matter because they determine whether the next layer of the capstone will feel stable or fragile. If your application can now create, retrieve, update, delete, search, and persist across restarts with a clear source of truth, that is real progress. Do not underestimate it.

Before the next session, encourage students to write down one thing they cleaned up architecturally and one bug they still want to understand better. That reflection makes the jump into Flask and API work much smoother.

---

## Facilitation Toolkit

### Pre-Class Quick Check

Before this hour begins, spend thirty seconds confirming that learners have the right file, environment, and mental context open. Many instruction problems that look conceptual are actually setup drift. Ask learners to open the project folder, point to the main entry file for the hour, and remind themselves which layer they are primarily working in. If the hour is centered on the API, ask them to name the route, service, and repository layers. If the hour is centered on analytics, ask them to name the dataset and report path. If the hour is centered on testing or packaging, ask them to name the target command they expect to run before the hour ends. This tiny reset reduces confusion and gives the room a shared starting line.

A second quick check is motivational rather than technical. Tell learners what "done" looks like in one sentence. Students perform better when the finish line is visible. For example, say: "By the end of this hour, you should be able to show one stable route with predictable errors," or "By the end of this hour, you should have one repeatable report artifact saved in the reports folder." The clarity matters more than the elegance of the wording.

### Layer-Specific Observation Checklist

As you circulate, avoid scanning only for syntax errors. Look for the layer-specific habits that show whether the learner is truly aligning with the course architecture.

For interface-facing work, check whether the learner is keeping the interface thin and delegating correctly. Look for signs that they are handling input, calling a service, and formatting output rather than placing business logic directly in callbacks or route handlers.

For service-layer work, check whether the learner is enforcing rules consistently and raising the right custom exceptions. Ask whether the same rule would behave the same way from multiple entry points.

For repository or persistence work, check whether the learner is using parameterized queries, committing intentionally, and mapping rows or outputs predictably. Ask whether there is one clear source of truth.

For analysis and reporting work, check whether the learner can explain how data moves from source to artifact. Ask what cleaning decisions were made and whether the result could be reproduced tomorrow.

For testing and packaging work, check whether the learner is proving meaningful behaviors rather than merely following a checklist. Ask what risk the test or fresh-run step is reducing.

This checklist helps you stay aligned to the course outcomes instead of getting trapped in line-by-line debugging for the whole hour.

### Coaching Ladder for Stuck Learners

Use a three-step coaching ladder when a learner is stuck.

Step one is diagnosis by description. Ask the learner to describe what they expected, what actually happened, and what they already checked. This keeps you from jumping into the wrong problem too early.

Step two is scope reduction. Help the learner shrink the problem to the smallest reproducible step. If a full GUI flow is failing, test the service method alone. If the full report fails, run the export alone. If the packaged app will not start, verify imports and environment setup before touching build tools. Small proofs are often faster than large guesses.

Step three is boundary identification. Ask which layer should own the fix. Many student problems persist because they keep applying the patch in the wrong layer. A route bug gets fixed in the service, a repository bug gets patched in the UI, or a packaging issue gets blamed on test code. Naming the layer often reveals the correct next action.

When learners are very anxious, narrate your thought process slowly and visibly. Say things like, "I want to verify the assumption before I change the code," or "Let's confirm the source of truth first." This models calm technical reasoning and reduces the impulse to thrash.

### Differentiation Moves for Mixed-Ability Cohorts

In almost every class, some learners finish early while others are still stabilizing the basics. Use differentiation deliberately instead of letting the room split into boredom on one side and panic on the other.

For learners who need more support, narrow the success condition without changing the underlying outcome. Replace a full feature set with the smallest honest version. One route before five. One query before search plus paging plus sorting. One report artifact before a whole dashboard. One integration test before an elaborate suite. The learner still practices the right habit, just with reduced surface area.

For learners who are ready for more challenge, add a bounded extension that reinforces the same lesson rather than a completely different topic. Examples include adding one more filter option, improving error messages, adding a second chart type, or writing one additional negative test. Bound the extension tightly so it does not become an escape hatch into unrelated rabbit holes.

A useful phrase for both groups is: "Keep the same architecture, change the ambition level." That sentence helps advanced learners stretch without drifting and helps struggling learners simplify without feeling like they failed.

### Discussion Prompts That Reveal Understanding

When you want to know whether a learner truly understands the hour, ask questions that require reasoning instead of recall. Useful prompts include:

- What part of this workflow would break first if the source of truth changed unexpectedly?
- What behavior in your code is currently easiest to explain to a teammate, and why?
- Where is the most fragile coupling in your design right now?
- If you had to test or demo only one thing from this hour, what would give the strongest evidence that the concept is working?
- What did you intentionally leave out to keep the project aligned with the course scope?

These prompts are helpful because they work across architecture, API, analytics, testing, and packaging topics. They also generate better class discussion than simply asking whether the code runs.

### Common Classroom Risks and Soft Interventions

One risk is silent divergence, where learners are working on different interpretations of the same task. You can reduce this by pausing for a thirty-second midpoint recap and restating the minimum success condition. Another risk is overbuilding, where a learner adds complexity because the simpler version feels too small. In that case, praise the initiative but redirect toward finishing the stable milestone first.

A third risk is shallow success, where the code appears to work once but the learner cannot explain why. Do not ignore that just because the output looks correct. Ask for a short explanation. If the explanation is weak, there is still learning work to do.

A fourth risk is perfection paralysis. Some learners freeze because they want the cleanest possible solution before they will run anything. Encourage executable increments. A visible imperfect step is often more teachable than a perfect idea still trapped in someone's head.

### Evidence Collection for Informal Assessment

If you need to assess quickly during the hour, look for five kinds of evidence:

- A concrete artifact exists, such as a running endpoint, saved report, passing test, or updated README.
- The learner can explain the responsibility of the layer they are touching.
- The learner can name one failure mode and how they checked it.
- The learner can connect the work back to the capstone architecture or delivery goals.
- The learner can identify one next improvement without losing sight of the current milestone.

This evidence-based approach is more reliable than grading on confidence or speed alone.

### End-of-Hour Documentation Prompt

Before learners leave the hour, ask them to capture three short notes in their own project documentation or notebook:

1. What changed?
2. What was verified?
3. What still needs attention?

This takes very little time, but it creates continuity between hours and improves final demos because learners have a record of decisions, validations, and remaining risks. It also makes the project feel like professional technical work instead of a sequence of disconnected classroom exercises.

### Closing Script You Can Reuse

**[Instructor speaks:]**

The point of this hour was not only to produce code or artifacts. It was to practice the habit behind the code: keeping boundaries clear, proving behavior honestly, and making the project easier to understand for the next person who touches it. If you can explain what changed, show evidence that it works, and name what still needs improvement, then you are making real progress.
