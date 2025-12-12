from lib.todo import *
import pytest

"""
Given a todo with a task
The task is reflected in the task property
"""
def test_creating_todo_sets_task_property():
    todo1 = ToDo("Wash the dishes")
    actual = todo1.task
    expected ="Wash the dishes"
    assert actual == expected

"""
Given a todo with a task
The complete property reflects the incomplete status
"""
def test_creating_todo_sets_complete_property_false():
    todo1 = ToDo("Wash the dishes")
    actual = todo1.complete
    expected = False
    assert actual == expected

"""
Given a todo with a task
Marking the task as complete updates the complete property
"""
def test_marking_todo_complete_updates_complete_property_true():
    todo1 = ToDo("Wash the dishes")
    todo1.mark_complete()
    actual = todo1.complete
    expected = True
    assert actual == expected

"""
Given a todo with a task
An empty todo_contacts list is created
"""
def test_empty_lists_todo_contacts_initialized():
    todo1 = ToDo("Wash the dishes")
    actual = todo1.todo_contacts
    expected = []
    assert actual == expected

"""
Given a todo with an empty task
Raise an Exception error
"""
def test_creating_empty_todo_raises_error():
    with pytest.raises(Exception) as error:
        todo1 = ToDo("") 
    actual = str(error.value)
    expected = "Task must not be empty"
    assert actual == expected