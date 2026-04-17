# Advanced Day 9 — Session 9 (Hours 33–36)
Python Programming (Advanced) • REST APIs and Flask Foundations

---

# Session 9 Overview

## Topics Covered Today
- Hour 33: REST fundamentals + Flask app setup
- Hour 34: CRUD endpoints for the main resource
- Hour 35: Serialization + validation
- Hour 36: App structure + dependency wiring

## Capstone Through-Line
- Expose the existing tracker logic through a Flask API
- Keep the service layer as the center of truth
- Build for maintainability, not framework novelty

---

# Alignment Sources

- Runbook: `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md` → Session 9 overview; Hours 33–36
- Lecture: `Advanced/lessons/lecture/Day9_Hour1_Advanced.md` through `Day9_Hour4_Advanced.md`
- Homework: `Advanced/assignments/Advanced_Day9_homework.ipynb`
- Quiz: `Advanced/quizzes/Advanced_Day9_Quiz.html`

## Today’s Output Target
- A working Flask surface over the tracker project
- Predictable JSON responses
- A structure that can keep growing tomorrow

---

# Session Success Criteria

- `/health` responds with JSON
- Main resource supports CRUD behavior
- Error responses use one consistent JSON shape
- Write-ready app structure uses explicit dependency wiring
- Homework and quiz checkpoints are visible in the day’s build flow

---

# Scope Guardrails for Today

- Stay in course scope: Flask + clean contracts + practical structure
- Do **not** drift into deployment, OAuth, JWT, or API versioning
- Reuse service and repository logic instead of rebuilding business rules in routes
- Choose one resource name and keep it consistent in your own project

---

# Hour 33: REST Fundamentals + Flask App Setup

## Learning Outcomes
- Explain REST-style resources in plain language
- Distinguish `GET` from `POST`
- Create a minimal Flask app
- Return JSON instead of default HTML errors

---

## Why an API Matters Now

- The capstone already has logic and persistence
- Flask becomes a **new interface**, not a new project
- An API lets other tools call the same application behavior
- Strong layering now makes later integration easier

```text
Client -> Flask route -> service -> repository -> SQLite
```

---

## REST in Plain English

- **Resource**: the thing the API exposes
- **Route**: URL pattern connected to code
- **Method**: `GET`, `POST`, `PUT`, `DELETE`
- **Status code**: fast signal of what happened
- **JSON contract**: predictable request/response shape

## Useful Day 9 status codes
- `200` success
- `201` created
- `400` bad input
- `404` missing resource
- `500` unexpected failure

---

## Minimal Flask Starter

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify({"status": "ok"})
```

## Teaching point
- Start with one honest route before adding CRUD

---

## Consistent Error Contract

```json
{
  "error": {
    "code": "not_found",
    "message": "Record 12 was not found.",
    "request_id": "a1b2c3d4"
  }
}
```

## Why it matters
- Clients can depend on one structure
- Logs and user-facing errors connect more cleanly

---

## Demo Flow: Hour 33

1. Create `app = Flask(__name__)`
2. Add `/health`
3. Run the server locally
4. Test with browser, `curl`, or a small Python call
5. Trigger one intentional failure and show JSON output

---

## Lab: Flask Starter + Smoke Test

**Time: 25–35 minutes**

### Tasks
- Create a small Flask app
- Add `/health`
- Return JSON on success
- Add one reusable error helper
- Verify the app from outside the Flask file

### Completion Criteria
- App starts reliably
- `/health` returns JSON
- Learner can explain what a route does

---

## Common Pitfalls (Hour 33)

⚠️ Mixing setup, routing, and service logic in one giant file  
⚠️ Returning HTML errors while success paths return JSON  
⚠️ Treating the API as a separate project instead of a new interface

---

## Homework + Quiz Emphasis (Hour 33)

- Homework goal: build a Flask app with a health route and clear REST basics
- Best practice: start with one small health endpoint before layering CRUD
- Quiz-ready anchor: `Hour 33 | framework: Flask`
- Deliverable check: can you show a health route and explain why it matters?

---

## Quick Check

**Question**: Why is a health endpoint a smart first step before building CRUD routes?

---

# Hour 34: CRUD Endpoints for the Main Resource

## Learning Outcomes
- Implement `GET`, `POST`, `PUT`, and `DELETE`
- Keep routes thin
- Connect handlers to the service layer
- Return the right status codes for the outcome

---

## Canonical Route Set

- `GET /records`
- `POST /records`
- `GET /records/<id>`
- `PUT /records/<id>`
- `DELETE /records/<id>`

## Naming note
- Lecture examples use `records`
- Homework/quiz output anchors may use `tasks`
- Your project should pick **one** resource name and stay consistent

---

## Thin Route Handler Mindset

### Route responsibilities
- Read request input
- Call the service
- Catch known exceptions
- Return JSON + status code

### Avoid in the route
- Direct SQL
- Deep business logic
- Hidden global state

---

## Safe JSON Parsing Pattern

```python
payload = request.get_json(silent=True)
if payload is None:
    return error_response(
        "invalid_json",
        "Request body must be valid JSON.",
        400,
    )
