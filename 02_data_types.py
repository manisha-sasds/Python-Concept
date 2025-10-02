	
import sys

# Python has 14 data Types, and they are classified into 6 Types. 

#1.	Fundamental Category Data Types
#1.1.	int # Purpose is to store the whole number in main memory , int dataty pe can  stored 4 typs if differet=t numer ssystem 4 Types of Number Systems. They are
 
#   1.1.1 Decimal Number System [Numbers 0-9 ,Base 10]
#	1.1.2 Binary Number System [Numbers 0 and 1  ,Base 2]
#	1.1.3 Octal Number System [Numbers 0-9 ,Base 10]
#	1.1.4 Hexa Decimal Number System [Numbers 0-9 and A-F,Base 16]]

# Storing numbers in different number systems using int
decimal_num = 123       # Decimal
# Momory Grows with digits
small_int = 7                 # 1 digit
medium_int = 1234567890       # 10 digits
large_int = 10**50            # 1 followed by 50 zeros

print("Memory for small_int:", sys.getsizeof(small_int), "bytes") # 28 bytes
print("Memory for medium_int:", sys.getsizeof(medium_int), "bytes") # 36 bytes
print("Memory for large_int:", sys.getsizeof(large_int), "bytes") # 72 bytes

a=0b1101    # Binary    # Python is High Level Programming Language, so it converts Binary, Octal , Hexadecimal to decimal internally.
print(a,type(a))  # 13 <class 'int'>

binary_num = 0b101     # Binary    
a=0o27
print('Binary number a is = ',a,type(a))  # 23 <class 'int'>
print(bin(13))  # '0b1101'

octal_num = 0o17        # Octal
a=0o27 
print('Ocatl number a is = ',a,type(a))  #23 <class 'int'>
print(oct(89))  # '0o131'

hex_num = 0x1A          # Hexadecimal
print(hex_num,type(hex_num))  # 26 <class 'int'>
a =0xAC
print('Hexa Decimal number a is = ',a,type(a))  # 172 <class 'int'>
print(hex(3054)) # '0XBEE'


#1.2.	float # Purpose is to store the decimal number or scientific notation in main memory , it saves momory,
# Float data does not support Binary, Octal nad Hexa Decimal Number System Values for storing float values.

x = 3.14       # Decimal float
y = 2.5e3      # Scientific notation, equals 2500.0

# Float has fixed memory usage(24–28 bytes)
small_float = 7.0
big_float = 1.23e50

print("Memory for small_float:", sys.getsizeof(small_float), "bytes") # 24 bytes
print("Memory for big_float:", sys.getsizeof(big_float), "bytes") # 24 bytes

#1.3.   bool - bool data type holds one of the two values: True(all non zero values) or False(all zero values) ).

a = 280
b = -456
c = 0

print("a is", bool(a))  # True (non-zero number)
print("b is", bool(b))  # True (negative numbers are also True)
print("c is", bool(c))  # False (zero is False)

a, b, c = 2.870, -45.6, 0 # float values
print("float values of a is", bool(a), ", b is", bool(b), ", c is", bool(c)) # True , True , False

a, b,c =2+3j,0+0j, 3+0j # complex values
print("complex values of a is", bool(a), ", b is", bool(b), ", c is", bool(c)) # True , False , True

a,b,c,d="Hello",""," " ," n"# string values
print("string values of a is", bool(a), ", b is", bool(b), ", c is", bool(c), "d is", bool(d)) # True , False , True , True

a,b,c,d=[],[123,876],{} ,{"name":"Jhon"} # list n Dict values
print("List n Dict values of a is", bool(a), ", b is", bool(b), ", c is", bool(c), "d is", bool(d)) # True , False , True , True

#1.4.   complex # Purpose is to store the complex numbers in main memory which has real and imaginary part 
# int to complex
a = 25
print(a, "->", complex(a))

# float to complex
a = 7.8
print(a, "->", complex(a))

# bool to complex
a = False
print(a, "->", complex(a))

# str to complex
a, b, c, d, e = "45", "9.67", "3+4j", "False", "hello"

for val in [a, b, c, d, e]:
    try:
        print(val, "->", complex(val))
    except ValueError:
        print(val, "-> Cannot convert to complex")

#2.     Sequence Category Data Types
#2.1.   str 
#2.2.   bytes      #   Purpose is to store the sequence of byte values (0-255) in main memory, bytes are immutable
#2.3.   bytearray
#2.4.   range
#
#3.     List Category Data Types (Collection Types)
#3.1.   list
#3.2.   tupl
#4.     Set Category Data Types  (Collection Types)
#4.1.   Set
#4.2.   frozenset
#5.     Dict Category  Data Types  (Collection Types)
#5.1.   dict
#6.     None Type Category  Data Types
#6.1.   nonetype





