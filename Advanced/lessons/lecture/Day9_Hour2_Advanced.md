# Day 9, Hour 2: CRUD Endpoints for the Main Resource
**Python Programming Advanced - Session 9**

---

## Timing Overview
**Total Time:** 60 minutes  
- Reconnect to the Flask starter: 5 minutes  
- Direct instruction on CRUD route design and status codes: 15 minutes  
- Live implementation of core endpoints: 10 minutes  
- Guided build using the service layer and SQLite repo: 25 minutes  
- Debrief and exit ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Implement `GET`, `POST`, `PUT`, and `DELETE` routes for the main API resource
2. Connect route handlers to the existing service layer instead of duplicating business logic
3. Return appropriate status codes and JSON response shapes
4. Distinguish clearly between invalid input and missing resources
5. Test CRUD endpoints with realistic examples

---

## Instructor Prep Notes

- Keep the route names stable and predictable: `/records` and `/records/<int:record_id>`
- Assume the service layer already exists and is the home of validation and domain rules
- Prepare one malformed request example and one not-found example
- Keep reminding learners that route handlers should orchestrate, not think too much

---

## Section 1: Route Design Without Guesswork (5 minutes)

### Opening Script

**[Instructor speaks:]**

You already have the API engine running. This hour gives the API something meaningful to do. The goal is not "make lots of routes." The goal is "make a small set of routes that behave predictably and connect cleanly to the service layer."

If learners try to solve everything directly in Flask handlers, the code will get tangled fast. Our discipline today is simple: let routes receive requests, call the service layer, and format responses. That is the job.

---

## Section 2: Direct Instruction on CRUD Endpoints (15 minutes)

### Canonical Route Set

**[Instructor speaks:]**

For one resource called `records`, the canonical route set is:

- `GET /records` to list all records or maybe filtered results later
- `POST /records` to create a record
- `GET /records/<id>` to fetch one record
- `PUT /records/<id>` to update a record
- `DELETE /records/<id>` to remove a record

This pattern is widely recognized. A teammate can guess your API more easily when you follow predictable naming.

### Status Code Reasoning

**[Instructor speaks:]**

Now let's connect route outcomes to status codes:

- `GET /records` successful: `200`
- `GET /records/<id>` successful: `200`
- `POST /records` successful: `201`
- `PUT /records/<id>` successful: `200`
- `DELETE /records/<id>` successful: `200` or `204`; we will use `200` with JSON for simplicity
- malformed JSON or missing required fields: `400`
- record ID does not exist: `404`

The distinction between `400` and `404` is one of the best places to sharpen API thinking. If the client sent bad input, that is `400`. If the input is well-formed but the target resource does not exist, that is `404`.

### Thin Route Handlers

**[Instructor speaks:]**

What should a route handler do?

- read request input
- call the service
- catch known exceptions
- return JSON and a status code

What should a route handler usually not do?

- write SQL directly
- perform deep validation rules that already exist in the service layer
- mutate global state
- contain long business workflows

### Parsing JSON Safely

**[Instructor speaks:]**

Flask gives us `request.get_json(silent=True)` or `request.get_json()`. For beginners, I recommend a gentle, explicit pattern:

```python
payload = request.get_json(silent=True)
if payload is None:
    return error_response("invalid_json", "Request body must be valid JSON.", 400)
```

That is much better than assuming the body exists and then crashing when it does not.

---

## Section 3: Live Implementation (10 minutes)

### Create and List Endpoints

**[Instructor speaks while coding:]**

Let's build the first useful pair: list and create.

```python
from flask import Flask, jsonify, request

app = Flask(__name__)
service = build_service()


@app.get("/records")
def list_records():
    records = service.list_records()
    return jsonify([record.to_dict() for record in records]), 200


@app.post("/records")
def create_record():
    payload = request.get_json(silent=True)
    if payload is None:
        return error_response("invalid_json", "Request body must be valid JSON.", 400)

    try:
        record = service.add_record(
            title=payload.get("title", ""),
            category=payload.get("category", ""),
            status=payload.get("status", "open"),
        )
    except ValidationError as exc:
        return error_response("validation_error", str(exc), 400)

    return jsonify(record.to_dict()), 201
```

Narrate the pattern:

**[Instructor speaks:]**

