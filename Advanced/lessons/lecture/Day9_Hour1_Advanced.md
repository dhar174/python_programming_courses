# Day 9, Hour 1: REST fundamentals + Flask app setup

**Python Programming Advanced - Session 9**
**Runbook alignment:** Session 9, Hour 33
**Capstone theme:** Full-stack Tracker with models, services, repositories, SQLite, Flask API, optional GUI/API integration, reports, pytest, and packaging.

## 60-minute Timing Overview

| Minutes | Activity | Instructor intent |
| --- | --- | --- |
| 0-5 | Welcome, recap, and outcome framing | Connect this hour to the previous capstone layer and name the deliverable. |
| 5-17 | Concept briefing and vocabulary | Teach the ideas learners need before touching code. |
| 17-35 | Live demo with happy and sad paths | Model careful implementation, prediction, and debugging. |
| 35-50 | Guided lab / build time | Learners implement the hour milestone in their own capstone. |
| 50-56 | Debrief and troubleshooting clinic | Surface common mistakes and reinforce contracts. |
| 56-60 | Quick check / exit ticket | Verify readiness for the next hour. |

## Learning Outcomes

By the end of this hour, learners will be able to:

- Create a small Flask application with a reliable health endpoint.
- Explain resources, HTTP verbs, status codes, and JSON response contracts.
- Use one consistent JSON error shape for every sad path.

## Instructor Prep Notes

- Confirm learners are in the correct project folder and virtual environment.
- Keep the authoritative runbook open to Session 9, Hour 33; this script expands that hour into a near-verbatim delivery guide.
- Use Python 3.11+ conventions: clear type hints, f-strings, `pathlib` for paths, context managers for resources, and small functions with one responsibility.
- Use the tracker capstone vocabulary consistently: model objects express domain data, services enforce workflow rules, repositories handle SQLite persistence, Flask routes expose JSON contracts, and reports/tests/packaging prove the app can be delivered.
- For API-related examples, keep this error contract visible on the board:

```json
{
  "error": {
    "code": "validation_error",
    "message": "name is required",
    "request_id": "..."
  }
}
```

## Opening Script (0-5 minutes)

**[Instructor speaks:]**
"Welcome back. In the previous parts of the advanced course, we built a layered tracker: domain model, service layer, repository, and persistence. Today we keep turning that code into a deliverable system. This hour is not about memorizing syntax. It is about making a design choice, proving it with code, and leaving the project easier to test and maintain."

*(Action: Ask learners to open the project and run the last known-good command. For API hours, that may be `flask run` or `python -m api.app`; for analytics it may be a report script; for testing it may be `pytest -q`.)*

**[Instructor speaks:]**
"Before we add anything, we want a baseline. If your project does not run at the start of the hour, adding a feature will make debugging harder. Run the smallest command that proves your project is alive. If it fails, write down the first error line and do not start editing yet."

### Bridge from prior work

- The tracker already has a model/service/repository shape from earlier sessions.
- SQLite remains the source of truth for persisted records.
- This hour adds or strengthens the outer layer: API behavior, client integration, analytics, tests, packaging, or final delivery.
- The class norm is still: make one small change, run it, observe the result, then continue.

## Concept Briefing (5-17 minutes)

**[Instructor speaks:]**
"Here are the ideas I want you to listen for during the demo. First, where does this responsibility belong? Second, what is the happy path? Third, what is the sad path? Fourth, how will another person know how to use or verify it? Advanced Python is less about clever lines of code and more about reliable boundaries."

### Talk points

- REST is not magic; it is a convention for naming resources and using HTTP methods predictably.
- Routes should translate HTTP details into service calls, not contain all business rules.
- A health endpoint is the simplest production habit: it proves the process is up before we test deeper behavior.
- Every error should return JSON, never a surprise HTML traceback.

### Why this matters in real projects

**[Instructor speaks:]**
"Real teams spend a surprising amount of time at boundaries: the boundary between a GUI and a service, an API and a client, a CSV and a DataFrame, or a test and the system under test. Bugs often appear where assumptions cross those boundaries. If we make contracts explicit, the next developer can reason about the program without reading every line."

Use these prompts to keep the class active:

