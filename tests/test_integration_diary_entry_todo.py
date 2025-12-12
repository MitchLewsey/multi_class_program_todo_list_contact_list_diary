from lib.todo import *
from lib.diary_entry import *
"""
Given a diary entry with two related todos
Calling get_todos
Returns a list of todo objects
"""
def test_diary_entry_added_todos_call_get_todos_returns_added():
    entry1 = DiaryEntry("My Title", "This is my diary entry")
    todo1 = ToDo("Wash the dishes")
    todo2 = ToDo("Mow the lawn")
    entry1.add_todo(todo1)
    entry1.add_todo(todo2)
    actual = entry1.get_todos()
    expected = [todo1, todo2]
    assert actual == expected
