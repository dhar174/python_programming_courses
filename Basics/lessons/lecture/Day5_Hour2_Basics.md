# Day 5, Hour 2: Sets — Uniqueness + Membership (Course Hour 18)
**Python Programming Basics – Session 5**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 5, Course Hour 18 – Sets: uniqueness + membership  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is a detailed read-aloud teaching guide for Course Hour 18. The entire hour focuses on sets: what they are, why uniqueness is built in, how to use them for fast membership checks, and how a few key operations (union, intersection, difference) solve real problems. Stay firmly within Basics scope — do not introduce frozensets, set comprehensions, or the `collections` module here. The key outcomes are (1) using `set()` to strip duplicates from a list, (2) checking membership with `in`, (3) building intuition for when a set beats a list, and (4) understanding why sets are unordered and how to work with that. The lab ties everything together in a practical "Unique Visitors" program that learners build step by step. Every "Say:" block is written to be read nearly verbatim; adapt phrasing to your natural voice as needed, but do not skip or abbreviate the conceptual explanations.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Create a set using a set literal and using the `set()` constructor to convert a list, and explain in plain language what makes a set different from a list or tuple.
2. Add items to a set with `add()`, remove items safely with `discard()`, and describe why sets never store duplicate values.
3. Check whether a value exists in a set using the `in` operator and explain why this is conceptually faster than checking a list.
4. Use union (`|`), intersection (`&`), and difference (`-`) to combine or compare two sets, and give a real example of when each operation is useful.
5. Build the Unique Visitors program: collect ten names from the user, store them in a list, convert to a set, and report the unique count — then explain why the duplicate names disappeared."

---

## 1) Agenda + Timing

- **0:00–0:05** Reconnect to Hour 17 (tuples); set up the problem sets solve
- **0:05–0:14** Core concept: what a set is, analogy, literal syntax, `set()` constructor
- **0:14–0:22** Adding, removing, and clearing: `add()`, `discard()`, `remove()`, `pop()`, `clear()`
- **0:22–0:28** Membership checks: `in` with sets vs lists, conceptual speed difference
- **0:28–0:34** Set operations: union, intersection, difference with classroom examples
- **0:34–0:39** Sets are unordered — demo and `sorted()` as the display fix
- **0:39–0:43** Live demo: list of names → set (typed live in class)
- **0:43–0:58** Guided lab: Unique Visitors
- **0:58–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist

- Open two clean files before class: `hour18_sets_demo.py` for the live demo, and `hour18_lab_visitors.py` with blank comment placeholders as a starter for learners.
- Have a Python REPL terminal ready for quick interactive experiments in Sections 4 and 5.
- Prepare to type the exact "wrong" code first (using `{}` for an empty set) — this is a planned pitfall demonstration, not an accident.
- Confirm learners have completed Hour 17 (tuples) and Hour 15–16 (lists deep dive). This hour builds directly on list knowledge.
- Have a whiteboard or screen annotation tool ready to sketch the "bag of unique tags" analogy.

**Say:** "Get your editor open and a fresh empty file ready. The best way to learn sets is to type the code yourself and watch what happens. This hour will be very hands-on."

---

## 3) Opening Script: Reconnect to Earlier Learning (~5 minutes)

### 3.1 Quick recap from Hour 17

**Say:**
"Last hour we learned about tuples. We found out that a tuple is like a locked list — it holds an ordered sequence of values that cannot be changed after creation. We used tuples for (x, y) coordinates and saw how unpacking lets us pull those values into named variables cleanly.

Tuples are the right tool when you have a small, fixed group of related values that belong together and should never change.

Now, today's question is different. Today we are going to think about a situation that comes up constantly in real programs: what do you do when you need a collection where every item is unique — where duplicates simply should not exist?"

### 3.2 The everyday problem of duplicates

**Say:**
"Let me paint a picture. Imagine you are running a conference and you have a sign-in sheet. Over the course of the day, people walk up and write their name. The sheet looks like this:

```
Alice
Bob
Alice
Carol
Bob
Bob
David
Alice
```

At the end of the day, someone asks: 'How many unique attendees did we have today?'

You know the answer is four — Alice, Bob, Carol, and David — but to get that answer from the raw list you have to scan through and mentally filter out the repeats.

Now imagine this is not eight names but eight thousand names. Or eighty thousand. Filtering duplicates by hand — or even by writing a loop that checks every entry against every other entry — gets expensive fast.

Python has a data structure built precisely for this problem. It is called a **set**, and its defining property is simple: a set can only ever contain each value once. No duplicates. Not because you have to prevent them manually — because the structure itself refuses to store them."

### 3.3 Transition and roadmap

**Say:**
"Here is what we are going to cover this hour. First, we will understand what a set is and how to create one. Then we will look at how to add and remove items. After that we will explore why sets are so good at answering the question 'is this value in here?' — the membership check. We will also look at three simple operations — union, intersection, and difference — that let you combine or compare two sets in ways that are very useful in real programs. And we will finish with a hands-on lab where you build a Unique Visitors program from scratch.

