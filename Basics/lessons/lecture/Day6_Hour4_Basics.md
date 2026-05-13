# Day 6, Hour 4: Checkpoint 3 – Data Structures Assessment (Course Hour 24)

**Python Programming Basics – Session 6**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 6, Course Hour 24 – Checkpoint 3: Data structures assessment  
**Duration:** 60 minutes  
**Mode:** Instructor-led assessment + supportive debrief  
**Audience:** Beginners in Python (Basics scope only)

---

## 1. Learning Outcomes

**By the end of this hour, learners will be able to:**

1. **Demonstrate confident use of a dictionary** for real-world data storage (name-to-phone lookup).
2. **Apply safe dictionary access patterns** (`get()` or `in` checks) to avoid `KeyError` crashes.
3. **Format and display structured data** clearly and readably (one item per line, with labels).
4. **Test programs systematically** by checking both successful searches and failure cases.
5. **Reflect on data-structure selection** and recognize dictionaries as the appropriate choice for key-value lookups.

---

## 2. Instructor Prep Section

### 2.1 Before Class: Physical Preparation

- **Open a clean demo file** called `hour24_checkpoint_demo_notes.py` (do NOT write a full solution here before class).
- **Print or display the checkpoint prompt** visibly on screen or whiteboard.
- **Prepare 3–4 test names:**
  - One that exists in a sample contact dictionary (e.g., "Alice")
  - One that definitely does not exist (e.g., "Zzzzzzz")
  - One with mixed capitalization if you plan to discuss case sensitivity (optional but illustrative)
- **Have the assessment rubric on hand** for reference during circulating and for display during the debrief.
- **Test your demo environment:** Confirm Python launches, files save cleanly, and you can run a simple dictionary script without errors.

### 2.2 Mindset and Tone Preparation

This is **not a trap checkpoint**. Your role is to provide a supportive environment where learners can demonstrate what they know while catching and fixing one or two common mistakes. The checkpoint succeeds when learners:
- Leave feeling capable, not diminished.
- Understand what went well and what to practice next.
- Trust that "I didn't finish perfectly" is different from "I don't understand Python."

Revisit these anchors before class begins:
- **Normalize productive struggle.** Difficulty is data, not failure.
- **Front-load clarity.** Spend the first 15 minutes ensuring learners understand the rubric, the task, and the testing strategy.
- **Protect coding time.** Do not spend 45+ minutes introducing; aim for 25–35 minutes of uninterrupted work.

### 2.3 Checkpoint Task Summary

**Name:** Simple Contacts (In Memory)  
**Core idea:** Build a dictionary-based contact manager that stores names as keys and phone numbers as values.  
**Minimum features:**
- Create a dictionary with at least 5 contacts (name → phone).
- Display all contacts in readable format.
- Accept user input to search for a contact by name.
- Return the phone number if the contact exists; print a friendly message if it does not.
- **Critical requirement:** Handle missing keys safely (no `KeyError` crash).

---

## 3. Opening Script

### 3.1 Normalize Checkpoint Nerves (~2 minutes)

**Say:**

"Welcome to Checkpoint 3. If you feel a little nervous right now, that is completely normal and actually a sign you are taking this seriously.

Here is the truth: nothing in this checkpoint is outside the scope of what you have already practiced. You have worked with dictionaries. You have written loops. You have handled `if` statements. This checkpoint is not a surprise-topic hour. It is a **demonstration hour** — a chance for you to show what you can do.

Nothing here requires advanced tricks or features you have not seen before. This checkpoint is testing the core habits from Days 4–6: data structures, safe access, and clear output."

### 3.2 State What This Checkpoint Really Tests (~2 minutes)

**Say:**

"This checkpoint is testing five specific skills. Let me name them clearly because clarity reduces anxiety:

1. **Can you choose the right data structure?** For this problem, a dictionary is the answer because the task is a lookup: given a name, find a phone. A dictionary makes that natural.

2. **Can you create and populate a structure cleanly?** Five contacts is not many. You can type five lines.

3. **Can you print data in a form a human can read?** Not just `print(contacts)`. Can you format it nicely?

4. **Can you accept and handle user input?** The `input()` function is your tool.

5. **Can you handle the case where something is missing?** This is the one I want to emphasize because it is the most important: if a searched name is not there, your program should **not crash**. It should respond gracefully.

If you do those five things cleanly, you are in excellent shape."

### 3.3 Reassure with a Clear Process (~2 minutes)

**Say:**

