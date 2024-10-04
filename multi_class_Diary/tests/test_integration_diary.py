from lib.diary import Diary
from lib.diary_entry import DiaryEntry


def test_diary_add_adds_diary_entry_instance():
    diary_entry_1 = DiaryEntry("my title", "contents of entry")
    diary = Diary()
    diary.add(diary_entry_1)
    assert diary.entries[0].title == "my title"
    assert diary.entries[0].contents == "contents of entry"
    

def test_diary_all_returns_list_of_diaryentry_instances():
    diary_entry_1 = DiaryEntry("my title", "contents of entry")
    diary_entry_2 = DiaryEntry("my title 2", "contents of entry on second entry")
    diary_entry_3 = DiaryEntry("my titl number 3", "contents of entry on the amazing third entry")
    
    diary = Diary()
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    
    assert diary.all() == [diary_entry_1,diary_entry_2,diary_entry_3]
    
    
def test_diary_count_returns_10_with_two_instances_of_5_contents():
    diary_entry_1 = DiaryEntry("my title", "contents of entry four five")
    diary_entry_2 = DiaryEntry("my title 2", "contents of entry on second")
    diary = Diary()
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.count_words() == 10