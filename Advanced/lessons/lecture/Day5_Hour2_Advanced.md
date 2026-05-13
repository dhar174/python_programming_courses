# Day 5 Hour 2 Advanced — Tkinter Layout, Usability, and Resizing (Instructor Script)

## Instructor intent and anti-drift guardrails

This hour is a layout and usability hour. Keep the center of gravity on how interface structure affects readability, alignment, and resizing behavior under realistic user interaction. Your teaching posture should be practical and design minded, not purely syntax minded. Learners should leave with the ability to look at a cluttered Tkinter screen and apply a repeatable refactor plan that improves legibility, spacing, and window adaptability.

Anti-drift note for you to say out loud near the beginning and repeat once before the lab:

- We are not re-teaching Hour 1 widget fundamentals. Assume learners already know basic widget creation and event wiring.
- We are not drifting into Hour 3 validation UX. We are not designing error states, field-level validation strategy, or submission validation messaging in this hour.
- This hour stays focused on layout, usability, and resizing behavior.

You can frame this as a contract with the room: if a question starts to move into Hour 1 basics or Hour 3 validation details, capture it in a parking lot note and bring the class back to layout and resizing.

## Runbook alignment: outcomes, talk points, demo, lab, completion criteria

Use this section as your internal checklist and as visible class framing.

Required runbook outcomes for this hour:

- Learners can explain when to use nested frames to impose structure.
- Learners can align labels, entries, lists, and action controls in a coherent grid.
- Learners can configure row and column weights so a window expands predictably.
- Learners can identify and fix common layout defects: overlap, collapse, cramped spacing, and unbalanced resizing.
- Learners can perform a practical refactor from messy initial layout to readable responsive layout.
- Learners can self-test usability by resizing the window and scanning for readability defects.

Required talk points to explicitly cover:

- Parent-child geometry ownership and why each parent should have one geometry strategy.
- Mental model for frame decomposition: page, regions, and local grids.
- Sticky behavior and anchor intent for readability.
- Padding as a usability signal, not decorative fluff.
- Row and column weights as resize budget allocation.
- Minimum size constraints and when to use them.
- Concrete pitfalls: overlap and collapse caused by missing sticky, missing padding, and missing weights.
- Decision flow for refactor: structure first, spacing second, resize behavior third.

Required demo outcomes:

- Show a flawed baseline UI.
- Refactor incrementally with narration.
- Verify each change using quick visual tests.
- Demonstrate resizing after each milestone.
- End with a readable, aligned, and acceptably resizable interface.

Required lab outcomes:

- Students refactor a provided or copied rough layout.
- Students run a checklist-based test sequence including narrow width, tall height, and wide layout scenarios.
- Students pair-check each other using observable criteria.
- Students capture one pitfall encountered and the fix they applied.

Completion criteria for this hour must be stated literally and visibly:

- UI readable and aligned
- resizing acceptable

## Timing map and arithmetic check

Segment timing must remain exact:

- 4 min recap
- 8 min layout manager mental model
- 7 min usability/resizing concepts
- 10 min live refactor demo
- 26 min hands-on lab
- 5 min debrief

Arithmetic check for class transparency and pacing discipline:

4 + 8 + 7 + 10 + 26 + 5 = 60.

Call out that this arithmetic is intentional. It helps learners trust the flow and helps you avoid over-teaching one segment at the expense of lab time.

## Segment 1 — 4 min recap

Facilitation goal: reactivate prior memory quickly, then pivot to today’s skill transfer.

Suggested near-verbatim script:

“Welcome back. In the previous hour, you already worked with core widgets and interaction wiring. Today we shift from widget existence to interface quality. Two apps can have the same widgets and wildly different usability. This hour is about making a Tkinter interface readable, aligned, and stable when users resize the window. You will practice diagnosis and refactoring, not just typing syntax.”

“Before we start, one boundary statement: we are not reteaching basic widget fundamentals from Hour 1, and we are not moving ahead into validation UX from Hour 3. We stay tightly focused on layout, usability, and resizing behavior.”

Rapid recall prompts:

- “What problems do users report when layout is weak?”
- “What visual signs tell you a UI is hard to scan?”
- “What often breaks first when a window is resized?”

Expected learner responses you can harvest:

- Text fields not aligned, labels drifting, buttons floating oddly.
- Crowded controls with no breathing room.
- Lists stay fixed while empty whitespace appears elsewhere.
- Controls overlap or disappear when the window gets smaller.
- One region stretches too much while another region collapses.

