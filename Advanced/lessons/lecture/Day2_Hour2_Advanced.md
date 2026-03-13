# Day 2, Hour 2: Pattern: Strategy (swap behaviors cleanly)

## Instructor Notes
- **Course**: Python Programming (Advanced)
- **Session**: 2 (Hour 6 of 48)
- **Focus**: The Strategy Pattern to dynamically change behavior at runtime.
- **Prerequisites**: Comfort with passing functions as arguments (callables) and/or inheritance.
- **Goal**: Teach students how to replace long `if/elif` chains with selectable "strategies" to reduce duplication and improve maintainability.

---

## 1. Instructor Talk Points (10–20 minutes)

**Instructor Talk Points:**

- **The Problem with Branching**: "Imagine your application needs to sort records in three different ways: by date, by priority, or alphabetically. Or maybe it checks a discount based on a membership tier. Usually, we start with a massive `if/elif` chain. As we add more sorting rules or discounts, this chain grows out of control."
- **The Strategy Pattern**: "The Strategy pattern offers a better design. We define a family of algorithms, put each one in its own function or class, and allow the application to select 'which strategy' to use at runtime. It separates *what* we want to do (filter/sort/calculate) from *how* it's done."
- **Strategies in Python**: "Many languages require heavy interfaces and abstract base classes for Strategy. Python is leaner. A strategy is just a **callable**—a regular function—that takes standard inputs and returns standard outputs. We can simply pass functions into other functions or look them up in a dictionary!"

## 2. Live Demo: Strategy Selection (5–10 minutes)

**Live Demo Steps:**

1. **Setup the Problem (`if/elif` smell)**:
   *(Action: Show a sorting function that uses hard-coded branches.)*
   "Let's say we have a function to format our data output based on a selection sort key. We want to sort a list of records."
   ```python
   # The bad way
   records = [
       {"id": 1, "name": "Charlie", "created": "2023-11-01"},
       {"id": 2, "name": "Alice", "created": "2023-10-15"},
       {"id": 3, "name": "Bob", "created": "2023-12-05"}
   ]

   def display_records(records, sort_by):
       if sort_by == 'name':
           sorted_records = sorted(records, key=lambda x: x['name'])
       elif sort_by == 'created':
           sorted_records = sorted(records, key=lambda x: x['created'])
       else:
           sorted_records = sorted(records, key=lambda x: x['id'])
       
       for r in sorted_records:
           print(r)
   ```

2. **Refactor to Strategy Plan**:
   *(Action: Define strategy functions.)*
   "Let's break the `if/elif` logic into independent, modular functions (our strategies)."
   ```python
   # Refactoring to Strategies
   def sort_by_name(record):
       return record["name"]

   def sort_by_date(record):
       return record["created"]

   def sort_by_id(record):
       return record["id"]

   # Use a dictionary to map the user selection to the strategy function
   sorting_strategies = {
       "name": sort_by_name,
       "created": sort_by_date,
       "id": sort_by_id
   }
   ```

3. **Demonstrate the Dynamic Approach**:
   *(Action: Re-write the display function to use a strategy.)*
   "Now the core logic doesn't care *how* we sort, it just executes the selected strategy."
   ```python
   def display_records_strategy(records, strategy_key):
       # Grab the correct strategy function, default to sort_by_id
       strategy_func = sorting_strategies.get(strategy_key, sort_by_id)
       # Resolve the actual key used so the header matches the behavior
       resolved_key = strategy_key if strategy_key in sorting_strategies else "id"
       
       sorted_records = sorted(records, key=strategy_func)
       
       print(f"--- Sorted by {resolved_key} ---")
       for r in sorted_records:
           print(r)

   # Dynamic usage:
   display_records_strategy(records, 'name')
   display_records_strategy(records, 'created')
   ```

## 3. Hands-on Lab: Strategy Selection (25–35 minutes)

**Lab Prompt for Students:**
"Let's apply the Strategy pattern to your capstone application to give the user flexible control."

1. **Identify a Need**: Think of something your app does that could happen in multiple ways:
   - Sorting by different fields (e.g., date vs. priority vs. name).
   - Filtering display results (e.g., active tasks, all tasks, overdue tasks).
   - Export formats (e.g., to terminal, to file).
2. **Implement Strategies**: Create two or more simple functions that implement these variations. Let's start with a 'filtering' strategy.
   - Example function 1: Returns only active records.
   - Example function 2: Returns all records.
3. **Wire it to a Menu**: In a small interactive loop, ask the user to choose an option (like '1' for Active, '2' for All). 
4. **Use a Dictionary Dispatcher**: Map the user's input to the chosen strategy function in a dictionary. Pass the selected function to the main processing routine.

*Optional Extensions for fast finishers:*
- Implement a *third* strategy.
- Can you apply the pattern to something else, like a validation strategy?

**Instructor: Circulate and check:**
- **Common Pitfall**: Students might still put `if/elif` chains inside their main function, completely missing the point. Remind them to use a dictionary or directly pass a function pointer.
- **Common Pitfall**: Are they accidentally *calling* the function in the dictionary definition? (e.g., `{"name": sort_by_name()}` instead of `{"name": sort_by_name}`). Emphasize they are passing the function object, not the result.

## 4. Quick Check / Exit Ticket (5 minutes)

- **Quick Check Question:** "How is a strategy pattern different from a giant `if/elif` chain?"
  - *Answer:* The Strategy pattern extracts the varied logic into separate, distinct callables (functions or classes) allowing behavior to be selected dynamically at runtime without modifying the core orchestrating code. It is more open to extension.
- **Wrap-up:** "You've just removed a major source of spaghetti code from your apps. Let's take a break. Up next, we'll make our own custom objects behave nicely when printed and inspected using Pythonic text representation."
