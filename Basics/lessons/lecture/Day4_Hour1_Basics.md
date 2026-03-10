# Day 4, Hour 1: Menu Loops (CLI Pattern)
**Python Programming Basics – Day 4 / Session 8 / Course Hour 29**

---

## Subtitle
**Building programs that stay open, repeat useful actions, and respond to the user one choice at a time**

**Instructor framing:** This is **Day 4, Hour 1** in the local course sequence and **Course Hour 29** in the full 48-hour Basics runbook. Students already know variables, strings, lists, dictionaries, conditionals, and loops. In this hour, they begin combining those pieces into a more realistic command-line program structure: the **menu loop**.

---

## Timing Overview
**Total Time:** 60 minutes  
- Recap & Transition from Day 3 / previous control-flow work: 5 minutes  
- Why menu-driven CLI programs matter: 8 minutes  
- Anatomy of a menu loop with `while` + `if/elif`: 12 minutes  
- Basic choice validation and shared state: 8 minutes  
- Live Demo (3 options + quit): 10 minutes  
- Hands-On Lab – Upgrade Menu: 12 minutes  
- Debrief & Exit Ticket: 5 minutes  

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Build a menu-driven program using a `while` loop
2. Repeatedly display choices and collect user input until the user quits
3. Route different actions using `if/elif/else`
4. Apply basic input validation for menu choices
5. Keep program state in memory while the loop runs
6. Explain why a menu loop is a common pattern in command-line tools
7. Preview how functions can later help organize menu-based programs

---

## Section 1: Recap & Transition into Day 4 (5 minutes)

### Reconnecting to Prior Learning

**[Instructor speaks:]**

Welcome to **Day 4**. In our local day-by-day sequence, this is the first instructional hour of the day. In the full runbook, this maps to **Course Hour 29**, which is the beginning of **Session 8**.

Before we start building menu-driven programs, let’s remember what students already know, because today is not a brand-new world. It is a **combination hour**.

Up to this point, learners have already practiced:

- variables and assignment
- strings and string methods
- `input()` and type conversion
- conditionals with `if`, `elif`, and `else`
- `while` loops and `for` loops
- lists and dictionaries for storing data in memory

That means today’s goal is not “learn one isolated syntax feature.” Today’s goal is:

> **Use several familiar tools together in a realistic command-line program pattern.**

A lot of students reach a point where they say, “I know loops,” or “I know dictionaries,” but then freeze when asked to build a tiny program. Menu loops help close that gap because they give learners a simple frame:

1. show choices
2. ask for a choice
3. do something
4. repeat

That is a huge step toward writing programs that feel interactive and useful instead of one-and-done.

### Suggested Warm-Up Questions

**[Instructor asks:]**

- When have you seen a menu in software before?
- If a command-line program should let a user do more than one thing, should it end after one action?
- What kind of loop feels like a good fit when we do not know ahead of time how many actions the user wants to perform?

[Pause. Invite a few answers.]

**[Instructor speaks:]**

Exactly. If the user might add one item, or five items, or search several times, we need a loop that keeps going **until some condition says stop**. That is why `while` is so useful here.

### Transition Statement

**[Instructor speaks:]**

In the previous control-flow work, we practiced loops and decision-making as separate ideas. In this hour, we merge them into a pattern you will use again and again: the **CLI menu loop**.

---

## Section 2: Why Menu-Driven CLI Programs Matter (8 minutes)

### The Problem with One-Shot Scripts

**[Instructor speaks:]**

Let’s say you wrote a simple script yesterday that lets a user add one item to a list. That script may work, but it usually has a limitation:

- it performs one action
- it prints one result
- then it ends

That is fine for a tiny script. But real tools often need to support **multiple actions in one run**.

Imagine a small in-memory program for:

- tracking books
- managing contacts
- storing student names
- keeping a grocery list
- managing tasks

Would it be good user experience to run the script once to add an item, close it, run it again to list items, close it, run it again to search?

Probably not.

### What a Menu Loop Gives Us

**[Instructor speaks:]**

A menu loop solves that by giving the user a clear, repeated interface.

A typical command-line flow looks like this:

```text
1. Add item
2. List items
3. Search items
Q. Quit
```

Then the program waits for input, performs the requested action, and returns to the menu.

That structure is powerful because it gives us:

- **clarity** — the user always knows the available actions
- **repeatability** — the program stays alive across multiple actions
- **state** — data remains in memory during the run
- **organization** — our program logic becomes easier to reason about

### Real-World Relevance

**[Instructor speaks:]**

Even when you later move beyond command-line programs, the thinking pattern still matters.

