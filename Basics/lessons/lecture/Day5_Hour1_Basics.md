# Day 5, Hour 1: Tuples + Unpacking (Course Hour 17)
**Python Programming Basics – Session 5**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 5, Course Hour 17 – Tuples + unpacking  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is written as a detailed read-aloud teaching guide. Keep the hour tightly focused on tuples: what they are, how they differ from lists, how immutability protects data, and how unpacking lets you pull values out cleanly. Stay within Basics scope — do not introduce named tuples, `collections.namedtuple`, or advanced destructuring. The key outcomes are creating tuples, understanding why they are immutable, unpacking tuple values into variables, and making a principled choice between tuple and list. The lab reinforces all of this in a concrete coordinate-tracking program.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Create a tuple and explain in plain language why it is different from a list.
2. Demonstrate what immutability means by deliberately triggering a `TypeError` and reading its message.
3. Unpack a tuple's values into named variables in one clean line.
4. Explain when choosing a tuple over a list makes your code clearer and safer.
5. Build a coordinate-tracking program that stores `(x, y)` points as tuples in a list, prints each point, and computes the minimum and maximum x values."

---

## 1) Agenda + Timing

- **0:00–0:05** Reconnect to Day 4 collections; introduce the problem tuples solve
- **0:05–0:18** Core concept: what a tuple is, syntax, analogy, immutability
- **0:18–0:28** Tuple unpacking: basic form, swap trick, ignoring values with `_`
- **0:28–0:33** Tuple vs list decision guide
- **0:33–0:43** Live demo: coordinate pair, return from function, immutability error
- **0:43–0:57** Guided lab: Coordinate Tracker
- **0:57–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist

- Open a clean file called `hour17_tuples_demo.py` before class begins.
- Have a second file called `hour17_lab_coords.py` ready with empty comments only as a starter for learners who fall behind.
- Have the Python REPL ready in a terminal (type `python` or `python3`) for quick interactive experiments.
- Plan to show one deliberate `TypeError` by trying to assign to a tuple index.
- Plan to show the single-element trap: `(42)` is an integer, `(42,)` is a tuple.
- Confirm that `min()` and `max()` are covered in your learners' prior knowledge — they were introduced in Hour 14 (Day 4, Hour 2). Briefly remind learners if needed.

**Say:** "Please have your editor open and an empty file ready. This hour involves a lot of typing together. The real learning happens at your keyboard, not just by watching."

---

## 3) Opening Script: Reconnect to Earlier Learning (~5 minutes)

### 3.1 Quick recap from Session 4

**Say:**
"Welcome back. In Session 4 we covered lists. We built shopping-list programs, worked with loops that iterated over collections, and used core list methods like `append()`, `remove()`, and `pop()`.

Lists gave us a very powerful tool: one variable that holds many related values in order, and that we can change whenever we need to.

But here is a question worth pausing on: is it always a good idea for a collection to be changeable?

Think about a GPS coordinate. A point in two-dimensional space — say, latitude and longitude, or an (x, y) pair on a grid — represents one fixed location. Once you record it, you do not expect it to change. If your program accidentally changed it, that would be a bug, not a feature.

Today we learn a data structure that is designed to be *fixed*: the tuple."

### 3.2 Motivating the need

**Say:**
"Let me give you a few real-world situations where you want a small, fixed collection of related values:

- A point in 2D space: `(3, 7)` — an x and a y.
- A date: `(2024, 6, 15)` — a year, month, and day.
- An RGB colour: `(255, 128, 0)` — red, green, blue channels.
- The result of a measurement: `(34.5, 'celsius')` — a value and a unit.

In each of these cases, the values are related to each other and should stay together. And in each case, you would not want your program to accidentally add an extra item or remove one. You want the structure to be locked.

A tuple is exactly that: an ordered, fixed-size, immutable group of values."

### 3.3 Set expectations for the hour

**Say:**
"In this hour, we will learn:
- how to create a tuple
- why tuples cannot be changed and why that is actually useful
- how to pull values out of a tuple cleanly using a technique called unpacking
- when to choose a tuple rather than a list
- and how to build a small coordinate-tracking program using these ideas