```

## Key distinction
- Bad input → `400`
- Missing resource → `404`

---

## CRUD Example

```python
@app.post("/records")
def create_record():
    payload = request.get_json(silent=True)
    if payload is None:
        return error_response("invalid_json", "Request body must be valid JSON.", 400)

    record = service.add_record(
        title=payload.get("title", ""),
        category=payload.get("category", ""),
        status=payload.get("status", "open"),
    )
    return jsonify(record.to_dict()), 201
```

---

## Demo Flow: Hour 34

1. Add list + create routes
2. Add get-by-id
3. Add update + delete
4. Show one success case
5. Show one validation or not-found case

## Smoke test habit
- Verify behavior from outside the Flask app

---

## Lab: Build the CRUD Surface

**Time: 25–35 minutes**

### Tasks
- Add the full CRUD route set
- Route everything through the service layer
- Return consistent JSON
- Test at least one success and one failure for each major path

### Completion Criteria
- CRUD endpoints respond predictably
- Status codes match the actual outcome
- Learner can explain `400` vs `404`

---

## Common Pitfalls (Hour 34)

⚠️ Returning `200` for everything  
⚠️ Writing business rules in Flask handlers  
⚠️ Forgetting to test malformed requests  
⚠️ Letting route names drift between files

---

## Homework + Quiz Emphasis (Hour 34)

- Homework goal: a small set of CRUD endpoints for the tracker resource
- Best practice: use HTTP verbs and status codes consistently
- Pitfall to avoid: wrong status codes make clients harder to trust
- Quiz-ready anchor: `Hour 34 | endpoint: POST /tasks`

---

## Quick Check

**Question**: When should a route return `400` instead of `404`?

---

# Hour 35: Serialization + Validation

## Learning Outcomes
- Centralize request parsing
- Centralize response serialization
- Keep validation rules coherent
- Use intentional negative cases to test the contract

---

## API Contracts Are Promises

- Requests should arrive in a predictable shape
- Responses should leave in a predictable shape
- Failure paths should look consistent too
- “It works” is not enough if every endpoint behaves differently

---

## Serializer Helper

```python
def serialize_record(record) -> dict:
    return {
        "id": record.id,
        "title": record.title,
        "category": record.category,
        "status": record.status,
        "priority": record.priority,
    }
```

## Benefit
- One change point instead of copy/paste edits across routes

---

## Parser + Validation Helper

```python
def parse_record_payload(payload: dict) -> dict:
    title = str(payload.get("title", "")).strip()
    category = str(payload.get("category", "")).strip()
    status = str(payload.get("status", "open")).strip().lower()

    if not title:
        raise ValidationError("Title is required.")
    if not category:
        raise ValidationError("Category is required.")
    if status not in {"open", "in_progress", "done"}:
        raise ValidationError("Status is invalid.")

    return {"title": title, "category": category, "status": status}
```

---

## Where Validation Should Live

- Parser helpers normalize and reject malformed payloads
- Service layer enforces domain invariants
- Routes should **not** duplicate the same rules repeatedly

## Negative test ideas
- invalid JSON
- missing title
- missing category
- invalid status value

---

## Cleaner Route Pattern

```python
@app.post("/records")
def create_record():
    payload = request.get_json(silent=True)
    if payload is None:
        return error_response("invalid_json", "Request body must be valid JSON.", 400)

    try:
        parsed = parse_record_payload(payload)
        record = service.add_record(**parsed)
    except ValidationError as exc:
        return error_response("validation_error", str(exc), 400)

    return jsonify(serialize_record(record)), 201
