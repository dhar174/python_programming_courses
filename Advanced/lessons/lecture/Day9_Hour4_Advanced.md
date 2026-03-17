# Day 9, Hour 4: App Structure, Blueprints, and Dependency Wiring
**Python Programming Advanced - Session 9**

---

## Timing Overview
**Total Time:** 60 minutes  
- Frame the maintainability problem: 5 minutes  
- Direct instruction on application structure and factories: 15 minutes  
- Live refactor into `create_app()` and routes module: 10 minutes  
- Guided refactor lab: 25 minutes  
- Debrief and exit ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Explain why a growing Flask app needs clearer structure
2. Refactor a single-file Flask app into a maintainable application layout
3. Use a simple `create_app()` pattern to wire dependencies predictably
4. Understand when Flask blueprints are helpful and when they are optional
5. Avoid common circular-import and hidden-global-state mistakes

---

## Instructor Prep Notes

- Use the word "pragmatic" often; the runbook explicitly warns against overframeworking
- Present blueprints as optional, not mandatory dogma
- Keep the focus on dependency wiring and predictable startup
- Prepare one example of a circular-import problem to discuss conceptually

---

## Section 1: Why Structure Starts to Matter Now (5 minutes)

### Opening Script

**[Instructor speaks:]**

Single-file applications are great for learning and fast starts. They become fragile once the route count grows, once the service layer matters, and once configuration enters the picture. At that moment, structure stops being aesthetic and starts being practical.

Today we are going to keep our API maintainable by making startup predictable, separating route definitions, and being clear about where services and repositories are created.

---

## Section 2: Direct Instruction on App Structure (15 minutes)

### The Problem With "Everything in `app.py`"

**[Instructor speaks:]**

When everything lives in one file, a few things tend to happen:

- imports get noisy
- route handlers get mixed with setup code
- configuration values hide in random places
- service and repository creation happens at import time
- tests become harder because the application is not easy to construct in a controlled way

None of that means the learner did something wrong. It means the project grew.

### A Simple Application Factory

**[Instructor speaks:]**

The application factory pattern sounds formal, but our version is simple. It means we wrap app construction in a function:

```python
def create_app() -> Flask:
    app = Flask(__name__)
    repo = SQLiteTrackerRepository("data/tracker.db")
    repo.init_db()
    service = TrackerService(repo=repo)

    register_routes(app, service)
    return app
```

Why is this helpful?

- startup happens in one place
- dependencies are created explicitly
- tests can construct the app when needed
- different environments can pass different settings later

### Where Blueprints Fit

**[Instructor speaks:]**

Blueprints are Flask's way of grouping routes. They are useful, but optional. In this course, the most important structural win is separating routes into a module and wiring the service clearly. If learners are comfortable, blueprints are a nice next step. If they are already juggling enough, a routes module plus `create_app()` is sufficient.

### Avoiding Hidden Global State

**[Instructor speaks:]**

One common trap is creating the repository or service as a global at import time:

```python
service = TrackerService(SQLiteTrackerRepository("data/tracker.db"))
```

That seems convenient, but it makes behavior harder to control. The moment the module is imported, the dependency is created. Tests become harder. Configuration becomes harder. Errors can occur before the app has even started properly.

### Circular Imports

**[Instructor speaks:]**

Circular imports often appear when `app.py` imports `routes.py`, `routes.py` imports `app`, and both want access to shared objects. The easiest course-level defense is to pass the dependencies in and keep module responsibilities narrow.

---

## Section 3: Live Refactor (10 minutes)

### Starting Point

Show a simplified single-file structure:

```python
app = Flask(__name__)
repo = SQLiteTrackerRepository("data/tracker.db")
service = TrackerService(repo)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/records")
def list_records():
    return [record.to_dict() for record in service.list_records()]
```

Then say:

**[Instructor speaks:]**

This works, but it scales poorly. Let's move toward clearer construction.

### Refactor Target

```python
# api/app.py
from flask import Flask
from tracker.repositories.sqlite_repo import SQLiteTrackerRepository
from tracker.services import TrackerService
from api.routes import register_routes


def create_app() -> Flask:
    app = Flask(__name__)
    repo = SQLiteTrackerRepository("data/tracker.db")
    repo.init_db()
    service = TrackerService(repo=repo)
    register_routes(app, service)
    return app


app = create_app()
```

