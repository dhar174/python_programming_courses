# Advanced Day 4 — Session 4 (Hours 13–16)
Python Programming (Advanced) • HTTP Clients, Security Habits, Capstone Planning, and Checkpoint 2

---

# Session 4 Overview

## Topics Covered Today
- Hour 13: HTTP client work: `requests` + JSON contracts
- Hour 14: Security basics — environment variables, safe secrets habits, and hashing concepts
- Hour 15: Capstone planning workshop — scope, milestones, and delivery path
- Hour 16: Checkpoint 2 — persistence-ready core + JSON save/load

### Source Alignment
- `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md` → `## Session 4 overview`
- `Advanced/lessons/lecture/Day4_Hour1_Advanced.md` → `# Day 4, Hour 1: HTTP Client Work – requests + JSON Contracts`
- `Advanced/lessons/lecture/Day4_Hour2_Advanced.md` → `# Day 4, Hour 2: Security Basics – Environment Variables, Safe Secrets Habits, and Hashing Concepts`
- `Advanced/lessons/lecture/Day4_Hour3_Advanced.md` → `# Day 4, Hour 3: Capstone Planning Workshop – Scope, Milestones, and Delivery Path`
- `Advanced/lessons/lecture/Day4_Hour4_Advanced.md` → `# Day 4, Hour 4: Checkpoint 2 – Persistence-Ready Core + JSON Save/Load`

---

# Session 4 Outcomes

- Treat outside data as untrusted until checked
- Keep secrets out of source control
- Choose a realistic capstone path
- Deliver a persistence-ready core that can survive restart

---

# Scope Guardrails for Today

## In Scope
- HTTP client fundamentals
- JSON contract validation
- Environment-variable habits
- Concept-level hashing discussion
- Capstone MVP planning
- JSON persistence checkpoint

## Not Yet
- Production auth systems
- Full deployment workflows
- Enterprise schema tooling
- Database integration beyond persistence-ready design

---

# Hour 13: HTTP Client Work + JSON Contracts

## Learning Outcomes
- Send a `GET` request with `requests`
- Always set a timeout
- Use `raise_for_status()`
- Validate the JSON shape before trusting it

---

## Big Shift for This Hour

- Up to now, most data has lived inside our program
- Today the program talks to something outside itself
- Outside data may be:
  - slow
  - missing
  - malformed
  - structurally different from what we expected

---

## HTTP Client Fundamentals

- Client sends request
- Server sends response

### High-Level Pieces
- method
- URL
- optional params/headers/body
- status code
- response body

### Today
- mainly `GET`
- JSON responses

---

## Reliability Habits

- **Always set a timeout**
- Prefer `raise_for_status()`
- Catch failure categories cleanly:
  - timeout
  - connection problem
  - HTTP error
  - invalid JSON
  - contract mismatch

---

## JSON Is a Contract

### Check the Minimum Shape You Need
- payload type
- required keys
- expected value types

```python
response = requests.get(url, timeout=5)
response.raise_for_status()
data = response.json()
```

---

## Demo: Small Wrapper Function

```python
def fetch_task(url: str) -> dict:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict) or "title" not in data:
        raise ValueError("Response contract mismatch")
    return data
```

- Centralize request behavior
- Avoid copy/paste request logic everywhere

---

## Lab: API Consumer

**Time: 15–25 minutes**

### Tasks
- Send a `GET` request to a sample endpoint
- Use `timeout=...`
- Call `raise_for_status()`
- Parse JSON
- Validate required keys before use
- Show a friendly failure message for one error case

---

## Completion Criteria (Hour 13)

✓ Request uses a timeout  
✓ Happy path parses JSON safely  
✓ Failure handling is intentional  
✓ Contract validation happens before downstream use

---

## Homework + Quiz Emphasis (Hour 13)

- Homework framing:
  - **Goal:** client call that reads JSON safely and prints labeled checks
  - **Best practice:** check status codes and JSON keys
  - **Pitfall:** assuming every response has the shape you want
- Quiz/canonical contract marker:
  - `Hour 13 | request url: https://api.example.test/tasks`

### Source Alignment
- `Advanced/assignments/Advanced_Day4_homework.ipynb` → `## Part 1: Hour 13 - HTTP client work`
- `Advanced/quizzes/Advanced_Day4_Quiz.html` → `QUIZ_DATA` questions 1–5

---

## Common Pitfalls (Hour 13)

⚠️ No timeout  
⚠️ Parsing JSON before checking status  
⚠️ Trusting missing keys blindly  
⚠️ Returning raw error noise to end users

---

## Quick Check

**Question:** Why is "the service returned valid JSON" not the same as "the response matches our contract"?

---

# Hour 14: Security Basics

