# Day 4, Hour 2: Security Basics – Environment Variables, Safe Secrets Habits, and Hashing Concepts
**Python Programming Advanced – Session 4**

---

## Timing Overview
**Total Time:** 60 minutes  
- Recap & Security Mindset Reset: 5 minutes
- Core Concepts (secrets, env vars, hard-coded risk): 12 minutes
- Hashing vs encryption at a high level: 10 minutes
- Live Demo (env var loading + gated admin action): 10 minutes
- Hands-On Lab (secure-ish configuration): 18 minutes
- Debrief & Exit Ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, you will be able to:
1. Explain why secrets should not be hard-coded into source files or committed to version control
2. Load configuration such as an API key or admin key from environment variables
3. Create a `.env.example` template with placeholders rather than real secrets
4. Describe the difference between hashing and encryption at a conceptual level
5. Use `hashlib.sha256` in a classroom-safe comparison demo while understanding its limited scope here
6. Update `.gitignore` guidance so local secret files are not committed
7. Add a README note telling users to set environment variables before running admin actions
8. Build an admin-only action that is gated by configuration rather than a hard-coded value

---

## Section 1: Recap & Security Mindset Reset (5 minutes)

### Connecting to the Previous Hour

**[Instructor speaks:]**

Last hour we talked about consuming data from outside our program. That forced us to think carefully about reliability: timeouts, status codes, JSON parsing, and response validation. This hour introduces a similar mindset, but from a security angle.

Security basics are not about turning everyone into a security engineer in sixty minutes. Security basics are about developing habits that prevent very common, very avoidable mistakes. In other words, today is less about advanced cryptography and more about refusing to do the unsafe obvious thing.

The unsafe obvious thing might be:

- putting a secret directly in code
- copying a real key into a demo file
- committing a local `.env` file by accident
- confusing hashing with encryption
- promising a level of security a classroom demo does not really provide

So I want to set the tone very clearly: **we are staying in appropriate scope**. We are covering good configuration habits, basic terminology, and a small comparison-only hashing demonstration. We are **not** implementing OAuth. We are **not** implementing JWT flows. We are **not** building a production authentication system.

That boundary is important. Good engineers know what they know, what they do not know yet, and what is out of scope.

### Framing Question

**[Ask students:]** If you find a secret key directly inside a source file in a repository, what risks come to mind?

[Pause. Collect 3–4 answers.]

Good answers usually include accidental leaks, hard-to-rotate credentials, insecure sharing, and secrets ending up in commit history forever.

---

## Section 2: Core Concepts – Secrets, Configuration, and Hard-Coded Risk (12 minutes)

### What Counts as a Secret?

**[Instructor speaks:]**

In this context, a secret is any value that should not be exposed publicly or casually shared. That might include:

- API keys
- database passwords
- admin tokens
- service credentials
- signing keys

Not every configuration value is secret. A port number might be configuration but not secret. A feature flag might be configuration but not secret. Students need to distinguish “settings” from “sensitive settings,” while also understanding that both are often loaded from the environment for flexibility.

### Why Hard-Coding Secrets Is a Problem

**[Instructor speaks:]**

Hard-coding means we literally write the secret into the source code:

```python
ADMIN_KEY = "super-secret-real-key"
```

It is easy. It is fast. It is also a bad idea.

Problems with hard-coded secrets include:

1. **They get committed to version control.** Even if you remove the line later, the secret may still exist in commit history.
2. **They spread through screenshots, code reviews, examples, and copy/paste.**
3. **They are difficult to rotate.** If the key changes, you now need a code change and redeploy instead of a configuration change.
4. **They encourage unsafe team habits.** Students start to treat secrets like normal text.

The safe habit is to load secrets from environment variables or another approved configuration mechanism.

### Environment Variables as a Simple, Practical Pattern

**[Instructor speaks:]**

Environment variables let the operating environment provide values at runtime. The code asks for a value by name; the value is not stored in the source file itself.

In Python, the basic access pattern uses `os.environ`:

```python
import os

api_key = os.environ.get("APP_API_KEY")
```

This gives us a much healthier separation:

- code defines **what configuration is needed**
- the environment supplies **the actual value**

We should still validate the value exists. Quietly getting `None` and stumbling later is not friendly. A helper function makes that better.

```python
import os


def get_required_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value
```

### A `.env.example` File Is a Template, Not a Secret Store

