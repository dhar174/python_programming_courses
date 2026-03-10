# Day 4, Hour 1: Lists Fundamentals (Course Hour 13)
**Python Programming Basics – Session 4**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 4, Course Hour 13 – Lists fundamentals  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is written as a detailed read-aloud teaching guide. Keep the hour tightly focused on lists as an ordered, changeable collection. Stay within Basics scope. Do not drift into dictionaries, file handling, or function design. The key outcomes for this hour are list creation, indexing, slicing, mutation, `append()`, `remove()`, `pop()`, and membership checks with `in`.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

“By the end of this hour, you will be able to:
1. Explain what a list is in plain beginner-friendly language.
2. Create a list and print it.
3. Access list items with indexing and look at portions of a list with slicing.
4. Change a list by updating items and by using `append()`, `remove()`, and `pop()`.
5. Check whether an item exists in a list using `in`.
6. Build a small shopping-list program that starts with an empty list, adds five items, removes one chosen item, and prints the final list and item count.

This is an important transition point in the course. Up to now, many of our programs have stored one value at a time. Lists let us store a whole collection of related values in one variable.”

---

## 1) Agenda + Timing (show slide / read quickly, ~2 minutes)

- **0:00–0:05** Recap, transition into Session 4, and motivation for lists
- **0:05–0:15** What lists are, why they matter, and list literal syntax
- **0:15–0:25** Indexing, slicing, and the idea that lists are mutable
- **0:25–0:35** Core operations: update, `append()`, `remove()`, `pop()`, and `in`
- **0:35–0:45** Live demo: build and modify a shopping list
- **0:45–0:57** Guided lab: shopping-list program
- **0:57–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist (before class)

- Open a clean file such as `hour13_lists_demo.py`.
- Have terminal and editor visible if possible so learners see both the code and the output.
- Prepare a few familiar item names ahead of time: `milk`, `bread`, `eggs`, `tea`, `rice`, `apples`, `soap`.
- Be ready to show one deliberate mistake: trying to remove an item that is not in the list.
- Be ready to show a second deliberate mistake: calling `pop()` with a value instead of an index.
- If some learners type slowly, have a starter file ready with comments only.

**Say:** “Please type with me today. Lists are much easier to understand when you build and change them yourself.”

---

## 3) Opening Script: Reconnect to Earlier Learning (~5 minutes)

### 3.1 Quick recap of the path so far

**Say:**
“Welcome back. Before today, we built the foundations of beginner Python. We learned how to print, store values in variables, work with numbers, work with strings, take input from users, compare values, format output, and read errors with a calmer mindset.

That is already a lot of progress.

But there is one limitation in most of the programs we have written so far: they usually work with one value at a time.

For example, if I want to store one name, one variable works perfectly. If I want to store one age, one variable works perfectly. But what if I need five grocery items? Or seven grades? Or ten tasks? Or the names of every learner in the room?”

### 3.2 Set up the problem

**Say:**
“If I try to solve that problem with separate variables, my code gets awkward very quickly.”

**Type and narrate:**

```python
item_1 = "milk"
item_2 = "bread"
item_3 = "eggs"
item_4 = "tea"
item_5 = "rice"
```

**Say:**
“This is possible, but it is not a good long-term pattern. It is repetitive. It is harder to print neatly. It is harder to search. It is harder to update. And if I suddenly need six items instead of five, I have to create another variable.

So today we learn a better tool: the list.”

### 3.3 Motivation in plain language

**Say:**
“A list is one variable that can hold multiple related values in order.

That word ‘order’ matters. Lists remember position.

That word ‘related’ matters too. A list is a very natural choice when you have a group of similar things such as:
- shopping items
- grades
- tasks
- names
- menu choices
- words collected from a user

If strings helped us work with one piece of text, lists help us work with many values together.”

**Ask learners:**
- “Where might a shopping app use a list?”
- “Where might a teacher use a list?”
- “Where might you personally use a list in a small script?”

Take two or three answers, then say:

“Good. The goal is not just to memorize list syntax. The goal is to recognize when a collection belongs together.”

---

## 4) Core Concept Delivery: What a List Is and How It Looks (~10 minutes)

### 4.1 Beginner-friendly definition

**Say:**
“A list is an ordered collection of values.

Let’s unpack that.
- **Collection** means one variable can hold many items.
- **Ordered** means each item has a position.
- **Changeable** means we can update the list after it is created.

That last idea is important. Later in the hour we will compare lists with strings. Strings are text values, and strings do not let us change one character in place. Lists do let us change items in place. That is why we say lists are mutable.”

### 4.2 Basic syntax

