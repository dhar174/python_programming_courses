# Day 6 Hour 4 Advanced — Checkpoint 3: GUI Milestone Demo

## Session context

This hour is the capstone checkpoint for **Session 6** of the Advanced Python course. Learners have spent the last two sessions building a Tkinter-based GUI for their full-stack tracker capstone. Session 5 established the GUI foundations: layout, usability, forms, validation, and a record list interface. Session 6 added update/delete workflows, cleaner architecture, and JSON persistence plus polish.

The purpose of this hour is to verify that the GUI milestone is real, not theoretical. Learners should be able to launch the app, perform end-to-end CRUD through the interface, restart the program, and show that data persists. Just as important, they should be able to explain the architecture choices that make the app maintainable.

This checkpoint is not meant to be punitive. It is a structured proof of progress and an opportunity to surface issues before Session 7 introduces SQLite.

---

## Learning objectives

By the end of this checkpoint hour, learners should be able to:

1. Demonstrate a working GUI tracker app that performs CRUD through the interface.
2. Show that data persists across restarts using JSON save/load.
3. Explain how their UI is separated from their service layer or core logic.
4. Handle normal error paths without crashing in typical use.
5. Reflect on one improvement they would make next.

For instructors, the goal is to evaluate milestone readiness using consistent prompts and a concrete rubric.

---

## Prerequisites and minimum expected deliverable

Learners should arrive at this hour with a project that can do the following:

- launch a Tkinter GUI reliably
- add a record through the form
- list records in a visual control such as `Treeview` or `Listbox`
- update a selected record through the GUI
- delete a selected record with confirmation
- save/load records using JSON
- keep a stable ID per record
- maintain some separation between UI and service/core logic

If a learner is missing one piece, you can still evaluate partial progress. The checkpoint is designed to distinguish between “working milestone,” “partially working with clear structure,” and “not yet checkpoint-ready.”

---

## Section navigation

1. Purpose and tone of the checkpoint
2. Instructor run-of-show
3. Learner demo prompt
4. Concrete grading rubric
5. Observation checklist and follow-up questions
6. Common failure modes and triage guidance
7. Debrief and next-step reflection

---

## Suggested timing

- **0–8 min:** reset expectations, explain rubric, and give demo order
- **8–45 min:** learner demos, pair demos, or instructor spot-checks depending on class size
- **45–55 min:** targeted remediation, quick feedback, and self-reflection
- **55–60 min:** whole-group debrief and bridge to Session 7

If the class is large, use a mixed model:

- pair demos for peer observation
- instructor rotates through a rubric checklist
- a few full live demos for the whole class

---

## Instructor speaking script

### 1) Set the tone: this is a milestone review, not a surprise attack

**Say:** “This hour is about showing a working milestone. I am not looking for enterprise-scale software. I am looking for evidence that your GUI is usable, your architecture choices are deliberate, and your data survives restart.”

**Say:** “The most important habits to demonstrate are correctness, clarity, and recoverability. If something small goes wrong, narrate what you see and how you would debug it. That is still valuable evidence of engineering maturity.”

This framing reduces panic and encourages honest demos.

### 2) Clarify the success path

Read the demo path aloud so everyone knows exactly what counts.

**Say:** “Your standard demonstration path is: launch the app, add a record, confirm it appears in the list, update that record, delete another record, restart the app, and show that saved data loads correctly.”

**Say:** “After the demo flow, be ready to explain where the service layer lives and how your GUI identifies the correct record for update and delete.”

### 3) Explain what you are grading

Tie your evaluation to the runbook’s focus areas.

**Say:** “I’m grading four big things: does the GUI work, does persistence work, are errors handled reasonably, and is the code organized clearly enough that you can keep building on it.”

This is a good moment to distribute or display the rubric.

---

## Concrete learner demo prompt

Read or paste this prompt directly. This is the required demo sequence for Checkpoint 3.

### Checkpoint 3 Demo Prompt

You have up to **5 minutes** for the core demo and **2–3 minutes** for code explanation and questions.

#### Part A — Launch and orient

1. Launch your tracker application.
2. Briefly state the tracker domain you chose: tasks, inventory, contacts, notes, expenses, or another approved variation.
3. Point out the form area, list area, and one user feedback feature such as a status bar or dialog.

