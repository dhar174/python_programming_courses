# Day 5, Hour 2: Sets – Uniqueness + Membership (Course Hour 18)
**Python Programming Basics – Session 5**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 5, Course Hour 18 – Sets: uniqueness + membership  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is written as a detailed read-aloud teaching guide. This hour introduces sets as the third data structure of Session 5. The two key messages are: (1) sets automatically remove duplicates, and (2) sets support fast membership testing. Keep the scope tight. Teach set literals, `add()`, `in` membership checks, and `len()` for unique counts. Union and intersection should be mentioned at a conceptual level only—do not require learners to use operators (`|`, `&`) or methods (`union()`, `intersection()`) in the lab. Do not introduce `frozenset`, set comprehensions, `discard()`, `remove()`, or `difference()`. The lab is the Unique Visitors counter.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:
1. Create a set using curly braces and explain why it differs from a list.
2. Add items to a set with `add()` and observe that duplicates are silently ignored.
3. Check whether a value is present in a set using `in`.
4. Convert a list to a set to remove duplicates, and count the unique values with `len()`.
5. Explain why sets are unordered and what that means for display.
6. Use `sorted()` to produce an alphabetical display of set contents.
7. Build a Unique Visitors program that collects names, removes duplicates automatically, and reports the unique count.

This hour answers a question that comes up constantly in real programs: 'I have a collection of values, but some of them repeat. How many unique ones do I have?'"

---

## 1) Agenda + Timing (show slide / read quickly, ~2 minutes)

- **0:00–0:05** Recap of tuples, transition to sets, and motivation for uniqueness
- **0:05–0:15** What a set is, how to create one, and the automatic-uniqueness property
- **0:15–0:25** `add()`, membership with `in`, and converting a list to a set
- **0:25–0:32** Sets are unordered: what this means and how `sorted()` helps display
- **0:32–0:42** Union and intersection: conceptual overview only
- **0:42–0:57** Guided lab: Unique Visitors
- **0:57–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist (before class)

- Open a clean file such as `hour18_sets_demo.py`.
- Prepare a list of names with deliberate duplicates: `["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]`.
- Be ready to show the contrast between printing a list vs printing a set of the same values.
- Be ready to demonstrate that set order is not guaranteed (the order may vary between runs).
- Have a short word list prepared for an optional second demo: `["cat", "dog", "cat", "fish", "dog"]`.
- If some learners type slowly, have a starter file with comments only ready.

**Say:** "Please type with me today. The set operations are quick to learn, but seeing the output change in real time is what makes the concept click."

---

## 3) Opening Script: From Ordered to Unique (~5 minutes)

### 3.1 Recap the data structures covered so far

**Say:**
"Welcome back. In the last hour we covered tuples: ordered, immutable sequences that are great for fixed-size records like coordinates.

Before tuples, we spent all of Session 4 on lists: ordered, mutable collections that grow and shrink as needed.

Both of those structures care about order. Both allow duplicates. If I have `['cat', 'cat', 'cat']` in a list, Python keeps all three.

Today we learn a structure that cares about neither order nor duplicates. It cares only about one question: is this value present or not?"

### 3.2 Real-world motivation

**Say:**
"Here is a situation you will recognize.

Imagine a website has a log of every page visit. Over the course of a day, many visitors come and go. Some visitors arrive once. Some arrive five or ten times.

At the end of the day, the site owner wants to know: 'How many unique visitors did I have today?' Not how many visits—how many distinct people.

If you store every visit in a list, you have to count carefully and avoid duplicates in your logic. If you use a set, the problem nearly solves itself. A set will hold only one copy of each visitor's name, no matter how many times you try to add them.

That is the core use case for sets: uniqueness tracking."

### 3.3 A second motivating example

**Say:**
"Here is another one. You are building a word-count program. Before you count frequencies, you want to know: 'How many distinct words appear in this document?' A set gives you the answer immediately.

Or: you have a survey where people can choose their favorite programming languages, and many people give the same answers. A set collapses all the repeated answers into one entry per language.

The pattern is always the same: you have a pile of values, some repeated, and you want the unique ones. That is a set."