**Type:**

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)
```

Run it.

**Say:**
“We create a list using square brackets. Inside the brackets, items are separated by commas.

The variable name is `fruits`.
The list contains three string items.
When we print the list, Python shows us the whole structure.”

### 4.3 Show that a list can start empty

**Type:**

```python
shopping_list = []
print(shopping_list)
```

**Say:**
“This is an empty list. It contains no items yet, but it is still a valid list.

Empty lists are extremely common. Often, we create an empty list first and then add items as the program runs.”

### 4.4 Keep the examples simple and consistent

**Say:**
“For beginners, it helps to keep lists consistent. If a list is meant to store grocery items, then use grocery-item strings. If a list is meant to store grades, then use numbers. Python technically allows mixed data in one list, but for now we want clarity more than cleverness.”

**Type:**

```python
numbers = [10, 20, 30]
print(numbers)
```

Then say:

“You can store numbers in a list. You can store strings in a list. The main point is: the list keeps the items together in order.”

### 4.5 Ask for prediction

**Ask learners:**
- “What do you think prints if I run `print(fruits)`?”
- “What do you think prints if I run `print(shopping_list)`?”
- “Why might an empty list still be useful?”

Use the predictions to reinforce: empty list first, then grow it later.

---

## 5) Indexing and Slicing Lists (~10 minutes)

### 5.1 Connect lists to a familiar idea

**Say:**
“If Day 2 felt comfortable, this next part should look familiar. Lists, like strings, use indexing. That means each item has a position number.

And just like strings, Python starts counting at zero.”

### 5.2 Indexing example

**Type:**

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
```

Run it.

**Say:**
“Index `0` is the first item.
Index `1` is the second item.
Index `2` is the third item.

This zero-based counting takes practice. It feels unusual at first, but it becomes normal very quickly.”

**Ask learners:**
“What do you predict `fruits[1]` prints?”

Pause, then run it.

### 5.3 Negative indexing

**Type:**

```python
print(fruits[-1])
print(fruits[-2])
```

**Say:**
“Negative indexes count from the end.
- `-1` means last item
- `-2` means second-to-last item

This is useful when you care more about the end than the beginning.”

### 5.4 Slicing example

**Type:**

```python
letters = ["a", "b", "c", "d", "e"]
print(letters[0:3])
print(letters[1:4])
print(letters[:2])
print(letters[2:])
```

**Say:**
“Slicing works like it did with strings. The pattern is `start:end`, and the end position is not included.

So `letters[0:3]` gives us index 0, index 1, and index 2.
It stops before index 3.”

### 5.5 Clarify what slicing returns

**Say:**
“One easy mistake is to think a slice returns one item. It does not. A slice returns a new list containing multiple items.

That means:
- indexing gives one item
- slicing gives a list of items”

**Type:**

```python
print(letters[2])
print(letters[2:4])
```

### 5.6 Quick practice questions

**Ask learners:**
- “What is the first item in `fruits`?”
- “What is the last item in `fruits`?”
- “If I want the first two items, what slice would I use?”
- “If I want everything from index 1 onward, what slice would I use?”

Let learners answer aloud before you confirm.

### 5.7 Gentle warning about out-of-range indexes

**Type:**

```python
# print(fruits[10])
```

**Say:**
“If I try to access an index that does not exist, Python raises an error. Today we only need to understand that positions must be valid. We do not need a deep exception-handling lesson here. Just remember: lists have boundaries.”

---

## 6) Lists Are Mutable: Changing Items Matters (~7 minutes)

### 6.1 Explain mutability simply

**Say:**
“Now we arrive at one of the most important ideas in today’s hour.

Lists are mutable.

That means we can change an existing list after it is created.

This is different from strings. With strings, we can create a new string, but we do not replace one character in place using indexing. With lists, we absolutely can replace one item at a specific position.”

### 6.2 Demonstrate item update

**Type:**

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)

fruits[1] = "blueberry"
print(fruits)
```

Run it.

**Say:**
“We changed the second item from `banana` to `blueberry`.

The list itself changed. That is the key idea.”

### 6.3 Compare gently with strings

**Type:**

```python
word = "cat"
# word[0] = "b"
```

**Say:**
“If I try to change one character of a string in place, Python will not allow it. That is because strings are not mutable in that way.

I do not want you to memorize the word ‘mutable’ as a fancy vocabulary term. I want you to connect it to a concrete idea:
- a list can be changed after it is created
- a string cannot be changed item-by-item that same way”

### 6.4 Ask a concept question

**Ask learners:**
“If I change `fruits[1]`, am I creating a completely different kind of structure, or am I updating the existing list?”

Guide them to: “updating the existing list.”

---

## 7) Core List Operations: `append()`, `remove()`, `pop()`, and `in` (~10 minutes)

### 7.1 `append()` adds to the end

**Type:**

```python
shopping_list = ["milk", "bread"]
print(shopping_list)

