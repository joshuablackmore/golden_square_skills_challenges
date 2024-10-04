def get_most_common_letter(text):
    counter = {}
    for char in text:
        # print(counter.get(char, 0)+1)
        if char.isalpha():
            counter[char] = counter.get(char, 0) + 1
            print("counter dictionary:--- ", counter)
        
    letter = sorted(counter.values())[-1]
    key = [letters for letters, value in counter.items() if value == letter]
    print("comp key",key)
    return key[0]


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