A menu loop teaches students to think in terms of:

- event → response
- input → decision → action
- persistent state during a session

That logic shows up in:

- terminal tools
- admin dashboards
- desktop menus
- web forms and button actions
- chatbot command handlers

So even though today’s work is simple and text-based, the thinking is absolutely real-world.

### Prediction Prompt

**[Instructor asks:]**

What do you think is the single most important reason to use a menu loop in a small CLI program?

[Accept answers such as “so the user can do multiple things,” “so the program doesn’t end immediately,” or “so we can reuse the same state.”]

**[Instructor speaks:]**

Yes. The central value is this:

> **A menu loop lets a program continue serving the user until the user decides to quit.**

That is the mental model we want students to keep.

---

## Section 3: The Anatomy of a Menu Loop (12 minutes)

### The Four-Part Pattern

**[Instructor speaks:]**

Here is the core pattern we want students to learn today. A menu-driven program usually has four repeating pieces:

1. **Display the menu**
2. **Get the user’s choice**
3. **Route that choice to the correct action**
4. **Repeat until quit**

Let’s write the most basic possible version:

```python
running = True

while running:
    print("\n=== Menu ===")
    print("1. Say hello")
    print("2. Show a message")
    print("Q. Quit")

    choice = input("Choose an option: ").strip().lower()

    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Python is fun to learn.")
    elif choice == "q":
        print("Goodbye!")
        running = False
    else:
        print("Invalid choice. Please try again.")
```

### Reading the Pattern Slowly

**[Instructor speaks:]**

Let’s slow this way down.

#### Part 1: The loop condition

```python
running = True
while running:
```

This means: keep repeating while `running` is `True`.

Later, when the user chooses quit, we change `running` to `False`. That causes the loop to end naturally.

#### Part 2: The menu display

```python
print("\n=== Menu ===")
print("1. Say hello")
print("2. Show a message")
print("Q. Quit")
```

We print the choices **inside the loop**, not outside. Why? Because the menu needs to appear again each time the loop repeats.

This is one of the biggest beginner mistakes.

### Common Mistake #1: Printing the Menu Only Once

**[Instructor speaks:]**

Students often do this:

```python
print("1. Add")
print("2. List")
print("Q. Quit")

while running:
    choice = input("Choose: ")
    ...
```

That prints the menu only one time at the beginning. After a few actions, the user may forget the choices.

A menu is most useful when it is **easy to see repeatedly**. So the display normally belongs **inside** the loop.

### Part 3: Normalize the input

```python
choice = input("Choose an option: ").strip().lower()
```

This is a great beginner-friendly pattern.

- `.strip()` removes accidental leading or trailing spaces
- `.lower()` makes uppercase and lowercase choices easier to handle

That means `Q`, `q`, and even ` q ` can all be treated consistently.

### Part 4: Route the choice using `if/elif/else`

**[Instructor speaks:]**

This is where the menu actually becomes a program.

```python
if choice == "1":
    ...
elif choice == "2":
    ...
elif choice == "q":
    ...
else:
    ...
```

Each branch is one possible action.

This is not fancy, and that is a good thing. In Basics, we want the routing logic to be **obvious**.

### Why `if/elif` Is the Right Level Here

**[Instructor speaks:]**

Could more advanced programmers use other patterns later? Yes. But at the Basics level, `if/elif/else` is perfect because:

- students can already read it
- it clearly matches the menu choices
- it keeps the control flow visible
- it supports small programs very well

We are not trying to be clever. We are trying to be understandable.

### Prediction Prompt

**[Instructor asks:]**

If I remove the `elif choice == "q":` branch, what happens when the user types `q`?

[Pause.]

**[Instructor speaks:]**

Right: the program never gets the signal to stop. It will likely fall into the `else` block and keep going. The loop itself is not magical. **We must design the exit condition.**

---

## Section 4: Basic Validation and Shared State (8 minutes)

### Basic Validation for Menu Choices

**[Instructor speaks:]**

Notice that our first level of validation is very simple: if the input is not one of the valid choices, we do not crash. We just respond with:

```python
print("Invalid choice. Please try again.")
```

That is an important design habit.

A beginner sometimes assumes validation means something complex. But in many cases, good validation simply means:

- check whether the input matches expected options
- if not, show a helpful message
- let the user try again

That alone makes a program feel far more solid.

### Shared State: Data Must Live Outside the Action Branches

**[Instructor speaks:]**

Now let’s connect the menu loop to stored data.

Suppose we are storing names in a list:

```python
names = []
running = True

while running:
    print("\n1. Add name")
    print("2. List names")
    print("Q. Quit")

    choice = input("Choose: ").strip().lower()

    if choice == "1":
        new_name = input("Enter a name: ").strip()
        names.append(new_name)
        print(f"Added: {new_name}")
    elif choice == "2":
        print(names)
    elif choice == "q":
        running = False
    else:
        print("Invalid choice.")
```

The critical idea is that `names` is created **before** the loop, not inside it.

### Common Mistake #2: Rebuilding the Data Structure Each Time

**[Instructor speaks:]**

A very common bug is this:

```python
while running:
    names = []
```

If `names = []` appears inside the loop, the list gets reset every time the menu repeats. Students then say:

> “My add option worked, but my list is empty again.”

That is not a mystery bug. It is a **state reset bug**.

If data should persist during the program run, create the list or dictionary **once**, outside the loop.

### Preview: Separating Logic into Functions

**[Instructor speaks:]**

Today we are only previewing this idea, not teaching functions in depth yet.

As menu programs get longer, it helps to separate actions into functions later, for example:

```python
def add_name(names: list[str]) -> None:
    new_name = input("Enter a name: ").strip()
    names.append(new_name)
    print(f"Added: {new_name}")
```

Then the menu branch can simply call `add_name(names)`.

We are **not** requiring students to organize everything with functions yet. But it is useful to mention the direction of travel:

- first learn the pattern clearly in one file
- later, break actions into functions for readability

That preview helps students understand that programs can grow in an organized way.

---

## Section 5: Live Demo – Menu Scaffold with 3 Options and Quit (10 minutes)

### Demo Goal

**[Instructor speaks:]**

Now I am going to build a small menu-driven program live. I want students to hear the reasoning, not just see the code appear.

For today’s demo, I’ll use a tiny **movie list manager**. It will store movie titles in memory and support:

1. Add movie
2. List movies
3. Search movies
Q. Quit

### Live Coding Script

**[Instructor types and speaks:]**

```python
# menu_movies.py
# Day 4, Hour 1 demo: menu loop scaffold

movies: list[str] = []
running = True

while running:
    print("\n=== Movie Menu ===")
    print("1. Add movie")
    print("2. List movies")
    print("3. Search movies")
    print("Q. Quit")

    choice = input("Choose an option: ").strip().lower()

    if choice == "1":
        movie = input("Enter a movie title: ").strip()
        if movie == "":
            print("Movie title cannot be empty.")
        else:
            movies.append(movie)
            print(f"Added '{movie}' to your list.")

    elif choice == "2":
        if len(movies) == 0:
            print("Your movie list is empty.")
        else:
            print("\nYour movies:")
            for index, movie in enumerate(movies, start=1):
                print(f"{index}. {movie}")

    elif choice == "3":
        search_term = input("Enter text to search for: ").strip().lower()
        found_movies = []

        for movie in movies:
            if search_term in movie.lower():
                found_movies.append(movie)

        if len(found_movies) == 0:
            print("No matches found.")
        else:
            print("Matches:")
            for movie in found_movies:
                print(f"- {movie}")

    elif choice == "q":
        print("Goodbye!")
        running = False

    else:
        print("Invalid menu choice. Please enter 1, 2, 3, or Q.")
```

### Narration Notes During the Demo

**[Instructor speaks:]**

As I code, I want to narrate decisions like these:

- “I’m creating `movies` outside the loop so the list persists.”
- “I’m printing the menu inside the loop so users see it every round.”
- “I’m normalizing input with `.strip().lower()`.”
- “I’m using `if/elif` because it maps clearly to menu choices.”
- “I’m checking for an empty list before listing items so the output stays friendly.”

### Student Prediction Prompts During Demo

**[Instructor asks:]**

- What happens if I add two movies, then list them?
- What happens if I type `Q` instead of `q`?
- What happens if I search for text that is not present?
- If I accidentally move `movies = []` inside the loop, what bug would appear?

Use these questions to keep the class mentally engaged.

### Testing the Demo in Front of Students

**[Instructor speaks:]**

Do not just write the code and move on. Model quick testing.

Run these cases live:

1. List when empty
2. Add one movie
3. Add a second movie
4. Search with a match
5. Search with no match
6. Enter an invalid menu choice
7. Quit

This teaches students an important habit:

> **A program is not finished when the typing stops. It is finished when the behavior is checked.**

---

## Section 6: Hands-On Lab – Upgrade Menu (12 minutes)

### Lab Setup

**[Instructor speaks:]**

Now students will build their own looped menu by upgrading a previous script or starting a fresh one with a familiar dataset.