shopping_list.append("eggs")
print(shopping_list)
```

**Say:**
“`append()` adds one item to the end of the list.

This is one of the most common list methods beginners use. If your program collects items from a user one at a time, `append()` is often exactly what you need.”

### 7.2 `remove()` removes by value

**Type:**

```python
shopping_list.remove("bread")
print(shopping_list)
```

**Say:**
“`remove()` removes by value, not by position.

That wording matters.
If I say `shopping_list.remove("bread")`, Python searches for the item with that value and removes it.”

### 7.3 `pop()` removes by index

**Type:**

```python
shopping_list = ["milk", "bread", "eggs"]
removed_item = shopping_list.pop(1)
print(removed_item)
print(shopping_list)
```

**Say:**
“`pop()` usually works with a position. It removes the item at a given index.

So now we have an important difference:
- `remove()` uses a value
- `pop()` uses an index”

### 7.4 Show `pop()` without an index

**Type:**

```python
shopping_list = ["milk", "bread", "eggs"]
last_item = shopping_list.pop()
print(last_item)
print(shopping_list)
```

**Say:**
“If you do not give `pop()` an index, it removes the last item.

That is useful when the last item is the one you want to take off.”

### 7.5 Membership test with `in`

**Type:**

```python
shopping_list = ["milk", "bread", "eggs"]
print("milk" in shopping_list)
print("tea" in shopping_list)
```

**Say:**
“The `in` operator answers a yes-or-no question: is this value present in the list?

The result is `True` or `False`.

That makes `in` very useful before removing an item.”

### 7.6 Model a safe removal check

**Type:**

```python
item_to_remove = "tea"

if item_to_remove in shopping_list:
    shopping_list.remove(item_to_remove)
    print("Item removed.")
else:
    print("That item is not in the list.")
```

**Say:**
“Notice what we are doing here. We are checking membership first. That helps us avoid a crash if the value is missing.

The runbook for this hour specifically mentions a common pitfall: `remove()` on a missing item raises an error. We are not doing a full lesson on exceptions right now. A simple membership check is enough for this hour.”

### 7.7 Deliberate mistake: `pop()` with a value

**Type:**

```python
shopping_list = ["milk", "bread", "eggs"]
# shopping_list.pop("bread")
```

**Say:**
“This is wrong because `pop()` expects an index, not a value. If I want to remove by value, I use `remove()`. If I want to remove by position, I use `pop()`.”

**Ask learners:**
- “Which method removes by value?”
- “Which method removes by position?”
- “Which method adds to the end?”

---

## 8) Live Demo: Shopping List Build and Update (~10 minutes)

### 8.1 Frame the demo

**Say:**
“Now let’s put the core list operations together in one realistic mini-example. I am going to build a shopping list, update it, remove items in two different ways, check for membership, and print the result after each step.

As I type, I want you to keep asking yourself: what changed in the list?”

### 8.2 Demo code, part 1: start empty and grow the list

**Type and narrate slowly:**

```python
shopping_list = []
print("Starting list:", shopping_list)

shopping_list.append("milk")
print("After adding milk:", shopping_list)

shopping_list.append("bread")
print("After adding bread:", shopping_list)

shopping_list.append("eggs")
print("After adding eggs:", shopping_list)
```

Run it.

**Say:**
“Notice the pattern. We began with an empty list and used `append()` three times. That is the exact same pattern learners will use in the lab, except the values will come from user input.”

### 8.3 Demo code, part 2: update an item

**Type:**

```python
shopping_list[1] = "whole grain bread"
print("After updating index 1:", shopping_list)
```

**Say:**
“This line reminds us that lists are mutable. We can change one item directly by index.”

### 8.4 Demo code, part 3: membership test and remove by value

**Type:**

```python
item_to_remove = "milk"

if item_to_remove in shopping_list:
    shopping_list.remove(item_to_remove)
    print(f"Removed {item_to_remove}.")
else:
    print(f"{item_to_remove} was not found.")

