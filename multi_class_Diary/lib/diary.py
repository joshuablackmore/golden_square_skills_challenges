# File: lib/diary.py
from lib.diary_entry import DiaryEntry

class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self.entries.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.entries
    
    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        return sum(diary_entry.count_words() for diary_entry in self.entries)
    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        return sum(entry.reading_time(wpm) for entry in self.entries)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        words_user_can_read = wpm * minutes
        entries_user_can_read = []
        for entry in self.entries:
            if entry.count_words() <= words_user_can_read:
                entries_user_can_read.append(entry)
                
        if entries_user_can_read == []:
            return None
        
        if len(entries_user_can_read) > 1:
                return max(entries_user_can_read, key=lambda x:x.count_words())
        
        return entries_user_can_read[0]
    
    
diary_entry_1 = DiaryEntry("my title", "one two three four five six seven")
diary_entry_2 = DiaryEntry("my title", "one two three four five six seven eight")
diary = Diary()
diary.add(diary_entry_1)
diary.add(diary_entry_2)

print("longest diary user can read:    - ",diary.find_best_entry_for_reading_time(2,4))


