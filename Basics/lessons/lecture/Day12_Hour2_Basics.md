# Session 12, Hour 2: Capstone Build Sprint

## 🎯 Outcomes
- Implement full CRUD feature set.
- Improve UX and robustness.

## 🗣️ Instructor Speaking Script

### Introduction (10-15 min)
"Welcome back. In our last hour, we set up our project skeleton and got one basic feature working. In this hour, we focus on a 'build sprint' to implement the rest of our CRUD features: Create, Read, Update, and Delete."

"I strongly recommend taking an iterative approach. Build your 'add' functionality, then test it. Next, build your 'list' functionality and test that. Once listing works, tackle 'search', and finally move on to 'update' and 'delete'."

"Remember, you must test your code at each step. Don't write 50 lines of code without running your program—that is a recipe for a debugging nightmare."

### Live Demo (5-10 min)
*Action: Open the project from Hour 1.*

"Let me demonstrate how to iteratively add another feature, like listing our data."

*Action: Add a listing feature to the scaffolding.*
```python
def list_items(data):
    if not data:
        print("No items found.")
        return
    print("\n--- Current Items ---")
    for i, item in enumerate(data, 1):
        print(f"{i}. {item}")

# In main():
# elif choice == '3':
#     list_items(data)
```

"See how simple that is? I just built the list feature, and now I'll run the program to ensure it works. Always test as you go."

## 💻 Hands-On Lab: Capstone Build (25-35 min)

**Prompt for Students:**
Continue building your Capstone MVP.

**Required:**
- Complete the remaining CRUD features based on the theme you chose.
- Add at least one 'quality' improvement to your application:
  - Sorted output
  - Confirmation prompts before deleting data
  - Input validation (e.g., ensuring a name isn't blank)

**Deliverable this hour:** All required features implemented, and data continuing to persist correctly across runs.

### ✅ Completion Criteria
- All required features (CRUD) are implemented.
- Data successfully persists across runs.

### 🛑 Common Pitfalls (Instructor Eyes Only)
- **Saving not called after updates:** Students might update the list in memory but forget to call `save_data()`.
- **Data structure mismatches:** Saving a list of dictionaries but trying to load it as a list of strings.

### 🚀 Optional Extensions
- Add a simple report export feature that writes a summary to a standard text file (`.txt`).

## 📝 Quick Check / Exit Ticket
**Ask the class:** "What is one bug you fixed during this sprint, and how did you figure it out?"
