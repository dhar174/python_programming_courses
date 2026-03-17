# Day 10, Hour 2: Consuming Your Own API with Python Client Functions
**Python Programming Advanced - Session 10**

---

## Timing Overview
**Total Time:** 60 minutes  
- Reframe the API from the client's point of view: 5 minutes  
- Direct instruction on `requests`, timeouts, and client design: 15 minutes  
- Live demo of a small client module: 10 minutes  
- Guided client build and error handling lab: 25 minutes  
- Debrief and exit ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Write small client functions that call the API predictably
2. Set request timeouts instead of allowing calls to hang indefinitely
3. Pass the API key header for protected operations
4. Translate server-side errors into friendly client-side messages
5. Explain why testing the API from the outside reveals different issues than calling service methods directly

---

## Instructor Prep Notes

- Have the Day 10 API running locally before the lesson begins
- Keep the client module simple and flat; this is not a full SDK
- Reuse the same response shapes from Day 9 and the API key pattern from Hour 37

---

## Section 1: Why Become Your Own Client? (5 minutes)

### Opening Script

**[Instructor speaks:]**

Yesterday and earlier today, we were mostly thinking like API builders. In this hour, we switch perspective and think like API consumers. That shift matters because an API that feels fine from inside the Flask app can still feel awkward or fragile from the outside.

Writing a client forces us to experience our own API the way another tool or teammate would experience it. That is healthy. It surfaces confusing contracts, inconsistent errors, and missing timeouts quickly.

---

## Section 2: Direct Instruction on Client Design (15 minutes)

### The Shape of a Simple Client Module

**[Instructor speaks:]**

For this course, the client module should be boring and readable. A file such as `client/api_client.py` is enough. Each function should do one thing:

- build the URL
- send the request
- set a timeout
- raise or handle errors predictably
- return parsed JSON or a small mapped result

### Why Timeouts Matter

**[Instructor speaks:]**

One of the most important habits in client code is setting a timeout. Without a timeout, a request can hang and leave the user wondering whether the application is frozen.

Use a small default:

```python
requests.get(url, timeout=5)
```

Or, if you want to mention connect/read separation:

```python
requests.get(url, timeout=(3, 10))
```

For the course, `timeout=5` is enough.

### Basic Error Handling Pattern

**[Instructor speaks:]**

Client code should not dump raw traceback details on the end user if a friendly message would do. A practical pattern is:

- call `raise_for_status()`
- catch `requests.Timeout`
- catch `requests.HTTPError`
- optionally inspect the API's JSON error payload
- present a user-oriented message

### Passing the API Key

**[Instructor speaks:]**

Our write routes now require `X-API-Key`. That means the client has to know when to send the header. A simple helper can keep this consistent:

```python
def auth_headers(api_key: str) -> dict:
    return {"X-API-Key": api_key}
```

That is enough for this course.

---

## Section 3: Live Demo of the Client Module (10 minutes)

```python
import requests


BASE_URL = "http://127.0.0.1:5000"


def list_records() -> list[dict]:
    response = requests.get(f"{BASE_URL}/records", timeout=5)
    response.raise_for_status()
    return response.json()


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

Then extend with error handling:

```python
def safe_create_record(payload: dict, api_key: str) -> dict | None:
    try:
        return create_record(payload, api_key)
    except requests.Timeout:
        print("The API request timed out. Check whether the server is running.")
    except requests.HTTPError as exc:
        print(f"Request failed: {exc}")
    return None
```

### Narration

**[Instructor speaks:]**

This is intentionally small. I want you to notice the discipline more than the syntax: timeout set, header passed, error path handled, and response returned in one predictable way.

---

## Section 4: Guided Client Build Lab (25 minutes)

### Lab Goal

**[Instructor speaks:]**

Build a client module that can talk to your API end to end. At minimum, you need list and create. If time allows, add update and delete.

### Required Functions

Learners should add:

1. `list_records`
2. `create_record`
3. `update_record`
4. `delete_record`

### Coaching Prompts

- Where is the timeout set?
- Are you passing the key on write operations?
- What happens if the API is not running?
- What happens if the key is wrong?
- How will a user know the difference between a timeout and a validation error?

### Common Mistakes

- no timeout
- forgetting headers on `PUT` and `DELETE`
- swallowing the error without any visible message
- building duplicate URL strings everywhere instead of reusing a base URL constant

### Recovery Script

**[Instructor speaks:]**

If the full client feels like too much, implement `list_records` and `create_record` first. Those two functions often reveal whether your base URL, error handling, and auth header pattern are correct.

---

## Section 5: Debrief and Exit Ticket (5 minutes)

### Debrief Script

**[Instructor speaks:]**

Writing a client is one of the fastest ways to expose how your API feels from the outside. If the client code became awkward, that is useful feedback. It may mean your response shapes are inconsistent, your errors are hard to read, or your route behavior is doing more than it should.

### Exit Ticket

1. Why should the client set a timeout by default?
2. Which client functions did you finish?
3. What did the client reveal about your API design?

### Preview of the Next Hour

**[Instructor speaks:]**

Next hour you will choose how the pieces fit together: GUI talking to the API or GUI and API existing in parallel over the same service and database layers.

---

## Shared Day 10 Instructor Reference

Reuse the shared day-level instructor support from `Day10_Hour1_Advanced.md` for this hour's facilitation details:

- `## Instructor Coaching Appendix`
- `## Facilitation Toolkit`

This keeps the Day 10 coaching guidance in one maintained location while preserving this file's hour-specific lecture script.
