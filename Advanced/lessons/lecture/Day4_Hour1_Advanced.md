# Day 4, Hour 1: HTTP Client Work – `requests` + JSON Contracts
**Python Programming Advanced – Session 4**

---

## Instructor Notes

- **Course**: Python Programming (Advanced)
- **Session**: Day 4, Hour 1 of 48, also Hour 13 in the Advanced runbook sequence
- **Focus**: Building a reliable HTTP client with `requests`, explicit timeouts, structured error handling, and JSON contract checks.
- **Source of truth**: `Advanced/Instructor/Python_Advanced_Instructor_Runbook_4hr_Days.md`, Session 4, Hour 13.
- **Prerequisites**: Learners should have completed the Day 3 tracker work or have equivalent familiarity with small service wrappers, logging, exceptions, and validating data before trusting it.
- **Advanced trajectory**: This hour moves from local application reliability into external-service reliability. Learners are not building a full API server yet; they are learning how a Python program responsibly consumes another service.
- **Instructor goal**: By the end of this hour, every learner can write a small API consumer that sets a timeout, handles network and HTTP failures, validates JSON shape, and prints friendly messages for timeout, 404, 500, and invalid JSON situations.

Important instructor positioning:

- Keep repeating the phrase **outside data is untrusted until checked**. It links directly to the JSON contract idea.
- The required lab must be protected. Students need time to implement the happy path and then exercise distinct failure branches.
- Do not let the hour drift into Flask routes, authentication systems, advanced retries/backoff, async clients, or production API architecture. Those topics can be named as future directions, but Hour 13 is about one reliable HTTP client wrapper.
- If internet access is unreliable, use an instructor-provided local endpoint or prepared response examples. The learning target is the client behavior, not dependence on a specific public service.
- Friendly user messages and developer diagnostics are different audiences. This is a useful bridge from Day 3 logging into Session 4 API work.

---

## Timing Overview
**Total Time:** 60 minutes  
- Recap & Transition from Session 3: 4 minutes
- HTTP client fundamentals: 9 minutes
- JSON contracts, status codes, and timeout patterns: 10 minutes
- Live Demo (public API consumer with wrapper function): 8 minutes
- Hands-On Lab (API consumer with failure-branch checks): 26 minutes
- Debrief & Exit Ticket: 3 minutes

This one-hour plan totals exactly 60 minutes: 4 + 9 + 10 + 8 + 26 + 3 = 60. The hands-on lab is 26 minutes, which stays inside the runbook's required 25-35 minute lab window. Protect the lab time. If the concept discussion runs long, shorten the demo narration rather than reducing the student practice, because the lab is where learners prove they can handle success, timeout, 404, 500, and invalid JSON cases.

---

## Learning Outcomes for This Hour

By the end of this hour, you will be able to:
1. Explain the practical difference between an HTTP client and an API server
2. Use the `requests` library to send a `GET` request and parse JSON safely
3. Set a timeout on every request and explain why timeouts matter in real systems
4. Use `response.raise_for_status()` and structured exception handling for network failures
5. Treat JSON as a contract by validating required keys and expected value types before use
6. Write a small wrapper function so request logic is not repeated throughout an application
7. Build a user-friendly API consumer that handles timeout, 404, 500, and invalid JSON cases gracefully

---

## Section 1: Recap & Transition from Session 3 (4 minutes)

### Quick Re-entry

**[Instructor speaks:]**

Welcome to Session 4. Up to this point in the advanced course, you have been building stronger program structure: organizing code into reusable functions and classes, separating responsibilities, and thinking about applications as systems instead of as one-off scripts. That matters today, because as soon as a program starts talking to something outside itself, the stakes change.

In the earlier sessions, most of our programs worked with data that was already inside Python: lists, dictionaries, objects, files we controlled, and logic we wrote. Today we start consuming data that comes from somewhere else. That “somewhere else” might be a public API, an internal service, a local development endpoint, or a future capstone backend.

The mental shift I want you to make is this: **outside data is untrusted until we check it**. It may be late. It may be malformed. It may be missing keys. The server may be down. The JSON may not match what we assumed yesterday. Professional-grade software is not the software that works only in the happy path; professional-grade software is software that behaves predictably when the world gets messy.

So in this hour we are not just learning how to “call an API.” We are learning how to build a small, reliable client.

