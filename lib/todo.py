class ToDo():
    def __init__(self, task):
        if task == "":
            raise Exception("Task must not be empty")
        self.task = task
        self.complete = False
        self.todo_contacts = []
        pass

    def mark_complete(self):
        self.complete = True

    def add_contact(self, contact: "Contact"):
        self.todo_contacts.append(contact)