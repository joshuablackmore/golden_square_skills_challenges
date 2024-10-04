from xmlrpc.client import Boolean
from lib.diary_entry import DiaryEntry

import pytest


def test_diary_entry_instnace():
    diary_entry = DiaryEntry("my title", "contents of entry")
    assert isinstance(diary_entry, DiaryEntry)
    assert diary_entry.title == "my title"
    assert diary_entry.contents == "contents of entry"
    
def test_diary_count_words():
    diary_entry = DiaryEntry("my title", "contents of entry")
    assert diary_entry.count_words() == 3
    
        
    
@pytest.mark.parametrize("none_valid_inputs", [None, float,'1',[1],Boolean])
def test_reading_time_invalid_inputs_exception(none_valid_inputs):
    diary_entry = DiaryEntry("my title", "contents of entry")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(none_valid_inputs)
    assert str(e.value) == "Please enter your Number of words per minute - must be a number"

def test_reading_time_5_wpm_with_7_words_return():
    diary_entry = DiaryEntry("reading time title", "one two three four five one two three")
    assert diary_entry.reading_time(5) == int(2)
    
    
def test_reading_chunk_5wpm_1min_9words_returns_five_words_then_remaining_four_words():
    diary_entry = DiaryEntry("reading chunk title", "one two three four five six seven eight nine")
    assert diary_entry.reading_chunk(5, 1) == "one two three four five"
    assert diary_entry.reading_chunk(5, 1) == "six seven eight nine"
    
    
def test_reading_chunk_4_wpm_1_minute_13_words():
    diary_entry = DiaryEntry("13 words title!", "one two three four five six seven eight nine ten eleven twelve thirteen")
    assert diary_entry.reading_chunk(4,1) == "one two three four"
    assert diary_entry.reading_chunk(4,1) == "five six seven eight"
    assert diary_entry.reading_chunk(3,1) == "nine ten eleven"
    assert diary_entry.reading_chunk(4,1) == "twelve thirteen"