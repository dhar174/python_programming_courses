# Day 8, Hour 1: Optional ORM Slice or Deeper SQL Practice
**Python Programming Advanced - Session 8**

---

## Timing Overview
**Total Time:** 60 minutes  
- Reconnect to the data-driven app milestone: 5 minutes  
- Direct instruction on abstraction choices: 15 minutes  
- Live demo of two valid paths: 10 minutes  
- Guided build time: 25 minutes  
- Debrief, tradeoffs, and exit ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Explain in plain language what an ORM is and what problem it is trying to solve
2. Compare an ORM-based approach with a deeper SQL approach without treating either as "the one right answer"
3. Implement one practical extension to the SQLite-backed tracker application
4. Describe the tradeoff between convenience and transparency when choosing a data-access layer
5. Stay within the course scope by using either a tiny SQLAlchemy example or a focused SQL summary query

---

## Instructor Prep Notes

- Default capstone example: a tracker app with records containing `id`, `title`, `category`, `status`, `priority`, and `created_at`
- Primary path for most cohorts: deeper SQL practice with aggregates and grouped summaries
- Optional path only if the lab supports package installs cleanly: a very small SQLAlchemy model and one or two queries
- Keep the tone pragmatic: this is an exposure hour, not an ORM mastery hour
- Reassure learners that either path satisfies the runbook objective
- Have the existing SQLite database ready with at least 10-20 seed rows so grouped queries are meaningful

---

## Section 1: Reconnect to Yesterday's Momentum (5 minutes)

### Opening Framing

**[Instructor speaks:]**

Welcome back. We now have a data-driven application, which is a big step forward. Up to this point, we have spent time thinking carefully about models, services, repositories, SQLite, and safe CRUD behavior. Today we are not starting over. Today we are extending the same architecture and becoming more intentional about how we talk to the database.

This hour is a fork in the road by design, and that is a good thing. Some environments support a tiny ORM experiment. Some do not. Some learners benefit from seeing a higher-level abstraction. Others benefit more from getting better at raw SQL. The runbook gives us permission to choose either one because the real learning outcome is not "memorize SQLAlchemy syntax." The real learning outcome is: understand what you gain, what you lose, and how to keep your app maintainable.

When students hear "optional ORM slice," they sometimes assume the ORM path is more advanced and therefore automatically better. I want you to actively push against that assumption. A small app with clean SQL can be excellent. An ORM can be helpful, but it can also hide details that beginners still need to see. So our message today is simple: use the right level of abstraction for the team, the lab, and the project.

### Why This Hour Matters

**[Instructor speaks:]**

Yesterday we translated objects into tables and tables back into objects. That mapping work is exactly where ORMs try to help. If we do not use an ORM, then we should still deepen our SQL enough to answer practical questions such as:

- How many records are in each status?
- Which categories are growing fastest?
- Which priorities are most common this week?
- How do we summarize data without exporting it first?

That is why both tracks belong in the same hour. One path explores a tool that automates object-to-table mapping. The other path sharpens the SQL skills that every Python developer benefits from, even if they later use an ORM professionally.

### Message to Learners

**[Instructor speaks:]**

I want you to hear this clearly: you do not need to finish both tracks. You need to complete one track well, explain the tradeoffs clearly, and keep your application stable. Stability beats novelty every time in a course project.

---

## Section 2: Core Concept Walkthrough (15 minutes)

### What an ORM Does

**[Instructor speaks:]**

ORM stands for Object-Relational Mapper. That name sounds bigger than it is. An ORM is a tool that helps Python objects and relational database tables speak to each other. Instead of hand-writing every SQL statement and then manually converting rows into Python objects, the ORM gives you a model class and an API for creating, querying, updating, and deleting data.

At a high level, an ORM often gives you:

- Python classes that correspond to tables
- Fields on those classes that correspond to columns
- A session or unit-of-work object for database interaction
- Query methods that generate SQL under the hood
- Some validation or declarative metadata close to the model definition

That can improve consistency. It can reduce repetitive SQL. It can make some refactors easier. But it also adds a new abstraction layer. If the abstraction is not understood, debugging becomes harder, not easier.

### What Raw SQL Gives You

**[Instructor speaks:]**

