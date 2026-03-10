# Day 4, Hour 3: Nested Lists for Table-Like Data (Course Hour 15)
**Python Programming Basics – Session 4**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 4, Course Hour 15 – Nested lists (table-like data)  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** Keep this hour concrete, visual, and small in scale. Avoid abstract data-structure language beyond what beginners need. A nested list should be taught as a list of rows, where each row is another list. The main goal is to help learners read and update simple 2D data, especially a 3x3 seating chart.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

“By the end of this hour, you will be able to:
1. Explain what a nested list is in simple language.
2. Represent small table-like data using a list of lists.
3. Access values using row and column positions.
4. Print each row of a nested list.
5. Update one value inside a 3x3 seating chart.
6. Avoid two common mistakes: mixing up row and column positions, and using an index that is out of range.

The purpose of this hour is not to make you experts in complex data structures. The purpose is to make table-like data feel understandable.”

---

## 1) Agenda + Timing (show slide / read quickly, ~2 minutes)

- **0:00–0:05** Review of single-row lists and why some data needs rows and columns
- **0:05–0:15** What a nested list is and how to picture it
- **0:15–0:25** Accessing rows, then individual cells by row and column
- **0:25–0:35** Live demo: 3x3 seating chart create, print, update
- **0:35–0:52** Guided lab: seating chart with one seat changed to `"X"`
- **0:52–0:58** Debrief and common mistakes
- **0:58–1:00** Recap and exit ticket

---

## 2) Instructor Setup Checklist (before class)

- Open a clean file such as `hour15_nested_lists.py`.
- Prepare a visual 3x3 grid on a whiteboard, slide, or shared screen.
- Have a seating-chart example ready with obvious labels such as `A1`, `A2`, `A3`.
- Plan to stay small. Use 3 rows and 3 columns throughout most of the hour.
- Be ready to show one deliberate indexing mistake so learners can practice reading it.
- Be ready to mention `IndexError` lightly without drifting into a full exceptions lesson.

**Say:** “Today we are still working with lists, but the shape changes. Instead of one row of values, we will build rows inside a larger list.”

---

## 3) Opening Script: From One-Dimensional Lists to Table-Like Data (~5 minutes)

### 3.1 Connect to Hour 14

**Say:**
“In the previous hour, we used one list of grades and processed the values one after another with a `for` loop. That worked well because the data naturally lived in a single row.

But not all data feels like a single row.
Some data is easier to understand when we picture rows and columns.”

### 3.2 Give relatable examples

**Say:**
“Think about these examples:
- a classroom seating chart
- a spreadsheet with rows and columns
- a tic-tac-toe board
- a simple weekly schedule
- a small grid of values on a screen

In each case, the data has a table-like feel. We care about both the row and the column.”

### 3.3 Explain why one flat list is not ideal

**Say:**
“If I store a seating chart in one long list, I can still keep the values, but the shape becomes harder to see.

For example, this is a valid list:”

```python
seats = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
```

**Say:**
“But the visual structure is hidden.
If I want to think in terms of rows, it is often clearer to store rows directly.”

### 3.4 Introduce the mental model

**Say:**
“A nested list is simply a list where each item is itself another list.

The beginner-friendly mental model is:
- the outer list holds the rows
- each inner list holds the values in that row

Do not let the phrase ‘nested list’ scare you. It is just layers: a list containing smaller lists.”

**Ask learners:**
- “If the outer list holds rows, what does an inner list hold?”
- “If I want the second seat in the first row, what two positions do I need?”

Guide them toward: row first, then column.

---

## 4) Core Concept Delivery: What Nested Lists Look Like (~10 minutes)

### 4.1 First example

**Type:**

```python
seating_chart = [
    ["A1", "A2", "A3"],
    ["B1", "B2", "B3"],
    ["C1", "C2", "C3"]
]

print(seating_chart)
```

Run it.

**Say:**
“This is a list of lists.
The outer list contains three inner lists.
Each inner list represents one row.”

### 4.2 Read the structure aloud

**Say:**
“Let’s read it carefully.
- Row 0 is `["A1", "A2", "A3"]`
- Row 1 is `["B1", "B2", "B3"]`
- Row 2 is `["C1", "C2", "C3"]`