Let's start."

---

## 4) Concept: What Is a Set?

### 4.1 The bag-of-unique-tags analogy

**Say:**
"Think of a set like a bag of tags. Each tag has a value written on it. Here is the key rule: you can only have one tag with any given value in the bag. If you try to drop in a tag that says 'Alice' and there is already a tag in the bag that says 'Alice', the bag rejects it. You end up with exactly one 'Alice' tag, no matter how many times you try to add it.

Now compare that to a list, which is more like a queue of numbered tickets. You can have as many tickets with the same number as you like — the list just keeps adding them to the end. Lists care about order and allow duplicates. Sets do not care about order and refuse duplicates.

That is the core trade-off in one sentence: **lists are ordered and allow duplicates; sets are unordered and enforce uniqueness.**"

### 4.2 Set literal syntax

**Say:**
"Let's look at the syntax. A set literal uses curly braces, just like this:"

```python
# A set literal — curly braces with comma-separated values
fruits: set = {"apple", "banana", "cherry"}
print(fruits)
```

**Say:**
"Type that into your REPL and run it. Notice two things: first, there are no duplicates (we only put one of each in). Second, when Python prints the set, the order might be different from the order you typed the items in. We will talk about why that is in a moment — it is one of the most important things to understand about sets.

Now let me show you what happens when you deliberately add a duplicate right in the literal:"

```python
# Python silently keeps only one copy
colours: set = {"red", "blue", "red", "green", "blue"}
print(colours)  # Only 3 items: {'red', 'blue', 'green'}
print(len(colours))  # 3
```

**Say:**
"Try that. Python does not raise an error. It does not warn you. It just quietly keeps one copy of each value and discards the rest. That is sets doing their job automatically."

### 4.3 The `set()` constructor — converting a list to a set

**Say:**
"The most common way to use a set in practice is not to write a set literal. It is to start with a list — which you already know how to build — and convert it.

That is where the `set()` constructor comes in."

```python
# Start with a list that has duplicates
names_list: list[str] = ["Alice", "Bob", "Alice", "Carol", "Bob", "Bob", "David"]

# Convert to a set — duplicates vanish automatically
unique_names: set[str] = set(names_list)

print(unique_names)        # {'Alice', 'Bob', 'Carol', 'David'} (order may vary)
print(len(unique_names))   # 4
```

**Say:**
"Let me read that code out loud so we absorb what is happening.

We start with `names_list` — a regular Python list with seven items, including two Alices, three Bobs, and a Carol and a David.

We call `set(names_list)`, passing the whole list in. Python reads through every item, and for each one, if it has not seen that value before, it keeps it. If it has seen it before, it throws it away. The result is a new set with four items: one Alice, one Bob, one Carol, one David.

That is the duplicate-removal pattern you will use over and over again in real programs. Build a list in whatever way makes sense — from user input, from a file, from an API — then call `set()` on it to get the unique values."

### 4.4 Important distinction: `{}` is NOT an empty set

**Say:**
"Before we go further, I want to flag a trap that catches almost every Python beginner at some point. Let me show you two things that look similar but are completely different:"

```python
# This creates an empty DICTIONARY, not an empty set
empty_dict = {}
print(type(empty_dict))  # <class 'dict'>

# This creates an empty SET — use set() with no arguments
empty_set = set()
print(type(empty_set))   # <class 'set'>
```

**Say:**
"In Python, a pair of empty curly braces `{}` creates an empty *dictionary*, not an empty set. Dictionaries also use curly braces, and when Python sees `{}` it defaults to dictionary. To get an empty set you must write `set()` explicitly.

This is one of the most common beginner mistakes with sets. We will come back to it in the pitfalls section, but I want to plant that flag in your memory right now: **empty set = `set()`, not `{}`**."

### 4.5 Sets hold hashable values

**Say:**
"One more rule before we move on. Sets can only store values that Python considers *hashable* — which in practical terms means values that are immutable: strings, numbers, tuples of immutable values, booleans.

Lists cannot go inside sets because lists can be changed (they are mutable). Dictionaries cannot go inside sets for the same reason. If you try, Python will raise a `TypeError` with the message 'unhashable type: list'.

At the Basics level, this mostly means: sets of strings, sets of numbers, and sets of tuples are fine. Sets of lists are not. You do not need to understand *why* hashability works the way it does right now — just know the practical rule."

```python
# Fine — strings, ints, tuples are hashable
valid_set: set = {"hello", 42, (1, 2)}

# This will raise TypeError
try:
    invalid_set = {[1, 2, 3]}  # list inside a set
except TypeError as e:
    print(f"Error: {e}")  # Error: unhashable type: 'list'
```

---

## 5) Adding and Removing Items

### 5.1 The `add()` method

**Say:**
"Sets are mutable — you can add and remove items after creation. But the methods look a little different from list methods because the rules are different.

