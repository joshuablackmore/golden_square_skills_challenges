# File: lib/diary_entry.py

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents
        self.reading_chunk_so_far = 0
    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        return len(self.contents.split(" "))

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        if not isinstance(wpm, (int)):
            raise Exception("Please enter your Number of words per minute - must be a number")
        
        return int(round(len(self.contents.split(" ")) / wpm,0))

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        
        #total amount of words the user reads each time function is called.
        max_words = wpm * minutes
        #words split up into a list.
        words = self.contents.split(" ")
        #the starting position of contents each time function is called.
        chunk_start = self.reading_chunk_so_far
        #sets the end index each time function is called. 
        chunk_end = self.reading_chunk_so_far + max_words
        #splits words into new variable
        chunk_words = words[chunk_start:chunk_end]
        #resets reading_chunk_so_far in state for next function call.
        self.reading_chunk_so_far = chunk_end
        return " ".join(chunk_words)