---

## 4) Core Concept: What a Set Is (~10 minutes)

### 4.1 Set syntax

**Say:**
"A set is created with curly braces and comma-separated values."

**Type:**

```python
languages = {"Python", "Java", "Python", "Go", "Java"}
print(languages)
print(type(languages))
```

Run it.

**Say:**
"Look at the output. Python only kept one copy of each value. 'Python' appeared twice in our literal, but the set contains it only once. Same with 'Java'.

`type(languages)` confirms we have a `set` object.

Notice something else: the order may not match the order I typed the values. When I run this on my machine, I might see `{'Go', 'Python', 'Java'}`. If I run it again, I might see a different order.

This is not a bug. Sets are intentionally unordered. Python uses an internal algorithm called hashing to store values efficiently, and the display order is a side effect of that algorithm, not something Python guarantees."

### 4.2 Empty set — the one exception to curly-brace syntax

**Say:**
"There is one important exception. If you want an empty set, you cannot use just `{}`. That creates an empty dictionary, which we will study in the next two hours."

**Type:**

```python
# This creates an empty DICTIONARY, not a set
not_a_set = {}
print(type(not_a_set))

# This creates an empty SET
real_empty_set = set()
print(type(real_empty_set))
```

Run it.

**Say:**
"This is a common source of confusion. Remember: `{}` is an empty dict. `set()` is an empty set.

For the lab today, you will start with a list and convert it to a set, so you will not need an empty set to begin with. But know this rule exists."

### 4.3 `add()` and the no-duplicate contract

**Type:**

```python
visitors = set()
visitors.add("Alice")
visitors.add("Bob")
visitors.add("Alice")  # duplicate
visitors.add("Charlie")
visitors.add("Bob")    # duplicate
print(visitors)
print(f"Unique visitors: {len(visitors)}")
```

Run it.

**Say:**
"We called `add()` five times but the set only has three elements. The duplicate calls for 'Alice' and 'Bob' were silently ignored.

This is the no-duplicate contract of a set. Calling `add()` with a value that already exists is not an error—Python simply does nothing. The value is already there.

`len(visitors)` returns `3`, the actual unique count, not the five times we called `add()`."

**Ask learners:**
"If I call `visitors.add('Alice')` ten more times, what does `len(visitors)` return?"

Pause for answers, then confirm: still `3`.

### 4.4 Membership testing with `in`

**Type:**

```python
visitors = {"Alice", "Bob", "Charlie"}

print("Alice" in visitors)
print("Dave" in visitors)
print("Dave" not in visitors)
```

Run it.

**Say:**
"Membership testing with `in` works the same way for sets as it does for lists and tuples. The syntax is identical.

The important difference is that for very large collections, `in` on a set is dramatically faster than `in` on a list. The reason is the internal hashing—Python can jump directly to where a value would be stored rather than checking each item one by one. You do not need to understand hashing deeply today. Just know: if you need fast membership checks on large data, a set is the right tool."

---

## 5) Converting a List to a Set (~7 minutes)

### 5.1 The conversion pattern

**Say:**
"In real programs, you often start with a list—because you collected data over time using `append()`—and then convert to a set to deduplicate."

**Type:**

```python
raw_names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice", "Dave"]
print(f"Raw list has {len(raw_names)} entries.")

unique_names = set(raw_names)
print(f"Unique names: {unique_names}")
print(f"Unique count: {len(unique_names)}")
```

Run it.

**Say:**
"The pattern is simple: `set(my_list)` converts a list into a set, removing all duplicates in one step.

The original list had seven entries with repeats. The set has four unique values.

This is one of the most useful one-liners in Python for data cleaning. You will use this in your own work."

### 5.2 `sorted()` for ordered display

**Say:**
"Since sets are unordered, printing a set directly gives unpredictable output—which is fine for a quick check, but not ideal if you want to show the user a clean alphabetical list.

The solution is `sorted()`. `sorted()` takes any iterable—including a set—and returns a list of the values in sorted order."

**Type:**

```python
unique_names = {"Dave", "Alice", "Charlie", "Bob"}
print("Raw set:", unique_names)
print("Sorted display:", sorted(unique_names))
```

