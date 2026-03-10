# Day 4, Hour 4: Checkpoint 2 – Lists + String Handling (Course Hour 16)
**Python Programming Basics – Session 4**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 4, Course Hour 16 – Checkpoint 2: Lists + string handling  
**Duration:** 60 minutes  
**Mode:** Instructor-led + checkpoint lab + debrief  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This is an assessment-centered hour, but it should still feel supportive and teachable. Stay tightly aligned to the Session 4 runbook. The checkpoint focuses on correct list use and clean output, not advanced architecture. The build target is a simple in-memory to-do list with menu-style options for add, remove, and show. No repeating menu loop is required yet. Walk through the structure at a high level only; do not give learners a full finished solution before they work.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

“By the end of this hour, you will be able to:
1. Demonstrate list creation and list updates in a short checkpoint program.
2. Use strings and list operations together to produce clean, user-facing output.
3. Display a numbered list of items.
4. Add items, remove items, and show items in a simple in-memory to-do list.
5. Explain the difference between removing by name and removing by position.
6. Reflect on whether your program is both correct and readable.

This checkpoint is not about trick questions. It is about showing that you can use the list skills from this session with confidence.”

---

## 1) Agenda + Timing (show slide / read quickly, ~2 minutes)

- **0:00–0:05** Calm framing, recap, and checkpoint expectations
- **0:05–0:15** Review of grading focus: correct list use + clean output
- **0:15–0:22** High-level walkthrough of the task structure only
- **0:22–0:47** Checkpoint Lab 2: simple to-do list in memory
- **0:47–0:55** Debrief, selected share-outs, and optional quick quiz
- **0:55–1:00** Recap and exit ticket

---

## 2) Instructor Setup Checklist (before class)

- Open a clean file such as `hour16_checkpoint2_todo.py`.
- Prepare a small example list such as `["email team", "buy notebook", "study lists"]` for explanation only.
- Prepare one example of clean numbered output.
- Have a short spot-check rubric ready: list storage, add item, remove item, show items, numbered output, no crash on typical inputs.
- Decide whether learners start from a blank file or a very small scaffold.
- Be ready to stop yourself from over-teaching. The checkpoint should measure learners’ control, not the instructor’s ability to complete the task for them.

**Say:** “This checkpoint is a chance to show what you can already do. You do not need advanced features. You need clear thinking, careful list use, and readable output.”

---

## 3) Opening Script: Set the Tone for Checkpoint 2 (~5 minutes)

### 3.1 Reconnect to the day’s learning arc

**Say:**
“Over the last three instructional hours, we have built a very specific skill set.

First, we learned how to create and change lists.
Then we learned how to process list items with a `for` loop.
Then we learned how to picture lists as rows inside a larger structure.

Now we pause for a checkpoint that stays in the same family of ideas: lists and strings together, with output that a user can actually read.”

### 3.2 Reduce unnecessary anxiety

**Say:**
“When some learners hear the word ‘checkpoint,’ they immediately assume the goal is to catch them making mistakes. That is not the purpose here.

The real purpose of a checkpoint is to make learning visible.
It answers questions like:
- Can you store items in a list?
- Can you update that list correctly?
- Can you show the current items cleanly?
- Can you produce output that a normal user could understand?”

### 3.3 State the build target clearly

**Say:**
“Your checkpoint task is to build a simple in-memory to-do list.
It needs three menu-style actions:
- add an item
- remove an item
- show items

At this point in the course, the menu does not need to repeat in a loop. A single pass through the user’s chosen action is enough. That scope control matters.”

### 3.4 State the scope boundaries out loud

**Say:**
“We are staying in Basics scope only.
That means:
- use a list to store to-do items
- keep the items as strings
- use clean printed output
- do not drift into files
- do not build a large multi-menu application
- do not introduce advanced features just because you know they exist”

---

## 4) Explain the Grading Focus Clearly (~10 minutes)

### 4.1 What the checkpoint is really measuring