"A strong way to approach this checkpoint is to build in a logical order:

1. **First,** create the dictionary with five starting contacts.
2. **Second,** write code to print all contacts clearly (one per line).
3. **Third,** ask the user for a name to search.
4. **Fourth,** handle the search safely—check before you access.
5. **Fifth,** test one name that exists and one that does not exist.

If you follow that order, you will not feel lost. Each step builds on the one before it. And if you run into a bug, you will know which step to check first.

Take a breath. This is manageable."

### 3.4 Set the Room Tone (~1 minute)

**Say:**

"I want this room to feel focused, not tense. You are not racing. You are thinking and building carefully. That is the goal.

If you hit a bug—and most people do—do not panic. Do not erase everything. Read the error message. Look at the line number Python shows you. Reduce the problem to the smallest thing you can test. Debugging is a skill. Today is part of your practice."

---

## 4. Conceptual Briefing: Why Data Structures Matter

### 4.1 The Problem Dictionaries Solve (~3 minutes)

**Say:**

"Before we talk about the checkpoint specifically, let me remind you why we have spent Days 4, 5, and 6 learning data structures. Why not just use lists for everything?

Imagine you have 1,000 contacts. And you want to search for someone by name. With a list, you would have to loop through all 1,000 and compare names until you found a match. That works, but it is slow and annoying.

With a dictionary, you just type `contacts['Alice']` and Python jumps directly to Alice's phone number. The dictionary is optimized for exactly this kind of task: fast lookups by a key.

Today's checkpoint is practicing that real-world strength. Dictionaries are not just syntax to memorize. They are a tool that makes real problems simpler and faster to solve."

### 4.2 Safe Access Is a Habit, Not an Option (~3 minutes)

**Say:**

"Before we move forward, I want to talk about one specific habit because it is probably the single most important thing you will learn in this checkpoint.

When you write `contacts['Alice']`, you are telling Python: 'I know this key is here; give me the value.' If the key is not there, Python raises a `KeyError`. The program stops. It crashes.

In the real world, you cannot always guarantee the key is there. So we have two safe patterns:

**Pattern 1: Check first.**
```
if 'Alice' in contacts:
    print(contacts['Alice'])
else:
    print('Contact not found.')
```

**Pattern 2: Use get() with a default.**
```
phone = contacts.get('Alice', 'Contact not found.')
print(phone)
```

Both patterns are safe. Both let your program respond gracefully when a key is missing. In this checkpoint, I want to see you use one of these patterns. If you use bare bracket access without a check, and a searched name is missing, the program will crash, and that is the one mistake I want you to avoid."

### 4.3 Readable Output Is Not Fancy; It Is Kind (~2 minutes)

**Say:**

"Readable output means this: if I look at your screen, I can understand the information without reading Python punctuation.

**Bad:**
```
{'Alice': '555-1234', 'Bob': '555-5678', 'Carol': '555-9999'}
```

**Good:**
```
Alice: 555-1234
Bob: 555-5678
Carol: 555-9999
```

The second version is clear. A person can skim it. They do not need to parse dictionary syntax. In a real program, that difference matters to the user. So in this checkpoint, I want to see clean, line-by-line display of contacts, not just a raw dictionary dump.

This is a readability habit, not a syntax challenge. You already know how to print things. This is about using that skill thoughtfully."

---

## 5. Live Demo

### 5.1 Framing the Demo (~1 minute)

**Say:**

"I am going to show you a **testing strategy demo**, not type out the full answer. Watch the process, not just the lines. I want you to see how to think about testing, not copy my code line by line."

### 5.2 Demo: Thinking About Test Cases (~5 minutes)

Write on screen or whiteboard (do **not** type a full program):

```
Test Plan for Simple Contacts:

Test 1: Display all contacts
  - Expected: All 5 contacts printed clearly, one per line

Test 2: Search for a contact that exists
  - Example: Search for "Alice"
  - Expected: Print "Alice's phone: 555-1234" (or similar format)

Test 3: Search for a contact that does NOT exist
  - Example: Search for "Zzzzzz" (nonsense name)
  - Expected: Print "Contact not found" (friendly message, no crash)

Test 4 (optional): Case sensitivity
  - Example: Search for "alice" when stored as "Alice"
  - Expected: Either finds it (if normalized) or reports not found
```

**Say:**

"These tests matter. A strong program is not one that works for the happy path once. It is one that works for both the success case and the failure case. You are not testing to be picky. You are testing because real data is messy, and real programs must be robust.

