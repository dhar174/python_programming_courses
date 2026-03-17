# Day 9, Hour 1: REST Fundamentals and Flask App Setup
**Python Programming Advanced - Session 9**

---

## Timing Overview
**Total Time:** 60 minutes  
- Reframe the capstone as a service: 5 minutes  
- REST and Flask concept lecture: 15 minutes  
- Live build of the first Flask app and `/health` endpoint: 10 minutes  
- Guided lab and API smoke testing: 25 minutes  
- Debrief and exit ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Explain what a REST-style resource is in plain language
2. Distinguish common HTTP methods such as `GET` and `POST`
3. Create a minimal Flask application with a JSON health endpoint
4. Return consistent JSON error payloads instead of default HTML errors
5. Test a small API using a browser, `curl`, or a Python client script

---

## Instructor Prep Notes

- Keep the framing practical: learners are exposing the same capstone logic through a new interface, not building a second unrelated project
- Default example resource name: `records`
- Use the same tracker domain from the service and SQLite work
- Have one terminal ready for the Flask app and another for `curl` commands
- Prewrite a request ID helper so the error response pattern feels real without becoming a detour

---

## Vocabulary for This Hour

- Resource: a thing the API exposes, such as a record, task, contact, or expense entry
- Route: a URL pattern connected to code in the Flask app
- Method: the HTTP verb such as `GET`, `POST`, `PUT`, or `DELETE`
- Status code: a numeric result that tells the client what happened
- JSON contract: the expected request and response shape
- Request ID: a lightweight identifier that helps connect logs to user-facing errors

---

## Section 1: Why an API Matters for This Capstone (5 minutes)

### Opening Script

**[Instructor speaks:]**

Up to this point, our application has been gaining capability: richer models, service-layer logic, validation, logging, SQLite persistence, and practical search. Today we are changing the surface area again. Instead of only interacting through local scripts or a GUI, we are going to expose our application's capabilities through a web API.

That does not mean we are abandoning the architecture we built. In fact, the reason today is possible is that we already separated the service layer from the storage layer. Flask is just going to become another consumer of the same service methods.

### Why Learners Should Care

**[Instructor speaks:]**

An API matters because it lets other systems, scripts, interfaces, or teammates interact with your application in a standard way. A GUI is for human users. An API is for structured communication. Once you have an API, you can:

- build a separate client later
- connect a GUI to the service over HTTP
- automate workflows with scripts
- document your application behavior more clearly

That is why REST fundamentals fit naturally after persistence. An API without a stable core is chaos. A stable core without an API is still useful, but less flexible.

---

## Section 2: REST and Flask Concepts (15 minutes)

### REST in Plain English

**[Instructor speaks:]**

REST can sound intimidating, but in our course we are using a lightweight meaning: organize your API around resources, use standard HTTP methods, and return predictable responses.

A resource is the thing the API is about. In our tracker example, the resource is `records`. So routes might look like:

- `GET /records` to list records
- `POST /records` to create a new record
- `GET /records/12` to fetch one record
- `PUT /records/12` to update record 12
- `DELETE /records/12` to delete record 12

That is already enough to feel REST-like and useful.

### Method Semantics

**[Instructor speaks:]**

Teach the verbs in a grounded way:

- `GET` asks for data and should not change state
- `POST` creates something new
- `PUT` updates or replaces an existing thing
- `DELETE` removes something

You can mention `PATCH` exists, but do not let the class disappear into an HTTP standards rabbit hole. For this course, `PUT` is enough.

### Status Codes That Matter Today

**[Instructor speaks:]**

We only need a small status code vocabulary for this hour:

- `200 OK` for a successful read or update response
- `201 Created` for a successful create
- `400 Bad Request` when the request body or input is invalid
- `404 Not Found` when the resource ID does not exist
- `500 Internal Server Error` for unexpected failures we did not handle cleanly

Explain that one sign of a professional API is that it does not return `200` for everything. The status code should help the client understand the outcome quickly.

### Why Flask

**[Instructor speaks:]**

Flask is a good fit for this course because it is small, readable, and easy to explain on one screen. Learners can focus on routes, request handling, and responses without a heavy framework ceremony.

The basic structure is:

```python
from flask import Flask

app = Flask(__name__)


@app.get("/health")
def health():
    return {"status": "ok"}
```

That small amount of code lets us talk about the important parts without distraction.

### JSON Error Contracts

**[Instructor speaks:]**

The runbook asks us to standardize error responses. That is not a cosmetic detail. It means the client can depend on a consistent structure. Instead of random strings, HTML error pages, or one-off shapes, we want something like:

```json
{
  "error": {
    "code": "not_found",
    "message": "Record 12 was not found.",
    "request_id": "a1b2c3d4"
  }
}
```

That structure gives us three wins:

1. the client gets a readable message
2. the application has a machine-readable code
3. the request ID helps correlate logs and troubleshooting

