from lib.diary_entry import *

def test_diary_entry_initialises_and_sets_title_and_content():
    diary_entry = Diary_Entry("title1","one two three four")    
    assert isinstance(diary_entry, Diary_Entry)
    assert diary_entry.title == "title1"
    assert diary_entry.content == "one two three four"


def test_diary_entry_returns_number_of_words_in_content():
    diary_entry = Diary_Entry("title1","one two three four")
    assert diary_entry.count_content() == 4