print("Current list:", shopping_list)
```

**Say:**
“This is the safer beginner pattern. Check membership first, then remove.”

### 8.5 Demo code, part 4: pop the last item

**Type:**

```python
popped_item = shopping_list.pop()
print(f"Popped item: {popped_item}")
print("Current list:", shopping_list)
```

**Say:**
“`pop()` not only removes an item. It also gives it back to us, so we can store it in a variable and print it.”

### 8.6 Demo code, part 5: final list and count

**Type:**

```python
print("Final shopping list:", shopping_list)
print(f"Item count: {len(shopping_list)}")
```

**Say:**
“`len()` tells us how many items are in the list. That is useful for summaries and clean output.”

### 8.7 Ask comprehension questions

**Ask learners:**
- “What part of the code actually made the list longer?”
- “What line changed an existing item?”
- “Why did I use `in` before `remove()`?”
- “What does `len(shopping_list)` measure?”

### 8.8 Optional quick variation if time permits

If the class is comfortable, add:

```python
print(shopping_list[0])
print(shopping_list[:1])
```

Then say:

“Notice the difference between one item and a slice containing items.”

---

## 9) Guided Lab: Shopping List Program (~12 minutes)

### 9.1 Introduce the lab clearly

**Say:**
“Now it is your turn. Your job is to build a shopping-list program that follows the Session 4 runbook exactly.

Your program should:
1. Start with an empty list.
2. Ask the user for 5 shopping items, one at a time.
3. Append each item to the list.
4. Ask the user for one item to remove.
5. Remove that item if it exists.
6. Print the final list.
7. Print the item count.”

### 9.2 Put the lab requirements on screen

```text
Lab: Shopping List
- Start with an empty list.
- Ask the user for 5 items, one at a time.
- Remove one chosen item.
- Print the final list and item count.
```

### 9.3 Provide a beginner-friendly starter structure

**Type and leave it on screen:**

```python
shopping_list = []

item = input("Enter shopping item 1: ")
shopping_list.append(item)

item = input("Enter shopping item 2: ")
shopping_list.append(item)

item = input("Enter shopping item 3: ")
shopping_list.append(item)

item = input("Enter shopping item 4: ")
shopping_list.append(item)

item = input("Enter shopping item 5: ")
shopping_list.append(item)

print("Your shopping list is:", shopping_list)

item_to_remove = input("Enter one item to remove: ")

if item_to_remove in shopping_list:
    shopping_list.remove(item_to_remove)
    print(f"Removed {item_to_remove}.")
else:
    print("That item was not found.")

print("Final shopping list:", shopping_list)
print(f"Item count: {len(shopping_list)}")
```

### 9.4 Explain why this starter is intentionally simple

**Say:**
“This is not the shortest possible program. It is the clearest possible program for this point in the course.

Later, loops will help us avoid repetition. Right now, repetition is acceptable if it helps you see the pattern clearly.

Notice that I am not trying to be fancy. I am trying to be readable.”

### 9.5 Prompt learners to personalize

**Say:**
“After you get the basic version working, you may personalize your test data. Use grocery items you actually buy. That makes it easier to reason about the output.”

### 9.6 Instructor circulation prompts during lab time

As learners work, walk around and ask:
- “Show me where the empty list is created.”
- “Which line adds a new item?”
- “How many times do you append?”
- “What happens if the user tries to remove an item that is missing?”
- “Where do you print the final count?”

### 9.7 If learners finish early

Offer these optional extensions, but emphasize they are optional:
- allow the user to type `done` before five items are entered
- print the list alphabetically using `sorted(shopping_list)`
- print each item on its own line instead of printing the whole list object

Be clear that these are extensions, not required outcomes.

---

## 10) Common Pitfalls and How to Coach Through Them (~6 minutes)

### 10.1 Pitfall: `remove()` on a missing item

**Symptom:** learner gets an error when the item is not in the list.

**Coach with these words:**
“Read the message calmly. The program is telling you that the value you tried to remove is not present. Before removing, check with `in`.”

Show again if needed:

```python
if item_to_remove in shopping_list:
    shopping_list.remove(item_to_remove)
else:
    print("That item was not found.")
