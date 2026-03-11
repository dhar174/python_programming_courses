# Day 6, Hour 4: Checkpoint 3 – Data Structures Assessment (Course Hour 24)
**Python Programming Basics – Session 6**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 6, Course Hour 24 – Checkpoint 3: Data structures assessment  
**Duration:** 60 minutes  
**Mode:** Instructor-led assessment + supportive debrief  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is a detailed read-aloud teaching guide for Course Hour 24. This hour is a checkpoint assessment, but the tone should remain calm, supportive, and confidence-building. The target skill is not speed for speed’s sake. The target skill is demonstrating correct, readable use of the core data structures covered so far, especially dictionaries. The assessment task is **Simple Contacts (in memory)**. Learners store contact names and phone numbers in a dictionary, add starting contacts, search by name, and list all contacts clearly. The most important technical reminder is: **handle missing keys safely**. Do not let learners crash with a `KeyError`. Before work time, provide structure, testing advice, rubric clarity, and supportive expectations. Do **not** give a full worked solution before work time. After work time, debrief at a high level and discuss common patterns, but do not turn the checkpoint into a copy exercise. Every **Say:** block is written to be read nearly verbatim; adapt naturally while preserving the calm, supportive pacing.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Demonstrate confident use of a dictionary for name-to-phone lookup.
2. Search for existing and missing names without causing a `KeyError`.
3. Format contact output clearly rather than printing only a raw dictionary.
4. Test your own program with both successful and unsuccessful search cases.
5. Reflect on which data-structure habits feel strong and which still need more practice."

---

## 1) Agenda + Timing

- **0:00–0:08** Assessment framing, reassurance, and rubric overview
- **0:08–0:15** Testing strategy demo and planning guidance
- **0:15–0:45** Individual checkpoint work time
- **0:45–0:55** Submission, debrief, and high-level review
- **0:55–1:00** Reflection and exit ticket

> **Instructor pacing note:** If your local delivery allows a longer assessment window, extend work time accordingly. The script below assumes a 60-minute hour, so it front-loads clarity and protects individual coding time.

---

## 2) Instructor Setup Checklist

- Open a clean file called `hour24_checkpoint_demo_notes.py` for showing testing ideas only. Do not type a full solution before work time.
- Have the checkpoint prompt visible on screen or printed.
- Prepare two or three sample test names:
  - one existing contact
  - one missing contact
  - one name with different capitalization if you want to discuss case sensitivity
- Have the checkpoint rubric visible.
- Be prepared to repeat the missing-key safety reminder several times.
- Decide how submissions or spot-checks will be collected before the hour begins.

**Say:** "This is a checkpoint, but it is a supportive checkpoint. The goal is to show what you can do, not to trick you. Read carefully, build step by step, and test with small examples as you go."

---

## 3) Opening Script: Supportive Assessment Framing (~8 minutes)

### 3.1 Normalize checkpoint nerves

**Say:**
"We are at Checkpoint 3. That means this hour is a chance to show what you can do with the core data structures we have covered so far.

If you feel a little nervous, that is normal. The good news is that nothing in this checkpoint is outside the scope of what you have already practiced. This is not a surprise-topic hour. This is a demonstration hour."

### 3.2 State what the checkpoint is really testing

**Say:**
"This checkpoint is not secretly about typing fast. It is not secretly about clever tricks. It is testing whether you can:
- choose a suitable structure
- store data clearly
- search it safely
- print readable output
- and avoid obvious crashes

That last point matters a lot today: if a searched name is missing, your program should handle that gracefully."

### 3.3 Reassure with a process

**Say:**
"A strong way to approach this checkpoint is:

1. Build the starting dictionary.
2. Print the contacts clearly.
3. Ask for a search name.
4. Handle the search safely.
5. Test one existing name and one missing name.

If you do those five things cleanly, you are in good shape."

### 3.4 Keep the environment calm

**Say:**
"I want the room to feel focused, not tense. Work steadily. If you hit a bug, do not panic and do not erase everything. Read the error, look at the line number, and reduce the problem to the smallest test you can understand."

---

## 4) Assessment Rules and Rubric Overview (~7 minutes)

### 4.1 Rules

