# Day 6, Hour 3: Mini-Project – In-Memory Tracker (Course Hour 23)
**Python Programming Basics – Session 6**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 6, Course Hour 23 – Mini-project: in-memory tracker  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided mini-project lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is a detailed read-aloud teaching guide for Course Hour 23. This hour is about synthesis. Learners should combine the data-structure ideas from Session 5 and the first half of Session 6 into one coherent mini application that runs completely in memory. Stay firmly within Basics scope: no file I/O, no classes, no external packages, and no advanced menu-loop architecture. The runbook allows several themes. For consistency and clarity, this script uses a **Book Library Tracker** built as a **list of dictionaries**. That model is pedagogically strong because each book is one record with named fields, and the outer list stores many records in order. Learners will add a record, list all records, and search records. Keep the project approachable. The point is not architectural perfection. The point is helping learners feel how multiple small skills fit together into a useful program. Every **Say:** block is written to be read nearly verbatim; adapt naturally, but keep the conceptual scaffolding and encouragement.

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Explain why a list of dictionaries is a good fit for a small in-memory tracker with multiple records.
2. Build a small tracker that stores records, adds a new record, lists all records, and searches records.
3. Read and write record fields using clear dictionary keys.
4. Loop through a list of records and format output cleanly with f-strings.
5. Describe one reason you chose this storage model instead of a different one."

---

## 1) Agenda + Timing

- **0:00–0:05** Frame the mini-project and define success
- **0:05–0:15** Choose a storage model and justify it
- **0:15–0:28** Live demo: scaffold data and one add action
- **0:28–0:47** Guided mini-project build: add, list, search
- **0:47–0:55** Debrief and walkthrough
- **0:55–1:00** Recap and exit ticket

---

## 2) Instructor Setup Checklist

- Open a clean file called `hour23_tracker_demo.py`.
- Open a second file called `hour23_book_tracker_lab.py` with section headers only.
- Prepare a starter dataset of three books.
- Make sure learners know this project is **in memory only**. No save/load yet.
- Decide in advance that the standard class version of the project will be the **Book Library Tracker**.
- Be ready to explain why a list of dictionaries fits better than a plain list of strings for this project.
- Prepare one example search that succeeds and one that fails.

**Say:** "This hour is where your data-structure skills start to feel like real application-building. We are going to build something small, but it will feel like a tiny program with real features instead of a one-line exercise."

---

## 3) Opening Script: From Isolated Patterns to a Coherent Program (~5 minutes)

### 3.1 Reconnect to earlier learning

**Say:**
"In Session 5, we learned the main built-in data structures. In Hour 21, we practiced choosing among them. In Hour 22, we drilled the core patterns quickly.

Now we are going to combine those ideas into one mini-project. This matters because real programs are rarely about one isolated line like `set(my_list)` or `counts[word] = counts.get(word, 0) + 1`. Real programs organize data, update it, print it clearly, and let the user ask useful questions."

### 3.2 Define the mini-project goal

**Say:**
"Our mini-project today is an **in-memory tracker**. ‘In memory’ means while the program is running, the data lives in Python variables. When the program stops, the data disappears. That is completely fine for today because our focus is structure, not saving files yet.

The tracker will let us:
- store records
- add a new record
- list all records
- search records

That is enough to feel like a real little application."

### 3.3 Why we are using a book tracker

**Say:**
"The runbook allows several themes like expenses, contacts, or a book library. Today we will use a **Book Library Tracker** because it gives us natural fields: title, author, and genre.

Each book is one record. Many books together form the collection. That immediately raises a design question: how should we store the data?"

---

## 4) Choosing the Storage Model (~10 minutes)

### 4.1 Option 1: A plain list of strings

**Say:**
"Before we write code, let’s compare a few possible storage models.

Option 1 is a plain list of strings."

```python
books = ["Dune", "1984", "The Hobbit"]
```

**Say:**
"This is simple, but it only stores one piece of information per book. The moment we also want author and genre, it stops fitting well."

### 4.2 Option 2: A dictionary mapping title to author

**Say:**
"Option 2 is a dictionary from title to author."

```python
books = {
    "Dune": "Frank Herbert",
    "1984": "George Orwell",
}
```

**Say:**
"This is better for lookup by title, but now where does genre go? We could make the value another dictionary, but that is a bigger jump than we need right now."