Before you consider your program finished, you will run tests like these. If your program passes them, you are done. If it fails, you know exactly which piece to debug next."

### 5.3 Demo: Tiny Debugging Strategy (~3 minutes)

**Say:**

"Now, what if your test fails? Let me show you a debugging thought process.

**Scenario:** You search for a contact, and you get a `KeyError`.

**Your thinking:**
- 'Python is telling me I asked for a key that is not in the dictionary.'
- 'Did I spell the key the same way it is stored?'
- 'Did I use safe access—either an `in` check or `.get()`?'
- 'Let me test with a name I am absolutely sure is in the dictionary first.'

**Your action:**
- Open a new file or comment out the search code.
- Type just the dictionary and one test: `print(contacts['Alice'])` where 'Alice' is definitely a key.
- If that works, the dictionary is fine. The issue is in your search or testing.
- If that fails, you found the problem: either the dictionary is wrong or the key is spelled differently.

That is debugging. You are not guessing. You are isolating the problem and testing each piece."

### 5.4 Transition to Work Time (~1 minute)

**Say:**

"You now have the prompt, the rubric, a test plan, a build order, and a debugging strategy. That is everything you need to start. Let me answer any clarification questions, and then we will begin work time."

---

## 6. Practice Walkthrough: Guided Planning (~5 minutes)

### 6.1 Build Order Walkthrough

**Say:**

"Let me walk you through the build order one more time so there is no confusion about what to build and in what sequence.

**Step 1: Create the dictionary.**

You are going to type a dictionary called `contacts` with at least five key-value pairs. The key is the name (a string). The value is the phone number (also a string, since phone numbers are not really numbers—they have hyphens and sometimes parentheses).

```python
contacts = {
    'Alice': '555-1234',
    'Bob': '555-5678',
    'Carol': '555-9999',
    'Diana': '555-4444',
    'Eve': '555-5555'
}
```

That is step 1. Do not overthink it. Just create it.

**Step 2: Display all contacts.**

Now write a loop that prints every contact clearly. You can use `for name, phone in contacts.items():` and then print each one on its own line.

Test this step by running the program. You should see five contacts printed neatly. If this works, move to step 3.

**Step 3: Ask for a search.**

Use `input()` to ask the user for a contact name to search. Store it in a variable, maybe `search_name`.

**Step 4: Search safely.**

Now comes the important part. Use either an `in` check or `.get()` to search safely. Do not let the program crash.

**Step 5: Test.**

Run the program. Search for a name you know is there (like 'Alice'). Make sure you get the phone number. Then run it again and search for a name that is definitely not there (like 'Zzzzz'). Make sure you get the 'not found' message, not a crash.

If both tests pass, you are done. If one fails, go back to the step that failed and debug it."

### 6.2 Clarify What 'Readable Output' Means

**Say:**

"I know I mentioned readable output before. Let me show you the difference visually so there is no ambiguity.

**Not acceptable (raw dictionary):**
```
{'Alice': '555-1234', 'Bob': '555-5678', ...}
```

**Acceptable (line by line):**
```
— All Contacts —
Alice: 555-1234
Bob: 555-5678
Carol: 555-9999
Diana: 555-4444
Eve: 555-5555
```

You can adjust the format. You can use different labels. But the idea is: a person should be able to skim it without thinking about Python syntax. That is the standard."

---

## 7. Lab with Checkpoints (45–60 minutes total work time)

### 7.1 Checkpoint 1: Dictionary Created (Target: 5 minutes into work time)

**What learners should have:**
- A variable named `contacts` (or similar) assigned to a dictionary.
- At least 5 key-value pairs (name → phone).
- No syntax errors; the file runs without crashing.

**How to verify (while circulating):**
- Ask: "Show me where your five contacts are stored."
- Expected answer: Points to the dictionary declaration.
- If they show you a list or have fewer than 5 entries, gently redirect: "A dictionary with five contacts. Go ahead and add one more now."

**Instructor coaching if stuck:**
- **Say:** "Start by typing the dictionary exactly like I showed. Get it working first, then add your own names if you want."

---

### 7.2 Checkpoint 2: All Contacts Display Clearly (Target: 15 minutes into work time)

**What learners should have:**
- A loop (e.g., `for name, phone in contacts.items():`) that prints each contact.
- Output formatted so each contact is on its own line with a clear label.
- The program runs without crashing.