**Say:**
“This checkpoint measures a small number of important basics. If learners understand these criteria, they usually perform better because the task feels concrete instead of mysterious.”

Write or read these aloud:

1. **Correct list creation and updates**
2. **Correct add and remove behavior**
3. **Clear, readable output**
4. **Numbered display of items when showing the list**
5. **No crashes on typical inputs**
6. **Reasonable code readability**

### 4.2 Correct list creation and updates

**Say:**
“First, the program must really use a list.
That means the to-do items should live in a list variable, not in separate variables.

Adding should place a new string into the list.
Removing should remove the intended item.
Showing should display the current contents of the list.”

### 4.3 Clean output matters

**Say:**
“This checkpoint is not only about internal correctness. It is also about communication.
If the program technically works but the output is messy, confusing, or incomplete, the user experience is poor.

For example, compare these two outputs:

`['email team', 'buy notebook', 'study lists']`

and

```text
To-Do List:
1. email team
2. buy notebook
3. study lists
```

The second version is much easier for a user to read.”

### 4.4 Numbered output should be explicit

**Say:**
“When learners show the to-do items, they should display them in a numbered list format.
That means the output should look like a list a human would naturally read.

A small detail like numbering makes a big difference in professionalism.”

### 4.5 Remove by name vs remove by index confusion

**Say:**
“The runbook names one important pitfall explicitly: confusion between removing by name and removing by index.

For this checkpoint, a clean beginner path is usually removing by name with `remove()` because the to-do items are strings.

If the learner tries to use `pop()`, they need to understand that `pop()` uses an index, not a name.”

### 4.6 The checkpoint is about calm correctness

**Say:**
“Remind learners that they do not need to add every possible feature. A smaller, correct, readable solution is stronger than a larger, fragile one.”

---

## 5) High-Level Walkthrough Only: Do Not Give the Full Solution (~7 minutes)

### 5.1 Explain the structure without handing over the answer

**Say:**
“I am going to walk through the shape of a good solution, but I am not going to project or hand you a full finished answer. The purpose is to help you organize your thinking, not to remove the problem-solving step.”

### 5.2 Step 1: create the list

**Say:**
“A good starting point is an empty list if the learner wants to build from scratch, or a short starter list if the exercise format provides one.”

Show this tiny fragment only:

```python
todo_items = []
```

Then say:

“This line creates the storage structure. Nothing more, nothing less.”

### 5.3 Step 2: ask the user which action they want

**Say:**
“The checkpoint uses menu-style options, but not a repeating menu loop yet. That means the learner can ask once which action they want, then branch based on that choice.”

Show only the idea, not a full solution:

```python
action = input("Choose an action: add, remove, or show: ")
```

### 5.4 Step 3: if the user chooses add

**Say:**
“If the action is `add`, the learner should ask for a to-do item and append it to the list.”

Show a tiny fragment:

```python
new_item = input("Enter a to-do item: ")
todo_items.append(new_item)
```

### 5.5 Step 4: if the user chooses remove

**Say:**
“If the action is `remove`, the learner should ask for the item name, then remove it if it exists. A membership check is a good beginner move here.”

Show only the key shape:

```python
item_to_remove = input("Enter the item to remove: ")

if item_to_remove in todo_items:
    todo_items.remove(item_to_remove)
```

Do **not** continue into a full finished program here.

### 5.6 Step 5: if the user chooses show

**Say:**
“If the action is `show`, the learner should print the items in a numbered list format. There are multiple valid ways to do that. For this checkpoint, a simple counter plus a `for` loop is completely appropriate.”

Show only the display pattern, still not a full program:

```python
number = 1
for item in todo_items:
    print(f"{number}. {item}")
    number += 1
```

### 5.7 Emphasize what you are intentionally not giving

**Say:**
“Notice what I did not do. I did not connect all of those pieces into one full answer for you. You still need to make the decisions about the branching structure, the exact output wording, and the flow of the program. That is the checkpoint part.”

---

## 6) Checkpoint Lab Instructions (~5 minutes of framing, then work time)

