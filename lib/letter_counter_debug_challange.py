# File: lib/letter_counter.py

class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        most_common = None
        most_common_count = 1
        for char in self.text:
            # print("char in text:--- ", char)
            if not char.isalpha():
                continue
            counter[char] = counter.get(char, 0) + 1
            print('counter[char]:    ',counter)
            if counter[char] > most_common_count:
                # print(counter[char])
                most_common = char
                most_common_count = counter[char]
        return [most_common_count, most_common]


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())
# Intended output:
# [2, "i"]