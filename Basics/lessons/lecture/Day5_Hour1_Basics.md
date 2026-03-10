# Day 5, Hour 1: Tuples + Unpacking (Course Hour 17)
**Python Programming Basics – Session 5**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 5, Course Hour 17 – Tuples + unpacking  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is written as a detailed read-aloud teaching guide. This hour introduces tuples as a second sequence type alongside lists. The critical comparison is mutability: lists can change; tuples cannot. Keep scope tight. The key concepts are tuple creation with parentheses and commas, why immutability is a feature rather than a limitation, tuple unpacking into separate variables, and the single-item tuple gotcha of the trailing comma. Do not introduce named tuples, `collections.namedtuple`, `typing.NamedTuple`, or advanced unpacking with `*`. The lab is the Coordinate Tracker.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:
1. Create a tuple using parentheses and commas, and explain what immutability means.
2. Explain when a tuple is a better choice than a list for storing related values.
3. Unpack a tuple's values into individual variables in a single assignment line.
4. Recognize and correct the single-item tuple mistake of omitting the trailing comma.
5. Store a collection of (x, y) coordinate tuples inside a list and iterate over them.
6. Compute the minimum and maximum x-values from a list of coordinate tuples.

This hour marks the beginning of Session 5. We are expanding our toolbox beyond lists. Today we learn a structure that is similar to a list in some ways, but fundamentally different in one important way: once you create a tuple, it cannot be changed."

---

## 1) Agenda + Timing (show slide / read quickly, ~2 minutes)

- **0:00–0:05** Session 5 introduction, recap of Session 4, and motivation for a new data structure
- **0:05–0:15** What a tuple is, how to write one, and why immutability matters
- **0:15–0:25** Tuple unpacking: pulling values out into separate variables
- **0:25–0:35** Common pitfalls: single-item tuples, trying to modify tuple items
- **0:35–0:45** Live demo: coordinates, unpacking, immutability error
- **0:45–0:57** Guided lab: Coordinate Tracker
- **0:57–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist (before class)

- Open a clean file such as `hour17_tuples_demo.py`.
- Have terminal and editor visible side by side so learners see code and output together.
- Prepare a few (x, y) coordinate pairs mentally: `(3, 7)`, `(0, 0)`, `(-2, 5)`, `(10, 4)`, `(1, 9)`.
- Be ready to demonstrate one deliberate `TypeError` by trying to assign to a tuple index.
- Be ready to show the single-item tuple trap: `(5)` vs `(5,)`.
- If some learners type slowly, have a starter file with comments only ready to paste.

**Say:** "Please type with me today. The tuple concepts are short, but the patterns—especially unpacking—become muscle memory only when you actually type them."

---

## 3) Opening Script: Welcome to Session 5 (~5 minutes)

### 3.1 Reconnect to the path so far

**Say:**
"Welcome to Day 5. We are now in Session 5 of the course.

Let me take thirty seconds to place today in context. In Sessions 1 and 2, we focused on individual values: numbers, strings, booleans, conditions, and loops. In Sessions 3 and 4, we introduced lists—our first real data structure. Lists gave us a way to store many related values in one variable and process them with loops.

If you now understand how to create a list, append to it, remove from it, access items by index, and loop over it, you have a very real foundation.

Today we are not abandoning any of that. We are widening the toolbox.

The question we are answering today is: are there situations where a list is actually the wrong tool? And the answer is yes—there are."

### 3.2 Motivate the need for a tuple

**Say:**
"Think about coordinates. A GPS coordinate has two parts: a latitude and a longitude. Those two values belong together. They describe one location.

If I want to store a location, I could use a list: `[48.8566, 2.3522]`. That works. But there is a risk with a list: I could accidentally change one of those values. I could call `append()` and suddenly my 'two-part coordinate' has three parts. I could `pop()` one value by mistake.