### 4.3 Option 3: A list of dictionaries

**Say:**
"Option 3 is a list of dictionaries."

```python
books = [
    {"title": "Dune", "author": "Frank Herbert", "genre": "Science Fiction"},
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian"},
]
```

**Say:**
"Now each book is one record with named fields, and the outer list stores many records in order. That is a very strong fit for our Basics mini-project.

- A list makes sense because we have many records.
- A dictionary makes sense because each record has named fields.
- The code stays readable.
- We can add, list, and search without introducing advanced ideas."

### 4.4 Name the design choice explicitly

**Say:**
"So our storage model is:

- **outer structure:** list
- **inner structure:** dictionary

That means: one list holds all books, and each book is a dictionary with keys like `title`, `author`, and `genre`."

### 4.5 Ask learners to justify it back

**Ask learners:**
"Why not just use one giant dictionary? Why might a list of dictionaries be a clearer teaching choice here?"

Take a few answers.

**Say:**
"Good. The important idea is that each book is a separate record, and the list keeps many records together cleanly."

---

## 5) Starter Data and Program Shape (~5 minutes)

### 5.1 Type the starter dataset

**Type and narrate:**

```python
books: list[dict[str, str]] = [
    {"title": "Dune", "author": "Frank Herbert", "genre": "Science Fiction"},
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "genre": "Fantasy"},
]
```

**Say:**
"This gives us three starting records so we have something to list and search before we even add new data. That is a good development habit: give yourself realistic starter data so you can test features quickly."

### 5.2 Preview the three required features

**Say:**
"Our tracker only needs three minimum features today:

1. **Add** a book
2. **List** all books
3. **Search** for a book by title

That is intentionally modest. A project becomes much easier when the minimum requirements are clear."

### 5.3 The “simple first” teaching principle

**Say:**
"We are not building a full menu loop today unless you want it as an extension later. We are going to keep the project linear and simple so the focus stays on data structures and clean thinking."

---

## 6) Live Demo: Scaffold the Tracker and Build the Add Feature (~13 minutes)

### 6.1 Frame the live demo

**Say:**
"I am going to build the first feature live: adding a new book. As I type, pay attention to what information belongs in the dictionary and what belongs in the outer list."

### 6.2 Type the add feature

**Type:**

```python
new_title: str = input("Enter a book title: ")
new_author: str = input("Enter the author: ")
new_genre: str = input("Enter the genre: ")

new_book: dict[str, str] = {
    "title": new_title,
    "author": new_author,
    "genre": new_genre,
}

books.append(new_book)
print("Book added.")
```

### 6.3 Narrate the structure carefully

**Say:**
"Let me say the structure out loud.

- We ask the user for three text values.
- We create one dictionary called `new_book`.
- The keys are field names: `title`, `author`, and `genre`.
- The values come from the user.
- Then we append that whole dictionary to the outer list.

So the list stores records, and each record stores named fields."

### 6.4 Test immediately

**Say:**
"Never trust a feature you have not tested. I am going to enter one sample book right now."

Run it with a sample such as:
- title: `Pride and Prejudice`
- author: `Jane Austen`
- genre: `Classic`

### 6.5 Confirm the data changed

**Type:**

```python
print(books)
```

**Say:**
"For debugging, printing the raw data structure is fine. For final user-facing output, we want cleaner formatting. That leads us into the next feature: listing all books clearly."

---

## 7) Core Teaching Section: Build a Clear List Feature (~8 minutes)

### 7.1 Explain why formatting matters

**Say:**
"One habit beginners often need to develop is the difference between *debug output* and *user-friendly output*.

Debug output is printing the raw list or raw dictionary to inspect what is inside.
User-friendly output is formatting the information in a way a person can read easily.

Both are useful, but they are not the same thing."

### 7.2 Type the list feature

**Type:**

```python
print("\nLibrary books:")
for book in books:
    print(f"- {book['title']} by {book['author']} ({book['genre']})")
```

### 7.3 Narrate the loop

**Say:**
"This loop is a good example of nested thinking that is still beginner-friendly.

- The outer structure is a list, so we loop through it.
- Each `book` is a dictionary.
- Inside the loop, we access the fields by key.
- Then we format the output with an f-string.

