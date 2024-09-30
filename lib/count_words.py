def count_words(input):
    if not isinstance(input, str):
        raise TypeError("Input must be a string")
    lis = input.split(" ")
    return len(lis)
