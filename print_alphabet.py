"""
import string

# alphabet = string.ascii_lowercase
alphabet = string.ascii_uppercase

for letter in alphabet:
    print(letter, end="")
"""
for i in range(ord('a'), ord('z') + 1):
    # Print the alphabet
    print(chr(i), end="")
