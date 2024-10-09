
class Readable_entry_finder():
    def __init__(self):
        pass
    def extract_entry(self, entries, wpm ,minutes):
        max_words = wpm * minutes
        entries_user_can_read = []
        for entries in entries:
            if entries.count_content() <= max_words:
                # print("entries.count_content:    ", entries.count_content())
                entries_user_can_read.append(entries)
        print(entries_user_can_read)
        if entries_user_can_read == []:
            return None
        
        if len(entries_user_can_read) > 1:
            return max(entries_user_can_read, key=lambda x: x.count_content())