# Day 8, Hour 3: CLI Contact Manager Mini-Project (Course Hour 31)
**Python Programming Basics – Session 8**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 8, Course Hour 31 – Mini-project: CLI Contact Manager (in-memory)  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is written as a read-aloud teaching guide. This hour combines `while` loops, dictionaries (or lists), and the menu and validation patterns just learned into a single, cohesive application. Emphasize incrementally building the application (menu first, then adding features one by one) and maintaining a clean user experience (UX). All data remains in memory (no File I/O yet).

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Combine a `while` loop, input validation, and a dictionary to build a fully functional Contact Manager.
2. Develop a program incrementally (step-by-step), rather than trying to write it all at once.
3. Handle missing data gracefully by checking for keys before attempting to delete them.
4. Provide clear user experience (UX) messages so the user always knows what is happening."

---

## 1) Agenda + Timing

- **0:00–0:05** Introduction: Bringing it all together
- **0:05–0:15** Concept: The Incremental Build Strategy
- **0:15–0:25** Live demo: Building the Add and List features
- **0:25–0:55** Guided lab: Complete the Contact Manager
- **0:55–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist

- Ensure students have successfully completed the previous hour on input validation and menus.
- Open an empty file named `hour31_contacts_demo.py` ready for live coding.
- Open another empty file named `hour31_contacts_lab.py` to serve as a starter for the lab portion.

**Say:** "Please have your editor open and an empty file ready. We are transitioning from learning isolated building blocks to assembling an entire application."

---

## 3) Opening Script: Bringing It All Together (~5 minutes)

### 3.1 The Mini-Project

**Say:**
"We have spent the last two hours learning how to build infinite loops that hold a program open, how to route choices with `if/elif`, and how to build safe inputs using `.isdigit()`.

Now, we are going to combine those tools with the collections we learned previously—specifically dictionaries—to build a Contact Manager. 

A Contact Manager needs to hold a name and a phone number. A dictionary is perfect for this, where the Name is the key, and the Phone Number is the value. Our program will allow a user to Add a contact, List all contacts, Search for a specific contact by name, and Delete a contact."

---

## 4) Concept: The Incremental Build Strategy

### 4.1 Don't write it all at once

**Say:**
"When you are asked to build an application with five features, the worst thing you can do is try to code all 150 lines from top to bottom before running it. If you do that, and hit 'Run', you will have 30 errors overlapping each other, and you won't know where to start fixing them.

Professional developers use the **Incremental Build Strategy**.
1. We build the scaffold (the empty menu loop) and make sure it loops and quits. We test it.
2. We add Feature 1 (Add Contact). We test it.
3. We add Feature 2 (List Contacts). We test it.
4. We add Feature 3 (Search). We test it.

By testing after every single feature, if something breaks, we know exactly which 5 lines of code caused the error because they are the only lines we just changed."

---

## 5) Live Demo: Building the Add and List features

### 5.1 Setting up the scaffolding and Add

**Say:**
"Let's practice this strategy together. Open `hour31_contacts_demo.py`. We will build the skeleton, and implement adding and listing. Then I will hand it over to you to finish."

**Type and narrate:**

```python
# hour31_contacts_demo.py

# 1. State Outside the Loop
contacts = {}

print("Welcome to the Contact Manager")

while True:
    print("\n=== Main Menu ===")
    print("1. Add Contact")
    print("2. List Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Quit")
    
    choice = input("Enter choice (1-5): ").strip()
    
    if choice == '1':
        print("\n-- Add Contact --")
        name = input("Name: ").strip().title() # Normalize the name
        
        # We can implement a quick loop for a valid phone number length
        while True:
            phone = input("Phone Number (digits only): ").strip()
            if phone.isdigit() and len(phone) >= 7:
                break
            print("Invalid phone format. Please use numbers only, min 7 digits.")
            
        contacts[name] = phone
        print(f"Success! {name} added.")

    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Feature not yet implemented or invalid choice.")
```

**Run it.** Test adding two names. Test entering text for the phone number to show the nested validation loop catches it. Test quitting.

**Say:**
"Step 1 is complete. Our loop works, our state persists outside the loop, we normalized the name using `.title()` so 'alice' and 'ALICE' become 'Alice', and we safely added our first nested `while` loop to guarantee the phone number is good."

### 5.2 Building the List feature

**Say:**
"Now let's build choice 2, Listing."

**Type and insert at the appropriate place:**

