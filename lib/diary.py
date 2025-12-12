from lib.diary_entry import *
import math

class Diary():
    def __init__(self):
        self.entries = []

    def add(self, entry: str):
        self.entries.append(entry)
    
    def all(self):
        return self.entries
    
    def count_words(self):
        return sum([entry.count_words() for entry in self.entries])
    
    def reading_time(self, wpm: int):
        return math.ceil(self.count_words() / wpm)
    
    def find_best_entry_for_reading_time(self, wpm: int, minutes: int):
        readable_words = wpm * minutes
        entries_contents = [entry.contents for entry in self.entries]
        for entry in sorted(entries_contents, key=len, reverse=True):
            if len(entry.split()) <= readable_words:
                return entry
        return None