Raw SQL gives you direct control. You see the exact query. You see the parameters. You know exactly what runs against the database. For learners who are still building intuition, that transparency matters. SQL also travels well across languages and frameworks. Even if a learner later switches to another tech stack, the ability to reason about `SELECT`, `JOIN`, `GROUP BY`, `COUNT`, `LIMIT`, and `WHERE` will stay valuable.

There is another practical reason to emphasize SQL: our course project is not trying to build a giant enterprise system. We are trying to build a solid, usable application with clear data rules. For that scale, SQLite plus clean SQL is often enough.

### The Real Comparison

**[Instructor speaks:]**

Here is the comparison I want learners to remember:

- ORM advantage: less repetitive mapping code, potentially faster development for common patterns
- ORM disadvantage: more abstraction, package dependency, hidden SQL, and more concepts to learn
- SQL advantage: clarity, portability, low dependency footprint, easy to debug in small apps
- SQL disadvantage: more boilerplate and more manual row-to-object conversion

This comparison is more honest than saying one is modern and the other is outdated. Both are modern. Both are useful. The right question is: "What helps this project and this team right now?"

### Scope Guardrails

**[Instructor speaks:]**

Today is not the day for migration frameworks, lazy-loading debates, advanced relationships, session lifecycle deep dives, or schema-generation magic. If learners start chasing those topics, gently bring them back. We are doing a tiny slice, not a full ORM course.

Likewise, if we stay on the SQL path, we are not trying to become database administrators in one hour. We are focusing on practical grouped summaries and safe query construction.

### Whiteboard Comparison

You can draw the following on the board:

```text
UI/API -> Service -> Repository -> SQLite

Option A:
UI/API -> Service -> ORM model/session -> SQLite

Option B:
UI/API -> Service -> SQL repository -> SQLite
```

Then narrate:

**[Instructor speaks:]**

Notice what stays the same across both options: the service layer still matters, the repository idea still matters, and SQLite is still the source of truth. That architectural continuity is what protects us from chaos.

---

## Section 3: Live Demo (10 minutes)

### Demo Track A: Tiny SQLAlchemy Slice

**[Instructor speaks:]**

If the environment supports SQLAlchemy, I will show the smallest useful example I can. I am not trying to impress you with syntax. I am trying to show you the shape of the abstraction.

```python
from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Base(DeclarativeBase):
    pass


class RecordRow(Base):
    __tablename__ = "records"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    category: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)


engine = create_engine("sqlite:///data/tracker.db")

with Session(engine) as session:
    rows = session.query(RecordRow).all()
    for row in rows:
        print(row.id, row.title, row.status)
```

Now narrate what learners should notice:

**[Instructor speaks:]**

The class is acting as a table description. The `Session` is our entry point for work with the database. The query returns Python objects with attributes. That is the convenience story in one screenful.

But then ask the important question:

**[Instructor speaks:]**

Would I replace my current repository with this right now, in the middle of the course, if the team is already succeeding with raw SQL? Maybe not. The tool is useful, but the timing matters.

### Demo Track B: Deeper SQL Practice

**[Instructor speaks:]**

Now let me show the SQL path that every cohort can use without additional packages. We already have a `records` table. I want a status summary. Instead of loading every row and counting in Python, I can let the database do the grouping.

```python
import sqlite3


def summarize_by_status(db_path: str) -> list[tuple[str, int]]:
    query = """
        SELECT status, COUNT(*) AS total
        FROM records
        GROUP BY status
        ORDER BY total DESC, status ASC
    """
    with sqlite3.connect(db_path) as connection:
        cursor = connection.execute(query)
        return cursor.fetchall()


for status, total in summarize_by_status("data/tracker.db"):
    print(f"{status}: {total}")
```

Then extend it slightly:

```python
def summarize_category_for_status(db_path: str, status: str) -> list[tuple[str, int]]:
    query = """
        SELECT category, COUNT(*) AS total
        FROM records
        WHERE status = ?
        GROUP BY category
        ORDER BY total DESC, category ASC
    """
    with sqlite3.connect(db_path) as connection:
        cursor = connection.execute(query, (status,))
        return cursor.fetchall()
```

Explain the teaching point:

**[Instructor speaks:]**

This is still very readable. It is parameterized. It is practical. And it answers questions a stakeholder might actually ask. That is the kind of SQL skill that pays off immediately.

### Demo Debrief

Ask:

**[Instructor speaks:]**

Which demo felt clearer to you? Which one felt faster to write? Which one would be easier for a new teammate to debug at 4 PM on a Friday?

