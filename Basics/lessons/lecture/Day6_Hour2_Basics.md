# Day 6, Hour 2: Data-Structure Drill Circuit (Course Hour 22)
**Python Programming Basics – Session 6**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 6, Course Hour 22 – Data-structure drill circuit  
**Duration:** 60 minutes  
**Mode:** Instructor-led + timed guided practice + share-out  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is a detailed read-aloud teaching guide for Course Hour 22. The purpose of this hour is fluency through structured repetition. Learners already know the core structures from Session 5 and just practiced structure choice in Hour 21. This hour should feel energetic, practical, and supportive. It is a drill circuit, not a high-stakes assessment. The runbook names four short tasks: list filtering, set uniqueness, dictionary counting, and tuple unpacking. Keep reinforcing a simple rhythm at every station: **read the prompt, choose the right structure, build the smallest working version, test with tiny data, then improve output if time remains**. Stay within Basics scope. Do not require comprehensions, lambdas, advanced sorting, nested dictionaries, or clever shortcuts. The goal is steady confidence, not speed for speed’s sake. Every **Say:** block is written to be read nearly verbatim; adapt naturally, but keep the supportive tone and practical guidance.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Complete short practice tasks using lists, tuples, sets, and dictionaries with increasing confidence.
2. Recognize the core pattern behind each structure quickly: list filtering, set uniqueness, dictionary counting, and tuple unpacking.
3. Test small pieces of code with sample values before deciding a task is finished.
4. Explain verbally why a given structure fits a specific short problem.
5. Share one working solution and describe one mistake you corrected during practice."

---

## 1) Agenda + Timing

- **0:00–0:05** Set expectations and explain the drill-circuit format
- **0:05–0:11** Quick demo of one station and expected output style
- **0:11–0:47** Four short stations with circulation and time checks
- **0:47–0:55** Share-out and solution walkthroughs
- **0:55–1:00** Recap and exit ticket

> **Pacing note:** The runbook describes four short tasks. In a live room, do not obsess over mathematically perfect equal timing. A practical rhythm is about 8–9 minutes per station plus transition time and a few whole-room resets.

---

## 2) Instructor Setup Checklist

- Open a clean file called `hour22_drill_demo.py`.
- Prepare either four starter files or one document with four clearly labeled station sections.
- Put the station titles on screen before class begins:
  1. Filter numbers > 10
  2. Unique emails
  3. Word frequency
  4. Coordinates unpacking
- Have a visible timer ready.
- Prepare one tiny test example for each station so you can model the testing habit.
- Decide whether learners will rotate physically, scroll through one worksheet, or move between files. Keep the logistics simple.
- Be ready to normalize partial completion. The runbook target is at least **three of four** stations completed.

**Say:** "This hour is about repetition with purpose. You do not need perfect code on the first try. You do need to choose a sensible structure, write the smallest working version you can, and test before you trust your result."

---

## 3) Opening Script: Why a Drill Circuit Matters (~5 minutes)

### 3.1 Reconnect to Hour 21

**Say:**
"In Hour 21, we focused on judgment. We asked, ‘Which structure fits this task best?’ That was important because design choices affect everything that comes next.

Now we need fluency. It is one thing to say, ‘A set is good for uniqueness.’ It is another thing to open a file, write the code, test it, and get the right result in a few minutes."

### 3.2 Normalize the format

**Say:**
"The point of a drill circuit is not to create stress. The point is to create useful repetition.

You are going to see patterns again and again until they start to feel familiar:
- filter with a list
- remove duplicates with a set
- count with a dictionary
- unpack fixed records with tuples

When those patterns become familiar, you stop guessing as much."

### 3.3 The work mindset for the hour

**Say:**
"Here is the mindset I want:

- Solve the actual prompt in front of you.
- Use the clearest structure, not the fanciest one.
- Test with tiny examples before polishing output.
- If you get stuck, simplify.
- If you finish early, improve formatting or add a small extension.

The goal is steady confidence, not racing."

---

## 4) Explain the Circuit Format Clearly

### 4.1 How the rotations work

**Say:**
"You will work through four short stations. You can do them in order. If you finish a station, move on. If you get stuck for more than two minutes, ask one focused question, test a smaller example, or move to the next station and come back later.

Your success target is to complete at least **three of the four** stations. If you complete all four, excellent. If you complete three cleanly and can explain your choices, that is also strong work."

### 4.2 What counts as ‘done’ at a station