```

### 10.2 Pitfall: confusing `pop()` with `remove()`

**Say:**
“This is one of today’s signature mistakes.
- `remove("bread")` uses a value.
- `pop(1)` uses a position.

If a learner writes `pop("bread")`, pause and ask: ‘Are you giving Python a position or a value?’ Usually that question helps them self-correct.”

### 10.3 Pitfall: forgetting that indexes start at zero

**Say:**
“If a learner thinks index 1 is the first item, bring them back to the phrase: ‘Python counts from zero.’ Have them print the list and label the positions out loud.”

### 10.4 Pitfall: printing too early and thinking the list is wrong

**Say:**
“Sometimes the list is fine, but the learner is printing it before the last update. Encourage them to print after each important change while debugging. Lists are easier to understand when you inspect them step by step.”

### 10.5 Pitfall: confusing one item with the full list

**Say:**
“Beginners sometimes forget whether they are printing the whole list or just one item. Ask them: ‘Do you want the collection, or one element from the collection?’ That simple question often clears it up.”

---

## 11) Debrief and Share-Out (~4 minutes)

### 11.1 Bring the class back together

**Say:**
“Let’s pause and compare what we built. Even if your code is not perfect yet, you can still learn a lot from the structure.”

### 11.2 Prompt two or three learners

Ask:
- “Who used the membership check before removing?”
- “Who can explain the difference between `remove()` and `pop()` in one sentence?”
- “Who printed the final item count with `len()`?”

### 11.3 Model a concise explanation

**Say:**
“A strong answer sounds like this:
‘My program starts with an empty list, collects five items using `append()`, asks for one item to remove, checks whether the item exists, removes it if present, and then prints the final list and the number of items.’

That explanation matters because it shows the learner understands the program, not just the syntax.”

---

## 12) Recap Script (~2 minutes)

**Say:**
“Today we introduced one of the most useful structures in beginner Python: the list.

We learned that:
- a list stores multiple related values in one variable
- lists keep their order
- lists use indexing and slicing
- lists are mutable, which means they can change
- `append()` adds to the end
- `remove()` removes by value
- `pop()` removes by index, or the last item if no index is given
- `in` checks whether an item exists in the list

That is a lot of progress for one hour, and it gives us the foundation for the next step: processing list items with loops.”

---

## 13) Exit Ticket (~1 minute)

Ask learners to answer verbally, in chat, or on paper:

1. Why can lists change after creation, but strings cannot change item-by-item the same way?
2. What is the difference between `remove()` and `pop()`?
3. If `shopping_list = ["milk", "bread", "eggs"]`, what does `"bread" in shopping_list` return?
4. If you wanted to start collecting user items before you knew them, why might `[]` be a good first line of code?

**Expected direction of answers:**
- lists are mutable
- `remove()` uses a value, `pop()` uses an index
- the membership test returns `True`
- an empty list gives you a place to store items as they are entered

---

## 14) Instructor Notes for the Transition to Hour 14

**Say:**
“Right now we know how to store many values together. In the next hour, we learn how to process every item in a list without writing repetitive code. That is where `for` loops enter the picture.”

If learners seem shaky, reinforce these two lines before moving on:
- “A list is a changeable collection.”
- “`append()`, `remove()`, `pop()`, and `in` are the core tools from this hour.”

---

## Appendix: Instructor Reinforcement Notes for Hour 13

### A) Quick board plan if learners need one more visual pass

If the room needs a calmer visual explanation, draw this on the board:

```text
shopping_list = ["milk", "bread", "eggs"]
                 0        1        2
```

Then ask:
- “Which item is at index 0?”
- “Which item is at index 2?”
- “If I change index 1, what changes?”
- “If I call `pop(0)`, which item leaves the list?”

This board sketch is helpful because it makes the list feel less abstract. Many beginners understand faster when they can point to a position with a finger.

### B) Short extra practice prompts you can use verbally

If there are two or three extra minutes, ask learners to answer these without typing first:

1. If `items = ["pen", "paper", "book"]`, what does `items[1]` return?
2. What does `items[-1]` return?
3. If you write `items.append("eraser")`, where does the new value go?
4. If you write `items.remove("paper")`, are you removing by value or by position?
5. If you write `items.pop(2)`, what kind of input does `pop()` expect?

Then say:

“Notice that each question is really checking one of four ideas: position, change, membership, or method choice. That is the heart of this hour.”

### C) Instructor language for gentle correction

When a learner makes a mistake, try short coaching lines like these:

- “Tell me whether you want one item or the whole list.”
- “Tell me whether you are removing by value or by position.”
- “Show me the line where the list actually changes.”
- “Print the list right after that line so we can see the result.”
- “If the item is missing, how could we check before removing?”

These phrases are effective because they guide thinking without taking the keyboard away from the learner.

### D) Suggested micro-debrief question set

If you want a slightly longer closing conversation before Hour 14, use these prompts:

- “Why is an empty list a good starting point when you plan to collect user input?”
- “Why is `append()` so useful for beginner programs?”
- “Why might `in` be helpful before `remove()`?”
- “What is one real-world example where a list would be better than five separate variables?”

A strong class debrief will keep the answers practical rather than overly theoretical.

### E) Final teaching reminder to yourself

The hour succeeds if learners leave with this mental model:

“A list is a changeable collection of values in order.”

If they can say that, create one, add items, remove an item safely, and print the result, the hour has met its runbook goal.
