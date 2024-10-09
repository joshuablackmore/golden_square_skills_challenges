from lib.diary import *
from lib.diary_entry import *
from lib.todo import *
from lib.todo_list import *

import pytest

def test_diary_instance_and_empty_list_for_entries():
    diary = Diary()
    assert isinstance(diary, Diary)
    assert diary.entries == []

def test_add_diary_throws_exception_if_None():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.add_diary(None)
    assert str(e.value) == "You must called add_diary with a diary entry instance"

def test_diary_list_complete_todos():
    diary = Diary()
    todo_complete = Todo("walk the dog")
    todo_incomplete = Todo("do the laundry")
    todo_list = Todo_list()
    todo_list.add_todo(todo_complete)
    todo_list.add_todo(todo_incomplete)
    todo_complete.mark_complete()
    assert diary.list_complete_todos(todo_list) == [todo_complete]
    
    
def test_diary_list_incomplete_todos():
    diary = Diary()
    todo_complete = Todo("walk the dog")
    todo_incomplete = Todo("do the laundry")
    todo_list = Todo_list()
    todo_list.add_todo(todo_complete)
    todo_list.add_todo(todo_incomplete)
    todo_complete.mark_complete()
    assert diary.list_incomplete_todos(todo_list) == [todo_incomplete]
    
    