**Say:**
"Here are the rules for the checkpoint:

- Work individually unless your local program rules say otherwise.
- Focus on correctness first, then formatting.
- Use concepts we have already learned.
- Do not worry about fancy features until the minimum requirements are complete.
- If you hit a bug, debug systematically instead of restarting from scratch."

### 4.2 The task at a glance

**Say:**
"Today’s build is **Simple Contacts (in memory)**.

That means you will store contact names and phone numbers using a dictionary. You will include at least five contacts, search by name, and print results clearly."

### 4.3 Rubric categories

**Say:**
"I will be looking at four broad areas:

1. **Correctness** — Does the program meet the prompt?
2. **Safe access** — Does it avoid a `KeyError` when a contact is missing?
3. **Readable output** — Does it print useful, clear information?
4. **Testing habits** — Did you check both a found and not-found case?

Those are the habits that matter most right now."

### 4.4 Read the minimum requirements aloud

Display or read:

### Checkpoint 3 — Simple Contacts (In Memory)

Build a Python program that does the following:

1. Create a dictionary that stores contact names as keys and phone numbers as values.
2. Include at least **five contacts** in the dictionary.
3. Print all contacts in a readable format.
4. Ask the user for a contact name to search.
5. If the contact exists, print the phone number.
6. If the contact does not exist, print a clear message without crashing.
7. Keep the program in memory only. Do not use files.

### 4.5 Name the most important technical reminder

**Say:**
"I am going to repeat the most important technical reminder: **handle missing keys safely**.

That means do not write code that assumes the searched name is definitely present unless you have already checked. You can use `get()` or you can use an `in` check first. Either is acceptable. What is not acceptable is a `KeyError` crash."

---

## 5) Planning Guidance Without Giving Away a Full Solution (~7 minutes)

### 5.1 Give high-level structure only

**Say:**
"Before you begin, let me give you a high-level structure — not a full solution, just a plan.

A sensible order is:

1. Create the starting dictionary with five contacts.
2. Print a heading like `Contacts:`.
3. Loop through the dictionary to print each name and phone number.
4. Ask the user for a name to search.
5. Handle the search safely.
6. Test one success case and one missing-name case.

That is enough structure to get you moving without me typing the whole answer for you."

### 5.2 Clarify acceptable safe patterns

**Say:**
"For the search part, there are two safe shapes you already know.

- You can use `if name in contacts:` and then access the value.
- Or you can use `contacts.get(name)` or `contacts.get(name, default_message)`.

Either approach is fine. Choose the one you understand best."

### 5.3 Discuss readable output expectations

**Say:**
"Readable output means more than dumping the raw dictionary with one `print(contacts)` and stopping there. During debugging, that is fine. For the final version, I want to be able to read each contact clearly, one line at a time, with labels if needed."

### 5.4 Optional case-normalization reminder

**Say:**
"If you want to make the search friendlier, you may normalize case. That is optional, but if you do it, be consistent. If you are not comfortable doing that cleanly, it is okay to leave the search case-sensitive and simply test it carefully."

### 5.5 Explicit reminder not to overbuild

**Say:**
"You do not need a menu system. You do not need file saving. You do not need classes. You do not need advanced formatting tricks. A simple, correct program is the goal."

---

## 6) Testing Strategy Demo (Without a Full Worked Solution) (~7 minutes)

### 6.1 Frame the demo carefully

**Say:**
"I am going to demonstrate *testing strategy*, not type the full answer. Watch the process, not just the lines."

### 6.2 Show how to think about test cases

On screen or board, write only sample test ideas, not full code:

```text
Test 1: Search for a name that exists
Test 2: Search for a name that does not exist
Test 3: If using case normalization, search with different capitalization
```

**Say:**
"These tests are important because many beginner programs work only for the happy path. Real confidence comes from testing both outcomes."

### 6.3 Model tiny debugging questions

**Say:**
"If your search is not working, ask yourself:

- Is the name I typed exactly the same as the key in the dictionary?
- Did I use safe access?
- Am I printing the value I think I am printing?
- Did I test with one known contact first before trying harder cases?"

### 6.4 Remind them about `KeyError`

