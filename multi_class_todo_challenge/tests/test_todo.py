from lib.todo import *

def test_todo_creates_new_instance_with_task():
    todo = Todo("walk the dog")
    assert isinstance(todo, Todo)
    assert todo.task == "walk the dog"
    
    
def test_todo_mark_complete_change_complete_to_True():
    todo1 = Todo("walk the dog")
    todo2 = Todo("cook dinner")
    todo1.mark_complete()
    assert todo1.complete == True
    assert todo2.complete == False