Run it a couple of times.

**Say:**
"Every time we run `sorted(unique_names)`, we get the same alphabetical order. The underlying set itself is still unordered, but `sorted()` gives us a predictable view of the data for display purposes.

For the lab today, I recommend using `sorted()` when you print the unique visitor names, so the output is clear and consistent."

### 5.3 You cannot access a set by index

**Say:**
"Before we move to the lab, I want to flag one more characteristic that surprises learners."

**Type:**

```python
visitors = {"Alice", "Bob", "Charlie"}
# print(visitors[0])  # This will fail
```

Uncomment the second line and run.

**Say:**
"Sets do not support indexing. You cannot say `visitors[0]`. Because a set has no guaranteed order, the concept of 'the item at position 0' does not exist.

This is why we use `sorted()` to produce a list first if we need indexed access or display in a specific order.

For the lab, you only need to print unique values and count them. Neither of those requires indexing."

Re-comment the line.

---

## 6) Union and Intersection: Conceptual Overview (~5 minutes)

### 6.1 Set operations in plain English

**Say:**
"Sets come from mathematics, and they support mathematical set operations. I want to give you a conceptual overview of two common ones: union and intersection.

I am not asking you to use these in the lab today. But knowing they exist will save you time in real programs, and they may appear in later exercises."

### 6.2 Union

**Say:**
"Union answers: what values appear in either set, or in both?"

**Type:**

```python
set_a = {"Alice", "Bob", "Charlie"}
set_b = {"Charlie", "Dave", "Eve"}

union_result = set_a | set_b
print("Union:", union_result)
```

Run it.

**Say:**
"The union contains all values from both sets. 'Charlie' appears in both, but since sets have no duplicates, it appears only once in the result.

The `|` operator is the union operator for sets. There is also a `.union()` method that does the same thing."

### 6.3 Intersection

**Say:**
"Intersection answers: what values appear in both sets at the same time?"

**Type:**

```python
intersection_result = set_a & set_b
print("Intersection:", intersection_result)
```

Run it.

**Say:**
"Only 'Charlie' appears in both sets, so the intersection contains only 'Charlie'.

The `&` operator is the intersection operator.

Use case: imagine you have a set of users who logged in on Monday and a set of users who logged in on Tuesday. The intersection tells you which users logged in on both days.

Again, you will not be asked to use these operators in today's lab. Just know they exist and what they do."

---

## 7) Live Demo: Putting It Together (~5 minutes)

**Say:**
"Let me now run a clean end-to-end demo that mirrors the lab structure closely."

**Type:**

```python
# hour18_sets_demo.py

# Simulated log of visitor names with duplicates
raw_log = [
    "Alice", "Bob", "Alice",
    "Charlie", "Bob", "Alice",
    "Dave", "Charlie", "Eve",
    "Bob"
]

print(f"Total log entries: {len(raw_log)}")

# Convert to set for unique visitors
unique_visitors = set(raw_log)
print(f"Unique visitor count: {len(unique_visitors)}")

# Display in alphabetical order
print("Unique visitors:")
for name in sorted(unique_visitors):
    print(f"  - {name}")

# Membership check
query = "Alice"
if query in unique_visitors:
    print(f"\n'{query}' did visit today.")
else:
    print(f"\n'{query}' did not visit today.")
```

Run it.

**Say:**
"This is almost exactly the structure you will build in the lab. The main difference is that in the lab, the names will be entered by the user—not hard-coded in a list. The `for` loop and the set conversion pattern are identical."

---

## 8) Guided Lab: Unique Visitors (~12 minutes)

### 8.1 Introduce the lab

**Say:**
"Your task is to build the Unique Visitors program. Here are the requirements:

1. Use a loop to collect 10 names from the user, one at a time. Allow repeats—that is the point.
2. Store the names in a list as they are entered.
3. After collection, convert the list to a set to find the unique names.
4. Print the total number of unique names.
5. Print the unique names in alphabetical order."

### 8.2 Put the requirements on screen