```python
    elif choice == '2':
        print("\n-- Contact List --")
        if not contacts:
            print("Your contact list is empty.")
        else:
            for name, phone in contacts.items():
                print(f"  {name}: {phone}")
```

**Run it.** Test listing an empty dictionary. Test adding a name. Test listing again.

**Say:**
"Step 2 is complete. Notice how important it is to provide clear UX (User Experience). When the dictionary is empty, we don't just print empty brackets `{}`; we print 'Your contact list is empty'. We iterate cleanly over the dictionary items using `.items()`."

---

## 6) Hands-on Lab: Complete the Contact Manager

### 6.1 Lab overview

**Say:**
"I have built the scaffolding, the Add feature, and the List feature. Your job for the next 30 minutes is to implement the Search and Delete features, managing the dictionary safely. You will also add one optional extension if you finish early."

### 6.2 Lab specification

**Display or read aloud:**

---

**Lab: Contact Manager (in-memory)**

**Task:**
1. Start with the scaffold we just built (or write your own from scratch).
2. Implement **Choice 3: Search Contact**. Ask the user for a name. If the name is in the dictionary, print their phone number. If they are not, print a friendly 'Not found' message.
3. Implement **Choice 4: Delete Contact**. Ask the user for a name. If the name exists, remove them from the dictionary using `del` or `.pop()`. Crucially, if they **do not exist**, catch this gracefully so the program does not crash with a `KeyError`.
4. Ensure all user names asked in Search/Delete are normalized with `.title()` so they match the keys in your dictionary.

**Expected Delete Interaction Example:**
```
-- Delete Contact --
Name to delete: Bob
Success! Bob has been removed.

Name to delete: Charlie
Error: Charlie is not in your contacts.
```

**Extra Challenge (Optional):** Add an 'Update' choice. If the name exists, prompt for a new phone number using the safe phone loop, and overwrite the old number.

---

Circulate the room for 25–30 minutes. Look specifically for:
- Not normalizing the search/delete keys with `.title()`. If you added 'Dave', searching for 'dave' will fail unless `dave` is converted to `Dave`.
- Trying to iterate over a dictionary while modifying it (they should just `del contacts[name]` directly).
- Crashing on deletion using `del` without checking `if name in contacts:` first.

### 6.3 Walkthrough solution for Choice 3 and 4

After working time, write out the brief solution additions:

```python
# hour31_contacts_lab.py (Additions)

    # ... inside the main loop
    elif choice == '3':
        print("\n-- Search Contact --")
        search_name = input("Name to find: ").strip().title()
        
        # Use python's safe .get() method, or `if in`
        if search_name in contacts:
            print(f"Found: {search_name} - {contacts[search_name]}")
        else:
            print(f"Sorry, {search_name} is not in your contacts.")
            
    elif choice == '4':
        print("\n-- Delete Contact --")
        del_name = input("Name to delete: ").strip().title()
        
        if del_name in contacts:
            del contacts[del_name]
            print(f"Success! {del_name} has been removed.")
        else:
            print(f"Error: {del_name} is not in your contacts.")
            
    # Optional Update Feature
    elif choice == '6': # Or a different assigned number
        print("\n-- Update Contact --")
        upd_name = input("Name to update: ").strip().title()
        
        if upd_name in contacts:
            while True:
                new_phone = input("New Phone Number: ").strip()
                if new_phone.isdigit() and len(new_phone) >= 7:
                    break
                print("Invalid format.")
            contacts[upd_name] = new_phone
            print(f"Updated {upd_name}.")
        else:
            print(f"Error: {upd_name} not found.")
```

**Say:**
"The critical part of deletion is this line: `if del_name in contacts:`. By checking membership first, we completely avoid the deadly `KeyError` that crashes the program. The combination of normalizing input with `.title()` and safe key checking makes this mini-app astonishingly robust for how few lines of code it actually takes."

---

## 7) Recap and Exit Ticket

### 7.1 Summary
**Say:**
"Today we built a real, functional command-line utility. You used a dictionary for state, loops for persistence, conditional logic for routing, string methods for normalization, and membership testing to prevent crashes."

### 7.2 Quick Check / Exit Ticket
**Ask:**
"Quick check: What was the hardest bug you hit or concept to grasp while building the menu loop today?"

**Expected answer:** Elicit discussion. Common answers include variable scope (initializing dict inside loop), endless loops due to missing `break`, or case sensitivity (falling prey to 'alice' vs 'Alice').

**Say:**
"Those are incredibly normal hurdles when first assembling larger applications. In our final hour today, we will assess everything we've covered in Session 7 and 8 with Checkpoint 4."
