# Day 4, Hour 4: Checkpoint 4 – Control Flow Assessment
**Python Programming Basics – Day 4 / Session 8 / Course Hour 32**

---

## Subtitle
**Assessment-centered instructor script for demonstrating conditionals, loops, and data structures through a CLI To-Do Manager**

**Instructor framing:** This is the standalone script for **Day 4, Hour 4**, aligned to **Course Hour 32** in the runbook. This hour is intentionally **assessment-centric** while still following the same instructional structure used in the Day 3 lecture scripts. The checkpoint asks learners to show that they can combine control flow and data structures into one coherent program.

---

## Timing Overview
**Total Time:** 60 minutes  
- Recap & transition into checkpoint mode: 5 minutes  
- Assessment framing and rubric explanation: 10 minutes  
- Clarifying required features and constraints: 8 minutes  
- Live Demo – how the instructor will spot-check submissions: 7 minutes  
- Hands-On Checkpoint Lab 4 – CLI To-Do Manager: 20 minutes  
- Debrief, reflection, and exit ticket: 10 minutes  

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Demonstrate conditionals, loops, and data structures in one coherent CLI program
2. Build a menu loop that remains active until quit
3. Add, list, mark complete, and delete to-do tasks in memory
4. Apply basic input validation, especially for non-empty task names
5. Avoid common state and index bugs in menu-driven programs
6. Explain how correctness, readability, required constructs, and robustness affect assessment quality
7. Reflect on how they tested their own work under checkpoint conditions

---

## Section 1: Recap & Transition into Assessment Mode (5 minutes)

### Framing the Hour

**[Instructor speaks:]**

We are now in **Day 4, Hour 4**, which aligns to **Course Hour 32** in the full Basics runbook. This is **Checkpoint 4**, our control-flow assessment point.

The previous three hours built the foundation for this moment:

- **Hour 29:** menu loops
- **Hour 30:** input validation using simple guards
- **Hour 31:** mini-project integration with a contact manager

Now students will demonstrate that they can use those ideas independently in a related but not identical program.

### Checkpoint Mindset

**[Instructor speaks:]**

When students hear the word “assessment,” some immediately become tense. It helps to set the tone carefully.

Say something like this clearly and sincerely:

> “This checkpoint is not here to trick you. It is here to help you prove what you can do with loops, conditions, and data structures.”

That matters. Good assessment language reduces panic and supports better performance.

### Transition Statement

**[Instructor speaks:]**

Today’s checkpoint program is a **CLI To-Do Manager**. It is similar in shape to the contact manager, but the student still has to make real choices about data storage, menu flow, and basic validation.

---

## Section 2: Explain the Rubric – Correctness, Readability, Required Constructs, Robustness (10 minutes)

### Why Share the Rubric Up Front?

**[Instructor speaks:]**

Students perform better when they know what “good” looks like. So before they start, explain the assessment criteria in plain language.

### Rubric Category 1: Correctness

**[Instructor speaks:]**

Correctness means the program actually does what it is supposed to do.

For this checkpoint, that includes:

- the menu loop works
- tasks can be added
- tasks can be listed
- tasks can be marked complete
- tasks can be deleted
- tasks stay in memory during the run

A program may look impressive, but if “mark complete” does nothing, it is not correct.

### Rubric Category 2: Readability

**[Instructor speaks:]**

Readability means another person can follow the code without confusion.

That includes basics like:

- clear variable names
- consistent indentation
- logical branch structure
- understandable output messages

A program can technically work and still be hard to read. We want students to value both.

### Rubric Category 3: Required Constructs

**[Instructor speaks:]**

This checkpoint is specifically about **control flow** and **data structures**. So students need to actually use those constructs.

Expected evidence includes:

- a loop that repeats until quit
- `if/elif/else` or equivalent conditional routing
- a data structure for storing tasks (`list` of `dict`s or a `dict` of statuses)
- basic input handling for required actions

If someone submits a very different program that avoids the intended constructs, it misses the learning target.

### Rubric Category 4: Robustness

**[Instructor speaks:]**

Robustness means the program handles ordinary mistakes reasonably well.

At this Basics level, we are not asking for industrial-strength validation. We are asking for sensible protections such as:

- non-empty task names
- polite response to invalid menu choices
- no crash when trying to complete or delete something that does not exist
- care around indices when deleting

This is the difference between “works in one perfect demo” and “works reliably enough for a beginner CLI tool.”

### Student-Friendly Summary

**[Instructor speaks:]**

A strong checkpoint program is:

- correct
- readable
- built with the required concepts
- reasonably robust

That four-part summary is worth repeating before work time starts.

