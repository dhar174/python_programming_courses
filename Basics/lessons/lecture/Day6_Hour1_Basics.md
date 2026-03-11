# Day 6, Hour 1: Choosing the Right Structure (Course Hour 21)
**Python Programming Basics – Session 6**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 6, Course Hour 21 – Choosing the right structure  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is a detailed read-aloud teaching guide for Course Hour 21. This hour is about judgment, not memorizing a new method. Learners already know the core structures — list, tuple, set, and dictionary — from Session 5. Now they need help making good choices. Stay firmly within Basics scope. Do not drift into performance benchmarking, Big O notation, data modeling theory, custom classes, or advanced nested structures. The key instructional move is comparison: take a real task, show a possible solution, then show a clearer structure choice and explain why it fits better. Keep reinforcing a short decision checklist: **Do I need order? Do I need duplicates? Do I need lookup by key? Is this a fixed record? Will the collection change?** The guided lab is a refactor challenge, so learners must do more than produce working code — they must explain at least one tradeoff. Every **Say:** block is written to be read nearly verbatim. Adapt naturally, but keep the explanations intact because they do the heavy teaching work.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Explain in plain language what problem each core structure solves best: list, tuple, set, and dictionary.
2. Choose between a list and a set based on whether order and duplicates matter.
3. Choose between a list and a dictionary based on whether searching by a meaningful key matters.
4. Explain when a tuple is a better fit than a list because the data is a small, fixed record.
5. Refactor a small working solution from one structure to a better-fitting structure and explain at least one tradeoff in clarity, safety, or simplicity."

---

## 1) Agenda + Timing

- **0:00–0:05** Reconnect to Session 5 and frame the structure-choice problem
- **0:05–0:14** Quick comparison review: list vs tuple vs set vs dictionary
- **0:14–0:24** Decision checklist: order, duplicates, key lookup, fixed records, mutability
- **0:24–0:34** Live demo 1: duplicate detection and membership — list first, then set
- **0:34–0:42** Live demo 2: phone lookup — awkward list approach, then dictionary refactor
- **0:42–0:55** Guided lab: Refactor Challenge
- **0:55–0:58** Debrief and learner explanations
- **0:58–1:00** Recap and exit ticket

---

## 2) Instructor Setup Checklist

- Open a clean file named `hour21_structure_choice_demo.py`.
- Open a second file named `hour21_refactor_lab.py` with section headers only for learners who need a scaffold.
- Have a Python REPL ready for tiny comparison examples.
- Put these four labels somewhere visible before class begins: **list**, **tuple**, **set**, **dict**.
- Prepare one everyday example for each structure:
  - shopping list → list
  - coordinate `(x, y)` → tuple
  - unique visitor names → set
  - contact name → phone number → dictionary
- Be ready to ask learners to justify choices out loud. This hour is about reasoning, not just syntax.
- Prepare one deliberate “not wrong, but awkward” solution to show that code can work and still be a poor fit.

**Say:** "Please have your editor open and a blank file ready. This hour is less about learning a brand-new feature and more about learning how to think before you code. That is a real programming skill, and it is one of the things that separates guesswork from confidence."

---

## 3) Opening Script: From Knowing Structures to Choosing Structures (~5 minutes)

### 3.1 Reconnect to Session 5

**Say:**
"Welcome to Session 6. Last session gave us a strong toolkit. We worked with tuples, sets, and dictionaries, and we reinforced list thinking. By the end of Session 5, you knew what each structure *is*, how to create it, and how to do the main operations with it.

Today we shift to a more professional question: **When should I choose this structure?**

That question matters because many beginner programs technically run, but they are harder to read, harder to extend, or easier to break than they need to be. Often the issue is not a syntax mistake. Often the issue is that the data structure does not match the job."

### 3.2 Why this matters in real work

**Say:**
"Imagine four tasks:

- You need to keep a sequence of songs in the order a user selected them.
- You need to store the coordinates of a point on a screen.
- You need to remove duplicate email addresses from a messy list.
- You need to look up a phone number by a person’s name.

Could you force all four tasks into one structure type? In some messy way, yes. But that is not the standard we want.

