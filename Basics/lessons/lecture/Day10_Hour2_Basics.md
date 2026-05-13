# Day 10, Hour 2: Collections of objects + searching (Course Hour 38)

**Python Programming Basics – Session 10**  
**Course:** Python Programming (Basics)  
**Runbook alignment:** Session 10, Course Hour 38 – Collections of objects + searching  
**Duration:** 60 minutes (including 30-minute guided lab with checkpoints)  
**Mode:** Instructor-led + live coding + guided lab  
**Audience:** Beginners in Python (Basics scope only)

---

## Learning Outcomes

**Read aloud at the start of the hour (approximately 2–3 minutes):**

"By the end of this hour, you will be able to:

1. **Search through collections of custom objects** by looping through a list and comparing object attributes.
2. **Update object fields (attributes) safely** by modifying objects found within a list, without needing to 're-save' them.
3. **Replace dictionary-based record keeping with object-based record keeping**, writing cleaner, more maintainable code.
4. **Combine loops, conditionals, and methods** to build practical, menu-driven applications using object collections.

These outcomes directly support your move from simple data structures to real-world object-oriented programming patterns. By the end of this hour, you'll understand that once you find an object in a list, you can modify it in place—the list sees the changes automatically."

---

## Instructor Prep Notes

### Setup Checklist (Complete before class)

- **Verify the `Contact` class is available** from Day 10, Hour 1. Have it copied into a fresh editor window.
- **Open a blank file** named `hour38_search_demo.py` in your editor, ready for live coding.
- **Test your code examples** locally. Run through both the search demo and the full contact manager walkthrough solution to confirm they execute without errors.
- **Prepare 4–5 sample contacts** (e.g., Alice, Bob, Charlie, Dana) mentally, so when you do live coding, you can populate the list quickly without typos.
- **Disable notifications** on your workstation to avoid interruptions during live demo.
- **Arrange the lab instructions** (section 7.2) in a visible location—either printed, in a second monitor window, or a tablet you can glance at.
- **Check the network/wifi** if you plan to share your screen. Latency can make live coding appear choppy.

### Opening Commentary

"In the last hour, we created the `Contact` class—a blueprint for representing a single contact record with a name, phone number, and a `display()` method. We made a few objects and put them in a list. But today, we're asking the real question: how do we **find** a contact by name, and how do we **update** their phone number without manually digging through the entire list?

This is exactly what real applications do. When you search your phone for 'Mom', it's looping through a list of contact objects and comparing the `name` attribute. Then it displays the match. If you edit the phone number, it updates the object in place. Today, we build that engine."

---

## Opening Script: Dealing with many objects (~5 minutes)

**Say (read aloud, roughly 5 minutes):**

"In the last hour, we created a single `Contact` blueprint and made a few contact objects. We even put them into a list and printed them out using our own `display()` method.

But in a real application, you don't just print every record. You usually want to find *one specific record*—for example, searching for a contact by their name so you can see their phone number or update it.

When dealing with a list of dictionaries, we had to check keys, like `if contact['name'] == search_term`. It worked, but it was error-prone: if you mistyped `'Name'` instead of `'name'`, your code would crash or silently fail.

With objects, we use the exact same attribute name every time, because it's defined once in the class. When we combine loops with object attributes, the code becomes cleaner, more predictable, and easier to maintain.

Here's what we're going to do today:
1. First, we'll learn how to loop through a list of objects and compare their attributes to find a specific one.
2. Then, we'll learn that once we've found an object, we can update its attributes *in place*—the list sees the change automatically.
3. We'll wrap that logic into a reusable function.
4. Finally, you'll rebuild your contact manager app using objects instead of dictionaries.

Let's get started."

---

## Concept Briefing: Looping and Searching by Attribute

### Why Searching Matters

**Instructional point (1–2 minutes):** 
"Searching is one of the most common operations in programming. A contact app searches for a person. A todo list searches for a task. A store searches for a product by ID. The pattern is always the same: loop through a collection, check each item against your search criteria, and return the one that matches—or return `None` if nothing matches."

### The Core Pattern

**Say (2–3 minutes):**

"When we loop through a list of objects, the loop variable represents the *entire object*. If we want to check if it's the right object, we just look at its attributes using dot notation. Let me show you."

**Type and narrate the first code block:**

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
"Look at line 18: `if person.name.lower() == query.lower():`. Here's what's happening step by step:

1. `person` is a `Contact` object—the current item in the loop.
2. `person.name` accesses the `name` attribute of that object. It's just a string.
3. `.lower()` converts it to lowercase so we can compare case-insensitively. 'Bob' and 'bob' will match.
4. We compare it to our query (also lowercased).
5. If there's a match, we save the *entire object* into `found_contact` and `break` the loop.

After the loop, we check if `found_contact` is still `None`. If it isn't, we found a match and can access its attributes. If it is, no match was found."

### Why Normalize Strings?

**Important teaching point (1 minute):**

"Why `.lower()`? Because users type 'alice', 'Alice', 'ALICE'—all different strings to Python unless we normalize them first. By converting both sides to lowercase before comparing, we catch all variations. This is a best practice you'll use everywhere in real applications."

---

## Concept: Updating Returned Objects Safely

**Say (3–4 minutes):**

"Now that we've found our object and stored it in `found_contact`, what if we want to change their phone number? Here's the magical part: because `found_contact` points to the *exact same object* that sits inside our list, any updates we make to `found_contact` will be permanent in the list too. We don't have to 'save' it back. The object itself is modified in memory."

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
"Run this code. You'll see Bob's phone updated in the printout. We didn't have to do anything special—we just assigned a new value to the attribute. Python handles the memory management for us. This is called 'passing by reference': the variable `found_contact` and the object inside the list both point to the same data."

---

## Live Demo: A `search_contact` Function (~10 minutes)

**Say:**
"Instead of writing that loop out in our main code every time we need to search, let's wrap it in a reusable function that returns the object if found, or `None` if not. This is the foundation of real applications."

**Type and narrate (with comments explaining each step):**

```python
def search_contact(contact_list, target_name):
    """
    Search for a contact by name (case-insensitive).
    Returns the Contact object if found, or None if not found.
    """
    # Loop through the list of objects
    for c in contact_list:
        if c.name.lower() == target_name.lower():
            return c  # Returns the actual object immediately
            
    return None  # Return None if the loop finishes without finding a match

# Testing the function
search_result = search_contact(directory, "Alice")

if search_result:
    print(f"Found {search_result.name}. Updating phone...")
    search_result.phone = "555-8888"
else:
    print("Not found.")

# Test again with a contact that doesn't exist
search_result2 = search_contact(directory, "Eve")
if search_result2:
    print(f"Found {search_result2.name}.")
else:
    print("Eve not found in directory.")
```

**Narrate as you run it:**
"Notice how clean our main logic becomes. We say 'search for Alice'. If the function gives us an object back, we update it. If it gives us `None`, we handle it gracefully. This pattern—search first, then operate—is used constantly in real software. And because the function encapsulates the loop, we don't have to repeat it everywhere."

**Ask learners to predict output** before you run it. This builds engagement and tests comprehension.

---

## Practice Exercise: Searching Multiple Contacts (~8 minutes)

**Guided activity (have learners code along with you on their own machines):**

"Let's practice one more time. I'm going to search for a few different contacts. You code along with me:

```python
# Let's try searching for different names
names_to_find = ["bob", "Charlie", "Nobody", "alice"]

for search_name in names_to_find:
    result = search_contact(directory, search_name)
    if result:
        print(f"✓ Found: {result.name} -- {result.phone}")
    else:
        print(f"✗ Not found: {search_name}")
```

**Ask:**
- What happens if we search for 'Nobody'?
- Why does 'bob' (lowercase) match 'Bob' (capitalized)?
- Where could we optimize this if we had 1 million contacts?

This engages higher-order thinking without overwhelming Basics learners."

---

## Hands-on Lab: Refactor Contact Manager to Objects (30 minutes)

### Lab Overview

**Say:**
"It's time to bring it all together. You are going to take the menu-driven contact manager we practiced previously and upgrade its core engine from dictionaries to objects. This is the most important activity of the hour. You'll have approximately 30 minutes, and I'll circulate to help if you get stuck."

### Lab Specification

**Display or share the following on screen and read aloud:**

---

**Lab: Refactor Contact Manager to Objects**

**Objective:** Build a menu-driven contact manager where contacts are stored as objects (not dictionaries) and implement search and update functionality.

**Requirements:**

1. **Class definition** — At the top of your script, define a `Contact` class:
   - `__init__` method accepting `name` and `phone`
   - `display()` method returning a formatted string like `"Alice -- 555-0101"`

2. **Initialize storage** — Create an empty list called `my_directory = []`.

3. **Menu loop** — Build a `while True:` loop that displays a menu:
   ```
   [1] Add
   [2] List
   [3] Search/Update
   [4] Quit
   ```

4. **Add feature** — When user chooses [1]:
   - Prompt for a name and phone number
   - Create a new `Contact` object
   - Append it to the list
   - Print "Added successfully."

