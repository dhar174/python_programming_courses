# Day 8, Hour 2: Integrate the Database into the App
**Python Programming Advanced - Session 8**

---

## Timing Overview
**Total Time:** 60 minutes  
- Reframe the architecture goal: 5 minutes  
- Direct instruction on repositories and service interfaces: 15 minutes  
- Live integration demo: 10 minutes  
- Guided wiring sprint: 25 minutes  
- Debrief and exit ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Explain why the service layer should depend on an interface or behavior rather than a specific storage implementation
2. Replace in-memory or JSON persistence with a SQLite-backed repository while keeping the rest of the app stable
3. Identify what should and should not change when a storage backend is swapped
4. Verify persistence across restarts without creating two conflicting sources of truth
5. Use dependency injection in a practical, beginner-friendly way

---

## Instructor Prep Notes

- Use the same tracker app from earlier sessions
- Have one prior persistence implementation available, such as `JsonTrackerRepository`
- Have the SQLite repository prepared or mostly prepared so the focus stays on integration, not table design
- Keep repeating the phrase "same service contract, new storage engine"
- Prepare a before-and-after folder diagram to make the swap visible

---

## Section 1: The Architecture Goal (5 minutes)

### Opening Script

**[Instructor speaks:]**

This hour is where architecture stops being a buzzword and starts paying rent. Up to this point, some of you have stored records in memory, some in JSON, and some already in SQLite. What matters now is that the application should not care very much which storage mechanism is being used, as long as the service layer can still ask for the same behaviors.

That is the whole point of the repository idea. It is not there to make your folder tree look professional. It is there so you can change storage without rewriting your GUI, without rewriting your API, and without scattering SQL all over the project.

### The One Big Idea

**[Instructor speaks:]**

The one big idea is this: the service layer should depend on what the repository can do, not on how it does it.

That means the service layer should be able to say things like:

- add a record
- list records
- get a record by id
- update a record
- delete a record
- search records

Whether the repository stores data in a list, a JSON file, or a SQLite table is a separate concern.

---

## Section 2: Direct Instruction on Clean Wiring (15 minutes)

### Dependency Injection Without the Jargon Overload

**[Instructor speaks:]**

You may hear the phrase "dependency injection" in software discussions. That phrase can sound more complicated than it is. In our course, dependency injection just means we give the service the repository it should use rather than hard-coding the service to create one specific repository by itself.

Here is the version we want:

```python
repo = SQLiteTrackerRepository("data/tracker.db")
service = TrackerService(repo=repo)
```

Here is the version we are trying to avoid:

```python
class TrackerService:
    def __init__(self):
        self.repo = SQLiteTrackerRepository("data/tracker.db")
```

Why avoid the second version? Because it traps us. It makes the service harder to test. It makes it harder to switch persistence backends. It hides a choice that should be visible.

### What Should Stay Stable

**[Instructor speaks:]**

When we swap the storage layer, these things should stay stable:

- the model classes
- the service method names
- the validation logic
- the exceptions we raise
- the UI callbacks or API routes that call the service

These are the things that may change:

- repository implementation details
- connection setup
- SQL statements
- row mapping code
- initialization steps like `init_db()`

That distinction helps learners avoid panic. They realize they are not rebuilding the whole app. They are replacing one layer.

### The Risk of Two Sources of Truth

**[Instructor speaks:]**

One of the easiest ways to break a student project at this stage is to leave JSON writes active while also writing to SQLite. Then the learner changes one thing in the GUI, another thing in the database, and suddenly nobody knows what the "real" data is.

Say this clearly:

**[Instructor speaks:]**

Once SQLite becomes your source of truth, stop treating JSON as live storage. JSON can still be used for export and import, but not as a second hidden persistence path.

### Recommended Structure

You can show a simple project layout:

```text
src/
  tracker/
    models.py
    exceptions.py
    services.py
    repositories/
      base.py
      json_repo.py
      sqlite_repo.py
    db.py
gui/
  app.py
api/
  app.py
data/
  tracker.db
tests/
```

Then narrate:

**[Instructor speaks:]**

Your folders do not need to match this exactly, but your responsibilities should. The important thing is that the service imports the repository contract or expected behavior, and the GUI or API builds the service with the repository instance.

---

## Section 3: Live Demo of the Storage Swap (10 minutes)

### Demo Setup

**[Instructor speaks:]**

I am going to show a storage swap with the smallest amount of drama possible. First, here is a service that already works with a repository-like object.

```python
class TrackerService:
    def __init__(self, repo):
        self.repo = repo

    def add_record(self, title: str, category: str, status: str):
        record = Record(title=title, category=category, status=status)
        return self.repo.add(record)

    def list_records(self):
        return self.repo.list_all()

    def update_status(self, record_id: int, new_status: str):
        return self.repo.update_status(record_id, new_status)
```