- "What do you expect this function to return on success?"
- "What should happen if the input is missing, malformed, or points to a record that does not exist?"
- "Which layer should know about this detail?"
- "How could we test this without clicking through the whole application?"

## Live Demo (17-35 minutes)

**[Instructor speaks:]**
"I am going to demo this in small slices. Please do not copy yet. First, predict what should happen. Then I will run it. Then we will decide whether the result matches the contract. After that, I will pause so you can implement the same pattern in your project."

### Demo steps

1. Show the project folders: api/, src/, tests/, data/, reports/.
2. Create a Flask app with /health returning {status: ok}.
3. Add error_response(code, message, status) with a request_id.
4. Call /health, then intentionally call a missing route or failing route and discuss the JSON error.

### Demo code or command sketch

```python
from __future__ import annotations

from uuid import uuid4
from flask import Flask, jsonify


def error_response(code: str, message: str, status: int):
    payload = {"error": {"code": code, "message": message, "request_id": str(uuid4())}}
    return jsonify(payload), status


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok", "service": "tracker-api"})

    @app.errorhandler(404)
    def not_found(_error):
        return error_response("not_found", "Route not found", 404)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

```

### Demo narration guide

**[Instructor speaks:]**
"Notice that I am not starting with the biggest possible version. I am building a thin vertical slice. A thin slice is one small feature that crosses the layers we need: input, service behavior, persistence or data handling if relevant, and a visible result. Once that slice is correct, the next route, chart, test, or packaging step is easier."

*(Action: Run the code or command once for a happy path. Ask: "What proves this worked?")*

**[Instructor speaks:]**
"Now we need a sad path. A feature is not done just because the perfect input worked. I am going to send bad input, omit a required value, use a missing id, stop the server, or run from a clean environment depending on the hour. The goal is not to embarrass the code; the goal is to define how the program behaves when reality is messy."

*(Action: Trigger the sad path deliberately. For API work, show JSON errors. For pandas and reports, show a missing file or bad column and discuss the message. For tests, show a failing assertion and read it carefully.)*

### Instructor checkpoints during the demo

- Ask learners to identify the layer being edited.
- Ask whether the code is using project-safe paths rather than machine-specific paths.
- Ask what a reviewer would need in order to reproduce the result.
- Ask what test or manual check would catch a regression later.

## Guided Practice (35-40 minutes)

**[Instructor speaks:]**
"Now you will implement the same idea, but keep the scope narrow. Do not redesign your whole capstone. Pick the smallest slice that satisfies the hour outcome. If you finish early, use the optional extensions; do not start an unrelated rewrite."

Suggested instructor circulation questions:

1. "Show me the file you are editing and tell me why this responsibility belongs there."
2. "What is your first happy-path command?"
3. "What is your first sad-path command?"
4. "If I review this tomorrow, where is the contract documented?"
5. "What would you test automatically if you had ten more minutes?"

## Hands-on Lab (40-50 minutes)

### Lab prompt

Flask starter: learners create api/app.py, run the app, test /health in a browser or with curl, and record one happy-path response plus one JSON error response.

### Required learner workflow

1. Start from a known-good run.
2. Make one small implementation change.
3. Run the narrowest check possible.
4. Add the happy-path proof.
5. Add one sad-path proof.
6. Commit or save the working state before attempting an extension.

### Completion criteria

- /health returns JSON with status ok.
- At least one error path returns the shared error contract.
- Learner can explain GET vs POST and why 201 is used for create.

## Debrief and Troubleshooting (50-56 minutes)

**[Instructor speaks:]**
"Let us collect what we learned. I want one example of a happy path, one example of a sad path, and one example of a design boundary that became clearer. If your code is not fully working yet, you can still contribute by naming the exact symptom and the next diagnostic step."

### Common pitfalls to watch for

- Port already in use; choose a different port rather than restarting the whole lab.
- Debug mode exposes tracebacks; helpful locally, inappropriate as an API contract.
- Returning plain strings makes clients harder to write.

### Debugging script for stuck learners

Use this sequence aloud when helping a learner:

1. "Read the first meaningful error message, not the last line only."
2. "What command produced it? Can we reproduce it?"
3. "What changed since the last working run?"
4. "Can we test the service or helper function without the outer UI/API/report layer?"
5. "What is the smallest rollback or fix that restores a working state?"