**Say:**
"At each station, I am looking for three things:

1. The code runs.
2. The output matches the prompt.
3. You can explain why the chosen structure fits the task.

Fast code that you cannot explain is not the goal. Clear code that works and makes sense is more valuable."

### 4.3 Testing habit reminder

**Say:**
"Before a station feels finished, test with a tiny example.

- two or three numbers, not fifty
- two emails with one duplicate, not a giant list
- three words with one repeat, not a paragraph
- two coordinate pairs, not a huge dataset

Small tests make bugs easier to spot and fix."

### 4.4 Normalize imperfect progress

**Say:**
"If one station goes badly, do not let it ruin the hour. In programming, you do not need every attempt to be smooth. You need to keep moving, keep testing, and keep learning from the mistakes."

---

## 5) Quick Demo: Model One Station from Start to Finish (~6 minutes)

### 5.1 Choose Station 1 for the demo

**Say:**
"I am going to model one station quickly so you can see the level of detail I expect. I am not trying to show off speed. I am trying to show a method."

### 5.2 Type the prompt

**Type:**

```python
numbers: list[int] = [4, 11, 9, 15, 22, 3, 10]
filtered: list[int] = []

for number in numbers:
    if number > 10:
        filtered.append(number)

print(filtered)
```

Run it.

### 5.3 Narrate the thinking process

**Say:**
"Notice the thinking:

- I saw an ordered sequence of numbers, so a list made sense.
- I needed to collect some numbers and skip others, so I created a second list.
- I used a simple loop and an `if` statement.
- Then I tested with a small example before calling it finished.

That is the exact rhythm I want you to use at every station."

### 5.4 Show what not to do

**Say:**
"What I do not want is staring at a blank file waiting for a perfect idea. Start small. Make the first working step obvious."

---

## 6) Station 1: Filter Numbers > 10 (List Pattern)

### 6.1 Station prompt

Display or read aloud:

### Station 1 — Filter Numbers > 10

You are given a list of numbers.

```python
numbers = [4, 11, 9, 15, 22, 3, 10, 18]
```

Tasks:
1. Create a new list containing only the numbers greater than 10.
2. Print the filtered list.
3. Print how many numbers made it into the filtered list.

### 6.2 Why this is a list task

**Say:**
"This is a list task because we are working with an ordered sequence, and we want to build another sequence from it. We are not removing duplicates. We are not doing lookup by key. We are filtering one ordered collection into another."

### 6.3 Suggested instructor guidance during work time

**Say:**
"If you are unsure how to begin, start with three lines:

- the original list
- an empty result list
- a `for` loop

Then add the `if` condition."

### 6.4 Completion criteria

```text
Completion criteria
```

- Program creates a second list with only values above 10.
- Output clearly shows the filtered values.
- Program also prints the count of filtered values using `len()`.

### 6.5 Hints if learners stall

**Say:**
"Ask yourself: which list am I looping through, and which list am I appending to? Those should not be confused."

**Say:**
"If your result is empty, check the `if` condition. If your program crashes, check indentation and colons first."

### 6.6 Common pitfalls

```text
Common pitfalls to watch for
```

- Appending to the original list instead of the result list
- Using `>= 10` when the prompt says greater than 10
- Forgetting the colon after `if number > 10`
- Printing the result before the loop finishes and misreading partial output

### 6.7 Optional extension

```text
Optional extensions (stay in Basics scope)
```

- Print the numbers one per line with a label such as `Accepted:`.
- Also create a second list of numbers `<= 10` and print both groups.

---

## 7) Station 2: Unique Emails (Set Pattern)

### 7.1 Station prompt

### Station 2 — Unique Emails

You are given a list of email addresses with duplicates.

```python
emails = [
    "ana@example.com",
    "ben@example.com",
    "ana@example.com",
    "chris@example.com",
    "ben@example.com",
    "dana@example.com",
]
```

Tasks:
1. Convert the list into a set of unique email addresses.
2. Print the unique emails.
3. Print the original count and the unique count.
4. Explain in one comment why a set fits this task.

### 7.2 Why this is a set task

**Say:**
"This station is built around the central strength of sets: uniqueness. If the problem says duplicates should disappear, that is your clue."

### 7.3 Read-aloud guidance

**Say:**
"Remember that a set is unordered. If the printed order looks different from the original list, that is normal. Do not waste time trying to force the set to print in the same order unless the prompt specifically requires that."

### 7.4 Completion criteria