**[Instructor speaks:]**

In many projects, developers use a local `.env` file during development. In this course, teach the pattern carefully:

- `.env.example` may be committed
- `.env` should usually be ignored
- `.env.example` contains placeholders, never real secrets

A good example template looks like this:

```env
APP_API_KEY=your-api-key-here
APP_ADMIN_KEY=replace-with-local-admin-key
APP_ENV=development
```

This tells collaborators what variables they need without exposing actual values.

### `.gitignore` and README Guidance

**[Instructor speaks:]**

Good secret hygiene is not just code. It includes project scaffolding.

In `.gitignore`, exclude local secret files such as:

```gitignore
.env
.env.local
.env.development
.env.production
!.env.example
secrets.json
local_settings.json
```

In the README, they should add a note such as:

> Set the required environment variables before running admin actions or API-enabled scripts.

That is simple, but it prevents confusion and encodes the right operational habit.

---

## Section 3: Hashing vs Encryption – High-Level Only (10 minutes)

### The Big Conceptual Difference

**[Instructor speaks:]**

Students often hear words like hashing and encryption as if they are interchangeable. They are not.

- **Encryption** is designed to be reversible when you have the right key.
- **Hashing** is designed to be one-way.

A hash function takes input and produces a digest. The key idea for this lesson is that you do not “decrypt” a hash back into the original value. Instead, one common pattern is to hash a new input and compare the digest to a stored digest.

Because this is an introductory security hour, keep this conceptual. We are not building a production password system today. We are using hashing to teach the one-way idea and to reinforce the difference from plain-text comparison.

### Why Scope Discipline Matters

**[Instructor speaks:]**

I want to model careful language here. If we demo `hashlib.sha256`, that does **not** mean we have taught full password security. It means we have demonstrated the concept of one-way hashing and digest comparison.

If students ask about production password storage, the accurate answer is that real systems use stronger, purpose-built password hashing approaches and broader security design practices. But those are beyond this lesson.

### `sha256` Demo for Comparison-Only Use

**[Instructor speaks:]**

Here is the classroom-safe pattern we will show:

```python
from __future__ import annotations

import hashlib
import secrets


def sha256_digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


admin_key = "demo-admin-key"
provided_key = "demo-admin-key"

expected_digest = sha256_digest(admin_key)
provided_digest = sha256_digest(provided_key)

print(secrets.compare_digest(expected_digest, provided_digest))
```

The point of this demo is not that we now have “security solved.” The point is that a hash digest can be compared without printing or storing the original value directly in application logic. Using `secrets.compare_digest(...)` also models a safer constant-time comparison habit.

**[Prediction prompt:]** If I change one character in the input, do you expect a small change in the digest or a completely different digest-looking string?

[Pause.]

Right. The digest changes dramatically. That property helps students understand why hashes are used as fingerprints of input.

### Important Scope Reminder

**[Instructor speaks:]**

Say this plainly: in this course hour, `sha256` is a **concept demo for comparison-only use**. We are not implementing OAuth. We are not implementing JWT. We are not designing a secure identity system. If students bring those up, welcome the curiosity and then protect the scope.

---

## Section 4: Live Demo – Environment Variables + Gated Admin Action (10 minutes)

### Demo Goal

**[Instructor speaks:]**

I am going to show a tiny script that:

- loads an admin key from an environment variable
- accepts a provided key value
- compares digests for demonstration purposes
- logs the attempt
- denies the admin action if the key is wrong

Again, this is a habits demo, not a production auth system.

```python
from __future__ import annotations

import hashlib
import logging
import os
import secrets

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)


def get_required_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def sha256_digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def run_admin_action(provided_key: str) -> None:
    expected_key = get_required_env("APP_ADMIN_KEY")

    if not secrets.compare_digest(
        sha256_digest(provided_key),
        sha256_digest(expected_key),
    ):
        logger.warning("Admin action denied due to invalid key.")
        print("Admin action denied.")
        return

    logger.info("Admin action approved.")
    print("Admin action completed.")


def main() -> None:
    provided_key = input("Enter admin key: ")
    run_admin_action(provided_key)


if __name__ == "__main__":
    main()
```

### Demo Narration

**[Instructor speaks:]**

Walk students through the helper function first. Explain why failing early on a missing environment variable is better than silently continuing with bad configuration.

Then highlight the logging. The user sees “Admin action denied,” while the log captures the event for later review. This is a nice bridge between security and observability.