You already know most of what you need. Tuples use a lot of the same intuitions as lists. The big new idea today is immutability and why it helps."

---

## 4) Concept: What Is a Tuple?

### 4.1 Beginner-friendly definition

**Say:**
"A tuple is an ordered, immutable collection of values.

Let's take that one word at a time.

- **Ordered** means the items have positions. First item, second item, third item. Same as a list.
- **Immutable** means the tuple cannot be changed after it is created. You cannot add items. You cannot remove items. You cannot swap one item for another. Once a tuple exists, it stays exactly as it was made.
- **Collection** means one variable holds multiple values.

If a list is like a whiteboard that you can write on and erase as much as you want, a tuple is like a laminated card. You can read it, you can pass it around, but you cannot change what is written on it."

### 4.2 Tuple literal syntax

**Type and narrate:**

```python
# A tuple with three values
point = (3, 7)
print(point)
print(type(point))
```

Run it.

**Say:**
"We create a tuple using parentheses. Inside the parentheses, values are separated by commas.

When we print `point`, Python shows us `(3, 7)`.
When we check the type, Python tells us `<class 'tuple'>`.

Notice that the parentheses appear in the output. Python uses them consistently to signal that this is a tuple, not a list."

### 4.3 Tuples with more than two values

**Type:**

```python
date = (2024, 6, 15)
colour = (255, 128, 0)
measurement = (34.5, "celsius")

print(date)
print(colour)
print(measurement)
```

**Say:**
"Tuples can hold any number of values. They can also mix types — notice `measurement` holds a float and a string together. That is valid because a measurement is a pair of related but differently-typed values.

However, for beginners, keep your tuples simple and focused. A tuple works best when it represents a single logical unit with a small, known number of parts."

### 4.4 Indexing into a tuple

**Say:**
"Because tuples are ordered, you can access individual items using index notation — exactly the same way you would with a list or a string."

**Type:**

```python
point = (3, 7)
print(point[0])   # 3
print(point[1])   # 7
```

**Ask learners:**
"What do you think `point[0]` prints? Call it out."

Wait for answers, then run it.

**Say:**
"Correct. Index zero gives us the first item, which is 3. Index one gives us the second item, which is 7.

The indexing rules are the same as lists: counting starts at zero, negative indices count from the right."

### 4.5 The critical trap: the single-element tuple

**Say:**
"Before we go any further, I want to show you one trap that catches almost every beginner the first time they see it.

How do you think we would write a tuple with just one value in it?"

Pause for guesses.

**Type:**

```python
not_a_tuple = (42)
print(type(not_a_tuple))
```

Run it.

**Say:**
"Look at the type. Python says `<class 'int'>`. This is an integer, not a tuple! Python sees `(42)` as ordinary parentheses around a number — the kind you use in a math expression. The parentheses do not automatically make something a tuple.

So how do we create a single-element tuple? We add a trailing comma."

**Type:**

```python
actually_a_tuple = (42,)
print(type(actually_a_tuple))
print(actually_a_tuple)
```

Run it.

**Say:**
"Now Python says `<class 'tuple'>`. That trailing comma is what tells Python: this is a tuple with one element, not just parentheses around a value.

This is one of the most common beginner mistakes with tuples. If your single-element tuple is behaving like an integer, check your comma.

For today's lab, all our tuples have two values, so you will not hit this trap. But I want you to have seen it before you encounter it by accident."

---

## 5) Immutability: Why Tuples Cannot Change

### 5.1 Show the TypeError

**Say:**
"The defining feature of a tuple is that it is immutable. Let me show you exactly what that means in code."

**Type:**

```python
point = (3, 7)
point[0] = 99   # attempt to change the first value
```

Run it.

**Say:**
"Python raises a `TypeError`. Read the message with me: `'tuple' object does not support item assignment`.

This is not a bug in your code that you need to fix — it is Python enforcing the rule. A tuple refuses to let you change any of its values after creation.

Now, here is the key question: why is this useful? Why would we ever *want* a collection we cannot change?"

### 5.2 Explain the value of immutability

**Say:**
"Immutability is a form of protection and communication.

