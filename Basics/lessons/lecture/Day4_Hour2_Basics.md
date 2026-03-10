# Day 4, Hour 2: Iterating Lists with `for` Loops (Course Hour 14)
**Python Programming Basics – Session 4**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 4, Course Hour 14 – Iterating lists with `for` loops (gentle intro)  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This hour should feel calm, concrete, and repetitive in a good way. The goal is not to teach every loop feature. The goal is to help beginners understand `for item in items:` in plain English, use a running total, compute an average, and find the highest grade in a list. Stay tightly aligned to the Session 4 runbook.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

“By the end of this hour, you will be able to:
1. Explain what `for item in items:` means in everyday language.
2. Loop through a list and perform an action for each item.
3. Use an accumulator variable to keep a running total.
4. Compute an average from values stored in a list.
5. Find the highest grade in a list using a beginner-friendly approach.
6. Build a grade-average program that asks for 5 numeric grades, stores them in a list, and reports the average and highest grade.

This hour is where lists become active. Last hour, we learned how to store values together. This hour, we learn how to process those values one by one.”

---

## 1) Agenda + Timing (show slide / read quickly, ~2 minutes)

- **0:00–0:05** Recap of lists and transition into loops
- **0:05–0:15** Why loops matter when a list has many items
- **0:15–0:25** Read `for item in items:` in plain English
- **0:25–0:35** Accumulator pattern: totals and averages
- **0:35–0:45** Live demo: sum numbers and compute average
- **0:45–0:57** Guided lab: grade average + highest grade
- **0:57–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist (before class)

- Open a clean file such as `hour14_for_loops_lists.py`.
- Prepare a short list like `[10, 20, 30, 40]` for the first demo.
- Prepare five sample grades, such as `88`, `92`, `76`, `95`, and `84`.
- Be ready to show one deliberate mistake: forgetting to convert `input()` to numbers.
- Be ready to show a second deliberate mistake: dividing by the wrong count.
- Keep the examples numeric and simple. This is a gentle intro, not an advanced looping lesson.

**Say:** “Today we are learning how to let Python repeat a simple action for each item in a list. That is one of the most useful beginner patterns in the language.”

---

## 3) Opening Script: Connect Lists to Loops (~5 minutes)

### 3.1 Review the storage idea from Hour 13

**Say:**
“In the previous hour, we learned how to create lists, change lists, and check whether an item is present. That was the storage side of the story.

But think about what happens next in real programs. If I have five grades in a list, I probably want to do something with all five grades. I might want to print them. I might want to total them. I might want to calculate an average. I might want to find the highest one.

That is where loops matter.”

### 3.2 Show the problem with repetition

**Type:**

```python
grades = [88, 92, 76, 95, 84]

print(grades[0])
print(grades[1])
print(grades[2])
print(grades[3])
print(grades[4])
```

**Say:**
“This works for exactly five grades. But it is repetitive, and it breaks down quickly if the list grows or changes.

If I had 100 grades, I would not want 100 print lines.
If I had 1,000 values, I definitely would not want 1,000 print lines.

So we need a tool that says: do the same action for each item in the list.”

### 3.3 Frame the new pattern

**Say:**
“That tool is the `for` loop.

A `for` loop is one of the cleanest ways to move through the items of a list.

You do not need to know advanced loop theory today. You just need this mental model:

‘For each item in this list, do these indented steps.’”

**Ask learners:**
- “If a list changes from 5 items to 50 items, would you rather rewrite 50 lines or use one loop?”
- “Why might repeated code be harder to manage?”

Guide them toward efficiency and readability.

---

## 4) Core Concept Delivery: Reading `for item in items:` (~10 minutes)

### 4.1 The basic pattern

**Type:**

```python
colors = ["red", "blue", "green"]

for color in colors:
    print(color)
```

Run it.

**Say:**
“Read this line out loud as:
‘For each color in colors, print color.’

That plain-English reading is important. If learners can read it out loud, they usually understand it much better.”

### 4.2 Explain the loop variable simply

**Say:**
“`color` is a temporary name for the current item.
On the first pass, `color` is `red`.
On the second pass, `color` is `blue`.
On the third pass, `color` is `green`.

