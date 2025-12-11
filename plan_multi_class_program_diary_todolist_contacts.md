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
│ -add(DiaryEntry)           │       -incomplete=>incomplete todo│  │                     │
│ -get_diary_contacts        │       -complete=>complete todos   │  │                     │
│                            │   │   -give_up                    │  │                     │
└────────────────────────────┘   ├───────────────────────────────┘  └────────▲────────────┘
           │                     │          │                                │             
           │list of              └ ┌────────┼────────┐            ┌──────────┼───────────┐ 
 ┌───────────────────────────┐     │ ToDo(task)      │            │ Contact(number)      │ 
 │DiaryEntry(title, contents)│     │ -mark_complete  │            └──────────────────────┘  
 │-diaryentry.contacts []    │     │ -add_contact    │          
 │-diaryentry.todos []       │     │ -get_contacts   │            
 │-add contact               │     └─────────────────┘                                     
 │-add todo                  │                                                             
 │-get contacts              │                                                             
 │- get todos                │                                                                                                                    
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
    #   date: a string representing the date in 'YYYY-MM-DD' format
    #   todo_contacts: list of contact objects associated with the task
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task: str, date: str):
        # Parameters:
        #   task: a string representing the task to be done
        #   date: a string representing the date in 'YYYY-MM-DD' format
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
        #   Adds the contact to the todo_contacts list
        pass

    def get_contacts(self)
        # Parameter:
        #   None
        # Returns:
        #   List of all phone numbers associated to the task
        # Side-effects:
        #   None

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
    #   date: a string
    #   diaryentry_todos: list
    #   diaryentry_contacts: list

    def __init__(self, title: str, contents: str, date: str): # title, contents are strings
        # Side-effects:
        #   Sets the title, contents and date properties
        # Notes:
        #   Creates related_todos []
        #   Created related_contacts []
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

    def add_contact(self, contact: Contact):
        # Parameter:
        #   contact: instance variable object of the Contact class
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the contact to the diary entry
        pass

    def add_todo(self, todo: ToDo):
        # Parameter:
        #   todo: instance variable object of the ToDo class
        # Returns:
        #   Nothing
        # Side-effects:
        #   adds the todo to related_todos
        #   adds the todo contacts to related_contacts
        pass

        def get_contacts(self)
        # Parameter:
        #   None
        # Returns:
        #   List of all contact objects related to the diary entry (related_contacts)
        # Side-effects:
        #   None

        def get_todos(self)
        # Parameter:
        #   None
        # Returns:
        #   List of all todo ojbects related to the diary entry (related_todos) 
        # Side-effects:
        #   None

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

# File: lib/contact.py
class Contact:
    # Public Properties:
    #   phone: a string

    def __init__(self, phone: str):
        # Side-effects:
        #   Sets the phone property
        pass

# File: lib/planner.py
class Planner:
    def __init__(self)
    pass

    def get_date(self, date: str)
        # Parameters:
        #   date: a string in 'YYYY-MM-DD' format
        # Returns:
        #   all todos and diary entries from that date
        # Side-effects:
        #   None
        pass

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python

# ToDo and ToDo List Integration Tests

"""
Given a ToDo List and two ToDos
When we add those two todos
Those todos are reflected in the todo list
"""
mylist = ToDoList()
todo1 = ToDo("Wash the dishes")
todo2 = ToDo("Mow the lawn")
mylist.add(todo1)
mylist.add(todo2)
mylist.all_todos => ["Wash the dishes", "Mow the lawn"]

"""
Given a ToDo List and three added ToDos
When we mark two of those as complete and call complete()
Only completed todos are returned
"""
mylist = ToDoList()
todo1 = ToDo("Wash the dishes")
todo2 = ToDo("Mow the lawn")
todo3 = ToDo("Feed the cat")
mylist.add(todo1)
mylist.add(todo2)
mylist.add(todo3)
todo1.mark_complete()
todo3.mark_complete()
mylist.complete => ["Wash the dishes", "Feed the cat"]

"""
Given a ToDo List and three added ToDos
When we mark one of those as complete and call incomplete()
Only incomplete todos are returned
"""

mylist = ToDoList()
todo1 = ToDo("Wash the dishes")
todo2 = ToDo("Mow the lawn")
todo3 = ToDo("Feed the cat")
mylist.add(todo1)
mylist.add(todo2)
mylist.add(todo3)
todo1.mark_complete()
mylist.incomplete => ["Mow the lawn", "Feed the cat"]