### What We Are Not Doing Yet

**[Instructor speaks:]**

Today is not the day for deployment pipelines, OpenAPI generators, background workers, or production-scale API versioning. We are building a solid course-level API with good habits.

---

## Section 3: Live Build of the First Flask App (10 minutes)

### Step 1: Create the App Skeleton

**[Instructor speaks while coding:]**

I am going to start with the smallest honest Flask app I can.

```python
from flask import Flask, jsonify
from uuid import uuid4


app = Flask(__name__)


def error_response(code: str, message: str, status: int):
    request_id = uuid4().hex[:8]
    payload = {
        "error": {
            "code": code,
            "message": message,
            "request_id": request_id,
        }
    }
    return jsonify(payload), status


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True)
```

### Step 2: Explain the Pieces

**[Instructor speaks:]**

Let's name what just happened:

- `app = Flask(__name__)` creates the Flask application
- `@app.get("/health")` connects a URL and method to a function
- `jsonify(...)` ensures we return JSON cleanly
- `error_response(...)` standardizes the shape of failures
- `if __name__ == "__main__":` gives us a simple local run path

### Step 3: Test the Endpoint

Run the app and then test it:

```bash
python api/app.py
curl http://127.0.0.1:5000/health
```

Then narrate:

**[Instructor speaks:]**

A health endpoint is boring on purpose. It gives us a quick way to verify that the app starts and responds before we add business logic.

### Step 4: Demonstrate a Consistent Error

Temporarily add:

```python
@app.get("/boom")
def boom():
    return error_response(
        code="demo_error",
        message="This is a sample structured error.",
        status=400,
    )
```

Then test it and emphasize:

**[Instructor speaks:]**

Even our error examples should look like part of the same application. Consistency is one of the easiest ways to make an API feel professional.

---

## Section 4: Guided Lab and API Smoke Testing (25 minutes)

### Lab Goal

**[Instructor speaks:]**

Your goal for this lab is to create a working Flask starter application for your own project. At minimum, it should run, respond to `/health`, and return JSON-formatted errors in a consistent structure.

### Required Tasks

Learners should:

1. Create `api/app.py` or an equivalent entry file
2. Initialize a Flask app
3. Add a `GET /health` route
4. Add an `error_response` helper
5. Run the app locally
6. Test it with a browser, `curl`, or a script

### Recommended Build Sequence

Guide learners in this order:

1. Make the file runnable
2. Make `/health` return JSON
3. Add the error helper
4. Trigger one controlled error path
5. Only then begin thinking about real resource routes

This sequence keeps the mental load low and gives fast wins.

### Circulation Questions

Ask learners:

- Can you explain the difference between a route and a resource?
- Why is `/health` useful before CRUD routes exist?
- What status code should a successful create return later?
- Why is JSON consistency important even when the API is small?

### Common Problems and How to Coach Them

#### Problem: Port Conflict

What to say:

**[Instructor speaks:]**

If the default port is already in use, do not panic. Change the port in `app.run(port=5001)` or stop the other process. This is an environment problem, not a design failure.

#### Problem: Returning Plain Dictionaries vs `jsonify`

What to say:

**[Instructor speaks:]**

Flask can return dictionaries directly in modern versions, but `jsonify` keeps the intent obvious for beginners and helps us stay consistent in teaching examples.

#### Problem: Learner Puts Database Logic into the Health Route

What to say:

**[Instructor speaks:]**

Keep `/health` simple. The point is to check if the service is up. It is not a checkpoint for all business logic.

#### Problem: Debug Mode Confusion

What to say:

**[Instructor speaks:]**

Debug mode is useful for development, but do not treat it as a production setup. For the course, it is a convenience, not part of the API contract.

### Fast Finishers

If learners finish early, let them add:

- `/version` endpoint from a constant
- a starter `/records` route that returns an empty list
- a README note showing how to launch the API

---

## Section 5: Debrief and Exit Ticket (5 minutes)

### Debrief Script

**[Instructor speaks:]**

Today was the beginning of a new interface, not a replacement for the architecture you already built. If your Flask starter is working, you are in a strong position for the next hour because the hard part is not typing route decorators. The hard part is keeping the route layer thin and the service layer central.

### Share-Out Prompts

- What part of Flask felt simpler than you expected?
- What status code would you return for a successful create?
- What structure did you choose for API files and folders?
- How are you going to keep error responses consistent as you add routes?

### Exit Ticket

1. What is a resource in your API?
2. What is the difference between `GET` and `POST` in today's terms?
3. What HTTP status code should represent a successful create?

### Preview of the Next Hour

**[Instructor speaks:]**

Next hour we turn the starter into something useful by adding CRUD endpoints for the main resource. The big challenge will not be route quantity. The big challenge will be correct status codes, validation, and keeping the API layer thin.

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
