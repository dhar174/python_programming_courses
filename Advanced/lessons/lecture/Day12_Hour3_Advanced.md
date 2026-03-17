# Day 12, Hour 3: Packaging and Delivery
**Python Programming Advanced - Session 12**

---

## Timing Overview
**Total Time:** 60 minutes  
- Reframe packaging as repeatable install and run: 5 minutes  
- Direct instruction on requirements, quickstart, and fresh-run checks: 15 minutes  
- Live demo of a clean install path: 10 minutes  
- Guided packaging lab: 25 minutes  
- Debrief and exit ticket: 5 minutes

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Explain the difference between \"it runs on my machine\" and a shippable deliverable
2. Create or refine `README.md`, `requirements.txt`, and `requirements-dev.txt`
3. Run the project from a fresh environment following documented steps
4. Identify missing dependencies or fragile file-path assumptions
5. Describe optional next steps such as wheel builds or executables without making them required

---

## Section 1: What Shipping Really Means (5 minutes)

### Opening Script

**[Instructor speaks:]**

Shipping is mostly not magic. It is repeatable install plus repeatable run. If another person cannot follow your README and get the project running, the project is not truly ready to hand off.

---

## Section 2: Direct Instruction on the Deliverable Recipe (15 minutes)

### Required Deliverable Pieces

Teach the runbook recipe:

- `README.md` with exact steps
- runtime dependencies in `requirements.txt`
- optional dev tooling in `requirements-dev.txt`
- `.gitignore` for environment and build outputs
- a verified entry point

### Fresh-Run Test

**[Instructor speaks:]**

The most honest packaging check is a fresh-run test in a new environment or folder. If you have to remember a hidden setup step, your documentation is incomplete.

### Optional Extras

Mention but do not require:

- `python -m build`
- wheel output
- PyInstaller executable

Keep reminding learners that the course minimum is a clear runnable source release.

---

## Section 3: Live Demo (10 minutes)

Show a quickstart sequence:

```bash
python -m venv .venv
.venv\\Scripts\\activate
python -m pip install -r requirements.txt
python -m pytest
python api/app.py
```

Then point at the README and say:

**[Instructor speaks:]**

If these steps are not written down clearly, the deliverable is weaker than you think.

---

## Section 4: Guided Packaging Lab (25 minutes)

### Lab Goal

**[Instructor speaks:]**

Make your project runnable by someone else. That means documentation, dependencies, and an honest smoke test.

### Required Tasks

1. update `README.md`
2. verify runtime dependencies
3. add or update dev dependencies
4. confirm `.gitignore` covers common env and build outputs
5. perform a fresh-run smoke test

### Coaching Prompts

- Could a teammate run this without asking you three questions?
- Which environment variables need to be documented?
- Which file paths might break outside your IDE?
- Are your dependencies complete or just locally installed?

### Common Mistakes

- missing dependency in `requirements.txt`
- undocumented environment variables
- entry point confusion between GUI, API, and scripts
- assuming a relative path that only works from one directory

### Recovery Script

**[Instructor speaks:]**

If packaging feels big, focus on the runnable source release. Make the README honest and the dependencies complete. That alone is a major professional improvement.

---

## Section 5: Debrief and Exit Ticket (5 minutes)

### Debrief Script

**[Instructor speaks:]**

Packaging is where a project becomes shareable. It is one of the clearest tests of whether your work is understandable beyond your own machine.

### Exit Ticket

1. What is the difference between \"it runs on my machine\" and \"it ships\"?
2. What file did you improve most today?
3. What did the fresh-run test reveal?

### Preview of the Final Hour

**[Instructor speaks:]**

Next hour is the final capstone demo, certification-style review, and retrospective. Today gives you the delivery confidence to finish well.

---

## Instructor Coaching Appendix

### Whiteboard Plan for Day 12

Draw three stacked layers on the board labeled `quality`, `delivery`, and `communication`. Under quality, write `pytest`, `coverage`, and `edge cases`. Under delivery, write `requirements`, `README`, `fresh run`, and `entrypoint`. Under communication, write `demo`, `explanation`, and `retrospective`. This visual helps learners understand that the final day is not a random collection of loose ends. It is the professional closeout sequence for the capstone.

Next, draw a short arrow from `tests` to `confidence`, from `packaging` to `shareability`, and from `demo` to `explainability`. Learners often undervalue explanation, but the final demo is where they prove they understand the system as a whole.

Keep the board visible during the whole day. When learners get lost in tool details, point back to the layer they are working on. Ask whether the current task is increasing quality, delivery confidence, or communication clarity.

### Listen-Fors During Labs

Positive Day 12 language includes:

- "This test proves a behavior, not just a line execution."
- "Coverage showed me a branch I actually care about."
- "I found a missing dependency during the fresh-run test."
- "The README now tells another person exactly how to start the project."
- "My demo flow shows the system, not every line of code."

Concerning language includes:

- "I am chasing 100 percent coverage because the number looks low."
- "I know it runs, but I have never tried it from a fresh environment."
- "The README is mostly fine if someone already knows the project."
- "I will explain the architecture if there is time after the live demo."
- "The packaging step broke something, so I stopped documenting it."

When you hear the concerning version, guide learners back with questions such as:

- "What important bug would this test actually catch?"
- "What did the fresh-run test teach you that local habits were hiding?"
- "Could a new teammate follow your README without you standing nearby?"
- "What is the one architecture decision you want the audience to understand?"
- "What part of the demo proves the project is reliable, not just feature-rich?"

