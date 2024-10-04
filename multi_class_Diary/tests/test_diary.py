from lib.diary import Diary

def test_diary():
    diary = Diary()
    assert isinstance(diary, Diary)
    assert diary.entries == []
    
def test_diary_all_returns_empty_list():
    diary = Diary()
    assert diary.all() == []