For data that has a fixed structure—two parts, three parts, some specific number of parts that should never change—a tuple is a better tool. It is like a list, but it is locked. Once created, it cannot be modified.

That locked quality is not a weakness. It is a deliberate protection."

### 3.3 Soften the introduction

**Say:**
"I want to reassure you: tuples are not harder than lists. They are simpler in one important way: there are fewer operations to learn, because most mutation operations simply do not exist on tuples. You cannot append to a tuple. You cannot remove from a tuple. You can read from a tuple. You can iterate over a tuple. And you can unpack a tuple's values, which is one of the most useful patterns in Python.

Let us look at the syntax first, and then we will talk about why the immutability is valuable."

---

## 4) Core Concept: What a Tuple Is (~10 minutes)

### 4.1 Tuple syntax explained

**Say:**
"A tuple is written with parentheses and comma-separated values."

**Type:**

```python
point = (3, 7)
print(point)
print(type(point))
```

Run it.

**Say:**
"When I print `point`, Python shows `(3, 7)`. The parentheses and the comma together tell Python this is a tuple, not just a calculation.

`type(point)` returns `<class 'tuple'>`. That confirms Python sees this as a tuple object.

Notice I named this variable `point`. That name is intentional. A tuple is a great fit for things that feel like a fixed record: a coordinate point, a color in RGB, a date as year/month/day, a name and age pair. When you look at the variable name, you should already have a sense of what the tuple contains."

### 4.2 Indexing works the same as a list

**Type:**

```python
point = (3, 7)
print(point[0])
print(point[1])
```

**Say:**
"Indexing works exactly like a list. Index 0 is the first value, index 1 is the second. The zero-based counting rule does not change.

I can use negative indexing too: `point[-1]` is `7`."

**Type:**

```python
print(point[-1])
```

**Say:**
"So reading from a tuple behaves like reading from a list. That should feel familiar."

### 4.3 Show immutability directly

**Say:**
"Now let me show you the defining characteristic of a tuple."

**Type:**

```python
point = (3, 7)
point[0] = 99  # This will cause a TypeError
```

Run it.

**Say:**
"Read the error message: `TypeError: 'tuple' object does not support item assignment`. Python is refusing to let me change the value at index 0.

This is not a bug. This is Python enforcing the contract we implicitly agreed to when we chose a tuple. We said: these two values belong together and will not change. Python is holding us to that commitment.

If I need to change a coordinate, I have two options:
1. Use a list instead.
2. Create a new tuple with the updated values.

For the Coordinate Tracker lab today, we will treat each coordinate as fixed, so tuples are exactly right."

### 4.4 Tuples without parentheses (brief mention)

**Say:**
"Python technically allows you to write a tuple without parentheses, just using commas."

**Type:**

```python
color = 255, 128, 0
print(color)
print(type(color))
```

**Say:**
"Python still recognizes this as a tuple. However, for clarity and readability—especially when you are learning—I strongly recommend always including the parentheses. Explicit is better than implicit.

I am showing you this only because you may encounter it in other people's code."

### 4.5 The single-item tuple trap

**Say:**
"This is the pitfall I want you to remember, because it surprises nearly every beginner."

**Type:**

```python
not_a_tuple = (5)
print(type(not_a_tuple))

real_tuple = (5,)
print(type(real_tuple))
```

Run both.

**Say:**
"Look at the types. `(5)` is just the number 5 inside parentheses—Python sees those as grouping parentheses, not a tuple. The type is `int`.

`(5,)` with the trailing comma is a real single-item tuple. The type is `tuple`.

The rule is simple: if you want a single-item tuple, you must include the trailing comma. If you omit it, you get a regular value, not a tuple.

For this course, you will almost always work with tuples that have two or more items, so this pitfall is unlikely to bite you in today's lab. But I want you to know it exists."

### 4.6 Ask for predictions