Bridge statement to next segment:

“Excellent. That list is our target. We now build a mental model that predicts those failures before they happen.”

Observation checkpoint in this recap:

- At least three learners can describe a concrete resize failure.
- At least two learners can name one mechanism they suspect is responsible, like missing weights or poor frame decomposition.

If energy is low, use a rapid vote:

- “Hands up if you have ever resized an app and watched the layout break.”
- “Hands up if that app might have been yours.”
- Use humor, then transition immediately.

## Segment 2 — 8 min layout manager mental model

Facilitation goal: give learners a durable reasoning model so they can design and debug layout with intent.

Start with plain language model:

“A Tkinter layout is a tree. Every widget has one parent. Geometry decisions happen per parent container. The parent decides how its direct children are arranged. This is why structure comes before polish.”

Core principle you must emphasize:

- In a given parent, use one geometry manager strategy for its direct children.
- You may use different geometry managers in different nested parents, but do not mix pack and grid in the same parent.

Explain with analogy:

“Think of each frame as a room. Inside one room, choose one rule for placing furniture. If you switch rules halfway inside the same room, the room manager gets conflicting instructions.”

Talk point detail:

- Parent ownership: each frame controls placement of children.
- Local coordination: each frame can have its own grid logic.
- Nested composition: page-level frame holds region frames, then each region frame manages local detail.

Use a minimal, clean example and narrate intent:

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Layout Mental Model")
root.geometry("860x500")
root.minsize(720, 420)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

page = ttk.Frame(root, padding=12)
page.grid(row=0, column=0, sticky="nsew")

page.columnconfigure(0, weight=3)
page.columnconfigure(1, weight=2)
page.rowconfigure(1, weight=1)

header = ttk.Frame(page, padding=(0, 0, 0, 8))
header.grid(row=0, column=0, columnspan=2, sticky="ew")

content = ttk.Frame(page, padding=(0, 0, 8, 0))
content.grid(row=1, column=0, sticky="nsew")

sidebar = ttk.Frame(page)
sidebar.grid(row=1, column=1, sticky="nsew")

header.columnconfigure(0, weight=1)
ttk.Label(header, text="Inventory Workspace").grid(row=0, column=0, sticky="w")
ttk.Button(header, text="Refresh").grid(row=0, column=1, sticky="e")

content.columnconfigure(1, weight=1)
ttk.Label(content, text="Item name").grid(row=0, column=0, sticky="w", padx=(0, 8), pady=(0, 8))
ttk.Entry(content).grid(row=0, column=1, sticky="ew", pady=(0, 8))
ttk.Label(content, text="Quantity").grid(row=1, column=0, sticky="w", padx=(0, 8), pady=(0, 8))
ttk.Entry(content).grid(row=1, column=1, sticky="ew", pady=(0, 8))

sidebar.rowconfigure(1, weight=1)
ttk.Label(sidebar, text="Items").grid(row=0, column=0, sticky="w", pady=(0, 8))
items = tk.Listbox(sidebar)
items.grid(row=1, column=0, sticky="nsew")
ttk.Button(sidebar, text="Delete Selected").grid(row=2, column=0, sticky="ew", pady=(8, 0))

root.mainloop()
```

Narration points while showing this:

- “I configured root and page to stretch, then I allocated proportional space at page level.”
- “Header, content, and sidebar are separate layout concerns.”
- “Within content, labels stay left and entries stretch horizontally.”
- “Within sidebar, the list area gets vertical growth budget.”

Now teach the prohibited pattern with short warning and explanation:

“Mixing pack and grid in the same parent creates unpredictable behavior and runtime errors. If you inherit code that does this, your first fix is structural: place one set of widgets into a nested frame, then give that frame one manager.”

Concrete pitfall example 1 for overlap via missing sticky:

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x320")

panel = ttk.Frame(root, padding=10)
panel.grid(row=0, column=0)

ttk.Label(panel, text="Name").grid(row=0, column=0)
entry = ttk.Entry(panel)
entry.grid(row=0, column=1)

notes = tk.Text(panel, width=30, height=6)
notes.grid(row=1, column=0, columnspan=2)

root.mainloop()
```

Explain defect:

- Window enlarges but entry and text do not follow available space.
- Crowding appears because no sticky and no column weight.
- People call this overlap or cramped collapse because controls visually collide as window shape changes.