## Optional Extensions

If learners meet the completion criteria early, offer one of these stretch goals:

- Add /version from a constant.
- Log the request_id before returning errors.
- Add a tiny smoke test for /health using Flask test_client().

Remind learners that optional work must not break the required slice. A polished required feature is better than three unfinished experiments.

## Quick Checks and Exit Ticket (56-60 minutes)

Ask learners to answer individually, then discuss two or three responses:

- What HTTP status code fits a successful create, and why is it not just 200?
- What is the happy path you proved this hour?
- What sad path did you test or plan to test next?
- Which file or module is now most important for the next hour?

**[Instructor speaks:]**
"Your exit ticket is a sentence, not an essay: name what works, name what still needs attention, and name your next command. That habit will keep your capstone moving as the system gets larger."

## Instructor Wrap-up Notes

- Reinforce the capstone through-line: each hour should leave behind a runnable artifact, not just notes.
- Encourage frequent commits with messages such as `feat: add records endpoint`, `test: cover validation errors`, or `docs: add report quickstart`.
- If multiple learners are blocked by the same issue, pause the room and debug one shared example rather than repeating the same fix individually.
- Keep advanced scope boundaries: do not detour into production OAuth, complex ORMs, elaborate front-end frameworks, or advanced machine learning unless the runbook marks the topic as optional.


## Expanded Facilitation Notes for a Full 60-Minute Delivery

Use this section when the class needs more structure, when learners are unevenly paced, or when you want a more detailed speaking guide than the core hour script above. It is intentionally written as an instructor companion rather than a student handout.

### Board plan and vocabulary anchor

At the start of the hour, reserve one side of the board for the capstone architecture and leave it visible. Draw the same four boxes every time: interface, service, repository, and data or artifact. For API hours, the interface is Flask routes and JSON. For client or GUI integration hours, the interface may be a Tkinter callback or a Python client object. For analytics hours, the artifact is a CSV, summary file, chart, or report. For testing and packaging hours, the artifact is evidence that the project can be verified and run by another person.

**[Instructor speaks:]**
"The box we edit today is important, but the boundaries between boxes are even more important. If we keep the boundary clean, we can swap a GUI for an API, replace manual checks with pytest, or generate a report without rewriting the domain model."

Use these vocabulary checks during the first ten minutes:

- A model represents the domain data and rules that belong with the data.
- A service coordinates use cases and raises meaningful domain exceptions.
- A repository hides SQLite details and returns domain objects or simple records.
- An API route translates HTTP into service calls and translates results back to JSON.
- A client translates Python function calls into HTTP requests and translates responses into useful Python values.
- A report pipeline turns persisted data into repeatable artifacts that can be reviewed.
- A test is executable evidence about expected behavior.
- A package or deliverable is successful only when another person can install and run it from instructions.

### Instructor pacing detail

If learners are new to this topic, spend extra time on prediction before execution. Before every run, ask, "What status code, file, chart, exception, or test result do we expect?" Prediction forces learners to state the contract. If the result differs, the class has a concrete debugging target.

If learners are moving quickly, shorten the lecture and lengthen the lab, but keep the same quality gates: happy path, sad path, readable code, and a repeatable command. Do not let the hour become a feature race. A learner who can explain one clean vertical slice is better prepared than a learner with five partial features.

Suggested minute-by-minute adjustment:

- If setup consumes more than 8 minutes, skip optional styling and focus on one minimal deliverable.
- If the demo fails, narrate the recovery process. This is valuable modeling, not a failure of instruction.
- If half the room is blocked by the same problem, pause the room and solve one shared example.
- If only one or two learners are blocked, keep the rest moving with the lab checklist while you circulate.

### Deeper demo prompts

Use this prompt cycle while live coding:

1. "What input enters this layer?"
2. "What output leaves this layer on success?"
3. "What named error or status represents failure?"
4. "Where is the rule written exactly once?"
5. "How will we prove this behavior after class?"

For API work, insist that learners show at least one JSON error body. A route that works for perfect input but returns an HTML traceback for predictable bad input is not yet a reliable API. For analytics work, insist that learners show the generated file path and explain whether it can be regenerated. For tests, insist that learners read the failing assertion aloud before editing. For packaging, insist that learners follow their own README rather than relying on memory.

