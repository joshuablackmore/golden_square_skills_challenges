from lib.diary import *
from lib.diary_entry import *


def test_diary():
    diary = Diary()
    assert isinstance(diary, Diary)
    assert diary.entries == []
    
def test_diary_all_returns_empty_list():
    diary = Diary()
    assert diary.all() == []
    
    
def test_reading_time_two_entrys_total_6_words_wpm4_returns_1():
    diary_entry1 = DiaryEntry("1st entry","1st bit of contents")
    diary_entry2 = DiaryEntry("1st entry","1st bit")
    diary = Diary()
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.reading_time(4) == 1
    
    
def test_count_words_returns_total_of_all_entries_contents():
    diary_entry1 = DiaryEntry("1st entry","1st bit of contents")
    diary_entry2 = DiaryEntry("1st entry","1st bit three")
    diary = Diary()
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.count_words() == 7