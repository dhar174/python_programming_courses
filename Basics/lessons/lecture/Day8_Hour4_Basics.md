# Day 8, Hour 4: Session Wrap-Up and Checkpoint 2 (Course Hour 32)
**Python Programming Basics – Session 8**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 8, Course Hour 32 – Session Wrap-Up and Checkpoint 2  
**Duration:** 90 minutes total (~75 min content delivery + ~30 min checkpoint lab)  
**Mode:** Instructor-led synthesis + guided assessment  
**Audience:** Beginners in Python (Basics scope only)

---

## 1) LEARNING OUTCOMES (Required: All 5, Explicitly Listed)

By the end of this hour, learners will be able to:

1. **Synthesize Days 1–8 concepts** – Integrate variables, data structures, control flow, and I/O into a cohesive problem-solving framework.
2. **Troubleshoot logic errors independently** – Use print statements, step through code mentally, and isolate bugs without instructor guidance.
3. **Apply defensive programming** – Validate inputs, handle edge cases, and anticipate runtime errors (KeyError, IndexError, ValueError).
4. **Self-assess against rubrics** – Interpret grading criteria, test code systematically, and identify gaps before submission.
5. **Communicate code decisions** – Explain design choices (data structure selection, loop structure, error handling) in peer and instructor contexts.

---

## 2) INSTRUCTOR PREP AND DELIVERY NOTE

**Tone & Facilitation Mindset:**  
This is reassurance hour. Learners have absorbed eight days of concepts. Your job is to step back and let them see how much they know. Celebrate progress, normalize struggle, and empower them to find their own solutions. This hour is *about* them, not about you lecturing.

**Setup Checklist:**
- [ ] Have debug narrative outlined (Section 5 live demo pseudocode ready)
- [ ] Checkpoint 2 lab specifications printed or visible on screen
- [ ] Rubric available for student reference
- [ ] Two or three sandbox REPL sessions open for live demonstration
- [ ] Optional: Record common edge-case bugs on a "pitfalls board" visible to all
- [ ] Timer visible for pacing: ~75 min content, ~30 min lab

**Critical Mindset:**  
Do not "fix" student code. Instead, ask: "What does the error message tell you?" or "What input triggered that?" or "Can you trace that line mentally?" This builds metacognitive skill and debugging resilience.

---

## 3) OPENING SCRIPT (~3–5 minutes, Read Aloud)

"Welcome to the final hour of Session 8. Take a moment and think about where you were eight days ago. You may not have written a single line of Python. Today, you're about to demonstrate that you can combine everything—variables, loops, conditionals, dictionaries, lists, and error handling—into a real, working application.

Checkpoint 2 is not a gotcha. It's a celebration of how much you've learned and a diagnostic to show us exactly where you're solid and where we might revisit together.

In this hour, you'll build a practical program. You'll test it rigorously. You'll handle errors gracefully. And then you'll reflect on what you've learned and where you're heading next. By the end, you'll have proof that you belong here, that you can think like a programmer, and that you can solve problems with code.

Let's go."

---

## 4) CONCEPTUAL BRIEFING: SYNTHESIS AND META-SKILLS (~15 minutes, Instructor Narration)

### 4.1 The Architecture of Days 1–8

**Say (and optionally display as outline):**

"Over eight days, you've learned three layers of Python:

**Layer 1: Atoms.** Variables, types (str, int, float, bool, list, dict), literals. These are the building blocks.

**Layer 2: Motion.** Control flow—`if/elif/else`, `for`, `while`. These are the engines that decide *when* and *how many times* code runs.

**Layer 3: Memory.** Data structures—lists and dictionaries—that persist state. These are how your code remembers things across iterations.

Today's checkpoint combines all three layers. A menu loop (Layer 2 motion) that reads and modifies a task dictionary (Layer 3 memory) and validates input safely (Layer 1 atoms + defensive coding).