This is one of the first moments where data structures start to feel genuinely useful together."

### 7.4 Ask learners to predict output

**Ask learners:**
"What do you think will print now that we added one more book?"

Run it.

### 7.5 Discuss readability

**Say:**
"Notice how much easier this is to read than printing the raw list of dictionaries. The data structure is the same. What changed is the way we present it."

---

## 8) Core Teaching Section: Build a Search Feature (~9 minutes)

### 8.1 Frame the search requirement

**Say:**
"Now let’s add the third feature: search by title. This feature is especially valuable because it turns our program from static output into something the user can ask a question of."

### 8.2 Keep the search logic simple

**Say:**
"Because our outer structure is a list, searching means looping through the books and comparing each title.

Could we design the data differently to make title lookup more direct? Yes, with a dictionary keyed by title. But for today’s project, the list-of-dicts model is easier to understand and more flexible for multiple fields."

### 8.3 Type the search feature

**Type:**

```python
search_title: str = input("\nEnter a title to search for: ")
found: bool = False

for book in books:
    if book["title"].lower() == search_title.lower():
        print("Found book:")
        print(f"  Title:  {book['title']}")
        print(f"  Author: {book['author']}")
        print(f"  Genre:  {book['genre']}")
        found = True
        break

if not found:
    print("Book not found.")
```

### 8.4 Explain the case-normalization choice

**Say:**
"Notice that I used `.lower()` on both sides of the comparison. That means if the stored title is `Dune` and the user types `dune`, the search still works. That is a small Basics-level improvement that makes the program friendlier."

### 8.5 Explain the `found` flag

**Say:**
"The `found` variable starts as `False`. If we find a matching book, we print it, set `found = True`, and break out of the loop. After the loop, if `found` is still `False`, we print `Book not found.`

That is a standard beginner-friendly search pattern."

### 8.6 Test both outcomes

Run once with an existing title and once with a missing title.

**Say:**
"Always test both the success path and the failure path. Real programs need both."

---

## 9) Guided Lab: Build Your Own Tracker Version (~19 minutes)

### 9.1 Lab framing

**Say:**
"Now it is your turn. You will build your own in-memory book tracker. You can follow the class version closely, but you should type it yourself and make sure you understand the role of each structure."

### 9.2 Lab prompt

### Mini-Project — Book Library Tracker (In Memory)

Build a small Python program that stores books using a **list of dictionaries**.

Each book record must include:
- `title`
- `author`
- `genre`

Your program must do the following:
1. Start with at least **three** book records already in the list.
2. Ask the user for one new book and add it to the list.
3. Print all books in a clean, readable format.
4. Ask the user for a title to search.
5. Print the matching book if found, or a clear message if not found.

### 9.3 Completion criteria

```text
Completion criteria
```

- Uses at least one list and one dictionary meaningfully.
- Starts with at least three records.
- Adds a new record correctly.
- Lists all records clearly using formatted output.
- Search works for both found and not-found cases.
- Code remains in Basics scope and runs without crashing.

### 9.4 Suggested build order for learners

**Say:**
"A strong build order is:

1. Create the starter list of dictionaries.
2. Test printing the raw data.
3. Add one new dictionary and append it.
4. Build the formatted list output.
5. Build the search feature last.

That order keeps the project manageable."

### 9.5 Hints to release after a few minutes

**Say:**
"A few helpful reminders:

- The list holds many books.
- Each book is one dictionary.
- When listing books, loop through the list.
- When searching, compare the user input to `book['title']`.
- If your code is getting tangled, comment out the last part and get one feature working at a time."

### 9.6 Common pitfalls to watch for

```text
Common pitfalls to watch for
```

- Storing each new book as a list instead of a dictionary
- Using different key names in different records, such as `name` in one place and `title` in another
- Printing the raw list and thinking the formatting requirement is complete
- Forgetting to set or check the `found` flag in the search logic
- Comparing titles without normalizing case and then assuming search is broken
- Creating the new book but forgetting to append it to `books`

### 9.7 Optional extensions for early finishers

```text
Optional extensions (stay in Basics scope)
```

- Add a `year` field as a string or integer.
- Sort the books by title before printing, if appropriate for your learners.
- Add a simple update feature such as changing the genre of a searched book.
- Add a delete-by-title feature using a loop and `pop()` or `remove()` carefully.
- Wrap listing and searching into small functions if learners are already comfortable previewing function ideas, but do not require it in this hour.

