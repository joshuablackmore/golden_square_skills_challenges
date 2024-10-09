from lib.phone_number_extractor import *
from lib.diary import *
from lib.diary_entry import *



def test_inits_with_empty_phone_list():
    diary_entry1 = Diary_Entry("title1", "one two three four 07590123456")
    phone_number_extractor = Phone_Number_extractor()
    assert phone_number_extractor.phone_numbers == []
    
    
def test_extracts_a_single_phone_number_given_list_of_two_diary_instances():
    diary_entry1 = Diary_Entry("title1", "one two three four 07590123456")
    diary_entry2 = Diary_Entry("title1", "one two three four")
    diary_entry3 = Diary_Entry("title1", "one two three four 07890654321")
    diary = Diary()
    diary.add_diary(diary_entry1)
    diary.add_diary(diary_entry2)
    diary.add_diary(diary_entry3)
    phone_number_extractor = Phone_Number_extractor()
    assert phone_number_extractor.extract([diary_entry1,diary_entry2,diary_entry3]) == ['07590123456','07890654321']