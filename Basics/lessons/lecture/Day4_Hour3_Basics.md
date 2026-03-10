# Day 4, Hour 3: Mini-Project – CLI Contact Manager (In-Memory)
**Python Programming Basics – Day 4 / Session 8 / Course Hour 31**

---

## Subtitle
**Combining loops, conditionals, lists, dictionaries, and user-friendly messaging into a functional mini-project**

**Instructor framing:** This is the standalone script for **Day 4, Hour 3**, aligned to **Course Hour 31** in the runbook. It asks students to integrate multiple Basics skills in one coherent CLI application. The program is intentionally **in-memory only**—no files yet—so the focus stays on control flow, data structures, and user experience.

---

## Timing Overview
**Total Time:** 60 minutes  
- Recap & transition from input validation: 5 minutes  
- Project framing and required features: 8 minutes  
- Choosing a data structure and planning the build: 10 minutes  
- Clean CLI messaging and testing habits: 7 minutes  
- Live Demo – implement add + list quickly: 10 minutes  
- Hands-On Lab – Contact Manager build: 15 minutes  
- Debrief & Exit Ticket: 5 minutes  

---

## Learning Outcomes for This Hour

By the end of this hour, learners will be able to:
1. Combine loops, lists or dictionaries, and conditionals into a functional CLI program
2. Build a looped menu that supports multiple user actions in one run
3. Store contact data in memory using an appropriate structure
4. Add, list, search, and delete contacts by name
5. Avoid crashing when a searched or deleted contact does not exist
6. Use clear prompts, confirmations, and friendly user-facing messages
7. Follow an incremental build strategy instead of trying to write the whole program at once

---

## Section 1: Recap & Transition from Hour 30 (5 minutes)

### Connecting the Pieces

**[Instructor speaks:]**

In **Day 4, Hour 2 / Course Hour 30**, students practiced a vital habit: validating user input before converting or using it. That means they now have two key ingredients for interactive programs:

- a menu loop structure
- basic input validation and re-prompting

Now we move into a mini-project where those skills come together with data structures.

This is an exciting hour because it feels more like building a “real program.”

### Why This Project Matters

**[Instructor speaks:]**

A lot of beginner exercises are small and isolated. That is useful early on, but learners also need moments where they can say:

> “I can build a complete little tool from start to finish.”

The contact manager gives them that experience.

It is still simple, but it includes everything we want at this point in the Basics course:

- menu choices
- repeated actions
- stored data
- search behavior
- deletion behavior
- handling missing values politely
- clearer user experience messages

### Warm-Up Prompt

**[Instructor asks:]**

If you had to build this contact manager in one sentence, what should it do?

Guide answers toward:

- let the user add contacts
- show all contacts
- search by name
- delete by name
- keep going until quit

---

## Section 2: Define the Required Features (8 minutes)

### The Core Requirement Set

**[Instructor speaks:]**

Let’s make the requirements concrete. Our **CLI Contact Manager** must support these required actions:

1. **Add contact**
   - collect a name
   - collect a phone number
   - store the contact in memory

2. **List contacts**
   - display all saved contacts clearly

3. **Search by name**
   - let the user type a name or search text
   - show the match if found
   - do **not** crash if no match exists

4. **Delete by name**
   - remove a contact by name
   - confirm deletion or explain that no match was found

5. **Quit**
   - stop the program cleanly

### Important Scope Reminder

**[Instructor speaks:]**

This project is **in-memory only**.

That means:

- data exists while the program is running
- data disappears when the program ends

That is okay. In fact, it is helpful for the learning stage we are in. We do **not** want to distract students with file saving yet.

### Clean UX Messaging

**[Instructor speaks:]**

The runbook also emphasizes **clear prompts and confirmations**. That matters.

Compare these two styles.

**Weak UX:**

```text
Input:
Done
```

**Better UX:**

```text
Enter contact name: 
Contact added successfully.
```

Students should learn that clarity is part of correctness in user-facing programs.

### Required vs Optional Features

**[Instructor speaks:]**

Required today:

- add
- list
- search
- delete
- loop until quit

Optional if time allows:

- update phone number
- normalize names
- duplicate detection

Keep students focused on getting the required version working first.

---

## Section 3: Choosing a Data Structure and Planning the Build (10 minutes)

### Reasoning About Structure

**[Instructor speaks:]**

One of the best things about this project is that students must decide how to represent data.

There are two natural options:

- a **dictionary** mapping names to phone numbers
- a **list of dictionaries** such as `[{"name": "Ava", "phone": "555-1234"}]`

### Option 1: Dictionary of Name → Phone

```python
contacts = {
    "Ava": "555-1234",
    "Leo": "555-8888",
}
```

**Advantages:**
- simple lookups by exact name
- simple updates
- simple deletes

**Tradeoffs:**
- duplicate names become awkward
- search by partial text requires extra logic
- case sensitivity needs attention

### Option 2: List of Dictionaries

```python
contacts = [
    {"name": "Ava", "phone": "555-1234"},
    {"name": "Leo", "phone": "555-8888"},
]
```

**Advantages:**
- each contact is a clear record
- easier to extend later with email, city, tags, etc.
- nice practice with lists and dictionaries together

**Tradeoffs:**
- exact lookup is a bit more manual
- deleting requires careful search logic

### Recommendation for This Hour

**[Instructor speaks:]**

For teaching purposes, I recommend the **list of dictionaries** approach in the live demo because it gives richer practice with data structures and loop logic.

However, if a student clearly prefers a dictionary and can meet the requirements, that is still within scope. The important thing is that the program works and that the student can explain the structure.

### Incremental Build Strategy

**[Instructor speaks:]**

A huge beginner mistake is trying to write the whole project in one pass. Instead, model the build order from the runbook:

1. menu
2. add
3. list
4. search
5. delete

That order matters because each step gives us something testable.

### Why This Order Works

- **Menu first** gives us the shell of the program
- **Add** gives us data to work with
- **List** helps us verify stored data visually
- **Search** builds on data access
- **Delete** adds mutation and careful checks

That is disciplined program construction.

### Prediction Prompt

**[Instructor asks:]**

If you try to build delete before add and list, what problem might you have while testing?

[Expected answer: there may be no data to delete, so it is harder to verify behavior or understand bugs.]

---

## Section 4: Clean CLI Messaging and Testing Strategy (7 minutes)

### Good Programs Explain What Happened

**[Instructor speaks:]**

We want students to go beyond “it technically runs.”

A contact manager should communicate clearly:

- when a contact is added
- when no contacts exist yet
- when a search finds a match
- when a search does not find a match
- when deletion succeeds
- when deletion cannot happen because the name does not exist

### Example of Friendly Messaging

```python
print(f"Added contact for {name}.")
print("No contacts saved yet.")
print(f"No contact found for '{search_name}'.")
print(f"Deleted contact for {name}.")
```

These messages help both the user and the programmer.

### Testing Strategy to Model

**[Instructor speaks:]**

Before students begin the lab, show that testing is not random. Use a quick checklist:

1. Add one contact
2. Add a second contact
3. List contacts
4. Search for an exact match
5. Search for something missing
6. Delete an existing contact
7. Delete a missing contact
8. Quit

This checklist gives students a sequence they can follow instead of guessing what to test.

### Common Risk Areas to Name Explicitly

**[Instructor speaks:]**

Call out two common pitfalls from the runbook:

- **case sensitivity**
- **deleting while iterating**

Explain them clearly.

#### Case sensitivity
If a contact is stored as `Ava` and the user searches for `ava`, an exact comparison may fail unless both sides are normalized.

#### Deleting while iterating
If a student loops through a list and removes items carelessly inside that loop, behavior can become confusing. In Basics, a clean approach is often:

- find the index to remove
- delete once after locating the match

or

- break immediately after removing the matching contact

---

## Section 5: Live Demo – Add + List First, Then Explain Testing (10 minutes)

### Demo Goal

**[Instructor speaks:]**

I will not build the entire project live from top to bottom. Instead, I will model the important early steps quickly:

- create the menu
- implement add
- implement list
- explain how that gives us a strong starting point for the rest

### Live Demo Code

```python
# contact_manager_demo.py
# Day 4, Hour 3 demo: start a contact manager

contacts: list[dict[str, str]] = []
running = True

while running:
    print("\n=== Contact Manager ===")
    print("1. Add contact")
    print("2. List contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("Q. Quit")

    choice = input("Choose an option: ").strip().lower()

    if choice == "1":
        name = input("Enter contact name: ").strip()
        phone = input("Enter phone number: ").strip()

        if name == "":
            print("Name cannot be empty.")
        elif phone == "":
            print("Phone number cannot be empty.")
        else:
            contact = {"name": name, "phone": phone}
            contacts.append(contact)
            print(f"Added contact for {name}.")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts saved yet.")
        else:
            print("\nSaved contacts:")
            for index, contact in enumerate(contacts, start=1):
                print(f"{index}. {contact['name']} - {contact['phone']}")

    elif choice == "3":
        print("Search feature coming next.")

    elif choice == "4":
        print("Delete feature coming next.")

    elif choice == "q":
        print("Goodbye!")
        running = False

    else:
        print("Invalid choice. Please select 1, 2, 3, 4, or Q.")
```

### Narration Notes

**[Instructor speaks:]**

As you type, narrate these ideas:

- “I am using a list of dictionaries because each contact has two fields.”
- “I am validating empty names and phone numbers with simple checks.”
- “I am implementing add before search/delete because I need sample data first.”
- “My list display is giving me a quick visual test that contacts are stored correctly.”

### Demo Testing in Front of Students

Run these quick cases live:

1. List contacts before adding any  
2. Add `Ava / 555-1234`  
3. Add `Leo / 555-8888`  
4. List contacts again  
5. Choose an invalid menu option  

Then say explicitly:

**[Instructor speaks:]**

“At this point, I already trust my foundation more, because I can prove add and list work before I build search and delete.”

That sentence models an excellent project habit.

---

## Section 6: Hands-On Lab – Build the CLI Contact Manager (15 minutes setup + work time)

### Lab Prompt

**Lab: Contact Manager (In-Memory)**

Build a command-line contact manager that stores contacts in memory while the program is running.

### Required Features

Your program must include:

- **Add contact** (`name`, `phone`)
- **List contacts**
- **Search by name**
- **Delete by name**
- **Menu loop until quit**

### Functional Requirements in Plain Language

1. **Add contact**
   - Ask for a name and phone number
   - Save the contact
   - Confirm success

2. **List contacts**
   - Show all contacts clearly
   - If no contacts exist, say so

3. **Search by name**
   - Ask for a name or search text
   - Show matching contact(s)
   - Do not crash if the name is not found

4. **Delete by name**
   - Ask for the name to delete
   - Remove the matching contact if it exists
   - If it does not exist, show a clear message

5. **Quit**
   - End the loop cleanly

### Completion Criteria

A student solution is complete when:

- ✅ all required actions work  
- ✅ the program does not raise `KeyError` for a missing name  
- ✅ the menu repeats until quit  
- ✅ prompts and confirmations are clear  
- ✅ contact data persists in memory during the run  

### Suggested Build Order for Students

Encourage them to build in this sequence:

1. menu shell
2. add
3. list
4. search
5. delete
6. polish messages

### Search Guidance

Students may choose exact matching or case-insensitive substring matching. Either is acceptable if they can explain it clearly and it behaves consistently.

A case-insensitive substring version looks like this:

```python
search_name = input("Enter name to search: ").strip().lower()

for contact in contacts:
    if search_name in contact["name"].lower():
        print(f"Found: {contact['name']} - {contact['phone']}")
```

### Delete Guidance

A beginner-friendly delete pattern with a list of dictionaries:

```python
delete_name = input("Enter name to delete: ").strip().lower()
found_index = -1

for index, contact in enumerate(contacts):
    if contact["name"].lower() == delete_name:
        found_index = index
        break

if found_index != -1:
    removed_contact = contacts.pop(found_index)
    print(f"Deleted contact for {removed_contact['name']}.")
else:
    print("No matching contact found.")
```

