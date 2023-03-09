"""
finditer() is a method in Python's re (regular expression) module that searches for all occurrences of a pattern in a string and returns an iterator that yields match objects for each match.

The syntax for using finditer() is: 
re.finditer(pattern, string, flags=0)
pattern: A regular expression pattern that you want to search for in the string.
string: The string to be searched.
flags: Optional flags that modify the behavior of the search. They are specified as constants in the re module, and can be combined using the bitwise OR operator (|).

"""
import re

string = """The quick brown fox jumps over the lazy dog.
333-445-7898
6678-333-33
hjk9hkjkl@yahoo.com
corey-321-sho@my-work.uk
onwukaebuka-278@gmail.com
mr. scout
Mr John
"""
pattern = r'[a-zA-Z0-9_-]+@[a-zA-Z-]+\.(com|edu|uk)'  # Find all words that are 5 letters long

for match in re.finditer(pattern, string):
    print(
        f"Found '{match.group()}' starting at index {match.start()} and ending at index {match.end()}.")