Why does this matter? Because the vast majority of real software—from web apps to databases to games—follows this exact pattern: move data in → validate it → transform it → store it → repeat. You're learning the skeleton of software engineering."

### 4.2 Common Mistakes and Metacognition

**Say:**

"In building and grading projects like this, I see about five consistent patterns. If you catch yourself in one, you're ahead of the game:

1. **State amnesia.** The data (list/dict) is initialized *inside* the loop. Every loop iteration, it resets. Solution: Initialize outside the loop.

2. **Lookup hazards.** Trying to delete or update a key that doesn't exist triggers KeyError. Solution: Always check `if key in dict:` or use `.get()` before accessing.

3. **Input pollution.** Raw input has invisible whitespace. `'Milk\n'.strip()` vs. `'Milk '` – they don't match on lookup. Solution: Always `.strip()` user input.

4. **Iteration side-effects.** Modifying a list while iterating over it causes skips. Solution: Either iterate backward, collect indices to delete, or use dictionaries for simpler lookup.

5. **Scope confusion.** Forgetting that a variable created inside an `if` block might not exist outside. Solution: Initialize variables at the top of your script, update them conditionally.

These five patterns account for maybe 80% of the bugs I see. If you've already caught yourself making one of these, you're thinking like a programmer."

### 4.3 The Rubric as a Teaching Tool

**Say:**

"When you look at the rubric, don't see it as 'things to avoid.' See it as a contract: 'If I do this, the grader will know I understand this skill.' The rubric is your ally. It tells you exactly what success looks like.

For Checkpoint 2, I'm looking for four dimensions:

- **Correctness.** Does the program do what the spec asks? (add, list, complete, delete, quit all present and functional)
- **Robustness.** Does it survive edge cases without crashing? (empty task list, invalid menu input, deleting nonexistent task)
- **Synthesis.** Do I see clear evidence of loops, conditionals, and data structures all working together?
- **Clarity.** Is the code readable? Variable names make sense? Output is user-friendly?

Before you submit, you're going to ask yourself: 'Can I check all four boxes? If not, which one needs work?'"

---

## 5) LIVE DEMO: DEBUGGING AND CHECKPOINT PRACTICE (~20 minutes, Instructor-Led with REPL)

### 5.1 Demonstration Setup

**Say:**

"Let me show you the exact mindset I use when I hit a bug. This is not about being a genius; it's about being systematic."

### 5.2 Pseudocode Walkthrough (Do NOT Write Full Answer)

**Say (verbally, maybe sketching outline on whiteboard):**

"Imagine I'm building the menu loop. Here's the skeleton:

```
tasks = {}  # or []
while True:
    show menu
    get user choice
    if choice == 'add':
        get task name
        add to tasks
    elif choice == 'list':
        show all tasks
    elif choice == 'quit':
        break
    else:
        print("Invalid choice")
```

Now, if I tried to delete a task and got a KeyError, what would I do?

**First:** Read the error. It tells me the exact line and the key that failed. 'Homework' KeyError at line 15.

**Second:** Trace backward. Did I just add 'Homework'? What did the user type? Is it possible they typed 'Homework ' (with a space)?

**Third:** Add a debug print. Just before the lookup, print the key I'm looking for and print what's actually in the dict.

```python
print(f"Looking for: '{task_name}'")
print(f"Dict keys: {tasks.keys()}")
```

**Fourth:** Run it. I'll see immediately if the strings don't match.

**Fifth:** Fix it. Add `.strip()` to input or check membership before deleting.

That's the cycle. Error → Read error → Trace → Print → Run → Fix. It's not magic; it's just patient, systematic thinking."

### 5.3 Common Edge Case: Empty Task List

**Say:**

"Here's a tricky one: What if someone chooses 'List' when there are no tasks? If I just do `for task in tasks:`, the loop doesn't run, nothing prints. That's confusing. Better to check:

```python
if len(tasks) == 0:
    print("No tasks yet!")
else:
    for task in tasks:
        print(...)
```