### Common Misconceptions for Day 12

One misconception is that testing means proving the code is flawless. Reframe that quickly. Testing creates feedback and confidence; it does not promise perfection.

Another misconception is that coverage is the goal. Coverage is a diagnostic aid. The goal is meaningful confidence in the parts of the system most likely to fail or most expensive to debug.

A third misconception is that packaging is mostly about fancy build tools. The runbook says otherwise. Packaging starts with a repeatable install, a repeatable run, and complete documentation.

A fourth misconception is that final demos should show as many features as possible. Strong demos are selective. They show the most convincing end-to-end flow and explain the architecture behind it.

### Suggested Mini-Conferences for Each Hour

For Hour 45, ask learners which behavior they most want a test to guard. This keeps testing grounded in risk and value.

For Hour 46, ask what their coverage report changed in their priorities. If the answer is "nothing," they may be treating coverage as a formality instead of feedback.

For Hour 47, ask a learner to walk you through the README as if you were a new teammate. This is often the fastest way to expose missing setup steps.

For Hour 48, ask learners to practice one two-sentence explanation of their architecture before they demo. Students who can explain their system clearly almost always demo more effectively.

### Pacing Adjustments

If testing is behind in Hour 45, shrink the target to five focused tests with two negative cases. That is already meaningful and aligned to the runbook.

If Hour 46 becomes a chase for percentages, stop the class and restate the purpose of coverage. Then ask them to add one test for the highest-value gap and one integration-style test. That reset usually improves quality.

If packaging work in Hour 47 reveals bigger dependency or path issues, reduce optional build steps immediately. README clarity and fresh-run success are higher priority than wheels or executables.

If the final demo hour feels rushed, shorten the code-reading review rather than allowing every capstone demo to spill over. Timeboxing is part of the final professional skill being practiced.

### Evidence of Mastery for Day 12

Look for these signals:

- Tests clearly state the behavior they protect.
- Coverage is used to improve meaningful gaps, not just inflate a number.
- The project can be run from a fresh environment with documented steps.
- The learner can explain one architecture decision and one tradeoff.
- The final demo proves minimum deliverables without confusion.
- The retrospective includes one immediate application skill and one practice goal.

### End-of-Day Instructor Wrap Script

**[Instructor speaks:]**

The final day is where all the hidden professional habits become visible. You tested the right things, measured what still needed attention, made the project runnable by someone else, and explained the system clearly in front of an audience. Those skills are not extras. They are how technical work becomes dependable and shareable. Leave this course remembering that the best project is not only one that works. It is one that can be tested, packaged, explained, and improved.

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

---

## Final Delivery Appendix

### Demo Coaching for Anxious Learners

Many learners finish the project with a working system but a shaky explanation. Help them rehearse a simple verbal pattern:

1. "My project helps users..."
2. "The core layers are..."
3. "Here is one end-to-end workflow..."
4. "Here is how I tested or packaged it..."
5. "One tradeoff I made was..."

This pattern keeps demos focused and reduces the tendency to wander into low-value details.

### Fast Review Prompts for the Final Day

Use prompts like these to keep the final session thoughtful:

- Which test gives you the most confidence right now?
- What did the fresh-run packaging check reveal?
- Which architecture decision are you most comfortable defending?
- What is one edge case your project now handles well?
- What would be the first improvement after the course ends?

These prompts work both during rehearsal and during retrospective discussion.

### What to Praise Explicitly

On the final day, praise not only visible features but also the habits that made them reliable. Good examples include:

- a clean negative test
- a corrected dependency list
- a clear README quickstart
- a demo that shows the source of truth honestly
- a student who trimmed scope to protect stability

Calling out these habits helps learners understand what professional quality looks like.

### Closing Reflection for Day 12

If you want a stronger ending, use this script:

**[Instructor speaks:]**

A complete technical project is more than functioning code. It is code that can be checked, explained, shared, and improved. The reason we finished with testing, coverage, packaging, and reflection is that these practices turn isolated effort into dependable work. Carry that lesson forward. The tools may change, but the habit of building something understandable and verifiable will keep paying off.

---

## Certification Review Appendix

### Quick Code-Reading Prompts

Keep two or three short prompts available for the final session so you can shift smoothly between demos and review. Good prompts include predicting the output of a small class example, identifying which exception will be raised, or explaining what happens when a module-level constant is changed before a function call. The goal is not to trick learners. The goal is to practice calm reading and reasoning under light pressure.

After each prompt, ask not only for the answer but also for the reasoning path. Students benefit from hearing how a careful reader notices state changes, method calls, and exception boundaries.

### Retrospective Questions That Lead to Action

Avoid retrospective questions that invite only vague positivity. Use prompts that point toward action:

- Which concept from the course will you apply in your next real project?
- Which concept is still shaky enough that you want one more mini-project for practice?
- Which artifact from your capstone best demonstrates your current level?
- What debugging or testing habit changed the way you work?

These questions make the final hour feel forward-looking rather than purely ceremonial.

### Final Closing Script

**[Instructor speaks:]**

You are leaving this course with more than a collection of files. You are leaving with a way of thinking about Python work: build in layers, make behavior testable, handle errors honestly, package the work so others can run it, and explain your tradeoffs clearly. That combination is what turns learning into capability.