That means the first index chooses the row.”

### 4.3 Access a whole row

**Type:**

```python
print(seating_chart[0])
print(seating_chart[1])
```

**Say:**
“These statements return whole rows.
The first index tells Python which inner list to retrieve.”

### 4.4 Access an individual value

**Type:**

```python
print(seating_chart[0][0])
print(seating_chart[1][2])
print(seating_chart[2][1])
```

**Say:**
“Now we are using two indexes.
- The first index chooses the row.
- The second index chooses the position within that row.

So `seating_chart[1][2]` means:
- row 1 first
- then item 2 inside that row”

### 4.5 Slow down and visualize

At this point, point to the grid on the board and say:

“Match the code to the picture.
If I say row 0, column 2, we land on the first row, third value.
If I say row 2, column 1, we land on the third row, second value.

The code feels much easier once the picture is clear.”

### 4.6 Ask prediction questions

**Ask learners:**
- “What do you think `seating_chart[0][1]` returns?”
- “What do you think `seating_chart[2][2]` returns?”
- “Which part chooses the row?”
- “Which part chooses the column?”

### 4.7 Clarify the term ‘column’ without overcomplicating it

**Say:**
“Strictly speaking, Python is not storing columns as a separate structure here. We are simply using the second position inside a row. But for beginners, it is fine to think of that second position as the column.”

---

## 5) Printing Rows Clearly (~7 minutes)

### 5.1 Why printing the whole nested list is not always ideal

**Say:**
“When we print the entire nested list, Python shows the whole structure on one screenful. That is useful, but not always easy to read.

For table-like data, it is often clearer to print one row at a time.”

### 5.2 Use a `for` loop over rows

**Type:**

```python
for row in seating_chart:
    print(row)
```

Run it.

**Say:**
“This is a very natural pattern.
The outer list contains rows, so the loop variable `row` becomes one inner list at a time.”

### 5.3 Ask learners to narrate it

**Ask learners:**
“How would you read `for row in seating_chart:` in plain English?”

Guide them to:
“For each row in the seating chart, print the row.”

### 5.4 Connect to prior learning

**Say:**
“Notice how this builds directly on the last hour.
Hour 14 taught us how to loop over a list.
Now we are looping over the outer list, and each item happens to be another list.”

### 5.5 Optional readability step

If you want a slightly clearer display, type:

```python
for row in seating_chart:
    print(" ".join(row))
```

Then say:

“This prints the seat labels with spaces between them. It is still Basics-friendly because we already worked with string joining earlier in the course.”

If the class seems overloaded, skip this and stay with plain `print(row)`.

---

## 6) Updating a Single Cell (~8 minutes)

### 6.1 Transition

**Say:**
“Once we can access a specific value inside the nested list, we can also update that value. This is one of the main practical goals of today’s hour.”

### 6.2 Demonstrate an update

**Type:**

```python
seating_chart[1][1] = "X"

for row in seating_chart:
    print(row)
```

Run it.

**Say:**
“We changed the middle seat in the second row to `"X"`.
That means a seat is now marked as taken, blocked, reserved, or otherwise changed.

The structure stayed the same.
Only one value inside the structure changed.”

### 6.3 Explain the order again

**Say:**
“This is the place where beginners most often mix up row and column.

Remember:
- first index = row
- second index = column position inside the row”

### 6.4 Deliberate mistake for discussion

**Type:**

```python
# seating_chart[3][0] = "X"
```

**Say:**
“This would fail because row 3 does not exist in a 3-row structure indexed from 0.
The valid row indexes are 0, 1, and 2.

This is the beginning of boundary awareness. The structure has limits.”

### 6.5 Mention `IndexError` lightly

**Say:**
“If a learner sees `IndexError`, the meaning is usually simple: the requested position does not exist.
We do not need a full exception-handling lesson here. We just need to understand the cause.”

---

## 7) Live Demo: Seating Chart Create, Print, Update (~10 minutes)

### 7.1 Frame the demo

**Say:**
“I am now going to build the exact kind of example the runbook calls for: a seating chart. I will create it, print it row by row, ask for a row and column, update one seat to `"X"`, and print it again.”

### 7.2 Demo code, part 1: create and print the chart

**Type:**

