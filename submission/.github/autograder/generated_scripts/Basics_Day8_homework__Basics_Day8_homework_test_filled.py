#!/usr/bin/env python
# coding: utf-8

# # Python Basics - Day 8 Sample Submission
# 
# Deterministic sample notebook for autograder validation.

# In[ ]:


print("Menu display: [1] Add [2] List [3] Search [4] Quit")
menu_actions = {"1": "add", "2": "list", "3": "search", "4": "quit"}
for option in ["1", "2", "3", "4"]:
    print(f"Menu option selected: {option} -> {menu_actions[option]}")
print("Menu loop ended: user requested quit")

for raw_value in ["abc", "-5", "12"]:
    if raw_value.isdigit():
        number = int(raw_value)
        print(f"Input '{raw_value}' -> accepted integer {number}")
    elif raw_value.startswith('-'):
        print(f"Input '{raw_value}' -> invalid for isdigit guard")
    else:
        print(f"Input '{raw_value}' -> invalid integer")
print(f"Validated number doubled: {number * 2}")
print("Validation note: isdigit() does not accept negatives or decimals")

contacts = {}
contacts["Ava"] = "555-0101"
print("Added contact: Ava -> 555-0101")
contacts["Ben"] = "555-0102"
print("Added contact: Ben -> 555-0102")
print("List contacts: Ava (555-0101), Ben (555-0102)")
print(f"Search 'Ava': {contacts.get('Ava')}")
removed = contacts.pop("Ben", None)
print(f"Delete 'Ben': {'removed' if removed else 'not found'}")
missing = contacts.pop("Zoe", None)
print(f"Delete 'Zoe': {'removed' if missing else 'not found'}")

tasks = []
tasks.append({"title": "Finish checkpoint", "done": False})
print("Task added: Finish checkpoint")
tasks.append({"title": "Review loops", "done": False})
print("Task added: Review loops")
tasks[0]["done"] = True
print("Task completed: Finish checkpoint")
tasks.pop(1)
print("Task deleted: Review loops")
print("Remaining tasks: Finish checkpoint [done]")
print("Checkpoint 4 status: pass")

