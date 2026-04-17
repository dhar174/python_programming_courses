# Advanced Day 10 — Session 10 (Hours 37–40)
Python Programming (Advanced) • API Security, Clients, and Milestone Demo

---

# Session 10 Overview

## Topics Covered Today
- Hour 37: API security basics with an API key gate
- Hour 38: Consuming your own API with Python client functions
- Hour 39: Integration choice — GUI to API or parallel UI/API
- Hour 40: Checkpoint 5 API milestone demo

## Day Goal
- Move from “API exists” to “API is controlled, usable, and demo-ready”

---

# Alignment Sources

- Runbook: `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md` → Session 10 overview; Hours 37–40
- Lecture: `Advanced/lessons/lecture/Day10_Hour1_Advanced.md` through `Day10_Hour4_Advanced.md`
- Homework: `Advanced/assignments/Advanced_Day10_homework.ipynb`
- Quiz: `Advanced/quizzes/Advanced_Day10_Quiz.html`

## Session Theme
- Protect the write surface
- Use the API from the outside
- Choose an integration path intentionally
- Stabilize for checkpoint evidence

---

# Session Success Criteria

- Write routes require an API key
- Client calls use timeouts and predictable error handling
- The project has a clear integration story
- Checkpoint 5 shows health, CRUD, protection, and architecture explanation

---

# Scope Guardrails for Today

- This is **not** full authentication or identity management
- API keys live in configuration, not source control
- Choose the architecture that best protects the milestone
- Stabilize before adding extra features

---

# Hour 37: API Security Basics

## Learning Outcomes
- Explain why writes need stronger protection than reads
- Load a key from configuration
- Require `X-API-Key` on `POST`, `PUT`, and `DELETE`
- Return clear `401` and `403` responses

---

## Security Framing Without Panic

- We are adding a **course-level gate**
- We are **not** building OAuth, JWT, or full auth systems
- The lesson is about:
  - safer configuration
  - boundary checks
  - consistent failure responses

## Rule of thumb
- Reads may be open
- Writes deserve protection

---

## What an API Key Is — and Is Not

- A shared secret checked at the HTTP boundary
- Good enough for course-level protection of write operations
- **Not** a user identity system
- **Not** a replacement for a production auth stack

---

## Keep the Secret Out of Source

```python
import os

API_KEY = os.getenv("TRACKER_API_KEY", "")
```

## Safe handling habits
- Do not hard-code the key
- Do not commit real values
- `.env.example` may hold placeholders only
- Do not log the actual secret

---

## Header + Status Code Pattern

### Client sends
```text
X-API-Key: <value>
```

### Server responds
- `401` when the key is missing
- `403` when the key is present but wrong

## Key habit
- Pick a rule and apply it consistently

---

## Guard Helper Example

```python
def require_api_key():
    provided = request.headers.get("X-API-Key", "")

    if not provided:
        return error_response("missing_api_key", "API key is required.", 401)

    if not API_KEY or not hmac.compare_digest(provided, API_KEY):
        return error_response("invalid_api_key", "API key is invalid.", 403)

    return None
```

---

## Demo Flow: Hour 37

1. Read the key from config
2. Add the helper
3. Protect write routes
4. Test three cases:
   - no key
   - wrong key
   - correct key

## Teaching point
- Security work is incomplete until the failure cases are tested

---

## Lab: Protect the Write Surface

**Time: 25–35 minutes**

### Tasks
- Load the key from configuration
- Protect `POST`, `PUT`, and `DELETE`
- Return structured auth failures
- Add placeholder documentation for secret setup

### Completion Criteria
- Every write route is protected
- Auth failures still use JSON
- Learner can explain why the service layer stays header-free

---

## Common Pitfalls (Hour 37)

⚠️ Hard-coding the key  
⚠️ Protecting some write routes but forgetting one  
⚠️ Logging the real secret  
⚠️ Treating missing and wrong keys as the same case without intention

---

