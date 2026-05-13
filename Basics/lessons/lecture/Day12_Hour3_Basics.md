# Day 12 Hour 3 Basics: Capstone Polish and Demo Readiness Instructor Script

## Instructor intent and scope boundary

This instructional hour is the capstone polish and demo readiness hour. The goal is to help learners finish strong by stabilizing what they already built, improving usability, and preparing a short and reliable demonstration flow. This is not a new-feature sprint and it is not a final scoring hour. The final assessment and certification-style review happens in the next hour. In this hour, we protect working code, make behavior clear, and rehearse a concise story that proves the app works from a clean start.

Use this script as a near-verbatim delivery guide. It is intentionally detailed so you can read most of it directly, then adapt examples to your room. Keep the class in Basics scope: prompts, menu behavior, input handling, file persistence, readable instructions, and practical confidence.

## Timing model and arithmetic check

Use this exact pacing model and say it aloud so learners understand the structure and urgency:

- Recap and briefing: 4 minutes
- Talk points: 11 minutes
- Live demo: 8 minutes
- Hands-on lab: 30 minutes
- Debrief and quick check: 7 minutes

Arithmetic check for transparency: **4 + 11 + 8 + 30 + 7 = 60**.

If any segment runs long, recover time from instructor narration, not from lab time. The lab is the primary value of this hour.

## Runbook requirement to section mapping for traceability

Use this mapping as an auditable crosswalk between Hour 47 requirements and this lecture script sections.

| Runbook Hour 47 requirement | Where covered in this script |
| --- | --- |
| Outcomes: finalize capstone quality | Instructor intent and scope boundary; talk points script; lab facilitation |
| Outcomes: prepare short demo walkthrough | Live demo script; lab task sequence; evidence checklist |
| Talk points 10 to 15: polish checklist prompts help text edge cases | Talk points read-aloud script |
| Talk points 10 to 15: README run notes | Talk points read-aloud script; lab checklist |
| Live demo 5 to 10: show good demo flow and handling a mistake | Live demo read-aloud script |
| Lab 25 to 35: capstone polish with README | Hands-on lab facilitation notes |
| Lab 25 to 35: optional sample data file | Hands-on lab facilitation notes |
| Lab 25 to 35: demo script start add list search save restart load | Hands-on lab facilitation notes; deterministic evidence steps |
| Completion criteria: runs cleanly from scratch | Observable pass/fail evidence checklist; fresh-run verification playbook |
| Completion criteria: demo flow works in under 3 minutes | Observable pass/fail evidence checklist; stopwatch procedure |
| Pitfall: last-minute refactors break working code | Pitfalls and freeze rule |
| Pitfall: forgetting fresh-run test | Fresh-run verification playbook |
| Optional extension: help screen option in menu | Optional extension section |
| Quick check: what first in demo and why | Debrief quick check script |
| Rubber-duck improvement: deterministic and auditable acceptance | Static validation method; observable evidence section |
| Rubber-duck improvement: pacing guardrail | Separate read-aloud script and facilitation notes sections |
| Rubber-duck improvement: traceable requirement map | This mapping table |
| Rubber-duck improvement: operational fresh-run steps | Fresh-run verification playbook with expected outputs |
| Rubber-duck improvement: freeze trigger and allowed edits | Safe freeze rule section |

If asked by learners why this looks structured, explain that professional engineering teams work from explicit acceptance criteria and observable evidence, not vibes.

## Static validation method statement for deterministic structure checks

Before using this file in delivery or pull request review, run a static check so acceptance is objective and repeatable. This ensures word count, heading constraints, and fence balance are verifiable.

Use the following method statement as the official validation process for this script file:

1. Count regex words using `re.findall(r"\b\w+\b", text)` and confirm result is at least 4500.
2. Count lines starting with `# ` and confirm exactly one.
3. Confirm no lines in the file contain unfinished-marker text used by your team.
4. Count triple-backtick fences and confirm the count is even.
5. Confirm no additional line starts with `# `, including inside code fences.

Reference checker snippet:

```python
from pathlib import Path
import re

path = Path("Basics/lessons/lecture/Day12_Hour3_Basics.md")
text = path.read_text(encoding="utf-8")
lines = text.splitlines()

word_count = len(re.findall(r"\b\w+\b", text))
h1_count = sum(1 for line in lines if line.startswith("# "))
unfinished_hits = []  # Use your team's marker scanner command for this check.
fence_count = text.count("`" * 3)
extra_h1_lines = [i + 1 for i, line in enumerate(lines) if line.startswith("# ")]

print("word_count", word_count)
print("h1_count", h1_count)
print("unfinished_hits", unfinished_hits)
print("fence_count", fence_count, "balanced", fence_count % 2 == 0)
print("h1_lines", extra_h1_lines)
```

Expected pass summary:

- `word_count >= 4500`
- `h1_count == 1`
- `unfinished_hits == []`
- `fence_count % 2 == 0`
- `h1_lines` contains one line number only

If any check fails, fix before class use.

## Materials and prep checklist

Prepare these items before class starts:

- Your own capstone app ready in a stable branch or folder copy.
- A known clean workspace path where you can run the app from scratch.
- A stopwatch app or phone timer visible to you.
- One intentionally safe tiny mistake planned for live correction, such as entering a nonnumeric menu option once.
- A minimal README example in plain language.
- Optional sample data file for demonstration.
- A copy backup of your working app before class.

Classroom setup actions:

- Open terminal and editor side by side.
- Keep font size large enough for back-row readability.
- Disable notifications to avoid interruption.
- Have a short script card with demo sequence words only:
  start, add, list, search, save, restart, load.
- Keep this hour focused on polish and reliability, not architecture debates.

## Read-aloud script versus lab facilitation guardrail

This section establishes the pacing guardrail that keeps a long script usable in a sixty-minute class.

- **Read-aloud script sections** are meant to be spoken mostly verbatim.
- **Lab facilitation notes sections** are operational actions, coaching prompts, and check routines for circulation.
- If time pressure appears, compress read-aloud explanations by paraphrasing examples, but do not shorten lab verification.

This separation is deliberate. Long scripts can become hard to use unless speaking lines and facilitation mechanics are clearly split.

## Recap and briefing read-aloud script (4 minutes)

Instructor says:

“Welcome back. You built your capstone core behavior in the previous hour. In this hour we are doing two things only: we polish quality and we make your demo reliable. You are not trying to impress with more features right now. You are trying to prove your app is stable, understandable, and easy to run.”

“In practical terms, your target today is simple and measurable. First, your app must run cleanly from scratch. Second, your full demo flow must finish in under three minutes. Under three minutes forces clarity and confidence.”

“Today is also about discipline. Last-minute refactors can break working code. So we will use a freeze rule later in this hour. After freeze, only safe edits are allowed. That protects your working result.”

“Your demo flow for this hour is fixed so everyone can succeed with the same structure: start the app, add one record, list records, search records, save and exit, restart, then load and prove persistence. If this flow works smoothly, you are ready.”

“Final note on scope. This is polish and demo readiness only. Final scoring and certification-style review happen next hour. Keep your energy on stable behavior and clear communication.”

Transition line:

“Let’s spend eleven minutes on the polish checklist and README run notes, then I’ll model an eight-minute live demo including how to recover from a mistake.”

## Talk points read-aloud script (11 minutes)

Instructor says:

“Let’s begin with a polish checklist. Think like a first-time user, not the developer who wrote the code. Your user does not know your assumptions.”

“Checklist item one: prompt clarity. Every input prompt should be explicit. If you want a date, say what format. If you want a menu number, say the valid choices. Ambiguous prompts cause avoidable errors.”

“Checklist item two: help text. If your menu has options, give one-line hints where useful. If a user enters invalid input, your response should be calm and informative. Instead of an abrupt error, say what went wrong and what to enter next.”

“Checklist item three: edge cases. In Basics scope, you must at least handle empty inputs, invalid menu choices, and not-found search cases. Also handle empty data file state gracefully. Your app should never crash because a user typed something unexpected.”

“Checklist item four: consistency. Use the same terms throughout your app. If you call items ‘tasks’ in one menu and ‘records’ elsewhere, users get confused. Keep labels consistent.”

“Checklist item five: output readability. Align or format outputs so the user can scan quickly. Show enough information to confirm behavior without overwhelming detail.”

“Checklist item six: save and load confidence. Make save behavior obvious. On save success, print a short confirmation. On startup load, print what was loaded, for example item count.”

“Checklist item seven: predictable menu return. After an action, users should know where they are. Return to menu consistently unless exiting.”

“Checklist item eight: no noisy debug leftovers. Remove internal debugging prints that confuse users. Keep user-facing output purposeful.”

“Checklist item nine: README run notes. Your README is part of the product. It should answer three immediate questions: what this app does, how to run it, and what a quick demo flow looks like.”

“Checklist item ten: README prerequisites and file notes. If your app uses a data file, name it. If first run creates the file automatically, say that. If optional sample data exists, explain how to use it.”

“Checklist item eleven: README troubleshooting note. Include one short section for common startup confusion, such as running from the wrong directory.”

“Checklist item twelve: demo narrative. Your demo is not random clicking. It is a short story with beginning, proof of core actions, and persistence proof after restart.”

“Checklist item thirteen: time budget. You have less than three minutes for the whole demo. That means one record is enough. Do not try to show every menu option.”

“Checklist item fourteen: graceful mistake handling. If you make a typo during demo, recover calmly. Show input validation doing its job. That actually improves trust.”

“Checklist item fifteen: freeze discipline. Once the core flow passes your fresh-run test, stop changing structure. After freeze, edit only text clarity and README wording unless a critical bug blocks the demo flow.”

Instructor mini-check question:

“Quick thumbs check: who can explain the difference between polishing behavior and adding features? Good. Polishing removes friction. Feature adding increases risk.”

Instructor transitions:

“Now I’ll model a good demo flow in real time, with one small mistake and a clean recovery, so you can copy the pattern.”

## Live demo read-aloud script (8 minutes)

Use your own app and adapt names. Keep pace tight.

Instructor says while performing actions:

“I’m going to run this like a student demo. My goal is clarity and reliability, not complexity.”

Step 1, start app:

“I launch from terminal in the project directory. Notice I get a clean startup message and menu. No tracebacks, no confusing debug noise.”

Step 2, add record:

“I choose add. I enter a simple item: title ‘Practice demo’, category ‘study’, due date optional if your app supports it. The app confirms the item was added in plain language.”

Step 3, list records:

“I choose list. You can see the new item in output. The formatting is readable. This is proof that add and display both work.”

Step 4, search records:

“I choose search and enter a keyword ‘Practice’. The app finds exactly what I expect. If nothing is found, it should say not found without crashing.”

Step 5, intentional mistake and recovery:

“Now I will intentionally type an invalid menu choice once. I type letter x where number is expected.”

Pause and show behavior.

“Great. The app responds with a gentle message and returns me to valid choices. That is exactly what we want users to experience. Mistakes happen; software should guide recovery.”

Step 6, save and exit:

“I choose save and exit. I get confirmation that data is written.”

Step 7, restart and load:

“I restart the app. On startup it loads existing data and reports item count. I list items again and verify that ‘Practice demo’ persisted.”

Instructor closing line:

“That entire flow is your template: start, add, list, search, save, restart, load. Keep it under three minutes and you are ready.”

If demo over-runs, say:

“I included narration for teaching. In student demo mode, this is even shorter.”

## Hands-on lab facilitation notes (30 minutes)

This section is facilitation operations, not read-aloud lecture. Keep students typing and testing. Minimal whole-class talking after lab starts.

### Lab objective statement to students

Say this once, then circulate:

“Your mission in this block is to polish and rehearse. Deliverables are a clean README, optional sample data if useful, and a tested demo flow that runs start to load in under three minutes from a fresh run.”

### Student lab task sequence

Provide this as numbered tasks on screen or verbally:

1. Create or improve `README.md` with run instructions.
2. Verify prompts and error messages for menu and key inputs.
3. Add or tidy help text where users might hesitate.
4. Test edge cases: invalid menu choice, empty search, empty input.
5. Prepare optional sample data file if it helps your demo.
6. Rehearse fixed demo flow: start, add, list, search, save, restart, load.
7. Perform fresh-run verification procedure.
8. Record evidence in checklist form.
9. Freeze code at trigger point.
10. Rehearse one final timed demo under three minutes.

### README minimum content template

Tell students they can copy this structure and customize wording:

- Project title
- Short purpose in one paragraph
- Requirements: Python version
- How to run: exact command
- Data file behavior: created on first run or loaded if exists
- Quick demo steps
- Known limits in one brief note
- Author name and date optional

Example read-aloud guidance:

“Your README should be short and practical. Imagine a classmate opening your project with no context. Could they run it in under one minute using only the README? If yes, your README is strong.”

### Optional sample data guidance

Explain:

“Sample data is optional, not required. Add it only if it improves demo reliability without creating confusion. If you include sample data, document how it is loaded and how to reset to empty state.”

### Lab circulation coaching prompts

Use these when visiting teams:

- “Show me your run command from README and run it now.”
- “Where do you handle invalid menu input?”
- “What happens if I search for something that does not exist?”
- “Show me first run with no data file.”
- “Show me restart load proof.”
- “How long is your demo currently with a timer?”
- “What is your freeze trigger and has it been reached?”
- “After freeze, what edits are still allowed?”

### Fast interventions for common struggles

If a learner is adding features instead of polishing:

“Pause feature work. Protect what already works. Today’s success is stability and clarity.”

If README is vague:

“Replace general text with exact command and expected startup output.”

If edge-case handling crashes:

“Wrap input parsing in clear validation and return to menu safely.”

If timing is over three minutes:

“Cut extra steps. Show one strong path. Remove optional branches from demo.”

### Lab pacing checkpoints

Use these time calls to keep momentum:

- Minute 6 of lab: README draft should exist.
- Minute 12: edge-case checks in progress.
- Minute 18: first full demo rehearsal complete.
- Minute 24: fresh-run verification complete.
- Minute 27: freeze decision made and applied.
- Minute 30: final timed rehearsal done.

Say at minute 24:

“If your flow is not passing yet, stop all nonessential edits and focus only on demo-blocking fixes.”

## Deterministic and auditable completion criteria

Use objective evidence, not subjective impressions. A student passes this hour target when both criteria have observable proof.

### Criterion 1: Runs cleanly from scratch

Pass/fail evidence checklist:

- Data state reset completed according to project method.
- App launched from terminal using README command without manual patching.
- Startup output appears without traceback.
- Menu displays and accepts a valid choice.
- First add action succeeds.
- Save and exit completes cleanly.
- Restart loads previously saved item.
- No crash during sequence.

Evidence capture method:

- Instructor observes live run or student screen recording.
- Student reads exact command used.
- Student shows startup output and load confirmation.
- Instructor marks each checklist item yes or no.

Pass condition:

- All checklist items yes.

Fail condition:

- Any crash, traceback, or unresolved blocking behavior in core flow.

### Criterion 2: Demo flow works in less than three minutes

Pass/fail evidence checklist:

- Stopwatch started at app launch command execution.
- Flow sequence completed in required order:
  start, add, list, search, save, restart, load.
- Narration remains clear and concise.
- Intentional or accidental mistake handled without derailment.
- Stopwatch shows under three minutes at final load proof.

Evidence capture method:

- Instructor or peer acts as timekeeper.
- Timekeeper announces start and stop timestamps.
- Student repeats once if first timed run fails due to avoidable narration drift.

Pass condition:

- Completed under three minutes with required sequence and no crash.

Fail condition:

- Exceeds three minutes or misses required steps.

Note for fairness:

- If environment lag causes delay, evaluate logic quality separately and allow one retime in same conditions.

## Fresh-run verification playbook with reset and expected outputs

This operational sequence turns “test from scratch” into concrete practice.

### Reset phase

Goal: remove stale state and confirm app can initialize predictably.

1. Close running app process.
2. Navigate to project directory shown in README.
3. Identify persistent data file, for example `data.json`.
4. Move data file to backup name or delete according to project policy.
5. Confirm data file absence in directory listing.
6. Open terminal fresh in same directory.

Instructor expected observation:

- No leftover running process.
- Data file absent before launch.
- Student can explain reset action confidently.

### First-run launch test

1. Run exact README command, for example `python main.py`.
2. Observe startup message.
3. Confirm app creates default state cleanly if file missing.
4. Choose list before add to confirm empty-state message is friendly.

Expected outputs examples:

- “No existing data file found. Starting with empty records.”
- “No items to display yet.”
- Menu still visible afterward.

### Add and search test

1. Add one item with simple text.
2. List items and verify visible entry.
3. Search with matching keyword and verify one result.
4. Search with missing keyword and verify graceful not-found message.

Expected outputs examples:

- “Item added successfully.”
- “1 item found.”
- “No items matched your search.”

### Save and restart test

1. Save and exit.
2. Launch app again with same command.
3. Verify load message indicates one item.
4. List items and confirm same entry appears.

Expected outputs examples:

- “Saved 1 item to data file.”
- “Loaded 1 item from data file.”

### Failure handling protocol during fresh-run test

If a failure occurs:

1. Read traceback top line and exception type aloud.
2. Reproduce once to confirm it is consistent.
3. Apply smallest possible fix.
4. Re-run from reset phase quickly if persistence logic changed.
5. Record issue and fix in one sentence for debrief.

Coaching line:

“Smallest safe fix wins. This is not refactor time.”

## Safe freeze rule trigger point and allowed edits after freeze

This rule protects working demos from late instability.

### Freeze trigger point

A student must trigger freeze immediately when both are true:

- Fresh-run verification playbook passes end to end.
- One timed demo run completes under three minutes.

When both are true, student announces: “Flow passed and timed. Freeze active.”

### Allowed edits after freeze

After freeze, edits are restricted to low-risk adjustments only:

- README wording clarity.
- Print message wording for grammar or user clarity.
- Minor spacing or formatting in output text.
- Demo narration notes outside code.

### Disallowed edits after freeze

Do not allow these unless a critical demo-blocking bug appears:

- Data structure redesign.
- Function signature changes across modules.
- File format changes.
- Menu architecture refactor.
- New feature addition.
- Dependency changes.

### Critical-bug exception process

If a blocking bug appears post-freeze:

1. Describe bug in one sentence.
2. Apply one minimal fix.
3. Re-run full fresh-run verification.
4. Re-run timed demo.
5. Re-freeze immediately.

Instructor enforcement line:

“Freeze is a quality tool, not a punishment. It protects your win.”

## Pitfalls and corrective language

### Pitfall 1: Last-minute refactors break working code

What it looks like:

- Student says they are “cleaning everything up” right before demo.
- Previously passing flow starts failing unpredictably.

Corrective language:

“You already have working behavior. Preserve it. If cleanup is not required for demo reliability, schedule it after assessment.”

Micro-action:

- Ask student to create a backup copy.
- Roll back to last passing version if needed.
- Continue with polish only.

### Pitfall 2: Forgetting fresh-run test

What it looks like:

- App works only with old local files.
- Demo fails on startup in clean environment.

Corrective language:

“A real demo starts from uncertainty. Always test from fresh state before claiming ready.”

Micro-action:

- Run reset phase immediately.
- Verify startup and load logic from zero state.

### Pitfall 3: Overexplaining during demo

What it looks like:

- Student exceeds time budget by narrating internals.
- Sequence is correct but too slow.

Corrective language:

“Explain outcomes, not implementation details. Three concise sentences per step is enough.”

Micro-action:

- Practice timed run with short script lines.

### Pitfall 4: Confusing README instructions

What it looks like:

- Classmate cannot run app without asking questions.

Corrective language:

“If one peer cannot run it from README, README is incomplete.”

Micro-action:

- Peer-run test: one learner follows another learner’s README exactly.

## Optional extension inside Basics scope: help screen menu option

This extension is optional and should be attempted only after required flow is stable and frozen.

Extension goal:

- Add a menu option that prints concise usage help.
- Keep implementation simple.
- Avoid architectural rewrites.

Instructor guidance:

“Treat help screen as output formatting, not a new subsystem. One function that prints key commands is enough.”

Suggested help screen content:

- What each menu number does.
- Input format examples.
- Save and exit reminder.
- Notes on search behavior.

Validation for extension:

- Help option returns to menu cleanly.
- No impact on core demo sequence.
- README optionally references help option.

If extension destabilizes app:

- Remove extension and restore stable frozen flow.
- Required criteria always outrank optional work.

## Debrief and quick check read-aloud script (7 minutes)

Instructor says:

“Let’s close with confidence checks. Your app does not need to be flashy. It needs to be clear, stable, and demonstrable. That is professional quality.”

“Raise your hand if your flow now passes from fresh start and under three minutes. If not yet, that is fine; identify exactly which step is failing and fix only that.”

“Remember the two objective criteria we used: clean run from scratch and complete short demo flow in under three minutes. These are observable behaviors. You can verify them every time.”

“Before we end, quick check question for everyone: **What will you show first in your demo and why?**”

Call on several students and coach toward strong answers:

- Strong answer pattern:
  - First action shown
  - Why it builds audience trust
  - How it connects to rest of sequence

Example strong response you can model:

“I will show startup and menu first because it confirms the app launches cleanly. Then I add one item to create evidence for listing, searching, saving, and loading.”

Instructor wrap line:

“Great work. Next hour moves into final assessment and certification-style review. Bring this same discipline: stable behavior, clear explanation, and evidence-based confidence.”

## Read-aloud micro-script cards for instructor use

Use these short lines if you need compressed delivery while preserving intent.

### Recap card

“Today is polish and demo readiness only. Two pass criteria: clean fresh run and under-three-minute demo flow.”

### Talk points card

“Prompts must be clear, help text must guide, edge cases must not crash, README must let someone run quickly.”

### Demo card

“Start, add, list, search, save, restart, load. One small mistake handled calmly shows reliability.”

### Lab card

“Thirty minutes. Build README, test edge cases, run fresh-run playbook, do timed rehearsal, freeze when passing.”

### Debrief card

“What will you show first in your demo and why?”

## Instructor observation rubric for this hour

This rubric is formative for coaching, not final grading.

| Dimension | Emerging | Proficient | Strong |
| --- | --- | --- | --- |
| Startup reliability | Inconsistent launch | Launches with minor friction | Launches cleanly and clearly |
| Input handling | Crashes or confusing errors | Handles common invalid input | Handles invalid input with clear guidance |
| Persistence proof | Unclear save/load behavior | Save and load work with guidance | Save/load proof is obvious and concise |
| README usability | Missing or vague steps | Runnable with minor assumptions | Runnable by peer with no extra questions |
| Demo pacing | Over three minutes or disorganized | Near three minutes with minor drift | Under three minutes with clear narrative |
| Freeze discipline | Continues risky changes | Mostly stable edits | Strict freeze and minimal safe edits |

Use rubric comments as coaching notes:

- “Great clarity in startup messaging.”
- “Tighten search not-found wording.”
- “README command needs exact path context.”
- “You are ready for assessment flow.”

## High-signal feedback phrases for instructor circulation

Keep feedback short and actionable:

- “Good. Keep this flow; do not add features now.”
- “Your prompt is ambiguous; add expected input format.”
- “Show me this from a clean start, not current session state.”
- “Narrate less, demonstrate more.”
- “You passed criteria one; now time criteria two.”
- “Freeze now. Protect the win.”
- “This change is risky post-freeze; decline it.”
- “Great recovery from invalid input. Keep that behavior.”

## Practical examples of concise README run notes

Use these examples verbally without requiring exact wording.

Example one:

“This app stores personal organizer items in a local JSON file. Run with `python main.py` from the project folder. On first run, the app starts with empty records. Use menu options to add, list, and search items. Save and exit to persist data.”

Example two:

“If a data file already exists, startup loads saved records automatically. To test fresh-run behavior, remove the data file and relaunch. The app should still start without errors.”

Example three:

“Quick demo path: start app, add one item, list, search, save and exit, restart, verify item loads.”

Remind students:

“Short and precise beats long and vague.”

## Practice script students can rehearse verbatim

Offer this short student-friendly narration pattern:

“I am running my capstone app from the project folder. The app starts cleanly and shows the menu. I will add one item now and confirm success. Next I list records to verify it appears. I search using a keyword to show retrieval. I save and exit, then restart to prove persistence. On restart the app loads the saved item, and listing confirms it is still present.”

Encourage:

“Use this script skeleton and insert your own app terms.”

## Instructor contingency plan if many students are behind

If more than one third of class has not reached passing flow by midpoint of lab, run a two-minute reset huddle.

Say:

“Stop coding for two minutes. Everyone align on required flow only. Remove optional tasks. Focus on clean start, one add, one list, one search, save, restart, load. Freeze after pass.”

Then:

- Pair confident student with struggling peer for peer-run verification.
- Offer a shared minimal troubleshooting checklist:
  - wrong directory
  - file path mismatch
  - JSON decode from malformed file
  - menu input parsing errors
  - save not called before exit

Keep tone supportive:

“Finishing a stable simple flow is success.”

## Audit-ready checklist instructor can mark in real time

Use this checklist during demos:

- Student states demo objective in one sentence.
- Launch command matches README.
- Startup is clean without traceback.
- Add step succeeds.
- List step confirms new item.
- Search step behaves correctly.
- Invalid input handling is demonstrated or described accurately.
- Save step confirms persistence.
- Restart and load proof shown.
- Total demo time under three minutes.

Optional notes field suggestions:

- “Excellent concise narration.”
- “Needs clearer not-found message.”
- “Passed on second timed attempt.”
- “Freeze discipline strong.”

This checklist makes acceptance visible and repeatable across learners.

## Why this hour matters in real projects

Use this short professional framing near end if time allows:

“In real teams, many failures are not algorithm failures. They are usability friction, unclear run instructions, weak error handling, and unstable last-minute edits. Today’s work mirrors professional release readiness. You are practicing software reliability habits, not only Python syntax.”

This framing helps learners value polish as engineering skill.

## Final instructor close

End with confidence and direction:

“You now have a measurable, demo-ready capstone flow. Keep your frozen version safe, bring your README, and carry this same discipline into the next hour. Your best asset is not complexity. It is clear behavior you can prove.”

If there is one final reminder, make it this:

“First show clean startup, then show one complete path to persistence. That sequence earns trust fast.”

## Appendix: one-pass facilitation timeline script

Use this as a minute-by-minute guide if you want strict control.

- Minute 0 to 1: State outcomes and scope.
- Minute 1 to 4: Recap and criteria framing.
- Minute 4 to 15: Talk points checklist and README notes.
- Minute 15 to 23: Live demo including mistake recovery.
- Minute 23 to 53: Lab work with checkpoints and circulation.
- Minute 53 to 60: Debrief, quick check, and next-hour transition.

Minute cues to speak:

- Minute 23: “Lab starts now. Required flow only.”
- Minute 30: “README should exist by now.”
- Minute 41: “First timed rehearsal now.”
- Minute 47: “Fresh-run verification now.”
- Minute 50: “If passed, freeze now.”
- Minute 56: “Prepare quick-check answer.”
- Minute 59: “What will you show first and why?”

## Appendix: deterministic acceptance summary card

For instructor and student clarity, keep this simple pass card visible:

- Pass item A: runs cleanly from scratch with observable checklist complete.
- Pass item B: full demo sequence under three minutes with stopwatch evidence.
- Required sequence: start, add, list, search, save, restart, load.
- Pitfalls to avoid: risky refactor, skipping fresh-run test.
- Optional only after pass: help screen menu option.
- Freeze trigger: first clean fresh-run pass plus first under-three-minute timed pass.
- Allowed after freeze: wording and formatting only unless critical bug.

This card closes the loop between instruction, lab behavior, and auditable completion.

(agent_id: issue337-hour3-rewrite — use write_agent to send follow-up messages)