### Framing the Hour

**[Instructor speaks:]**

Here is the storyline for this hour:

- First, we will define what an HTTP client is and why applications use one.
- Then we will talk about practical HTTP concerns: methods, status codes, timeouts, and failures.
- After that, we will introduce a very important design habit: **JSON is a contract**.
- Then I will demo a tiny client wrapper built with `requests`.
- Finally, you will build a small consumer script that handles both success and failure cases cleanly.

**[Ask students:]** Before we start typing, where have you seen an application use outside data? Weather apps? Maps? Streaming recommendations? Payment systems? Inventory dashboards?

[Pause. Invite 2–3 examples.]

Exactly. Nearly every serious application is, in some form, an HTTP client.

---

## Section 2: HTTP Client Fundamentals (9 minutes)

### What an HTTP Client Does

**[Instructor speaks:]**

An HTTP client is simply code that sends an HTTP request to a server and receives an HTTP response. The client asks for something; the server answers. That answer might be HTML for a browser, JSON for a program, or an error if something went wrong.

At a high level, think of the client as the side initiating the conversation. Our Python program becomes the client. A service on another machine becomes the server. We do not need to memorize the entire HTTP specification today. We need a practical model that lets us build reliable code.

The request usually includes:

- a method such as `GET` or `POST`
- a URL
- optional query parameters
- optional headers
- sometimes a request body

The response usually includes:

- a status code such as 200, 404, or 500
- headers
- a body, often JSON in API work

### GET vs POST at a High Level

**[Instructor speaks:]**

For this hour, the two verbs I want students to hear clearly are `GET` and `POST`.

- `GET` means “please give me data.”
- `POST` means “please accept this data or create something.”

We are focusing mainly on `GET` because it is the cleanest place to start. It lets us practice receiving and validating JSON without adding the complexity of request payloads. But students should still hear the distinction because their capstones may eventually need both.

**[Prediction prompt:]** If I say “fetch the current weather,” which method sounds more likely: `GET` or `POST`?

[Pause. Students should say `GET`.]

Correct. We are asking for information, not sending a new record to be created.

### Why We Use the `requests` Library

**[Instructor speaks:]**

Python includes lower-level tools for networking, but `requests` is widely used because it gives us a readable, ergonomic interface. Its value for learners is that it removes noise so we can concentrate on good client behavior.

A very small example looks like this:

```python
import requests

response = requests.get("https://example.com/api/items", timeout=5)
print(response.status_code)
print(response.text)
```

That is approachable, but it is not yet robust. If the server hangs, we need a timeout. If the server returns a 404 or 500, we need structured handling. If the body is not valid JSON, we need a fallback plan. If the JSON shape changes, we need validation. Those are the habits that separate classroom demos from dependable code.

### The Reality of Failure

**[Instructor speaks:]**

Students often assume a request either “works” or “does not work.” In real systems there are multiple kinds of not-working, and they matter because the user-facing message should match the failure.

A few examples:

- The network is unavailable.
- DNS fails.
- The server takes too long.
- The server responds, but with a 404.
- The server responds, but with a 500.
- The server responds with text that is not valid JSON.
- The server responds with valid JSON, but not the JSON we expected.

All of those are different. Good client code distinguishes them where it is useful and gives friendly, safe feedback.

---

## Section 3: JSON Contracts, Timeouts, and Status Codes (10 minutes)

### Always Set a Timeout

**[Instructor speaks:]**

This is one of the most practical lessons in the entire session: **always set a timeout**.

If students remember only one implementation habit from today, let it be that one. Without a timeout, the program can wait indefinitely for a server response. In a small script, that feels like a frozen program. In a real application, that becomes a terrible user experience and, potentially, a reliability incident.

A timeout says, “I am willing to wait this long, and after that I will handle the situation myself.”

Examples:

```python
requests.get(url, timeout=5)
requests.get(url, timeout=(3, 10))
```

The first form is a single overall timeout value. The second form separates connection timeout and read timeout. At this stage, students do not need deep networking theory. They just need to understand that the client should never hang forever.

**[Quick check:]** What is the difference between “the server is slow” and “the client hangs forever”? The first is a situation we can manage. The second is a program design mistake if we forgot the timeout.

### Prefer `raise_for_status()`

**[Instructor speaks:]**