**Say:**
"If you see a `KeyError`, do not just feel bad and stare at it. Read it. It is Python telling you that you asked for a key that is not in the dictionary. That is a fixable design issue, and today’s fix is safe key handling."

### 6.5 Give the green-light to begin

**Say:**
"At this point, you have the prompt, the rubric, a planning order, and a testing strategy. That is enough. Start building."

---

## 7) Individual Work Time Facilitation Guide (~30 minutes)

### 7.1 Start-of-work-time script

**Say:**
"Begin with the starting dictionary. Do not skip straight to the search before you have data to search. Build in order, and test after each step."

### 7.2 What to watch for while circulating

During work time, circulate and watch for:

- learners using a dictionary with at least five contacts
- learners printing only the raw dictionary and thinking they are finished
- learners writing `contacts[name]` before checking whether the key exists
- learners forgetting to test a missing name
- learners getting stuck on formatting before correctness is complete

### 7.3 Short coaching prompts to use individually

**Say:**
"Show me where your five contacts are stored."

**Say:**
"How are you handling the case where the name is missing?"

**Say:**
"Run it once with a name that exists. Now run it with one that does not. What happens?"

**Say:**
"Can you print the contacts one per line instead of printing the raw dictionary?"

**Say:**
"What is the smallest next step you can finish right now?"

### 7.4 Support learners without giving the full answer

**Say:**
"I can help you think, test, and debug, but I am not going to take your keyboard and write the solution for you. This checkpoint works best when you build it yourself."

### 7.5 Normalize productive struggle

**Say:**
"If you are stuck, that does not mean you are failing. It often means you are one small idea away from understanding. Reduce the problem. Test one piece. Then add the next piece."

### 7.6 Suggested midpoint time call

**Say:**
"You are about halfway through work time. By now, you should ideally have your contact dictionary created and the listing feature working. If you do not, simplify and finish the minimum requirements first."

### 7.7 Suggested late-stage time call

**Say:**
"You have about ten minutes left. Make sure you test an existing name and a missing name before you consider the program done. That missing-name test is especially important today."

---

## 8) Submission + Supportive Debrief (~10 minutes)

### 8.1 Transition from coding to reflection

**Say:**
"Please save your work and prepare to submit or share it according to our class process. Take one last look at your search logic and make sure missing names are handled safely."

### 8.2 High-level review only

**Say:**
"Now that work time has ended, let’s review the checkpoint at a high level without turning it into a copy session.

A strong solution had these traits:
- a clear dictionary of contacts
- at least five entries
- readable listing output
- safe search handling
- testing of both found and not-found cases"

### 8.3 Common patterns you likely saw

**Say:**
"Some common patterns I saw or expected to see include:
- a `for` loop through `contacts.items()` for display
- safe search with `get()`
- or safe search with `if name in contacts:`
- formatted printing with f-strings

Those are all appropriate Basics-level solutions."

### 8.4 Common mistakes to discuss supportively

**Say:**
"Common mistakes in this checkpoint are very normal:
- forgetting to handle a missing key safely
- printing the raw dictionary instead of formatting each contact
- testing only one name and assuming the program is finished
- mixing up keys and values in the display loop

If one of those happened to you, that gives you a clear practice target for next time."

### 8.5 Celebrate what this checkpoint represents

**Say:**
"Checkpoint 3 matters because it shows you can now use Python data structures to build something useful and reasonably robust on your own. That is a real milestone."

---

## 9) Reflection + Exit Ticket (~5 minutes)

### 9.1 Short written or spoken reflection

**Say:**
"Take a minute to reflect honestly. What part of this checkpoint felt solid, and what part still feels shaky? There is no penalty for honest reflection. It helps you practice smarter."

### 9.2 Exit ticket

```text
Quick check / exit ticket
```

Ask learners to answer one or more of these:

1. What structure did you use for the contacts, and why was it a good fit?
2. How did you avoid a `KeyError` for missing names?
3. What test case gave you the most confidence that your program worked?
4. What data-structure topic do you want to practice again before the next checkpoint?

### 9.3 Close the session positively

**Say:**
"Today you demonstrated real progress. You are not just learning syntax anymore. You are storing data purposefully, searching it safely, and presenting it clearly. That is the foundation of many real programs."