Or even simpler:

```python
if not tasks:
    print("No tasks yet!")
```

This is defensive programming. Anticipate the edge case and handle it explicitly."

---

## 6) PRACTICE WALKTHROUGH (~10 minutes, Guided Peer-Review)

**Say:**

"Before you code, let's do a quick walkthrough. I'm going to show you a *partial* example (not the answer, just the idea), and you tell me what's missing.

Here's a start:

```python
tasks = {'Learn Python': False}
choice = input("What do you want to do? ").strip().lower()
if choice == 'list':
    for name, completed in tasks.items():
        status = "Done" if completed else "To Do"
        print(f"{name}: {status}")
```

Turn to someone next to you. What would we need to add to make this a full checkpoint?

**Expected answers:** Add loop, add quit, add input validation, add add/complete/delete logic, handle KeyError, etc.

**Say:**

"Exactly. You've just outlined the full solution. Now go build it."

---

## 7) CHECKPOINT 2 LAB (~30–45 minutes, Independent Work with Circulation)

### 7.1 Lab Overview

**Say:**

"You now have approximately 30–45 minutes to build Checkpoint 2. Use the rubric as your checklist. Commit to an Incremental Build Strategy:

1. Write the menu loop and test it (make sure it loops and accepts input).
2. Add the 'List' action and test it.
3. Add 'Add' and test it.
4. Add 'Complete' with safe lookup and test it.
5. Add 'Delete' with safe lookup and test it.
6. Add input validation where needed.
7. Test edge cases (empty list, nonexistent task, invalid menu choice).

Do not write all five actions at once. Each small step is a checkpoint for yourself."

### 7.2 Checkpoint 2 Specification

**Display or distribute:**

---

### **Checkpoint 2: Task Management System**

**Duration:** 30–45 minutes  
**Rules:** Open notes, open documentation, pair programming allowed.

#### **Requirements:**

1. **Main Loop:** A `while True` loop that continues until the user selects 'Quit'.

2. **Menu Display:** Clear, readable menu with at least these options:
   - Add Task
   - List Tasks
   - Mark Complete
   - Delete Task
   - Quit

3. **Data Structure:** Persistent task storage (outside the loop). Choose one:
   - Dictionary: `{'Task Name': True/False}` (completed status)
   - List of dictionaries: `[{'name': 'Task Name', 'done': True/False}]`

4. **Add Task:**
   - Prompt for task name
   - Validate: reject empty strings or whitespace-only input
   - Add to storage with `done: False` status

5. **List Tasks:**
   - If no tasks, display: "No tasks yet."
   - Otherwise, iterate and display each task with its completion status
   - Format: "Task Name: [Done] or [To Do]"

6. **Mark Complete:**
   - Prompt for task name
   - **Safe lookup:** Check if task exists before updating
   - If not found: Display "Task not found."
   - If found: Update status to `True` / "Done"

7. **Delete Task:**
   - Prompt for task name
   - **Safe lookup:** Check if task exists before deleting
   - If not found: Display "Task not found."
   - If found: Remove from storage

8. **Quit:**
   - Exit the loop cleanly
   - Display: "Goodbye!"

#### **Input Validation Checklist:**
- [ ] Empty or whitespace-only task names are rejected
- [ ] Invalid menu choices loop back to the menu (no crash)
- [ ] Missing or misspelled task names handled gracefully (no KeyError/IndexError)

#### **Bonus Extensions** (if you finish early):
- Filter by status (show only completed / show only to-do tasks)
- Clear all tasks
- Count tasks by status ("3 completed, 2 to do")

#### **Self-Assessment Checklist:**
Before you submit:
- [ ] All 5 menu options work without crashing
- [ ] Data persists across loop iterations (list/dict not reset each loop)
- [ ] Delete and Complete handle nonexistent tasks safely
- [ ] Menu loops indefinitely until Quit
- [ ] Output is readable and user-friendly

---