This avoids deleting repeatedly while scanning the list.

### Optional Extensions

If students finish early, they may add:

- update phone number
- normalize names
- duplicate detection

### Coaching Prompts While Circulating

**[Instructor speaks:]**

Use prompts like:

- “What structure are you using for contacts, and why?”
- “What happens if the name is not found?”
- “Can your user tell whether an action succeeded?”
- “How are you avoiding a missing-key or missing-name crash?”
- “How are you testing search and delete?”

These prompts keep the work student-owned while still guiding quality.

---

## Section 7: Debrief & Exit Ticket (5 minutes)

### Debrief Questions

**[Instructor asks:]**

- Which feature took the most time: add, list, search, or delete?
- What bug appeared most often?
- How did you test missing-name behavior?
- What design choice did you make for contact storage?

### Instructor Synthesis

**[Instructor speaks:]**

This mini-project is important because students are no longer just practicing isolated syntax. They are creating a coherent tool that has:

- a repeated interface
- stored records
- multiple actions
- polite failure handling
- visible program flow

That is a significant jump in competence.

### Exit Ticket

**[Instructor asks:]**

Answer in one or two sentences:

**What was the hardest bug you hit in the menu loop or contact logic, and how did you approach fixing it?**

The goal is to build reflection, not just produce code.

---

## Recap: What We Accomplished in Day 4, Hour 3 / Course Hour 31

In this hour, learners:

- combined loops and data structures in a real CLI mini-project
- practiced an incremental build strategy
- added, listed, searched, and deleted in-memory contact data
- avoided missing-name crashes
- improved user-facing prompts and confirmation messages
- experienced a fuller sense of “I built a program”

**[Instructor speaks:]**

This hour sets up the assessment mindset for the next block. In **Day 4, Hour 4 / Course Hour 32**, students will demonstrate these control-flow skills in a structured checkpoint: a **CLI To-Do Manager**.

---

## Appendix A: Instructor Exemplar Solution

```python
# contact_manager.py
# In-memory contact manager

contacts: list[dict[str, str]] = []
running = True

while running:
    print("\n=== Contact Manager ===")
    print("1. Add contact")
    print("2. List contacts")
    print("3. Search by name")
    print("4. Delete by name")
    print("Q. Quit")

    choice = input("Choose an option: ").strip().lower()

    if choice == "1":
        name = input("Enter contact name: ").strip()
        phone = input("Enter phone number: ").strip()

        if name == "":
            print("Name cannot be empty.")
        elif phone == "":
            print("Phone number cannot be empty.")
        else:
            contacts.append({"name": name, "phone": phone})
            print(f"Added contact for {name}.")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts saved yet.")
        else:
            print("\nSaved contacts:")
            for index, contact in enumerate(contacts, start=1):
                print(f"{index}. {contact['name']} - {contact['phone']}")

    elif choice == "3":
        search_text = input("Enter name to search: ").strip().lower()
        matches = []

        for contact in contacts:
            if search_text in contact["name"].lower():
                matches.append(contact)

        if len(matches) == 0:
            print("No matching contacts found.")
        else:
            print("Matches:")
            for contact in matches:
                print(f"- {contact['name']} - {contact['phone']}")

    elif choice == "4":
        delete_name = input("Enter exact name to delete: ").strip().lower()
        found_index = -1

        for index, contact in enumerate(contacts):
            if contact["name"].lower() == delete_name:
                found_index = index
                break

        if found_index != -1:
            removed_contact = contacts.pop(found_index)
            print(f"Deleted contact for {removed_contact['name']}.")
        else:
            print("No matching contact found.")

    elif choice == "q":
        print("Goodbye!")
        running = False

    else:
        print("Invalid choice. Please select 1, 2, 3, 4, or Q.")
```

---

## Appendix B: Case Sensitivity Teaching Notes

Case sensitivity is one of the easiest ways for students to accidentally write a program that “works” but feels unreliable.