---

## 10) Post-Work Debrief Script: High-Level Review Without Giving a Pre-Work Walkthrough

### 10.1 Why the debrief still matters

**Say:**
"Even though this is a checkpoint, the debrief still matters. Learners need help turning the assessment experience into useful next steps. The debrief should focus on patterns, decisions, and common corrections — not on reading out a full finished answer line by line."

### 10.2 Review the structure choice explicitly

**Say:**
"The core structure choice in this checkpoint was a dictionary. That was the right fit because the problem was fundamentally a lookup problem: given a contact name, find the phone number. A dictionary maps naturally to that question."

### 10.3 Review what ‘clear output’ looked like

**Say:**
"Clear output did not mean fancy output. It simply meant that another person could look at the screen and understand the contacts without reading Python dictionary punctuation. Printing each contact on its own line with a name and a phone number label was completely sufficient."

### 10.4 Review safe missing-key handling again

**Say:**
"The safety habit from this checkpoint is worth naming again: never assume a searched key is present unless you have checked or used a safe access method. That is why `get()` and `in` checks matter. They help the program respond gracefully instead of crashing."

### 10.5 Invite short learner reflection

Ask:
- "What part of the checkpoint felt straightforward?"
- "What part caused the most hesitation?"
- "What one change improved your program the most?"

### 10.6 Keep the tone constructive

**Say:**
"If your program did not fully work yet, that does not erase what you understood. The goal of the debrief is to identify the next thing to practice, not to label yourself as good or bad at Python."

---

## 11) Common Pitfalls and Instructor Responses

### 11.1 Pitfall: Using bare bracket access unsafely

Problem pattern:

```python
print(contacts[search_name])
```

when `search_name` may not exist.

**Say:**
"This is the most important pitfall in the checkpoint. If the searched name is missing, the program raises a `KeyError`. When you see this, do not just tell the learner to 'be careful.' Guide them toward a safe pattern they already know."

Instructor response:

**Say:**
"What happens in your program when the name is not in the dictionary? Show me that branch. If there is no branch, that is the part to build next."

### 11.2 Pitfall: Printing only the raw dictionary

**Say:**
"Some learners will technically satisfy themselves by writing `print(contacts)` and moving on. That is not wrong as a debugging move, but it is not the final output standard we want."

Instructor response:

**Say:**
"That print helped you inspect the data. Good. Now how could you display one contact per line so a person could read it more easily?"

### 11.3 Pitfall: Mixing up keys and values in the display loop

Common buggy shape:

```python
for phone, name in contacts.items():
    print(phone, name)
```

**Say:**
"This is a great moment to reinforce that `items()` returns `(key, value)` pairs in that order. In this checkpoint, the key is the contact name and the value is the phone number."

Instructor response:

**Say:**
"Say out loud what your dictionary maps. Is it name to phone, or phone to name? Your loop variables should match that meaning."

### 11.4 Pitfall: Testing only one successful search

**Say:**
"A learner may search for an existing name, see a correct result once, and assume the program is done. But the whole checkpoint specifically requires safe handling of missing names."

Instructor response:

**Say:**
"Now test a name you know is not there. What happens? That test matters just as much as the success case today."

### 11.5 Pitfall: Case mismatch confusion

**Say:**
"Sometimes the learner typed `maya` but stored `Maya` and thinks the dictionary is broken. This is not a data-structure failure. It is a string-comparison issue."

Instructor response:

**Say:**
"For now, either search using the exact stored capitalization or consistently normalize both sides. Do not let a casing detail distract you from the bigger goal of safe dictionary access."

### 11.6 Pitfall: Overbuilding during the checkpoint

**Say:**
"A few learners will start adding menus, update features, delete features, or extra formatting before the minimum requirements are stable. This often creates more bugs."

Instructor response:

**Say:**
"Freeze the extra features for a moment. Do you already have five contacts, clear listing, safe search, and both test cases? If not, return to the minimum requirements first."

---

## 12) Remediation Notes: What to Practice After the Checkpoint

### 12.1 If the learner struggled with dictionary creation

Recommend practice with:
- writing small dictionaries by hand
- reading values by key
- adding one new key-value pair