Then talk about the digest comparison. Be explicit that we are demonstrating the concept of comparing one-way digests rather than storing or reusing a plain-text value directly in business logic, and point out that `secrets.compare_digest(...)` is the safer comparison helper to model.

**[Instructor action:]** Show, but do not commit, example setup guidance:

```bash
export APP_ADMIN_KEY="replace-with-local-value"
python admin_demo.py
```

Show an accompanying `.env.example` file content on screen:

```env
APP_ADMIN_KEY=replace-with-local-admin-key
APP_API_KEY=replace-with-local-api-key
```

Show `.gitignore` guidance:

```gitignore
.env
.env.local
.env.development
.env.production
!.env.example
```

Show the README note:

```markdown
## Configuration
Set the required environment variables before running admin actions.
```

### Questions to Ask During the Demo

**[Ask students:]**

- What would be wrong with placing `APP_ADMIN_KEY = "real-secret"` in the Python file?
- Why is `.env.example` safe to commit when it contains placeholders only?
- Why is logging an admin-denied event useful even if the program already printed a message?

These questions make the demo about reasoning, not imitation.

---

## Section 5: Hands-On Lab – Secure-ish Configuration (18 minutes)

### Lab Framing

**[Instructor speaks:]**

Students now apply the pattern in their own project context. The scope is intentionally modest and realistic.

They are not building login systems. They are making their code stop depending on hard-coded secrets.

### Student Task

**Lab: Secure-ish Configuration**

Students should:

- add support for an API key or admin key read from an environment variable
- implement a simple admin-only action gated by that key
- avoid hard-coding the secret in code or commits
- create `.env.example` with placeholder values only
- update `.gitignore` to exclude `.env` and similar local secret files
- add a README note telling users to set environment variables before running admin actions
- log whether the admin action was approved or denied

### Completion Criteria

A student solution is complete when:

- the key is loaded from environment or config rather than source code
- the admin action is gated correctly
- `.env.example` exists with placeholders only
- `.gitignore` guidance prevents local secret files from being committed
- the README includes a configuration note
- an allow or deny event is logged

### Circulation Notes

**[Circulate:]**

Look for these common issues first:

1. A real-looking key still appears in code.
2. The student created `.env.example` but accidentally put an actual value in it.
3. The code uses `os.environ["NAME"]` without a friendly failure message if the variable is missing.
4. The student logs the actual secret value. Stop that immediately; logs should record the event, not the secret.
5. The student begins drifting toward JWT or OAuth discussion and loses the assignment scope.

If a student is stuck, give them a checklist:

- first, write `get_required_env()`
- second, use it in one admin function
- third, create `.env.example`
- fourth, update `.gitignore`
- fifth, add one README note

That sequence keeps the lab manageable.

### Common Pitfalls to Watch For

- Accidentally committing secrets.
- Printing secret values during debugging.
- Confusing hashing with encryption.
- Assuming a hash demo equals a production password system.
- Forgetting to document required variables for future users.
- Using local configuration files without adding ignore rules.

### Optional Extensions

If a student finishes early, allow one of these safe extensions:

- add a second required environment variable such as `APP_ENV`
- create a small configuration module that loads multiple values
- add a “configuration check” command that reports missing variables without revealing their values
- add more structured logging messages

Do **not** turn extensions into a full authentication project. Protect the lesson boundary.

---


### Security Habit Checklist for Everyday Development

**[Instructor speaks:]**

Before we wrap this lab, I want to give students a checklist they can reuse long after this session. Security can feel abstract until it becomes a small set of repeatable questions.

When you are about to add configuration or a privileged action, ask:

1. Is this value sensitive, or is it just configuration?
2. If it is sensitive, does it appear anywhere in source code, screenshots, or commit history?
3. If I rotate the value tomorrow, can I do it without changing code?
4. Have I documented what variable names are required?
5. Did I add local secret files to `.gitignore`?
6. Did I accidentally log or print the secret value?
7. Does the README tell another developer how to configure the project safely?

This checklist is intentionally simple. The point is not exhaustive security review. The point is to stop predictable mistakes before they happen.

### Environment Variables Are Better, Not Magical

**[Instructor speaks:]**

Students sometimes hear “use environment variables” and conclude that the problem is fully solved. This is a good place to teach nuance.