```text
Completion criteria
```

- Learner creates a set from the list successfully.
- Program prints the unique collection and both counts.
- Comment explains that the set removes duplicates automatically.

### 7.5 Hints

**Say:**
"The built-in `set()` constructor is your friend here. You already know this pattern from Session 5."

**Say:**
"If you want the counts, think `len(emails)` and `len(unique_emails)`."

### 7.6 Common pitfalls

```text
Common pitfalls to watch for
```

- Creating `{}` and accidentally making an empty dictionary instead of a set
- Expecting the set to preserve the original order
- Forgetting that printing a set directly is acceptable for this station
- Trying to use `append()` on a set instead of `add()` if building it manually

### 7.7 Optional extension

```text
Optional extensions (stay in Basics scope)
```

- Ask the user for one more email and report whether it is already present using `in`.
- Convert the set to a sorted list for prettier display if learners already know `sorted()`.

---

## 8) Station 3: Word Frequency (Dictionary Pattern)

### 8.1 Station prompt

### Station 3 — Word Frequency

You are given a short list of words.

```python
words = ["red", "blue", "red", "green", "blue", "red"]
```

Tasks:
1. Build a dictionary that counts how many times each word appears.
2. Print the dictionary.
3. Print each word and count on its own line.
4. Add a short comment explaining why a dictionary is a better fit than a list for this task.

### 8.2 Why this is a dictionary task

**Say:**
"This is the counting pattern from Session 5. The question is not just what words we have, but how many times each one appears. That naturally suggests a mapping from word to count. That is a dictionary."

### 8.3 Remind the core counting pattern

**Say:**
"If learners need a nudge, remind them of the essential line:

`counts[word] = counts.get(word, 0) + 1`

That line says: if the word is not in the dictionary yet, start from 0. Then add 1. If it is already there, take the existing count and add 1."

### 8.4 Completion criteria

```text
Completion criteria
```

- Program builds a correct frequency dictionary.
- Output includes at least one loop through `items()` to print each word with its count.
- Learner explanation mentions key-value mapping or lookup by word.

### 8.5 Hints

**Say:**
"Start with an empty dictionary. Then loop through the words. Then update the count one word at a time."

**Say:**
"If your counts look wrong, test with the smallest possible list like `['red', 'red']` and trace the dictionary after each step."

### 8.6 Common pitfalls

```text
Common pitfalls to watch for
```

- Using `counts[word] += 1` before the key exists, causing a `KeyError`
- Forgetting to use `.items()` when printing both the word and count together
- Replacing the count with `1` every time instead of adding to it
- Not testing with a tiny list before assuming the logic is correct

### 8.7 Optional extension

```text
Optional extensions (stay in Basics scope)
```

- Ask the user for a color word and print its count using `get()`.
- Print the counts in sorted word order using `for word in sorted(counts.keys()):` if appropriate for your learners.

---

## 9) Station 4: Coordinates Unpacking (Tuple Pattern)

### 9.1 Station prompt

### Station 4 — Coordinates Unpacking

You are given a list of coordinate pairs.

```python
points = [(2, 3), (5, 8), (1, 4), (7, 2)]
```

Tasks:
1. Loop through the points.
2. Unpack each tuple into `x` and `y`.
3. Print each point in a sentence like `Point at x=2, y=3`.
4. Track the largest `x` value and print it at the end.

### 9.2 Why this is a tuple task

**Say:**
"Each point is one fixed record with two parts: x and y. That is exactly the kind of small, fixed grouping tuples were made for."

### 9.3 Guidance for the loop

**Say:**
"The key pattern here is unpacking right in the loop header:

`for x, y in points:`

That works because each item in `points` is a tuple with exactly two values."

### 9.4 Completion criteria

```text
Completion criteria
```

- Learner loops through all points successfully.
- Each tuple is unpacked into `x` and `y`.
- Program prints a sentence for each point.
- Program reports the largest `x` value correctly.

### 9.5 Hints

**Say:**
"If you are not sure how to find the largest x value, start with `largest_x = None`, then compare each new `x` as you loop."

**Say:**
"If unpacking fails, check that every item in the list is actually a two-value tuple."

### 9.6 Common pitfalls

```text
Common pitfalls to watch for
```

- Writing `for point in points:` and then forgetting to unpack the tuple
- Comparing the entire tuple instead of the `x` value when tracking the largest x
- Initializing `largest_x` in the wrong place so it resets every loop
- Confusing the role of x and y in the output sentence