Good programmers do not just ask, ‘Can I make this work?’ They also ask, ‘What structure makes this simpler, clearer, and safer?’"

### 3.3 Set expectations for the hour

**Say:**
"By the end of this hour, I want you to have a small mental checklist you can apply almost automatically:

- Does order matter?
- Can duplicates happen?
- Do I need to look something up by a key like a name?
- Is this really one fixed record with a small number of parts?
- Will the collection change over time?

Those questions will not solve every design problem in programming, but they will solve a surprising number of Basics-level ones."

---

## 4) Quick Comparison Review: The Four Core Structures

### 4.1 Lists: ordered and flexible

**Say:**
"Let’s begin with the list. A list is an ordered, mutable collection. Ordered means position matters. Mutable means you can change it after creation.

Use a list when:
- order matters
- duplicates are allowed
- the collection may grow, shrink, or change

Examples include a shopping list, a playlist, a list of temperatures, or a queue of tasks."

**Type:**

```python
shopping_list: list[str] = ["milk", "bread", "apples", "bread"]
print(shopping_list)
print(shopping_list[0])
```

**Say:**
"Notice that duplicates are fine here. The fact that `bread` appears twice is not an error. In some situations that is exactly what we want. The key idea is that lists preserve the sequence exactly as we entered it."

### 4.2 Tuples: fixed records that stay together

**Say:**
"A tuple is also ordered, but unlike a list it is immutable. That means after creation, you do not change it.

Use a tuple when:
- you have a small, fixed record
- the values belong together as one unit
- you want to signal that the record should not be edited casually

Examples include a coordinate, a date, an RGB color, or a measurement with a value and a unit."

**Type:**

```python
point: tuple[int, int] = (4, 9)
print(point)
print(point[0], point[1])
```

**Say:**
"The tuple is not a general-purpose growing collection. It is best for a fixed grouping. A coordinate is a great example because the `x` and `y` belong together and usually should not be treated like an editable shopping list."

### 4.3 Sets: uniqueness built in

**Say:**
"A set is an unordered collection of unique values.

Use a set when:
- duplicates should disappear
- membership checking matters
- order does not matter

Examples include unique visitor names, unique email addresses, or a collection of tags."

**Type:**

```python
emails: set[str] = {"a@example.com", "b@example.com", "a@example.com"}
print(emails)
print(len(emails))
```

**Say:**
"This is a perfect example of a structure doing useful work for us automatically. We gave Python a duplicate email, and the set kept just one copy. If uniqueness is the rule, a set is often the simplest answer."

### 4.4 Dictionaries: lookup by key

**Say:**
"A dictionary stores key-value pairs. The key gives you a direct path to the value.

Use a dictionary when:
- each item has a meaningful key
- you want to look up values by name, code, or label
- you want the code to express relationships clearly

Examples include contact name to phone number, item name to quantity, or country code to country name."

**Type:**

```python
contacts: dict[str, str] = {
    "Maya": "555-0101",
    "Evan": "555-0130",
}

print(contacts["Maya"])
print(contacts.get("Noah", "Not found"))
```

**Say:**
"The dictionary shines when the question is not ‘What is item number 3?’ but ‘What is the value for this key?’ That is a different kind of access, and it maps naturally to real problems."

### 4.5 A one-minute comparison table

**Say:**
"Let me summarize these in one quick comparison table. Encourage learners to copy this into notes if it helps."

| Structure | Ordered? | Mutable? | Duplicates? | Best for |
| --- | --- | --- | --- | --- |
| List | Yes | Yes | Allowed | sequences that change |
| Tuple | Yes | No | Allowed | small fixed records |
| Set | No | Yes | Not allowed | uniqueness and membership |
| Dictionary | In insertion order | Yes | Keys must be unique | lookup by key |

**Say:**
"Do not memorize this as a dead chart. Use it as a thinking tool. When you are unsure, come back to what the problem needs."

---

## 5) Decision Checklist: How to Choose the Right Structure

### 5.1 Question 1: Does order matter?

**Say:**
"Here is the first question: **Does order matter?**