Environment variables are better than hard-coded secrets because they separate code from sensitive values and make rotation easier. But they are not magic. You still need to:

- avoid printing them
- avoid checking local secret files into version control
- document required names clearly
- avoid pasting real values into examples or chat threads

The mental model I want students to keep is this: environment variables are a safer delivery mechanism, not a substitute for judgment.

### What to Do If a Secret Is Accidentally Committed

**[Instructor speaks:]**

This is an excellent short discussion prompt because it moves security from theory to incident response.

If a secret is accidentally committed, the fix is not “delete the line and move on.” The correct mindset is:

- assume the secret is exposed
- rotate or replace it
- remove it from the current codebase
- update `.gitignore` or workflow habits so it does not happen again
- inform the right people if the repository is shared

Students do not need a full incident response playbook, but they do need the instinct that exposed secrets should be treated as compromised.

### Instructor Response Guide for Common Questions

**Question: “Can I just keep the key in a Python constant for now because this is only local?”**

**[Instructor response:]**

For a throwaway scratch file, students may be tempted to do that, but this course is teaching habits that transfer to real projects. If the project is important enough to save, it is important enough to configure safely.

**Question: “Why do we commit `.env.example` if `.env` is ignored?”**

**[Instructor response:]**

Because collaborators need to know what variables exist. The example file is documentation. The real file is local configuration.

**Question: “Why not just print the loaded key to prove it worked?”**

**[Instructor response:]**

Because debugging should not normalize exposing secrets. Prove it worked by confirming the variable exists or by showing downstream behavior, not by displaying the secret value.

**Question: “Should we implement JWT or OAuth for our capstone now?”**

**[Instructor response:]**

No. That is intentionally out of scope for this hour. Your job right now is to demonstrate sound foundational habits: environment-based configuration, secret hygiene, and a clear boundary around admin actions.

### Instructor Mini-Scenario Discussion

**[Instructor speaks:]**

Use these quick scenarios to test student judgment:

**Scenario 1:** A teammate adds `API_KEY = "12345"` directly in `services.py` so the demo works faster.

Ask: What should happen next?

Expected direction: remove it, rotate if real, move configuration to environment, update docs.

**Scenario 2:** A student adds `.env.example` with an actual working secret copied from their machine.

Ask: Why is that still a problem even though the file name says “example”?

Expected direction: the filename does not make the value safe; the content matters.

**Scenario 3:** The app logs “Admin action denied for key abc123.”

Ask: What is wrong with that log entry?

Expected direction: the event is worth logging; the secret value is not.

**Scenario 4:** The student says, “We hashed the key with sha256, so now we have secure authentication.”

Ask: What is too broad or inaccurate about that claim?

Expected direction: the lesson demonstrates one-way hashing concepts, not a complete authentication system.

### Suggested Instructor Language for Scope Control

**[Instructor speaks:]**

Security conversations can expand quickly. Here are phrases that help keep the lesson on track without shutting down curiosity:

- “That is a great advanced topic, and we are intentionally keeping today’s scope smaller.”
- “For this checkpoint, I care more that your secret is not hard-coded than that you design a full auth workflow.”
- “Let’s separate foundation from extension. Foundation is env-based config and secret hygiene. Extension is advanced auth.”
- “I want you to leave with safe defaults, not a false sense that we solved security in one hour.”

These lines help students feel respected while staying focused.

### Strong Solution Characteristics to Highlight Publicly

**[Instructor speaks:]**

When you debrief the room, call out solutions that demonstrate maturity in small ways:

- missing env vars produce clear setup guidance
- `.env.example` contains placeholders only
- `.gitignore` protects local files
- README notes tell another person how to run the project safely
- logs record security-relevant events without exposing secrets

Those are the habits we want to normalize.


### Final Reinforcement Before Debrief

**[Instructor speaks:]**

One more idea I want to anchor before we close: security basics are often invisible when they are done well. No one applauds a missing hard-coded key the way they might applaud a flashy dashboard, but professional projects depend on these quiet decisions.

Students should leave this hour understanding that project quality includes operational habits:

- the codebase does not teach unsafe examples
- the repository does not invite accidental leaks
- the README helps the next person configure the project safely
- admin behavior is protected by configuration rather than trust or luck

If they internalize that security is partly about avoiding preventable mistakes, then this hour has accomplished exactly what it should.

### Short Reflection Prompt if Time Remains

**[Instructor speaks:]**