## Learning Outcomes
- Explain why secrets should not live in source files
- Load sensitive values from environment variables
- Distinguish hashing from encryption conceptually
- Keep this hour in appropriate scope

---

## Security Mindset Reset

- We are teaching **habits**, not full security engineering
- Good boundaries matter

### Not This Hour
- OAuth
- JWT flows
- production identity systems

### This Hour
- secret hygiene
- env vars
- `.env.example`
- hashing concept demo

---

## Hard-Coded Secrets Are a Trap

```python
ADMIN_KEY = "super-secret-real-key"
```

### Problems
1. Secrets end up in version control
2. Rotation becomes painful
3. Unsafe sharing habits spread
4. Commit history keeps the mistake around

---

## Environment Variable Pattern

```python
import os


def get_required_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value
```

- Code names what it needs
- Environment supplies the real value

---

## `.env.example` vs `.env`

```env
APP_API_KEY=your-api-key-here
APP_ADMIN_KEY=replace-with-local-admin-key
APP_ENV=development
```

- `.env.example` may be committed
- `.env` should usually be ignored
- placeholders only — never real secrets

---

## Hashing vs Encryption

- **Encryption** is meant to be reversible with the right key
- **Hashing** is meant to be one-way

### Classroom-Safe Demo Idea
- compute a digest
- compare digests
- do **not** claim this solves production auth

---

## Demo: Gated Admin Action

```python
import hashlib
import secrets


def sha256_digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


authorized = secrets.compare_digest(
    sha256_digest(expected_key),
    sha256_digest(provided_key),
)
```

---

## Lab: Secure-ish Configuration

**Time: 18–25 minutes**

### Tasks
- Read one required value from the environment
- Add a `.env.example` template plan
- Add `.gitignore` guidance for local secret files
- Gate one admin action using configuration, not a hard-coded literal

---

## Completion Criteria (Hour 14)

✓ Secret value is not hard-coded in the source  
✓ Missing env var fails clearly  
✓ Learner can explain hashing vs encryption at a high level  
✓ Scope stays disciplined and honest

---

## Homework + Quiz Emphasis (Hour 14)

- Homework framing:
  - **Goal:** secure config pattern that separates secrets from code
  - **Best practice:** read secrets from env vars, store only hashes when appropriate
  - **Pitfall:** checking secrets into source control
- Quiz/canonical contract marker:
  - `Hour 14 | secret source: environment variable`

### Source Alignment
- `Advanced/assignments/Advanced_Day4_homework.ipynb` → `## Part 2: Hour 14 - Security basics`
- `Advanced/quizzes/Advanced_Day4_Quiz.html` → `QUIZ_DATA` questions 6–10

---

## Common Pitfalls (Hour 14)

⚠️ Real secrets in demo files  
⚠️ Committing `.env`  
⚠️ Treating hashing and encryption as synonyms  
⚠️ Promising production-grade security from a classroom-safe example

---

## Quick Check

**Question:** Why is a `.env.example` helpful even though it contains no real secret values?

---

# Hour 15: Capstone Planning Workshop

## Learning Outcomes
- Lock an MVP scope
- Choose a delivery path
- Break the project into milestones
- Define "done" before the build gets bigger

---

## What This Workshop Is Really For

- Replace vague enthusiasm with a delivery plan
- Protect the project from scope drift
- Decide what proves value earliest

### Strong Planning Questions
- Who is the user?
- What is the primary workflow?
- What is the smallest useful version?

---

## Recommended Milestone Path

1. Core
2. Persistence
3. UI
4. Analytics
5. Tests
6. Package

- Do not jump to a flashy shell around unstable logic

---

## Definition of Done Examples

### Core
- service logic works in isolation

### Persistence
- data survives restart

### UI
- primary workflow works through the chosen surface

### Tests
- major business rules and failure paths have repeatable checks

---

## Delivery Path Decision

### GUI-First
- tangible demo quickly
- risk: logic hides in callbacks

### API-First
- clearer service boundaries
- risk: less visually exciting at first

### Non-Negotiable
- core logic still lives in reusable services

---

## Demo Artifact Shape

```text
capstone_project/
├── README.md
├── src/
├── tests/
└── data/
```

### README Needs
- project goal
- MVP features
- setup steps
- run steps

---

## Workshop: One-Page Capstone Plan

**Time: 20 minutes**

### Include
- chosen domain
- primary user workflow
- GUI-first or API-first decision
- milestone list
- persistence plan
- key risks
- test targets

---

## Completion Criteria (Hour 15)

✓ Scope is realistic  
✓ Delivery path is chosen and justified  
✓ Milestones are sequenced clearly  
✓ README skeleton or plan notes exist

---

## Homework + Quiz Emphasis (Hour 15)

- Homework framing:
  - **Goal:** milestone plan with one domain, one interface, and staged deliverables
  - **Best practice:** keep scope narrow enough to finish
  - **Pitfall:** trying to build every optional feature before core CRUD is stable