First, **protection**: if a coordinate should never change, making it a tuple means Python will stop you — or anyone else editing the code — from accidentally modifying it. If you store a GPS point as a list, nothing prevents a careless line of code from doing `coords[0] = 0.0` and silently corrupting your data. If you store it as a tuple, Python raises an error immediately, and the bug is caught early.

Second, **communication**: when another programmer — or your future self — reads your code and sees a tuple, it sends a message. It says 'this group of values is meant to be fixed. Do not change it. Treat it as a record.'

Lists say 'this collection will grow and change'. Tuples say 'these values belong together and should not be touched'.

That distinction makes code easier to understand at a glance."

### 5.3 What you *can* do with a tuple

**Say:**
"Immutability does not mean useless. There is plenty you can do with a tuple.

You can read any item by index. You can iterate over it with a for loop. You can check membership with `in`. You can pass it to a function. You can store it in a list. You can unpack its values into separate variables — and unpacking is one of the most powerful patterns you will learn today."

**Type:**

```python
point = (3, 7)

# Reading
print(point[0])

# Membership check
print(3 in point)

# Iterating
for value in point:
    print(value)
```

Run it.

**Say:**
"All of this works. The only thing that does not work is *changing* the tuple in place."

---

## 6) Tuple Unpacking

### 6.1 The concept

**Say:**
"Tuple unpacking is one of my favourite Python features. It looks simple, but it turns out to be incredibly useful.

The idea is this: instead of accessing tuple items by index — `point[0]`, `point[1]` — you can unpack all the values in one line and give each of them a name."

**Type:**

```python
point = (3, 7)
x, y = point

print(x)   # 3
print(y)   # 7
```

Run it.

**Say:**
"In one line, `x, y = point`, Python takes the first value of `point` and assigns it to `x`, and takes the second value and assigns it to `y`.

This is far more readable than:

```python
x = point[0]
y = point[1]
```

With unpacking, the code *reads like natural language*. You can see immediately that `point` has two parts: an x-coordinate and a y-coordinate."

### 6.2 Unpacking must match the count

**Say:**
"There is one important rule: the number of variables on the left must match the number of values in the tuple."

**Type:**

```python
point = (3, 7)
x, y, z = point   # wrong! three names for two values
```

Run it.

**Say:**
"Python raises a `ValueError`: `not enough values to unpack`. It expected three values but only found two.

The same error occurs in reverse if you have too many values. Unpacking is strict — it requires an exact match."

Fix the code:

```python
x, y = point   # back to the correct version
```

### 6.3 Unpacking any tuple

**Say:**
"Unpacking works with any tuple, not just two-element ones."

**Type:**

```python
date = (2024, 6, 15)
year, month, day = date

print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
```

Run it.

**Say:**
"Now instead of `date[0]`, `date[1]`, `date[2]`, we have meaningful names: `year`, `month`, `day`. Anyone reading this code understands immediately what each value represents."

### 6.4 The swap trick

**Say:**
"Here is one of Python's most elegant patterns. Without a temporary variable, you can swap two variable values in one line using tuple unpacking."

**Type:**

```python
a = 10
b = 20

print(f"Before: a={a}, b={b}")

a, b = b, a   # swap

print(f"After:  a={a}, b={b}")
```

Run it.

**Say:**
"In most other languages you would need a third variable — `temp = a; a = b; b = temp`. In Python, `a, b = b, a` works because Python evaluates the right side first, creates a tuple `(20, 10)`, and then unpacks it into `a` and `b`.

You do not need to fully understand the mechanics today. What matters is recognising the pattern and knowing it works."

### 6.5 Ignoring values with `_`

**Say:**
"Sometimes a tuple has more values than you care about in a particular moment. Python has a convention: use an underscore `_` as a variable name to signal 'I deliberately don't need this value'."

**Type:**

```python
measurement = (34.5, "celsius")
value, _ = measurement   # we only care about the number

print(f"Temperature: {value}")
```

Run it.

**Say:**
"The underscore is assigned the string `'celsius'`, but we are not planning to use it. Using `_` communicates to anyone reading the code: 'I know there is a second value here and I am intentionally ignoring it'. This is better than naming it something throwaway like `unused`."