### 9.7 Optional extension

```text
Optional extensions (stay in Basics scope)
```

- Also find the largest `y` value.
- Count how many points have `x > y`.

---

## 10) Whole-Room Time Checks During the Circuit

### 10.1 First time check (~15 minutes into work time)

**Say:**
"Quick room check: by now you should have at least one station finished or almost finished. If you are stuck on syntax, simplify and test a smaller example. If you are stuck on the structure choice, look back at the station title — it is giving you a clue."

### 10.2 Second time check (~30 minutes into work time)

**Say:**
"At this point, aim to have two stations complete and be moving into your third. Remember, three clean stations is a strong result. Do not let perfection slow down progress."

### 10.3 Final time check (~40 minutes into work time)

**Say:**
"You have a few more minutes. If you are mid-station, focus on getting the minimum working version done. Fancy formatting can wait."

---

## 11) Share-Out and Walkthroughs (~8 minutes)

### 11.1 Transition back to whole group

**Say:**
"Let’s come back together. I want to hear a few solutions, but I especially want to hear the thinking behind them."

### 11.2 Suggested share-out structure

Ask for one volunteer per pattern if possible:
- one learner shares list filtering
- one learner shares set uniqueness
- one learner shares dictionary counting
- one learner shares tuple unpacking

### 11.3 Suggested instructor prompts

**Ask learners:**
- "Why was a list the right fit for Station 1?"
- "What did the set do automatically in Station 2?"
- "Why is a dictionary a natural match for word frequency?"
- "What did tuple unpacking make easier to read in Station 4?"

### 11.4 Model a strong verbal explanation

**Say:**
"A strong explanation sounds like this: ‘I used a dictionary in Station 3 because each word needed to map to a count. The dictionary let me look up the current count for a word and update it as I looped.’

That kind of explanation shows structure awareness, not just code copying."

### 11.5 Normalize mistakes as useful feedback

**Say:**
"I also want to normalize something important: if you made a mistake today and then corrected it, that is progress. Some of the best learning in programming comes from noticing, ‘Oh, I used the wrong structure there,’ or ‘I forgot to test a tiny case.’"

---

## 12) Recap + Exit Ticket (~5 minutes)

### 12.1 Recap the four patterns

**Say:**
"Today’s hour was about making four important patterns feel more natural:

- list for filtering an ordered sequence
- set for uniqueness
- dictionary for counting or lookup
- tuple for fixed records and unpacking

These are not random exercises. They are the building blocks of many real Python programs."

### 12.2 Exit ticket

```text
Quick check / exit ticket
```

Ask learners to answer one or more of these:

1. Which station felt easiest, and why?
2. Which station felt most useful for real work, and why?
3. Name one bug you hit and how you fixed it.
4. Name one data-structure pattern you think you will use again soon.

### 12.3 Closing bridge to Hour 23

**Say:**
"In the next hour, we move from short drills to a more coherent mini-project. The patterns from today will come back, but now they will work together in one in-memory tracker program."

---

## 13) Detailed Share-Out Walkthrough Guide

### 13.1 Why the share-out matters

**Say:**
"Do not rush the share-out just because the station work felt busy. The share-out is where learners convert activity into understanding. They need to hear the pattern named clearly after they have struggled with it a little."

### 13.2 Suggested sequence for the walkthrough

Use this order if time allows:

1. Station 1 — list filtering  
2. Station 2 — set uniqueness  
3. Station 4 — tuple unpacking  
4. Station 3 — dictionary counting

**Say:**
"I like ending with the dictionary station because it is often the richest one conceptually. It reminds learners that dictionaries are not only for storing fixed information like contacts or inventory. They are also for *building information* as a program runs."

### 13.3 Station 1 walkthrough talking points

**Say:**
"In Station 1, the important idea was that we started with one ordered sequence and built another ordered sequence from it. We did not need uniqueness. We did not need key lookup. We simply needed to test each number and decide whether it belonged in the result.

That is why a list was the natural fit. If a learner used a set here, the program might still contain numbers above 10, but it would lose the original order and might remove duplicates that were actually meaningful. So the structure choice really mattered."

Ask:
- "What line actually decides whether a number belongs in the new list?"
- "Why do we append to `filtered` instead of changing `numbers` directly?"

### 13.4 Station 2 walkthrough talking points

**Say:**
"In Station 2, the crucial shift was from storing every email to storing each email only once. That is the exact moment where a set becomes powerful. A set enforces the rule of uniqueness for us. We do not have to write extra code to remove duplicates one by one."