---

## Section 3: Clarify the Checkpoint Lab Requirements (8 minutes)

### Checkpoint Lab 4 Prompt

**[Instructor speaks:]**

Students will build a **CLI To-Do Manager**.

Required features:

- menu loop until quit
- add task
- list tasks
- mark complete
- delete task
- store tasks in a **list of dictionaries** or a **dictionary of status**
- include basic input validation for **non-empty task name**

### Acceptable Data Structures

#### Option A: List of Dictionaries

```python
tasks = [
    {"name": "Buy milk", "done": False},
    {"name": "Call mom", "done": True},
]
```

This structure is usually the easiest for readable listing.

#### Option B: Dictionary of Status

```python
tasks = {
    "Buy milk": False,
    "Call mom": True,
}
```

This is also acceptable if students use it correctly.

### Recommended Default for Most Learners

**[Instructor speaks:]**

For most students, I recommend a **list of dictionaries** because it naturally supports listing with numbers and keeps each task record explicit.

### Required Behaviors in Plain Language

1. **Add task**
   - ask for a task name
   - reject empty task names
   - store the task in memory

2. **List tasks**
   - show all tasks
   - indicate whether each task is complete or not

3. **Mark complete**
   - let the user mark a task as done
   - this may be by name or by number, depending on the student’s design

4. **Delete task**
   - remove a task safely
   - avoid index errors

5. **Quit**
   - stop the menu loop cleanly

### Suggested Simplification for Stronger Success Rates

**[Instructor speaks:]**

If you want to keep the checkpoint accessible, encourage students to use **task numbers** for complete/delete after listing tasks. That reduces ambiguity when there are duplicate names.

However, if they choose name-based complete/delete and it works reliably, that is also fine.

---

## Section 4: Live Demo – How the Instructor Will Spot-Check Quickly (7 minutes)

### Why Model Spot-Checking?

**[Instructor speaks:]**

The runbook calls for a simple demo of how the checkpoint will be tested:

- run the program
- try invalid input
- try missing data

This is helpful because students learn what good self-testing looks like.

### Demo Script to Narrate

**[Instructor speaks:]**

I am not going to build the whole solution here. I am going to show how I would quickly evaluate whether a student program is ready.

### Spot-Check Sequence

1. **Run the program**
   - Does the menu appear immediately?

2. **Add a task**
   - Example: `Buy milk`
   - Do I get a confirmation?

3. **List tasks**
   - Does the task appear?
   - Is completion status visible?

4. **Try invalid input**
   - Example: choose menu option `9`
   - Does the program recover politely?

5. **Try missing data**
   - Example: delete or complete a task number that does not exist
   - Does the program avoid crashing?

6. **Quit**
   - Does the loop end cleanly?

### Short Instructor Demo Snippet

```python
print("\nQuick self-test checklist:")
print("1. Add task")
print("2. List tasks")
print("3. Try invalid menu choice")
print("4. Try missing task")
print("5. Quit")
```

### Key Message to Students

**[Instructor speaks:]**

Before you call your program “done,” run the same kind of spot-check on your own work. If you only test the happy path once, you are not finished.

### Prediction Prompt

**[Instructor asks:]**

If deleting uses list positions, what bug might happen if we do not check whether the chosen number is valid?

[Expected answer: an `IndexError` or deletion of the wrong item.]

---

## Section 5: Hands-On Checkpoint Lab 4 – Build the CLI To-Do Manager (20 minutes setup + work time)

### Assessment Prompt

**Checkpoint Lab 4: Build a CLI To-Do Manager**

Create a command-line to-do manager that allows the user to manage tasks during one program run.

### Required Features

Your program must:

- use a menu loop until the user quits
- add a task
- list tasks
- mark a task complete
- delete a task
- store tasks in a **list of dictionaries** or **dictionary of status**
- include basic input validation for **non-empty task names**

### Completion Criteria

A submission meets the checkpoint target when:

- ✅ the menu loop works  
- ✅ tasks persist in memory during the run  
- ✅ complete and delete actions work  
- ✅ invalid or empty task input is handled sensibly  
- ✅ the program does not lose all data during each menu cycle  

### Recommended Starter Structure

```python
tasks = []
running = True

while running:
    print("\n=== To-Do Manager ===")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark complete")
    print("4. Delete task")
    print("Q. Quit")

    choice = input("Choose an option: ").strip().lower()

    if choice == "1":
        # add task
        pass
    elif choice == "2":
        # list tasks
        pass
    elif choice == "3":
        # mark complete
        pass
    elif choice == "4":
        # delete task
        pass
    elif choice == "q":
        running = False
    else:
        print("Invalid choice.")
```