## Homework + Quiz Emphasis (Hour 37)

- Homework goal: a simple API key check around write operations
- Best practice: environment-based key in course scope
- Pitfall to avoid: hard-coded credentials in source or logs
- Quiz-ready anchor: `Hour 37 | protected route: POST /tasks`

---

## Quick Check

**Question**: Why should the API key check live in the route layer instead of inside the service layer?

---

# Hour 38: Consuming Your Own API

## Learning Outcomes
- Write small client functions
- Set request timeouts
- Pass auth headers for protected operations
- Turn server-side failures into readable client feedback

---

## Why Become Your Own Client?

- An API can feel fine from the inside but awkward from the outside
- Client code reveals:
  - confusing contracts
  - inconsistent errors
  - missing timeouts
  - unreliable route behavior

## Healthy mindset
- Let the API prove itself from the consumer’s side

---

## Shape of a Simple Client Module

- Keep it flat and readable
- Each function should:
  - build the URL
  - send the request
  - set a timeout
  - handle errors predictably
  - return parsed JSON or a small mapped result

---

## Timeout + Header Pattern

```python
import requests

def create_record(payload: dict, api_key: str) -> dict:
    response = requests.post(
        f"{BASE_URL}/records",
        json=payload,
        headers={"X-API-Key": api_key},
        timeout=5,
    )
    response.raise_for_status()
    return response.json()
```

## Habit to keep
- Never let requests hang indefinitely

---

## Friendly Error Handling

```python
def safe_create_record(payload: dict, api_key: str):
    try:
        return create_record(payload, api_key)
    except requests.Timeout:
        print("The API request timed out.")
    except requests.HTTPError as exc:
        print(f"Request failed: {exc}")
    return None
```

## Teaching point
- The client should help the user understand what failed

---

## Lab: Build the Client Module

**Time: 25–35 minutes**

### Required functions
- `list_records`
- `create_record`
- `update_record`
- `delete_record`

### Completion Criteria
- Timeout is visible in each request path
- Write operations pass the header
- Learner can explain the difference between timeout and validation failure

---

## Common Pitfalls (Hour 38)

⚠️ No timeout  
⚠️ Forgetting headers on `PUT` or `DELETE`  
⚠️ Copy-pasting base URLs everywhere  
⚠️ Swallowing errors with no visible message

---

## Homework + Quiz Emphasis (Hour 38)

- Homework goal: a reusable Python client for the tracker API
- Best practice: wrap requests in small client functions
- Pitfall to avoid: raw requests calls scattered everywhere
- Quiz-ready anchor: `Hour 38 | client base url: http://localhost:5000`

---

## Quick Check

**Question**: What problem does `timeout=5` solve that a successful happy-path demo might hide?

---

# Hour 39: Integration Choice

## Learning Outcomes
- Describe two valid integration patterns
- Choose the safer path for the current project state
- Prove the system stays coherent
- Explain tradeoffs clearly

---

## Two Valid Paths

### Option A: GUI talks to API
```text
GUI -> client functions -> API -> service -> repository -> database
```

### Option B: Parallel GUI and API
```text
GUI -> service -> repository -> database
API -> service -> repository -> database
```

## Important
- Both are valid in this course

---

## Option A: GUI to API

### Benefits
- One outward-facing contract
- GUI exercises the same HTTP behavior as other clients
- Good practice for decoupled systems

### Tradeoffs
- More moving parts
- More failure points
- GUI must handle network-style issues

---

## Option B: Parallel GUI and API

### Benefits
- Faster to stabilize
- Lower integration friction
- Still demonstrates architecture reuse

### Tradeoffs
- GUI does not exercise the HTTP contract directly
- Fields and behavior can drift if discipline slips

---

## How to Choose Well

- If the API and client are stable, Option A is reasonable
- If the project still feels shaky, Option B often protects the milestone better
- Choosing the safer path is a **professional decision**, not a weaker one

---

## Integration Sprint

**Time: 25–35 minutes**