### 9.8 Instructor circulation prompts

Use short coaching questions:

**Say:**
"Which part of your data is the collection of records, and which part is one record?"

**Say:**
"If I point at one `book`, what type is it? What keys does it have?"

**Say:**
"Show me where the new dictionary gets appended to the list."

**Say:**
"Can your search handle a title that does not exist yet? Test that before you call it finished."

---

## 10) Debrief and Walkthrough (~8 minutes)

### 10.1 Invite a few learners to share

**Say:**
"Let’s come back together. I want to hear from a few people about what storage model you used and why it made sense."

Even though the standard model is list of dictionaries, some learners may have experimented. Invite short shares.

### 10.2 Model the reasoning explicitly

**Say:**
"A strong explanation sounds like this: ‘I used a list of dictionaries because I had many books, and each book had multiple named fields. The list let me store many records, and the dictionary made each record readable.’

That kind of explanation shows design understanding, not just code copying."

### 10.3 Highlight good output habits

**Say:**
"I also want to praise anyone who moved beyond printing the raw structure and created readable output. That is an underrated programming skill. Programs are for people, not just for Python."

### 10.4 Normalize partial completion

**Say:**
"If you completed add and list but your search is still shaky, that is still useful progress. Make a note of exactly where the search logic got confusing. That gives you a clear practice target."

---

## 11) Recap + Exit Ticket (~5 minutes)

### 11.1 Recap the main lessons

**Say:**
"Today’s big lesson was that data structures become much more meaningful when they work together.

We used:
- a **list** to hold many records
- a **dictionary** to represent one record with named fields
- a **loop** to list records
- a simple search pattern to find one matching record

That is a very real slice of application-building."

### 11.2 Exit ticket

```text
Quick check / exit ticket
```

Ask learners one or more of these:

1. Why was a list of dictionaries a good fit for this tracker?
2. What is one advantage of named dictionary keys like `title` and `author`?
3. What part of the mini-project felt easiest? What part felt hardest?
4. If you changed the project theme to contacts or expenses, what would stay structurally the same?

### 11.3 Bridge to Hour 24

**Say:**
"In the next hour, you will use these data-structure skills in Checkpoint 3. The checkpoint task is simpler than today’s mini-project, but it will ask you to work independently and safely — especially with dictionary access."

---

## 12) Guided Build Milestones for the Lab Block

### 12.1 Why milestones help beginners

**Say:**
"When learners build a mini-project, one of the easiest ways for them to get overwhelmed is to think of the whole project as one giant task. Milestones solve that problem. They turn one mini-project into several smaller wins."

### 12.2 Milestone 1 — Define the starting data

**Say:**
"The first milestone is simply getting the starter list of dictionaries written correctly. If a learner completes this part, they already have a meaningful data model. Encourage them to print the raw structure once and confirm that every book has the same keys."

Checklist for Milestone 1:
- `books` is a list
- each item in `books` is a dictionary
- every dictionary has `title`, `author`, and `genre`
- the code runs before adding any user input

### 12.3 Milestone 2 — Add one new record

**Say:**
"The second milestone is collecting user input and creating one new dictionary. Beginners often understand the overall project but get tangled right at the moment when several input values need to become one record. Slow them down here."

Coaching language:

**Say:**
"What are the three values you need from the user? Good. Now place those three values into one dictionary. Only after that do you append it to the list."

### 12.4 Milestone 3 — Print all records clearly

**Say:**
"The third milestone is readable output. This is where the project starts to feel satisfying, because learners can see all of their records printed cleanly."

Ask:
- "What does one line of output for one book need to include?"
- "Can someone reading your screen understand the data without seeing the raw dictionary syntax?"

### 12.5 Milestone 4 — Search successfully

**Say:**
"The fourth milestone is a successful search for an existing title. I recommend getting the found-case working before worrying about the not-found case."

### 12.6 Milestone 5 — Handle not-found safely

**Say:**
"The fifth milestone is the complete search feature: existing title works, missing title gives a clear message, and the program does not crash. That is often the moment when the project becomes truly complete."

### 12.7 Why this matters for learner confidence