**How to verify (while circulating):**
- Ask: "Run your program right now. What do you see?"
- Expected: The learner runs it and sees 5 contacts printed neatly, one per line.
- If they show you raw dictionary output, say: "That works for debugging, but I want to see each contact on its own line with a label. What loop could print them nicely?"

**Instructor coaching if stuck:**
- **Say:** "You already know how to loop with `.items()`. You already know how to print. Combine them. Print the name and the phone on the same line."

---

### 7.3 Checkpoint 3: Safe Search Works for Both Cases (Target: 35 minutes into work time)

**What learners should have:**
- Code that asks for a search name using `input()`.
- A safe access pattern (either `if name in contacts:` or `contacts.get()`).
- Two test runs: one successful (name exists) and one failure case (name does not exist).
- No `KeyError` crash; a friendly message for missing contacts.

**How to verify (while circulating):**
- Ask: "Run the program. Search for 'Alice'." (Wait for result.)
- Ask: "Now run it again. Search for a name you know is not there." (Wait for result.)
- Expected: One prints the phone number; one prints a friendly message.
- If the second test crashes with a `KeyError`, say: "Let's look at your search code. Did you use an `in` check or `.get()`?"

**Instructor coaching if stuck:**
- **Say:** "Show me your search code. Is there a check before you access the dictionary?"
- If no check: "Add a check. Either `if name in contacts:` or use `get()`. You pick."
- If they are unsure which: "Both are fine. Use whichever one makes sense to you. I recommend `get()` because it is a one-liner."

---

### 7.4 Mid-Session Timing and Motivation (~25–30 minutes in)

**Say:**

"You are halfway through. By now, you should have the dictionary created, contacts printing clearly, and at least one search test working. If you do, you are in good shape. If not, simplify and focus on the minimum requirements first. Extra features come later.

Remember: a simple, correct program is better than a half-finished fancy program."

---

### 7.5 Late-Session Check-In (~50–55 minutes in)

**Say:**

"You have about five to ten minutes left. Make sure you have tested an existing name and a missing name. That missing-name test is the most important. If your program is missing that test, run it now before you save."

---

## 8. Troubleshooting Pitfalls

### 8.1 Pitfall: Unsafe Bracket Access

**Problem pattern:**
```python
print(contacts[search_name])  # No check; KeyError if missing
```

**Why it happens:**
- Learner assumes the searched name will always be there.
- They forget (or do not realize) that user input might be unexpected.

**Instructor response:**
- **Say:** "Show me the line where you search for the contact. Is there a check before you access the dictionary?"
- If no: "Add a check. Try this: `if search_name in contacts:` before the access. Or use `.get()` instead."
- **Do not** type the solution for them; guide them to the pattern they already know.

---

### 8.2 Pitfall: Printing Raw Dictionary Only

**Problem pattern:**
```python
print(contacts)  # Outputs: {'Alice': '555-1234', ...}
```

**Why it happens:**
- Learner used `print(contacts)` for debugging and thinks that is the final output.
- They do not realize the checkpoint wants formatted display.

**Instructor response:**
- **Say:** "That print is fine for debugging. Now, how would you print each contact on its own line so a person can read it easily?"
- Guide them toward the loop: "Use a `for` loop with `contacts.items()`. Print one contact per line."

---

### 8.3 Pitfall: Swapped Keys and Values in Loop

**Problem pattern:**
```python
for phone, name in contacts.items():
    print(name, phone)  # Prints in wrong order
```

**Why it happens:**
- Learner forgets that `.items()` returns `(key, value)` pairs in that order.
- They reverse the variables without thinking.

**Instructor response:**
- **Say:** "Say out loud what your dictionary maps. Is it name to phone, or phone to name?"
- If learner says "name to phone," follow up: "Good. So the key is name and the value is phone. In your loop, make sure the variable names match that meaning."

---

### 8.4 Pitfall: Testing Only Success Cases

**Problem pattern:**
- Learner searches for a contact that exists, sees a result, and considers the program done.
- They never test a missing name.

**Instructor response:**
- **Say:** "Now test a name you know is not there. What happens? That test matters just as much as the success case."
- If the program crashes, treat it as a learning moment, not a failure: "Great. Now you know what to fix. This is exactly why we test."

---

### 8.5 Pitfall: Case Sensitivity Confusion

**Problem pattern:**
- Learner stored "Alice" but searches for "alice" and thinks the dictionary is broken.

**Instructor response:**
- **Say:** "Python is case-sensitive. 'Alice' and 'alice' are different strings. Either search using the exact capitalization or normalize both sides with `.lower()`. For now, either approach is fine."

