class ToDoList():
    def __init__(self):
        self.all_todos = []

    def add(self, task):
        self.all_todos.append(task)
    
    def complete(self):
        return [todo.task for todo in self.all_todos if todo.complete]
    
    def incomplete(self):
        return [todo.task for todo in self.all_todos if not todo.complete]
    
    def give_up(self):
        for todo in self.all_todos:
            todo.complete = True