Example issue:

- Stored name: `Ava`
- User searches: `ava`
- Exact case-sensitive comparison fails

A simple fix is to compare lowercase versions:

```python
if contact["name"].lower() == search_name.lower():
```

Or for substring matching:

```python
if search_text.lower() in contact["name"].lower():
```

This is a nice place to remind students that computers are literal, so part of our job is to normalize data when appropriate.

---

## Appendix C: Duplicate Name Discussion

Students may discover the duplicate-name problem naturally.

Example:

- Add `Alex / 555-1000`
- Add `Alex / 555-9000`

Now what should search or delete do?

At the Basics level, there are several acceptable responses:

1. allow duplicates and return multiple matches
2. warn and refuse duplicates
3. require exact delete behavior and remove the first match only

Do not let this derail the hour. Acknowledge it as a real design question and keep the class anchored to the required features.

---

## Appendix D: Common Student Bugs and Debugging Coaching

### Bug: `KeyError`
**Likely cause:** Wrong dictionary key such as `contact['phone_number']` when the stored key is `phone`.  
**Coaching response:** “What are the exact keys in the contact dictionary? Can you print one contact record?”

### Bug: Search never finds a match
**Likely cause:** Case mismatch or comparing the wrong variable.  
**Coaching response:** “What two strings are you comparing? Are you normalizing both?”

### Bug: Delete removes the wrong item
**Likely cause:** Confusion around indices or reuse of stale variables.  
**Coaching response:** “What contact did you match, and what index are you popping?”

### Bug: Delete crashes when nothing matches
**Likely cause:** Program assumes a contact exists without checking.  
**Coaching response:** “What value tells you that a match was found? What happens if no match is found?”

### Bug: List display is unreadable
**Likely cause:** Printing the raw list instead of formatting each contact.  
**Coaching response:** “What would a user want to read? Can you print one contact per line?”

---

## Appendix E: Suggested Manual Test Checklist

Use or share this checklist during the lab or debrief.

- [ ] Start program and list contacts while empty
- [ ] Add one contact and verify confirmation
- [ ] Add second contact and list all
- [ ] Search for existing contact
- [ ] Search for missing contact
- [ ] Delete existing contact
- [ ] Try deleting same contact again
- [ ] Use invalid menu choice
- [ ] Quit cleanly

This checklist teaches students that testing should cover both happy paths and edge cases.

---

## Appendix F: Additional Instructor Scaffolds

### If students are overwhelmed by the full project

Shrink the problem visibly:

1. First get the menu to repeat
2. Then make add work
3. Then make list work
4. Only after that move to search
5. Delete comes last

Write that sequence on the board. Many students calm down when the “big project” becomes a series of manageable checkpoints.

### If students want to use a dictionary instead

That is fine if they can still meet the requirements.

Example:

```python
contacts = {}
contacts[name] = phone
```

Then search/delete can use exact names. Remind them that duplicate names become a design tradeoff with this structure.

### If students finish early

Use polish prompts rather than immediately adding complexity:

- “Can your messages be clearer?”
- “Can search be case-insensitive?”
- “Can you add update phone as an optional feature?”
- “Can you reduce duplicate contact confusion?”

This keeps advanced students engaged while protecting the main learning target.

---

## Appendix G: Quick Reference Card for Students

### Contact Manager Build Order

```text
1. Menu
2. Add
3. List
4. Search
5. Delete
6. Polish messages
```

### Good CLI Messages

- “Added contact for Ava.”
- “No contacts saved yet.”
- “No matching contact found.”
- “Deleted contact for Leo.”

### Remember

- store contacts outside the loop
- keep the menu repeating until quit
- handle missing names without crashing
- test each feature right after building it
- clear prompts and confirmations matter

---

## Appendix H: Instructor Build-Along Script in Plain English

Use this appendix if you want a more detailed verbal walkthrough while circulating or while re-teaching to students who are stuck.

### Step 1: Build the shell first

**[Instructor speaks:]**