- Quiz/canonical contract marker:
  - `Hour 15 | chosen domain: tracker`

### Source Alignment
- `Advanced/assignments/Advanced_Day4_homework.ipynb` → `## Part 3: Hour 15 - Capstone planning workshop`
- `Advanced/quizzes/Advanced_Day4_Quiz.html` → `QUIZ_DATA` questions 11–15

---

## Common Pitfalls (Hour 15)

⚠️ Wish-list scope instead of MVP scope  
⚠️ README postponed until the final hour  
⚠️ UI selected before the core is stable  
⚠️ No persistence or test plan in the roadmap

---

## Quick Check

**Question:** Which milestone do students most often try to jump to too early, and why is that risky?

---

# Hour 16: Checkpoint 2 — Persistence-Ready Core

## Learning Outcomes
- Separate domain, service, and persistence responsibilities
- Save JSON using a safe-save pattern
- Load saved state back into application objects
- Handle missing files, invalid JSON, and validation failures cleanly

---

## What Checkpoint 2 Proves

- The core survives beyond one run
- The package layout under `src/` is intentional
- State can be saved and restored
- Logging captures meaningful persistence events
- Custom exceptions still communicate domain and persistence issues

---

## Sample Persistence-Ready Layout

```text
project_root/
├── demo_persistence.py
├── logs/app.log
├── data/state.json
└── src/reading_tracker/
    ├── errors.py
    ├── logging_config.py
    ├── models.py
    ├── persistence.py
    └── services.py
```

---

## Separation of Concerns

- **models.py** → structured domain data
- **services.py** → business rules
- **persistence.py** → JSON save/load
- **errors.py** → custom exceptions
- **logging_config.py** → file logging setup

### Why It Matters
- JSON today
- database later
- less rewiring when storage changes

---

## Demo: Safe Save + Load Shape

```python
class PersistenceError(Exception):
    pass


class JSONStateStore:
    def save(self, state):
        ...

    def load(self):
        ...
```

- save started
- save succeeded
- load started
- file missing handled
- invalid JSON handled

---

## Demo Workflow

### Save → Restart → Load
1. Create a few records
2. Save to JSON safely
3. Recreate the service/store
4. Load state back in
5. Confirm records still exist

---

## Hands-On Checkpoint Build

**Time: 15–25 minutes**

### Tasks
- Organize or confirm package layout
- Add a persistence layer
- Implement safe save behavior
- Load JSON back into objects
- Log the key events
- Demonstrate one failure case and one happy path

---

## Completion Criteria (Hour 16)

✓ Core state round-trips through JSON  
✓ Save path is safer than direct overwrite  
✓ Load handles missing/bad files intentionally  
✓ The project is visibly more persistence-ready than it was yesterday

---

## Homework + Quiz Emphasis (Hour 16)

- Homework framing:
  - **Goal:** core app that can add records and round-trip them through JSON
  - **Best practice:** checkpoint save/load before expanding the interface
  - **Pitfall:** delaying persistence checks until after major UI work
- Quiz/canonical contract marker:
  - `Hour 16 | checkpoint model: Task`

### Source Alignment
- `Advanced/assignments/Advanced_Day4_homework.ipynb` → `## Part 4: Hour 16 - Checkpoint 2`
- `Advanced/quizzes/Advanced_Day4_Quiz.html` → `QUIZ_DATA` questions 16–20

---

## Common Pitfalls (Hour 16)

⚠️ Dumping JSON logic everywhere instead of using a persistence layer  
⚠️ Direct overwrite with no safety net  
⚠️ Treating file absence as a crash-only situation  
⚠️ Adding more features before proving save/load works

---

## Quick Check

**Question:** If the app works beautifully in memory but loses state after restart, what milestone is still incomplete?

---

# Session 4 Wrap-Up

## What We Locked In Today
- Reliable HTTP client habits
- Safer secret/config practices
- A concrete capstone roadmap
- Persistence-ready core architecture

### Key Rule
**Trustworthy software plans for failure, scope, and restart behavior.**

---

## Day 4 Homework / Study Checklist

- Re-run the HTTP wrapper with a failure case in mind
- Remove any hard-coded secret from demo code
- Finalize the one-page capstone plan
- Test save -> load round-trip behavior
- Match the canonical output labels expected by the notebook

### Source Alignment
- `Advanced/assignments/Advanced_Day4_homework.ipynb` → `## Submission Checklist`

---

## Next Step Framing

### After Session 4
- keep the core stable
- preserve scope discipline
- carry forward logging and safe-save habits
- use the capstone plan as the default decision filter

---

# Thank You!

Validate outside data.  
Keep secrets out of source.  
Plan the MVP.  
Prove persistence before expanding.