Python is taking one item at a time from the list and placing it into the loop variable.”

### 4.3 Emphasize indentation

**Say:**
“The indented line belongs to the loop. That means Python repeats that indented action once for each item.

If the indentation is wrong, the loop does not behave the way you expect. Indentation is not decoration in Python. It changes meaning.”

### 4.4 Ask for prediction

**Ask learners:**
- “How many times will `print(color)` run?”
- “What do you think prints first?”
- “What do you think prints last?”

### 4.5 Show another simple example

**Type:**

```python
shopping_items = ["milk", "bread", "eggs"]

for item in shopping_items:
    print(f"Need to buy: {item}")
```

**Say:**
“This demonstrates something important: the loop pattern is the same even when the action changes. We are still going through each item in the list, but now we are printing a sentence instead of just the raw item.”

### 4.6 Clarify what the loop gives you

**Say:**
“A very important beginner point: `for x in my_list` gives you each item, not the position number.

At this stage, that is perfect. We want the values themselves.
Later, you will learn more patterns, but right now this one is enough.”

---

## 5) Accumulator Pattern: Running Totals and Averages (~10 minutes)

### 5.1 Motivation

**Say:**
“If a loop can visit every number in a list, then we can build totals by adding those numbers one by one.

This brings us to one of the most useful loop ideas in beginner programming: the accumulator.”

### 5.2 Define accumulator in plain language

**Say:**
“An accumulator is a variable that starts with an initial value and changes as the loop runs.

For totals, we usually start at zero.”

### 5.3 Demonstrate running total

**Type:**

```python
numbers = [10, 20, 30, 40]
total = 0

for number in numbers:
    total = total + number
    print(f"Added {number}, total is now {total}")

print(f"Final total: {total}")
```

Run it.

**Say:**
“Watch the total grow.
It starts at `0`.
Then it becomes `10`.
Then `30`.
Then `60`.
Then `100`.

This is a strong beginner pattern because the state changes in a way you can follow.”

### 5.4 Show shorthand but explain gently

**Type:**

```python
numbers = [10, 20, 30, 40]
total = 0

for number in numbers:
    total += number

print(total)
```

**Say:**
“`total += number` is shorthand for `total = total + number`.

If learners are brand new, say both versions are acceptable. Clarity matters more than shorthand.”

### 5.5 Move from total to average

**Say:**
“An average is just a total divided by how many values you have.”

**Type:**

```python
numbers = [10, 20, 30, 40]
total = 0

for number in numbers:
    total += number

average = total / len(numbers)
print(f"Average: {average}")
```

**Say:**
“Notice the structure:
1. build the total
2. divide by the count

The count comes from `len(numbers)`.”

### 5.6 Stress the count issue

**Say:**
“One of today’s biggest pitfalls is dividing by the wrong count. If you have five grades, divide by 5. If you use `len(grades)`, Python computes that count for you, which is safer and clearer.”

### 5.7 Briefly introduce highest grade

**Say:**
“The runbook also asks us to report the highest grade. There are two beginner-friendly ways to think about that:
- use `max(grades)` once the list is built
- or compare values manually in a loop

For a gentle intro, it is perfectly fine to use `max(grades)` in the lab. I will also show you the manual logic so you can see how a loop can track the biggest value.”

**Type:**

```python
grades = [88, 92, 76, 95, 84]
highest = grades[0]

for grade in grades:
    if grade > highest:
        highest = grade

print(f"Highest grade: {highest}")
```

**Say:**
“Even if we do not make this the center of the hour, it is good for learners to see the logic.
We start with the first grade as the current highest.
Then we walk through the list.
If we find something larger, we update `highest`.”

---

## 6) Live Demo: Sum Numbers in a List and Compute Average (~10 minutes)

### 6.1 Frame the demo

**Say:**
“I am going to solve a small problem from start to finish. I have a list of numbers. I want to total them and compute an average. Then I will adapt the same pattern to grades.”

### 6.2 Demo code, part 1: print each number

**Type:**

```python
numbers = [12, 18, 25, 30]

for number in numbers:
    print(number)
```

**Say:**
“Start simple. Before we calculate anything, make sure the loop is visiting the values we expect.”

### 6.3 Demo code, part 2: build the total

**Type:**