### Capstone quality gate

Before the exit ticket, have learners mark their hour result against this quick rubric:

| Category | Ready evidence | Needs attention |
| --- | --- | --- |
| Correctness | The feature works with a realistic happy path. | It only works with hard-coded or instructor-only data. |
| Error handling | A sad path produces a clear exception, JSON error, message, or test failure. | The app crashes or hides the cause. |
| Structure | The responsibility is in the correct layer. | Route, GUI, service, SQL, and reporting logic are tangled together. |
| Repeatability | There is a command, test, or documented step to reproduce the result. | The result depends on manual memory or IDE state. |
| Maintainability | Names are clear and the next feature has an obvious place to go. | The code works once but will be hard to extend. |

**[Instructor speaks:]**
"This rubric is not only for grading. It is a professional checklist. When you leave a feature behind, the next developer should be able to run it, understand it, and change it without fear."

### Common instructor interventions

When a learner puts too much logic in a Flask route or GUI callback, say: "Let us underline the business rule. Now move that sentence into the service or validation helper. The route or callback should coordinate, not own the rule."

When a learner hard-codes paths, say: "This path works on your machine because your machine is currently the hidden dependency. Replace it with a project-relative pathlib Path and create the directory in code."

When a learner catches Exception broadly, say: "Catching everything is like turning off the smoke alarm. Catch the error you expect, convert it into a helpful message, and let surprising errors remain visible during development."

When a learner wants to add a large optional feature before the required slice works, say: "Park that idea in a comment or issue. First make the required slice boring and reliable. Advanced projects succeed through boring reliability."

### Exit-ticket collection options

Choose one depending on time:

- Verbal round-robin: each learner states the working command and the next command.
- Written note: learners submit three bullets: works, broken, next.
- Pair check: partners run each other’s command from the README or lab note.
- Demo lottery: randomly choose two learners to show one happy path and one sad path.

Close the hour by connecting forward: the next hour assumes today has a runnable artifact. If a learner is behind, help them identify the smallest safe stopping point rather than encouraging a risky last-minute rewrite.

## Additional Instructor-Ready Expansion

Use this expansion to deepen the hour without changing the runbook mapping. The focus remains **Flask setup and REST fundamentals**. The concrete artifact for this hour is a minimal Flask application with a `/health` endpoint and JSON 404 handling. Keep returning to that artifact whenever discussion becomes abstract: learners should be able to point at a command, a file, a response, a chart, a test, or a README step and say, "This is the evidence that the hour worked."

### Deeper instructor narration

**[Instructor speaks:]**
"The most important habit in this hour is separating the visible surface from the rule underneath it. Today we are working at the API boundary around the existing tracker service. That layer matters because it is where another human or another part of the system forms expectations. If we leave the expectation implicit, the next person has to guess. If we make it explicit, the project becomes easier to test, easier to debug, and easier to explain during the final capstone review."

**[Instructor speaks:]**
"Before I run anything, I want us to predict the evidence. Our baseline is `flask --app api.app run --debug` or the project-specific `python -m api.app` command. A successful run should prove this happy path: `GET /health` returns HTTP 200 with `{"status": "ok"}` and a service name. A responsible implementation should also prove this sad path: a missing route returns the shared JSON error envelope instead of an HTML traceback. Notice that we are not adding sad paths to be negative. We are adding them because production code spends much of its life receiving imperfect input, missing configuration, stale data, or unexpected user behavior."

Pause after that statement and ask learners to write a one-sentence contract in their own words. For example: "When this input arrives, this layer returns this result or this named error." Circulate quickly and listen for vague language such as "it works" or "it fails." Coach those learners to replace vague language with observable evidence: a status code, exception type, saved filename, printed message, chart title, pytest result, or README command.

### Detailed demo walkthrough

Run the demo as a sequence of small predictions rather than one long typing performance. The suggested demo arc is to create the app factory, register `/health`, add `error_response`, then call both a real and missing route. At each pause, ask the room to identify three things: the input entering this layer, the output leaving this layer, and the single responsibility that should not leak into neighboring layers. If learners cannot name those three things, slow down and draw the boundary again.

Use this checkpoint rhythm:

