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

## Shared Day 9 Instructor Reference

Reuse the shared day-level instructor support from `Day9_Hour1_Advanced.md` for this hour's facilitation details:

- `## Instructor Coaching Appendix`
- `## Facilitation Toolkit`

This keeps the Day 9 coaching guidance in one maintained location while preserving this file's hour-specific lecture script.
