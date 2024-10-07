from lib.todo_list import TodoList
from lib.todo import Todo

def test_todolist_adds_new_todo():
    todo_list = TodoList()
    todo1 = Todo("feed the chickens")
    todo_list.add(todo1)
    assert todo_list.todos == [todo1]
    
def test_todolist_return_incomplete_tasks_with_one_marked_completed():
    todo_list = TodoList()
    todo1 = Todo("feed the chickens")
    todo2 = Todo("walk the dog")
    todo3 = Todo("cook dinner")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)
    todo1.mark_complete()
    assert todo_list.incomplete() == [todo2,todo3]
    
    
def test_todolist_return_complete_tasks_with_two_marked_completed():
    todo_list = TodoList()
    todo1 = Todo("feed the chickens")
    todo2 = Todo("walk the dog")
    todo3 = Todo("cook dinner")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)
    todo1.mark_complete()
    todo3.mark_complete()
    assert todo_list.complete() == [todo1, todo3]
    
    
def test_todolist_giveup_marks_all_todos_as_complete():
    todo_list = TodoList()
    todo1 = Todo("feed the chickens")
    todo2 = Todo("walk the dog")
    todo3 = Todo("cook dinner")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)
    todo_list.give_up()
    
    assert todo_list.complete() == [todo1,todo2,todo3]