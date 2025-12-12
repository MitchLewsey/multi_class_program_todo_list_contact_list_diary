from lib.diary_entry import *
from lib.contact import *
from lib.todo import *
# Diary Entry, ToDo and Contact Integration Tests

"""
Given a diary entry with two related todos, that have two related contacts each
Calling get_contacts
Returns a list of the contact objects associated to those todos
"""
def test_diary_entry_with_two_todos_with_two_contacts_added_to_related_contacts():
    entry1 = DiaryEntry("My Title", "This is my diary entry")
    todo1 = ToDo("Wash the dishes")
    todo2 = ToDo("Mow the lawn")

    contact1 = Contact("07111111111")
    contact2 = Contact("07111111112")
    contact3 = Contact("07111111113")
    contact4 = Contact("07111111114")

    todo1.add_contact(contact1)
    todo1.add_contact(contact2)
    
    todo1.add_contact(contact3)
    todo1.add_contact(contact4)

    entry1.add_todo(todo1)
    entry1.add_todo(todo2)

    actual = entry1.get_contacts()
    expected = [contact1, contact2, contact3, contact4]
    assert actual == expected