```python
numbers = [12, 18, 25, 30]
total = 0

for number in numbers:
    total += number
    print(f"After adding {number}, total = {total}")

print(f"Final total = {total}")
```

Run it.

**Say:**
“This is a strong teaching move: print inside the loop while learners are still new. It helps them see the running total instead of treating the result like magic.”

### 6.4 Demo code, part 3: compute average

**Type:**

```python
average = total / len(numbers)
print(f"Average = {average}")
```

**Say:**
“Now the average is easy because the total is already prepared.”

### 6.5 Demo code, part 4: adapt to grades

**Type:**

```python
grades = [88, 92, 76, 95, 84]
total = 0

for grade in grades:
    total += grade

average = total / len(grades)
highest = max(grades)

print(f"Grades: {grades}")
print(f"Average grade: {average}")
print(f"Highest grade: {highest}")
```

**Say:**
“Notice what stayed the same:
- a list of values
- a loop through the list
- a total that starts at zero
- an average that uses total divided by count

The exact values changed, but the pattern stayed the same. That is what makes loops powerful.”

### 6.6 Ask learners to narrate the logic back

**Ask learners:**
- “Why does `total` start at zero?”
- “What does the loop add each time?”
- “Where does the average come from?”
- “What does `max(grades)` return?”

---

## 7) Guided Lab: Grade Average (~12 minutes)

### 7.1 Introduce the task clearly

**Say:**
“Now you will build the lab from the runbook.

Your program should:
1. Ask the user for 5 numeric grades.
2. Store them in a list.
3. Compute the average.
4. Report the highest grade.
5. Print the results clearly.”

### 7.2 Put the runbook-aligned lab prompt on screen

```text
Lab: Grade Average
- Ask for 5 numeric grades.
- Store them in a list.
- Compute average and highest grade.
- Print results with formatting.
```

### 7.3 Provide a beginner-friendly starter

**Type:**

```python
grades = []

grade = float(input("Enter grade 1: "))
grades.append(grade)

grade = float(input("Enter grade 2: "))
grades.append(grade)

grade = float(input("Enter grade 3: "))
grades.append(grade)

grade = float(input("Enter grade 4: "))
grades.append(grade)

grade = float(input("Enter grade 5: "))
grades.append(grade)

total = 0

for grade in grades:
    total += grade

average = total / len(grades)
highest = max(grades)

print(f"Grades entered: {grades}")
print(f"Average grade: {average}")
print(f"Highest grade: {highest}")
```

### 7.4 Explain the design choice

**Say:**
“Yes, we could eventually use a loop to collect the five inputs too, but that is not today’s teaching target. Today’s teaching target is iterating through the finished list with a `for` loop.

So we will keep input collection simple and make the list-processing part the star of the lesson.”

### 7.5 Challenge questions during circulation

Ask learners:
- “Where do you convert the input to a number?”
- “Where does the running total begin?”
- “What does the loop variable represent each time?”
- “What happens if you accidentally divide by 4 instead of 5?”
- “How are you finding the highest grade?”

### 7.6 Encourage output checks

**Say:**
“Always test with values where you can estimate the answer. If you enter `80`, `80`, `80`, `80`, `80`, the average should clearly be `80`. Use simple test data to build confidence.”

### 7.7 Optional extension for early finishers

If time permits, offer:
- drop the lowest grade using `min(grades)` and a modified total
- print a message like `Great job!` if the average is 90 or above
- count how many grades are above 80 using another loop variable such as `count_above_80`

Make it clear these are optional and still within Basics scope.

---

## 8) Common Pitfalls and Coaching Moves (~6 minutes)

### 8.1 Pitfall: forgetting numeric conversion

**Symptom:** grades are stored as strings, and math does not work as expected.

**Say:**
“This is one of today’s most important mistakes to catch. `input()` returns text. If we want math, we must convert the input to `int` or `float`.”

Show:

```python
grade = float(input("Enter grade 1: "))
```

Then say:

“If a learner forgets this step, do not just fix it for them. Ask: ‘What type does `input()` return?’ That question helps them reconnect to earlier lessons.”

### 8.2 Pitfall: dividing by the wrong count