### Suggested Task Structure

```python
{"name": "Buy milk", "done": False}
```

### A Beginner-Friendly Add Pattern

```python
task_name = input("Enter task name: ").strip()

if task_name == "":
    print("Task name cannot be empty.")
else:
    tasks.append({"name": task_name, "done": False})
    print(f"Added task: {task_name}")
```

### A Beginner-Friendly List Pattern

```python
if len(tasks) == 0:
    print("No tasks yet.")
else:
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not done"
        print(f"{index}. {task['name']} [{status}]")
```

### A Beginner-Friendly Complete Pattern

```python
if len(tasks) == 0:
    print("No tasks to complete.")
else:
    task_number_text = input("Enter task number to mark complete: ").strip()

    if task_number_text.isdigit():
        task_index = int(task_number_text) - 1

        if 0 <= task_index < len(tasks):
            tasks[task_index]["done"] = True
            print(f"Marked '{tasks[task_index]['name']}' as complete.")
        else:
            print("Task number not found.")
    else:
        print("Please enter a valid task number.")
```

### A Beginner-Friendly Delete Pattern

```python
if len(tasks) == 0:
    print("No tasks to delete.")
else:
    task_number_text = input("Enter task number to delete: ").strip()

    if task_number_text.isdigit():
        task_index = int(task_number_text) - 1

        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Deleted task: {removed_task['name']}")
        else:
            print("Task number not found.")
    else:
        print("Please enter a valid task number.")
```

### Common Pitfalls to Watch For

1. **Reinitializing the list inside the loop**  
   This erases all tasks every cycle.

2. **Index errors when deleting**  
   Students may forget that list indices start at 0 but user-facing numbering often starts at 1.

3. **Empty task names**  
   Without a basic check, students may add blank tasks.

4. **No invalid-choice handling**  
   The program becomes brittle if unsupported menu input is ignored or crashes.

5. **Marking complete on missing task**  
   The code must check the selected number or name before updating.

### Optional Extension

If students finish early, they may add a filter such as:

- show only completed tasks
- show only incomplete tasks

This stays within Basics scope but should not distract from required functionality.

### Instructor Circulation Prompts

**[Instructor speaks:]**

While students work, use short assessment-friendly prompts:

- “Show me where your tasks are stored.”
- “How do you know the loop ends?”
- “What happens if I enter an empty task name?”
- “What happens if I choose task number 99?”
- “Can you prove complete/delete works with a quick test?”

These prompts support the assessment without giving away the entire solution.

---

## Section 6: Debrief, Reflection, and Exit Ticket (10 minutes)

### Debrief Focus

**[Instructor speaks:]**

Because this is an assessment-centered hour, the debrief should focus less on re-teaching content and more on reflection, quality, and transfer.

### Debrief Questions

**[Instructor asks:]**

- What testing strategy did you use before calling your program complete?
- Where did input validation matter most?
- What structure did you choose for task storage, and why?
- What bug did you catch by trying an invalid input or missing task?

### Instructor Synthesis

**[Instructor speaks:]**

This checkpoint is about more than one to-do manager. It is about whether students can organize their thinking around:

- looped user interaction
- conditional routing
- stored state
- safe updates and deletions
- predictable behavior when input is imperfect

If they can do that here, they are building durable programming habits.

### Exit Ticket

**[Instructor asks:]**

Answer in one or two sentences:

**What is one strategy you used to test a boundary case in your To-Do Manager?**

Examples of acceptable answers:

- “I tried deleting from an empty list.”
- “I entered a task number bigger than the number of tasks.”
- “I tested an empty task name to make sure it was rejected.”
- “I tried an invalid menu choice like `9`.”

---

## Recap: What We Accomplished in Day 4, Hour 4 / Course Hour 32

In this checkpoint hour, learners:

- demonstrated control flow and data structure skills in a single program
- built or refined a CLI To-Do Manager
- used a menu loop until quit
- added, listed, completed, and deleted in-memory tasks
- applied basic validation for empty input and invalid choices
- practiced self-testing with quick spot-checks and boundary cases

**[Instructor speaks:]**

This is a strong checkpoint because it asks students to combine what they know instead of repeating one isolated pattern. That is exactly how confidence grows: not from memorizing syntax, but from using familiar tools together in a meaningful way.

---

## Appendix A: Instructor Exemplar Solution

