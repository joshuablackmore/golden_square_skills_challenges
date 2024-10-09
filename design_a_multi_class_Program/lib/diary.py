import re
from lib.phone_number_extractor import Phone_Number_extractor
class Diary():
    
    def __init__(self):
        self.entries = []


    def add_diary(self, diary_instance):
        if diary_instance == None:
            raise Exception("You must called add_diary with a diary entry instance")
        self.entries.append(diary_instance)

    def list_complete_todos(self, todo_list_instance):
        return [todo for todo in todo_list_instance.todos if todo.complete]
    
    def list_incomplete_todos(self, todo_list_instance):
        return [todo for todo in todo_list_instance.todos if not todo.complete]
    
    def list_diary_entries(self):
        return self.entries

    def find_best_entry_for_reading_time(self, wpm, minutes):
        max_words = wpm * minutes
        entries_user_can_read = []
        for entries in self.entries:
            if entries.count_content() <= max_words:
                # print("entries.count_content:    ", entries.count_content())
                entries_user_can_read.append(entries)
        print(entries_user_can_read)
        if entries_user_can_read == []:
            return None
        
        if len(entries_user_can_read) > 1:
            return max(entries_user_can_read, key=lambda x: x.count_content())
        
        return self.entries[0]
    
    def extract_phone_numbers(self):
        phone_number_extractor = Phone_Number_extractor()
        return phone_number_extractor.extract(self.entries)