Notice that the handler does not know how records are stored. It does not know SQL. It does not construct IDs. It receives input, delegates to the service, and formats output.

### Add Get, Update, and Delete

```python
@app.get("/records/<int:record_id>")
def get_record(record_id: int):
    try:
        record = service.get_record(record_id)
    except NotFoundError as exc:
        return error_response("not_found", str(exc), 404)
    return jsonify(record.to_dict()), 200


@app.put("/records/<int:record_id>")
def update_record(record_id: int):
    payload = request.get_json(silent=True)
    if payload is None:
        return error_response("invalid_json", "Request body must be valid JSON.", 400)

    try:
        record = service.update_record(record_id, payload)
    except ValidationError as exc:
        return error_response("validation_error", str(exc), 400)
    except NotFoundError as exc:
        return error_response("not_found", str(exc), 404)

    return jsonify(record.to_dict()), 200


@app.delete("/records/<int:record_id>")
def delete_record(record_id: int):
    try:
        deleted = service.delete_record(record_id)
    except NotFoundError as exc:
        return error_response("not_found", str(exc), 404)

    return jsonify({"deleted": deleted.to_dict()}), 200
```

Then pause and explain:

**[Instructor speaks:]**

This is already enough for a meaningful CRUD API. Do not confuse "small" with "unfinished." A small API that is correct is a much better milestone than a big API with inconsistent behavior.

### Smoke Test Commands

Show:

```bash
curl http://127.0.0.1:5000/records

curl -X POST http://127.0.0.1:5000/records ^
  -H "Content-Type: application/json" ^
  -d "{\"title\":\"Send invoice\",\"category\":\"finance\",\"status\":\"open\"}"
```

If on PowerShell, mention quoting differences. The point is the sequence, not terminal perfection.

---

## Section 4: Guided Build with the Service Layer (25 minutes)

### Lab Goal

**[Instructor speaks:]**

Your job now is to wire CRUD endpoints into your project using the service layer and SQLite repository you already built. Keep the route layer thin. Keep the responses predictable. Keep the status codes honest.

### Required Tasks

Learners should implement:

1. `GET /records`
2. `POST /records`
3. `GET /records/<id>`
4. `PUT /records/<id>`
5. `DELETE /records/<id>`

### Suggested Work Order

1. Build list and create first
2. Add get-by-id
3. Add update
4. Add delete
5. Test one error path for `400`
6. Test one error path for `404`

This order keeps confidence high while complexity increases gradually.

### Coaching Prompts

Ask learners:

- What exception does your service raise when validation fails?
- What exception does it raise when the ID does not exist?
- What shape does your success response use?
- Are your route handlers repeating validation logic that already exists elsewhere?

### Common Mistakes

- Returning `200` for every outcome
- Letting Flask generate HTML errors on route failures
- Forgetting to set `Content-Type: application/json` when testing `POST` or `PUT`
- Mixing integer IDs and string IDs inconsistently
- Creating SQL directly inside the route

### Instructor Recovery Script for a Stuck Learner

**[Instructor speaks:]**

Let's shrink the problem. Start with `GET /records` and confirm you can serialize a list of records. Next add `POST /records` and create exactly one record. Once those two work, the rest of CRUD often becomes easier because the wiring pattern is already established.

### Fast Finishers

If time remains, learners can add query-parameter filtering to `GET /records?q=...`, but only after the basic CRUD routes are stable.

---

## Section 5: Debrief and Exit Ticket (5 minutes)

### Debrief Script

**[Instructor speaks:]**

The most important design habit from this hour is that your Flask routes should feel boring. That is a compliment. Boring routes usually mean the architecture is doing its job. The service layer handles rules. The repository handles persistence. The route handler handles the HTTP boundary.

### Share-Out Questions

- When should an API return `400` instead of `404`?
- Which endpoint did you find easiest to implement?
- Which endpoint revealed the most about your service design?
- Did you discover any validation that was living in the wrong place?

### Exit Ticket

1. When should you return `400`?
2. When should you return `404`?
3. Why should route handlers stay thin?

### Preview of the Next Hour

**[Instructor speaks:]**

Next hour we clean up the contract itself by standardizing serialization and validation. That is how we make the API feel consistent instead of improvised.

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