```python
seating_chart = [
    ["A1", "A2", "A3"],
    ["B1", "B2", "B3"],
    ["C1", "C2", "C3"]
]

print("Original seating chart:")
for row in seating_chart:
    print(row)
```

Run it.

**Say:**
“This confirms that our data starts in the shape we expect.”

### 7.3 Demo code, part 2: collect row and column

**Type:**

```python
row_index = int(input("Enter row (0, 1, or 2): "))
column_index = int(input("Enter column (0, 1, or 2): "))
```

**Say:**
“We are using numeric positions, not seat names, because the learning target is row and column indexing.”

### 7.4 Demo code, part 3: update the seat

**Type:**

```python
seating_chart[row_index][column_index] = "X"
```

**Say:**
“This is the exact line where the change happens. If the indexes are valid, the selected seat changes to `"X"`.”

### 7.5 Demo code, part 4: reprint the chart

**Type:**

```python
print("Updated seating chart:")
for row in seating_chart:
    print(row)
```

Run the full program with sample inputs like row `1`, column `2`.

### 7.6 Optional safety improvement

If time permits and learners seem ready, show a basic boundary check:

```python
if 0 <= row_index <= 2 and 0 <= column_index <= 2:
    seating_chart[row_index][column_index] = "X"
    print("Updated seating chart:")
    for row in seating_chart:
        print(row)
else:
    print("Row and column must be between 0 and 2.")
```

**Say:**
“This is an optional improvement, not the main teaching target. The main teaching target is understanding the structure and the indexing.”

### 7.7 Ask learners to explain the change

**Ask learners:**
- “Which line selects the row?”
- “Which line selects the column position?”
- “Why do we print the chart again after changing it?”

---

## 8) Guided Lab: 3x3 Seating Chart (~12 minutes)

### 8.1 Introduce the task clearly

**Say:**
“Now it is your turn to build the seating chart lab from the runbook.

Your program should:
1. Create a 3x3 seating chart.
2. Print the rows.
3. Ask the user for a row and a column.
4. Change that seat to `"X"`.
5. Reprint the chart.”

### 8.2 Put the runbook-aligned lab prompt on screen

```text
Lab: Seating Chart
- Create a 3x3 seating chart.
- Print it as rows.
- Ask for row/column and change that seat to "X".
- Reprint the chart.
```

### 8.3 Provide a clear starter

**Type:**

```python
seating_chart = [
    ["A1", "A2", "A3"],
    ["B1", "B2", "B3"],
    ["C1", "C2", "C3"]
]

print("Current seating chart:")
for row in seating_chart:
    print(row)

row_index = int(input("Enter row (0, 1, or 2): "))
column_index = int(input("Enter column (0, 1, or 2): "))

seating_chart[row_index][column_index] = "X"

print("Updated seating chart:")
for row in seating_chart:
    print(row)
```

### 8.4 Explain why this starter is enough

**Say:**
“We are intentionally keeping the chart small and the task focused. The goal is not to build a complete seat-booking system. The goal is to practice reading and updating a nested list.”

### 8.5 Instructor circulation prompts

As learners work, ask:
- “Show me the outer list.”
- “Show me one inner list.”
- “Which part of your code prints each row?”
- “Which index picks the row?”
- “Which index picks the seat inside the row?”
- “What happens if the user enters `2` and `1`?”

### 8.6 Encourage paper sketches

**Say:**
“If a learner is confused, encourage them to draw the 3x3 grid on paper and label the row and column positions. Sometimes the fastest debugging tool is a simple sketch.”

### 8.7 Optional extension for early finishers

Offer these only if time allows:
- validate that the row and column are between 0 and 2 using a basic `if` statement
- replace the seat with a learner’s initials instead of `"X"`
- print rows with spaces between seat labels

Again, keep these optional.

---

## 9) Common Pitfalls and Coaching Moves (~6 minutes)

### 9.1 Pitfall: mixing up row and column

**Say:**
“This is the signature mistake of the hour. Learners often know they need two indexes but forget the order.

Coach with this phrase:
‘First pick the row. Then pick the item inside that row.’”

You can also point physically to the grid and say:
- move down to choose the row
- move across to choose the column position

### 9.2 Pitfall: out-of-range indexes