#### Part B — CRUD workflow

Perform the following actions live through the GUI:

1. Add a new record.
2. Show that the new record appears in the list.
3. Select a record and update at least one field.
4. Show that the correct record changed.
5. Delete a record using the GUI’s delete path.
6. Show that the record is removed from the visible list.

#### Part C — Persistence workflow

1. Save if your app uses an explicit save command, or explain that your app auto-saves after changes.
2. Close the application.
3. Relaunch the application.
4. Show that previously saved records load successfully.

#### Part D — Code explanation

Be ready to answer these questions:

1. Where is your service layer or core logic?
2. How does your GUI know which record to update or delete?
3. How do you avoid relying on the list index as the true record identity?
4. What happens if the JSON file is missing or invalid?
5. If you had one more hour, what would you improve first?

---

## Concrete grading rubric

Use the rubric below consistently. A 100-point scale works well and maps cleanly to partial completion.

### Rubric summary table

| Category | Points | What strong performance looks like |
| --- | ---: | --- |
| GUI launches and basic usability | 15 | App opens reliably; layout is understandable; form and list are usable. |
| CRUD through the UI | 30 | Add, list, update, and delete all work correctly through the GUI. |
| Persistence with JSON | 20 | Data saves and loads across restart; no hidden manual steps beyond what the learner explains. |
| Architecture and code organization | 20 | UI and service/core logic are separated; stable IDs are used; callbacks are reasonably thin. |
| Error handling and user feedback | 10 | Validation/no-selection/file errors are handled without crashing; user messages are clear. |
| Demo clarity and reflection | 5 | Learner can explain decisions and identify one next improvement. |

### Detailed rubric descriptors

#### 1) GUI launches and basic usability — 15 points

**13–15 points**

- app launches on first attempt
- form and list areas are visually clear
- controls are labeled in a way a user can understand
- at least one usability enhancement is present, such as status feedback, About dialog, menu, clear form, or shortcut

**8–12 points**

- app launches, but layout or labels are somewhat rough
- usability is functional but not polished
- minor awkwardness does not prevent use

**0–7 points**

- launch is unreliable
- major UI confusion prevents normal use
- instructor must intervene significantly to reach the interface

#### 2) CRUD through the UI — 30 points

**26–30 points**

- add works through the form
- records appear correctly in the list
- update changes the intended selected record
- delete removes the intended selected record
- delete includes confirmation or similarly safe behavior
- list refresh stays in sync after each operation

**16–25 points**

- most CRUD actions work, but one area is inconsistent
- refresh or selection behavior may be rough
- correctness is mostly present, but there is at least one notable weakness

**0–15 points**

- only add/list work
- update or delete target the wrong record or fail completely
- major sync issues make the app hard to trust

#### 3) Persistence with JSON — 20 points

**17–20 points**

- app loads existing JSON data on startup
- app saves after changes or provides an explicit save that clearly works
- restart confirms persistence
- saved IDs remain stable across runs

**10–16 points**

- some persistence exists, but one path is unreliable
- for example, add saves but update/delete do not
- or restart works only with extra manual steps the learner only partly explains

**0–9 points**

- no true persistence across restart
- persistence is claimed but not demonstrated
- the app crashes or loses data during the persistence workflow

#### 4) Architecture and code organization — 20 points

**17–20 points**

- clear separation between GUI layer and service/core logic
- stable IDs are used for update/delete operations
- callbacks are reasonably thin
- learner can point to where responsibilities live

**10–16 points**

- some separation exists, but boundaries blur
- callbacks may still contain some business logic
- code is understandable enough to continue with support

**0–9 points**

- GUI directly manipulates data structures in fragile ways
- update/delete rely on list position instead of stable identity
- architecture is too tangled to explain clearly

#### 5) Error handling and user feedback — 10 points

**8–10 points**

- common errors produce clear messages instead of crashes
- examples include no-selection warnings, validation feedback, or load/save errors
- the app keeps running in typical error cases

**4–7 points**

- some errors are handled, but others still crash or confuse the user
- feedback may exist but be inconsistent

**0–3 points**