To add a single item to an existing set, use `add()`:"

```python
visitors: set[str] = {"Alice", "Bob"}
print(visitors)  # {'Alice', 'Bob'}

# Add a new name
visitors.add("Carol")
print(visitors)  # {'Alice', 'Bob', 'Carol'}

# Try to add a name that already exists — nothing changes
visitors.add("Alice")
print(visitors)  # Still {'Alice', 'Bob', 'Carol'} — no duplicate
print(len(visitors))  # 3
```

**Say:**
"Notice: adding a value that is already in the set does nothing. No error, no warning, no second copy. The set stays the same. This is the uniqueness guarantee working for you — you never need to check 'is this already in here?' before calling `add()`. The set checks for you."

### 5.2 The `remove()` and `discard()` methods

**Say:**
"To remove an item, you have two options: `remove()` and `discard()`. They do the same thing when the item exists. They behave differently when the item does not."

```python
visitors: set[str] = {"Alice", "Bob", "Carol", "David"}

# remove() raises KeyError if the item is not found
visitors.remove("Carol")
print(visitors)  # {'Alice', 'Bob', 'David'}

try:
    visitors.remove("Zara")  # Zara is not in the set
except KeyError as e:
    print(f"KeyError: {e}")  # KeyError: 'Zara'

# discard() silently does nothing if the item is not found
visitors.discard("Zara")   # No error
visitors.discard("Bob")    # Bob IS here, so this works normally
print(visitors)  # {'Alice', 'David'}
```

**Say:**
"The rule of thumb is easy: if you *know* the item is in the set, use `remove()`. If you are not sure and you do not want an error if it is missing, use `discard()`. In most beginner programs, `discard()` is the safer default."

### 5.3 The `pop()` method

**Say:**
"`pop()` removes and returns *some* item from the set. The catch is that because sets are unordered, you have no control over which item gets removed. It is essentially random from your perspective."

```python
colours: set[str] = {"red", "green", "blue", "yellow"}
removed = colours.pop()  # Removes some item — we don't know which
print(f"Removed: {removed}")
print(f"Remaining: {colours}")
```

**Say:**
"You will rarely use `pop()` on a set in everyday code. It exists for cases where you need to process items one by one and do not care about order. For now, just know it is there."

### 5.4 The `clear()` method

**Say:**
"`clear()` removes every item from the set, leaving you with an empty set:"

```python
temp_set: set[str] = {"a", "b", "c"}
temp_set.clear()
print(temp_set)   # set()
print(len(temp_set))  # 0
```

**Say:**
"Notice that when Python prints an empty set, it shows `set()` rather than `{}`. That is consistent with what we said earlier — `{}` is always a dictionary in Python's display."

---

## 6) Membership Checks

### 6.1 Using `in` with a set

**Say:**
"One of the most valuable things about sets — maybe the most valuable — is how fast they answer the question 'is this value in here?'

The syntax is the same `in` keyword you already know from lists:"

```python
approved_users: set[str] = {"alice", "bob", "carol", "david", "eva"}

username = "carol"
if username in approved_users:
    print(f"Welcome, {username}!")
else:
    print("Access denied.")

username = "zara"
if username in approved_users:
    print(f"Welcome, {username}!")
else:
    print("Access denied.")  # This one prints
```

**Say:**
"Clean and readable. `username in approved_users` reads almost like English: 'is username in approved_users?' — yes or no."

### 6.2 Sets vs lists for membership — conceptual speed difference

**Say:**
"Here is where sets have a real advantage over lists for this kind of check, and I want you to understand *why* even if we are not going to run benchmarks today.

When you check `item in my_list`, Python starts at the beginning of the list and checks item one by one: 'Is it the first element? No. Is it the second? No...' and so on, until it either finds the item or reaches the end. If the item is at the end of a list with a million elements, Python checks a million elements.

When you check `item in my_set`, Python uses a mathematical trick called *hashing*. It computes a numeric fingerprint of your item and uses that fingerprint to jump almost directly to where the item would be stored — like looking up a word in a dictionary that has an alphabetical index versus scanning every single page. The check takes roughly the same time whether the set has five items or five million items.

The practical lesson: **if you are going to check membership many times and you do not need order or duplicates, use a set instead of a list.**

Let's see a side-by-side example that illustrates the idea:"

```python
# Same data — once as a list, once as a set
blocked_words_list: list[str] = ["spam", "scam", "fake", "fraud", "phishing"]
blocked_words_set: set[str] = {"spam", "scam", "fake", "fraud", "phishing"}

message_word = "fraud"

# Both work correctly — the difference is how Python searches internally
if message_word in blocked_words_list:
    print("List check: word is blocked.")

if message_word in blocked_words_set:
    print("Set check: word is blocked.")
```

**Say:**
"Both produce the same answer. The set check is conceptually faster for large collections — but for five items, you will never notice the difference. The point is to build the habit: when the collection is a lookup table and you do not care about order or duplicates, reach for a set."

---

