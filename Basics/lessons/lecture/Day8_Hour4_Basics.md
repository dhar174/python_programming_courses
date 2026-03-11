# Day 8, Hour 4: Checkpoint 4 – Control flow assessment (Course Hour 32)
**Python Programming Basics – Session 8**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 8, Course Hour 32 – Checkpoint 4: Control flow assessment  
**Duration:** 60 minutes  
**Mode:** Instructor-led introduction + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This hour primarily belongs to the learners. It serves as an integrated checkpoint for conditionals, `while` and `for` loops, data structures, and the menu CLI pattern from the previous hour. Spend the first 15 minutes setting expectations, demonstrating the spot-checking process, and running through the rubric. Then give the learners 45 minutes to build the CLI To-Do Manager autonomously.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Demonstrate mastery of control flow (Conditionals and Loops) by combining them into a menu-driven application.
2. Demonstrate mastery of Data Structures (Lists, Dictionaries) to persistently hold program state during execution.
3. Validate user inputs robustly using string methods to avoid crashes.
4. Interpret a project rubric and test your code rigorously to meet all criteria."

---

## 1) Agenda + Timing

- **0:00–0:10** Concept: Checkpoint Rubric & Requirements
- **0:10–0:15** Live demo: How to spot-check quickly
- **0:15–0:55** Guided lab: Checkpoint Lab 4
- **0:55–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist

- Have the rubric available (either on screen or distributed) for the learners.
- Open the interactive REPL to quickly demonstrate how you will intentionally try to break their code during grading.

**Say:** "For this full hour, we are focusing on your fourth Checkpoint. The goal here is to prove that you can confidently combine branches, loops, and data structures to build a cohesive, crash-resistant console runner."

---

## 3) Concept: Checkpoint Rubric & Requirements (~10 minutes)

### 3.1 Establishing the Requirements

**Say:**
"We have spent Session 7 and 8 assembling loops and decisions. Today, you will build a CLI To-Do Manager.

Here is what is required:
- You must build a Menu loop that runs until the user explicitly tells it to quit.
- You must allow the user to **Add a task**, **List Tasks**, **Mark a Task Complete**, and **Delete a Task**.
- To store the tasks in memory, you can either:
  1. Store tasks in a List of Dictionaries (e.g., `[{'name': 'Laundry', 'done': False}]`).
  2. Store tasks in a single Dictionary where the key is the task name and the value is the status (e.g., `{'Laundry': False}`).
- You must include Basic input validation. At a minimum, checking that a task name is not completely empty, and ensuring your menu inputs handle invalid characters safely.

The **Completion Criteria** requires:
- The menu loop cycles endlessly till quit.
- Tasks persist in memory across iterations (they do not mysteriously disappear).
- Both Delete and Complete commands work without causing a `KeyError` or `IndexError`."

### 3.2 Explaining the Rubric

**Say:**
"When assessing this, I am looking for four things:
1. **Correctness:** Does it do what the prompt asked?
2. **Robustness:** Does it handle missing keys safely (KeyError protection)? Does it handle an empty task name safely? Does it avoid list iteration errors?
3. **Required Constructs:** Did you successfully synthesize a `while` loop, an `if/elif` block, and a persistent List or Dictionary?
4. **Readability:** Did you format your console prints decently and name your variables clearly?"

---

## 4) Live Demo: How to Spot-Check Quickly

### 4.1 Demonstrating testing methodology

**Say:**
"Before you begin coding, I want to show you exactly how I, as a developer (and as your instructor grading this), test a brand new CLI tool. This is how you should test your own code before submitting."

**Note for Instructor:** Do this entirely verbally or with pseudocode; do not write the actual answer.

**Say:**
"Here is my test plan:
1. I will run the program. I should see the menu.
2. I will hit Enter without typing anything, or I will type 'cat'. I expect the menu to politely reject it and loop again.
3. I will choose 'List Tasks' immediately. Because the list is empty, I expect a polite message, not an error.
4. I will attempt to 'Delete' a task called 'Unicorn' that I haven't added. I expect it to say 'Unicorn not found!', not crash with a `KeyError`.
5. I will Add a task called 'Milk'.
6. I will List Tasks and expect to see 'Milk'.
7. I will Mark 'Milk' as Complete.
8. I will List Tasks and expect to see 'Milk' is updated to completed.
9. I will Delete 'Milk'.
10. I will List Tasks and expect an empty list.
11. Finally, I will choose Quit, and the loop should end.

If your code can survive that 11-step onslaught, your architecture is solid. Use this script yourself as you build."

---

## 5) Hands-on Lab: Checkpoint Lab 4

### 5.1 Lab overview

**Say:**
"You have 45 minutes to build your CLI To-Do Manager. Remember the Incremental Build Strategy from the last hour: build the menu core first and test it. Do not write the four actions all at once."

### 5.2 Lab specification

**Display or read aloud:**

---

**Checkpoint Lab 4: CLI To-Do Manager**

**Time Limit:** 45 - 60 minutes
**Rules:** Open notes, open documentation.

**Requirements Checklist:**
1. [ ] A `while True` main application loop.
2. [ ] A Menu showing at least: Add, List, Complete, Delete, Quit.
3. [ ] Memory state (List or Dictionary) instantiated OUTSIDE the loop.
4. [ ] Input validation (empty string checks, invalid menu option handling).
5. [ ] **Add:** Prompts for a task name.
6. [ ] **Complete:** Prompts for a task name. Safe lookup (avoid `KeyError`). Modifies status to 'Done' or `True`.
7. [ ] **Delete:** Prompts for a task name. Safe lookup (avoid `KeyError`). Deletes entry.
8. [ ] **List:** Iterates clearly over tasks, showing not just the name, but its completion status.

**Optional Extension:**
- Add a feature to **Filter by Status**: List only completed tasks, or list only uncompleted tasks.

---

Circulate the room aggressively during the first 10 minutes. 
Look for:
- Initializing the To-Do list *inside* the loop. (Pothole: "My data keeps vanishing!")
- Missing `.strip()` when getting input, leading to lookup failures.
- Iterating a list and deleting items simultaneously, leading to index skips. (Guide them to use dicts for simpler lookup and deletion, or deleting by exact exact name match).

### 5.3 Post-Lab Check-In

**Say:** 
"Time is up! Let's do a quick show of hands. 
Who got the basic menu loop working? (Most should raise their hands).
Who got Add and List working?
Who successfully prevented a KeyError on Delete?

If you were missing that last piece—the safe Delete—remember you always need to double-check membership: `if item in tasks: del tasks[item] else: print('Not found')`.

Your To-Do lists represent real persistent state. This is exactly how massive scale databases work internally, simply running a tighter, larger loop over a bigger dictionary."

---

## 6) Recap and Exit Ticket

### 6.1 Summary
**Say:**
"In this Session and the last, you have fully leveled up. By understanding `if/elif`, `for`, `while`, and dictionaries, you have moved past simple scripts and into writing interactive, stateful applications."

### 6.2 Quick Check / Exit Ticket
**Ask:**
"Quick check: Which strategy did you personally use to test the boundary case of deleting a task that didn't exist?"

**Expected answer:** Invite a learner to share. Expect answers like: checking `== False` or checking `in dictionary.keys()` or simply `if name in dict:`.

**Say:**
"Fantastic. Thank you for your hard work on this Checkpoint. Tomorrow, in Session 9, we dive deep into Custom Functions to make these blocks of code much cleaner."