Now the repository implementation:

```python
class SQLiteTrackerRepository:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def add(self, record: Record) -> Record:
        query = """
            INSERT INTO records (title, category, status)
            VALUES (?, ?, ?)
        """
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.execute(
                query, (record.title, record.category, record.status)
            )
            connection.commit()
            record.id = cursor.lastrowid
        return record

    def list_all(self) -> list[Record]:
        query = """
            SELECT id, title, category, status
            FROM records
            ORDER BY id ASC
        """
        with sqlite3.connect(self.db_path) as connection:
            rows = connection.execute(query).fetchall()
        return [Record.from_row(row) for row in rows]
```

Now wire it into the application entry point:

```python
def build_service() -> TrackerService:
    repo = SQLiteTrackerRepository("data/tracker.db")
    repo.init_db()
    return TrackerService(repo=repo)
```

### Demo Debrief

After you run the app, add a record, close the app, reopen it, and show that the record persists.

Then say:

**[Instructor speaks:]**

The exciting part of this demo is not that SQLite exists. The exciting part is that the UI barely changed. That is architecture paying off.

### Show a Controlled Failure

If possible, intentionally break the database path and show the error handling or logs:

**[Instructor speaks:]**

I also want you to see a failure. If I point to a missing or wrong database path, the app should fail in a way we can diagnose. Logs matter. Clear errors matter. This is part of shipping, not a side concern.

---

## Section 4: Guided Wiring Sprint (25 minutes)

### Lab Brief

**[Instructor speaks:]**

During this lab, your mission is to replace your old persistence layer with SQLite as the true backing store. You are not trying to redesign every class. You are trying to preserve as much of the surface area as possible.

### Required Tasks

Learners should:

1. Confirm the SQLite repository implements the methods the service expects
2. Add `init_db()` or equivalent startup initialization
3. Update the app entry point to construct the service with the SQLite repository
4. Remove or disable the old JSON-as-primary-storage workflow
5. Prove that add, list, update, and delete still work
6. Prove persistence across restarts

### Suggested Coaching Sequence

When circulating, guide learners in this order:

1. Check the constructor wiring first
2. Check the repository method names second
3. Check row-to-object mapping third
4. Check commit behavior fourth
5. Check UI refresh or API response behavior last

This order matters because many students debug symptoms instead of causes. A stale UI list may be caused by missing commits, a mismatched method name, or the wrong database path.

### What to Say to Learners Who Want to Rewrite Everything

**[Instructor speaks:]**

If you are tempted to refactor every file at once, stop. This is one of those moments where restraint is a professional skill. Make the smallest change that proves the architecture works. Once the app is stable, then improve naming or structure if time remains.

### Common Integration Bugs to Watch For

- Method mismatch such as `list_all()` in one repository and `list_records()` in another
- Forgetting to call `commit()` after inserts, updates, or deletes
- Mapping SQLite rows into dictionaries when the rest of the app expects model objects
- Initializing the service before the database schema exists
- Pointing the GUI at one database file and the API or tests at another

### Mid-Lab Checkpoint Questions

Ask learners:

- If I removed SQLite and gave you a new repository object, what would your service care about?
- Where does validation happen now?
- What is your single source of truth?
- How do you prove the data survives restart?

If they cannot answer those questions, they may have code that works temporarily but an architecture they do not really understand yet.

### Stretch Direction

If a learner finishes early, suggest an export feature:

**[Instructor speaks:]**

Keep SQLite as your source of truth, but add a CSV or JSON export command. That is a useful extension because it adds value without breaking the architecture.

---

## Section 5: Debrief and Exit Ticket (5 minutes)

### Debrief Script

**[Instructor speaks:]**

Let's close with the architectural lesson, not just the implementation detail. The goal was never "put data in SQLite" by itself. The goal was "put data in SQLite without turning the rest of the app into spaghetti." If your service interface stayed stable, that is a real design win.

### Share-Out Prompts

Invite learners to share:

- What changed the most during the storage swap?
- What changed the least?
- Where did you discover a hidden coupling?
- What would you refactor next if you had another hour?

### Exit Ticket

Ask:

1. What interface stayed the same when you swapped storage?
2. Why is it risky to keep JSON and SQLite as simultaneous live sources of truth?
3. What part of the integration felt most fragile?

### Transition to the Next Hour

**[Instructor speaks:]**

Next hour we build on this foundation by adding search, filter, and optional pagination patterns. That is where a data-driven app starts feeling genuinely useful instead of just technically correct.

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