Concrete pitfall example 2 for collapse due to missing weights:

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("820x420")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main = ttk.Frame(root, padding=10)
main.grid(row=0, column=0, sticky="nsew")

main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=1)

left = ttk.Frame(main)
left.grid(row=0, column=0, sticky="nsew")
right = ttk.Frame(main)
right.grid(row=0, column=1, sticky="nsew")

left_list = tk.Listbox(left)
left_list.grid(row=0, column=0, sticky="nsew")
right_list = tk.Listbox(right)
right_list.grid(row=0, column=0, sticky="nsew")

root.mainloop()
```

Explain defect:

- Parent grids have some weights, but inner frames lack row and column weight.
- Lists appear but do not grow as expected, giving a collapsed feel.
- Users perceive wasted blank zones and cramped lists.

Concrete pitfall example 3 for readability collapse via missing padding:

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("640x280")

frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

for r, label in enumerate(["First", "Last", "Email", "Phone"]):
    ttk.Label(frame, text=label).grid(row=r, column=0, sticky="w")
    ttk.Entry(frame).grid(row=r, column=1, sticky="ew")

ttk.Button(frame, text="Save").grid(row=4, column=0)
ttk.Button(frame, text="Cancel").grid(row=4, column=1)

root.mainloop()
```

Explain defect:

- No internal or external padding causes visual crowding.
- Scan path is noisy because rows touch each other.
- Buttons sit too close to fields, reducing readability and increasing accidental clicks.

Transition line:

“Mental model first, then usability decisions, then resize tuning. That sequence reduces thrash.”

## Segment 3 — 7 min usability and resizing concepts

Facilitation goal: connect geometry choices to user perception and task efficiency.

Open with high-value statement:

“A good layout is not merely pretty. It reduces cognitive load. Users find controls faster, make fewer mistakes, and trust the app more.”

Concept cluster 1: readability through alignment and spacing

- Align labels consistently, usually left aligned in a label column.
- Align entry widgets so start and end edges create visual rhythm.
- Keep action buttons grouped by intent and separated from data entry area.
- Use consistent vertical rhythm with small repeated pady values.
- Use asymmetric padding intentionally when label-to-field spacing differs from section-to-section spacing.

Concept cluster 2: resizing as behavior contract

- Decide what should grow and what should remain stable.
- Text areas and lists often grow.
- Labels, compact buttons, and small status badges often remain fixed or minimally stretched.
- Horizontal and vertical growth should feel intentional, not accidental.

Explain sticky succinctly:

- sticky controls where a widget attaches within its grid cell.
- Use ew for horizontal stretch, ns for vertical stretch, and nsew for full stretch.
- Without sticky, widget may sit centered and underuse available space.

Explain weights as budget:

“Weight is your resize budget. A column with weight two gets twice the extra width of a column with weight one. A row with weight zero gets no extra stretch. If you do not assign budget, the interface has nowhere sensible to send extra space.”

Teach minimum size and practical limits:

- Use minsize to protect baseline readability.
- Avoid making minsize so large that users on smaller displays cannot use the app.
- Test three conditions live: narrow, wide, and tall.

Usability checkpoint script:

“Ask yourself: can a user scan labels top to bottom without zig-zag eye movement? Can the user see which controls belong together? When I resize, does useful content gain space while utility controls remain stable?”

Concrete before/after explanation for missing sticky:

- Before: entry remains fixed width while window grows, creating awkward blank area.
- After: entry sticky ew plus column weight gives fluid width.
- User impact: less truncation, easier editing, fewer horizontal scroll surprises.

Concrete before/after explanation for missing padding:

- Before: labels, entries, and buttons touch or nearly touch.
- After: consistent padx and pady define chunks.
- User impact: faster visual parsing and lower error rate.

Concrete before/after explanation for missing weights:

- Before: listbox does not expand; user sees clipped content.
- After: relevant row and column weights let listbox claim expansion space.
- User impact: more visible records and smoother interaction.

Transition to demo:

“Now we do a full refactor with narration. Watch sequence more than typing speed.”

## Segment 4 — 10 min live refactor demo

Facilitation goal: model expert thinking and sequencing under real constraints.

Demo framing:

- Start with intentionally rough UI.
- Apply changes in small batches.
- After each batch, run a visual test.
- Speak cause and effect explicitly.