We could manually inspect `response.status_code` everywhere, but a cleaner habit is to call `response.raise_for_status()`. That method raises an exception for 4xx and 5xx responses.

Why is that helpful?

Because it keeps happy-path code clean and pushes failures into exception-handling logic where they belong.

```python
response = requests.get(url, timeout=5)
response.raise_for_status()
data = response.json()
```

This reads as: request, verify success, parse body.

We can then catch `requests.HTTPError` and present a safe, useful message.

### JSON Is a Contract, Not Just a Blob of Data

**[Instructor speaks:]**

Here is the most important design concept of the hour: **JSON is a contract**.

Beginners often write code that assumes the response is exactly what they imagined:

```python
title = data["title"]
user_id = data["userId"]
```

That may work until the API changes, or the field is missing, or the value type shifts from `int` to `str`, or the endpoint returns a list instead of a dictionary. Suddenly the code crashes somewhere far from the actual problem.

A better approach is to define the minimum contract you require before using the data.

For example:

- The payload must be a dictionary.
- It must contain `id`, `title`, and `body`.
- `id` must be an integer.
- `title` and `body` must be strings.

This does not need to become enterprise-grade schema tooling for today’s lesson. A small validation function is enough to teach the principle.

### Friendly Failure Categories

**[Instructor speaks:]**

I want students to leave with a simple mapping between failure types and user-facing responses:

- **Timeout** → “The service took too long to respond.”
- **Connection problem** → “The service may be unreachable.”
- **HTTP error** → “The service returned an error.”
- **Invalid JSON** → “The service returned unreadable data.”
- **Contract mismatch** → “The service response did not match expectations.”

Notice what is missing from those messages: stack traces, raw server internals, and confusing technical noise. We can log details for developers, but users should get a calm, actionable message.

### A Simple Wrapper Function Pattern

**[Instructor speaks:]**

One common anti-pattern is repeating request logic everywhere in an application. A better habit is to create a tiny wrapper function or client function that centralizes the request behavior.

That wrapper can:

- set the timeout
- call `raise_for_status()`
- parse JSON
- validate required structure
- log failures
- return clean Python data to the rest of the program

The benefit is not just less typing. The benefit is consistency. When you later update your timeout strategy, add headers, or improve error handling, you do it in one place.

---

## Section 4: Live Demo – Public API Consumer with a Wrapper Function (8 minutes)

### Demo Setup

**[Instructor speaks:]**

I’m going to use a public sample endpoint for demonstration. If internet access is restricted in your environment, switch this to an instructor-provided local endpoint. The teaching goal is the same: make a request, parse JSON, validate the contract, and handle failures.

As I code, I want students watching for four specific moves:

1. I set a timeout.
2. I call `raise_for_status()`.
3. I validate the JSON structure.
4. I return a friendly message on failure.

```python
from __future__ import annotations

import logging
from typing import Any

import requests

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


class APIContractError(Exception):
    """Raised when API data does not match the expected shape."""


def validate_post_contract(payload: dict[str, Any]) -> None:
    required_fields: dict[str, type] = {
        "id": int,
        "title": str,
        "body": str,
    }

    for field_name, expected_type in required_fields.items():
        if field_name not in payload:
            raise APIContractError(f"Missing required field: {field_name}")
        if not isinstance(payload[field_name], expected_type):
            actual_type = type(payload[field_name]).__name__
            expected_name = expected_type.__name__
            raise APIContractError(
                f"Field '{field_name}' expected {expected_name}, got {actual_type}"
            )


def fetch_post(post_id: int) -> dict[str, Any] | None:
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        response = requests.get(url, timeout=(3, 10))
        response.raise_for_status()
        data: Any = response.json()

        if not isinstance(data, dict):
            raise APIContractError("Expected a JSON object")

        validate_post_contract(data)
        return data

    except requests.Timeout:
        logger.error("The service timed out.")
    except requests.ConnectionError:
        logger.error("The service appears unreachable.")
    except requests.HTTPError as error:
        status_code = (
            error.response.status_code
            if error.response is not None
            else "unknown"
        )
        logger.error("The service returned an HTTP error: %s", status_code)
    except requests.exceptions.JSONDecodeError:
        logger.error("The service returned invalid JSON.")
    except APIContractError as error:
        logger.error("The JSON contract was not satisfied: %s", error)

    return None


def main() -> None:
    post = fetch_post(post_id=1)
    if post is None:
        print("Sorry, we could not load the post right now.")
        return

    print(f"Post #{post['id']}")
    print(f"Title: {post['title']}")
    print(f"Preview: {post['body'][:60]}...")


if __name__ == "__main__":
    main()
```