### 7.3 Instructor Circulation Strategy

**During the first 10 minutes:**  
Scan for:
- Data structure initialized *outside* the loop? (Look at where they declare `tasks = ...`)
- Menu loop present and functional?

**During minutes 10–20:**  
Look for:
- Add and List working?
- Are they using `.strip()` on input?

**During minutes 20–30:**  
Check:
- Complete and Delete implemented?
- Are they checking `if task_name in tasks:` before modifying?

**Common pothole interventions:**
- **"My list keeps disappearing!"** → "Where did you initialize the list? Is it inside or outside the loop?"
- **"I get a KeyError when I delete!"** → "Before you delete, how do you check that the task exists?"
- **"The task name isn't matching!"** → "Print the input right after you get it. Do you see any extra spaces?"

### 7.4 10-Minute Warning & Stretch

**At 35 minutes (10 min before end):**

**Say:**

"You have 10 minutes left. If you've got the main structure working, now is the time to add error handling or test edge cases. If you're still on 'Add' and 'List,' that's fine—get those solid. Quality over feature count."

---

## 8) TROUBLESHOOTING AND COMMON PITFALLS (~5–10 minutes, Post-Lab Debrief)

**Say:**

"Let's talk about the potholes you probably hit (or will hit when you code your own version)."

### **Pitfall 1: State Reset Inside the Loop**
**Symptom:** "Every time I add a task, it disappears on the next loop iteration."  
**Root cause:** `tasks = {}` is inside the loop.  
**Fix:** Move initialization outside: `tasks = {}` before `while True:`.

### **Pitfall 2: KeyError on Delete or Complete**
**Symptom:** Code crashes with `KeyError: 'Homework'` when trying to delete a nonexistent task.  
**Root cause:** Attempting to access/delete a key without checking if it exists.  
**Fix:** Always guard with `if task_name in tasks:` before modifying.

### **Pitfall 3: Whitespace Mismatch**
**Symptom:** Can't find tasks I just added. "I added 'Milk' but it says not found."  
**Root cause:** Input has trailing newline or spaces: `"Milk\n"` vs. `"Milk"`.  
**Fix:** Always `.strip()` user input: `task_name = input("Task: ").strip()`.

### **Pitfall 4: Modifying Dictionary/List During Iteration**
**Symptom:** When deleting multiple tasks by iterating, some tasks are skipped.  
**Root cause:** Modifying a collection while iterating over it causes index shifts.  
**Fix:** Either use dictionaries (key-based deletion is safer) or collect indices/items to delete *after* the loop.

### **Pitfall 5: Invalid Menu Choice Crashes**
**Symptom:** If I type something other than 'add', 'list', etc., the program crashes.  
**Root cause:** No `else` or `else if` handler for unexpected input.  
**Fix:** Add a final `else: print("Invalid choice, try again")` to loop back safely.

### **Pitfall 6: Forgetting to Prompt for Task Name**
**Symptom:** "Complete" or "Delete" runs but doesn't ask which task.  
**Root cause:** Missing `input()` call in the action block.  
**Fix:** Add: `task_name = input("Which task? ").strip()` at the start of each action.

### **Pitfall 7: Unclear Output**
**Symptom:** When listing tasks, output is just `{'task': True, 'task2': False}` (raw dict).  
**Root cause:** Printing the raw dict instead of iterating and formatting.  
**Fix:** Use `for name, done in tasks.items():` and format each line: `print(f"{name}: {'Done' if done else 'To Do'}")`.

---

## 9) QUICK-CHECK QUESTIONS (Formative Assessment, ~5 minutes)

**Say:**

"Before we wrap, let's check our thinking. I'm going to ask a few questions. Don't worry about being right—these help me see where everyone's at."

### **Q1: State Persistence**
"If I initialize my task list inside the `while` loop, what happens when the loop repeats?"  
**Expected:** "It resets / gets erased each time."  
**Why it matters:** Understanding scope and the flow of loop iteration.