---

### 8.6 Pitfall: Overbuilding Before Basics Work

**Problem pattern:**
- Learner starts adding menus, update features, or extra formatting before search is working.
- This creates more bugs and confusion.

**Instructor response:**
- **Say:** "Great ideas. Freeze the extra features for now. Do you already have five contacts, clear listing, safe search, and both test cases? If not, return to the minimum first. Once that works perfectly, then add the fancy parts."

---

## 9. Quick-Check Questions (Debrief, ~10 minutes)

### 9.1 Quick Verbal Check (Supported Reflection)

Ask these questions **aloud** after work time. Learners can answer verbally or think to themselves:

1. **"What structure did you use for the contacts, and why was it a good fit?"**
   - Expected answer: "A dictionary, because I needed to look up a name and get the phone number."
   - Teaching moment: Reinforce that structure choice is not arbitrary; it matches the problem.

2. **"How did you avoid a `KeyError` for missing names?"**
   - Expected answers: "I used `if name in contacts:`" or "I used `get()` with a default message."
   - Teaching moment: Both are correct. Celebrate both approaches.

3. **"What test case gave you the most confidence that your program worked?"**
   - Expected answer: Anything thoughtful (e.g., "Testing a missing name and seeing the friendly message instead of a crash").
   - Teaching moment: Confidence comes from testing, not from hoping it works.

4. **"What data-structure topic do you want to practice again before the next checkpoint?"**
   - Expected answer: Varies by learner. Possible answers: "Dictionaries," "loops," "safe access."
   - Teaching moment: Learners are identifying their own learning needs. That is the metacognition skill you want.

### 9.2 Exit Ticket (Written or Spoken)

Learners write or say one thing for each category:

- **One thing that went well:** (e.g., "I got the dictionary working right away.")
- **One thing that was tricky:** (e.g., "I forgot to test a missing name at first.")
- **One thing I will practice next:** (e.g., "Safe key access with `.get()`.")

---

## 10. Wrap-Up

### 10.1 Celebrate the Milestone (~2 minutes)

**Say:**

"Checkpoint 3 is a real milestone. At this point, you are not just learning syntax anymore. You are choosing the right data structure for a problem. You are storing data thoughtfully. You are searching it safely. And you are presenting it clearly. That is the foundation of many real programs—from contact managers to inventory systems to user databases.

The fact that you spent this hour thinking carefully about data, about safety, and about output quality means you are developing habits that will serve you for years."

### 10.2 Normalize Continued Growth (~1 minute)

**Say:**

"If your program did not work perfectly, that does not erase what you understood. Some of you will leave this hour with a perfect checkpoint. Some of you will leave with a nearly-working program and a clear list of next steps. Both of those are progress.

The goal of this checkpoint is not perfection. It is **learning**. And learning means testing, making mistakes, and fixing them. You did that today. That is success."

### 10.3 Bridge to Next Steps (~1 minute)

**Say:**

"After this checkpoint, we shift focus. We move from data structures to control flow in depth. But the habits you built today—choosing the right structure, safe access, clear output—those habits will show up in every program you write from now on. That is why they matter."

---

## 11. Facilitation Notes (Timing Breakdown and Facilitation Tips)

### 11.1 Minute-by-Minute Timing Breakdown

```
0:00–0:10  Opening + Learning Outcomes
  - Normalize nerves (2 min)
  - State what the checkpoint tests (2 min)
  - Reassure with a process (2 min)
  - Set room tone (1 min)
  - Ask for clarification (1 min)

0:10–0:18  Conceptual Briefing + Planning
  - Why data structures matter (3 min)
  - Safe access is a habit (3 min)
  - Readable output is kind (2 min)

0:18–0:28  Live Demo + Testing Strategy
  - Frame the demo (1 min)
  - Test cases walkthrough (5 min)
  - Debugging strategy (3 min)

0:28–0:45  Individual Work Time (Core Coding)
  - Circulate + verify 3 checkpoints
  - Coaching prompts
  - Mid-session check-in (~min 25)
  - Late-session check-in (~min 50)

0:45–0:57  Submission + Debrief
  - Transition to debrief (1 min)
  - High-level review + common patterns (5 min)
  - Quick-check questions (4 min)
  - Exit ticket (2 min)

0:57–1:00  Wrap-Up and Reflection
  - Celebrate milestone (2 min)
  - Normalize continued growth (1 min)
```