**Say:**
"If the very first step felt shaky, more tiny dictionary exercises will help more than bigger projects right now."

### 12.2 If the learner struggled with safe search

Recommend practice with:
- `get()` vs bracket access
- `if key in d` checks
- deliberately testing present and missing keys

**Say:**
"Safe key access is one of the most valuable habits from this stage of the course. It is worth extra repetition."

### 12.3 If the learner struggled with loops for display

Recommend practice with:
- looping through `d.items()`
- printing `key` and `value` clearly
- using short f-strings for readable output

**Say:**
"Many programs become easier to understand once the display loop feels natural. That is a very worthwhile practice target."

### 12.4 If the learner struggled with reading the prompt

Recommend practice with:
- underlining verbs like create, print, ask, search, handle
- checking off requirements one by one
- testing each requirement separately

**Say:**
"Sometimes the issue is not Python knowledge. Sometimes it is project management: reading carefully, building in order, and verifying each requirement."

---

## 13) Appendix: Instructor Reference for Rubric and Coaching

### 10.1 Suggested simple rubric categories

Use or adapt the following categories if you need a fast scoring guide:

- **Meets structure requirement** — Uses a dictionary for name-to-phone mapping
- **Completes core features** — Has 5 contacts, listing, and search
- **Handles missing names safely** — No `KeyError`
- **Readable output** — Contact list and search result are clear
- **Basic testing evident** — Existing and missing names checked

### 10.2 High-level acceptable solution shapes

Without giving a full worked program, remember that acceptable solutions may use either of these safe search shapes:

```python
# Shape A
if search_name in contacts:
    ...
else:
    ...

# Shape B
phone = contacts.get(search_name)
if phone is None:
    ...
else:
    ...
```

### 10.3 Reminder about case handling

If you choose to discuss case normalization during debrief, keep it gentle:

**Say:**
"Case normalization is a nice improvement, but it is not more important than getting the basic safe search working. Correct and clear beats fancy."

### 10.4 Final instructor reminder

**Say:**
"Keep the checkpoint supportive. Learners should leave with a clear sense of what they can do and what to practice next, not with the feeling that one bug erased their progress."

---

## 14) Appendix: High-Level Structure You May Put on the Board

If learners need a non-code planning aid before work time, you may put this **high-level structure** on the board without turning it into a worked solution:

```text
1. Create contacts dictionary
2. Print all contacts clearly
3. Ask for name to search
4. Handle found case
5. Handle missing-name case safely
6. Test both cases
```

**Say:**
"This is not the answer. It is just a build order. The coding is still yours."

### 14.1 Why this level of scaffolding is appropriate

**Say:**
"Beginners often benefit from procedural structure even when they still need to write the actual code themselves. A build order reduces panic without removing the thinking."

### 14.2 What not to put on the board before work time

Do **not** put a full search solution, a full display loop, or a completed dictionary literal on the board before work time if that would effectively turn the checkpoint into a copy exercise. Keep the scaffolding high-level.

---

## 15) Appendix: Observation Notes for Fair, Supportive Scoring

### 15.1 What strong work looks like in this checkpoint

**Say:**
"Strong work in this checkpoint is not flashy. It is calm, correct, and readable. A strong submission usually has a clean dictionary, clear printed output, a safe search path, and evidence that the learner tested both an existing and a missing name."

### 15.2 What developing work looks like

**Say:**
"Developing work may still show meaningful understanding even if it is incomplete. For example, a learner may create the dictionary correctly and print it clearly but still struggle with the not-found search path. That should be understood as partial mastery, not total failure."

### 15.3 What to note for follow-up instruction

As you observe, note whether the learner mainly struggled with:

- choosing the correct structure
- dictionary syntax
- safe key handling
- loop-based display
- testing discipline

**Say:**
"These notes are valuable because they tell you what to reteach or review next. A checkpoint is not only for scoring. It is also diagnostic."

### 15.4 End the checkpoint on a growth message

**Say:**
"When you close the hour, remind learners that a checkpoint captures one moment of performance, not their ceiling. The most useful outcome is knowing what feels stronger now and what still needs repetition. That mindset keeps assessment connected to learning instead of turning it into a label."
