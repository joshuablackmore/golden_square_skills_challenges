import re
from lib.phone_number_extractor import Phone_Number_extractor
from lib.readable_entry_finder import Readable_entry_finder
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
        readable_entry_finder = Readable_entry_finder()
        return readable_entry_finder.extract_entry(self.entries,wpm,minutes)
    
    def extract_phone_numbers(self):
        phone_number_extractor = Phone_Number_extractor()
        return phone_number_extractor.extract(self.entries)


