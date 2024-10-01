def encode(text, key):
    # print("Text argument:   ", text)
    # print("Key argument :   ", key)
    cipher = make_cipher(key)
    # print("make_cipher output:    ", cipher)

    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        # print("cipher.index(i):    ", cipher.index(i))
        # print("ciphered_char :    ", ciphered_char)
        # print(i)
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    # encrypted = encrypted.lower()
    cipher = make_cipher(key)
    print("make_cipher output:    ",cipher)
    plaintext_chars = []
    for i in encrypted:
        print("ord(1):   ", ord(i))
        plain_char = cipher[abs(65 - ord(i))]
        print("Plain chars:---  ", plain_char)
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 97) for i in range(26)]
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")