Ask students to write one sentence completing each prompt:

- “The most important secret-handling habit I learned today is ________.”
- “The easiest mistake to make in a small project is ________.”
- “One thing I will change in my own workflow is ________.”

This gives the lesson a personal action step instead of leaving it as abstract advice.


### Safe Demo Practices in the Classroom

**[Instructor speaks:]**

Because this is a security-flavored hour, I also want to model safe demonstration habits, not just safe application code. Students notice what instructors normalize.

If I am projecting code or terminal commands, I should avoid using anything that looks like a real secret. Use placeholder values that are obviously fake. Use names like `replace-with-local-value` or `demo-only-key`. That matters because students often copy examples literally, and a casual-looking “temporary” real key can become part of their workflow much faster than expected.

When demonstrating environment variables, narrate the process explicitly:

- “I am setting a local value for demonstration.”
- “This is not a real credential.”
- “In a team project, each developer would use their own local configuration.”

That narration teaches operational context, not just syntax.

Another helpful classroom move is to avoid reward language around shortcuts. If a student says, “I just hard-coded it because it was faster,” do not reinforce that with “That’s fine for now.” Instead say, “I understand why that felt faster, and this is exactly the point where we practice the safer habit instead.”

This keeps the classroom from accidentally teaching that security only matters when a project becomes “serious enough.” Habits are formed much earlier than that.

### Mini Debrief Questions for Stronger Discussion

**[Instructor speaks:]**

If the room is engaged and you want a stronger whole-group discussion before the exit ticket, ask one or two of these:

- What is the difference between a project that is easy to run and a project that is easy to run safely?
- Why is configuration documentation part of security hygiene?
- What kinds of mistakes happen when teams treat secrets like normal strings?
- Why is “just for local testing” often the beginning of long-lived bad habits?

These questions help students connect security habits to teamwork, maintenance, and professionalism rather than seeing them as isolated technical trivia.


### Final Instructor Checklist for Review

**[Instructor speaks:]**

As a final pass during circulation, I can review a student solution in under a minute with this checklist:

- Can I point to the environment variable name in code?
- Can I point to a helpful error message when it is missing?
- Can I point to `.env.example` with placeholder values only?
- Can I point to `.gitignore` coverage for local secret files?
- Can I point to the README note about configuration?
- Can I point to an admin action that is gated and logged?

This quick review keeps assessment aligned to the runbook rather than drifting into unrelated security topics.


### One-Sentence Takeaway to Repeat Aloud

**[Instructor speaks:]**

If students remember one sentence from this hour, let it be this: **keep secrets out of code, document configuration clearly, and never confuse a classroom demo with a complete security system.**


Add one final reminder: placeholders belong in shared examples, while real values belong only in local runtime configuration. That distinction is simple, practical, and worth repeating.

## Section 6: Debrief & Exit Ticket (5 minutes)

### Group Debrief

**[Instructor speaks:]**

Today’s lesson was about disciplined security habits. The goal was not to make students experts in cryptography. The goal was to eliminate easy mistakes and replace them with healthier defaults.

The habits to reinforce are:

- keep secrets out of source code
- use environment variables for sensitive configuration
- commit `.env.example`, not `.env`
- update `.gitignore` intentionally
- document configuration in the README
- understand hashing as a one-way concept
- avoid claiming more security than the code actually provides

**[Ask students:]** Which one of those habits feels easiest to adopt immediately in your own work? Which one feels easiest to forget?

Let them answer briefly. This helps move the lesson from abstract advice into future behavior.

### Exit Ticket

**[Instructor asks:]**

1. Why is hashing not reversible, and why is that useful?
2. Why is a `.env.example` file safe to commit when it contains placeholders only?
3. What is one risk of hard-coding a secret into a Python file?
4. Why are OAuth and JWT intentionally out of scope for this hour?

**[Expected direction of answers:]**

- Hashing is designed as a one-way transformation, which makes it useful for comparison-style checks without recovering the original value.
- `.env.example` teaches required variable names without exposing real secrets.
- Hard-coded secrets can leak into version control, history, screenshots, and shared code.
- OAuth and JWT are larger topics; this hour focuses on basic, practical secret-handling habits.

### Instructor Closing Line

**[Instructor speaks:]**

In the next hour, we shift from implementation habits to project planning. Good engineering is not just secure code and working code; it is also knowing how to scope, sequence, and deliver a project you can actually finish.
