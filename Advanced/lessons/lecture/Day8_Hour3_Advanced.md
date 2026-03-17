# Day 8, Hour 3: Search, Filter, and Pagination Patterns
**Python Programming Advanced - Session 8**

---

## Timing Overview
**Total Time:** 60 minutes  
- Problem framing and user need: 5 minutes  
- Direct instruction on search and paging patterns: 15 minutes  
- Live demo with safe SQL: 10 minutes  
- Guided implementation sprint: 25 minutes  
- Debrief and exit ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Add a practical search feature to a SQLite-backed application
2. Use parameterized `LIKE` queries safely
3. Explain the purpose of `LIMIT` and `OFFSET` in basic pagination
4. Keep search and pagination logic in the repository layer instead of scattering it across the app
5. Recognize common usability and correctness issues that appear when data sets grow

---

## Instructor Prep Notes

- Seed the database with enough records to make search meaningful
- Prepare examples with multiple categories and statuses so filters return noticeably different results
- Decide whether learners will expose search through the GUI, a small script, or both
- Keep pagination simple; learners do not need fully polished page controls to meet the hour goal

---

## Section 1: Why Search Matters (5 minutes)

### Opening Script

**[Instructor speaks:]**

An application stops feeling like a toy when users can actually find what they need. Up until now, many of our demos have involved tiny lists where we can just show all records. That works for ten rows. It stops working when the data grows. Search, filtering, and pagination are not glamorous features, but they are exactly the features that make users trust an application.

### The Real User Story

**[Instructor speaks:]**

Imagine a task tracker with 300 records. A user wants all items in the "billing" category that are still "open." They do not want to scroll forever. They do not want to visually inspect every row. They want the app to answer a question quickly and safely.

That is our design lens today. We are not adding search because it is on a feature checklist. We are adding search because it reduces friction for the user and creates better access patterns for larger data sets.

---

## Section 2: Core Search and Pagination Concepts (15 minutes)

### Safe Search with `LIKE`

**[Instructor speaks:]**

The first pattern we need is a parameterized `LIKE` query. In SQLite, `LIKE` lets us match partial strings. The mistake beginners often make is building SQL like this:

```python
query = f"SELECT * FROM records WHERE title LIKE '%{term}%'"
```

That is exactly what we do not want. Even in a course project, get learners in the habit of separating SQL structure from user-provided values.

Instead, do this:

```python
term = f"%{search_term.strip().lower()}%"
query = """
    SELECT id, title, category, status, priority
    FROM records
    WHERE lower(title) LIKE ?
       OR lower(category) LIKE ?
    ORDER BY id ASC
"""
rows = connection.execute(query, (term, term)).fetchall()
```

Point out two things:

1. The wildcard characters are added to the parameter value, not concatenated into the SQL string structure
2. We normalize case so the search feels more forgiving

### Filtering vs Searching

**[Instructor speaks:]**

It is helpful to distinguish these terms:

- Search usually means partial text matching
- Filter usually means narrow by an exact field or a constrained set of values

For example:

- Search: title contains "invoice"
- Filter: status equals "open"
- Filter: category equals "finance"

Combining them is normal. A clean repository method might accept both:

```python
def search(
    self,
    term: str = "",
    status: str | None = None,
    limit: int = 20,
    offset: int = 0,
) -> list[Record]:
    ...
```

### Why Pagination Exists

**[Instructor speaks:]**

Pagination exists because returning everything all the time is inefficient and unpleasant. When the data set grows, users should not have to render every row just to see the first screen of results. Pagination also gives the UI or API a predictable chunk size.

The simplest version uses:

- `LIMIT` for how many rows you want
- `OFFSET` for how many rows to skip

Example:

```sql
SELECT id, title, category, status
FROM records
ORDER BY id ASC
LIMIT 20 OFFSET 40;
```

That means: give me 20 rows starting after the first 40.

### What "Practical" Means in This Course

**[Instructor speaks:]**

We are not building infinite scroll, cursor-based pagination, or a dynamic search ranking engine. We are keeping this practical:

- one search box
- maybe one status filter
- a small page size such as 10 or 20
- optional next and previous controls

That is enough to teach the pattern and improve the app.

---

## Section 3: Live Demo (10 minutes)

### Repository Search Method

**[Instructor speaks:]**

Let me show a repository method that stays readable and safe.

```python
def search_records(
    self,
    term: str = "",
    status: str | None = None,
    limit: int = 20,
    offset: int = 0,
) -> list[Record]:
    conditions = []
    parameters: list[object] = []

    if term.strip():
        wildcard = f"%{term.strip().lower()}%"
        conditions.append("(lower(title) LIKE ? OR lower(category) LIKE ?)")
        parameters.extend([wildcard, wildcard])

    if status:
        conditions.append("status = ?")
        parameters.append(status)

    where_clause = ""
    if conditions:
        where_clause = "WHERE " + " AND ".join(conditions)

    query = f"""
        SELECT id, title, category, status, priority
        FROM records
        {where_clause}
        ORDER BY id ASC
        LIMIT ? OFFSET ?
    """
    parameters.extend([limit, offset])

    with sqlite3.connect(self.db_path) as connection:
        rows = connection.execute(query, tuple(parameters)).fetchall()

    return [Record.from_row(row) for row in rows]
```