```python
# api/routes.py
from flask import jsonify, request


def register_routes(app, service):
    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.get("/records")
    def list_records():
        return jsonify([record.to_dict() for record in service.list_records()])
```

### Narrated Debrief

**[Instructor speaks:]**

This structure is not fancy, and that is exactly why it is appropriate. Construction is explicit. The routes module receives the service. The app still runs normally. We gained maintainability without disappearing into framework complexity.

---

## Section 4: Guided Refactor Lab (25 minutes)

### Lab Goal

**[Instructor speaks:]**

Your goal is to refactor your API so a future teammate can understand startup and route wiring quickly. You do not need perfect architecture. You need architecture that is readable and predictable.

### Required Tasks

Learners should:

1. Move route definitions into a dedicated module or grouping structure
2. Add a `create_app()` function
3. Construct the repository and service in one visible place
4. Confirm `/health` and `/records` still work after the refactor

### Optional Task

If comfortable, learners may introduce a blueprint for the resource routes, but this is not required.

### Suggested Refactor Order

1. Create `routes.py`
2. Move one route first and confirm imports work
3. Add `create_app()`
4. Pass `service` into the route registration function
5. Run the app and verify endpoints

This incremental approach is much safer than cutting everything over in one move.

### Common Mistakes

- Importing `app` from the routes module, which creates circular imports
- Creating dependencies both globally and in `create_app()`
- Moving code before confirming the original app still works
- Refactoring too many concepts at once, such as adding config classes, blueprints, environment loading, and testing hooks all in the same hour

### Coaching Prompts

- Where is the one place a teammate should look to understand startup?
- If you wanted a test database tomorrow, where would that setting enter?
- Are you constructing the service once or in multiple places?
- Could a reader identify which module owns routes and which module owns domain logic?

### Instructor Recovery Script

**[Instructor speaks:]**

If the refactor feels risky, move one route, run it, and only then move the next. Refactors are safer when you preserve a working state after each step.

### Fast Finishers

Strong learners can add a simple config constant or configurable database path, but only after the structural refactor is stable.

---

## Section 5: Debrief and Exit Ticket (5 minutes)

### Debrief Script

**[Instructor speaks:]**

This hour was about maintainability, not visible features. Those hours are easy to undervalue because the app may look similar from the outside. But this kind of structural clarity is what lets the project survive future changes instead of becoming brittle.

### Share-Out Questions

- What part of your Flask app became clearer after the refactor?
- Where do you now create the repository and service?
- Did you use a routes module only, or routes plus blueprints?
- What circular-import risk did you avoid?

### Exit Ticket

1. What is the risk of creating the repository or service at import time?
2. Why is `create_app()` useful?
3. When are blueprints helpful, and why are they optional in this course?

### Preview of the Next Session

**[Instructor speaks:]**

Next session we secure the API at a basic level, build a small Python client, and make a deliberate integration choice between GUI and API surfaces. Today's structure work will make that much easier.

---

## Instructor Coaching Appendix

### Whiteboard Plan for Day 9

Draw a horizontal flow across the board that reads `client -> route -> service -> repository -> database`. Underneath it, draw the reverse response flow: `database -> repository -> service -> serializer -> JSON response`. Spend a minute on each boundary. Explain that Day 9 is about making these boundaries predictable enough that another interface can trust them.

Beside the client box, list the tools students are using to talk to the API: browser, curl, PowerShell, or a later Python client. Beside the route box, list `methods`, `status codes`, and `JSON parsing`. Beside the service box, list `validation rules`, `exceptions`, and `business behavior`. Beside the serializer area, list `consistent shape` and `error contract`. This picture helps students see why route handlers should stay thin.

In Hour 33, emphasize the health endpoint and the request-response contract. In Hour 34, add the CRUD route set to the board and underline the difference between `400` and `404`. In Hour 35, draw two smaller boxes labeled `parse` and `serialize` and connect them to the route layer. In Hour 36, circle the left side of the diagram and label it `API structure`, then note that maintainability improves when startup and route registration happen in one predictable place.

### Listen-Fors During Labs