```text
Lab: Unique Visitors
- Collect 10 names from the user (allow repeats)
- Store in a list
- Convert to a set
- Print unique count
- Print unique names in sorted order
```

### 8.3 Provide a beginner-friendly starter structure

**Type and leave on screen:**

```python
# hour18_lab_unique_visitors.py

# Step 1: collect names from the user
names_log = []

for i in range(1, 11):
    name = input(f"Enter visitor name {i}: ")
    names_log.append(name)

print(f"\nTotal entries collected: {len(names_log)}")

# Step 2: convert to set for uniqueness
unique_names = set(names_log)

# Step 3: report results
print(f"Unique visitors: {len(unique_names)}")
print("\nUnique names (alphabetical):")
for name in sorted(unique_names):
    print(f"  {name}")
```

### 8.4 Explain the starter

**Say:**
"This structure is clear and direct. `range(1, 11)` gives us numbers 1 through 10 for the prompt. We collect each name and append it to `names_log`. Then we convert to a set in one line. Then we display.

Your first goal is to get this running. Enter some names with deliberate repeats and confirm that the unique count is correct."

### 8.5 Optional extension

**Say:**
"If you finish the core lab early, here is an extension: after displaying the unique names, ask the user to check whether a specific name appears in the visitor log. Use `in` to check membership and print a friendly message either way."

**Type the extension hint:**

```python
# Optional extension: membership check
query_name = input("\nCheck if a visitor was present: ")
if query_name in unique_names:
    print(f"Yes, {query_name} was a visitor today.")
else:
    print(f"No, {query_name} was not in today's visitor log.")
```

**Say:**
"Notice that we check membership on `unique_names`, the set, not on `names_log`, the list. Either would work for correctness, but checking the set is more intentional: we care about unique presence, not visit count."

### 8.6 Optional second extension

**Say:**
"If you complete the first extension, try this: add a second prompt that asks for another batch of visitor names (say, five names for 'afternoon visitors'). Convert those to a second set. Then show the union—everyone who visited at any point—and the intersection—people who visited in both batches."

### 8.7 Instructor circulation prompts

As learners work, walk around and ask:
- "What is the type of `names_log`? What is the type of `unique_names`?"
- "How many entries did you add to `names_log`? How many unique values does the set have?"
- "If you call `add()` with a duplicate, what happens to `len()` of the set?"
- "Why do we use `sorted()` before printing? What would happen without it?"
- "What is the difference between the list and the set in terms of what they store?"

---

## 9) Common Pitfalls and How to Coach Through Them (~3 minutes)

### 9.1 Pitfall: expecting a set to preserve insertion order

**Symptom:** learner enters names in a specific order, prints the set, and the output order is different.

**Coach with these words:**
"Sets are unordered. Python does not guarantee the order you see. If you need a consistent display, use `sorted()`. That is not a weakness—it is just a characteristic you need to account for."

### 9.2 Pitfall: using `{}` for an empty set

**Symptom:** learner creates `s = {}` expecting a set, then gets a `TypeError` when trying to `add()`.

**Coach with these words:**
"Check `type(s)`. If it shows `dict`, you created a dictionary by accident. Use `s = set()` for an empty set."

### 9.3 Pitfall: trying to index a set

**Symptom:** learner writes `unique_names[0]` and gets a `TypeError`.

**Coach with these words:**
"Sets have no indexes. If you need the first item alphabetically, convert to a sorted list first: `sorted(unique_names)[0]`. But for the lab, you just need to loop and print."

### 9.4 Pitfall: case sensitivity

**Symptom:** learner enters "Alice" once and "alice" once; the set treats them as different values.

**Coach with these words:**
"Python's `in` operator is case-sensitive. 'Alice' and 'alice' are different strings. If you want case-insensitive uniqueness, you can normalize inputs with `.lower()` before adding them. Try it as an extension if you are interested."

---

## 10) Debrief and Share-Outs (~4 minutes)

### 10.1 Bring the class back together

**Say:**
"Let's compare what we built. The Unique Visitors program is simple, but it demonstrates a powerful and reusable pattern."

### 10.2 Ask targeted questions