### 6.1 State the build requirements exactly

**Say:**
“Here is the checkpoint task in clear, simple language.”

```text
Checkpoint Lab 2: Simple To-Do List (in-memory)
- Menu options (no loop required yet): add item, remove item, show items.
- Store items in a list.
- Show numbered list output.
```

Then say:

“Your code should stay in memory only. No file saving. No repeated menu loop required yet. No advanced features required.”

### 6.2 Clarify what counts as success

**Say:**
“A successful checkpoint submission can do these three things:
- add an item correctly
- remove an item correctly
- show items clearly with numbering

And it should not crash on normal, expected usage.”

### 6.3 Encourage a build order

**Say:**
“If you are not sure where to start, use this order:
1. create the list
2. get the user’s action
3. make `show` work first because it is easy to see
4. make `add` work
5. make `remove` work
6. clean up your output”

This gives anxious learners a reliable path.

### 6.4 Remind them to test small cases

**Say:**
“Test your program with very small examples.
For example:
- start with one item and show it
- add one item and show again
- remove one item and show again

Small tests are easier to trust.”

---

## 7) Instructor Support During Work Time (~20–25 minutes)

### 7.1 What to say while circulating

Use these prompts instead of taking over the keyboard:
- “Show me where the list is created.”
- “What action did the user choose here?”
- “How are you deciding which block of code runs?”
- “If the user chooses `remove`, what value are you asking for?”
- “Are you removing by name or by position?”
- “Where is your numbered output?”
- “After changing the list, are you showing the updated result?”

### 7.2 Encourage debugging through observation

**Say to learners who are stuck:**
“Before you change more code, print what you already have.
Print the action.
Print the list before the change.
Print the list after the change.
That often reveals the misunderstanding quickly.”

### 7.3 Support learners who finish one branch only

**Say:**
“If you finish `show` first, that is good progress.
If you finish `add` second, that is more progress.
Then move to `remove`.
A checkpoint can be built piece by piece.”

### 7.4 Keep the class inside scope

If a learner starts designing a full application with repeating menus, data files, or advanced validation, say:

“That is interesting, but save it for later. Right now, the checkpoint is measuring the basics. Finish the Basics version first.”

### 7.5 Gentle help for learners who want to remove by number

**Say:**
“You may remove by number if you are very clear about the difference between number shown to the user and index used by Python, but for this checkpoint, removing by item name is often simpler and safer.”

That keeps the assessment aligned to the stated pitfall.

---

## 8) Common Pitfalls and How to Coach Through Them (~6 minutes)

### 8.1 Pitfall: remove by name vs remove by index confusion

**Say:**
“This is the most likely conceptual mistake in the checkpoint.
If the list contains strings like `"buy milk"` and the learner writes `pop("buy milk")`, the code is mixing up value and position.

Coach with the question:
‘Are you trying to remove by the item itself, or by where it sits in the list?’”

### 8.2 Pitfall: forgetting to reprint after a change

**Say:**
“Sometimes the learner successfully changes the list but never shows the updated state. Ask them: ‘How will the user know the action worked?’”

### 8.3 Pitfall: unclear output labels

**Say:**
“Output like `['task1', 'task2']` is technically valid Python output, but it is not the clearest user-facing output. Encourage labels like `To-Do List:` and numbered lines beneath it.”

### 8.4 Pitfall: action text mismatch

**Say:**
“If the learner expects `add` but types `Add`, the program may not match. At this stage, a simple `.lower()` is acceptable if already known, but do not let validation become the main story. The main story is list use and clean output.”

### 8.5 Pitfall: empty list display confusion

**Say:**
“If the list is empty, learners may wonder what to print. A simple message like `No items in the to-do list.` is perfectly reasonable and user-friendly.”

A tiny display fragment you can suggest if needed:

```python
if len(todo_items) == 0:
    print("No items in the to-do list.")
```

### 8.6 Pitfall: turning the checkpoint into a later-topic lesson