- normal mistakes cause a crash
- the user receives little or no useful feedback

#### 6) Demo clarity and reflection — 5 points

**5 points**

- learner explains the architecture clearly and names one next improvement thoughtfully

**3–4 points**

- explanation is mostly clear but incomplete

**0–2 points**

- learner cannot explain how the app is organized or what they would improve next

---

## Instructor observation checklist

Use this checklist during demos for quick consistency.

### Launch and UI checklist

- [ ] App launches without instructor repair.
- [ ] Form fields are visible and understandable.
- [ ] Record list is visible and readable.
- [ ] Buttons or menu actions are discoverable.

### CRUD checklist

- [ ] Add creates a visible new record.
- [ ] Selecting a record loads or clearly targets that record.
- [ ] Update changes the intended record.
- [ ] Delete removes the intended record.
- [ ] The UI refreshes after changes.

### Persistence checklist

- [ ] Save behavior is demonstrated or clearly explained.
- [ ] App restart occurs during demo or via instructor-approved equivalent.
- [ ] Data appears after restart.

### Architecture checklist

- [ ] Learner identifies service/core layer.
- [ ] Learner explains use of stable IDs.
- [ ] UI callbacks are not the only place where business rules exist.

### Error-handling checklist

- [ ] No-selection or validation path is handled.
- [ ] App does not crash during normal mistakes.
- [ ] User feedback is understandable.

---

## Follow-up questions for instructors

Ask one or two depending on time. These questions help distinguish between copied wiring and understood architecture.

1. “If the list order changes, why do update and delete still hit the correct record?”
2. “What role does your service layer play compared with your Tkinter callbacks?”
3. “If your JSON file were corrupted, what does your app do now?”
4. “Which part of your app would change most when we switch to SQLite next session?”
5. “What repeated UI behavior did you factor into a helper method?”

Strong answers show that the learner understands responsibility boundaries, not just button wiring.

---

## Common failure modes and how to respond

### Failure mode 1: app only works if started from a very specific directory

If this is a classroom-wide issue, remind learners to use `Path` objects and relative paths anchored clearly. For scoring, note the issue but do not necessarily zero out the checkpoint if the app is otherwise functional and the learner understands the problem.

### Failure mode 2: update/delete rely on visible row index

This is a major architecture concern because it directly conflicts with the session objective. Ask a probing question:

**Ask:** “If I sort or insert a record, how do you know the right record still gets updated?”

If the learner cannot answer or the app misbehaves, score architecture and CRUD accordingly.

### Failure mode 3: persistence only works for add

This is a very common bug. Ask the learner to explain when save is triggered. If update/delete do not persist, mark down persistence but still recognize what works.

### Failure mode 4: JSON corruption causes crash

If the crash occurs during the checkpoint, stop the demo kindly and ask the learner what should happen instead. This allows partial credit for understanding even when implementation is incomplete.

### Failure mode 5: code is extremely hard to explain even though the GUI works

This often means the project grew without refactoring. Score working behavior fairly, but note weaker architecture. Encourage cleanup before Session 7 so the SQLite transition does not become painful.

---

## Remediation guidance if a learner is not checkpoint-ready

If a learner is missing the milestone, give practical next steps rather than vague criticism.

### Fast remediation priorities

1. Make sure the app launches reliably.
2. Fix stable ID handling for update/delete.
3. Centralize save behavior so add/update/delete all persist.
4. Add minimum error messaging for no-selection and load/save problems.
5. Separate one layer of UI from service logic before next session.

You can say:

**Say:** “You are closer than it may feel. The next step is not a rewrite. The next step is to stabilize identity, persistence, and one clean boundary between the UI and the service.”

---

## Suggested delivery formats based on class size

### Small class format

- each learner demos live to the room or instructor
- use the full rubric per learner
- allow 6–8 minutes per person if schedule permits

### Medium class format

- learners demo in pairs while the instructor rotates
- each learner still completes the full prompt
- peers use a simplified checklist
- instructor scores a subset live and spot-checks the rest

### Large class format

- require a standard demo path
- instructor performs timed spot-checks
- peers complete rubric-aligned feedback forms
- select a few representative full demos for shared discussion