Ask:
- "Who can explain in one sentence why the set has fewer items than the list?"
- "Who used `sorted()` for display? What difference did it make?"
- "Who discovered the empty-set trap while working?"
- "Who tried the membership check extension? What did it feel like compared to searching a list?"

### 10.3 Model a concise explanation

**Say:**
"A strong description of the Unique Visitors program: 'I collected 10 names in a list, allowing repeats. I converted the list to a set using `set()`, which automatically removed duplicates. I printed `len()` of the set for the unique count, and used `sorted()` before the loop so names appear in alphabetical order.'

That explanation shows you understood both what the code does and why each step was chosen."

---

## 11) Recap Script (~2 minutes)

**Say:**
"Today we added sets to our toolbox.

Here is what you should be able to say:
- A set stores unique values only. Duplicates are silently ignored when you call `add()` or when you convert a list.
- Sets are unordered. Do not rely on display order. Use `sorted()` if you need alphabetical output.
- `in` membership testing works on sets and is conceptually the same as `in` for lists.
- `set(my_list)` is the standard deduplication pattern.
- For an empty set, always use `set()`, never `{}`.

In the next hour, we introduce dictionaries: a structure that stores key-value pairs. Dictionaries will become one of your most-used Python tools."

---

## 12) Exit Ticket (~1 minute)

Ask learners to answer verbally, in chat, or on paper:

1. If I run `s = {"cat", "dog", "cat"}`, what does `len(s)` return?
2. How do I create an empty set without accidentally creating a dictionary?
3. Why does the order of items in a set change between runs?
4. What does `sorted(my_set)` return?

**Expected direction of answers:**
- `len(s)` returns `2`
- use `set()`, not `{}`
- sets are unordered; Python uses hashing for internal storage and does not preserve insertion order
- a sorted list (not a set) of the elements in ascending order

---

## 13) Instructor Notes for the Transition to Hour 19

**Say:**
"We now have three data structures in our toolkit: lists (ordered, mutable), tuples (ordered, immutable), and sets (unordered, unique values). Each one answers a different kind of question.

In the next hour, we meet dictionaries—the structure that answers: 'What is the value associated with this key?' Dictionaries power an enormous range of real programs: phone books, inventory systems, configuration files, HTTP request data, JSON parsing, and much more. It is the most flexible and widely used structure we will study in the Basics course."

---

## Appendix: Instructor Reinforcement Notes for Hour 18

### A) Board sketch for visual learners

Draw this on the board:

```text
List:  ["Alice", "Bob", "Alice"]   ← allows duplicates, has order
Set:   {"Alice", "Bob"}             ← no duplicates, no guaranteed order

set(["Alice", "Bob", "Alice"])  →  {"Alice", "Bob"}
```

Ask: "Which structure would you use for a vote count where you need only unique voters?"

### B) Short extra practice prompts

If you have extra minutes:

1. `s = {1, 2, 3, 2, 1}`. What does `len(s)` return?
2. `s.add(3)`. Now what does `len(s)` return?
3. Is `5 in {1, 3, 5, 7}` True or False?
4. If I want to print the contents of a set in reverse alphabetical order, what do I write?
5. What is the difference between `len(names_log)` and `len(set(names_log))`?

### C) Instructor language for gentle correction

- "Check whether your variable holds a set or a list. Use `type()` if you are not sure."
- "Read the error out loud. What is Python complaining about?"
- "If the output order surprised you, remember: sets are unordered. Wrap with `sorted()` for display."
- "Before calling `in`, ask yourself: are you checking the set or the original list? For this program, checking the set is the right choice."

### D) Coaching if learners ask about `remove()` and `discard()` on sets

If a learner asks about removing items from a set, say:

"Sets do have a `remove()` method and a `discard()` method—the difference is that `remove()` raises an error if the item is not present, while `discard()` silently does nothing. But for today's lab, we are not removing items from the set. We are only adding and reading. Save set removal for when you encounter a specific problem that needs it."

### E) Connecting sets to data-cleaning scenarios

If you want to deepen the debrief discussion, mention these real-world scenarios where the list-to-set conversion pattern is immediately useful:

**Scenario 1: De-duplicating email lists**
An email list for a newsletter has been built up over months from multiple sign-up forms. There are duplicates. Before sending a campaign, the sender converts the list to a set to get unique addresses only.

```python
all_signups = ["alice@example.com", "bob@example.com",
               "alice@example.com", "carol@example.com",
               "bob@example.com"]
unique_recipients = set(all_signups)
print(f"Sending to {len(unique_recipients)} unique addresses.")
```

**Scenario 2: Tracking which students have submitted**
A teacher receives assignment submissions throughout the day. Some students accidentally submit twice. The teacher uses a set to track who has submitted at all.

```python
submissions = ["Alice", "Bob", "Alice", "Charlie", "Dave", "Bob"]
submitted = set(submissions)
print(f"{len(submitted)} students have submitted.")
```

**Scenario 3: Finding shared interests**
Two users each list their favorite topics. Intersection shows what they have in common.

```python
user_a = {"Python", "hiking", "cooking", "chess"}
user_b = {"Python", "gaming", "cooking", "running"}
shared = user_a & user_b
print(f"Shared interests: {sorted(shared)}")
```

These examples show that `set` is a practical, frequently-needed tool—not an academic curiosity.

### F) Extended drill questions for fast finishers or after-class practice

Give these to learners who complete the lab early or want more practice:

1. Write a program that asks for three different users' tag lists (comma-separated) and finds which tags all three users share.
2. Given two lists of product IDs, find: (a) products in either list, (b) products in both lists.
3. Given a paragraph of text, count how many distinct words it contains using a set.
4. Why can you not use a list as a set element? What does Python say if you try?
5. A set `s = {1, 2, 3}`. Write the one-line expression to create a new set with only elements greater than 1 (hint: use a for loop and a new set, since comprehensions are out of scope).
6. Explain in plain English why checking `'Alice' in large_set` is faster than `'Alice' in large_list` for very large data.

For question 4: if learners try `{[1, 2], [3, 4]}`, Python raises `TypeError: unhashable type: 'list'`. The brief answer is that set elements must be hashable (their value cannot change), so lists—which can change—cannot be set elements. Strings, integers, and tuples can be.

For question 6: the brief answer is that a list checks each item one by one (up to N steps), while a set uses hashing to jump directly to the relevant location (near-constant time). Do not go deeper than this at Basics level.

### G) Calm language for the "order keeps changing" confusion

When a learner is surprised that printing the same set twice shows different orders, use this explanation:

"Python uses a technique called hashing to store set values efficiently. The display order is a byproduct of that internal storage, not something Python promises to preserve. Think of a corkboard where you push pins without worrying about their exact position—you can still check whether a pin is there or not, and that check is very fast. The order of pins on the board is irrelevant. That is what a set does."

### H) Final teaching reminder to yourself

The hour succeeds if learners leave with this mental model:

"A set holds unique values. Duplicates disappear automatically. Use `set(my_list)` to deduplicate. Use `in` for membership. Use `sorted()` for clean display."

---

## Speaker Notes: Scope Guardrails

**Teach in this hour:**
- Set creation with curly braces
- `set()` for empty set and list-to-set conversion
- `add()` method
- Automatic uniqueness (duplicates ignored)
- `in` membership testing on a set
- `len()` for unique count
- Sets are unordered — use `sorted()` for display
- Union (`|`) and intersection (`&`) at a conceptual/demo level only

**Do NOT introduce in this hour:**
- `frozenset` (out of scope — Basics)
- Set comprehensions (out of scope — Advanced)
- `discard()` and `remove()` methods (Advanced complexity; not needed for lab)
- `difference()`, `symmetric_difference()` (out of scope)
- Performance benchmarking of set vs list (not needed at Basics level)
- Hashing internals (mention the word only if asked; do not explain in depth)
- `collections.Counter` class (out of scope — Advanced; this is for Hour 20 counting pattern using only dicts)
- Set operations in the lab requirements (conceptual overview only — do not require `|` or `&` in lab submission)

Keep the conceptual message simple: **sets give you unique values and fast membership checks. Duplicates disappear automatically.**