Narrate what matters:

**[Instructor speaks:]**

The SQL structure is still visible. The values remain parameterized. We only add conditions that are needed. The method returns model objects so the service and UI stay consistent.

### Optional UI Hook

Then show a tiny GUI or script hook:

```python
def on_search(self):
    term = self.search_var.get()
    status = self.status_var.get() or None
    self.current_offset = 0
    records = self.service.search_records(term=term, status=status, limit=20, offset=0)
    self.populate_table(records)


def on_next_page(self):
    self.current_offset += 20
    records = self.service.search_records(
        term=self.search_var.get(),
        status=self.status_var.get() or None,
        limit=20,
        offset=self.current_offset,
    )
    self.populate_table(records)
```

Then caution learners:

**[Instructor speaks:]**

Notice that page state belongs in the UI layer, but query logic belongs in the service and repository layers. That separation keeps the design understandable.

### Demo Debrief

Ask:

**[Instructor speaks:]**

What would break if I moved the SQL into the button callback? The answer is not just "it would look messy." The deeper answer is that the logic would be harder to test, harder to reuse, and harder to expose later through an API.

---

## Section 4: Guided Implementation Sprint (25 minutes)

### Lab Brief

**[Instructor speaks:]**

Your mission is to make your app easier to use when the number of records grows. At minimum, add a search capability backed by the repository. If you have time, add a simple filter and next/previous paging.

### Minimum Success Criteria

Learners must:

1. Add a repository search method
2. Use parameterized SQL
3. Return correct results for at least one search scenario
4. Keep the logic outside the GUI callback or route handler

### Stronger Submission Criteria

If time allows, learners should also:

1. Add an exact-match status filter
2. Add `LIMIT` and `OFFSET`
3. Add a next/previous page pattern
4. Show a "no results" state clearly

### Suggested Lab Sequence

1. Start in the repository with a fixed search term hard-coded in a tiny script
2. Confirm the query returns the expected rows
3. Move the method into the service layer if needed
4. Connect the search term from the GUI or script input
5. Add pagination only after search works

This sequence reduces cognitive overload. Learners who attempt search, filter, paging, sorting, and UI polish all at once usually lose the thread.

### Coaching Prompts During Circulation

Ask questions like:

- What does this query return if the term is empty?
- Where are you adding the wildcard characters?
- What happens if there are zero matching results?
- How will the user know what page they are on?
- Are you ordering the results deterministically?

That last question is important. Pagination without deterministic ordering creates strange behavior. If page one and page two are based on an unstable order, users may see duplicates or missing rows.

### Common Bugs to Catch Early

- String-concatenated SQL with user input
- Search only checks one field when the learner intended multiple
- Offset increases forever without reset when a new search starts
- Previous page can go negative
- Empty term returns no rows when the learner expected "show all"
- UI does not clear stale rows before displaying new results

### Instructor Recovery Script for Overwhelmed Learners

**[Instructor speaks:]**

Let's reduce scope. First, search only by title. Then confirm it works. After that, search by title or category. Then, and only then, consider adding a filter. Pagination is optional until the core search path is correct.

### Stretch Extension

Advanced learners can add sorting:

**[Instructor speaks:]**

If you add sorting, do it carefully. Do not pass arbitrary column names directly from user input into SQL. Use a controlled mapping of allowed choices such as `"title"`, `"created_at"`, or `"priority"`.

---

## Section 5: Debrief and Exit Ticket (5 minutes)

### Debrief Script

**[Instructor speaks:]**

Search and pagination are great examples of features that look small on the surface but reveal the quality of your architecture. If your repository is clean, these features are straightforward. If your data access is tangled with the UI, these features become frustrating very quickly.

### Share-Out Questions

Invite learners to respond:

- What field did you search by?
- Did you add a filter, pagination, or both?
- Where did you keep your query logic?
- What bug did you hit that taught you something useful?

### Exit Ticket

1. Where should the `%` wildcard be added: the SQL string or the parameter value?
2. Why should paginated queries have a stable `ORDER BY`?
3. What should happen in the interface when a search returns zero rows?

### Transition to the Next Hour

**[Instructor speaks:]**

Next hour is Checkpoint 4. You will use everything from today and yesterday to demonstrate a genuine data-driven app: SQLite-backed CRUD, initialization, search, and architecture that still makes sense under pressure.

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
