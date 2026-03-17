# Day 10, Hour 4: Checkpoint 5 - API Milestone Demo
**Python Programming Advanced - Session 10**

---

## Timing Overview
**Total Time:** 60 minutes  
- Frame the checkpoint and success criteria: 10 minutes  
- Show the demo checklist: 5 minutes  
- Independent stabilization and rehearsal: 35 minutes  
- Showcase, reflection, and exit ticket: 10 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Demonstrate a working Flask API backed by SQLite
2. Show consistent JSON errors and an API key gate on write operations
3. Explain how the API connects to the service and repository layers
4. Identify the most fragile part of their current API milestone
5. Evaluate the milestone against correctness, structure, persistence, and maintainability

---

## Instructor Prep Notes

- Keep the checkpoint flow focused on the runbook requirements: CRUD, SQLite, JSON errors, API key gate, optional client
- Have a fast-grade sequence ready
- Encourage learners to stabilize instead of adding new features in the middle of the checkpoint

---

## Section 1: Frame the Milestone (10 minutes)

### Opening Script

**[Instructor speaks:]**

This checkpoint validates whether your API is not only present, but trustworthy. A trustworthy API responds predictably, protects the right operations, and still uses the same stable service and persistence layers underneath.

For this milestone, I am looking for:

- Flask API with CRUD routes
- SQLite-backed persistence
- consistent JSON error responses
- API key protection on write operations
- optional Python client, if you built one

### What Counts as Success

**[Instructor speaks:]**

Success today is not a giant feature list. Success is a believable demo where the API behaves consistently and you can explain the architecture behind it.

---

## Section 2: Show the Demo Checklist (5 minutes)

### Fast-Grade Sequence

Use this quick sequence:

1. `GET /health`
2. `GET /records`
3. `POST /records` with a valid API key
4. `PUT /records/<id>` with a valid API key
5. `DELETE /records/<id>` with a valid API key
6. one missing or invalid key failure
7. one invalid input or not-found failure

Then say:

**[Instructor speaks:]**

If your API can survive that sequence with clean responses, it is in strong shape for this checkpoint.

---

## Section 3: Stabilization and Rehearsal Time (35 minutes)

### Build Goal

**[Instructor speaks:]**

Use this time to rehearse and stabilize. Remove guesswork from the demo. Confirm your commands, sample payloads, headers, and expected status codes before you are on the clock.

### Suggested Validation Checklist

```text
[ ] API starts reliably
[ ] /health returns JSON
[ ] List route works
[ ] Create route returns 201
[ ] Update route returns 200
[ ] Delete route returns 200
[ ] Invalid input returns 400 with JSON error
[ ] Missing or wrong key returns 401/403 with JSON error
[ ] Data persists in SQLite
```

### Common Failure Modes

- route returns HTML error page instead of JSON
- one write route forgot the API key check
- service exception is not caught cleanly
- test payload does not match the parser contract
- database path differs between environments

### Coaching Prompts

- Which route are you least confident about?
- Can you explain the difference between a validation failure and a missing resource?
- Where is the API key loaded?
- Where is the repository constructed?
- What evidence do you have that SQLite is the source of truth?

### Recovery Script

**[Instructor speaks:]**

If one route is unstable, do not keep guessing in the interface. Reproduce the behavior in the smallest possible test. Then work outward again. Stable demos come from narrowing uncertainty, not from clicking faster.

---

## Section 4: Showcase and Reflection (10 minutes)

### Showcase Format

Invite a few learners or groups to show:

1. health
2. one successful write
3. one protected failure
4. one explanation of architecture

Keep demos short so the energy stays up.

### Reflection Questions

- What part of your API feels strongest?
- What part still feels fragile?
- What design choice saved you time today?
- What would you improve first if you had one extra hour?

---

## Section 5: Exit Ticket and Transition (5 minutes)

### Exit Ticket

1. What made your API milestone feel maintainable, not just functional?
2. Which failure case was most useful to test?
3. What is one thing you will carry into the analytics session next?

### Transition

**[Instructor speaks:]**

Next session we pivot into data analysis and reporting. Because your application now stores structured data cleanly, you can export, summarize, visualize, and report on it in a meaningful way.

---

## Instructor Coaching Appendix

### Whiteboard Plan for Day 10

Draw two diagrams side by side. On the left, write `client -> API -> service -> repository -> database`. On the right, write `GUI -> service -> repository -> database` and `API -> service -> repository -> database`. Explain that Day 10 is partly about security at the API boundary and partly about making an intentional decision about how the GUI and API surfaces fit together.

