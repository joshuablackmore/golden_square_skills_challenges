import pytest
from lib.todo_list import *
from lib.todo import *

def test_todo_list_initiates_with_empty_todo_list():
    todo_list = Todo_list()
    assert isinstance(todo_list, Todo_list)
    assert todo_list.todos == []
    
    
def test_add_todo_raises_exception_with_none():
    todo_list = Todo_list()
    with pytest.raises(Exception) as e:
        todo_list.add_todo(None)
    assert str(e.value) == "You must add a todo instance to this method"
    
def test_todo_list_adds_new_todo_instance_to_self_todos():
    todo_list = Todo_list()
    todo1 = Todo("task one two three")
    todo_list.add_todo(todo1)
    assert todo_list.todos == [todo1]