**Ask learners:**
- "What is the type of `(10, 20)`?"
- "What is the type of `(10)`?"
- "What is the type of `(10,)`?"
- "If I try `(10, 20)[0] = 99`, what happens?"

Pause after each, then confirm by running the code.

---

## 5) Tuple Unpacking (~10 minutes)

### 5.1 Introduce unpacking with motivation

**Say:**
"One of the most elegant and frequently used features of tuples is unpacking. Instead of accessing each value by index, you can assign all the values of a tuple to separate variables in a single line.

This is especially powerful when a function returns a tuple, or when you loop over a list of tuples."

### 5.2 Basic unpacking example

**Type:**

```python
point = (3, 7)
x, y = point
print(f"x = {x}")
print(f"y = {y}")
```

Run it.

**Say:**
"This is unpacking. Python looks at `point`, sees it has two values, and assigns the first value to `x` and the second value to `y` in one step.

The result is the same as writing:
```python
x = point[0]
y = point[1]
```

But unpacking is cleaner and more readable. When you read `x, y = point`, you immediately understand the intent: we are pulling the x-coordinate and y-coordinate out of the point."

### 5.3 Unpacking in a for loop over a list of tuples

**Say:**
"This is where unpacking becomes genuinely powerful. When we have a list of tuples—which is exactly what the lab asks for—we can unpack directly in the loop."

**Type:**

```python
coordinates = [(3, 7), (0, 0), (-2, 5), (10, 4), (1, 9)]

for x, y in coordinates:
    print(f"Point: x={x}, y={y}")
```

Run it.

**Say:**
"Look at the loop header: `for x, y in coordinates`. Python automatically unpacks each tuple in the list. First iteration: `x = 3`, `y = 7`. Second: `x = 0`, `y = 0`. And so on.

This pattern is extremely common in real Python. When you see `for a, b in some_list_of_pairs`, that is tuple unpacking at work."

### 5.4 Mismatched unpacking error

**Say:**
"Unpacking requires that the number of variables exactly matches the number of items in the tuple."

**Type:**

```python
point = (3, 7)
x, y, z = point  # This will fail
```

**Say:**
"Before I run this, what do you predict will happen?"

Pause, then run.

**Say:**
"We get a `ValueError: not enough values to unpack`. Python has three target variables but only two values. The counts must match.

This is actually a useful error. It tells you immediately that your understanding of the tuple's structure does not match reality. If this happens in real code, check how many items your tuple actually has."

### 5.5 Practical pattern: returned pairs

**Say:**
"Tuple unpacking also works beautifully when a function returns two values. You will see this pattern everywhere in Python, even though we have not fully covered functions with return values yet. Here is a quick preview."

**Type:**

```python
def min_max(numbers: list) -> tuple:
    return min(numbers), max(numbers)

low, high = min_max([5, 2, 9, 1, 7])
print(f"Min: {low}, Max: {high}")
```

Run it.

**Say:**
"The function returns a tuple of two values. We immediately unpack them into `low` and `high`. This is a very clean pattern.

Do not worry about fully understanding function return values today—that comes in Session 7. The point is to see that unpacking is useful far beyond just coordinate data."

---

## 6) Live Demo: Full Tuple Workflow (~10 minutes)

### 6.1 Set up the demo file

**Say:**
"Let me now put together a complete demo that shows everything we have discussed: creating tuples, immutability, and unpacking together in one coherent piece of code."

**Type the full demo:**

```python
# hour17_tuples_demo.py

# 1. Create a list of coordinate tuples
coordinates = [
    (3, 7),
    (0, 0),
    (-2, 5),
    (10, 4),
    (1, 9)
]

# 2. Print each coordinate with unpacking
print("All coordinates:")
for x, y in coordinates:
    print(f"  ({x}, {y})")

# 3. Extract just the x values
x_values = []
for x, y in coordinates:
    x_values.append(x)

print(f"\nX values: {x_values}")
print(f"Minimum x: {min(x_values)}")
print(f"Maximum x: {max(x_values)}")

# 4. Show immutability
first_point = coordinates[0]
print(f"\nFirst point: {first_point}")

# Uncomment to see the error:
# first_point[0] = 99
```

