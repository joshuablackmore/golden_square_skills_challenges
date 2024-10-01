from lib.class_exercise import *

import pytest

def test_errors_on_empty_title_and_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry("", "")
    assert str(e.value) == "Diary entries must have a title or contents"


#given a tittle and title contents
#format() returns a formatted entry, like:
#"My Title: these are the contents"

def test_format_with_title_and_contents():
    diary_entry = DiaryEntry("My title", "Some contents")
    
    result = diary_entry.format()
    assert result == "My title: Some contents"
    
#count_words return the number of words in the diary entry

def test_count_words_in_both_title_and_contents():
    diary_entry = DiaryEntry("My title", "Some contents")
    result = diary_entry.count_words()
    assert result == 4
    

#given an int of words per minute based on the speed in which a user can read. reading_time return an esmated time it would take to read contents of diary.

def test_reading_time_with_5wpm_and_10_words():
    diary_entry = DiaryEntry("A much longer title with", "a much longer contents again")
    result = diary_entry.reading_time(7)
    assert result == 2
    
def test_reading_time_with_0wpm():
    diary_entry = DiaryEntry("A much longer title with", "a much longer contents again")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    assert str(e.value) == "Cannont calculate with zero words per minute"


#given a contents of 6 words
#and a wpm of 2 
#and minutes of 2
#reading_chunk returns the first four words.

def test_reading_chunk_with_two_wpm_and_one_minutes():
    diary_entry = DiaryEntry("My title", "one two three four five six")
    result = diary_entry.reading_chunk(2,2)
    assert result == "one two three four"
    
def test_reading_chunk_with_multiple_calls():
    diary_entry = DiaryEntry("My title", "one two three four five six")
    assert diary_entry.reading_chunk(2,1) == "one two"
    assert diary_entry.reading_chunk(1,1) == "three"
    assert diary_entry.reading_chunk(2,1) == "four five"
    assert diary_entry.reading_chunk(2,5) == "six"