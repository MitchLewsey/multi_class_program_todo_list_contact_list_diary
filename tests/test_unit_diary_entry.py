from lib.diary_entry import *
import pytest

"""
Given a diary entry with a title and contacts
Two empty lists are returned on diaryentry_contacts and diaryentry_tasks
"""
def test_empty_list_contacts_and_tasks_initialized():
    entry = DiaryEntry("My Title", "This is the contents")
    actual1 = entry.diaryentry_contacts
    actual2 = entry.diaryentry_tasks
    expected = []
    assert actual1 == expected
    assert actual2 == expected

"""
Given a diary entry with no added contacts
Calling get_contacts
Returns an empty list
"""
def test_no_added_contacts_get_contacts_returns_empty_list():
    entry = DiaryEntry("My Title", "This is the contents")
    actual = entry.get_contacts()
    expected = []
    assert actual == expected

"""
Given a diary entry with a title and contacts
Calling get_contacts
Returns an empty list
"""
def test_no_added_todos_get_todos_returns_empty_list():
    entry = DiaryEntry("My Title", "This is the contents")
    actual = entry.get_todos()
    expected = []
    assert actual == expected

"""
Calling count_words method
Returns the word count of contents as an integer
"""

def test_count_words_contents_four_words_returns_four_words():
    entry = DiaryEntry("My Title", "This is the contents")
    actual = entry.count_words()
    expected = 4
    assert actual == expected

"""
Calling reading_time method with a wpm of 2 and a contents of length 4
Returns 1 as an integer
"""
def test_reading_time_four_wpm_contents_eight_words_returns_two():
    entry = DiaryEntry("My Title", "This is the contents")
    actual = entry.reading_time(2)
    expected = 2
    assert actual == expected

"""
Calling reading_time method with a wpm of 5 and a contents of length 4
Rounds up 0.8 to 1 and returns 1 as an integer
"""

def test_reading_time_four_wpm_contents_four_words_returns_one():
    entry = DiaryEntry("My Title", "This is the contents")
    actual = entry.reading_time(5)
    expected = 1
    assert actual == expected

"""
Calling reading_chunk method twice with 2 wpm for 1 minute
Returns the 1st and 2nd word, then the 3rd and 4th word.
"""
def test_reading_chunk_two_wpm_one_minute_returns_first_two_words():
    entry = DiaryEntry("My Title", "This is the contents")
    actual = entry.reading_chunk(2, 1)
    expected = "This is"
    assert actual == expected

"""
Calling reading_chunk method twice with 2 wpm for 1 minute
Returns the 1st and 2nd word, then the 3rd and 4th word.
"""

def test_reading_chunk_two_wpm_one_minute_twice_returns_third_fourth_words():
    entry = DiaryEntry("My Title", "This is the contents")
    entry.reading_chunk(2, 1)
    actual = entry.reading_chunk(2, 1)
    expected = "the contents"
    assert actual == expected

"""
Calling reading_chunk method after having read all contents (e.g. reading four-word contents thrice with 2 wpm for 1 minute)
Returns the first two words

"""

def test_reading_chunk_two_wpm_one_minute_thrice_returns_third_fourth_words():
    entry = DiaryEntry("My Title", "This is the contents")
    entry.reading_chunk(2, 1)
    entry.reading_chunk(2, 1)
    actual = entry.reading_chunk(2, 1)
    expected = "This is"
    assert actual == expected

"""
Calling reading_chunk method twice with 3 wpm for 1 minute with a contents of 4 words
Returns the 1st, 2nd word and 3rd word, then just the 4th word.
"""
def test_reading_chunk_three_wpm_one_minute_twice_returns_just_fourth_words():
    entry = DiaryEntry("My Title", "This is the contents")
    entry.reading_chunk(3, 1)
    actual = entry.reading_chunk(3, 1)
    expected = "contents"
    assert actual == expected

"""
Instantiating a DiaryEntry without providing a Title argument
Raises an Exception error
"""
def test_empty_title_raises_error():
    with pytest.raises(Exception) as error:
        entry = DiaryEntry(None, "This is the contents with eight words in")
    actual = str(error.value)
    expected = "Diary entries must have a title"
    actual == expected

"""
Instantiating a DiaryEntry without providing a Title argument
Raises an Exception error
"""
def test_empty_contents_raises_error():
    with pytest.raises(Exception) as error:
        entry = DiaryEntry(None, "This is the contents with eight words in")
    actual = str(error.value)
    expected = "Diary entries must have a title"
    actual == expected