---

## 7) When to Use a Tuple vs a List

### 7.1 The core distinction

**Say:**
"You now know two ordered collection types: lists and tuples. How do you choose between them?

Here is the clearest way I can put it:

- Use a **list** when the collection is meant to grow, shrink, or change over time.
- Use a **tuple** when the collection represents a fixed record with a known, specific structure.

Ask yourself: 'Does this collection need to be modified after I create it?' If yes, use a list. If no, think about whether a tuple is the better signal."

### 7.2 Decision guide

| Situation | Best choice | Why |
|-----------|-------------|-----|
| Shopping cart that items are added to and removed from | List | The collection changes |
| All the tasks a user enters during a session | List | Grows over time |
| An (x, y) coordinate that should never change | Tuple | Fixed record, immutability protects it |
| A date like (year, month, day) | Tuple | Fixed structure, three known parts |
| A series of test scores | List | May grow; order matters but content evolves |
| RGB colour value: (255, 128, 0) | Tuple | Three fixed channels, never changes |
| A collection of user messages | List | Grows as messages arrive |
| A function returning two results | Tuple | Fixed pair; caller will unpack |

**Say:**
"Notice that tuples show up naturally when a function needs to return multiple values. In Python, the conventional way to return two things from a function is to return them as a tuple. The caller then unpacks them. We will see this in the live demo."

### 7.3 Keep it practical

**Say:**
"For beginners, this rule of thumb covers most cases: if the collection is a bunch of things that accumulate — add, remove, append — use a list. If the collection is a small, structured record with a fixed number of named parts — an address, a coordinate, a date, a size — use a tuple.

You will not always be certain which to choose. That is normal. As you write more programs, the right choice becomes more intuitive."

---

## 8) Live Demo: Coordinate Pairs

### 8.1 Overview

**Say:**
"Let me bring all of these ideas together in a live demo before we move into the lab. I am going to build a short program step by step. Please type along.

We will:
- create a pair of coordinates as a tuple
- unpack the x and y values
- show the immutability error
- then simulate a function returning a tuple

Open `hour17_tuples_demo.py`."

### 8.2 Part 1 — A simple coordinate

**Type and narrate:**

```python
# hour17_tuples_demo.py

# --- Part 1: Create and read a coordinate tuple ---
origin = (0, 0)
home = (3, 7)
destination = (-2, 5)

print(f"Origin:      {origin}")
print(f"Home:        {home}")
print(f"Destination: {destination}")
```

Run it.

**Say:**
"Three coordinate tuples. Each one is a (x, y) pair. Python prints each pair with its parentheses intact, which is a visual reminder that these are tuples."

### 8.3 Part 2 — Unpacking coordinates

**Type:**

```python
# --- Part 2: Unpack and use the values ---
x, y = home
print(f"Home x-coordinate: {x}")
print(f"Home y-coordinate: {y}")
```

Run it.

**Say:**
"Instead of writing `home[0]` and `home[1]`, we unpack into meaningful names. When we later use `x` and `y`, the intent is perfectly clear."

### 8.4 Part 3 — Show the immutability error

**Say:**
"Now I want to deliberately trigger the immutability error so you see the full picture."

**Type:**

```python
# --- Part 3: Show immutability ---
# This line will raise a TypeError — that is expected!
home[0] = 10
```

Run it.

**Say:**
"Read the message: `TypeError: 'tuple' object does not support item assignment`.

If you ever see this error in your own code, your first question should be: 'Did I intend this to be mutable? Should it be a list instead?' If the answer is no — if the tuple genuinely should stay fixed — then the error is Python protecting you."

Delete or comment out the failing line:

```python
# home[0] = 10  # intentional demo — do not run in lab
```

### 8.5 Part 4 — A function that returns a tuple

**Say:**
"Here is a common and very clean Python pattern: a function that returns two values as a tuple."

**Type:**