**Say:**
"Milestones matter because they let learners say, 'I have part of it working.' That is much more motivating than feeling like everything is broken just because the final feature is not complete yet."

---

## 13) Troubleshooting and Coaching Guide for the Mini-Project

### 13.1 If a learner uses inconsistent keys

**Say:**
"One of the most common bugs in record-based projects is inconsistent key naming. A learner may use `title` in one dictionary and `book_title` in another, or `author` in one place and `writer` in another. When that happens, the loop logic looks broken even though the real problem is inconsistent structure."

Coaching prompt:

**Say:**
"Pick one book record and read its keys out loud. Now compare that to the keys your print or search code expects. Do they match exactly?"

### 13.2 If a learner stores books as lists instead of dictionaries

**Say:**
"Sometimes learners fall back to a list like `['Dune', 'Frank Herbert', 'Science Fiction']`. That can work, but it is harder to read and much easier to misuse because the meaning depends on remembering positions."

Use this coaching line:

**Say:**
"Right now your code depends on remembering that index 0 means title, index 1 means author, and index 2 means genre. Would named keys make that clearer?"

### 13.3 If a learner prints only the raw data

**Say:**
"Do not scold raw-data printing. It is useful for debugging. Instead, distinguish between debugging output and final output."

Coaching line:

**Say:**
"Printing the raw list showed you the structure, which is good. Now what would a person-friendly version look like if this were a real little app?"

### 13.4 If the search logic never finds a match

**Say:**
"Common causes include:
- comparing to the wrong key
- case mismatch
- searching before the new record was appended
- indentation that places the `if not found` logic inside the loop"

Ask:
- "What exact value is stored under `book['title']`?"
- "What exact value did the user type?"
- "Where does your `break` happen?"

### 13.5 If the learner’s code is getting too tangled

**Say:**
"Encourage them to comment out the unfinished feature and return to the last working version. A stable partial solution is much more useful than a fully tangled file."

### 13.6 If a learner finishes very early

**Say:**
"Give them a meaningful extension, not just extra typing. Good extensions include:
- add a `year` field
- add an update feature
- sort by title before listing
- count how many books are in each genre using a dictionary"

This keeps the work in scope while still stretching strong learners.

### 13.7 If a learner is behind

**Say:**
"Reduce the goal temporarily. Ask them to complete just three things:

1. one correct starter list
2. one successful append
3. one readable listing loop

Once those work, search becomes much easier to add."

---

## 14) Debrief Extension: Make the Design Reasoning Explicit

### 14.1 Questions to ask during debrief

Use some of these prompts:

- "Why was the outer structure a list?"
- "Why was each individual book a dictionary?"
- "What did named keys make easier?"
- "What was the hardest part: add, list, or search?"
- "If you changed the project to contacts or expenses, what structure would stay the same?"

### 14.2 Model the transfer to other themes

**Say:**
"One reason this mini-project matters is that the structure generalizes. If I replace books with contacts, each record still has named fields. If I replace books with expenses, each record still has named fields. The exact field names change, but the design pattern remains useful."

### 14.3 Highlight the project’s hidden lesson

**Say:**
"The hidden lesson today is that programs become easier to reason about when the data shape matches the real-world shape of the problem. We had many books, so we used a list. Each book had named facts, so we used a dictionary. That is good modeling at a beginner level."

---

## 15) Appendix: Instructor Quick Reference

### 12.1 Why this project is still firmly Basics-level

**Say:**
"This project is still firmly in Basics scope because it uses only the tools learners already know: lists, dictionaries, loops, `input()`, conditionals, string methods, and formatted printing. No file handling, no classes, no external libraries."

### 12.2 Acceptable variations during the lab

If a learner chooses a different runbook-approved theme such as contacts, expenses, or a simple book list, that is acceptable if the program still:

- stores records in memory
- uses at least one list and one dictionary meaningfully
- includes add, list, and search
- prints readable output

### 12.3 Compact reminder pattern for a record-based tracker

```python
records = [
    {"field1": "value1", "field2": "value2"},
]

new_record = {"field1": user_value1, "field2": user_value2}
records.append(new_record)

for record in records:
    print(record["field1"])
```

**Say:**
"Again, do not treat this as a magic template. Treat it as a pattern you can adapt when you have many records and each record has named fields."
