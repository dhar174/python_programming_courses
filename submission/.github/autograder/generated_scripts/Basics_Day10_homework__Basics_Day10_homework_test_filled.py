#!/usr/bin/env python
# coding: utf-8

# # Python Basics - Day 10 Homework (Filled Test Submission)
# 
# This sample submission is used for local and CI autograder validation.
# 

# In[ ]:


class Contact:
    def __init__(self, name: str, phone: str) -> None:
        self.name = name
        self.phone = phone

    def display(self) -> str:
        return f"{self.name} -> {self.phone}"

    def announce_ready(self) -> str:
        return f"{self.name} is ready to contact."

    def matches_name(self, target_name: str) -> bool:
        return self.name.strip().lower() == target_name.strip().lower()

    def update_phone(self, new_phone: str) -> bool:
        candidate = new_phone.strip()
        if candidate.isdigit() and len(candidate) == 7:
            self.phone = candidate
            return True
        return False

def normalize_name(name: str) -> str:
    return name.strip().lower()

def find_contact_by_name(contacts: list[Contact], target_name: str):
    normalized_target = normalize_name(target_name)
    for contact in contacts:
        if contact.matches_name(normalized_target):
            return contact
    return None

def checkpoint_functions() -> list[str]:
    return ["add_contact", "list_contacts", "find_contact"]

def checkpoint_plan() -> dict[str, str]:
    return {
        "main": "main.py handles menu",
        "utils": "utils.py normalizes search",
        "class_name": "Contact",
        "features": "add, list, search",
        "readiness": "modular, readable, in-memory organizer"
    }

def main() -> None:
    ada = Contact("Ada", "5551234")
    grace = Contact("Grace", "5552222")
    linus = Contact("Linus", "5557777")

    print("Class defined: Contact(name, phone)")
    print(f"Object created: {ada.name} / {ada.phone}")
    print(f"Display method: {ada.display()}")
    print(f"Method call result: {ada.announce_ready()}")
    print("self reminder: self refers to the current object")

    contacts = [ada, grace, linus]
    found = find_contact_by_name(contacts, "grace")
    missing = find_contact_by_name(contacts, "Maya")
    print(f"Found contact: {found.display()}")
    print(f"Missing contact: {missing}")
    print("Search uses normalize: 'grace' matched 'Grace'")
    found.update_phone("5553333")
    print(f"Updated phone: {found.display()}")
    print(f"Object count: {len(contacts)}")

    valid_result = found.update_phone("5554444")
    invalid_result = found.update_phone("55-abc")
    print(f"Valid update accepted: {valid_result}")
    print(f"Stored phone after valid update: {found.phone}")
    print(f"Invalid update accepted: {invalid_result}")
    print(f"Stored phone after invalid update: {found.phone}")
    print("Validation location: class methods keep business rules together")

    plan = checkpoint_plan()
    print(f"Checkpoint functions: {', '.join(checkpoint_functions())}")
    print(f"Checkpoint module plan: {plan['main']}, {plan['utils']}")
    print(f"Checkpoint class used: {plan['class_name']}")
    print(f"Checkpoint features: {plan['features']}")
    print(f"Checkpoint readiness: {plan['readiness']}")

if __name__ == "__main__":
    main()