```python
# --- Part 4: Function returning a tuple ---
def get_midpoint(point_a: tuple[int, int], point_b: tuple[int, int]) -> tuple[float, float]:
    """Return the midpoint between two (x, y) coordinates."""
    mid_x = (point_a[0] + point_b[0]) / 2
    mid_y = (point_a[1] + point_b[1]) / 2
    return (mid_x, mid_y)


result = get_midpoint(home, destination)
print(f"Midpoint: {result}")

mid_x, mid_y = get_midpoint(home, destination)
print(f"Mid x = {mid_x}, Mid y = {mid_y}")
```

Run it.

**Say:**
"The function returns a tuple `(mid_x, mid_y)`. We can use the return value in two ways:

1. Keep the tuple whole: `result = get_midpoint(...)` — useful if we want to store it.
2. Unpack immediately: `mid_x, mid_y = get_midpoint(...)` — useful if we want named variables straight away.

Both forms are valid. Choose based on what makes the calling code most readable."

### 8.6 Part 5 — A list of tuples

**Say:**
"Our lab is built around a list of coordinate tuples. Let me show the pattern quickly so you can see it before you build it."

**Type:**

```python
# --- Part 5: A list of coordinate tuples ---
path = [
    (0, 0),
    (1, 3),
    (4, 2),
    (6, 8),
    (5, 1),
]

for point in path:
    x, y = point
    print(f"  x={x}, y={y}")
```

Run it.

**Say:**
"Notice the structure: `path` is a list — it is mutable, it can grow or shrink. Each item inside the list is a tuple — each coordinate is fixed. This is a natural and very common pattern in Python: a mutable outer container of immutable records."

---

## 9) Hands-on Lab: Coordinate Tracker

### 9.1 Lab overview

**Say:**
"Now it is your turn. The lab task is called the Coordinate Tracker. You have 14 minutes to work through it, then we will walk through the solution together.

This lab reinforces:
- creating tuples
- storing tuples in a list
- iterating with a for loop and unpacking
- using `min()` and `max()` on extracted values

Open a new file called `hour17_lab_coords.py`."

### 9.2 Lab specification

**Display or read aloud:**

---

**Lab: Coordinate Tracker**

**Situation:** You are tracking the positions of five sensors on a grid. Each sensor has an (x, y) location. Your program should record the positions and analyse them.

**Your task:**

1. Create a list called `sensors` containing **five (x, y) tuples**. Use any integer values you like. Make them varied — use positive and negative numbers, different magnitudes. Example: `(3, 7)`, `(-1, 4)`, `(8, 2)`, `(0, -5)`, `(6, 3)`.

2. Use a **for loop** to print each sensor's coordinates in this format:
   ```
   Sensor at x=3, y=7
   Sensor at x=-1, y=4
   ...
   ```

3. **Extract all the x values** from the sensor list into a new list called `x_values`. Use a for loop or a list comprehension (if you have seen those).

4. Print the **minimum x value** and the **maximum x value** using `min()` and `max()`.

**Expected output shape (your numbers will differ):**
```
Sensor at x=3, y=7
Sensor at x=-1, y=4
Sensor at x=8, y=2
Sensor at x=0, y=-5
Sensor at x=6, y=3

Minimum x: -1
Maximum x: 8
```

**Starter hint if you are stuck:**

```python
sensors = [
    (3, 7),
    # add four more...
]

for point in sensors:
    x, y = point   # unpack here
    print(...)

x_values = []
for point in sensors:
    x, y = point
    x_values.append(x)

print(f"Minimum x: {min(x_values)}")
print(f"Maximum x: {max(x_values)}")
```

---

Give learners approximately 12–14 minutes of working time. Circulate the room. Watch for:
- learners writing `[x, y]` instead of `(x, y)` for tuples
- learners forgetting to append to `x_values`
- learners trying to do `sensors[0, 1]` instead of `sensors[0][1]`

### 9.3 Walkthrough solution

After working time, say:

**Say:**
"Let's walk through the solution together. I will type it from scratch so you can see the whole picture."

**Type the full solution:**