## 7) Set Operations at a Conceptual Level

**Say:**
"Sets in mathematics have three fundamental operations that let you combine or compare two sets. Python implements all three with simple operators. You do not need to write any loops — Python does the work. Let me walk through each one."

### 7.1 Setup — two classroom rosters

**Say:**
"To make these concrete, let's use two class rosters as our example. Imagine you are coordinating two optional workshops at the conference:"

```python
# Students in the Python workshop
python_workshop: set[str] = {"Alice", "Bob", "Carol", "David", "Eva"}

# Students in the Data workshop
data_workshop: set[str] = {"Carol", "Eva", "Frank", "Grace", "David"}
```

### 7.2 Union (`|`) — everyone in either group

**Say:**
"The **union** of two sets gives you every item that appears in *either* set — or in both. Think of it as 'everyone who attended at least one workshop.' In Python, the union operator is the pipe character `|`:"

```python
# Union: all students in either workshop
all_students = python_workshop | data_workshop
print(all_students)
# {'Alice', 'Bob', 'Carol', 'David', 'Eva', 'Frank', 'Grace'}
```

**Say:**
"Notice Carol, Eva, and David attended both workshops, but they only appear once in the result — because it is a set. That is exactly right. We want a list of unique people who attended any workshop, not a count of attendances.

The union answers the question: 'Give me everyone.'"

### 7.3 Intersection (`&`) — only those in both groups

**Say:**
"The **intersection** of two sets gives you only the items that appear in *both* sets — the overlap. Think of it as 'students who attended both workshops.' In Python, the intersection operator is the ampersand `&`:"

```python
# Intersection: students who attended BOTH workshops
attended_both = python_workshop & data_workshop
print(attended_both)
# {'Carol', 'Eva', 'David'}
```

**Say:**
"Only Carol, Eva, and David are in both sets. Alice, Bob, Frank, and Grace each attended only one. The intersection filters down to just the overlap.

The intersection answers the question: 'Give me only those who are in all groups.'

Real-world use: imagine running a survey about two products. Who completed both surveys? Intersection. Who bought both products? Intersection. Who is in both your email list and your social-media followers? Intersection."

### 7.4 Difference (`-`) — in one but not the other

**Say:**
"The **difference** of two sets gives you the items that are in the first set but *not* in the second. Think of it as 'students who attended only the Python workshop, not the Data workshop.' In Python, the difference operator is the minus sign `-`:"

```python
# Difference: in Python workshop but NOT in data workshop
python_only = python_workshop - data_workshop
print(python_only)
# {'Alice', 'Bob'}

# You can flip it too: in data workshop but NOT in python workshop
data_only = data_workshop - python_workshop
print(data_only)
# {'Frank', 'Grace'}
```

**Say:**
"The order matters for difference — `A - B` is not the same as `B - A`. `python_workshop - data_workshop` gives you people in the Python workshop who skipped the Data workshop. Flip it, and you get Data workshop attendees who skipped Python.

Real-world use: you send a marketing email to list A. You also have list B of people who already unsubscribed. `A - B` is the safe list of people you can contact.

Or: you have a list of tasks to do today (set A) and a list of tasks already completed (set B). `A - B` is your remaining to-do list."

### 7.5 Quick summary table

**Say:**
"Here is a summary you can refer back to:"

```
Operation  | Operator | Plain English question
-----------|----------|-------------------------------------------
Union      |    |     | Who is in either (or both) groups?
Intersection|   &     | Who is in ALL groups (the overlap)?
Difference |    -     | Who is in the first group but NOT the second?
```

**Say:**
"You do not need to memorise these right now. Just know that they exist, that they use simple symbols, and that they let you compare collections without writing loops. We will practice them more in later sessions."

---

## 8) Sets Are Unordered — What That Means

### 8.1 Demonstrating the lack of order

**Say:**
"I mentioned several times that sets are unordered. Let me be precise about what that means and why it matters.

When you create a set, Python internally arranges the items using a hashing system that is optimised for fast lookups. That arrangement has nothing to do with the order you typed the items in, the order you added them, or alphabetical order. Every time you print a set, the items may appear in a completely different order.

Let me show you:"

```python
# Create the same set three different ways — notice the print order
tags: set[str] = {"python", "beginner", "coding", "tutorial", "free"}
print(tags)
# Output might be: {'free', 'beginner', 'coding', 'python', 'tutorial'}
# ...but it could be different on your machine or in a different run
```

**Say:**
"If you run this multiple times, or run it on different computers, the order of the printed output may vary. This is not a bug. It is the expected behaviour of sets.

The practical implication: **never write code that relies on the order of items in a set.** Do not assume the first item you added will be first when you iterate. Do not assume alphabetical order. Assume no order at all."

### 8.2 Why this catches beginners off guard

**Say:**
"Coming from lists, where the order is always preserved, this feels strange. Here are the two situations where it bites beginners most often:

**Situation 1 — Displaying results:** You convert a list to a set to remove duplicates, then print the set. The items come out in a random-looking order that confuses your users.

**Situation 2 — Testing:** You write a test that says 'the first element of my set should be X.' It passes on your machine, fails on someone else's. The test is wrong because it assumes order."

### 8.3 The `sorted()` fix for display

**Say:**
"The solution is simple: when you need to display the contents of a set in a readable, predictable order, wrap it in `sorted()`. This does not modify your set — it creates a temporary sorted list just for display purposes:"

```python
unique_tags: set[str] = {"python", "beginner", "coding", "tutorial", "free"}

# Do NOT do this for user-facing output:
print(unique_tags)           # Order unpredictable

# DO this instead:
print(sorted(unique_tags))   # ['beginner', 'coding', 'free', 'python', 'tutorial']
```

**Say:**
"`sorted()` returns a **list** in ascending order (alphabetical for strings, numerical for numbers). Your set is unchanged — `unique_tags` still contains the same five items, still unordered. But your display is clean and consistent.

This is the pattern you will use in the lab. Collect data into a set, do your set operations, then use `sorted()` whenever you need to show the results to a user."

---

## 9) Live Demo: List of Names → Set

**Say:**
"Let's pull everything together in a live demo. I am going to type this in `hour18_sets_demo.py` in my editor. Follow along and type the same code."

### 9.1 Set up the demo file

**Say:**
"Here is the scenario: we have a conference sign-in sheet. Multiple people signed in throughout the day, some more than once. We want to know how many unique attendees there were."

```python
# hour18_sets_demo.py
# Demo: List of names → set, removing duplicates

# Step 1: Raw sign-in data — names collected throughout the day
# (Simulating input that has duplicates)
sign_ins: list[str] = [
    "Alice",
    "Bob",
    "Alice",      # duplicate
    "Carol",
    "Bob",        # duplicate
    "David",
    "Bob",        # duplicate again
    "Alice",      # duplicate
    "Eva",
    "Carol",      # duplicate
]

print("--- Raw sign-in sheet ---")
print(f"Total sign-ins: {len(sign_ins)}")
print(sign_ins)
```

**Say:**
"Run that. You should see 10 total sign-ins in the list, with obvious duplicates."

### 9.2 Convert to a set

```python
# Step 2: Convert the list to a set — duplicates are removed automatically
unique_visitors: set[str] = set(sign_ins)

print("\n--- After converting to a set ---")
print(f"Unique attendees: {len(unique_visitors)}")
print(unique_visitors)
```

**Say:**
"Run this next section. You should see five unique attendees: Alice, Bob, Carol, David, Eva. The duplicates are gone. We went from 10 items in the list to 5 unique items in the set. And we did not write a single loop to check for duplicates — `set()` did all the work."

### 9.3 Display with sorted() and loop over the results

```python
# Step 3: Display neatly with sorted()
print("\n--- Unique attendees (sorted) ---")
for name in sorted(unique_visitors):
    print(f"  - {name}")

print(f"\nTotal unique attendees: {len(unique_visitors)}")
```

**Say:**
"Now we use `sorted()` to display the names in alphabetical order, and a loop to print each one with a dash. This looks professional and is easy to read.

Notice that we are looping over `sorted(unique_visitors)`, not over `unique_visitors` directly. We still have the set; we are just sorting a copy of it for display."

### 9.4 Bonus: membership check in the demo

```python
# Step 4: Check whether a specific person attended
person_to_check = "Alice"
if person_to_check in unique_visitors:
    print(f"\n{person_to_check} attended the conference.")
else:
    print(f"\n{person_to_check} did NOT attend the conference.")

# Check someone who didn't attend
person_to_check = "Zara"
if person_to_check in unique_visitors:
    print(f"{person_to_check} attended the conference.")
else:
    print(f"{person_to_check} did NOT attend the conference.")
```

**Say:**
"Clean and fast. `in` does the work. No loop, no manual scanning.

Here is the full picture of what we just built:

- We started with a raw list of 10 sign-ins, some duplicates.
- One call to `set()` gave us 5 unique visitors.
- `sorted()` let us display them in alphabetical order.
- `in` let us answer 'did this person attend?' instantly.

That is the complete pattern for uniqueness and membership in Python. Now let's build it from scratch in the lab."

---

## 10) Hands-on Lab: Unique Visitors

### 10.1 Lab overview

**Say:**
"This lab takes the demo pattern and makes it interactive. Instead of hard-coding names, you are going to ask the user to type in 10 names — some of them repeated on purpose — and then your program will figure out the unique count automatically.

Here are the requirements:

1. Ask the user to enter 10 names, one at a time (encourage them to type some names more than once to test uniqueness).
2. Store each name in a list as the user types it.
3. After all 10 names are collected, convert the list to a set.
4. Print the number of unique names.
5. Print the unique names themselves in sorted alphabetical order.
6. Explain in a comment *in your code* why duplicates disappear.