Baseline rough UI code for demonstration:

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Order Console")
root.geometry("840x460")

main = ttk.Frame(root)
main.grid(row=0, column=0)

ttk.Label(main, text="Customer").grid(row=0, column=0)
ttk.Entry(main).grid(row=0, column=1)
ttk.Label(main, text="Order ID").grid(row=0, column=2)
ttk.Entry(main).grid(row=0, column=3)

ttk.Label(main, text="Notes").grid(row=1, column=0)
notes = tk.Text(main, width=30, height=6)
notes.grid(row=1, column=1)

listbox = tk.Listbox(main, height=8)
listbox.grid(row=1, column=2)

ttk.Button(main, text="Add").grid(row=2, column=0)
ttk.Button(main, text="Delete").grid(row=2, column=1)
ttk.Button(main, text="Refresh").grid(row=2, column=2)

root.mainloop()
```

Narrate observed defects:

- Regions are not conceptually grouped.
- Labels and entries on row zero are cramped.
- Notes and listbox do not share space clearly.
- Buttons are disconnected from the list region.
- Resizing is poor due to no meaningful sticky and no weights.

Refactor step 1 structure with nested frames:

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Order Console")
root.geometry("840x460")
root.minsize(720, 400)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

page = ttk.Frame(root, padding=12)
page.grid(row=0, column=0, sticky="nsew")

page.columnconfigure(0, weight=3)
page.columnconfigure(1, weight=2)
page.rowconfigure(1, weight=1)

form = ttk.Frame(page, padding=(0, 0, 10, 0))
form.grid(row=1, column=0, sticky="nsew")

list_panel = ttk.Frame(page)
list_panel.grid(row=1, column=1, sticky="nsew")

ttk.Label(page, text="Order Workspace").grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))
```

What to say:

“I created page, then two primary regions: form and list panel. This gives us local control and cleaner mental boundaries.”

Refactor step 2 alignment and spacing in form:

```python
form.columnconfigure(1, weight=1)
form.rowconfigure(2, weight=1)

ttk.Label(form, text="Customer").grid(row=0, column=0, sticky="w", padx=(0, 8), pady=(0, 8))
customer_entry = ttk.Entry(form)
customer_entry.grid(row=0, column=1, sticky="ew", pady=(0, 8))

ttk.Label(form, text="Order ID").grid(row=1, column=0, sticky="w", padx=(0, 8), pady=(0, 8))
order_entry = ttk.Entry(form)
order_entry.grid(row=1, column=1, sticky="ew", pady=(0, 8))

ttk.Label(form, text="Notes").grid(row=2, column=0, sticky="nw", padx=(0, 8), pady=(0, 8))
notes = tk.Text(form, wrap="word")
notes.grid(row=2, column=1, sticky="nsew", pady=(0, 8))
```

What to say:

“Now labels align left, entries stretch, notes gets vertical growth. Padding creates rhythm. Notice how this immediately improves readability without changing business logic.”

Refactor step 3 list region behavior and optional extension hook:

```python
list_panel.columnconfigure(0, weight=1)
list_panel.rowconfigure(1, weight=1)

ttk.Label(list_panel, text="Recent Orders").grid(row=0, column=0, sticky="w", pady=(0, 8))

orders = tk.Listbox(list_panel)
orders.grid(row=1, column=0, sticky="nsew")

toolbar = ttk.Frame(list_panel, padding=(0, 8, 0, 0))
toolbar.grid(row=2, column=0, sticky="ew")
toolbar.columnconfigure((0, 1, 2), weight=1)

ttk.Button(toolbar, text="Add").grid(row=0, column=0, sticky="ew", padx=(0, 4))
ttk.Button(toolbar, text="Delete").grid(row=0, column=1, sticky="ew", padx=4)
ttk.Button(toolbar, text="Refresh").grid(row=0, column=2, sticky="ew", padx=(4, 0))
```

What to say:

“Here is the optional extension already scaffolded as a toolbar frame with Add, Delete, Refresh. This is useful for learners who finish early. Also notice the toolbar is in its own frame so button spacing and growth are locally controlled.”

Refactor step 4 resize verification script:

- Drag window wider: check entries and list expand.
- Drag window taller: notes and list gain height.
- Drag narrower to minsize: confirm baseline readability retained.
- Confirm no overlap or clipping.

Say:

“Every layout change should be followed by a resize test. If you only test at default size, you are not done.”

