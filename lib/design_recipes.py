
def reading_time(wordsInt):
    words_per_min = 200
    time = wordsInt / words_per_min
    return f"{time} minutes"


def verify_grammar(str):
    first_char = str[0]
    last_char = str[-1]
    
    if first_char.isupper() and last_char == '.':
        return True
    
    return False