### Demo Narration

**[Instructor speaks:]**

Walk line by line. Do not rush the wrapper pattern.

Start with the custom exception. Explain that a contract mismatch is not exactly the same kind of problem as a timeout or 404. Naming the problem makes the code easier to reason about.

Then point to `validate_post_contract()`. Explain that this is not overengineering. It is a small safety checkpoint between unknown input and trusted application logic.

Then point to `fetch_post()`. Emphasize that the rest of the application does not need to know about status codes, timeout tuples, or `requests` internals. It asks for a post. The wrapper deals with transport-level concerns.

**[Prediction prompt:]** What do you think happens if the endpoint returns HTML instead of JSON?

[Pause.]

Right: `response.json()` will fail, and we want that failure to become a friendly message and a useful log entry.

**[Instructor action:]** If possible, intentionally demonstrate one failure at a time:

- Change the URL to a missing path to trigger a 404.
- Use a deliberately tiny timeout to discuss timeout behavior.
- Point to where invalid JSON would be caught.

If the environment does not make it easy to trigger a real timeout, narrate it conceptually. The goal is the pattern, not the drama.

### Teaching Notes During the Demo

**[Circulate / observe:]**

Watch for students copying the code without understanding why each `except` exists. Pause and ask:

- Which block handles a timeout?
- Which block handles a valid response with unexpected content?
- Why do we check `isinstance(data, dict)` before validation?

If students answer those questions correctly, they are moving beyond syntax into design thinking.

---

## Section 5: Hands-On Lab – API Consumer with Failure-Branch Checks (26 minutes)

### Lab Framing

**[Instructor speaks:]**

Now students will build their own small API consumer. Keep the scope modest. This is not an API framework. It is a single script or tiny client module that demonstrates disciplined request handling.

The lab target is intentionally close to the demo, but not identical. I want them to type, adapt, and make decisions.

### Student Task

**Lab: API Consumer**

Students should build a script that:

- calls an HTTP endpoint
- parses JSON and displays selected fields
- uses `timeout=...` on every request
- handles non-200 responses with a friendly message
- distinguishes at least these failure cases:
  - timeout
  - connection or network failure
  - 404
  - 500
  - invalid JSON
- validates that required keys exist before using them

If students are unsure which endpoint to use, provide one. A simple public JSON endpoint or instructor-provided local endpoint is fine.

### Required Lab Milestones

Use these milestones to make the 26-minute lab concrete. Students should not stop after the first successful request.

1. **Happy path first.** Call a known-good endpoint, parse the JSON, validate at least one required field, and print selected fields in a user-friendly format.
2. **Timeout path.** Confirm that every request call includes `timeout=...`. If a real timeout is hard to trigger in class, have students point to the `except requests.Timeout` block and explain the message it would show.
3. **404 path.** Change the URL or identifier to something missing and verify the program prints a friendly "not found" style message rather than a traceback.
4. **500 path.** Use an instructor-provided endpoint, mock response, or prepared discussion case if the public API does not offer a stable 500. The required habit is that 5xx responses are handled separately from success.
5. **Invalid JSON path.** Use a non-JSON endpoint, local sample, or instructor-provided response to verify that JSON parsing failures do not crash the program.
6. **Contract mismatch path.** Adjust the expected key name temporarily and confirm the program catches missing or wrong-typed data before using it.
7. **Connection failure path.** Use a deliberately invalid host, a stopped local endpoint, or an instructor-provided scenario to verify the program reports "service unreachable" instead of crashing.

The point is not that every student must find a perfect public endpoint for every failure. The point is that every student can show where each failure is handled and can demonstrate at least the happy path plus one real failure during class.

### Suggested Lab Timing

- First 5 minutes: choose endpoint, run one successful request, and print a status or small payload summary.
- Next 6 minutes: move request logic into `fetch_resource()` with `timeout=...`, `raise_for_status()`, and `response.json()`.
- Next 6 minutes: add contract checks for required keys and expected types.
- Next 6 minutes: add friendly branches for timeout, connection failure, 404/500 HTTP errors, invalid JSON, and contract mismatch.
- Final 3 minutes: run one success case and one failure case, then write a short note explaining the difference between timeout and retry.

