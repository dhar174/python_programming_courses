# Day 10, Hour 2: Collections of objects + searching (Course Hour 38)
**Python Programming Basics – Session 10**

**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 10, Course Hour 38 – Collections of objects + searching  
**Duration:** 60 minutes  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Instructor Deliverable Script (Use Largely Verbatim)

> **Instructor note:** This document is written as a read-aloud teaching guide. Emphasize how iterating through a list of objects works just like any other list, but now we access specific attributes (like `.name`) to compare against search terms. 

---

## 0) Learning Outcomes (read aloud, ~2 minutes)

"By the end of this hour, you will be able to:

1. Search through lists of custom objects by comparing their attributes.
2. Update specific object fields (attributes) safely.
3. Replace dictionary-based record keeping with object-based record keeping."

---

## 1) Agenda + Timing

- **0:00–0:05** Introduction: Dealing with many objects at once
- **0:05–0:15** Core concept: Looping and searching by attribute
- **0:15–0:25** Core concept: Updating returned objects safely
- **0:25–0:35** Live demo: `search_contact` function
- **0:35–0:55** Guided lab: Refactoring Contact Manager to objects
- **0:55–1:00** Debrief, recap, and exit ticket

---

## 2) Instructor Setup Checklist

- Open an empty file named `hour38_search_demo.py` ready for live coding.
- Keep the `Contact` class from the previous hour available for reuse.
- **Say:** "Please open your editors and create a new file called `object_search.py`. Copy over your `Contact` class from our last hour; we are going to build on it today."

---

## 3) Opening Script: Dealing with many objects (~5 minutes)

**Say:**
"In the last hour, we created a single `Contact` blueprint and made a few contact objects. We even put them into a list and printed them out using our own `display()` method.

But in a real application, you don't just print every record. You usually want to find one specific record—for example, searching for a contact by their name so you can see their phone number or update it. 

When dealing with a list of dictionaries, we had to check keys, like `if contact['name'] == search_term`. Let's see how much cleaner this process is when we combine loops with object attributes."

---

## 4) Concept: Looping and searching by attribute

### 4.1 Seeking a needle in the haystack

**Say:**
"When we loop through a list of objects, the loop variable represents the *entire object*. If we want to check if it's the right object, we just look at its attributes using dot notation."

**Type and narrate:**

```python
# hour38_search_demo.py

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

# Let's populate a directory
directory = [
    Contact("Alice", "555-0101"),
    Contact("Bob", "555-0202"),
    Contact("Charlie", "555-0303")
]

# Searching for Bob
query = "bob"
found_contact = None

for person in directory:
    # Remember to normalize strings when comparing!
    if person.name.lower() == query.lower():
        found_contact = person
        break

if found_contact:
    print(f"Found them! Their phone is {found_contact.phone}")
else:
    print("Contact not found in directory.")
```

**Say:**
"Look at the condition: `if person.name.lower() == query.lower():`. We are asking the `person` object to give us its `name` attribute, which is just a string. Then we lower-case it and compare it to our query. When we find a match, we save the *whole object* into a new variable called `found_contact` and `break` the loop."

---

## 5) Concept: Updating returned objects safely

**Say:**
"Now that we've found our object and stored it in `found_contact`, what if we want to change their phone number? Because `found_contact` points to the *exact same object* that sits inside our list, any updates we make to `found_contact` will be permanent."

**Type and narrate:**

```python
# Assuming found_contact is Bob's object from the previous step
if found_contact:
    print(f"Old phone: {found_contact.phone}")
    
    # Updating the attribute directly
    found_contact.phone = "555-9999"
    
    print(f"New phone: {found_contact.phone}")

# To prove it changed in the main list:
print("\nVerifying the main list was updated:")
for p in directory:
    print(f"{p.name}: {p.phone}")
```

**Say:**
"We updated the attribute, and when we printed the whole directory again, Bob's number was updated! We didn't have to 'save' it back into the list. The object itself was modified in memory."

---

## 6) Live Demo: A `search_contact` function

**Say:**
"Instead of writing that loop out in our main code every time, let's wrap it in a function that returns the object if found, or `None` if not."

