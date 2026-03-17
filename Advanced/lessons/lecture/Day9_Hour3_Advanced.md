# Day 9, Hour 3: Serialization and Validation
**Python Programming Advanced - Session 9**

---

## Timing Overview
**Total Time:** 60 minutes  
- Reframe the importance of API contracts: 5 minutes  
- Direct instruction on serialization and validation boundaries: 15 minutes  
- Live demo of parser and serializer helpers: 10 minutes  
- Guided cleanup lab with negative tests: 25 minutes  
- Debrief and exit ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Explain what a request and response contract is
2. Centralize record parsing and serialization logic instead of scattering it across routes
3. Keep validation rules in one coherent place
4. Return consistent JSON error shapes across endpoints
5. Use a few intentional negative test cases to verify API behavior

---

## Instructor Prep Notes

- Prepare one example of messy, duplicated route code and one cleaned-up version
- Use the same `ValidationError` and `NotFoundError` patterns from earlier sessions
- Emphasize "manual and consistent" as the runbook wording, meaning clear helpers instead of a new framework detour

---

## Section 1: API Contracts as Promises (5 minutes)

### Opening Script

**[Instructor speaks:]**

By now, many of you will have CRUD routes that work. That is a real milestone. But working routes can still feel messy if every endpoint invents its own input parsing rules and output shape. This hour is about making the API feel coherent.

An API contract is a promise. It says, "If you send data in this shape, and if your request is valid, I will respond in that shape. If something fails, I will fail in a predictable shape." Clients depend on that promise.

---

## Section 2: Direct Instruction on Boundaries (15 minutes)

### Serialization Means Turning Domain Objects into API-Friendly Data

**[Instructor speaks:]**

Your service layer may work with model objects. Your API returns JSON. Serialization is the step that turns a model object into a dictionary that can become JSON. In many student projects, serialization gets repeated inside every route. That repetition becomes expensive because every change must be made in multiple places.

A cleaner pattern is:

```python
def serialize_record(record: Record) -> dict:
    return {
        "id": record.id,
        "title": record.title,
        "category": record.category,
        "status": record.status,
        "priority": record.priority,
    }
```

Then routes call the helper instead of rebuilding dictionaries ad hoc.

### Parsing Means Turning Request Data into a Valid Internal Shape

**[Instructor speaks:]**

Parsing is the opposite direction. The route receives JSON. That JSON may be incomplete, malformed, or type-inconsistent. Our parser should normalize what it can and reject what it cannot.

Example:

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
        raise ValidationError("Status must be open, in_progress, or done.")

    return {
        "title": title,
        "category": category,
        "status": status,
    }
```

### Where Validation Should Live

**[Instructor speaks:]**

There are two reasonable layers for validation in this course:

- parsing helpers that normalize and reject clearly malformed payloads
- service-layer rules that enforce domain invariants

What we want to avoid is duplicating the same rules in every route. If five routes all check for a non-empty title separately, drift is inevitable.

### Consistent Error Shapes

**[Instructor speaks:]**

The runbook reminds us to keep the error shape consistent. That means no route should return:

- plain text in one place
- a dictionary with different keys in another
- a Flask default HTML page somewhere else

Consistency matters because it reduces surprise for the client and creates one place to improve behavior later.

---

## Section 3: Live Demo of Cleaner Helpers (10 minutes)

### Before: Messy Route

Show a messy route:

```python
@app.post("/records")
def create_record():
    payload = request.get_json()
    if "title" not in payload:
        return {"error": "missing title"}, 400
    if "category" not in payload:
        return {"msg": "missing category"}, 400

    record = service.add_record(
        title=payload["title"].strip(),
        category=payload["category"].strip(),
        status=payload.get("status", "open"),
    )
    return {
        "id": record.id,
        "title": record.title,
        "category": record.category,
        "status": record.status,
    }, 201
```

Then critique it openly but kindly:

**[Instructor speaks:]**

This route works on a good day, but it is already drifting. The error keys are inconsistent. Validation is embedded here. Serialization is embedded here. If another route needs similar logic, we will copy and paste it.

### After: Cleaner Route

```python
def serialize_record(record: Record) -> dict:
    return {
        "id": record.id,
        "title": record.title,
        "category": record.category,
        "status": record.status,
    }


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

Then say:

**[Instructor speaks:]**

The route is now much easier to scan. Helpers are reusable. Changes become safer. This is the kind of cleanup that turns "it works" into "it is maintainable."

---

## Section 4: Guided Cleanup Lab (25 minutes)

### Lab Goal

**[Instructor speaks:]**

Your goal now is to make your API consistent. You are not adding lots of new endpoints. You are making the existing endpoints easier to trust.

### Required Tasks

Learners should:

1. Create a serializer helper for the main resource
2. Create a parser or validation helper for request bodies
3. Update CRUD routes to use these helpers
4. Ensure all known errors return the same JSON error shape
5. Test at least three negative cases manually

### Recommended Negative Cases

Use these examples:

1. Missing title
2. Invalid status value
3. Valid JSON but nonexistent record ID

Encourage learners to record the expected status code and response shape before testing. That makes the test intentional instead of random.

### Coaching Prompts

- If you change one field name, how many route handlers do you have to edit?
- Are your error keys identical across routes?
- Which validation rules belong in the parser, and which belong in the service layer?
- Does your parser normalize casing and whitespace consistently?

### Common Mistakes

- Helpers that are too magical and hide obvious logic
- Routes that still build their own output dictionaries
- Validation duplicated in both parser and service without a clear reason
- Response shapes that vary between list and single-item endpoints without explanation

### Instructor Recovery Script

**[Instructor speaks:]**

If this feels abstract, pick one endpoint and clean only that one first. Once one route is clean, use it as the pattern for the others. Most maintainability improvements in real projects spread through good examples, not through one giant rewrite.

### Stretch Option

If time remains, learners can add a response wrapper that includes the request ID for successful writes as well, but this is optional. The main requirement is consistent error behavior.

---

## Section 5: Debrief and Exit Ticket (5 minutes)

### Debrief Script

**[Instructor speaks:]**

API quality is not only about adding more endpoints. It is also about making the behavior legible. Serialization and validation are the quiet systems that make an API feel coherent. Clients may never thank you for that consistency, but they will definitely notice when it is missing.

### Share-Out Questions

- What logic did you move out of your routes today?
- Which negative test taught you the most?
- What validation rule was duplicated before you cleaned it up?
- How consistent is your error contract now?

### Exit Ticket

1. Why should all API errors follow a consistent format?
2. What is the difference between parsing and serialization?
3. Why is duplicated validation expensive?

### Preview of the Next Hour

**[Instructor speaks:]**

Next hour we keep the API maintainable as it grows by refactoring the app structure and wiring dependencies cleanly. That will prepare you for the security and client work in the next session.

---

## Shared Day 9 Instructor Reference

Reuse the shared day-level instructor support from `Day9_Hour1_Advanced.md` for this hour's facilitation details:

- `## Instructor Coaching Appendix`
- `## Facilitation Toolkit`

This keeps the Day 9 coaching guidance in one maintained location while preserving this file's hour-specific lecture script.
