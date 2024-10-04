class Todos():
    def __init__(self):
        self._todos = []
        
    def add(self, item):
        if item is None or not isinstance(item, str) or item.strip() == "":
            raise Exception("No todo item entered, please enter an item.")
        
        self._todos.append(item)
        
    def remove(self, item_to_delete):
        if item_to_delete is None or not isinstance(item_to_delete, str) or item_to_delete.strip() == "":
            raise Exception("No remove item entered, please enter an item to remove")
        
        if item_to_delete in self._todos:
            i = self._todos.index(item_to_delete)
            self._todos.pop(i)
        else:
            return "This todo item is not in your list"
        
    def display_todos(self):
        return self._todos
    
# test
    
    