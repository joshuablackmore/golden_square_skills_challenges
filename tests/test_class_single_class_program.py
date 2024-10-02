from lib.class_single_class_program import *

import pytest
def test_Todos_adds_single_todo():
    my_todos = Todos()
    my_todos.add("first todo item")
    assert my_todos._todos == ["first todo item"]
    
def test_Todos_adds_without_arg_raises_exception():
    my_todos = Todos()
    with pytest.raises(Exception) as e:
        my_todos.add(None)
    assert str(e.value) == "No todo item entered, please enter an item."
    
def test_Todos_Remove_adds_two_todos_and_removes_one_todo():
    my_todos = Todos()
    my_todos.add("first")
    my_todos.add("second")
    my_todos.remove("first")
    assert my_todos._todos == ["second"]
    
def test_Todos_Remove_returns_message_if_todo_not_in_list():
    my_todos = Todos()
    my_todos.add("one")
    result = my_todos.remove("two")
    assert result == "This todo item is not in your list"
    
def test_Todos_Remove_no_arg_raises_exception():
    my_todos = Todos()
    with pytest.raises(Exception) as e:
        my_todos.remove(None)
    assert str(e.value) == "No remove item entered, please enter an item to remove"