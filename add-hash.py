# Original text (your notes)
notes = """1. Strings- store a sequence of characters
2. Strings can be stored in single or double quotes
3. Multi-line strings use triple quotes
4. strings are immutable - cannot be changed once created
5. strings are iterable - can be looped through
6. strings can be concatenated - can be joined together using + operator
7. strings can be repeated - can be repeated using * operator
8. strings can be sliced - can be accessed using slicing operator
9. strings have many built-in methods - can be used to perform various operations on strings
"""

# Add '#' at the start of each line
commented_notes = "\n".join("# " + line for line in notes.splitlines())

print(commented_notes)
