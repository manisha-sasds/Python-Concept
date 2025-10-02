
# 1. Strings- store a sequence of characters
name ="Jhon"
print(name)
# 2. Strings can be stored in the variable in single or double quotes
str1='Hello'
str2="Jhon"
print(str1,str2) # Hello Jhon
# 3. Multi-line strings use triple quotes
multi_line_str = '''This is a singal quotes multi-line string. 
we can write multiple lines of text here.
we can add more lines here.'''
print(multi_line_str)

multi_line_str1 = """This is a double quotes multi-line string. 
we can write multiple lines of text here."""
print(multi_line_str1)

# 4. strings are immutable - cannot be changed once created
name="Monalisa"
# name[0]='S' # TypeError: 'str' object does not support item assignment
print(name)
# To change the string, we need to create a new string
name="Monalisa" 
name ="S"+name[1:]
print(name) # Sonalisa

# 5. strings are iterable - can be looped through
for char in name:
    print(char)

# 6. strings can be concatenated - can be joined together using + operator
a= "Hello"
b= "Monalisa"
c= a + "  "+"******"+"  " + b
print(c) # Hello  ******  Monalisa

# 7. strings can be repeated - can be repeated using * operator
d= "Hello "*5   
print(d) # Hello Hello Hello Hello Hello

# 8. strings can be sliced - can be accessed using slicing operator
e= "Hello Monalisa"
print(e[0:5]) # Hello
print(e[:5])  # Hello
print(e[6:])  # Monalisa
print(e[-7:]) # Monalisa
print(e[-7:-1]) # Monali
print(e[:])   # Hello Monalisa 

# 9. strings have many built-in methods - can be used to perform various operations on strings
f= "   Hello Monalisa   "
print(f.lower()) # hello monalisa
print(f.upper()) # HELLO MONALISA
print(f.strip()) # Hello Monalisa
print(f.replace("Monalisa","Jhon")) #    Hello Jhon   
print(f.split(" ")) # ['', '', '', 'Hello', 'Monalisa', '', '', '']
print(f.find("Monalisa")) # 8
print(f.startswith("   Hello")) # True
print(f.endswith("Monalisa   ")) # True
print(f.isalpha()) # False (because of spaces)
print(f.isdigit()) # False
print(f.isspace()) # False
print(f.capitalize()) #    hello monalisa
print(f.title()) #    Hello Monalisa
print(f.count("l")) # 4
print(f.index("Monalisa")) # 8
print(f.swapcase()) #    hELLO mONALISA