Ask:
- "What information was important here: order, or uniqueness?"
- "What happened automatically when the duplicate emails were converted into a set?"

Then reinforce:

**Say:**
"Remember that a set being unordered is not a bug. It is part of the tradeoff. When order matters, choose something else. When uniqueness matters more, a set is often the cleaner tool."

### 13.5 Station 3 walkthrough talking points

**Say:**
"Station 3 matters because it takes learners beyond storing data and into *accumulating* data. A word-frequency dictionary starts empty and grows as the loop runs. The keys are words. The values are counts. That is a beautiful example of matching a structure to the shape of the problem."

Write or restate the central line:

```python
counts[word] = counts.get(word, 0) + 1
```

**Say:**
"This one line handles both cases:
- if the word is new, start at 0 and add 1
- if the word is already present, take the current count and add 1

That is one of the most reusable patterns beginners learn in the first half of a Python course."

Ask:
- "Why does this use a dictionary instead of a list?"
- "What would go wrong with `counts[word] += 1` if the key is not there yet?"

### 13.6 Station 4 walkthrough talking points

**Say:**
"Station 4 reminded us that tuples are not just a weird alternative to lists. They are useful when one item naturally has a fixed number of parts. Each point had exactly two values, x and y, and unpacking let us work with those values clearly."

Ask:
- "What made the tuple a good fit for one point?"
- "What made the outer structure a list?"

Then reinforce:

**Say:**
"That combination — a list of tuples — is worth remembering. It shows how structures can work together: the list stores many records, and the tuple stores the fixed parts of one record."

### 13.7 End the share-out by naming the patterns again

**Say:**
"I want to name the four patterns one more time because repetition matters:

- filter with a list
- keep unique values in a set
- count with a dictionary
- unpack fixed records from tuples

If those four patterns start to feel familiar, learners are building real fluency."

---

## 14) Troubleshooting Playbook During the Circuit

### 14.1 If learners freeze at the blank page

**Say:**
"Write the data first. Then write the empty result structure if needed. Then write the loop. Then write the condition. That order reduces stress because it turns one big task into a small sequence of obvious steps."

### 14.2 If learners choose the wrong structure

**Say:**
"Do not immediately say, 'That is wrong.' Instead ask a question that lets them notice the mismatch:

- Do duplicates matter here?
- Do you care about order here?
- Are you looking things up by key here?
- Is this one fixed record or many items?"

This preserves learner ownership while still guiding them toward a better fit.

### 14.3 If learners have syntax errors

**Say:**
"Read the error calmly. Then check the beginner basics first:

- missing colon
- indentation mismatch
- missing comma
- unmatched quote
- variable name typo

Many drill-circuit errors are not deep logic issues. They are fast syntax issues caused by rushing."

### 14.4 If learners have logic errors

**Say:**
"Shrink the test case. If the list has eight numbers, try two. If the words list has six items, try two repeated words. Tiny tests make the logic visible."

### 14.5 If learners finish early

**Say:**
"Do not let early finishers drift. Give them one of these productive next steps:

- improve output formatting
- add a tiny extension
- help explain a pattern to a neighbor without taking over the keyboard
- write one comment per station explaining why the structure fit"

### 14.6 If learners finish only two stations

**Say:**
"That is still useful information. Ask which pattern slowed them down and why. The goal is not to shame partial completion. The goal is to identify where the next practice should go."

### 14.7 Instructor wrap-up language

**Say:**
"This hour was meant to create productive repetition, not perfection. If one or two patterns still feel shaky, that is normal. What matters is that learners can now name the pattern, recognize it in a prompt, and get started with less hesitation than before."

---

## 15) Appendix: Instructor Reference for Fast Support During Stations

### 13.1 Fast coaching questions

Keep these ready while circulating:

- "What is the main job of this collection?"
- "Do you need order here?"
- "Do duplicates matter here?"
- "Would a key-value mapping help here?"
- "Can you test with a smaller example?"

### 13.2 Minimal pattern reminders you can put on the board

```python
# List filtering
result = []
for item in items:
    if condition:
        result.append(item)

# Set uniqueness
unique_items = set(items)

# Dictionary counting
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

# Tuple unpacking
for x, y in points:
    print(x, y)
```

**Say:**
"These are not magic spells to memorize. They are reusable patterns. The more you practice them, the more natural they become."