Strong Day 9 language sounds like this:

- "This handler just parses the request and calls the service."
- "We return `201` because the record was created."
- "This is a validation error, so it should be `400`."
- "The route no longer builds the response shape itself; the serializer does."
- "We moved the app construction into `create_app()` so testing and startup are clearer."

Concerning language sounds like this:

- "I wrote SQL in the Flask route because it was nearby."
- "Everything returns `200` for now and I'll clean it later."
- "This route returns a string here and a dictionary there, but it works."
- "I import the app from routes and routes from app, and it mostly runs."
- "I added more logic to the handler because I wasn't sure where else it belonged."

When you hear those warning signs, ask questions that move learners back toward architectural clarity:

- "What is the one responsibility of this route?"
- "Which layer should own this validation rule?"
- "Could another endpoint reuse this parsing logic?"
- "If you changed the response shape, how many files would you edit?"
- "What happens if a teammate reads this route cold tomorrow morning?"

### Common Misconceptions for Day 9

Students often think REST means memorizing a large ruleset. Keep reminding them that for this course REST means resource-oriented thinking, standard verbs, and predictable responses. That is enough.

Another common misconception is that adding more endpoints automatically means stronger API design. Counter that quickly. A small API with consistent contracts and honest status codes is stronger than a large API with improvised behavior.

A third misconception is that validation belongs only in the route because the route sees the raw request. In practice, some normalization belongs in parsing helpers and some domain rules still belong in the service layer. Students need to learn that "where data first appears" is not the same as "where every rule should live."

Finally, many learners think refactoring structure is secondary to visible feature work. Day 9 is a good place to explain that a clear app factory, explicit dependency wiring, and route grouping are not extras. They are how the project stays teachable and testable.

### Suggested Mini-Conferences for Each Hour

For Hour 33, ask students to define a resource using their own project language. If they cannot name the resource clearly, their route design often becomes fuzzy.

For Hour 34, ask one student to explain when `400` is correct and when `404` is correct. Then ask another student to identify where the service layer is being called. This keeps both HTTP reasoning and architecture reasoning active.

For Hour 35, ask students what changed after they introduced parsing and serialization helpers. Good answers mention fewer duplicated shapes, easier cleanup, or clearer route handlers. Weak answers reveal that helpers exist but are not actually central.

For Hour 36, ask learners to point to the exact place dependencies are created and the exact place routes are registered. If they can do that quickly, their structure is probably improving.

### Pacing Adjustments

If the cohort struggles with Flask startup in Hour 33, do not rush into multiple resource routes. Make sure the app runs, `/health` works, and structured errors are visible first. Those early wins reduce the anxiety that often shows up when students first touch web frameworks.

If Hour 34 becomes a status-code tangle, pause and do a mini whole-class sorting exercise. Give three scenarios and ask the class to vote on `200`, `201`, `400`, or `404`. This short reset often saves more time than letting confusion continue silently.

If students are overwhelmed in Hour 35, let them centralize only one route first. Once the pattern is visible, the remaining routes are much easier to clean. This keeps the lesson about repeatable design rather than perfection.

If Hour 36 reveals a lot of import confusion, temporarily defer blueprints. A routes module plus a simple application factory is enough. The runbook explicitly allows blueprints to remain optional.

### Evidence of Mastery for Day 9

Look for these evidence signals:

- Students can explain their route set without looking at the code.
- Their API returns structured JSON instead of accidental HTML errors.
- They understand why `201` is different from `200`.
- Their parsing and serialization logic is not scattered everywhere.
- Their application startup is visible and predictable.
- They can explain where a validation rule lives and why.

Students do not need a perfect web architecture to succeed. They need a coherent one. Coherence is the standard.

### End-of-Day Instructor Wrap Script

**[Instructor speaks:]**

Today you transformed your capstone from a local application into a service that can be spoken to over HTTP. More importantly, you practiced an architectural habit that matters far beyond Flask: keep the boundaries honest. The route handles the request. The service handles the rules. The repository handles persistence. The serializer handles the outward shape. When those boundaries stay clear, the whole project becomes easier to reason about.

As learners leave, ask them to write down one route that feels clean and one route they still want to simplify. That reflection will help them tremendously in the security and client work coming next.

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