Quick diagnostic prompts while demo runs:

- “Which row is responsible for vertical growth in form?”
- “Which column is responsible for horizontal growth in form?”
- “Where did we assign list panel growth budget?”
- “What would break if we removed sticky nsew from notes?”

Expected answers:

- form row 2.
- form column 1.
- list_panel row 1 and column 0.
- notes would stop filling space and appear collapsed relative to cell.

Remediation mini-playbook during demo:

- If entry not stretching, check columnconfigure weight and entry sticky ew.
- If text area not stretching vertically, check rowconfigure weight and text sticky nsew.
- If elements look cramped, add consistent padding at region and widget levels.
- If mixed geometry warning appears, identify parent and unify manager strategy.

Close demo with explicit criteria mapping:

“We now have readable alignment and acceptable resizing behavior. This is the same target you will apply in lab.”

## Segment 5 — 26 min hands-on lab

Facilitation goal: convert observed refactor pattern into independent execution and diagnosis skill.

Lab framing script:

“You now own the process. You are not copying style line by line. You are applying a layout strategy. Your deliverable is a refactored UI that meets objective criteria under resize tests.”

Lab objective:

Refactor a rough Tkinter screen so structure, spacing, alignment, and resizing behavior are intentional and testable.

Lab setup instructions:

1. Start from the provided starter file or copy the rough baseline layout from the demo.
2. Run once and observe default problems.
3. Sketch region decomposition on paper or in comments in plain text.
4. Implement structural frames first.
5. Apply alignment and spacing.
6. Configure resize behavior with weights and sticky.
7. Run resize test checklist.
8. Perform peer observation and adjust.

Suggested starter code for lab use:

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Project Tracker")
root.geometry("900x520")

main = ttk.Frame(root)
main.grid(row=0, column=0)

ttk.Label(main, text="Project").grid(row=0, column=0)
ttk.Entry(main).grid(row=0, column=1)
ttk.Label(main, text="Owner").grid(row=0, column=2)
ttk.Entry(main).grid(row=0, column=3)
ttk.Label(main, text="Status").grid(row=1, column=0)
ttk.Combobox(main, values=["Open", "In Progress", "Blocked", "Done"]).grid(row=1, column=1)

ttk.Label(main, text="Details").grid(row=2, column=0)
details = tk.Text(main, width=34, height=8)
details.grid(row=2, column=1)

tasks = tk.Listbox(main, height=10)
tasks.grid(row=2, column=2)

ttk.Button(main, text="Add Task").grid(row=3, column=0)
ttk.Button(main, text="Delete Task").grid(row=3, column=1)
ttk.Button(main, text="Refresh").grid(row=3, column=2)