5. **List feature** — When user chooses [2]:
   - Print a header like "--- Directory ---"
   - Loop through the list and call `.display()` on each object
   - Print each result

6. **Search/Update feature** — When user chooses [3]:
   - Prompt for the name to search for
   - Use a loop (or a separate `search_contact` function) to find the contact
   - If found:
     - Print the current phone number
     - Ask if they want to update it: "New phone (or press enter to skip):"
     - If they enter a phone number, update the object's `phone` attribute
     - Print "Updated!"
   - If not found:
     - Print "Contact not found."

7. **Quit feature** — When user chooses [4]:
   - Print a goodbye message and `break` from the loop

8. **Invalid choice handling** — For any other input, print "Invalid choice."

**Completion Checkpoints (verify these as you work):**
- [ ] The program starts and displays the menu
- [ ] You can add a contact and it appears in the list
- [ ] You can search for a contact by name (case-insensitive)
- [ ] You can update a contact's phone number
- [ ] The updated phone appears in the list
- [ ] You can quit cleanly

**Extension (if you finish early):**
- Allow duplicate names by adding an ID field (simple counter: contact 1, contact 2, etc.)
- Implement a delete feature
- Add a search that finds all contacts whose names *contain* a search term (use the `in` operator)

---

### Instructor Facilitation During Lab

**What to watch for (circulate and spot-check):**

- **Error 1:** Learners comparing search string to the whole object (`if query == contact:`) instead of the attribute (`if query == contact.name:`). Remind them: "You're searching for a *name*, not a person."

- **Error 2:** Learners forgetting to use `.lower()` when comparing. If 'Bob' doesn't match 'bob', ask: "What if I type 'bob' in all lowercase?"

- **Error 3:** Learners not using the object reference correctly after finding it. Remind: "Once you have the object, you can change its attributes directly. You don't need to save it back to the list."

- **Error 4:** Typos in the class definition. If they write `def display()` but call `.display` without parentheses, clarify that `display` is a method and needs `()`.

**Checkpoint discussions (every 10 minutes):**
- Minute 10: "Does your menu loop work? Can you add a contact?"
- Minute 20: "Can you search and find a contact? Can you update their number?"
- Minute 30: "Test one more time: add a new contact, find it by name, update it, list all contacts to verify."

### Walkthrough Solution

**After 20 minutes of lab time, display this solution (do not give it earlier—learners need struggle time):**

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
        if not my_directory:
            print("(No contacts yet)")
        else:
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
            if new_p.strip():  # If they typed something
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

**After showing the solution, say:**

"By swapping dictionaries for objects, we established a clear, rigid structure for what a 'Contact' looks like. We don't have to worry about accidentally misspelling a dictionary key like `'Name'` vs `'name'` throughout our code, because the attributes belong to the class definition. The code is easier to read, maintain, and extend."

---

## Troubleshooting & Common Pitfalls

### Comparing Wrong Attribute

**Symptom:** Learner writes `if query == contact:` instead of `if query == contact.name:`.

**Why it happens:** Confusion between the object and its attributes.

**Fix:** Emphasize: "You're comparing a *string* (the query) to an *attribute* (which is a string). You can't compare a string to an entire object; you need the attribute."

### String Comparison Case Sensitivity

**Symptom:** Search for 'bob' doesn't find 'Bob'.

**Why it happens:** Python treats 'Bob' and 'bob' as different strings.

**Fix:** Always use `.lower()` on both sides when doing name searches. Practice this pattern repeatedly.

### Forgetting the `break` Statement

**Symptom:** Loop continues searching even after finding a match; may return the wrong contact or crash.

**Why it happens:** Learner forgets that without `break`, the loop continues. If there are duplicates, it might overwrite `found_contact`.

**Fix:** Trace through the loop with a debugger or print statements. Show that `break` stops the loop immediately.

### Not Updating the Actual Object

**Symptom:** Learner updates `found_obj.phone`, but the change doesn't persist when they list the directory again.

**Why it happens:** Misunderstanding of reference vs. copy. (This is usually not a Basics-level issue, but can occur.)

**Fix:** Show them that `found_obj` *is* the object in the list. Print the object's memory address to prove it's the same one: `print(id(found_obj))` vs `print(id(my_directory[0]))`.

### Empty List on Search

**Symptom:** Learner searches for a contact in an empty directory and gets an unexpected result.

**Why it happens:** No error-handling for an empty list.

**Fix:** Add a simple check: `if not my_directory: print("Directory is empty."); continue`.