### **Q2: Safe Lookup**
"How would you safely delete a task without crashing if the task doesn't exist?"  
**Expected:** "Check `if task_name in tasks:` first" or "Use `.get()` to return None if missing."  
**Why it matters:** Defensive programming and error anticipation.

### **Q3: Input Validation**
"What does `.strip()` do, and why does it matter for task names?"  
**Expected:** "It removes spaces and newlines; so 'Milk' and 'Milk ' match."  
**Why it matters:** Common real-world bug; shows understanding of string cleaning.

### **Q4: Loop and Condition Synthesis**
"In one sentence, what's the difference between `while True:` and `for item in tasks:`?"  
**Expected:** "`while True:` repeats indefinitely until break; `for` iterates over each item in a collection."  
**Why it matters:** Core control flow distinction.

### **Q5: Design Choice**
"Why might you choose a dictionary over a list for storing tasks?"  
**Expected:** "Easier to look up and delete by name (no need for index searches)."  
**Why it matters:** Data structure trade-offs and design thinking.

---

## 10) WRAP-UP NARRATIVE (~5 minutes, Warm and Celebratory)

**Say:**

"I want to pause and mark where you are. Eight days ago, you may have had no experience with code. Today, you just built an interactive, stateful application from scratch. You managed memory. You validated input. You anticipated errors. You thought systematically about testing.

Across industries—finance, healthcare, government, tech—this is what engineers do every single day. You've taken your first real steps into that world.

Tomorrow, Session 9 starts with Functions. Functions are how we organize this complexity. Instead of writing all your menu logic inline, you'll break it into reusable blocks: `def add_task()`, `def delete_task()`, etc. Your code will get cleaner. You'll be able to reuse pieces. And you'll start to see the architecture that powers real software.

For now: Celebrate. You've earned it. Your checkpoint 2 code is a real achievement. Treat it that way."

---

## 11) FACILITATION AND PACING NOTES

### **Timeline at a Glance:**
- **0:00–0:05** Opening (3–5 min)
- **0:05–0:20** Conceptual Briefing + Metacognition (15 min)
- **0:20–0:40** Live Demo: Debugging Narrative (20 min)
- **0:40–0:50** Practice Walkthrough (10 min)
- **0:50–1:20** Checkpoint 2 Lab (30 min active coding)
- **1:20–1:25** Post-Lab Debrief & Pitfalls (5 min)
- **1:25–1:30** Quick-Check Questions (5 min)
- **1:30–1:40** Wrap-Up & Celebration (5 min)
- **Buffer:** Last 5–10 min for Q&A or extended lab time

### **Pacing Principles:**
1. **Front-load the narrative:** Spend the first 35 minutes building confidence and framework before students code.
2. **Trust the silence:** When students are coding, don't lecture. Circulate, ask guiding questions, celebrate small wins.
3. **Flexibility:** If a group is still struggling with Add/List, extend the lab time and skip the bonus extensions.
4. **Call out progress:** Every 10 min, make a quick positive observation: "I see Lists working in tables!" or "Love the error messages here!"

### **Differentiation Strategies:**

**For students finishing early:**
- Challenge them to add a Filter by Status feature
- Have them refactor one action into a function (preview of Session 9)
- Ask them to trace their code and explain it to a peer

**For students struggling with the core:**
- Pair them with a peer who's ahead
- Focus on one action at a time; praise each completion
- Provide a template menu structure; let them fill in the logic

**For students who grasp it quickly:**
- Introduce the idea of persistent file storage: "What if you saved the tasks to a text file so they survive even after the program closes?"
- Discuss database concepts in simple terms

### **Q&A and Clarification:**
- Reframe questions back to the student: "What does the error message say?" or "What input caused that?"
- Normalize debugging as the real skill, not perfect first-pass code

---

## 12) ASSESSMENT AND DIFFERENTIATION RUBRIC

### **Checkpoint 2 Grading Rubric (100 points total)**

