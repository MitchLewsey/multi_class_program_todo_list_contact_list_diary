from lib.diary import *
from lib.diary_entry import *
import pytest

"""
Calling count_words on a diary object
Returns the sum of words in contents for all added diary_entry objects
"""
def test_count_words_two_by_four_word_contents_returns_eight():
    entry1 = DiaryEntry("My Title", "This is the contents")
    entry2 = DiaryEntry("Second Entry", "These are more words")
    mitch = Diary()
    mitch.add(entry1)
    mitch.add(entry2)
    actual = mitch.count_words()
    expected = 8
    assert actual == expected

"""
Given the wpm of 4 and sum of words in contents for all diary_entry objects is 8
Return 2 as an integer
"""
def test_four_wpm_eight_words_returns_two():
    entry1 = DiaryEntry("My Title", "This is the contents")
    entry2 = DiaryEntry("Second Entry", "These are more words")
    mitch = Diary()
    mitch.add(entry1)
    mitch.add(entry2)
    actual = mitch.reading_time(4)
    expected = 2
    assert actual == expected

"""
Given a wpm of 3 and minutes of 2, and one diary entry with 8 words in the contents and one diary entry with 6 words in the contents
Returns the diary entry with 6 words in the contents
"""
def test_reading_chunk_three_wpm_two_mins_returns_entry_six_words():
    entry1 = DiaryEntry("My Title", "This is the contents with eight words in")
    entry2 = DiaryEntry("Second Entry", "This entry has only six words")
    mitch = Diary()
    mitch.add(entry1)
    mitch.add(entry2)
    actual = mitch.find_best_entry_for_reading_time(3, 2)
    expected = "This entry has only six words"
    assert actual == expected