```python
# todo_manager.py
# Checkpoint 4 exemplar using list of dictionaries

tasks: list[dict[str, object]] = []
running = True

while running:
    print("\n=== To-Do Manager ===")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark complete")
    print("4. Delete task")
    print("Q. Quit")

    choice = input("Choose an option: ").strip().lower()

    if choice == "1":
        task_name = input("Enter task name: ").strip()

        if task_name == "":
            print("Task name cannot be empty.")
        else:
            tasks.append({"name": task_name, "done": False})
            print(f"Added task: {task_name}")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nTasks:")
            for index, task in enumerate(tasks, start=1):
                status = "Done" if task["done"] else "Not done"
                print(f"{index}. {task['name']} [{status}]")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to complete.")
        else:
            task_number_text = input("Enter task number to mark complete: ").strip()

            if task_number_text.isdigit():
                task_index = int(task_number_text) - 1

                if 0 <= task_index < len(tasks):
                    tasks[task_index]["done"] = True
                    print(f"Marked '{tasks[task_index]['name']}' as complete.")
                else:
                    print("Task number not found.")
            else:
                print("Please enter a valid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            task_number_text = input("Enter task number to delete: ").strip()

            if task_number_text.isdigit():
                task_index = int(task_number_text) - 1

                if 0 <= task_index < len(tasks):
                    removed_task = tasks.pop(task_index)
                    print(f"Deleted task: {removed_task['name']}")
                else:
                    print("Task number not found.")
            else:
                print("Please enter a valid task number.")

    elif choice == "q":
        print("Goodbye!")
        running = False

    else:
        print("Invalid choice. Please select 1, 2, 3, 4, or Q.")
```

---

## Appendix B: Suggested Rubric Notes for Instructors

### Correctness
- Menu loop repeats until quit
- All four required actions are present
- Task state persists during run
- Complete/delete actually change program state

### Readability
- Clear names like `tasks`, `task_name`, `choice`
- Indentation is consistent
- Output is understandable to the user
- Code branches align with menu choices

### Required Constructs
- Loop present
- Conditional routing present
- Data structure present
- Basic validation present

### Robustness
- Empty task names rejected
- Invalid menu choice handled
- Out-of-range task numbers handled
- Empty-list cases handled politely

---

## Appendix C: Common Assessment Errors and Interventions

### Error: Tasks disappear after each action
**Cause:** `tasks = []` placed inside the loop.  
**Intervention:** “Should the task list be created once or every cycle?”

### Error: Deleting the wrong task
**Cause:** Off-by-one confusion between display number and list index.  
**Intervention:** “If the user sees task 1, what is its actual list index?”

### Error: Program crashes on invalid complete/delete selection
**Cause:** No digit or range check before indexing.  
**Intervention:** “What should happen if I type `abc` or `99` here?”

### Error: Blank tasks allowed
**Cause:** Missing `.strip()` or empty-string check.  
**Intervention:** “What does your code do if the user just presses Enter?”

### Error: Student stops after add/list only
**Cause:** Incomplete feature set under time pressure.  
**Intervention:** “Which required action can you implement next with the least extra code?”

---

## Appendix D: Sample Boundary and Spot-Check Cases

Use these cases during grading, conferencing, or self-checking.

1. Start program and choose list before adding anything
2. Add `Buy milk`
3. Add `Study Python`
4. List tasks and confirm both appear as not done
5. Mark task 2 complete
6. List tasks and confirm status changed
7. Try menu choice `9`
8. Try delete task number `99`
9. Try adding an empty task name
10. Delete task 1 and verify remaining list
11. Quit cleanly

This test set is intentionally small but revealing.

---

## Appendix E: Additional Instructor Support Moves

### If students freeze because it is an assessment

Use calming, specific language:

- “Start with the menu shell.”
- “Get add working before anything else.”
- “List tasks as soon as you can so you can see your data.”
- “Then add complete and delete one at a time.”

This keeps the hour assessment-centered but not emotionally overwhelming.

### If students are close but incomplete

Coach them toward the highest-value unfinished feature. For example:

- If add/list work, push next toward mark complete.
- If complete works but delete does not, simplify delete to task number removal.
- If validation is weak, add the non-empty task name check first.

This helps students meet the checkpoint targets efficiently.

### If students want to over-engineer

Some learners may want to add due dates, categories, priorities, or colored output. Gently redirect:

“Those are interesting stretch ideas, but first make sure your required checkpoint features are correct and robust.”

That protects alignment to the rubric.

---

## Appendix F: Quick Reference Card for Students

### Checkpoint Success Checklist

- [ ] Menu repeats until quit
- [ ] Add task works
- [ ] List tasks works
- [ ] Mark complete works
- [ ] Delete task works
- [ ] Empty task names are rejected
- [ ] Invalid menu choices are handled
- [ ] Tasks stay in memory while running