```python
# hour17_lab_coords.py
# Lab: Coordinate Tracker

# Step 1 — Five sensor positions as (x, y) tuples in a list
sensors: list[tuple[int, int]] = [
    (3, 7),
    (-1, 4),
    (8, 2),
    (0, -5),
    (6, 3),
]

# Step 2 — Print each sensor using tuple unpacking
print("=== Sensor Positions ===")
for point in sensors:
    x, y = point
    print(f"Sensor at x={x}, y={y}")

# Step 3 — Extract all x values
x_values: list[int] = []
for point in sensors:
    x, y = point
    x_values.append(x)

# Step 4 — Compute min and max x
print()
print(f"Minimum x: {min(x_values)}")
print(f"Maximum x: {max(x_values)}")
```

Run it.

**Say:**
"Let's review what we did.

Line by line:

- `sensors` is a **list** because it is a collection that could grow or change. Each item inside it is a **tuple** because each coordinate is a fixed (x, y) record.
- In the first loop, `x, y = point` unpacks each tuple. We then format the output with an f-string.
- We build `x_values` by looping again and appending just the x value from each tuple.
- Finally, we call `min()` and `max()` on `x_values`.

This is a clean and readable program. It makes the structure of the data very clear."

### 9.4 Verify correctness

**Say:**
"Let's check the min and max manually. My x values are 3, -1, 8, 0, 6. The smallest is -1. The largest is 8. Python agrees. If your numbers are different, double-check your tuple values and your append loop."

### 9.5 Discuss design decisions

**Say:**
"Why did we put the sensors in a list rather than five separate variables?

Because we want to iterate over them. If they were five separate variables, we could not write a for loop.

Why is each sensor a tuple rather than a list?

Because a coordinate is a fixed pair. It is a record, not something that grows. Using a tuple communicates that clearly and protects the data.

This pattern — a list of tuples — is one you will use many times in real Python programs."

---

## 10) Common Pitfalls

### 10.1 The single-element tuple trap (revisited)

**Say:**
"We saw this earlier, but it is worth repeating because it is so common.

If you write `value = (42)`, you get an integer, not a tuple. Python reads the parentheses as a math grouping expression.

To make a single-element tuple, you must add a trailing comma: `value = (42,)`.

Here is a quick test to build the reflex:"

**Type:**

```python
a = (5)
b = (5,)
print(type(a))   # <class 'int'>
print(type(b))   # <class 'tuple'>
```

Run it.

**Say:**
"The comma is what makes the tuple. Remember: comma first, parentheses optional."

**Pause.**

"Actually — here is a surprising fact you can verify. The parentheses in a tuple literal are technically optional in most contexts. What makes something a tuple is the commas, not the parentheses."

**Type:**

```python
point = 3, 7      # no parentheses!
print(point)
print(type(point))
```

Run it.

**Say:**
"Python sees `3, 7` as a tuple without parentheses. However, using parentheses is strongly preferred because it makes the intent explicit and the code easier to read. Always write `(3, 7)` in practice. But understanding that the comma is the mechanism helps when you are puzzled by a bug."

### 10.2 Trying to modify a tuple

**Say:**
"The second pitfall is trying to use list-style mutation on a tuple. These all fail with a `TypeError`:"

**Type (but pause before running each):**

```python
coords = (3, 7)

# All of these raise errors:
coords[0] = 10          # TypeError: does not support item assignment
coords.append(5)        # AttributeError: 'tuple' has no attribute 'append'
coords.remove(3)        # AttributeError: 'tuple' has no attribute 'remove'
```

**Say:**
"Do not run all three at once — Python stops at the first error. Run each one individually to read its message.

The key diagnosis: if you see a `TypeError` about item assignment or an `AttributeError` about a missing method like `append`, ask yourself whether you accidentally used a tuple where you meant a list."

### 10.3 Over-parenthesising and confusing tuples with grouped expressions

**Say:**
"A related trap is over-parenthesising and thinking you have a tuple when you do not.

For example:"

**Type:**

```python
result = (10 + 5)
print(type(result))   # int, not tuple!
```

**Say:**
"This is just arithmetic in parentheses. Python evaluates `10 + 5` and assigns the integer `15`.

If you meant a tuple, you need the comma: `result = (15,)`.

The rule is simple: parentheses alone do not make a tuple. Commas make a tuple."

### 10.4 Unpack count mismatch