### Suggested Starter Shape

```python
from __future__ import annotations

from typing import Any
import logging

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)


class APIContractError(Exception):
    pass


def fetch_resource(url: str) -> dict[str, Any] | None:
    # Students implement this.
    raise NotImplementedError


def main() -> None:
    # Students call fetch_resource() and print selected fields.
    raise NotImplementedError


if __name__ == "__main__":
    main()
```

### Completion Criteria

A student solution is complete when:

- the request succeeds and prints parsed output
- the client does not hang indefinitely
- at least one required field is validated before use
- timeout, connection failure, 404, 500, and invalid JSON each produce a friendly user-facing message
- the code avoids duplicating request logic all over the script

### Circulation Notes

**[Circulate:]**

When circulating, prioritize these questions:

1. **Did the student set a timeout?** If not, that is the first intervention.
2. **Are they calling `raise_for_status()`?** If not, show how this simplifies their branching.
3. **Are they assuming keys exist?** Ask, “What happens if `title` is missing?”
4. **Are they printing raw exceptions directly to users?** Encourage safe, plain-language messages.
5. **Have they repeated request code in multiple places?** Suggest a wrapper function.

If a student is stuck, reduce the problem:

- first, print the status code
- then parse JSON
- then validate one field
- then add one `except` block at a time

That sequencing helps anxious learners regain momentum.

### Common Pitfalls to Watch For

- No timeout set, so the request may hang.
- Calling `.json()` and assuming it always works.
- Assuming `response.status_code == 200` is the only success worth considering without using `raise_for_status()`.
- Accessing `data["title"]` before checking that `data` is a dictionary.
- Catching a giant broad `except Exception:` first and masking the real problem.
- Treating logging and user messages as the same audience.

### Optional Extensions

If a student finishes early, suggest one of these:

- add query parameters with `params={...}`
- add a simple retry loop with up to 3 attempts for timeout or connection failure
- create a second wrapper function for another endpoint
- convert validated JSON into a small dataclass or typed dictionary shape

Be careful that extensions do not replace the required foundation. This hour is about reliability habits, not feature sprawl.

---


### Instructor Troubleshooting Playbook

**[Instructor speaks:]**

Before we close the lab, I want students to hear the debugging mindset out loud, because network bugs can feel mysterious if you treat the internet like magic. Here is the progression I want to model whenever a student says, “My API code doesn’t work.”

**Step 1: Identify which layer is failing.**

Ask, “Did the request fail before the server responded, or did the server respond with something unexpected?” That separates transport problems from application-data problems.

- If there is a timeout, the server may be slow or unreachable.
- If there is a 404, the path may be wrong.
- If there is a 500, the server had an internal problem.
- If `response.json()` fails, the body may not be valid JSON.
- If the contract validator fails, the JSON exists but the structure is not what the code expects.

Students gain confidence when they learn that not every failure belongs to the same bucket.

**Step 2: Reduce the number of assumptions.**

If a student has a long script, ask them to strip it down temporarily.

- Print the URL.
- Print the status code.
- Print one safe summary of the response.
- Validate one required field.
- Then add the rest back.

That sequence prevents students from debugging ten moving parts at once.

**Step 3: Compare the failure message to the user experience.**

Ask, “If you were using this program instead of writing it, would this output help you?”

A raw traceback may help a developer, but it does not help most users. A strong answer often looks like two channels:

- a friendly console message for the user
- a detailed log entry for the developer

This is an excellent moment to reinforce the audience difference between user-facing communication and diagnostics.

**Step 4: Check for repeated request code.**

If a student has nearly identical `requests.get(...)` code in three places, coach them to pull it into a wrapper. That one suggestion often improves both readability and reliability at the same time.

### Instructor Mini-Conferences During Circulation

**[Circulate:]**

When you stop at a student’s station, avoid grabbing the keyboard too quickly. Instead, ask short, targeted questions that reveal whether they understand the design choices.

A useful mini-conference sounds like this:

- “Show me where your timeout is set.”
- “Where do you handle 4xx and 5xx responses?”
- “What happens if the JSON body is a list instead of a dictionary?”
- “What happens if the `title` key is missing?”
- “Where would you change behavior if every request in the app needed a different timeout later?”

