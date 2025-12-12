from lib.todo_list import *
import pytest
"""
Given a todo list with no tasks
An empty list is created for all_todos
"""
def test_creating_todo_list_creates_empty_list():
    mylist = ToDoList()
    actual = mylist.all_todos
    expected = []
    assert actual == expected