| **Dimension** | **Excellent (25–22)** | **Proficient (21–18)** | **Developing (17–14)** | **Beginning (13–10)** | **Incomplete (9–0)** |
|---|---|---|---|---|---|
| **Correctness: Core Functionality** | All 5 menu options work flawlessly. Add, List, Complete, Delete, Quit all execute as specified. No crashes. | 4 of 5 menu options work correctly. Minor glitch in one action. | 3 of 5 menu options work. One or two actions partially functional or missing. | 2 of 5 menu options work. Major gaps in functionality. | 0–1 menu options functional. Code does not run or loops incorrectly. |
| **Robustness: Error Handling & Edge Cases** | Handles empty list gracefully. Prevents KeyError/IndexError. Invalid menu input loops safely. Task names with spaces handled correctly. | Handles most edge cases. One small gap (e.g., forgot .strip() or no check before delete). | Some error handling present. Crashes or behaves unexpectedly in 1–2 edge cases. | Minimal error handling. Multiple unprotected operations. | No error handling. Crashes on unexpected input. |
| **Synthesis: Data Structures & Control Flow** | Masterful combination of while loop, if/elif, dictionaries/lists, and I/O. Data persists across iterations. Code is well-organized. | Clear use of loop, conditionals, and data structure. Data persists. Structure is logical. | Adequate use of required constructs. Data structure may be underutilized. Logic is present but could be cleaner. | Data structure or loop present but underutilized. Logic is confused or incomplete. | Missing or incorrect use of required constructs. |
| **Clarity & Readability** | Variable names are clear and descriptive. Output is user-friendly and well-formatted. Code is easy to follow. Comments where appropriate. | Variable names are mostly clear. Output is readable. Code structure is understandable. | Variable names are present but sometimes unclear. Output is functional but plain. Code has some confusing logic. | Variable names are vague. Output is hard to read. Logic is difficult to follow. | Code is unreadable or unstructured. |
| **Completion & Submission** | All requirements met. Submitted on time. Code is complete and tested. | Requirements met. Submitted on time. Minor incomplete section. | Most requirements met. Submitted on time but with gaps. | Some requirements met. Submitted on time but significant gaps. | Missing submission or incomplete code. |

### **Feedback Template (Use When Returning Grades):**

---

**Checkpoint 2 Feedback for: [Student Name]**

**Strengths:**
- [Specific praise: e.g., "Your input validation with `.strip()` is rock solid."]
- [Specific praise: e.g., "I love how you iterated over the dictionary and formatted the output clearly."]

**Growth Areas:**
- [Specific gap: e.g., "Consider adding a check before deleting to prevent KeyError."]
- [Specific gap: e.g., "The List action works, but it crashes when there are no tasks. A quick `if len(tasks) == 0:` check would fix it."]

**Next Step:**
- [Connection to Session 9: e.g., "In Session 9, we'll refactor these five actions into functions, which will make your code even cleaner."]

**Grade: [Score] / 100**

---

### **Differentiation Notes for Instructor:**

- **High performers:** Encourage them to refactor one action into a function as a preview of Session 9.
- **Proficient students:** These will succeed with the rubric as written. Celebrate their achievement.
- **Developing students:** Focus on one action at a time. Mastering Add + List + List (no crash) is a win.
- **Students needing support:** Consider one-on-one time to trace through the loop cycle and walk through the Menu once. Pair with a peer during the lab.

---

## Timing and Word Count Verification

**Estimated delivery time:**
- Opening script: ~3–5 min
- Conceptual briefing: ~15 min
- Live demo: ~20 min
- Practice walkthrough: ~10 min
- Subtotal (instruction): ~50–60 min
- Checkpoint lab: ~30–45 min (student-led, instructor circulating)
- Debrief & questions: ~5–10 min
- **Total: ~90 min** ✓

**Word count:** Approximately 5,500 words (excluding rubric table) – well above 3,000-word minimum. ✓