```

---

## Lab: Make the API Coherent

**Time: 25–35 minutes**

### Tasks
- Add one serializer helper
- Add one parser/validator helper
- Replace ad hoc route logic with helpers
- Run a few negative cases intentionally

### Completion Criteria
- Output shape is consistent across routes
- Validation rules live in one obvious place
- Learner can explain at least one negative test result

---

## Common Pitfalls (Hour 35)

⚠️ Different key sets across endpoints  
⚠️ Validation logic duplicated in multiple routes  
⚠️ Plain-text errors in one handler and JSON in another  
⚠️ Negative cases never tested until demo time

---

## Homework + Quiz Emphasis (Hour 35)

- Homework goal: manual serializers and validators for tracker payloads
- Best practice: one consistent request/response contract
- Pitfall to avoid: different key sets confuse clients
- Quiz-ready anchor: `Hour 35 | request fields checked: title, priority`

---

## Quick Check

**Question**: Why is centralizing parsing and serialization safer than rebuilding dictionaries inside each route?

---

# Hour 36: App Structure + Dependency Wiring

## Learning Outcomes
- Explain why growing apps need structure
- Refactor toward a `create_app()` pattern
- Wire dependencies explicitly
- Avoid circular imports and hidden globals

---

## When Structure Starts to Matter

- Single-file apps are great for learning
- Growth creates import noise and setup confusion
- Testing gets harder when construction happens at import time
- Clear startup makes the app easier to reason about

---

## Simple Application Factory

```python
def create_app():
    app = Flask(__name__)
    repo = SQLiteTrackerRepository("data/tracker.db")
    repo.init_db()
    service = TrackerService(repo=repo)
    register_routes(app, service)
    return app
```

## Why it helps
- One visible startup path
- Explicit dependencies
- Easier testing later

---

## Structure Options for This Course

### Minimum good structure
- `api/app.py` for startup
- `api/routes.py` for route registration
- service + repository modules stay separate

### Optional structure
- Flask blueprints if the learner is ready

## Guardrail
- Do not overframework the capstone

---

## Common Architecture Risks

- Global service creation at import time
- `routes.py` importing `app.py` and vice versa
- Repository construction hidden in random modules
- Learners changing file layout without updating imports deliberately

---

## Refactor Sprint

**Time: 25–35 minutes**

### Tasks
- Move routes into a dedicated module or grouping
- Add `create_app()`
- Construct repository + service in one clear place
- Re-test `/health` and main resource routes

### Completion Criteria
- Startup is predictable
- Route wiring is readable
- API still behaves the same after refactor

---

## Common Pitfalls (Hour 36)

⚠️ Circular imports  
⚠️ Hidden global singletons  
⚠️ Refactoring too much at once  
⚠️ Losing a working route while reorganizing

---

## Homework + Quiz Emphasis (Hour 36)

- Homework goal: an app structure that can grow beyond one file
- Best practice: use an app factory and optional blueprints to organize startup
- Pitfall to avoid: global singletons hide dependencies and hurt testing
- Quiz-ready anchor: `Hour 36 | app factory: create_app`

---

## Quick Check

**Question**: What problem does `create_app()` solve that a global `service = ...` pattern does not?

---

# Day 9 Wrap-Up

## What Learners Should Leave With
- A Flask entry point
- CRUD routes around one main resource
- Manual parser + serializer helpers
- A maintainable startup path for tomorrow’s security and client work

---

## Homework Focus

- Build deterministic outputs in `Advanced_Day9_homework.ipynb`
- Keep the contract stable enough for autograder-style labels
- Rehearse the hour anchors:
  - `framework: Flask`
  - `endpoint: POST /tasks`
  - `request fields checked: title, priority`
  - `app factory: create_app`

---

## Exit Ticket

1. Which route feels strongest right now?
2. Which failure case still needs testing?
3. What part of your API structure will make tomorrow easier?

---

# Looking Ahead

## Next Session
- Protect write routes with an API key
- Build a Python client
- Choose an integration path
- Demo the API milestone confidently
