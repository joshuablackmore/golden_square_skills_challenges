
class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todos.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        return [items for items in self.todos if items.complete == False]

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        return [items for items in self.todos if items.complete == True]


    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self.todos:
            if todo.complete == False:
                todo.complete = True
    
# todo_list = TodoList()
# todo1 = Todo("feed the chickens")
# todo2 = Todo("walk the dog")
# todo3 = Todo("cook dinner")
# todo_list.add(todo1)
# todo_list.add(todo2)
# todo_list.add(todo3)
# todo1.mark_complete()

# print(todo_list.incomplete())