**Completion criteria:**
- The unique count is correct.
- The output shows sorted unique names.
- There is at least one comment that explains the uniqueness property of sets."

### 10.2 Starter hints

**Say:**
"Before you start coding, here are a few hints to guide your thinking:

**Hint 1:** You already know how to collect user input in a loop. Think: `for i in range(10):` with `input()` inside.

**Hint 2:** Use `append()` to add each name to the list as you go.

**Hint 3:** After the loop ends, convert the whole list with one call: `unique = set(name_list)`.

**Hint 4:** Use `len(unique)` for the count and `sorted(unique)` for the display loop.

**Stretch challenge:** After showing unique names, ask the user if they want to check whether a specific name was entered. If yes, read a name and use `in` to answer."

```python
# hour18_lab_visitors.py — STARTER TEMPLATE (fill in the blanks)

# Step 1: Create an empty list to hold all sign-ins
# ...

# Step 2: Collect 10 names from the user
# for i in range(10):
#     ...

# Step 3: Convert the list to a set (duplicates removed automatically)
# ...

# Step 4: Print the unique count
# ...

# Step 5: Print unique names in sorted order
# ...
```

**Say:**
"You have 15 minutes. Work at your own pace. If you finish early, attempt the stretch challenge. If you get stuck, raise your hand or re-read the hints — do not stare at a blank screen for more than two minutes."

*(Allow 15–18 minutes of lab time. Circulate and help. Look for: students who forgot to strip whitespace from `input()`, students who try to use `{}` for the empty container, students who loop over the set without `sorted()`.)*

### 10.3 Walkthrough solution

**Say:**
"Let's walk through the solution together. Even if you got it right, follow along — we will make sure the logic is tight and the code is clean."

```python
# hour18_lab_visitors.py — COMPLETE SOLUTION

# Step 1: Empty list to accumulate all sign-ins (duplicates included)
all_sign_ins: list[str] = []

print("=== Conference Visitor Sign-In ===")
print("Enter 10 names (repeats are fine — that is the point!):\n")

# Step 2: Collect 10 names from the user
for i in range(1, 11):
    name = input(f"  Visitor {i}: ").strip()  # .strip() removes accidental spaces
    all_sign_ins.append(name)

# Step 3: Convert to a set.
# Sets enforce uniqueness: if a name appears more than once in the list,
# the set will only keep one copy of it automatically.
unique_visitors: set[str] = set(all_sign_ins)

# Step 4: Report the unique count
print(f"\nTotal sign-ins recorded : {len(all_sign_ins)}")
print(f"Unique visitors today   : {len(unique_visitors)}")

# Step 5: Display unique names in sorted order
# sorted() returns a list in ascending order — does NOT change the set.
print("\nAttendee list (alphabetical):")
for name in sorted(unique_visitors):
    print(f"  - {name}")

# --- Stretch challenge ---
check = input("\nCheck if someone attended? (yes/no): ").strip().lower()
if check == "yes":
    lookup = input("Enter name to look up: ").strip()
    if lookup in unique_visitors:
        print(f"Yes — {lookup} attended today.")
    else:
        print(f"No — {lookup} was not recorded as a visitor.")
```

**Say:**
"Let's read through this together.

The list `all_sign_ins` is our raw data — everything the user types, duplicates and all. We use `append()` in the loop to build it up.

After the loop, `set(all_sign_ins)` does the uniqueness work in a single line. We store the result in `unique_visitors`.

We print `len(all_sign_ins)` for the raw count and `len(unique_visitors)` for the unique count. The difference tells the user how many duplicates there were.

Then we loop over `sorted(unique_visitors)` to display the names alphabetically — because sets are unordered and we want a predictable, readable output.

The stretch challenge uses `in` to check a name against the set. Notice that this is the membership check we practised earlier, applied in a real interactive context.

One detail worth noting: we call `.strip()` on every `input()`. This removes leading and trailing whitespace. Without it, a user who accidentally hits the spacebar before typing would create a string like `' Alice'`, which is different from `'Alice'`. The set would treat them as two different values. `.strip()` is a small habit that saves a lot of confusion."

### 10.4 Design discussion

**Say:**
"Let me ask a question to make sure you understand the design choices: why did we use a list first and then convert to a set, instead of adding directly to a set from the beginning?

Take a moment to think about that."

*(Pause 20–30 seconds.)*

**Say:**
"The answer is: we could have added directly to a set. Here is what that would look like:"

```python
# Alternative: build the set directly (also valid)
unique_visitors_v2: set[str] = set()
for i in range(1, 11):
    name = input(f"  Visitor {i}: ").strip()
    unique_visitors_v2.add(name)  # add() instead of append()
```

**Say:**
"This is shorter and perfectly correct. The reason we used a list first is that in real programs, you often collect data in a list before you know you need to de-duplicate it. You might read from a file, receive data from an API, or accumulate entries over time — all of which naturally produce a list. Then you convert to a set as a processing step.