Run it.

**Say:**
"Notice how clean the code reads. The `for x, y in coordinates` loop is self-documenting. Anyone reading the code understands immediately that each element of `coordinates` is an (x, y) pair.

I left the immutability error as a comment. Let me uncomment it now and show you what happens."

Uncomment `first_point[0] = 99`, save, and run.

**Say:**
"There is the `TypeError` again. This is Python protecting the data we told it should not change."

Re-comment the line.

### 6.2 Build intuition for when to choose tuples

**Say:**
"Let me leave you with a simple mental model for when to reach for a tuple versus a list.

Use a list when:
- the number of items can change
- you need to add or remove items
- you are building a collection over time

Use a tuple when:
- the number of items is fixed
- the items form a meaningful record
- you want immutability as a built-in guarantee
- you are returning multiple values from a function

The most common real-world uses for tuples are: coordinates, RGB colors, database row records, key-value pairs in some patterns, and function return values with multiple outputs."

**Ask learners:**
"Given this, should a shopping list be a list or a tuple?"

Pause.

"Right—a shopping list changes over time. It is a list.

Should a screen resolution like 1920 × 1080 be a list or a tuple?"

Pause.

"Right—a resolution is two fixed values. It is a tuple."

---

## 7) Common Pitfalls and Coaching (~5 minutes)

### 7.1 Pitfall: trying to change a tuple item

**Symptom:** learner gets `TypeError: 'tuple' object does not support item assignment`.

**Coach with these words:**
"Read the error. Python is not broken. The tuple is doing its job. If you actually need to change the value, ask yourself: should this be a list? If yes, switch to a list. If the data should be immutable, create a new tuple with the corrected values."

### 7.2 Pitfall: single-item tuple missing the trailing comma

**Symptom:** learner writes `single = (5)` and is confused when it behaves like an integer.

**Coach with these words:**
"Check the type with `print(type(single))`. If it shows `int`, you are missing the trailing comma. Change it to `(5,)` and re-check."

### 7.3 Pitfall: unpacking variable count mismatch

**Symptom:** learner gets `ValueError: too many values to unpack` or `not enough values to unpack`.

**Coach with these words:**
"Print the tuple first. Count its items. Count your target variables. They must match exactly. If you have a three-item tuple, you need three target variables: `a, b, c = my_tuple`."

### 7.4 Pitfall: confusing a tuple with a function call

**Symptom:** learner writes `print(3, 7)` and thinks `(3, 7)` is stored somewhere.

**Coach with these words:**
"The parentheses in a function call are syntax for the function, not a tuple. If you want to store a tuple, assign it to a variable: `point = (3, 7)`. Then pass it to print if you like: `print(point)`."

### 7.5 Pitfall: forgetting tuples support indexing and len()

**Say:**
"Beginners sometimes think tuples are mysterious. They are not. `len(my_tuple)` works. `my_tuple[0]` works. `for item in my_tuple` works. The only thing that does not work is modifying items in place."

---

## 8) Guided Lab: Coordinate Tracker (~12 minutes)

### 8.1 Introduce the lab

**Say:**
"Now it is your turn. This lab connects directly to what we built in the demo. You are going to build a Coordinate Tracker that stores five (x, y) points as tuples, prints each one, and computes the minimum and maximum x-values.

Here are the requirements:
1. Create a list containing exactly five (x, y) tuples. You can use the coordinates from the demo or choose your own.
2. Use a loop to print each point in a clean, readable format.
3. Compute the minimum x-value across all five points.
4. Compute the maximum x-value across all five points.
5. Print the minimum and maximum."

### 8.2 Put the requirements on screen

