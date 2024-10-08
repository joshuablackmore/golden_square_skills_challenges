from lib.todo import *

# Given a todo item
# #instance stores the todo and complete = false


def test_todo_stores_task_and_set_complete_to_false():
    todo = Todo("first todo item")
    assert isinstance(todo, Todo)
    assert todo.task == "first todo item"
    assert todo.complete == False



"""
# Given a todo item, mark_complete() sets to false
# # """

def test_todo_marks_complete():
    todo = Todo("first todo item")
    todo.mark_complete()
    assert todo.complete == True