Both patterns are valid. The list-then-convert pattern is more common and more general. The direct-to-set pattern is fine when you know from the start that uniqueness is all you care about."

---

## 11) Common Pitfalls

### 11.1 Expecting order to be preserved

**Say:**
"This is the big one and it is worth repeating. A set does not preserve the order of insertion. If you need to display items in order, always use `sorted()`. If you need the original insertion order, keep the list alongside the set — use each for what it is good at."

```python
# PITFALL: Don't rely on set iteration order
tags: set[str] = {"z", "a", "m", "b"}
for tag in tags:
    print(tag)  # Could print in any order — don't assume

# FIX: Use sorted() when order matters for output
for tag in sorted(tags):
    print(tag)  # 'a', 'b', 'm', 'z' — consistent alphabetical order
```

### 11.2 Using `{}` to create an empty set

**Say:**
"We covered this earlier but it is important enough to repeat as a named pitfall."

```python
# PITFALL: This creates an empty DICT, not an empty SET
wrong = {}
print(type(wrong))  # <class 'dict'>

# FIX: Use set() explicitly
correct = set()
print(type(correct))  # <class 'set'>
```

**Say:**
"If you ever get a confusing error like `'set' object does not support item assignment` or `AttributeError: 'dict' object has no attribute 'add'`, the first thing to check is whether you accidentally created a dict with `{}` instead of a set with `set()`."

### 11.3 Trying to modify a set while iterating over it

**Say:**
"Just like lists, you should not add or remove items from a set while you are looping over it. Python may raise a `RuntimeError` or produce unpredictable behaviour."

```python
numbers: set[int] = {1, 2, 3, 4, 5}

# PITFALL: Modifying a set during iteration
# for n in numbers:
#     if n % 2 == 0:
#         numbers.discard(n)  # RuntimeError: Set changed size during iteration

# FIX: Decide what to keep, then build a new set
new_numbers: set[int] = set()
for n in numbers:
    if n % 2 != 0:
        new_numbers.add(n)
numbers = new_numbers
print(numbers)  # {1, 3, 5}
```

**Say:**
"For beginners: the safe rule is to never modify a set inside the loop that is iterating over it. Instead, build a new set with the items you want to keep."

### 11.4 Putting unhashable items (like lists) into a set

**Say:**
"If you ever see `TypeError: unhashable type: 'list'`, it means you tried to add a list (or another mutable object) into a set. Sets can only contain immutable values. Convert the inner list to a tuple if you need to store it in a set."

```python
# PITFALL
# bad_set = {[1, 2], [3, 4]}  # TypeError: unhashable type: 'list'

# FIX: Use tuples instead of lists
good_set: set[tuple[int, int]] = {(1, 2), (3, 4)}
print(good_set)  # {(1, 2), (3, 4)}
```

---

## 12) Optional Extension: Sorted Display

**Say:**
"If you finished the lab early or want to extend your Unique Visitors program, here is a clean extension that demonstrates a useful pattern: keeping both the list and the set, and using them for different purposes."

```python
# Extension: work with both list and set simultaneously

all_sign_ins: list[str] = []
print("Enter 10 visitor names:")

for i in range(1, 11):
    name = input(f"  Name {i}: ").strip()
    all_sign_ins.append(name)

unique_visitors: set[str] = set(all_sign_ins)

# --- Use the LIST to count total sign-ins per person ---
print("\n=== Visitor Frequency ===")
for name in sorted(unique_visitors):
    count = all_sign_ins.count(name)  # list.count() counts occurrences
    print(f"  {name}: signed in {count} time(s)")

# --- Use the SET for the unique summary ---
print(f"\n=== Summary ===")
print(f"Total sign-ins  : {len(all_sign_ins)}")
print(f"Unique visitors : {len(unique_visitors)}")
print(f"Repeat sign-ins : {len(all_sign_ins) - len(unique_visitors)}")
```

**Say:**
"This extension shows something important about choosing the right data structure. The list is valuable for tasks that need the full record including duplicates — like counting how many times each person signed in. The set is valuable for tasks that need uniqueness — like reporting the unique headcount.

Using both together is completely normal. In professional code you will often see a list and a set created from the same data, each serving a different purpose."

**Say:**
"Notice `all_sign_ins.count(name)` — this is the list `count()` method, which counts how many times a value appears in the list. It loops through every element internally, so it is not fast for very large data, but for a lab program with 10 or even 100 names it is perfectly fine.

A second extension, staying in Basics scope: demonstrate all three set operations (union, intersection, difference) using two separate groups. Imagine morning visitors and afternoon visitors — the union tells you total unique attendance for the day, the intersection tells you who attended both sessions, the difference tells you who only came in the morning."

```python
# Further extension: morning vs afternoon visitors
morning: set[str] = {"Alice", "Bob", "Carol", "David"}
afternoon: set[str] = {"Carol", "David", "Eva", "Frank"}

all_day = morning | afternoon          # Union
both_sessions = morning & afternoon    # Intersection
morning_only = morning - afternoon     # Difference

print(f"Attended either session : {sorted(all_day)}")
print(f"Attended both sessions  : {sorted(both_sessions)}")
print(f"Morning only            : {sorted(morning_only)}")
```

