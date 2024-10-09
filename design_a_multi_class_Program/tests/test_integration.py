from lib.diary import *
from lib.diary_entry import *
from lib.todo import *
from lib.todo_list import *

def test_add_diary_takes_diary_entry_instance_and_stores_in_entries():
    diary = Diary()
    diary_entry1 = Diary_Entry("title1", "one two three four five")
    diary.add_diary(diary_entry1)
    assert diary.entries == [diary_entry1]


def test_add_diary_extracts_any_phone_number_and_stores_in_phonenumber_list():
    diary = Diary()
    diary_entry1 = Diary_Entry("title1", "one two three four five")
    diary_entry2 = Diary_Entry("title2", "content with a phone number of 07590123456")
    diary_entry3 = Diary_Entry("title2", "more content with a phone number of 07890123321")
    diary.add_diary(diary_entry1)
    diary.add_diary(diary_entry2)
    diary.add_diary(diary_entry3)
    assert diary.phone_numbers == ['07590123456', '07890123321']

def test_add_todo_adds_new_todo_instance_to_diary_todos_list():
    todo1 = Todo("do the laundy")
    todo2 = Todo("walk the dog")
    # diary = Diary()
    # diary.add_todo(todo1)
    # diary.add_todo(todo2)
    todo_list = Todo_list()
    todo_list.add_todo(todo1)
    todo_list.add_todo(todo2)
    assert todo_list.todos == [todo1, todo2]
    
    
def test_list_diary_entries_returns_list_of_entries():
    diary_entry1 = Diary_Entry("title1", "one two three four")
    diary = Diary()
    diary.add_diary(diary_entry1)
    assert diary.list_diary_entries() == [diary_entry1]

def test_find_best_entry_for_time():
    diary_entry1 = Diary_Entry("title1", "one two three four five six seven")
    diary_entry2 = Diary_Entry("title2", "one two three four five six seven eight")
    diary = Diary()
    diary.add_diary(diary_entry1)
    diary.add_diary(diary_entry2)
    assert diary.find_best_entry_for_reading_time(2,4) == diary_entry2
    
def test_find_best_entry_returns_longest_possible_with_too_long_entry_also():
    diary_entry1 = Diary_Entry("title1", "one two three four five six seven")
    diary_entry2 = Diary_Entry("title2", "one two three four five six seven eight")
    diary_entry3 = Diary_Entry("title3", "one two three four five six seven eight nine ten")
    diary = Diary()
    diary.add_diary(diary_entry1)
    diary.add_diary(diary_entry2)
    diary.add_diary(diary_entry3)
    assert diary.find_best_entry_for_reading_time(2,4) == diary_entry2
    
def test_phone_list_returns_list_of_two_numbers():
    diary = Diary()
    diary_entry1 = Diary_Entry("title1", "one two three four five")
    diary_entry2 = Diary_Entry("title2", "content with a phone number of 07590123456")
    diary_entry3 = Diary_Entry("title2", "more content with a phone number of 07890123321")
    diary.add_diary(diary_entry1)
    diary.add_diary(diary_entry2)
    diary.add_diary(diary_entry3)
    assert diary.phone_list() == ['07590123456','07890123321']