Encourage them to choose a simple dataset they can reason about easily. Good options include:

- books
- favorite songs
- grocery items
- student names
- game scores
- recipes

The point is not the theme. The point is the **menu pattern**.

### Lab Prompt

**Lab: Upgrade Menu**

Turn a previous script into a looped menu program, or create a new one from scratch.

Your program must:

- use a menu-driven `while` loop
- include **add**, **list**, and **search** actions
- keep state in memory while the program runs
- repeat until the user chooses quit

### Required Features

1. **Add action**
   - Let the user add a new item to the dataset
2. **List action**
   - Show all stored items
3. **Search action**
   - Let the user search for text or a name
4. **Quit action**
   - End the program cleanly
5. **Basic invalid-choice handling**
   - If the user types an unsupported menu option, show a message and continue

### Suggested Starter Template

```python
items: list[str] = []
running = True

while running:
    print("\n=== My Menu ===")
    print("1. Add item")
    print("2. List items")
    print("3. Search items")
    print("Q. Quit")

    choice = input("Choose an option: ").strip().lower()

    if choice == "1":
        # add logic
        pass
    elif choice == "2":
        # list logic
        pass
    elif choice == "3":
        # search logic
        pass
    elif choice == "q":
        # quit logic
        pass
    else:
        print("Invalid choice.")
```

### Completion Criteria

A student solution is complete when:

- ✅ the menu repeats until quit  
- ✅ add works  
- ✅ list works  
- ✅ search works  
- ✅ data stays available during the run  
- ✅ invalid menu choices do not crash the program  

### Coaching Language While Circulating

**[Instructor speaks:]**

Use short coaching prompts while moving around the room:

- “Where is your shared list created?”
- “What tells your loop when to stop?”
- “What should happen after a successful add?”
- “Does your menu show again after each action?”
- “If the user searches for text that is not found, what message do they see?”

These questions guide students without taking over the keyboard.

### Common Pitfalls to Watch For

1. **Forgetting to reprint the menu**  
   Usually caused by printing it outside the loop.

2. **Not updating the shared data structure**  
   Students gather input but never append it to the list.

3. **Resetting the list inside the loop**  
   This makes data disappear after each action.

4. **Search variable mismatch**  
   Students compare the search term to the wrong variable or forget `.lower()` on both sides.

5. **No feedback messages**  
   The program technically works, but the user experience is confusing.

### Optional Extension

If students finish early, invite them to add:

- **update** option
- **delete** option

Keep this optional. Today’s required learning target is the menu loop pattern itself.

---

## Section 7: Debrief & Exit Ticket (5 minutes)

### Debrief Questions

**[Instructor asks:]**

- What part of the menu loop felt easiest?
- What part was most error-prone?
- What bug happened when data did not seem to “stick” between actions?
- Why is the menu pattern more realistic than a one-shot script?

### Instructor Synthesis

**[Instructor speaks:]**

What we built today is a very big step in beginner programming. Even though the code is still small, students are now organizing programs around:

- repeated interaction
- branch-based actions
- in-memory state
- user-driven flow

That is real program structure.

### Exit Ticket

**[Instructor asks:]**

Write one or two sentences answering this:

**Why is a menu loop useful for CLI programs?**

**Expected ideas:**
- it lets the user do multiple actions in one run
- it keeps the program open until the user chooses to quit
- it keeps state in memory during the session
- it makes the user interface clearer

---

## Recap: What We Accomplished in Day 4, Hour 1 / Course Hour 29

In this hour, learners:

- built or analyzed a menu-driven `while` loop
- routed choices with `if/elif/else`
- handled invalid choices without crashing
- practiced keeping shared data in memory
- saw how menu-based CLI programs are structured
- previewed how functions can later organize menu actions

**[Instructor speaks:]**

The key takeaway is not just “I can write a loop.” The key takeaway is:

> **I can design a small interactive program that stays alive and responds to user choices.**

That is a major milestone.

In **Day 4, Hour 2 / Course Hour 30**, we will improve these programs by adding **input validation**, so user mistakes are handled more gracefully.

---

## Appendix A: Full Demo Solution with Comments