**Say:**
“In a 3x3 chart, the valid indexes are `0`, `1`, and `2`. If the learner enters `3`, there is no fourth row or fourth column position.

That leads to `IndexError`.”

### 9.3 Pitfall: printing the whole chart but forgetting to reprint after the update

**Say:**
“A learner may correctly change the data but forget the final display step. Remind them: if the user cannot see the result, the program feels unfinished.”

### 9.4 Pitfall: misunderstanding what the loop prints

**Say:**
“When we write `for row in seating_chart:`, each `row` is itself a list. That is why printing `row` shows one row at a time.”

### 9.5 Pitfall: confusing labels with indexes

**Say:**
“Learners sometimes look at `A1` and think the code should somehow use `A` and `1`. That is not today’s task. Today’s task uses numeric row and column positions. The seat labels are just values stored inside the structure.”

---

## 10) Debrief and Share-Out (~4 minutes)

### 10.1 Bring the class together

**Say:**
“Let’s pause and compare results. If your program is not perfect yet, that is okay. The important question is whether you can explain the structure.”

### 10.2 Ask for learner explanations

Ask:
- “Who can explain what the outer list represents?”
- “Who can explain what one inner list represents?”
- “Who can say, in one sentence, how to access the middle seat in a 3x3 chart?”

### 10.3 Model the answer

**Say:**
“A strong answer sounds like this:
‘The outer list stores the rows. Each inner list stores the seats in one row. To access a seat, use the row index first and the column position second.’

That explanation matters because it shows understanding, not just copying.”

---

## 11) Recap Script (~2 minutes)

**Say:**
“Today we learned how to model table-like data with nested lists.

We learned that:
- a nested list is a list of lists
- the outer list can represent rows
- each inner list can represent values in a row
- `chart[row][column]` is the basic access pattern
- we can print each row with a `for` loop
- we can update one specific cell by assigning a new value
- the biggest beginner risks are row/column confusion and out-of-range indexes

That is exactly the understanding we need before moving into the checkpoint hour.”

---

## 12) Exit Ticket (~1 minute)

Ask learners to answer verbally, in chat, or on paper:

1. In a nested list used like a seating chart, what does the outer list usually represent?
2. In `chart[1][2]`, which part selects the row?
3. What two mistakes are most common when beginners work with nested lists?
4. Why might printing each row separately be easier to read than printing the full nested list all at once?

**Expected direction of answers:**
- the outer list represents rows
- the first index selects the row
- row/column confusion and `IndexError`
- row-by-row output matches the visual table more clearly

---

## 13) Instructor Notes for the Transition to Hour 16

**Say:**
“We have now worked with lists in three ways:
- creating and changing them
- looping through them
- arranging them into small table-like structures

Next comes Checkpoint 2, where learners show they can use lists and strings together in a practical mini-program with clean output.”

Close with this final reminder:

“Nested lists are not a different universe. They are still lists. They just have rows inside them.”

---

## Appendix: Instructor Reinforcement Notes for Hour 15

### A) A board-first visualization routine

If learners feel overwhelmed by the brackets in a nested list, stop coding for a moment and move to a diagram.

Draw this:

```text
        column 0   column 1   column 2
row 0      A1         A2         A3
row 1      B1         B2         B3
row 2      C1         C2         C3
```

Then say:

“This picture and the code describe the same structure.
The rows on the left correspond to the first index.
The column positions across the top correspond to the second index.

So when I write `seating_chart[1][2]`, I am saying:
- go to row 1 first
- then go to item 2 inside that row”

Many learners need this visual translation before double indexing feels natural.

### B) Simple verbal drills that fit the hour

Use these quick questions during instruction or lab time:

- “What does the outer list hold?”
- “What does one inner list hold?”
- “If I want the first value in the third row, what index pair should I use?”
- “If I want the middle value in a 3x3 chart, what index pair should I use?”
- “What is the difference between printing the whole nested list and printing one row at a time?”

These questions are small, but they reveal whether learners truly see the structure.

### C) Micro-drills with numbers instead of seat names

Some learners understand the shape better when the values are plain numbers. If needed, show this alternate example:

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Then ask:
- “What is `grid[0][0]`?”
- “What is `grid[1][2]`?”
- “What is `grid[2][1]`?”
- “How would I change the center value to `0`?”

