import re

class Diary():
    
    def __init__(self):
        self.entries = []
        self.phone_numbers = []


    def add_diary(self, diary_instance):
        if diary_instance == None:
            raise Exception("You must called add_diary with a diary entry instance")
        self.entries.append(diary_instance)
        
        #this is my regex pattern
        pattern = r'07\d{9}'
    
        # Search for the pattern in the diary content
        match = re.search(pattern, diary_instance.content)
        if match:
            self.phone_numbers.append(match.group(0))

    def list_todos(self, todo_instance):
        return todo_instance.todos

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

    def phone_list(self):
        return self.phone_numbers