---

## 13) Debrief, Recap, and Exit Ticket

### 13.1 Concept recap

**Say:**
"Let's take two minutes to consolidate what we covered this hour. I will summarise the key ideas and then give you an exit-ticket question to answer before you close your laptop.

**What is a set?**
A set is an unordered collection that automatically enforces uniqueness — every value can appear at most once. You create a set literal with curly braces containing values, or you convert an existing list with `set()`.

**How do you add and remove items?**
Use `add()` to add a single item (silently does nothing if the item already exists), `discard()` to remove an item without raising an error if it is absent, and `remove()` when you want an error on a missing item. Use `clear()` to empty the set.

**Why are sets good for membership checks?**
`value in my_set` is conceptually very fast regardless of how large the set is, because Python uses hashing to jump near-directly to the answer rather than scanning every element.

**What are the three main set operations?**
Union (`|`) — everyone in either group. Intersection (`&`) — only those in both groups. Difference (`-`) — in the first group but not the second.

**What does 'unordered' mean in practice?**
Never rely on the order items come out of a set. When you need to display or process items in a consistent order, wrap the set in `sorted()`.

**What is the empty-set trap?**
`{}` creates a dictionary, not a set. Always write `set()` for an empty set."

### 13.2 When to reach for a set vs a list vs a tuple

**Say:**
"Here is a decision guide to close out our discussion of all three collection types so far:

| Question | Best choice |
|---|---|
| Do I need to maintain insertion order? | List or Tuple |
| Can duplicates exist? | List or Tuple |
| Do I frequently check 'is X in here?' | Set |
| Do I need to remove duplicates from a list? | Convert to Set |
| Is the collection fixed / should never change? | Tuple |
| Do I need to combine two groups and check overlap? | Set operations |
| Do I need to track how many times each item occurs? | Keep the List |

You will not always get this perfect — that is fine. Learning to notice these trade-offs comes with practice."

### 13.3 Looking ahead

**Say:**
"Next hour — Hour 19 — we are going to meet the last and arguably most powerful built-in data structure: the dictionary. Dictionaries let you associate a *key* with a *value*, like a real-world dictionary that associates a word with its definition. We will see how dictionaries extend what we can do with data well beyond lists, tuples, and sets.

Before we get there, take 30 seconds to answer the exit ticket."

### 13.4 Exit ticket

**Say:**
"Here is your exit ticket. Answer this in your own words — out loud, in a note, or just think it through:

**When is a set better than a list?**

Think about at least two distinct situations. If you have a partner nearby, tell them your answer. If you are working solo, write two bullet points in a comment at the bottom of your lab file.

*(Pause 30–60 seconds for reflection.)*

I will share what I am looking for: a good answer mentions (1) when you want to remove or prevent duplicates, and (2) when you need to check membership many times and the collection is large. Bonus points if you mention set operations — union, intersection, difference — as a third reason to choose a set over a list."

### 13.5 Closing

**Say:**
"Great work today. You learned a new data structure — the set — and you saw how it solves the uniqueness problem elegantly with almost no code. You practised the most important patterns: creating a set from a list, checking membership with `in`, using union and intersection to combine groups, and displaying sorted output.

Save your files. In the next hour we will open up dictionaries and your toolkit for working with data in Python will be complete at the Basics level.

See you in a few minutes."

---

## Quick Reference Card

> Copy this to the top of your notes file, or keep it open as a reference during the lab.

```python
# ── CREATING SETS ──────────────────────────────────────────────
literal:   s = {"a", "b", "c"}         # set literal (no duplicates)
from list: s = set(my_list)             # convert list → set (removes duplicates)
empty:     s = set()                    # NEVER use {} for empty set (that's a dict)

# ── ADDING / REMOVING ──────────────────────────────────────────
s.add("x")         # add one item (no-op if already present)
s.discard("x")     # remove (silent if not found — safe default)
s.remove("x")      # remove (KeyError if not found)
s.pop()            # remove and return an arbitrary item
s.clear()          # empty the set

# ── MEMBERSHIP ─────────────────────────────────────────────────
"x" in s           # True if "x" is in the set
"x" not in s       # True if "x" is NOT in the set

# ── SET OPERATIONS ─────────────────────────────────────────────
a | b              # Union        — items in a OR b (or both)
a & b              # Intersection — items in BOTH a AND b
a - b              # Difference   — items in a but NOT in b

# ── DISPLAY IN ORDER ───────────────────────────────────────────
sorted(s)          # returns a sorted LIST — does not change s
for item in sorted(s):
    print(item)

# ── SIZE ───────────────────────────────────────────────────────
len(s)             # number of unique items in the set
```

---

*End of Day 5, Hour 2 — Course Hour 18: Sets — Uniqueness + Membership*
