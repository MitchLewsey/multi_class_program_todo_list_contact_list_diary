# Diary, Contacts & ToDo List Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
                 ┌────────────────┐                                                        
                 │ Planner        │                                                        
        ┌───────►│ - diary        │                                                        
        │        │ - contact list │◄───────────────────────────────────────┐               
        │        │ - to do list   │   ◄───┐                                │               
        │        │ - get date     │       │                                │               
        │        └────────────────┘       │                                │               
        │                                 │                                │               
        │                                 │                                │               
┌────────────────────────────┐   ┌───────────────────────────────┐  ┌─────────────────────┐
│ Diary                      │   │   To Do List                  │  │ Contact List        │
│ -diary entries             │   │   -todos list                 │  │ -contacts list      │
│ -get_diary_entry(wpm, mins)│   │   - add(todo)                 │  │ - add               │
│ -add(DiaryEntry)           │   │   -incomplete=>incomplete todo│  │ - get contact       │
└────────────────────────────┘   │   -complete=>complete todos   │  │                     │
           │                     │   -give_up                    │  │                     │
           │list of              └───────────────────────────────┘  └────────▲────────────┘
 ┌───────────────────────────┐              │                                │             
 │DiaryEntry(title, contents)│     ┌────────┼────────┐            ┌──────────┼───────────┐ 
 │-diaryentry.contacts []    │     │ ToDo(task)      │            │ Contact(name, number)│ 
 │-diaryentry.todos []       │     │ -mark complete  │            │                      │ 
 │-add contact               │     │                 │            │                      │ 
 │-add todo                  │     └─────────────────┘            └──────────────────────┘ 
 └───────────────────────────┘                                                             
```

_Also design the interface of each class in more detail._

```python
# File: lib/todo_list.py
class ToDoList:
    def __init__(self):
        # Parameters:
        #   None
        # Returns:
        #   Nothing
        # Side-effects:
        #   Creates empty list all_todos = []
        pass

    def add(self, todo: ToDo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        pass

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        pass

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass


# File: lib/todo.py
class ToDo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   contacts: list of contact objects associated with the task
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task: str):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass

    def add_contact(self, contact: Contact):
        # Parameter:
        #   contact: instance variable object of the Contact class
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass

class Diary:
    def __init__(self):
        # Note:
        #   Creates an empty list 'entries'
        pass


    def add(self, entry: DiaryEntry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        pass

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # Note:
        #   This method uses the `count_words` method on DiaryEntry.
        pass

    def reading_time(self, wpm: int):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes 
        #   if the user were to read all entries in the diary.
        # Notes:
        #   Will call count_words to get total words
        pass

    def find_best_entry_for_reading_time(self, wpm: int, minutes: int):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title: str, contents: str): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        pass

    def reading_time(self, wpm: int):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        pass

    def reading_chunk(self, wpm: int, minutes: int):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        pass

    def reading_chunk(self, wpm: int, minutes: int):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        pass

# File: lib/contact_list.py
class ContactList:
    def __init__(self):
        # Parameters:
        #   None
        # Returns:
        #   Nothing
        # Side-effects:
        #   Creates empty list all_contacts = []

    def add(self, contact: Contact):
        # Parameters:
        #   contact: an instance of Contact class
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the contact to the all_contacts list
        pass
        pass
```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