root.mainloop()
```

Lab constraints you should post clearly:

- Keep this hour focused on layout and resizing.
- Do not add validation workflows.
- Do not rework widget event logic beyond what is needed for layout.
- Use nested frames intentionally.
- Use consistent padding and sticky strategy.
- Configure row and column weights where growth is expected.

Mandatory student tests during lab:

- Narrow width test: reduce width until near minsize and inspect clipping.
- Wide width test: expand width significantly and inspect wasted space distribution.
- Tall height test: expand height and verify text/list growth priorities.
- Quick scan test: verify labels and entries are easy to read in one top-to-bottom pass.

Observation checkpoints at minute 8 of lab:

- Each student has identified at least two region frames.
- At least one row and one column weight is configured in a meaningful parent.
- Students can articulate which widgets should stretch and which should remain compact.

Observation checkpoints at minute 16 of lab:

- Most students have spacing rhythm applied through padx and pady.
- At least one concrete resize defect has been found and fixed.
- Students can point to exact line causing the fix.

Observation checkpoints at minute 22 of lab:

- Peer review pairs run each other’s window through three resize scenarios.
- Peer gives one commendation and one targeted adjustment.
- Student writes a short rationale for final layout choices.

Instructor roaming script and questions:

- “Show me your parent frame tree. Where does each responsibility live?”
- “Which parent owns this widget’s geometry?”
- “If this entry should expand, where is the weight configured?”
- “If this row should absorb height, which row has weight and which widget uses sticky nsew?”
- “Is this spacing intentional or accidental?”
- “What happens if I shrink width by 35 percent right now?”

Common lab pitfalls and remediation playbook:

Pitfall A: overlap feel from missing sticky
Symptom: entries remain tiny while cells enlarge, controls appear mispositioned.
Fix path:
- Confirm target widget sticky includes ew or nsew.
- Confirm parent column weight exists.
- Re-run wide test and verify change.

Pitfall B: collapse feel from missing row weight
Symptom: text area or listbox does not gain height when window grows vertically.
Fix path:
- Add rowconfigure for the row containing expanding widget.
- Confirm widget sticky nsew.
- Re-run tall test and compare.

Pitfall C: crowded interface from missing padding
Symptom: labels, fields, and actions visually blend and scan poorly.
Fix path:
- Add region-level padding first.
- Add widget-level padx and pady rhythm second.
- Maintain consistency instead of random values.

Pitfall D: mixed manager confusion
Symptom: runtime warning or unpredictable arrangement in one container.
Fix path:
- Identify offending parent.
- Keep one geometry manager for direct children.
- If needed, insert a nested frame and isolate strategy.

Pitfall E: uneven growth budget
Symptom: one side stretches aggressively while primary content remains constrained.
Fix path:
- Reassess column weights at page region level.
- Decide intended ratio based on use case.
- Validate with wide test.

Pitfall F: minsize too restrictive or too permissive
Symptom: either app cannot fit smaller display or app becomes unreadable when tiny.
Fix path:
- Set practical minsize after layout is stable.
- Test with target classroom and laptop resolutions.
- Keep readability threshold as guiding standard.

Quick intervention snippets you can suggest without taking keyboard control:

- “Try setting the form entry column to weight one and entry sticky ew.”
- “Give the text widget row vertical budget and sticky nsew.”
- “Move action buttons into a toolbar frame to simplify spacing.”
- “Add top padding below section titles for hierarchy clarity.”

Optional extension for fast finishers:

- Add a toolbar frame with Add/Delete/Refresh controls.
- Keep toolbar local to list or task panel.
- Make buttons stretch evenly.
- Demonstrate that toolbar remains stable while list grows.

Example extension guidance in near-verbatim voice:

“If you are done early, implement the optional extension: create a toolbar frame containing Add, Delete, Refresh. Place it under your list panel. Give toolbar columns equal weight so buttons align and stretch evenly. This extension reinforces local layout ownership and avoids clutter in the main frame.”

Lab quality rubric you can announce:

- Structure clarity: frame decomposition is obvious.
- Alignment quality: labels and fields align predictably.
- Spacing quality: breathing room is consistent.
- Resize behavior: growth allocation matches task priority.
- Defect handling: student can explain at least one pitfall and fix.

Peer review script for students:

- “I can read this quickly without searching for labels.”
- “When I resize wider, the most useful region gains space.”
- “When I resize taller, long-text or list regions gain space.”
- “I did not observe overlap, clipping, or collapse under normal ranges.”

Time management cues for you:

- Minute 0 to 4 of lab: planning and first frame decomposition.
- Minute 5 to 12: alignment and spacing pass.
- Minute 13 to 18: resize behavior and defect fixes.
- Minute 19 to 23: peer review and final tune.
- Minute 24 to 26: prepare debrief response.

Keep lab psychologically safe:

- Praise diagnosis language, not just final appearance.
- Normalize iterative correction.
- Encourage small test loops after each change.
- Discourage giant edits followed by one late run.

Instructor notes on helping struggling learners:

If a learner is blocked, do not rewrite their full layout for them. Ask sequence questions:

1. “What should this region do when width increases?”
2. “Which parent controls that region?”
3. “Where can we assign horizontal budget?”
4. “Which widget should attach to that budget using sticky?”

Then let learner apply one change and run.

If a learner overcomplicates:

- Recommend reducing to three regions.
- Remove ornamental widgets.
- Stabilize core layout first, then reintroduce extras.

If a learner attempts validation logic work:

- Appreciate initiative.
- Park it for Hour 3.
- Bring them back to resize and readability checklist.

Documenting learning during lab:

Ask each learner to write short notes:

- One defect observed.
- One line-level fix applied.
- One test scenario that confirmed improvement.
- One remaining edge case they want to revisit later.

This reflection improves transfer beyond this hour.

## Quick-check section

Why shouldn’t you mix pack and grid in the same parent?

Use this exact sentence as displayed above, then ask for verbal responses from at least two learners. Expected answer pattern: one parent should have one geometry strategy for direct children, otherwise conflicting geometry instructions cause unstable or error-prone behavior.

## Segment 6 — 5 min debrief

Facilitation goal: consolidate mental model, validate outcomes, and set up next hour without drifting into it.

Debrief script:

“Let’s close by naming what changed in your thinking. We moved from placing widgets to designing behavior. Layout is not a final polish pass. It is a structural decision that directly affects usability.”

“Tell me one defect you fixed and the mechanism behind the fix.”

Harvest examples and map to core concepts:

- Missing sticky corrected by ew or nsew.
- Missing weight corrected by rowconfigure or columnconfigure.
- Missing spacing corrected by consistent padx and pady.
- Confused structure corrected by introducing nested frames.

State completion criteria visibly and literally:

- UI readable and aligned
- resizing acceptable

Ask for confirmation:

“Raise your hand if your current version meets both criteria under at least three resize scenarios.”

If hands are mixed, normalize and give immediate recovery plan:

“Not finishing perfection in one pass is normal. Before next hour, run one more three-case resize test, then fix one highest-impact issue first.”

Close with boundary reminder to prevent drift:

“In the next hour we can talk about validation UX concerns. For this hour, success means your structure, alignment, spacing, and resize behavior are solid. Keep your focus on layout quality.”

## Practical instructor appendix: expanded facilitation notes

Use this appendix during delivery if you need richer prompts without improvising from scratch.

High-impact phrasing library:

- “Structure first, detail second, behavior third.”
- “Every parent is a local layout jurisdiction.”
- “Resize behavior is part of correctness, not optional polish.”
- “Padding is information architecture, not decoration.”
- “If a user cannot scan quickly, layout is not done.”
- “Weights allocate extra space, sticky claims that space.”

Advanced diagnostic sequence you can model on projector:

1. Identify the widget showing a defect.
2. Find its parent.
3. Inspect parent grid weight configuration.
4. Inspect widget sticky value.
5. Inspect spacing and neighboring constraints.
6. Run one resize test.
7. Confirm behavioral change.
8. Repeat for next defect.

Use this micro-sequence when students ask “why is this not stretching.”

Comparative checklist for learners who finish very early:

- Did you separate primary content from action controls?
- Are labels consistently aligned left?
- Do text and list regions gain space first on resize?
- Are compact controls prevented from over-stretching?
- Is there clear spacing between input region and action region?
- Is minsize appropriate for readability?
- Does toolbar extension behave consistently?

Edge-case prompts for stronger learners:

- “What happens at very narrow widths?”
- “Does section hierarchy remain obvious at large widths?”
- “Which controls become hard to reach in tall windows?”
- “Could you simplify one nested frame without losing clarity?”
- “Is your ratio of content to sidebar space justified by task frequency?”

Remediation mini-script if the room is behind schedule at lab minute 15:

“We will prioritize minimum viable layout quality. Focus only on three goals: frame structure, one consistent alignment rhythm, and one robust resize path for your largest content region. Ignore cosmetic tweaks. Hit criteria first, then style.”

Remediation mini-script if the room is ahead of schedule:

“Great pace. Add the toolbar extension and run peer stress testing. Try intentional break tests by removing one weight or one sticky, predict failure, then restore. This deepens your diagnostic confidence.”

Classroom management notes for near-verbatim coaching:

- Keep explanations short during roaming, then ask students to narrate back.
- Avoid keyboard takeover except for class-wide demo moments.
- Praise precise language like row weight, parent frame, and sticky intent.
- Redirect generic statements into concrete observations.

Examples:
- Student says “It looks weird.”
  Coach response: “Point to one widget and one behavior. Is it alignment, spacing, or resize allocation?”

- Student says “It does not work.”
  Coach response: “Run one test scenario and tell me expected versus observed behavior.”

This keeps learners in a diagnostic mindset.

## Reference implementation for post-lab comparison

Use this only after most students have attempted their own solution. Present as one possible design, not the only design.

```python
import tkinter as tk
from tkinter import ttk