“Before we worry about storing a single contact, let’s make the skeleton of the program stable. I want a menu. I want a loop. I want quit to work. If those three things are solid, the rest becomes much easier.”

Suggested micro-goals:

1. print the menu
2. read the choice
3. handle invalid choice
4. quit cleanly

### Step 2: Add one contact feature and test immediately

**[Instructor speaks:]**

“Now I am not building everything. I am building one branch. Add contact. As soon as that branch works once, I test it. Then I move on.”

This is worth repeating because many beginners write three branches before testing even one of them.

### Step 3: Add list as the visual proof

**[Instructor speaks:]**

“Listing is not just a feature. It is also a debugging tool. If I can add a contact and then list contacts, I can see whether my stored data structure actually contains what I think it contains.”

### Step 4: Add search with polite missing-case behavior

**[Instructor speaks:]**

“A search feature should not crash or stay silent. If nothing matches, say so clearly.”

That sentence helps students think about user experience instead of only code paths.

### Step 5: Add delete carefully

**[Instructor speaks:]**

“Delete is where state changes, so this is where many bugs appear. I want to know exactly what I matched before I remove anything.”

Encourage students to print or inspect the match before deleting if they are unsure.

---

## Appendix I: Mini Debugging Cases Specific to Contact Managers

### Case 1: Contact added, but list shows nothing

Possible causes:
- the list was reset inside the loop
- the contact was never appended
- the student appended the wrong variable

Coaching prompt:

**[Instructor speaks:]**

“Show me the exact line where the contact gets added. What is the name of the list? Can we print the list right after append?”

### Case 2: Search only works when capitalization matches exactly

Possible cause:
- comparison is case-sensitive

Coaching prompt:

**[Instructor speaks:]**

“What happens if we convert both the stored name and the search text to lowercase before comparing?”

### Case 3: Delete crashes on a missing name

Possible cause:
- code assumes a match exists

Coaching prompt:

**[Instructor speaks:]**

“What variable tells you that you found a match? What should the code do if that value never changes?”

### Case 4: `KeyError` appears during list or search

Possible cause:
- contact dictionary keys are inconsistent

Coaching prompt:

**[Instructor speaks:]**

“Let’s print one contact record exactly as stored. Are your keys always `name` and `phone`, or do they change in different parts of the program?”

### Case 5: Duplicate contacts create confusing behavior

Possible cause:
- two entries share the same name

Coaching prompt:

**[Instructor speaks:]**

“For this hour, it is okay to choose a simple rule. Will you allow duplicates, reject them, or delete the first exact match? Pick one rule and make it clear.”

---

## Appendix J: Additional Debrief Prompts for a Stronger Wrap-Up

If time allows, use one or two of these questions after the lab.

- “Which feature gave you the clearest evidence that your data structure was working?”
- “How did you make your program more understandable for the user?”
- “What did you learn about building in small steps?”
- “If you had ten more minutes, what one improvement would you make first?”

These questions reinforce process, not just output.

### Reflection Sentence Stems for Students

You can also offer reflection stems such as:

- “The most useful test I ran was …”
- “The hardest part of the project was …”
- “I fixed one bug by …”
- “If I rebuild this program later, I will start by …”

These are especially helpful for quieter learners who need structure to express their thinking.

---

## Appendix K: Fast-Finisher Variations That Stay in Scope

If several students complete the required version early, offer extensions that reinforce the same concepts instead of changing the lesson topic.

### Extension 1: Update Phone Number

Add a menu option that asks for a contact name and a new phone number, then updates the first matching contact.

### Extension 2: Normalize Names

Store names using `.title()` when adding them so that `ava stone` becomes `Ava Stone`.

### Extension 3: Duplicate Warning

Before adding a new contact, check whether a contact with the same lowercase name already exists. If so, print a warning message.

### Extension 4: Export Preview Text

Still without saving to a file, build a formatted text block such as:

```text
Contacts:
- Ava: 555-1234
- Leo: 555-8888
```

This practices string construction while staying in-memory.

---

**End of Day 4, Hour 3 Script / Course Hour 31**