**Say:**
“Beginners sometimes hard-code the divisor incorrectly. A safer pattern is `len(grades)` because it always matches the list length.”

### 8.3 Pitfall: resetting the total inside the loop

**Say:**
“If `total = 0` is placed inside the loop, the total restarts every time. Ask learners: ‘Should this happen once before the loop, or again and again during the loop?’”

### 8.4 Pitfall: indentation mistakes

**Say:**
“If only one line belongs to the loop but the learner intended two, or vice versa, the result will look strange. Have them point to the exact indented block and say out loud what repeats.”

### 8.5 Pitfall: misunderstanding what `for grade in grades` gives you

**Say:**
“At this stage, the loop gives you each grade value, not the position. If a learner wants the value itself, the pattern is correct. Remind them to focus on the item.”

---

## 9) Debrief and Share-Out (~4 minutes)

### 9.1 Bring learners back together

**Say:**
“Let’s compare approaches. Even if your formatting is different, the core logic should be similar.”

### 9.2 Invite short reflections

Ask:
- “Who can read `for grade in grades:` out loud in plain English?”
- “Who can explain why `total` starts at zero?”
- “Who used `max(grades)` for the highest grade?”
- “Who tested with easy values to verify the average?”

### 9.3 Model the summary of the pattern

**Say:**
“A strong summary sounds like this:
‘I stored the grades in a list, used a `for` loop to add them into a running total, divided by the number of grades to get the average, and reported the highest value.’

That sentence captures the logic of the hour.”

---

## 10) Recap Script (~2 minutes)

**Say:**
“Today we learned how to process list items with a `for` loop.

We learned that:
- `for item in items:` means do something once for each item
- the loop variable is a temporary name for the current item
- an accumulator is a variable that keeps a running result
- totals often start at zero
- averages come from total divided by count
- `len()` gives the count
- `max()` can help report the highest value in a list

This is one of the first patterns that makes beginner code feel efficient instead of repetitive.”

---

## 11) Exit Ticket (~1 minute)

Ask learners to answer verbally, in chat, or on paper:

1. In plain English, what does `for grade in grades:` mean?
2. Why does an accumulator like `total` usually start at `0`?
3. If your list has five grades, what should you divide by to compute the average?
4. What problem happens if you forget to convert `input()` to a number?

**Expected direction of answers:**
- the loop visits each grade in the list one at a time
- total starts at zero because nothing has been added yet
- divide by the number of items, often using `len(grades)`
- the data stays as strings, so math is incorrect or fails

---

## 12) Instructor Notes for the Transition to Hour 15

**Say:**
“So far our lists have been one-dimensional: one item after another in a single row. In the next hour, we will change the shape of the data. We will build a list where each item is itself another list. That will let us model table-like data such as a seating chart.”

Reinforce this final line before transition:

“Store values in a list, then let the loop visit each one.”

---

## Appendix: Instructor Reinforcement Notes for Hour 14

### A) A second spoken walkthrough of the loop pattern

If the room still feels unsure about loops, slow everything down and read the code almost like a story.

Use this example:

```python
numbers = [5, 10, 15]
total = 0

for number in numbers:
    total += number
    print(f"Added {number}, total is now {total}")
```

Then say:

“On the first pass, `number` is `5`, so `total` becomes `5`.
On the second pass, `number` is `10`, so `total` becomes `15`.
On the third pass, `number` is `15`, so `total` becomes `30`.
Then the loop stops because there are no more items.

That is the whole shape of the pattern.
The loop variable changes.
The accumulator grows.
The indented code repeats.”

This kind of slow narration often helps learners who feel that loops are ‘magic.’

### B) Extra board drills for running totals

Write these on the board and ask learners to answer before you run anything.

**Drill 1**

```python
scores = [2, 4, 6]
total = 0

for score in scores:
    total += score
```

Ask:
- “What is `total` after the first pass?”
- “What is `total` after the second pass?”
- “What is `total` at the end?”

**Drill 2**

```python
scores = [10, 20, 30, 40]
average = sum(scores) / len(scores)
```

Ask:
- “What does `len(scores)` represent?”
- “Why would dividing by `3` be wrong here?”

**Drill 3**

```python
grades = [91, 84, 88, 97]
print(max(grades))
```