This can reduce cognitive load because the learner no longer has to interpret seat labels and indexing at the same time.

### D) A calm troubleshooting script for `IndexError`

When a learner sees `IndexError`, resist the urge to jump straight to the fix. Instead, say:

“Let’s read the position you requested.
What row did you ask for?
What column did you ask for?
Which indexes are actually valid in a 3x3 structure?”

Then reinforce:
- valid row indexes: `0`, `1`, `2`
- valid column indexes: `0`, `1`, `2`

This helps learners connect the error to the structure instead of treating it like random failure.

### E) Instructor phrasing that tends to work well

Try these short coaching lines:

- “Pick the row first.”
- “Now pick the value inside that row.”
- “Print one row to see what Python is looking at.”
- “Draw the grid if the code feels too abstract.”
- “After you update the data, show the data again.”

These phrases are especially helpful for beginners because they turn a potentially abstract problem into a sequence of manageable steps.

### F) Optional extension discussion without drifting off-scope

If a learner finishes early and wants a small extension, you can suggest one of these:
- validate that row and column must be between 0 and 2
- let the user mark the seat with initials instead of `"X"`
- print the chart with spaces for a slightly cleaner display

But keep reminding the class that the core goal is simple: understand the list-of-lists structure, access values with two indexes, and update one seat correctly.

### G) Strong end-of-hour summary to repeat out loud

If you want one final sentence learners can remember, use this:

“A nested list is still just a list; it simply stores rows, and each row stores values.”

That sentence keeps the topic grounded in what learners already know instead of making it feel like a completely new world.

### H) Final review prompts before the checkpoint

Before moving into Checkpoint 2, you can ask learners to answer these quickly:

- “What does the outer list represent in our seating chart?”
- “What does one inner list represent?”
- “In `chart[2][1]`, which number chooses the row?”
- “Why do we print the chart again after changing one value?”
- “What usually causes `IndexError` in this hour?”

Then restate the key idea:

“The first index chooses the row. The second index chooses the value inside that row. That is the whole access pattern.”

### I) Extra confidence statement for beginners

If the room seems hesitant, say:

“Nested lists can look more complex than they really are because there are more brackets on the screen. But the underlying idea is still familiar. You already know what a list is. Today you simply learned that a list can hold rows, and each row can hold values.

That means you are not starting from zero. You are extending what you already know.”

### J) One more quick practice grid

If learners need a final simple check, show this 2x2 example:

```python
boxes = [
    ["top-left", "top-right"],
    ["bottom-left", "bottom-right"]
]
```

Ask:
- “What is `boxes[0][1]`?”
- “What is `boxes[1][0]`?”
- “How would I change `bottom-right` to `X`?”

Then say:

“Notice how the exact values change, but the access pattern does not. First choose the row. Then choose the value inside the row. That is the consistent rule learners should leave with.”

### K) Closing teaching sentence to repeat aloud

Use this short summary if you want one last anchor before the checkpoint:

“A nested list is a list of rows. The first index chooses the row. The second index chooses the value inside that row.”

That sentence keeps the concept stable and memorable for beginners.

A final reminder for beginners: the extra brackets in a nested list can make the code look more intimidating than it really is. Underneath the syntax, the logic is simple. Choose the row first. Then choose the value inside that row. If learners can say that confidently and update one seat correctly, they have met the essential goal of this hour.

If you need one more last review question, ask learners this: “If I point to the bottom-left item in a 3x3 chart, what row am I in, and what column position am I choosing?” Questions like that reveal whether the learner truly sees the grid or is still guessing. End by reminding them that printing rows one at a time and updating one selected value are the two most practical skills from this hour.

A final instructor reminder: keep the examples small, the language concrete, and the indexing visible. When the grid stays 3x3, learners can focus on the row-and-column idea without being distracted by size. The purpose is confidence with structure, not complexity for its own sake.

If you want one last closing check, ask learners to point to the middle item, the top-right item, and the bottom-left item in the same chart. That fast verbal exercise often confirms whether the structure is really clear. When they can answer those confidently and update one selected value correctly, they are ready to move on.

That is enough for a strong Basics-level nested-list introduction.