```text
Lab: Coordinate Tracker
- Create a list of 5 (x, y) tuples
- Print each point in a clear format
- Compute and print the minimum x-value
- Compute and print the maximum x-value
```

### 8.3 Provide a beginner-friendly starter structure

**Type and leave on screen:**

```python
# hour17_lab_coordinate_tracker.py

# Step 1: create the list of coordinate tuples
coordinates = [
    (3, 7),
    (0, 0),
    (-2, 5),
    (10, 4),
    (1, 9),
]

# Step 2: print each coordinate
print("Points:")
for x, y in coordinates:
    print(f"  ({x}, {y})")

# Step 3: collect x values and compute min/max
x_values = []
for x, y in coordinates:
    x_values.append(x)

print(f"\nMin x: {min(x_values)}")
print(f"Max x: {max(x_values)}")
```

### 8.4 Explain the starter

**Say:**
"This starter structure breaks the problem into three clear steps. Step 1 is the data. Step 2 is the display. Step 3 is the calculation. Each step uses what we have covered today.

Your first task is to get this running with your own coordinate values. After that, you can explore the optional extension."

### 8.5 Optional extension

**Say:**
"If you finish the core lab early, try this extension: compute the distance of each point from the origin, which is (0, 0).

The distance formula is the square root of `(x squared + y squared)`. In Python, you can compute a square root with `x ** 0.5` or by importing `math.sqrt`—but `** 0.5` works fine without any imports.

Print each point alongside its distance from the origin."

**Type the extension hint:**

```python
# Optional extension: distance from origin
for x, y in coordinates:
    distance = (x**2 + y**2) ** 0.5
    print(f"  ({x}, {y}) → distance from origin: {distance:.2f}")
```

**Say:**
"The `:.2f` in the f-string formats the float to two decimal places. That keeps the output tidy."

### 8.6 Instructor circulation prompts

As learners work, walk around and ask:
- "Show me your tuple list. How many elements does it have?"
- "Which line unpacks the x and y values?"
- "Where do you collect the x values? Is that a list or a tuple?"
- "What do `min()` and `max()` return when you pass in the x_values list?"
- "What is the type of each element in your `coordinates` list?"

---

## 9) Debrief and Share-Outs (~5 minutes)

### 9.1 Bring the class back together

**Say:**
"Let's look at a few different solutions. The goal is not to find the single correct version—there are always multiple valid approaches. The goal is to identify what made certain solutions clean and readable."

### 9.2 Ask targeted questions

Ask:
- "Who used tuple unpacking in their loop? What did your loop header look like?"
- "Who can explain why we used a separate `x_values` list to collect x values before calling `min()` and `max()`?"
- "Did anyone try to modify a tuple item during the lab? What happened?"
- "Who tried the distance extension? What did the output look like?"

### 9.3 Model a concise explanation

**Say:**
"A strong explanation of this lab sounds like: 'I created a list where each element is an (x, y) tuple. I used a for loop with unpacking to print each point. I collected the x values into a separate list, then called min() and max() on that list.'

That explanation shows you understood both the data structure and the process."

---

## 10) Recap Script (~2 minutes)

**Say:**
"Today we introduced tuples. Here is what you should be able to say when you walk out:

- A tuple is an ordered, immutable sequence. You create it with parentheses and commas.
- You read from a tuple using indexing, just like a list. You cannot change items in place.
- Single-item tuples require a trailing comma: `(5,)` not `(5)`.
- Unpacking assigns each item in a tuple to a separate variable in one line: `x, y = point`.
- A list of tuples is a very practical pattern for storing structured records like coordinates.

The next hour continues Session 5. We move to sets: a collection that automatically removes duplicates and supports fast membership testing."

---

## 11) Exit Ticket (~1 minute)

Ask learners to answer verbally, in chat, or on paper:

1. What does `(10,)` do that `(10)` does not?
2. Write the one-line code that unpacks `point = (4, 9)` into two variables `x` and `y`.
3. Name one situation where a tuple is a better choice than a list.
4. What error do you get if you try to change an item in a tuple?

**Expected direction of answers:**
- `(10,)` is a single-item tuple; `(10)` is just the integer 10
- `x, y = point`
- fixed-size records (coordinates, RGB, function return values)
- `TypeError: 'tuple' object does not support item assignment`

---

## 12) Instructor Notes for the Transition to Hour 18

**Say:**
"We now have two sequence types in our toolkit: lists (mutable, ordered) and tuples (immutable, ordered). In the next hour, we add a third data structure: the set. Sets are unordered and contain no duplicates. They answer a completely different question: 'Is this value present, and how many unique values do I have?' That is a question you will need constantly in real programs."

If learners seem shaky, reinforce these core ideas before moving on:
- "A tuple cannot be changed after creation. That is the essential rule."
- "Unpacking is the most useful thing you can do with a tuple: `a, b = my_tuple`."

---

## Appendix: Instructor Reinforcement Notes for Hour 17

### A) Board sketch for visual learners

Draw this on the board if the room needs a visual anchor:

```text
List:  [3, 7]      ← can be changed
Tuple: (3, 7)      ← cannot be changed

Unpacking:
x, y = (3, 7)
x ← 3
y ← 7
```

Point to each element and ask: "What index is this?" Then ask: "What variable does this unpack into?"

### B) Short extra practice prompts

If you have two or three extra minutes, ask learners to answer these without typing first:

1. If `point = (10, 20)`, what does `point[0]` return?
2. If `color = (255, 128, 0)`, write the unpacking line.
3. If I write `t = (42)`, is `t` a tuple?
4. Can I use `len()` on a tuple?
5. If `pairs = [(1, 2), (3, 4)]`, what does `for a, b in pairs` do on the first iteration?

### C) Instructor language for gentle correction

When a learner makes a mistake:
- "Check the type with `type()`. What does Python say it is?"
- "Count the values in your tuple. Count your unpacking variables. Do they match?"
- "Is that value something that should be able to change? If so, should we use a list instead?"
- "Read the error name out loud. What does `TypeError` mean in plain English?"

### D) Coaching if learners ask about named tuples

If a learner asks about `namedtuple` or `typing.NamedTuple`, say:

"That is a great question, and it exists in Python—it lets you access tuple fields by name instead of index. But it is an Advanced-scope topic. For today, the important thing is to get comfortable with basic tuples and unpacking. Named tuples build on exactly what we are practicing right now."

### E) Final teaching reminder to yourself

The hour succeeds if learners leave with this mental model:

"A tuple is a fixed, ordered record. I can read it, loop over it, and unpack it. I cannot change it. Unpacking is the most useful pattern: `x, y = point`."

If they can create a list of tuples, unpack in a loop, and extract values for min/max computation, the hour has met its runbook goal.

---

## Speaker Notes: Scope Guardrails

**Teach in this hour:**
- Tuple creation with parentheses and commas
- Immutability (cannot assign to an index after creation)
- Tuple indexing (reading values by index)
- Tuple unpacking into variables
- Single-item tuple trailing-comma rule
- List of tuples + unpacking in a for loop

**Do NOT introduce in this hour:**
- `collections.namedtuple` (out of scope — Advanced)
- `typing.NamedTuple` (out of scope — Advanced)
- Extended unpacking with `*` (out of scope — Advanced)
- Tuple as a dictionary key (mention only if directly asked; do not demo)
- `zip()` function (save for when functions are more established)
- Comprehensions for generating tuple lists (out of scope for Basics)
- Comparison of tuple performance vs list (not needed at Basics level)
- `tuple()` constructor converting other types (not needed today)

Keep the conceptual message simple and repeatable: **tuples are immutable, they unpack cleanly, and they are ideal for fixed-size records like coordinates.**