1. **Baseline:** Run `flask --app api.app run --debug` or the project-specific `python -m api.app` command before editing. If it fails, narrate the failure honestly and recover before adding new code.
2. **First slice:** Implement only enough to prove `GET /health` returns HTTP 200 with `{"status": "ok"}` and a service name. Do not add optional polish yet.
3. **Read the code aloud:** Point to the function or method boundary and say what it accepts and returns.
4. **Sad path:** Trigger a missing route returns the shared JSON error envelope instead of an HTML traceback deliberately. Ask, "Is this failure understandable to the person who receives it?"
5. **Architecture check:** Ask whether the code belongs in the route, client, service, repository, analytics helper, test fixture, or delivery documentation.
6. **Repeatability check:** Identify the exact command or manual step that proves the result again later.
7. **Commit-quality check:** Ask whether the current state could be saved with a clear commit message.

A useful live-coding move is to introduce one small defect on purpose, such as a wrong field name, missing header, missing timeout, incorrect path, or overly broad exception handler. Then read the observed behavior with the class. This models a mature debugging posture: we do not panic; we compare expected behavior with observed behavior, isolate the layer, and make the smallest correction that restores the contract.

### Guided lab checkpoints

During the lab, avoid answering first with a complete solution. Ask learners to show evidence in this order:

- "Show me the command you ran before editing."
- "Show me the smallest code change that targets this hour's artifact."
- "Show me the happy-path evidence: `GET /health` returns HTTP 200 with `{"status": "ok"}` and a service name."
- "Show me the sad-path evidence: a missing route returns the shared JSON error envelope instead of an HTML traceback."
- "Show me where this behavior would be changed if the requirement changed next week."

If a learner is ahead, direct them to this extension only after the required artifact is stable: add `/version` or `/metadata` that reports a safe app name and schema version without exposing secrets. Make it clear that extension work must be reversible. A good extension leaves the required path cleaner or better documented. A risky extension creates a second debugging problem right before the hour closes.

For pairs, assign roles for five-minute intervals. The driver types and runs commands. The navigator reads the contract and watches for boundary violations. Halfway through, switch roles. This keeps faster learners from taking over and gives quieter learners a defined speaking responsibility. Ask the navigator to use the review question: Does every route response look like a deliberate contract rather than whatever Flask happened to return?

### Troubleshooting decision tree

Use this decision tree when the room gets stuck:

- If the first command cannot start, stop feature work and fix environment, import, or configuration issues first.
- If the happy path fails, inspect the boundary closest to the symptom. For API work, inspect request body, headers, route pattern, and service call. For analytics work, inspect path, columns, dtypes, and row counts. For testing work, inspect fixture setup and the exact assertion. For packaging work, inspect README steps and dependency installation.
- If the sad path returns a confusing result, improve the translation layer. Convert expected domain errors into the agreed JSON response, user message, report warning, or pytest assertion. Do not hide unexpected errors while still developing.
- If two layers disagree, choose the service or documented contract as the source of truth and update the outer layer to match it.
- If a learner proposes a rewrite, ask for the smallest reversible change that proves the next fact. Rewrites are sometimes necessary, but they should be chosen deliberately, not as an emotional response to a messy error.

Name the common risk explicitly: letting Flask defaults leak implementation details before the class has agreed on an API contract. Write it on the board as an anti-pattern, then ask learners to point to the line or step in their project that prevents it.

### Formative questions and differentiation notes

Use these questions for quick checks throughout the hour:

- What is the contract this layer promises?
- Which command proves the contract without relying on your memory?
- What invalid input or missing dependency did you test?
- Which part of the code should not know about this detail?
- What would a teammate need in order to reproduce your result tomorrow?
- If this breaks during the final demo, what is the first diagnostic step?

For learners who need more support, narrow the task to one happy path and one sad path. Provide a partially completed function signature or checklist, but still require them to run the command and explain the result. For learners who are ready for more challenge, ask them to document the contract in README language, add a focused test, or compare two design options and justify the simpler one. Keep both groups anchored to the same hour outcome so the class does not split into unrelated projects.

Close by saying: "The goal is not to make this layer impressive. The goal is to make it dependable. Dependable code has a clear contract, a repeatable proof, a known failure behavior, and an obvious next place to change it."
