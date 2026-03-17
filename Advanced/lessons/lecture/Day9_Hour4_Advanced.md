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

## Shared Day 9 Instructor Reference

Reuse the shared day-level instructor support from `Day9_Hour1_Advanced.md` for this hour's facilitation details:

- `## Instructor Coaching Appendix`
- `## Facilitation Toolkit`

This keeps the Day 9 coaching guidance in one maintained location while preserving this file's hour-specific lecture script.
