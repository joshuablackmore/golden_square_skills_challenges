from lib.diary import *
from lib.diary_entry import *
from lib.todo import *
from lib.todo_list import *

import pytest

def test_diary_instance_and_empty_lists_for_variables():
    diary = Diary()
    assert isinstance(diary, Diary)
    assert diary.entries == []
    assert diary.phone_numbers == []
    # assert diary.todos == []

def test_add_diary_throws_exception_if_None():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.add_diary(None)
    assert str(e.value) == "You must called add_diary with a diary entry instance"

def test_diary_list_todos():
    diary = Diary()
    todo = Todo("walk the dog")
    todo_list = Todo_list()
    todo_list.add_todo(todo)
    assert diary.list_todos(todo_list) == [todo]