**Type and narrate:**

```python
def search_contact(contact_list, target_name):
    # Loop through the list of objects
    for c in contact_list:
        if c.name.lower() == target_name.lower():
            return c  # Returns the actual object immediately
            
    return None # Return None if the loop finishes without finding a match

# Testing the function
search_result = search_contact(directory, "Alice")

if search_result:
    print(f"Found {search_result.name}. Updating phone...")
    search_result.phone = "555-8888"
else:
    print("Not found.")
```

**Run it and demonstrate.**

**Say:**
"Notice how clean our main logic becomes. We say 'search for Alice'. If the function gives us an object back, we update it. If it gives us `None`, we gracefully handle it."

---

## 7) Hands-on Lab: Refactor Contact Manager to objects

### 7.1 Lab overview

**Say:**
"It's time to bring it all together. You are going to take the menu-driven contact manager we practiced previously and upgrade its core engine from dictionaries to objects."

### 7.2 Lab specification

**Display or read aloud:**

---

**Lab: Refactor Contact Manager to objects**

**Task:**
1. Start a new script. Define your `Contact` class at the top. It needs `name` and `phone` attributes, and a `display()` method.
2. Initialize an empty list called `my_directory = []`.
3. Build a standard `while True:` loop containing a menu: `[1] Add  [2] List  [3] Search/Update  [4] Quit`.
4. **Add**: Ask for name and phone, create a new `Contact` object, and append it to the list.
5. **List**: Loop through the list and call `.display()` on every object.
6. **Search**: Implement the name-matching logic (either inline in the menu loop, or using a separate function).
   - If found, ask the user if they want to enter a new phone number, then update the object's `phone` attribute.
   - If not found, print a 'not found' message.

---

**Instructor Note for Circulation:**
Watch out for learners comparing the search string to the whole object (e.g., `if query == contact:`) instead of the attribute (`if query == contact.name:`). Remind them that if two contacts share the same name (like "John"), a simple `break` or `return` will only ever find the first one. This is expected behavior for the Basics level, but a good talking point if they notice it.

### 7.3 Walkthrough solution

**After 20 minutes, show a brief solution:**

```python
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display(self):
        return f"{self.name} -- {self.phone}"

my_directory = []

while True:
    print("\n[1] Add  [2] List  [3] Search/Update  [4] Quit")
    choice = input("> ")

    if choice == '1':
        n = input("Name: ")
        p = input("Phone: ")
        new_obj = Contact(n, p)
        my_directory.append(new_obj)
        print("Added successfully.")

    elif choice == '2':
        print("\n--- Directory ---")
        for c in my_directory:
            print(c.display())

    elif choice == '3':
        target = input("Enter name to search: ")
        found_obj = None
        
        for c in my_directory:
            if c.name.lower() == target.lower():
                found_obj = c
                break
                
        if found_obj:
            print(f"Found! Current phone: {found_obj.phone}")
            new_p = input("New phone (or press enter to skip): ")
            if new_p.strip(): # If they typed something
                found_obj.phone = new_p
                print("Updated!")
        else:
            print("Contact not found.")

    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
```

**Say:**
"By swapping dictionaries for objects, we established a clear, rigid structure for what a 'Contact' looks like. We don't have to worry about accidentally misspelling a dictionary key like `'Name'` vs `'name'` throughout our code, because the attributes belong to the class definition."

---

## 8) Recap and Exit Ticket

### 8.1 Summary
**Say:**
"We explored how working with lists of objects is incredibly powerful. We iterated through the list, accessed specific attributes to perform searches using string normalization, and then modified those attributes in place without needing to save them back over the list."

### 8.2 Quick Check / Exit Ticket
**Ask:**
"Quick check: Why might using objects make code easier to maintain than using deeply nested dictionaries?"

**Expected answer:** Let them answer. "Objects provide a guaranteed structure (you define the blueprint once), you can bundle helper behaviors (like `display()`) right alongside the data, and using dot notation (`obj.name`) is cleaner and less error-prone than bracket notation (`dict['name']`)."