**Say:**
“This is not the time to introduce advanced loop design, exceptions, files, or functions as the core teaching focus. Keep bringing the class back to the essentials.”

---

## 9) Debrief and Selected Share-Outs (~8 minutes)

### 9.1 Reassemble the room calmly

**Say:**
“Let’s pause and look at what made solutions strong. Remember, the goal is not to compare who wrote the longest code. The goal is to identify what made the code clear and correct.”

### 9.2 Ask targeted reflection questions

Ask:
- “Who used a list and can point to where items were added?”
- “Who can explain how their remove logic works?”
- “Who printed the items in a numbered format?”
- “Who added a helpful message when the list was empty or an item was missing?”

### 9.3 Model high-level solution reasoning only

**Say:**
“A strong checkpoint solution usually has this shape:
- create a list
- ask for the action
- branch based on the action
- update or display the list as needed
- print clean output so the user sees what happened

That is the level of reasoning I want learners to take away.”

### 9.4 Reinforce that readable output is part of programming skill

**Say:**
“When beginners first start coding, they often focus only on ‘Does it run?’ That is an important question, but it is not the only question.

A second important question is ‘Can a human understand the output?’

This checkpoint intentionally asks for both.”

---

## 10) Optional Quick Quiz: Strings + Lists + Loops Basics (~4 minutes)

Use these as verbal checks, quick polling, or a mini whiteboard quiz.

1. What does `append()` do to a list?
2. What is the difference between `remove()` and `pop()`?
3. In plain English, what does `for item in todo_items:` mean?
4. Why is numbered output easier for a user to read?
5. If a list is empty, what is one polite message you could print?

**Instructor answer direction:**
- `append()` adds one item to the end
- `remove()` uses a value; `pop()` uses an index or the last item by default
- the loop visits each item one at a time
- numbering makes the output clearer and easier to scan
- something like `No items in the to-do list.`

---

## 11) Recap Script (~2 minutes)

**Say:**
“Checkpoint 2 brought together several important basics from Session 4.

We used lists to store items.
We used string handling to collect and display text clearly.
We used list operations to add and remove values.
We used simple loop logic to print numbered items.
And we kept the scope under control so the solution stayed readable.

That combination matters. Real beginner programs are not just about storing data. They are also about presenting it clearly.”

---

## 12) Exit Ticket (~1 minute)

Ask learners to answer verbally, in chat, or on paper:

1. What is the difference between removing an item by name and removing an item by index?
2. Why is a list a good structure for a simple to-do program?
3. What makes output ‘clean’ from a user’s point of view?
4. If your program works but the output is confusing, is the job fully done? Why or why not?

**Expected direction of answers:**
- name means the value itself, index means the position
- a list stores multiple to-do strings together in order
- clear labels, numbering, and readable messages
- no, because usable programs need understandable output too

---

## 13) Instructor Notes for Moving Beyond the Checkpoint

**Say:**
“Session 4 was all about building confidence with lists.

Across these four hours, learners have now practiced:
- creating and changing lists
- iterating through lists with `for` loops
- thinking about small table-like structures with nested lists
- combining list skills with string handling in a checkpoint task

That is strong progress. The next sessions will broaden the learner’s toolbox, but this foundation matters because collections show up everywhere in Python.”

Close with this final reminder:

“A short, correct, readable program is a strong program.”

---

## Appendix: Instructor Reinforcement Notes for Hour 16

### A) A simple spot-check rubric for live support

While learners work, keep the checkpoint aligned to a few visible questions:

1. Is there a real list storing the to-do items?
2. Does the learner have a clear action choice such as add, remove, or show?
3. Does add actually place a new string into the list?
4. Does remove operate on the intended item?
5. Does show produce readable, numbered output?
6. Does the program avoid crashing on normal inputs?

This keeps your support focused on the runbook goals: correct list use and clean output.

### B) Example instructor questions that preserve learner ownership

Instead of taking the keyboard, try these prompts:

- “What should the user type first?”
- “What should happen to the list after that?”
- “How will the user know the action worked?”
- “Are you removing by the item text or by its position?”
- “What output would look clearest to someone who is not reading your code?”

These questions guide the learner toward self-correction.

### C) Small test scenarios you can suggest during work time

If a learner says, “I think it works,” suggest one of these tests:

**Test 1: Empty show**
- choose `show`
- expected idea: a polite message or an empty-state output

**Test 2: Add one item**
- choose `add`
- enter `call dentist`
- expected idea: the item appears when shown

**Test 3: Remove existing item**
- choose `remove`
- remove a real item from the list
- expected idea: the item disappears and the output confirms the change

**Test 4: Remove missing item**
- choose `remove`
- enter an item not in the list
- expected idea: a readable message instead of a crash

These tests are small enough that beginners can reason about them easily.

### D) Example clean output formats for reference

You can show the class examples of good output without showing a full solution.

**Show action example**

```text
To-Do List:
1. email team
2. buy notebook
3. study lists
```

**Empty list example**

```text
No items in the to-do list.
```

**Remove-missing-item example**

```text
That item was not found.
```

The exact wording can vary. The important thing is that the output is easy to understand.

### E) Coaching language for common moments of frustration

If a learner says, “My code is messy,” say:

“Choose clarity over cleverness. One small step at a time is better than trying to solve everything in one jump.”

If a learner says, “Can I make the menu repeat forever?” say:

“You can later. For this checkpoint, finish the one-pass version first. The Basics version is the required version.”

If a learner says, “Can you just give me the answer?” say:

“I can help you see the shape of the answer, but I want you to connect the pieces so the checkpoint reflects what you understand.”

### F) A high-level closing reflection you can use

At the end of the hour, you can say:

“This checkpoint matters because it combines three beginner habits that really matter in real programs:
- storing related values together
- changing those values correctly
- presenting results in a way another person can read

That combination is more important than writing the shortest code.”

### G) Extra review prompts for the checkpoint debrief

If you want a slightly longer closing discussion, ask:

- “What made your output easier to read?”
- “How did you decide whether to remove by name or by position?”
- “What message did you show when an item was missing?”
- “What part of the checkpoint felt easiest?”
- “What part helped you realize you understand lists better than you did an hour ago?”

These questions help learners reflect on both correctness and communication.

### H) Final encouragement script

You can close the checkpoint hour with these words:

“You do not need a giant program to prove real progress. A small, correct, readable program is meaningful work.

If you can store items in a list, change them on purpose, and present them clearly to a user, you are doing real programming.

That is exactly what this checkpoint was designed to reveal.”

### I) Suggested final self-check learners can run before submitting

Invite learners to ask themselves:

- “Does my program really use a list?”
- “Can I add an item and see the change?”
- “Can I remove an item correctly?”
- “Does `show` produce numbered output?”
- “Would another person understand the printed messages?”

Then say:

“If the answer to those questions is yes, then the checkpoint is doing what it is supposed to do. It is showing that you can combine list skills and clean string output in a practical beginner program.”

### J) Closing teaching sentence to repeat aloud

Use this final line if you want a clean end to Session 4:

“Clear output matters because programs are for people, not just for Python.”

That sentence reinforces why the checkpoint focuses on both correct list use and readable string output.

One final checkpoint reminder: do not measure success only by how much code was written. Measure success by whether the program uses a list correctly, responds to a simple action clearly, and shows output that another person can read without guessing.

If there is time for one final reflection, ask learners to describe their program in plain English before they leave: “My program stores to-do items in a list, lets the user choose a simple action, and shows the results clearly.” That sentence reinforces both the technical structure and the communication goal of the checkpoint.

A final instructor reminder: the checkpoint stays successful when the learner can explain what the list stores, what action the user selected, and what the user sees after the action. That explanation is just as important as the code itself because it shows intentional, readable problem solving.

Keep the closing message simple: correct list use plus clean output is already meaningful programming work, and that is the exact target of Checkpoint 2.

That is enough for a strong Basics-level checkpoint hour.