"""
Given a ToDo List and two added ToDos
When we call giveup() all are marked as completed
"""
mylist = ToDoList()
todo1 = ToDo("Wash the dishes")
todo2 = ToDo("Mow the lawn")
mylist.add(todo1)
mylist.add(todo2)
mylist.give_up()
mylist.complete() => ["Wash the dishes", "Mow the lawn"]
todo1.complete == True
todo2.complete == True

# ToDo and Contacts Integration Tests

"""
Given a ToDo with two added contacts
Calling get_contacts returns a list of phone numbers
"""
todo1 = ToDo("Wash the dishes")
contact1 = Contact(07123456789)
contact2 = Contact(07987654321)
todo1.add_contact(contact1)
todo1.add_contact(contact2)
todo1.get_contacts() => [contact1, contact2]

# Diary and Diary Entry Integration Tests
"""
Calling count_words on a diary object
Returns the sum of words in contents for all diary_entry objects
"""
entry1 = DiaryEntry("My Title", "This is the contents")
entry2 = DiaryEntry("Second Entry", "These are more words")
mitch = Diary()
mitch.add(entry1)
mitch.add(entry2)
mitch.count_words() => 8

"""
Given the wpm of 4 and sum of words in contents for all diary_entry objects is 8
Return 2 as an integer
"""
entry1 = DiaryEntry("My Title", "This is the contents")
entry2 = DiaryEntry("Second Entry", "These are more words")
mitch = Diary()
mitch.add(entry1)
mitch.add(entry2)
mitch.reading_time(4) => 2

"""
Given a wpm of 3 and minutes of 2, and one diary entry with 8 words in the contents and one diary entry with 6 words in the contents
Returns the diary entry with 6 words in the contents
"""
entry1 = DiaryEntry("My Title", "This is the contents with eight words in")
entry2 = DiaryEntry("Second Entry", "This entry has only six words")
mitch = Diary()
mitch.add(entry1)
mitch.add(entry2)
mitch.find_best_entry_for_reading_time(3) => 
"Second Entry\n This entry has only six words"

"""
Given a wpm of 3 and 2 minutes, and one diary entry with 8 words in the contents and two diary entries with 6 words in the contents
Returns only the first diary entry with 6 words in the contents
"""

entry1 = DiaryEntry("My Title", "This is the contents with eight words in")
entry2 = DiaryEntry("Second Entry", "This entry has only six words")
entry3 = DiaryEntry("Third Entry", "Six words, this entry also has")
mitch = Diary()
mitch.add(entry1)
mitch.add(entry2)
mitch.find_best_entry_for_reading_time(4) => 
"Third Entry\n"
"Six words, this entry also has"

# Contact and Contact List Integration Tests
"""
Given a contact list with two added contacts
all_contacts returns a list of added contact objects
"""
contact1 = Contact(07111111111)
contact2 = Contact(07111111112)
contactlist1 = ContactList()
contactlist1.add(contact1)
contactlist1.add(contact2)
contactlist1.all_contacts() => [contact1, contact2]

# Diary Entry and ToDo Integration Tests
"""
Given a diary entry with two related todos
Calling get_todos
Returns a list of todo objects
"""
entry1 = DiaryEntry("My Title", "This is my diary entry")
todo1 = ToDo("Wash the dishes")
todo2 = ToDo("Mow the lawn")
entry1.add_todo(todo1)
entry1.add_todo(todo2)
entry1.get_todos() => [todo1, todo2]

# Diary Entry, ToDo and Contact Integration Tests

"""
Given a diary entry with two related todos, that have two related contacts each
Calling get_contacts
Returns a list of the contact objects associated to those todos
"""

entry1 = DiaryEntry("My Title", "This is my diary entry")
todo1 = ToDo("Wash the dishes")
todo2 = ToDo("Mow the lawn")
entry1.add_todo(todo1)
entry1.add_todo(todo2)
contact1 = Contact(07111111111)
contact2 = Contact(07111111112)
todo1.add_contact(contact1)
todo1.add_contact(contact2)
contact3 = Contact(07111111113)
contact4 = Contact(07111111114)
todo1.add_contact(contact3)
todo1.add_contact(contact4)
entry1.get_contacts(0) => [contact1, contact2, contact3, contact4]


