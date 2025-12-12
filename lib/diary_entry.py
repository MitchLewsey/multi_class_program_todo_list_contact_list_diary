import math

class DiaryEntry():
    def __init__(self, title: str, contents: str):
        if title == None:
            raise Exception("Diary entries must have a title")
        if contents == None:
            raise Exception("Diary entries must have a contents")
        self.title = title
        self.contents = contents
        self.diaryentry_contacts = []
        self.diaryentry_tasks = []
        self.starting_word_position = 0
    
    def count_words(self):
        return len(self.contents.split())
    
    def reading_time(self, wpm: int):
        return math.ceil(len(self.contents.split())/wpm)
    
    def reading_chunk(self, wpm: int, minutes: int):
        number_of_words = wpm * minutes #calculate total words to read

        contents_list = self.contents.split(" ") #turn the contents into a list for slicing
        ending_word_position = self.starting_word_position + number_of_words #end position of slice
        words_to_read = contents_list[self.starting_word_position:ending_word_position] #get the words to read

        self.starting_word_position += number_of_words #update starting position for next time

        if ending_word_position >= len(contents_list): #if our ending position is after the contents is finished
            self.starting_word_position = 0 #set the starting position to 0
        return " ".join(words_to_read)
    
    def get_contacts(self):
        return self.diaryentry_contacts
    
    def add_contact(self, contact: "Contact"):
        self.diaryentry_contacts.append(contact)
    
    def get_todos(self):
        return self.diaryentry_tasks
    
    def add_todo(self, todo: "ToDo"):
        self.diaryentry_tasks.append(todo)
        for contact in todo.todo_contacts:
            self.diaryentry_contacts.append(contact)