def build_app() -> tk.Tk:
    root = tk.Tk()
    root.title("Project Tracker Refactor")
    root.geometry("960x560")
    root.minsize(760, 440)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    page = ttk.Frame(root, padding=12)
    page.grid(row=0, column=0, sticky="nsew")

    page.columnconfigure(0, weight=3)
    page.columnconfigure(1, weight=2)
    page.rowconfigure(1, weight=1)

    title_row = ttk.Frame(page, padding=(0, 0, 0, 10))
    title_row.grid(row=0, column=0, columnspan=2, sticky="ew")
    title_row.columnconfigure(0, weight=1)

    ttk.Label(title_row, text="Project Tracker Workspace").grid(row=0, column=0, sticky="w")
    ttk.Label(title_row, text="Layout and resizing focus").grid(row=0, column=1, sticky="e")

    form = ttk.Frame(page, padding=(0, 0, 10, 0))
    form.grid(row=1, column=0, sticky="nsew")
    form.columnconfigure(1, weight=1)
    form.rowconfigure(3, weight=1)

    ttk.Label(form, text="Project").grid(row=0, column=0, sticky="w", padx=(0, 8), pady=(0, 8))
    project_entry = ttk.Entry(form)
    project_entry.grid(row=0, column=1, sticky="ew", pady=(0, 8))

    ttk.Label(form, text="Owner").grid(row=1, column=0, sticky="w", padx=(0, 8), pady=(0, 8))
    owner_entry = ttk.Entry(form)
    owner_entry.grid(row=1, column=1, sticky="ew", pady=(0, 8))

    ttk.Label(form, text="Status").grid(row=2, column=0, sticky="w", padx=(0, 8), pady=(0, 8))
    status_combo = ttk.Combobox(form, values=["Open", "In Progress", "Blocked", "Done"], state="readonly")
    status_combo.current(0)
    status_combo.grid(row=2, column=1, sticky="ew", pady=(0, 8))

    ttk.Label(form, text="Details").grid(row=3, column=0, sticky="nw", padx=(0, 8), pady=(0, 8))
    details = tk.Text(form, wrap="word")
    details.grid(row=3, column=1, sticky="nsew", pady=(0, 8))

    right = ttk.Frame(page)
    right.grid(row=1, column=1, sticky="nsew")
    right.columnconfigure(0, weight=1)
    right.rowconfigure(1, weight=1)

    ttk.Label(right, text="Tasks").grid(row=0, column=0, sticky="w", pady=(0, 8))
    tasks = tk.Listbox(right)
    tasks.grid(row=1, column=0, sticky="nsew")

    toolbar = ttk.Frame(right, padding=(0, 8, 0, 0))
    toolbar.grid(row=2, column=0, sticky="ew")
    toolbar.columnconfigure(0, weight=1)
    toolbar.columnconfigure(1, weight=1)
    toolbar.columnconfigure(2, weight=1)

    ttk.Button(toolbar, text="Add").grid(row=0, column=0, sticky="ew", padx=(0, 4))
    ttk.Button(toolbar, text="Delete").grid(row=0, column=1, sticky="ew", padx=4)
    ttk.Button(toolbar, text="Refresh").grid(row=0, column=2, sticky="ew", padx=(4, 0))

    status_bar = ttk.Frame(page, padding=(0, 10, 0, 0))
    status_bar.grid(row=2, column=0, columnspan=2, sticky="ew")
    status_bar.columnconfigure(0, weight=1)
    ttk.Label(status_bar, text="Resize test: narrow, wide, tall").grid(row=0, column=0, sticky="w")
    ttk.Label(status_bar, text="Target: readable and aligned").grid(row=0, column=1, sticky="e")

    return root

if __name__ == "__main__":
    app = build_app()
    app.mainloop()
```

Debrief this implementation with restraint:

- Mention that many layouts can satisfy criteria.
- Highlight how structure and behavior mapping are explicit.
- Reinforce that this is a reference, not a single correct answer.

## Instructor self-check before ending hour

Use this quick internal review in the final minute:

- Did I preserve the exact timing plan?
- Did I explicitly show arithmetic 4 + 8 + 7 + 10 + 26 + 5 = 60.
- Did I enforce anti-drift boundaries?
- Did I include concrete pitfall examples for missing sticky, missing padding, and missing weights?
- Did learners practice resize testing, not just static visual inspection?
- Did I state completion criteria literally as required?
- Did I include the optional toolbar extension pathway?

If all are true, this hour is complete and aligned.

## Final spoken close

“Strong work. You now have a repeatable method for Tkinter layout quality: frame structure, alignment rhythm, and resize behavior contracts. Keep this process close. It will save you time every time a UI grows. Next session can build on this foundation, but for now your win condition is clear and met when your interface is readable, aligned, and stable under resize tests.”

(agent_id: issue296-hour2-finaldraft — use write_agent to send follow-up messages)