```


## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

# Diary Unit Tests
"""
On instantiating the Diary class
An empty list is initialised
"""
mitch = Diary()
mitch.entries => []

"""
Adding two entries to diary and calling 'all'
Returns the self.entries list
"""
mitch = Diary()
mitch.add("entry1")
mitch.add("entry2")
mitch.all() => ["entry1", "entry2"]

# DiaryEntry Unit Tests

"""
Given a diary entry with a title and contacts
Two empty lists are returned on diaryentry_contacts and diaryentry_tasks
"""
entry = DiaryEntry("My Title", "This is the contents")
entry.diaryentry_contacts => []
entry.diaryentry_tasks => []

"""
Given a diary entry with a title and contacts
Calling get_contacts
Returns an empty list
"""
entry = DiaryEntry("My Title", "This is the contents")
entry.get_contacts() => []

"""
Given a diary entry with a title and contacts
Calling get_todos
Returns an empty list
"""
entry.get_todos() => []

"""
Calling format method
Returns the diary entry object written as :
"title
contents"
"""
entry = DiaryEntry("My Title", "This is the contents")
entry.format() => "My Title"
"This is the contents"

"""
Calling count_words method
Returns the word count of contents as an integer
"""
entry = DiaryEntry("My Title", "This is the contents")
entry.format() => 4

"""
Calling reading_time method with a wpm of 2 and a contents of length 4
Returns 2 as an integer
"""
entry = DiaryEntry("My Title", "This is the contents")
entry.reading_time(2) => 2

"""
Calling reading_time method with a wpm of 5 and a contents of length 4
Rounds up 0.8 to 1 and returns 1 as an integer
"""
entry = DiaryEntry("My Title", "This is the contents")
entry.reading_time(5) => 1

"""
Calling reading_chunk method with 2 wpm for 1 minute
Returns the 1st and 2nd word.
"""
entry = DiaryEntry("My Title", "This is the contents")
entry.reading_chunk(2, 1) => "This is"

"""
Calling reading_chunk method twice with 2 wpm for 1 minute
Returns the 1st and 2nd word, then the 3rd and 4th word.
"""
entry = DiaryEntry("My Title", "This is the contents")
entry.reading_chunk(2, 1)
entry.reading_chunk(2, 1) => "the contents"


"""
Calling reading_chunk method after having read all contents (e.g. reading four-word contents thrice with 2 wpm for 1 minute)
Returns the first two words
"""
entry = DiaryEntry("My Title", "This is the contents")
entry.reading_chunk(2, 1)
entry.reading_chunk(2, 1)
entry.reading_chunk(2, 1) => "This is"

"""
Calling reading_chunk method twice with 3 wpm for 1 minute with a contents of 4 words
Returns the 1st, 2nd word and 3rd word, then just the 4th word.
"""
entry = DiaryEntry("My Title", "This is the contents")
entry.reading_chunk(3, 1) => "This is the"
entry.reading_chunk(3, 1) => "contents"

"""
Instantiating a DiaryEntry without providing a Title argument
Raises an Exception error
"""
entry = DiaryEntry("", "This is the contents with eight words in") => "Diary entries must have a title"

"""
Instantiating a DiaryEntry without providing a contents argument
Raises an Exception error
"""
entry = DiaryEntry("My Title", "") => "Diary entries must have a contents"

# class ToDo Unit Tests

"""
Given a todo with a task
The task is reflected in the task property
"""
todo1 = ToDo("Wash the dishes")
todo1.task => "Wash the dishes"

"""
Given a todo with a task
The complete property reflects the incomplete status
"""
todo1 = ToDo("Wash the dishes")
todo1.complete => False

"""
Given a todo with a task
Marking the task as complete updates the complete property
"""
todo1 = ToDo("Wash the dishes")
todo1.markcomplete()
todo1.complete => True

"""
Given a todo with a task
An empty todo_contacts list is created
"""
todo1 = ToDo("Wash the dishes")
todo1.todo_contacts => []
"""
Given a todo with an empty task
Raise an Exception error
"""
todo1 = ToDo("") => "Task must not be empty"

# class ToDo_List Unit Tests

"""
Given a todo list with no tasks
An empty list is created for all_todos
"""
mylist = ToDoList()
mylist.all_todos => []

# class Contact Unit Tests
"""
Given a contact with a number
The number is associated with the number property
"""
contact1 = Contact(07111111111)
contact1.phone => 07111111111

# class Contact List Unit Tests
"""
Given a Contact List
An empty list called all_contacts is initialized
"""

contactlist1 = ContactList()
contactlist1.all_contacts => []
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
