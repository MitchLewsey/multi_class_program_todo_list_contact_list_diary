from lib.diary import *

"""
On instantiating the Diary class
An empty list is initialised
"""
def test_empty_list_on_instantiation():
    mitch = Diary()
    actual = mitch.entries
    expected = []
    assert actual == expected

"""
Adding two instances of diary entry to diary and calling 'all'
Returns the diary entries in a list
"""
def test_adding_two_entries_to_diary_returning_instance_names():
    entry1 = DiaryEntry("Title", "Contents")
    entry2 = DiaryEntry("Title2", "Contents2")
    mitch = Diary()
    mitch.add(entry1)
    mitch.add(entry2)
    actual = mitch.all()
    expected = [entry1 , entry2]
    assert actual == expected