**Say:**
"One more pitfall: forgetting to match the number of variables to the size of the tuple during unpacking."

**Type:**

```python
point = (3, 7, 5)      # three values
x, y = point           # only two variables on the left
```

**Say:**
"This raises `ValueError: too many values to unpack`. Python expected to assign three values but only found two slots.

The fix is simple: match the count, or use `_` to discard values you do not need."

---

## 11) Optional Extension: Distance from Origin

> **Instructor note:** Offer this only if learners finish the lab early and there is time remaining. This stays within Basics scope — we only use the `math` module's `sqrt` function and the exponentiation operator `**`. Do not introduce complex math or trigonometry.

**Say:**
"If you have finished the lab and want a stretch challenge, here it is.

For each sensor in your coordinate tracker, calculate the distance from the origin `(0, 0)`.

The formula is the Pythagorean theorem: distance = √(x² + y²)

In Python, that is `(x**2 + y**2) ** 0.5`, or you can use `math.sqrt(x**2 + y**2)` after `import math`.

Try adding a line to your loop that prints the distance for each sensor."

**Full extension solution:**

```python
import math

sensors: list[tuple[int, int]] = [
    (3, 7),
    (-1, 4),
    (8, 2),
    (0, -5),
    (6, 3),
]

print("=== Sensor Positions and Distances from Origin ===")
for point in sensors:
    x, y = point
    distance = math.sqrt(x**2 + y**2)
    print(f"Sensor at x={x}, y={y}  |  Distance from origin: {distance:.2f}")
```

Run it.

**Say:**
"The `:.2f` in the f-string rounds the distance to two decimal places.

`math.sqrt()` returns a float. For a point like `(3, 7)`, the distance is `√(9 + 49)` = `√58` ≈ `7.62`.

This is a taste of how tuples connect naturally to geometric calculations in real programs."

---

## 12) Debrief, Recap, and Exit Ticket

### 12.1 Recap the key ideas

**Say:**
"We covered a lot of ground in one hour. Let me recap the five most important things to take away.

**First:** A tuple is an ordered, immutable collection. You create it with parentheses and commas: `(3, 7)`.

**Second:** Immutability is a feature, not a limitation. It tells other programmers — and Python itself — that these values are not meant to change. If you try to change them, Python raises a `TypeError` immediately.

**Third:** Tuple unpacking lets you assign the values of a tuple to named variables in one clean line: `x, y = point`. This is one of Python's most readable patterns.

**Fourth:** The single-element tuple trap: `(42)` is an int, `(42,)` is a tuple. The comma is what matters.

**Fifth:** Use a tuple when your data is a fixed record with known parts. Use a list when your collection grows and changes. A list of tuples — like our sensor list — is a natural and common combination."

### 12.2 Connections to what comes next

**Say:**
"In the next hours, we will see tuples appear again when we work with dictionaries — specifically, when we iterate over a dictionary's key-value pairs, we will unpack them as two-element tuples. So the unpacking pattern you just practised will keep paying off.

You will also see tuples appear naturally when functions return multiple results. Returning a tuple is the idiomatic Python way to 'return two things at once'."

### 12.3 Exit ticket

**Say:**
"Before we close, I want to give you one question to think about — either discuss it with a neighbour or just reflect for thirty seconds.

Here is the question:

**Why might you choose a tuple over a list?**

Think about what you have learned this hour. Name at least two reasons."

Give learners 60 seconds to think or discuss briefly, then collect a few answers.

**Good answers to listen for:**
- "Because the data should not change — immutability protects it."
- "Because the collection represents a fixed record with a known structure."
- "Because it communicates intent — a reader knows the values are fixed."
- "Because it is slightly more memory-efficient than a list for the same data." *(accept this if offered; do not prioritise it)*

**Say:**
"Those are excellent reasons. The most important one, in my view, is intent and communication. Tuples are a design choice. When you write a tuple, you are making a statement: 'these values belong together and they are not meant to change'. That kind of clarity makes programs easier to understand, maintain, and trust."

### 12.4 Final thought