### High-Value Reminders

- create the task list outside the loop
- validate before indexing into a list
- display numbering can start at 1 even though indices start at 0
- test empty and invalid cases, not just happy paths
- readable code is part of quality

---

## Appendix G: Instructor Observation Checklist During the Checkpoint

Use this as a quiet circulation tool while students work.

### Program Structure Checks

- [ ] Does the student have a visible menu loop?
- [ ] Is the shared task structure created outside the loop?
- [ ] Do the menu branches line up clearly with the listed choices?
- [ ] Is there an obvious quit path?

### Feature Checks

- [ ] Add task implemented
- [ ] List tasks implemented
- [ ] Mark complete implemented
- [ ] Delete implemented
- [ ] Basic non-empty validation present

### Robustness Checks

- [ ] Invalid menu choice handled
- [ ] Empty task list handled gracefully
- [ ] Out-of-range selection handled safely
- [ ] No obvious data reset bug

### Coaching Priority Rule

If a student is behind, prioritize support in this order:

1. menu + quit
2. add
3. list
4. complete
5. delete
6. polish

That order keeps the checkpoint achievable.

---

## Appendix H: Sample Instructor Conference Script

If you are doing short desk-side check-ins, these are helpful near-verbatim prompts.

### When a student says, “I don’t know where to start.”

**[Instructor speaks:]**

“Start with the smallest working version. Can you print the menu and make quit work first? Once that works, we’ll add one feature at a time.”

### When a student says, “My code is long and messy.”

**[Instructor speaks:]**

“Messy is okay while building. Let’s focus on whether each branch does one clear job. Which branch works already? Which branch is next?”

### When a student says, “Delete is broken.”

**[Instructor speaks:]**

“Before deleting, can you prove which task you matched? What number or name did the program receive, and what index does that map to?”

### When a student says, “I think I’m done.”

**[Instructor speaks:]**

“Great. Show me your self-test. Add a task, list it, try an invalid menu choice, try an invalid task number, then quit. If all of that behaves well, you are in strong shape.”

### When a student is overbuilding

**[Instructor speaks:]**

“Your extra ideas are good, but let’s secure the checkpoint requirements first. Correctness on the required features matters more than optional features that only partly work.”

---

## Appendix I: Reflection and Self-Assessment Prompts

These prompts help students think like evaluators of their own code.

### Quick Written Prompts

- “The feature I trust most is … because …”
- “The feature I tested most carefully was …”
- “One boundary case I checked was …”
- “If I had five more minutes, I would improve …”

### Verbal Pair-Share Prompts

Ask students to explain to a partner:

- how their tasks are stored
- how their loop ends
- how they prevent empty task names
- how they handle invalid selections

If a student can explain those four pieces clearly, they usually understand the core design of their program.

### Instructor Use

These reflections are useful even if a student’s code is incomplete. They reveal whether the student understands the intended control-flow design even when implementation is still in progress.

---

## Appendix J: Optional Post-Checkpoint Review Notes

If time remains after collection or informal grading, use the class’s experience to reinforce durable habits.

### Discussion Point 1: Why state placement matters

Revisit the classic bug:

```python
while running:
    tasks = []
```

**[Instructor speaks:]**

“A checkpoint like this makes the cost of that bug obvious. If tasks reset every cycle, your program cannot function as a manager at all.”

### Discussion Point 2: Why happy-path testing is not enough

Students often test:

- add one task
- list one task

and stop there.

Encourage the class to name additional checks that reveal quality:

- deleting from an empty list
- choosing menu option `9`
- typing an empty task name
- marking complete with an out-of-range number

### Discussion Point 3: How readability supports correctness

Messy code is not just a style issue. It makes bugs harder to spot. When branch logic is easy to read, debugging becomes faster. That is why readability belongs in the rubric.

---

## Appendix K: Short Oral Wrap-Up Script for the End of the Checkpoint

Use this short closing script if you want a more reflective ending before dismissing students.

**[Instructor speaks:]**

Today’s checkpoint was not just about tasks. It was about whether you can take a problem, organize it into menu choices, store data in memory, and update that data safely while the user interacts with your program.

That is a real programming skill.

Some of you finished every required feature. Some of you got close but still have one branch to clean up. In both cases, the important question is not only “What did I complete?” but also “What did I learn about building programs in stages?”

If your program had a bug, that does not erase the learning. In fact, checkpoints often make your next step clearer:

- test earlier
- build one branch at a time
- validate before indexing
- keep shared state outside the loop

Those are durable lessons, and they matter far beyond this one assessment.

---

**End of Day 4, Hour 4 Script / Course Hour 32**