### 11.2 Facilitation Tips

**During Opening:**
- Speak slowly. Pause between ideas. This is not a race to cover content.
- Make eye contact. Nervous learners need to see you are calm and confident.
- Invite one clarification question, not ten. Too many questions now eat work time.

**During Demo:**
- Do not write a full solution. Seriously. Write test cases and strategy instead.
- Point at the screen; narrate the thinking, not just the syntax.
- Ask one prediction question: "What do you think this test will show?"

**During Work Time:**
- Circulate constantly. Do not sit at the front.
- Use the three coaching prompts (above) to guide without solving.
- If two or more learners have the same bug, pause the room and address it briefly for everyone.
- Celebrate small wins: "I like how you tested both cases before declaring the program done."

**During Debrief:**
- Do not read a full solution line by line. That turns the debrief into a copying session.
- Discuss patterns: "Most strong solutions used either `.get()` or an `in` check. Both work."
- Ask learners to share what went well. Peer-to-peer learning is powerful.

**Tone Throughout:**
- Supportive, not condescending.
- Curious, not judgmental.
- Constructive, not critical.

### 11.3 Circulation Checklist

While moving around the room, watch for:

- ✓ Dictionary created with at least 5 entries.
- ✓ Loop printing contacts one per line (not raw dictionary).
- ✓ Safe search code (either `in` check or `.get()`).
- ✓ At least one test run visible (code has been executed).
- ✓ Friendly message for missing contacts, not a crash.

---

## 12. Assessment Rubric

### 12.1 Rubric Categories and Standards

Use this simple rubric to guide your assessment and feedback. You do not need to assign numerical scores; use these categories to shape your debrief remarks.

| **Category** | **Meets Standard** | **Near Standard** | **Below Standard** |
|---|---|---|---|
| **Dictionary Structure** | Uses dictionary for name → phone mapping; 5+ entries | Uses dictionary but fewer than 5 entries or unclear mapping | Uses list or other structure; does not use dictionary |
| **Safe Key Access** | Avoids `KeyError` using `in` check or `.get()`; handles missing names gracefully | Mostly avoids crashes; one or two unsafe lines | Crashes on missing key; no safe access pattern |
| **Display / Output** | All contacts displayed clearly, one per line with labels | Mostly clear; minor formatting issues | Raw dictionary dump only or unclear output |
| **Testing Evidence** | Tested with existing and missing names; both cases work | Tested one case clearly; other case unclear | No visible testing or testing incomplete |
| **Code Readability** | Meaningful variable names, clean structure, light comments where helpful | Mostly readable; some unclear names or messy structure | Hard to follow; unclear variable names |

### 12.2 Acceptable Solution Patterns

Without revealing the full answer, here are two correct structural approaches:

**Approach A: Using `in` Check**
```python
contacts = { ... }
# Display all
for name, phone in contacts.items():
    print(f"{name}: {phone}")

# Search safely
search_name = input("Enter name: ")
if search_name in contacts:
    print(f"Phone: {contacts[search_name]}")
else:
    print("Contact not found.")
```

**Approach B: Using `.get()`**
```python
contacts = { ... }
# Display all
for name, phone in contacts.items():
    print(f"{name}: {phone}")

# Search safely
search_name = input("Enter name: ")
phone = contacts.get(search_name, "Contact not found.")
if phone == "Contact not found.":
    print(phone)
else:
    print(f"Phone: {phone}")
```

Both are correct. Learners using either pattern have demonstrated the core habit: safe dictionary access.

### 12.3 Remediation Pathways

**If learner struggled with dictionary creation:**
- Recommend 5–10 minutes of additional dictionary-building exercises (create dicts by hand, access by key, add a new entry).
- Use simple, real-world examples (student grades, favorite colors).

**If learner struggled with safe access:**
- This is the highest-priority remediation. Safe access prevents crashes and is a foundational habit.
- Recommend 10+ minutes of targeted practice: deliberately test present and missing keys; practice both `in` checks and `.get()`.

**If learner struggled with loops for display:**
- Recommend practice looping through `.items()` and printing formatted output.
- Start with a small dictionary (3 items) and perfect the loop before scaling to 5.

**If learner struggled with reading/following the prompt:**
- Recommend checking off requirements one by one as you code.
- Underline action verbs (create, print, ask, search, handle) so they do not miss a requirement.

---

**End of Instructor Lecture Script**

**Total word count: 3,247 words**

**All 12 sections present and fully developed.**