If the answer is yes, you are probably leaning toward a list or a tuple.

If the answer is no, a set or a dictionary may be a better fit.

For example, if you are storing the order students entered a room, a list makes sense because the first student and second student matter. If you only care who attended at all, not the order, a set might be better."

**Ask learners:**
"If I am storing the top five songs in the exact order a user ranked them, which structure sounds more natural right away?"

Pause for answers.

**Say:**
"Yes — a list. Order is part of the meaning of the data."

### 5.2 Question 2: Are duplicates allowed or meaningful?

**Say:**
"Next question: **Are duplicates allowed or meaningful?**

A shopping list may contain `bread` twice if you truly want two loaves. A playlist may contain the same song twice if someone added it twice. A temperature list may repeat `72` many times and that is fine.

But a set of unique employee IDs should never contain the same ID twice. A list of registered usernames probably should not contain duplicates either.

If duplicates should not exist, a set deserves serious consideration."

**Type:**

```python
visitor_names: list[str] = ["Ana", "Ben", "Ana", "Chris", "Ben"]
print(visitor_names)
print(set(visitor_names))
```

**Say:**
"The list preserves every entry exactly. The set keeps the unique names only. Neither is universally better. The right one depends on the question you are trying to answer."

### 5.3 Question 3: Do I need lookup by key?

**Say:**
"Third question: **Do I need to look something up by a meaningful key like a name, code, or label?**

If the answer is yes, that is often a dictionary.

Imagine storing student scores. A list of scores like `[90, 88, 95]` tells us almost nothing unless we separately know whose score is whose. A dictionary like `{'Ava': 90, 'Liam': 88, 'Zoe': 95}` immediately answers the question, ‘What is Zoe’s score?’"

**Ask learners:**
"If I need to search a phone number by contact name, what sounds more natural: a list of names, a set of names, or a dictionary from name to phone number? Why?"

Take one or two responses.

**Say:**
"Exactly. A dictionary matches the shape of the problem."

### 5.4 Question 4: Is this a small fixed record?

**Say:**
"Fourth question: **Is this one small fixed record?**

If it is, think tuple.

A coordinate `(x, y)` is not really a growing collection. A date `(year, month, day)` is not a bag of items to keep appending to. A measurement `(34.5, 'celsius')` is one record with pieces that belong together.

That is where tuples are clearer than lists. A list would technically work, but it suggests ongoing change, which may not match the meaning."

### 5.5 Question 5: Will this collection change over time?

**Say:**
"Fifth question: **Will this collection change over time?**

If you will add, remove, or update items regularly, that pushes you toward mutable structures like lists, sets, and dictionaries.

If the data should stay fixed after creation, tuple may be a better signal.

This is not about strict rules. It is about what message the structure sends to you and to anyone reading your code later."

### 5.6 The decision checklist in one simple script

**Say:**
"I want to say the full checklist out loud one more time. This is the heart of the hour:

1. Do I need order?
2. Do I need duplicates?
3. Do I need lookup by key?
4. Is this a fixed record?
5. Will the collection change?

If learners can ask those five questions automatically, they are making strong progress."

---

## 6) Worked Comparison: The Same Problem, Different Structures

### 6.1 Problem A: Checking whether a username has already been seen

**Say:**
"Let’s start with a practical problem: you are processing usernames one by one, and you want to know whether each name has already appeared.

A beginner might start with a list because lists feel familiar. That is not wrong. Let’s do that first."

**Type and narrate:**

```python
seen_users_list: list[str] = []

new_users: list[str] = ["maya", "evan", "maya", "zoe", "evan"]

for username in new_users:
    if username in seen_users_list:
        print(f"{username} is a duplicate")
    else:
        seen_users_list.append(username)
        print(f"Added {username}")

print(seen_users_list)
```

**Say:**
"This works. That matters. We do not insult working code. But now let’s ask a design question: what are we really using `seen_users_list` for?

We are not using positions.
We are not using duplicates meaningfully.
We are mainly asking, ‘Have I seen this value before?’

That makes a set a better fit."

**Type the refactor:**