In all cases, maintain consistent expectations. The rubric should not change depending on delivery format.

---

## Peer observation prompt

If using peer review, give learners a simple, aligned prompt:

1. Did the app launch cleanly?
2. Did you see all four CRUD actions through the GUI?
3. Did the learner prove persistence across restart?
4. Did the learner explain how the app identifies the correct record for update/delete?
5. Name one thing that felt polished.
6. Name one next improvement you would suggest.

Peer observers should comment on evidence, not just impressions.

---

## Debrief script for the last 10 minutes

Bring the room together after demos.

**Say:** “Checkpoint 3 is not the end of the capstone. It is the point where your GUI becomes trustworthy enough to carry more serious persistence next session. The best projects today did three things well: they used stable IDs, they kept the service layer in charge of business operations, and they treated persistence as part of correctness, not as an optional extra.”

Ask the room:

- “What was one design choice that made your GUI easier to demo?”
- “What was one bug pattern that showed up repeatedly today?”
- “If you had one extra improvement hour before SQLite, what would you choose?”

Capture answers visibly if possible. Good common answers include:

- clearer selection handling
- status messages
- central save helper
- better file path handling
- cleaner app class structure
- search/filter as a future enhancement

### Instructor closing language

**Say:** “Next session, we shift from JSON files to SQLite. If your architecture is clean, that transition will feel like replacing a storage mechanism, not rebuilding the whole app. That is exactly why today’s checkpoint matters.”

---

## Quick check / exit ticket

To close the hour, ask each learner to write or say one response:

1. If you had one more hour, what would you improve first in your GUI?
2. What part of your current architecture will help most when moving to SQLite?

Encourage answers that connect to design rather than only appearance.

Strong examples:

- “I would add search/filter because my stable IDs and refresh helper already make list updates manageable.”
- “My service layer will help most because the UI already delegates CRUD there, so I can change storage without rewriting button logic.”

---

## Instructor notes

- Keep the checkpoint supportive but evidence-based.
- Score what is demonstrated, not what is promised.
- When in doubt, ask the learner to narrate what their app is doing. Explanation often reveals understanding gaps faster than scrolling through code silently.
- Preserve time for a closing reflection. Learners often need help seeing that the checkpoint is preparing them for the database integration to come.
- Be especially alert for unstable-ID designs. That is the one issue most likely to create pain in later sessions if left uncorrected.


---

## Expanded run-of-show and facilitation notes

Use this section when you want more operational detail for running the checkpoint smoothly.

### Before demos begin

Have the following visible:

- the core demo path
- the rubric summary table
- the time limit
- the order of presenters or pairs

**Say:** “Your goal is not to narrate every line of code. Your goal is to provide evidence. Show the app working, then explain the key design choices.”

If learners are nervous, remind them that the rubric rewards explanation and architecture clarity in addition to raw feature success.

### Suggested presenter instructions

Tell each learner or pair:

- start with the app already closed unless time constraints require otherwise
- avoid editing code during the demo unless debugging is itself the point of the question
- narrate what you are doing in short phrases
- if something goes wrong, do not panic; explain what you expected and what you would inspect next

This guidance helps the checkpoint measure maturity, not just perfect performance under stress.

### Running pair demos efficiently

If the class is large, pair demos can still be rigorous if you structure them well.

- Learner A demos while Learner B scores with the checklist.
- Learner B demos while Learner A scores.
- Instructor circulates and performs rubric spot-checks.
- Require each learner to answer at least one architecture question individually.

This prevents one partner from carrying the whole checkpoint.

### Time-saving instructor moves

If time is tight, use the following abbreviations without losing rigor:

- ask learners to restart the app only once after a grouped set of CRUD operations
- ask one architecture question instead of three, but make it specific
- use the checklist live and fill out detailed comments afterward only where needed

---

## Sample feedback language by rubric category

Having ready-made language speeds grading and keeps feedback consistent.

### Strong performance examples

- “Your app demonstrated the full CRUD workflow cleanly, and your update/delete actions clearly targeted stable IDs rather than row position.”
- “Persistence was convincing because you showed restart behavior instead of only describing it.”
- “Your code organization is strong for this stage; the service layer boundaries are clear and your callbacks are thin.”
- “You handled normal user mistakes calmly, which made the app feel trustworthy.”

