
class Todo_list():
    def __init__(self):
        self.todos = []
        
    def add_todo(self, todo_instance):
        if todo_instance == None:
            raise Exception("You must add a todo instance to this method")
        self.todos.append(todo_instance)