These questions do two things. First, they expose fragile code quickly. Second, they reinforce that engineering means making deliberate choices, not just getting output once.

### Sample Student Misconceptions and How to Respond

**Misconception 1: “If I got data once, the code is fine.”**

**[Instructor response:]**

Not yet. One successful response proves the happy path. Reliable client code proves it can behave sensibly when the service is slow, missing, or inconsistent.

**Misconception 2: “I checked status code 200, so I’m done.”**

**[Instructor response:]**

A 200 means the server answered successfully at the HTTP layer. It does not guarantee the JSON is valid or that the structure matches your expectations. HTTP success is not the same thing as application-level correctness.

**Misconception 3: “I can just catch `Exception` for everything.”**

**[Instructor response:]**

You can, but then you lose clarity. A timeout and invalid JSON are different problems. Specific exceptions help you respond more intelligently and debug faster.

**Misconception 4: “Retries and timeouts are basically the same.”**

**[Instructor response:]**

A timeout defines how long one attempt may wait. A retry defines whether you will try again after a failed attempt. They solve related but different problems.

### Optional Instructor-Driven Reflection if Time Remains

**[Instructor speaks:]**

If the room is moving quickly, pause for a two-minute reflection and ask students to write short answers to these prompts:

1. What is one failure mode your client now handles that it did not handle at the start of the hour?
2. What part of the JSON contract are you validating explicitly?
3. If you had to add a second endpoint tomorrow, what code could you reuse immediately?

This reflection turns the lab from a copy exercise into an architecture exercise.

### Strong Solution Characteristics to Call Out Publicly

**[Instructor speaks:]**

When you spotlight student work, do not only praise the student whose program has the fanciest output. Look for evidence of dependable habits. Public praise should go toward things like:

- clean wrapper functions
- specific exception handling
- calm, friendly failure messages
- explicit timeout use
- a clear validation step before accessing JSON fields

That teaches the room what “good” means in this course.


### Final Reinforcement Talking Points Before Debrief

**[Instructor speaks:]**

If I have one extra minute before the formal debrief, I want to say this very directly: an HTTP client is not “done” when it returns data once. It is much closer to done when another developer can read the wrapper function, understand the contract, and trust that the obvious failure paths were considered.

That means students should walk away from this hour with a new default instinct. When they see an API call in their own project, the automatic questions should be:

- Where is the timeout?
- What happens on 4xx and 5xx?
- What if the body is not valid JSON?
- What if the JSON shape changes?
- Where is the reusable wrapper?

If those questions become habits, this hour has paid off far beyond a single exercise.

## Section 6: Debrief & Exit Ticket (3 minutes)

### Group Debrief

**[Instructor speaks:]**

Bring students back together and anchor the main ideas.

Today was about making a Python program interact with a service responsibly. The technical skills matter, but the deeper habits matter more:

- set a timeout every time
- let status errors surface through `raise_for_status()`
- treat JSON as a contract, not a guess
- centralize request logic in a wrapper function
- show users a friendly message while logging useful detail for developers

If students only learn how to fetch a JSON payload, they have learned a trick. If they learn how to fetch data **safely and predictably**, they have learned an engineering habit.

**[Ask students:]** What failure case felt most surprising today: timeout, invalid JSON, or contract mismatch?

Invite one or two answers. Use those answers to reinforce that robust software is designed for imperfect conditions.

### Exit Ticket

**[Instructor asks:]**

1. What is the difference between a timeout and a retry?
2. Why is `response.raise_for_status()` usually cleaner than manually checking every status code branch?
3. What does it mean to say “JSON is a contract”?
4. Name one reason to put request logic inside a wrapper function.

**[Expected direction of answers:]**

- A timeout limits how long we wait for one attempt; a retry is a decision to try again after a failed attempt.
- `raise_for_status()` keeps success-path code cleaner and moves failures into structured exception handling.
- JSON being a contract means we validate required keys and expected types before trusting the data.
- A wrapper avoids duplication and gives us one place to manage timeouts, logging, and validation.

### Instructor Closing Line

**[Instructor speaks:]**

Next hour, we will stay connected to real application work, but we will shift from reliability in network calls to reliability in security habits. Keep today’s mindset with you: outside input should be handled carefully, not casually.
