'''# Python script to add # at the beginning of every line of a file
text="""1.2.	float
1.3.	bool
1.4.	complex

2.	Sequence Category Data Types
2.1.	str
2.2.	bytes
2.3.	bytearray
2.4.	range

3.	List Category Data Types (Collection Types)

3.1.	list
3.2.	tupl
4.	Set Category Data Types  (Collection Types)
4.1.	Set
4.2.	frozenset
5.	Dict Category  Data Types  (Collection Types)
5.1.	dict
6.	None Type Category  Data Types
6.1.	nonetype
"""
# Add # at the beginning of each line
updated_text = "\n".join(f"#{line}" for line in text.splitlines())

print(updated_text)

'''

import sys

x = 172
y = 172.0

print(sys.getsizeof(x))  # Memory used by int
print(sys.getsizeof(y))  # Memory used by float

import sys

# Big integer
big_int = 1230000000000000000

# Float in scientific notation
sci_not = 1.23e18

# Check memory usage
print("Memory for int:", sys.getsizeof(big_int), "bytes")
print("Memory for float (scientific notation):", sys.getsizeof(sci_not), "bytes")