That question usually produces better thinking than, "Which one is more advanced?"

---

## Section 4: Guided Build and Lab Coaching (25 minutes)

### Lab Brief

**[Instructor speaks:]**

For lab time, you will choose one path. Path A is the ORM mini-lab if the environment supports it. Path B is the SQL mini-lab. If you are undecided, choose Path B. It is the safer, more universal option and it directly improves your current application.

### Path A: ORM Mini-Lab

Learners should:

1. Install SQLAlchemy only if lab policy and package support are confirmed
2. Create one model class that represents the `records` table
3. Open a session and list rows
4. Explain how the ORM model maps to the table
5. Write down one advantage and one disadvantage in their README or notes

Coach with language like:

**[Instructor speaks:]**

Do not rebuild your whole app around SQLAlchemy today. The target is exposure and explanation. If you can define one model, run one query, and explain the mapping, you have succeeded.

### Path B: SQL Mini-Lab

Learners should:

1. Add one grouped summary query to the repository or reporting helper
2. Print a useful summary such as records by status or records by category
3. Keep the query parameterized if it accepts user input
4. Add a small display or command-line output that proves the query works
5. Capture the result in a `reports/` text file or console example for later demo use

You can suggest a starting point:

```python
def summarize_by_category(self) -> list[tuple[str, int]]:
    query = """
        SELECT category, COUNT(*) AS total
        FROM records
        GROUP BY category
        ORDER BY total DESC, category ASC
    """
    with sqlite3.connect(self.db_path) as connection:
        return connection.execute(query).fetchall()
```

Then ask learners to think one layer higher:

**[Instructor speaks:]**

Where should this live? Inside the service layer? Inside the repository? In a separate reporting helper? There is not only one defensible answer, but there are bad answers. A bad answer is putting this query directly inside a GUI callback or a Flask route. Keep the separation clean.

### Circulation Talking Points

As you circulate, listen for these patterns:

- Learner tries to concatenate strings into SQL
- Learner starts a huge ORM refactor instead of a tiny slice
- Learner cannot explain what problem the new query answers
- Learner duplicates logic that should live in the repository
- Learner is building a summary in Python after fetching all rows unnecessarily

Use short coaching nudges:

**[Instructor speaks:]**

What question is this query answering?

Could the database do that count for you?

If you swap storage later, which interface do you want to keep stable?

Where would a teammate look first for this logic?

### Sample Instructor Walkthrough for a Stuck Learner

If a learner is stuck, narrate a small recovery path:

**[Instructor speaks:]**

Let's simplify. We do not need the perfect report. We need one summary that works. Start with a plain SQL query. Run it in a tiny script. Once the result is correct, move it into the repository. Then call it from a service or report helper. Stable, small, testable.

If the learner is on the ORM path and losing time:

**[Instructor speaks:]**

Pause the package exploration. Keep one model, one session, one read query. The success condition is understanding the idea, not replacing your whole codebase.

---

## Section 5: Debrief, Tradeoffs, and Exit Ticket (5 minutes)

### Group Debrief Prompts

Invite two or three learners to share:

- What path did you choose?
- What question did your query or model help answer?
- What felt easier than expected?
- What felt more complex than you hoped?

### Common Pitfalls to Name Explicitly

**[Instructor speaks:]**

Before we move on, let me name the most common mistakes from this hour so you can recognize them quickly next time:

- Installing a new package without confirming the environment supports it
- Switching architecture mid-course because the abstraction looked exciting
- Writing unsafe SQL with string concatenation
- Creating reports in the UI layer instead of the repository or service layer
- Forgetting the difference between "interesting experiment" and "working project"

### Key Takeaway Script

**[Instructor speaks:]**

Here is the one sentence I want you to remember: abstraction is only helpful when it reduces confusion more than it adds confusion. That is the standard. Not trendiness. Not novelty. Clarity.

### Exit Ticket

Ask learners to answer out loud or in a chat message:

1. Name one advantage of an ORM.
2. Name one disadvantage of an ORM.
3. If you stayed with SQL, what is one new kind of question your database can answer now?

### Transition to the Next Hour

**[Instructor speaks:]**

In the next hour we are going to do something even more important than choosing abstractions: we are going to wire the repository cleanly into the application so our service layer can swap storage backends without breaking the UI. That architectural discipline is what makes the rest of the capstone realistic.

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