Next, write three labels near the API boundary: `headers`, `status codes`, and `timeouts`. Tell learners that these three concerns become much more visible once they stop calling the service layer directly and begin interacting through HTTP. Write `X-API-Key` near the header label, `401/403` near status codes, and `timeout=5` near client behavior. These small notes help students connect security, client design, and integration in one picture instead of treating them as disconnected topics.

For the checkpoint hour, circle the entire system and write `trustworthy flow`. That phrase is useful because the API milestone is really testing whether the whole system can be trusted from the outside: does it protect writes, return structured failures, keep persistence stable, and still tell a coherent architectural story?

### Listen-Fors During Labs

Positive signals on Day 10 include statements like:

- "The API key is loaded from configuration, not hard-coded."
- "The client has a default timeout so the GUI will not hang forever."
- "We chose the parallel architecture because it was the safest way to keep the milestone stable."
- "The GUI and API both talk to the same underlying data store."
- "I tested missing credentials and wrong credentials separately."

Warning signs include:

- "I pasted the key into the source file for now."
- "I forgot to protect `DELETE` but the others are fine."
- "The client works if the API is perfect, but I did not test failure cases."
- "The GUI and API are using slightly different field names, but I think it is okay."
- "We ended up with two different database files because one path was easier."

When you hear a warning sign, use questions that restore system thinking:

- "Which layer should know about HTTP headers?"
- "How does the client behave when the server is slow or down?"
- "What tradeoff made this architecture choice the right one for your project today?"
- "How can you prove both surfaces are really connected to the same source of truth?"
- "Which route would you trust the least in a live demo, and why?"

### Common Misconceptions for Day 10

One misconception is that adding an API key makes the application secure in a complete sense. Correct that quickly. An API key gate is a useful boundary control for the course, but it is not a full identity and authorization system.

Another misconception is that GUI-to-API is automatically the more advanced and therefore better architecture. The more honest framing is that it is one possible architecture with more moving parts. Sometimes the parallel GUI and API approach is the stronger decision because it reduces risk while still demonstrating reuse of the core layers.

A third misconception is that client code is mostly a convenience wrapper. In reality, client code often reveals the user experience of an API very clearly. If timeouts are missing, errors are confusing, or response shapes are inconsistent, the client makes those weaknesses visible immediately.

A fourth misconception is that checkpoint hours should be used to add last-minute features. The opposite is usually true. Checkpoint hours should be used to reduce uncertainty, rehearse realistic demo flows, and stabilize the parts most likely to fail under observation.

### Suggested Mini-Conferences for Each Hour

For Hour 37, ask a learner to point to the exact place the API key is loaded and the exact place it is checked. This tells you quickly whether they understand boundary-level authorization or just copied a snippet.

For Hour 38, ask learners what happens if the request times out. If they cannot answer, they may have written a client that only handles the perfect case.

For Hour 39, ask learners to defend their integration choice in one or two sentences. If they say, "I just started wiring things and this is what happened," push them gently toward a more intentional decision.

For Hour 40, ask learners to rehearse the first thirty seconds of their demo. Strong milestones usually begin with clear framing: what the system does, how it is protected, and which path they are about to demonstrate.

### Pacing Adjustments

If students are still shaky on the Day 9 API, slow down Hour 37 and focus on protecting one write route first. The habit matters more than the number of lines covered.

If the client work in Hour 38 becomes too scattered, narrow the requirement to `list_records` and `create_record`. Those two functions often reveal the important issues with base URLs, headers, and timeouts.

If Hour 39 becomes a debate about architecture style, bring the class back to the runbook's practical framing. The question is not which architecture wins a blog post. The question is which architecture produces a coherent, demo-ready capstone in the available time.

If the checkpoint hour reveals many small failures, convert the last part of the session into guided rehearsal. A milestone demo improves dramatically when students have practiced the exact sequence they plan to show.

### Evidence of Mastery for Day 10

Look for these evidence points:

- Write operations are protected consistently.
- The key is loaded safely from configuration.
- The client includes timeouts and can handle at least a few failure cases.
- The integration choice is visible and intentional.
- The demo proves persistence and security behavior together.
- The learner can explain architecture from the outside in, not only from the source code out.

A very strong student can also explain what they deliberately did not build because it would have increased risk without adding enough value for the course milestone.

### End-of-Day Instructor Wrap Script

**[Instructor speaks:]**

Today was about trust at the system boundary. You protected writes, consumed your own API from the outside, and made an intentional architecture decision about how your interfaces fit together. Those are not cosmetic improvements. They are the things that make an application believable when someone else uses it. If your API now behaves predictably, protects the right paths, and still tells a coherent story with the rest of the capstone, then you are exactly where you need to be heading into analytics and final delivery work.

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