---

## Quick-Check Questions (Exit Ticket, ~5 minutes)

**Pose these questions to the class. Invite 2–3 learners to answer each one:**

### Question 1: Attribute Access
"When we search through a list of `Contact` objects, how do we access the `name` attribute of the current object in the loop?"

**Expected answer:** "Using dot notation: `person.name` or `contact.name`."

### Question 2: String Normalization
"Why do we use `.lower()` when comparing names?"

**Expected answer:** "So that 'Alice', 'alice', and 'ALICE' are all treated the same way. It makes the search case-insensitive."

### Question 3: Object Reference
"If we find a contact in the list and update their phone number, does the change persist in the list?"

**Expected answer:** "Yes, because the object in the list and the variable we're using both point to the same object in memory. We're modifying the actual object, not a copy."

### Question 4: Design Thinking
"Why is it better to wrap the search logic in a function like `search_contact()` instead of writing the loop every time you need to search?"

**Expected answer:** "Because functions let us reuse code. If we discover a bug in the search logic, we fix it in one place, and all code that calls the function benefits."

### Question 5: Architecture
"Why might using objects make code easier to maintain than using deeply nested dictionaries?"

**Expected answer:** "Objects provide a guaranteed structure (you define the blueprint once), you can bundle helper behaviors (like `display()`) right alongside the data, and using dot notation (`obj.name`) is cleaner and less error-prone than bracket notation (`dict['name']`)."

---

## Wrap-Up Notes: Summary & Reflection

**Recap (read aloud, ~2 minutes):**

"Today, we explored one of the most powerful patterns in programming: searching through collections of objects. We learned that:

1. **Looping through objects is intuitive:** We iterate through a list and check each object's attributes.
2. **String normalization matters:** Using `.lower()` makes searches robust and user-friendly.
3. **Objects can be updated in place:** Once we find an object, we can modify its attributes without 'saving' them back.
4. **Functions abstract complexity:** By wrapping our search logic in a function, we write cleaner, more maintainable code.

This hour represents a major milestone. You've moved from working with individual objects to collections of objects, and you've implemented realistic, practical features. The contact manager you built today is a scaled-down version of apps used in real software systems.

**Reflection prompts for learners (pose to the class, allow think-pair-share time):**

- "What was the trickiest part of building the contact manager today, and how did you overcome it?"
- "If you had to add a 'delete contact' feature, where would you add it in your menu?"
- "What would happen if two people in your directory had the same name? How would you handle it?"

---

## Facilitation Notes: Instructor Tips & Timing

### Pacing Tips

- **0:00–0:05:** Opening script + learning outcomes. Don't rush. This sets the motivation.
- **0:05–0:20:** Concept briefing (both looping and updating). This is dense; allow time for questions.
- **0:20–0:30:** Live demo. Do this slowly. Narrate each step. Let learners predict output.
- **0:30–0:05** (into the lab): Hand out lab instructions and circulate immediately.
- **Lab time:** Don't check in too early. Learners need 5–10 minutes to get oriented. Then start circulating every 3–5 minutes.
- **0:55–1:00:** Recap, quick-check questions, and reflection.

### Contingency Plans

**If learners are ahead of pace:**
- Ask them to add a delete feature
- Have them implement a search that finds all contacts whose name *contains* a substring
- Invite them to add a 'sort by name' feature (using `sorted()`)

**If learners are behind pace:**
- Shorten the walkthrough solution demo to focus on the key parts (search and update)
- Provide a partial template for the menu loop and have them fill in the search logic
- Focus on just the search and list features; defer update to a follow-up session if needed

**If there are conceptual blocks:**
- Use a physical analogy: "The list is like a phonebook. When I search, I'm flipping through pages. When I find the page, I can write on it directly."
- Use `print()` statements liberally to show what's happening at each step
- Consider pairing learners who understand with those who don't

### Encouraging Debugging Habits

"If your code doesn't work, don't panic. Add `print()` statements to show what's happening at each step. Print the value of `found_obj` after the loop. Print the contact's name and phone after you update it. These prints are your friends; they let you see inside the computer's memory."

### Extension Ideas (if time permits or for homework)

1. **Multi-field search:** Allow searching by phone number, not just name.
2. **Validation:** Ensure phone numbers are a certain format (e.g., at least 10 digits).
3. **Persistence:** Save the directory to a text file when the program closes, and load it when the program starts.
4. **Sorting:** Display the directory sorted by name.
5. **Duplicate handling:** Add an ID field so multiple contacts can have the same name but be distinguished by ID.