```python
# menu_movies.py
# Day 4, Hour 1 demo: menu-driven CLI pattern

movies: list[str] = []
running = True

while running:
    print("\n=== Movie Menu ===")
    print("1. Add movie")
    print("2. List movies")
    print("3. Search movies")
    print("Q. Quit")

    choice = input("Choose an option: ").strip().lower()

    if choice == "1":
        movie = input("Enter a movie title: ").strip()
        if movie == "":
            print("Movie title cannot be empty.")
        else:
            movies.append(movie)
            print(f"Added '{movie}'.")

    elif choice == "2":
        if len(movies) == 0:
            print("No movies stored yet.")
        else:
            print("\nSaved movies:")
            for index, movie in enumerate(movies, start=1):
                print(f"{index}. {movie}")

    elif choice == "3":
        search_term = input("Search text: ").strip().lower()
        matches = []

        for movie in movies:
            if search_term in movie.lower():
                matches.append(movie)

        if len(matches) == 0:
            print("No matches found.")
        else:
            print("Matches:")
            for movie in matches:
                print(f"- {movie}")

    elif choice == "q":
        print("Goodbye!")
        running = False

    else:
        print("Invalid choice. Please select 1, 2, 3, or Q.")
```

---

## Appendix B: Instructor Whiteboard / Slide Outline

Use this if you want a fast visual summary during teaching.

### Board Sketch 1: Menu Loop Pattern

```text
while running:
    show menu
    get choice
    if/elif route action
    if quit -> stop loop
```

### Board Sketch 2: State Placement

```text
GOOD:
items = []
while running:
    ...

BAD:
while running:
    items = []
    ...
```

### Board Sketch 3: Core Question

```text
How do we keep the program alive
until the user chooses to stop?
```

---

## Appendix C: Common Student Bugs and Coaching Responses

### Bug: “My list is empty every time I go back to the menu.”
**Likely cause:** The list is being recreated inside the loop.  
**Coaching response:** “Show me where the list is initialized. Should that happen once, or every menu cycle?”

### Bug: “My quit option does nothing.”
**Likely cause:** The quit branch is missing, or the user input is not normalized.  
**Coaching response:** “What exact value are you checking for in the quit branch? What happens if the user types uppercase Q?”

### Bug: “I can search, but it never finds anything.”
**Likely cause:** Case mismatch or wrong comparison variable.  
**Coaching response:** “What two strings are you comparing? Are they in the same case?”

### Bug: “My menu disappears after one choice.”
**Likely cause:** Menu printing is outside the loop, or the loop ends too early.  
**Coaching response:** “Where is the print block for the menu? Does execution return there after each branch?”

---

## Appendix D: Stretch Discussion – Why Functions Help Later

**[Instructor speaks:]**

We are not formally teaching functions in this hour, but it is helpful to preview where this is going.

A menu program often starts small and becomes messy as it grows. For example, a long `if/elif` chain may contain:

- input prompts
- data updates
- loop logic
- output formatting

Later, functions help by allowing us to separate responsibilities.

For example:

```python
def add_movie(movies: list[str]) -> None:
    movie = input("Enter a movie title: ").strip()
    if movie == "":
        print("Movie title cannot be empty.")
    else:
        movies.append(movie)
        print(f"Added '{movie}'.")
```

Then the menu branch becomes:

```python
if choice == "1":
    add_movie(movies)
```

That is not required today, but it is valuable for students to hear that the pattern they are learning now will scale later.

---

## Appendix E: Additional Instructor Notes for Pacing and Support

### If the class is moving quickly

**[Instructor speaks:]**

If students understand the core pattern quickly, use the extra time to strengthen quality rather than immediately raising complexity.

Possible fast-finisher directions:

- improve output formatting
- make search case-insensitive
- add a confirmation message after list when no items exist
- add update or delete as optional features
- refactor one branch into a helper function as a preview

### If the class is moving slowly

Slow the pace and make the success target smaller:

- first get the menu printing repeatedly
- then get quit working
- then get one action working, such as add
- then add list
- only then attempt search

This preserves confidence. Students do not need a perfect polished app in the first 20 minutes. They need a stable mental model.

### If many students are stuck on branching

Re-center them on a paper model:

```text
choice == "1" -> add
choice == "2" -> list
choice == "3" -> search
choice == "q" -> quit
anything else -> invalid
```

Sometimes the clearest debugging step is not more code. It is writing the decision map in plain English.

---

## Appendix F: Quick Reference Card for Students

### Menu Loop Recipe

```python
items = []
running = True

while running:
    print("menu")
    choice = input("Choose: ").strip().lower()

    if choice == "1":
        ...
    elif choice == "2":
        ...
    elif choice == "q":
        running = False
    else:
        print("Invalid choice")
```

### Remember

- Print the menu **inside** the loop
- Create your shared list/dictionary **outside** the loop
- Use `if/elif/else` to route actions
- Normalize user input with `.strip()` and `.lower()`
- Make quit an explicit option
- Show helpful feedback after each action

---

**End of Day 4, Hour 1 Script / Course Hour 29**