**Say:**
"Congratulations on completing Hour 17. You have added a new data structure to your toolbox, and — more importantly — you have started thinking about *why* to choose one data structure over another. That kind of thinking is what separates someone who knows Python syntax from someone who writes good Python programs.

See you in Hour 18."

---

## Appendix A: Complete Demo File

```python
# hour17_tuples_demo.py
# Day 5, Hour 1 — Tuples + Unpacking

# --- Part 1: Create and read coordinate tuples ---
origin = (0, 0)
home = (3, 7)
destination = (-2, 5)

print(f"Origin:      {origin}")
print(f"Home:        {home}")
print(f"Destination: {destination}")

# --- Part 2: Unpack and use the values ---
x, y = home
print(f"Home x-coordinate: {x}")
print(f"Home y-coordinate: {y}")

# --- Part 3: Immutability (deliberate error — comment out before lab) ---
# home[0] = 10  # TypeError: 'tuple' object does not support item assignment

# --- Part 4: Function returning a tuple ---
def get_midpoint(
    point_a: tuple[int, int],
    point_b: tuple[int, int],
) -> tuple[float, float]:
    """Return the midpoint between two (x, y) coordinates."""
    mid_x = (point_a[0] + point_b[0]) / 2
    mid_y = (point_a[1] + point_b[1]) / 2
    return (mid_x, mid_y)


result = get_midpoint(home, destination)
print(f"Midpoint: {result}")

mid_x, mid_y = get_midpoint(home, destination)
print(f"Mid x = {mid_x}, Mid y = {mid_y}")

# --- Part 5: A list of coordinate tuples ---
path = [
    (0, 0),
    (1, 3),
    (4, 2),
    (6, 8),
    (5, 1),
]

print("\nPath coordinates:")
for point in path:
    x, y = point
    print(f"  x={x}, y={y}")
```

---

## Appendix B: Complete Lab Solution

```python
# hour17_lab_coords.py
# Lab: Coordinate Tracker

# Step 1 — Five sensor positions as (x, y) tuples in a list
sensors: list[tuple[int, int]] = [
    (3, 7),
    (-1, 4),
    (8, 2),
    (0, -5),
    (6, 3),
]

# Step 2 — Print each sensor using tuple unpacking
print("=== Sensor Positions ===")
for point in sensors:
    x, y = point
    print(f"Sensor at x={x}, y={y}")

# Step 3 — Extract all x values into a separate list
x_values: list[int] = []
for point in sensors:
    x, y = point
    x_values.append(x)

# Step 4 — Compute and display min and max x
print()
print(f"Minimum x: {min(x_values)}")
print(f"Maximum x: {max(x_values)}")
```

---

## Appendix C: Optional Extension Solution

```python
# hour17_lab_coords_extension.py
# Lab Extension: Distance from Origin
import math

sensors: list[tuple[int, int]] = [
    (3, 7),
    (-1, 4),
    (8, 2),
    (0, -5),
    (6, 3),
]

print("=== Sensor Positions and Distances from Origin ===")
for point in sensors:
    x, y = point
    distance = math.sqrt(x**2 + y**2)
    print(f"Sensor at x={x}, y={y}  |  Distance from origin: {distance:.2f}")

x_values: list[int] = []
for point in sensors:
    x, _ = point
    x_values.append(x)

print()
print(f"Minimum x: {min(x_values)}")
print(f"Maximum x: {max(x_values)}")
```

---

## Appendix D: Quick-Reference Card (share with learners)

| Concept | Syntax | Example |
|---|---|---|
| Create a tuple | `name = (val1, val2)` | `point = (3, 7)` |
| Single-element tuple | `name = (val,)` | `solo = (42,)` |
| Access by index | `name[i]` | `point[0]` → `3` |
| Unpack two values | `a, b = name` | `x, y = point` |
| Unpack, ignore one | `a, _ = name` | `val, _ = measurement` |
| Swap two variables | `a, b = b, a` | `x, y = y, x` |
| Check membership | `val in name` | `3 in point` → `True` |
| Iterate over tuple | `for v in name:` | `for v in point:` |
| List of tuples | `[(...), (...)]` | `[(0,0),(1,3)]` |
| Immutability error | attempt `name[i] = v` | `TypeError` |
