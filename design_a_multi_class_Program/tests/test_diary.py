from lib.diary import *
from lib.diary_entry import *
from lib.todo import *

import pytest

def test_diary_instance_and_empty_lists_for_variables():
    diary = Diary()
    assert isinstance(diary, Diary)
    assert diary.entries == []
    assert diary.phone_numbers == []
    assert diary.todos == []

def test_add_diary_throws_exception_if_None():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.add_diary(None)
    assert str(e.value) == "You must called add_diary with a diary entry instance"
    
def test_add_todo_throws_exception_if_None():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.add_todo(None)
    assert str(e.value) == "You must add a todo instance to this method"