Ask:
- “What should print?”
- “Why is `max()` useful after the list is built?”

These drills reinforce the exact runbook outcomes: processing list items, totals, averages, and highest value.

### C) Common learner questions and ready responses

**Question:** “Why do I need a loop if there are only five grades?”

**Suggested response:**
“Because the loop teaches a pattern that works even if the number of grades changes later. Good habits in programming are about patterns that scale.”

**Question:** “Why can’t I just add them manually?”

**Suggested response:**
“You can for a tiny one-time script, but the loop is clearer, more reusable, and less error-prone once the list grows.”

**Question:** “Why is my average incorrect?”

**Suggested response:**
“Check three things in order:
1. Are the values numbers or strings?
2. Did your total start at zero before the loop?
3. Did you divide by the correct count?”

**Question:** “Do I have to use `max()`?”

**Suggested response:**
“No. `max()` is a convenient built-in. The manual comparison pattern is also valid. The key thing is understanding what the program is trying to compute.”

### D) A short manual-highest walkthrough for learners who are curious

If a learner wants to understand highest-value logic more deeply, use this small example:

```python
grades = [88, 92, 76, 95, 84]
highest = grades[0]

for grade in grades:
    if grade > highest:
        highest = grade

print(highest)
```

Talk it through like this:

“Start by assuming the first grade is the highest.
Now compare every grade to that current highest value.
If a new grade is larger, replace `highest`.
At the end, `highest` stores the biggest grade we saw.”

This is useful because it connects looping to comparison logic without turning the hour into an advanced topic.

### E) Suggested instructor reminders during the lab

While circulating, you can repeat these prompts:

- “Show me where the list of grades is stored.”
- “Show me where the total begins.”
- “What value is the loop variable holding on each pass?”
- “How are you making sure the average uses the right count?”
- “How are you finding the highest grade?”

These keep the learner’s attention on the exact target of the hour.

### F) Optional mini-debrief if learners finish early

If several learners finish early, ask them to write or say a three-sentence explanation:

1. One sentence explaining what `for grade in grades:` means.
2. One sentence explaining what an accumulator is.
3. One sentence explaining how average is calculated.

This quick reflection helps turn pattern-following into understanding.

### G) Extra end-of-hour review prompts

If you want one more short review cycle before transitioning to nested lists, ask learners to respond to these prompts in one sentence each:

- “What does the loop variable represent during a `for` loop?”
- “Why does the running total start at zero?”
- “Why is `len(grades)` safer than guessing the count?”
- “What mistake happens if the grades stay as strings?”
- “What is one reason loops are better than repeated lines of code?”

Then summarize with this read-aloud statement:

“A `for` loop helps us process every item in a list. An accumulator keeps a running result. An average comes from total divided by count. These three ideas work together.”

### H) Short instructor script for a final confidence boost

You can close the hour with these exact words if learners still seem cautious:

“Do not worry if loops still feel a little new. That is normal. At the beginning, the pattern can feel mechanical. That is okay.

What matters is that you can now read the loop in plain English, trace what happens on each pass, and use it to solve a real beginner problem with totals and averages.

That is real progress, and it is enough for this hour.”

### I) Mini whiteboard exercise for last-minute reinforcement

Write this on the board:

```python
values = [3, 6, 9, 12]
total = 0

for value in values:
    total += value

average = total / len(values)
```

Then ask learners to talk through it without running it:

- “What is the list storing?”
- “What does `value` represent each time?”
- “What is the final total?”
- “What is the average?”

After a few responses, say:

“This tiny example contains the whole pattern of the hour. Store values in a list, visit each value with a loop, build a total, then divide by the count. If you understand this pattern, you are on solid ground.”

### J) Closing teaching sentence to repeat aloud

If you want one sentence learners can carry into the next session, use this:

“A list stores many values together, and a `for` loop helps us process those values one by one.”

That sentence is short, but it captures the exact bridge from Hour 13 into Hour 14 and prepares learners for later list work.

One final reminder for learners: loops become easier through tracing. If a learner can point to each value as the loop visits it and explain how the total changes, they are understanding the core pattern of the hour.

That ability to trace the loop, explain the accumulator, and connect the average back to total divided by count is exactly the kind of understanding this hour is designed to build.
