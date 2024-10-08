from lib.todo_list import *

def test_todolist_initialises():
    todo_list = TodoList()
    assert isinstance(todo_list, TodoList)
    assert todo_list.todos == []
    