```python
seen_users_set: set[str] = set()

for username in new_users:
    if username in seen_users_set:
        print(f"{username} is a duplicate")
    else:
        seen_users_set.add(username)
        print(f"Added {username}")

print(seen_users_set)
```

**Say:**
"Same behavior, but the structure now matches the goal. We want uniqueness and membership checking, so the set expresses our intent more clearly.

This is a key habit: sometimes the best sign that a structure is wrong is not that the code crashes. It is that you keep fighting the structure to do a job another structure naturally handles."

### 6.2 Problem B: Storing a point on a map

**Say:**
"Now let’s look at a different kind of problem: storing a point on a map.

Could we use a list? Yes."

```python
point_list: list[int] = [12, 30]
print(point_list[0], point_list[1])
```

**Say:**
"But if the point is conceptually one fixed pair — x and y — a tuple often communicates that more cleanly."

```python
point_tuple: tuple[int, int] = (12, 30)
x, y = point_tuple
print(f"x = {x}, y = {y}")
```

**Say:**
"This is a subtle choice. The list version is not a disaster. But the tuple says, ‘These two values belong together as one record.’ That is a better message."

### 6.3 Problem C: Looking up a phone number by name

**Say:**
"Now let’s take a problem that really highlights the value of dictionaries.

Suppose you start with paired data in a list of tuples."

```python
contacts_as_pairs: list[tuple[str, str]] = [
    ("Maya", "555-0101"),
    ("Evan", "555-0130"),
    ("Zoe", "555-0165"),
]
```

**Say:**
"This is not terrible. In fact, it is perfectly readable for a tiny set of contacts. But what happens when I want the phone number for `Zoe`? I have to loop through the whole list and compare names one by one."

**Type:**

```python
search_name: str = "Zoe"
found_phone: str | None = None

for name, phone in contacts_as_pairs:
    if name == search_name:
        found_phone = phone
        break

print(found_phone)
```

**Say:**
"Again, this works. But the structure does not match the question. The question is ‘given a name, what is the phone number?’ That is a dictionary question."

**Type the refactor:**

```python
contacts_dict: dict[str, str] = {
    "Maya": "555-0101",
    "Evan": "555-0130",
    "Zoe": "555-0165",
}

print(contacts_dict.get("Zoe", "Not found"))
```

**Say:**
"One line, clear meaning, and safe missing-key handling with `get()`. That is the kind of clarity we want learners to notice."

### 6.4 “Best” depends on the actual need

**Say:**
"One thing I want to emphasize carefully: the correct structure depends on the *actual requirement*, not on what seems most sophisticated.

If I need to keep contacts in the exact order they were entered and I want to allow duplicate names, maybe a list of records makes sense.
If I need name-to-phone lookup, a dictionary makes sense.
If I only care about unique names seen so far, a set makes sense.

So the structure is chosen by the job, not by our personal favorite."

---

## 7) Live Demo 1: Duplicate Detection and Membership — List First, Then Set (~10 minutes)

### 7.1 Frame the demo

**Say:**
"In this first live demo, I want to model a useful professional habit: start with a simple working idea, then improve the structure once the real need becomes clear."

### 7.2 Step 1: Solve with a list

**Type from a blank file:**

```python
usernames: list[str] = ["ava", "liam", "ava", "mia", "liam", "noah"]
seen: list[str] = []

for username in usernames:
    if username in seen:
        print(f"Duplicate found: {username}")
    else:
        seen.append(username)
        print(f"New user: {username}")

print(f"Seen users: {seen}")
```

**Say:**
"Before I run this, predict the output. Which names will be marked as duplicates?"

Take brief predictions, then run it.

**Say:**
"Good. The code does what we asked. That is our baseline."

### 7.3 Step 2: Ask whether the structure fits

**Say:**
"Now let’s step back and inspect the role of `seen`.

- Are we using the order in `seen` for anything important? Not really.
- Do we want duplicates in `seen`? Definitely not.
- Are we mostly using `in` to check membership? Yes.

That is the moment to recognize that `seen` wants to be a set, not a list."

### 7.4 Step 3: Refactor to a set

**Type:**