### Partial-credit feedback examples

- “Your GUI launches and basic CRUD is present, but update persistence needs work because changes did not survive restart.”
- “The interface works, but your architecture explanation suggests the GUI still owns too much business logic. That will become painful in the SQLite session if not cleaned up.”
- “Your delete flow works, but the app still depends on visible row position more than I would want for a stable milestone.”

### Growth-oriented feedback examples

- “Your next best improvement is to centralize save behavior so add, update, and delete all persist consistently.”
- “Before Session 7, invest in preserving stable IDs through load/save and separating the service logic more clearly from Tkinter callbacks.”
- “A small refactor now will save you a much larger rewrite later.”

---

## Evidence guide: what counts as proof during demo

Sometimes learners describe features they intended to finish. Keep the checkpoint grounded in evidence.

### Evidence that CRUD is really working

- you see a new record appear after Add
- you see an existing record change after Update
- you see a record disappear after Delete
- the learner can point to the selected row or explain how the app identified it

### Evidence that persistence is really working

- the learner restarts the app and the saved records reappear
- or the learner clearly demonstrates a save command followed by restart and load
- the app does not depend on re-running seed code or manually reconstructing in-memory data during the checkpoint

### Evidence that architecture is really present

- the learner can open a file or describe a module that acts as the service/core layer
- the learner can explain where the stable ID lives
- callbacks are not the only location where domain rules exist

### Evidence that error handling is really present

- no-selection path triggers a warning rather than a crash
- validation issues show a useful message
- malformed load behavior is described accurately if not demonstrated live

Keep reminding yourself: score what is shown or convincingly explained, not what is promised vaguely.

---

## Intervention rules when a demo goes off track

Instructors often need a plan for when something fails live.

### If the app fails to launch

Give the learner up to one minute to correct a simple path or typo issue if the class format allows. If the problem is deeper, shift to code explanation and partial-credit evaluation.

Suggested language:

**Say:** “Let’s pause the launch attempt there. Walk me through your architecture and tell me what you would inspect first.”

### If CRUD partly works but one action fails

Do not end the checkpoint immediately. Ask the learner to explain the intended flow and the likely bug source. This distinguishes incomplete implementation from total misunderstanding.

### If persistence fails on restart

Ask:

- “When is save triggered?”
- “What path does the app write to?”
- “Does update/delete call the same save path as add?”

These questions often surface whether the issue is a missing hook or a path mismatch.

### If the learner freezes during explanation

Offer one scaffolding question:

- “Which file or class should I open first if I want to see your core logic?”

That usually gives them a stable starting point.

---

## Optional peer and self-assessment rubric prompts

If you want learners to evaluate themselves or peers in parallel with the checkpoint, use these prompts.

### Self-assessment

Rate yourself from 1 to 4 on each statement:

1. My GUI can perform all four CRUD actions reliably.
2. My app preserves data across restart.
3. I can explain how my app identifies the correct record for update/delete.
4. My UI and service/core logic are meaningfully separated.
5. I know the first improvement I should make next.

Then ask learners to write one sentence starting with:

- “The strongest part of my milestone is…”
- “The first thing I need to improve before SQLite is…”

### Peer review

Ask peers to note:

- one piece of evidence that the app is checkpoint-ready
- one specific improvement suggestion tied to the rubric

This keeps peer feedback concrete and useful.

---

## Bridge to Session 7: how to frame the next step

End the checkpoint by helping learners see the upcoming transition as evolution, not replacement.

**Say:** “If your architecture is sound, next session is not ‘throw away the GUI and start over.’ It is ‘swap the storage strategy behind a service layer that already knows how to manage records cleanly.’” 

**Say:** “That is why I have been pushing stable IDs and thin callbacks so hard. Those choices are what make future persistence changes manageable.”

You can also give a short preview of the next questions learners will answer in Session 7:

- How does a record map to a row in a table?
- How do we preserve stable IDs in a relational store?
- How can the service layer talk to a repository instead of in-memory data or JSON?

That preview helps the checkpoint feel like a launchpad rather than just an evaluation stop.