### Tasks
- Choose Option A or B intentionally
- Document the choice briefly
- Prove both surfaces touch the same underlying data
- Fix at least one mismatch if it appears

### Completion Criteria
- The architecture choice is explicit
- The system still looks like **one** application

---

## Common Pitfalls (Hour 39)

⚠️ GUI and API using different field names  
⚠️ Stale GUI data after writes  
⚠️ Accidentally creating two database files  
⚠️ Drifting into a hybrid design nobody can explain

---

## Homework + Quiz Emphasis (Hour 39)

- Homework goal: an integration story that connects the interface to the API cleanly
- Best practice: pick one path and document the communication flow
- Pitfall to avoid: parallel flows without a clear source of truth
- Quiz-ready anchor: `Hour 39 | chosen path: gui talks to api`

---

## Quick Check

**Question**: When would Option B be the smarter choice even if Option A feels more impressive?

---

# Hour 40: Checkpoint 5 — API Milestone Demo

## Learning Outcomes
- Demonstrate a working API backed by SQLite
- Show security and error handling in action
- Explain the layer connections
- Identify the weakest part of the milestone honestly

---

## What Counts as Success

- Flask API with CRUD routes
- SQLite-backed persistence
- Consistent JSON errors
- API key protection on write operations
- Optional Python client if available

## Reminder
- Today rewards stability more than feature count

---

## Fast-Grade Demo Sequence

1. `GET /health`
2. `GET /records`
3. `POST /records` with valid key
4. `PUT /records/<id>` with valid key
5. `DELETE /records/<id>` with valid key
6. one missing or invalid key failure
7. one invalid input or not-found failure

---

## Stabilization Checklist

```text
[ ] API starts reliably
[ ] /health returns JSON
[ ] Create returns 201
[ ] Update returns 200
[ ] Delete returns 200
[ ] Invalid input returns 400 JSON
[ ] Missing/wrong key returns 401/403 JSON
[ ] Data persists in SQLite
```

---

## Rehearsal Mindset

- Confirm payloads before demo time
- Confirm headers before demo time
- Confirm database path before demo time
- Reproduce failures intentionally
- Fix the weakest route first

## Scope guardrail
- Stabilize before adding any “nice-to-have” endpoint

---

## Common Failure Modes

⚠️ HTML error page instead of JSON  
⚠️ One write route forgot the API key check  
⚠️ Service exceptions leaking uncaught  
⚠️ Payload shape not matching parser rules  
⚠️ Different database paths in different environments

---

## Showcase Prompt

- Show one healthy path
- Show one protected failure
- Explain the architecture in one minute
- Name the most fragile part honestly

## Good demo standard
- believable
- repeatable
- explainable

---

## Homework + Quiz Emphasis (Hour 40)

- Homework goal: a checkpoint demo showing the secured API and client path
- Best practice: checkpoint the full request flow from caller to response
- Pitfall to avoid: proving only one endpoint and calling it a milestone
- Quiz-ready anchor: `Hour 40 | api demo health: ok`

---

## Quick Check

**Question**: What makes an API milestone feel maintainable, not just functional?

---

# Day 10 Wrap-Up

## End-of-Day Evidence
- Key-based protection is working
- Client code can consume the API safely
- Integration choice is deliberate
- Checkpoint 5 can be demoed without guesswork

---

## Homework Focus

- Keep output deterministic in `Advanced_Day10_homework.ipynb`
- Rehearse the anchor lines:
  - `protected route: POST /tasks`
  - `client base url: http://localhost:5000`
  - `chosen path: gui talks to api`
  - `api demo health: ok`

---

## Exit Ticket

1. Which endpoint is strongest in your demo flow?
2. What did the client reveal about your API?
3. Which architecture choice did you make — and why?

---

# Looking Ahead

## Next Session
- Turn stored data into summaries
- Build report-ready charts
- Try a limited regression workflow or fallback analysis
- Add analytics as a real capstone feature