```python
usernames: list[str] = ["ava", "liam", "ava", "mia", "liam", "noah"]
seen: set[str] = set()

for username in usernames:
    if username in seen:
        print(f"Duplicate found: {username}")
    else:
        seen.add(username)
        print(f"New user: {username}")

print(f"Seen users: {seen}")
```

**Say:**
"Notice how small the code changes are. The important change is conceptual: the structure now expresses the rule of the program more accurately."

### 7.5 Pull out the lesson explicitly

**Say:**
"Here is the design lesson: if your code is using a collection mostly for membership checks and uniqueness, that is a clue to consider a set.

That does not mean lists are bad. It means the set better matches the purpose in this case."

---

## 8) Live Demo 2: Phone Lookup — Awkward List Approach, Then Dictionary Refactor (~8 minutes)

### 8.1 Start with the awkward but working version

**Say:**
"For the second demo, we will deliberately start with a structure that works but feels awkward. That is a good exercise because beginners often stop at ‘it works.’ We want to take one more step and ask whether it is a good fit."

**Type:**

```python
contacts: list[tuple[str, str]] = [
    ("Ava", "555-0111"),
    ("Liam", "555-0222"),
    ("Mia", "555-0333"),
]

search_name: str = input("Enter a contact name: ")
found_phone: str | None = None

for name, phone in contacts:
    if name == search_name:
        found_phone = phone
        break

if found_phone is None:
    print("Contact not found")
else:
    print(f"{search_name}: {found_phone}")
```

Run it once with an existing name and once with a missing name.

### 8.2 Discuss the design

**Say:**
"There is nothing illegal or broken here. But the moment the main task is lookup by name, the dictionary becomes the more natural tool. It lets the structure carry some of the logic for us."

### 8.3 Refactor to a dictionary

**Type:**

```python
contacts: dict[str, str] = {
    "Ava": "555-0111",
    "Liam": "555-0222",
    "Mia": "555-0333",
}

search_name: str = input("Enter a contact name: ")
phone: str = contacts.get(search_name, "Contact not found")
print(f"Result: {phone}")
```

### 8.4 Highlight safe missing-key access

**Say:**
"Notice one important detail: I used `get()` rather than bare bracket access. If the key is missing, `get()` lets us handle that safely instead of crashing with a `KeyError`.

That safety habit will matter again in Hour 24 when learners do their checkpoint assessment."

---

## 9) Guided Lab: Refactor Challenge (~13 minutes)

### 9.1 Lab framing

**Say:**
"Now it is your turn. This lab is called the **Refactor Challenge**. The goal is not just to write fresh code. The goal is to improve a working solution by choosing a better-fitting structure and then explain why your refactor is better."

### 9.2 Lab prompt

Give learners this prompt on screen or in the starter file:

### Refactor Challenge

You will complete **two short refactors**.

**Part A — Duplicate Checker**

Start with this list-based program idea:

```python
raw_names = ["Ana", "Ben", "Ana", "Chris", "Ben", "Dana"]
```

Tasks:
1. Build a version that uses a list called `seen_names` to report duplicates.
2. Refactor it to use a set instead.
3. Print the final unique names.
4. Add a short comment explaining why the set version is a better fit.

**Part B — Score Lookup**

Start with this paired data:

```python
score_pairs = [("Ava", 91), ("Liam", 88), ("Mia", 95)]
```

Tasks:
1. Write a version that searches the list of tuples for one student name.
2. Refactor it to use a dictionary.
3. Search for one existing name and one missing name.
4. Use safe access for the dictionary version.
5. Add a short comment explaining the tradeoff.

### 9.3 Completion criteria

```text
Completion criteria
```

- Both parts run without crashing.
- Part A includes a list version and a set version.
- Part B includes a list-of-tuples version and a dictionary version.
- The dictionary version handles a missing name safely.
- Learner explanation mentions at least one tradeoff such as order, duplicates, lookup by key, or readability.

### 9.4 Hints to release verbally after 3–4 minutes

**Say:**
"A few hints if you need them:

- In Part A, ask yourself whether the final collection of seen names needs duplicates or order.
- In Part B, ask yourself whether the main job is scanning every item or looking up by key.
- For safe dictionary access, think back to `get()` from Session 5.
- If your first version works, that is good. Refactoring is the second step, not a sign that the first step was worthless."

### 9.5 Common pitfalls to circulate for

```text
Common pitfalls to watch for
```

- Forgetting that an empty set is `set()`, not `{}`
- Writing the dictionary version with `scores[name]` when the key might not exist
- Refactoring the structure but forgetting to change methods, such as using `append()` on a set
- Assuming the set will print in the same order as the original list
- Explaining only that one version is “better” without saying *why*

### 9.6 Optional extensions for early finishers

```text
Optional extensions (stay in Basics scope)
```

- In Part A, print the duplicate names only once by storing duplicates in a second set.
- In Part B, print all scores in a neat table using `for name, score in scores.items()`.
- Add a small search loop that lets the user test several names one after another.

### 9.7 Instructor circulation script

As learners work, circulate with short coaching prompts:

**Say:**
"Tell me what question your program is asking most often."

If the learner says, "It keeps checking whether a name is already there," guide them toward the set idea.

**Say:**
"What matters more here — the position of the data, or the ability to look it up by a meaningful key?"

If the learner is stuck on the dictionary refactor, ask:

**Say:**
"If you already know the student’s name, what structure lets you go directly to the score instead of looping?"

---

## 10) Debrief: Make the Thinking Visible (~3 minutes)

### 10.1 Invite explanation, not just answers

**Say:**
"Let’s come back together. I want to hear not only what you built, but why you made the structure choices you made."

Invite two or three learners to share.

Suggested prompts:
- "In Part A, what changed when you moved from a list to a set?"
- "In Part B, why is a dictionary a cleaner fit for score lookup?"
- "What tradeoff did you notice?"

### 10.2 Model a strong explanation

**Say:**
"A strong explanation sounds like this: ‘The list version worked, but the set was a better fit because I only cared whether a name had already been seen. I did not need order or duplicates. For the scores, the dictionary was better because I needed lookup by name, and `get()` let me handle missing names safely.’

That kind of explanation shows real understanding."

### 10.3 Reinforce that working code is step one, not step zero

**Say:**
"One habit I want you to keep: do not be embarrassed if your first solution is not the cleanest one. In real programming, it is very common to write a working version first and then improve the structure once the problem becomes clearer. That is called progress, not failure."

---

## 11) Recap + Exit Ticket (~2 minutes)

### 11.1 Recap the hour in plain language

**Say:**
"Today’s big idea was simple but important: good programming is not only about writing valid syntax. It is also about choosing the data structure that naturally fits the problem.

We reviewed the four core structures:
- lists for ordered, changeable sequences
- tuples for small fixed records
- sets for uniqueness and membership
- dictionaries for lookup by key

And we practiced moving from ‘it works’ to ‘it fits.’"

### 11.2 Exit ticket

```text
Quick check / exit ticket
```

Ask learners to answer aloud, on paper, or in chat:

1. If you need fast lookup by name, which structure usually fits best?
2. If you need unique values and do not care about order, which structure usually fits best?
3. If you are storing a coordinate `(x, y)`, why might a tuple be clearer than a list?
4. Give one example of a task where a list is still the best choice.

### 11.3 Closing script

**Say:**
"In the next hour, we are going to strengthen this judgment through repetition. You will move through a data-structure drill circuit and practice these patterns quickly. Today was about choosing well. Next hour is about using those choices fluently."

---

## 12) Appendix: Quick Reference for Instructor Wrap-Up or Posting

### 12.1 The five-question decision guide

**Say:**
"If you want one tiny reference to keep beside your keyboard, make it this:

- Need order? Think list or tuple.
- Need change over time? Think list, set, or dictionary.
- Need uniqueness only? Think set.
- Need lookup by name or code? Think dictionary.
- Need a small fixed record? Think tuple."

### 12.2 A final reminder against overengineering

**Say:**
"One last teaching point: choosing the right structure does not mean choosing the fanciest structure. If a simple list solves the actual problem clearly, that is a good choice. Overengineering is not sophistication. The goal is fit."

