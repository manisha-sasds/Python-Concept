# Tuples in Python- From Basics to Advanced Operations
#A tuple in Python is an ordered, immutable, meaning once created, their elements cannot be changed, added, or removed. it is used to store multiple items in a single variable.# You can create a tuple by placing comma-separated values inside square brackets ().
# Tuples are faster than lists and are often used to store data that should not be modified.
# Tuples are hashable, which means they can be used as keys in dictionaries and elements in sets, unlike lists.

print ("\n----------------- 1.Firts way to Creating a  tuple -----------------")

# Integers
int_tuple = (1, 2, 3, 4, 5,88,99)
print("\n Created Tuple of integers :=" , int_tuple)


# Creating a tuple of strings
str_tuple = ("apple", "banana", "wattermelon","fig","grape")
print("\n Created Tuple of strings:=", str_tuple) # only one item can be added


# Creating a mixed tuple
mixed_tuple = (1, "John", 389.14, True,"Banana")
print("\n Created Mixed tuple with integers, strings, Boolean, float:=", mixed_tuple)

# Creating a nested tuple
nested_tuple = (1, 2, [3, 4], [5, 6])
print("\n Nested tuple:=" , nested_tuple)
nested_mix_tuple=([54,87,99],['Banaga','Mango','Orange'],[23.4,67.8,90.1],['age', 25,'height', 5.7  ])
print("\n Nested mixed tuple with integers, strings, float is :=", nested_mix_tuple)


# Create a is using tuple() constructor
print ("\n----------------- 2.Second way to Creating a  tuple in python tuple() constructor function -----------------")

# Python: Demonstration of list() vs tuple() for various scenarios

scenarios = {
    "String 'Hello'": "Hello",
    "List ['Hello']": ["Hello"],
    "List ['Hello','World']": ["Hello","World"],
    "Tuple ('Hello','World')": ("Hello","World"),
    "List ['a','b','c']": ["a","b","c"],
    "String 'abc'": "abc",
    "List [1,2,3]": [1,2,3],
    "Tuple (1,2,3)": (1,2,3),
    "Nested List [[1,2],[3,4]]": [[1,2],[3,4]],
    "String 'Python123'": "Python123",
    "Deeply Nested List [[['nested']]]": [[["nested"]]],
    "String ' ' (space)": " ",
    "Empty List []": [],
    "Empty Tuple ()": (),
    "Single Character String 'A'": "A"
}

print("=== list() vs tuple() some Examples ===\n")

for desc, value in scenarios.items():
    print(f"Scenario: {desc}")
    try:
        list_result = list(value)
        tuple_result = tuple(value)
        print(f"  list({value})  = {list_result}")
        print(f"  tuple({value}) = {tuple_result}")
    except Exception as e:
        print(f"  Error: {e}")
    print("-"*50)
          

print ("\n----------------- 2. How to access Tuple Elements by Indexing and Slicing -----------------")

# You can access individual elements in a tuple using their index. Note that Python uses zero-based indexing, meaning the first element is at index 0.
print("\n\t First element:", int_tuple[0])  # Output: 1
print("\n\t Second element:", str_tuple[1])  # Output: banana
print("\n\t After append:", mixed_tuple)
print("\n\t Third element from end :", mixed_tuple[-3])  # Output:  389.14     
print("\n\t First element of nested tuple:", nested_tuple[2][0])  # Output: 3  
print("\nnested_mix_tuple=",nested_mix_tuple)
print("\n\t Second element of nested mixed tuple:", nested_mix_tuple[1][1])  # Output: Mango
print("\n\t Fourth element of nested mixed tuple:", nested_mix_tuple[3][3])  # Output: 5.7
print("\n\t First element of first tuple in nested mixed tuple:", nested_mix_tuple[0][0])  # Output: 54
print("\n\t Third element of third tuple in nested mixed tuple:", nested_mix_tuple[2][2])  # Output: 90.1

print ("\n----------------- 3. Slicing tuples -----------------")
# You can extract a portion of a tuple using slicing. The syntax is tuple[start:end],
print("\n\t first three elements:", int_tuple[0:3])
print("\n\t from second element to end:", str_tuple[1:])
print("\n\t last two elements:", mixed_tuple[-2:])
print("\n\t first two elements:", nested_tuple[0:2])
print("\n\t first three tuples:", nested_mix_tuple[0:3])
print("\n\t last two tuples:", nested_mix_tuple[-2:])

print ("\n----------------- 4. Python - Add Items to a tuple is not possible because tuples are immutable but we can do this with diffrent method by converting into list and then  using methods like append(), insert(), and extend() -----------------")
print("\t   -----------------Add one items at the end of a tuple using methods like append()-----------------")

# if you try to use append() directly on a tuple, it will raise an AttributeError because tuples do not have an append() method.
#int_tuple.append(66)

# First convert tuple to list
int_list_tup = list(int_tuple)
int_list_tup.append(66)
# Convert back to tuple
int_tuple = tuple(int_list_tup)
print("\n\t After append:", int_tuple)

# first convert nested_mix_tuple to list 
mixed_list_tup = list(nested_mix_tuple)
mixed_list_tup.append(['weight', 60, 'city', 'Coventry'])
# Convert back to tuple
nested_mix_tuple = tuple(mixed_list_tup)
print("\n\t After append:", nested_mix_tuple)

print("\n\t   -----------------Add new  one item at specific index in the tuple using insert() method-----------------")

# str_tuple.insert(2, "blueberry")  # Insert "blueberry" at index 2
# print("\n\t After insert at index 2:", str_tuple) # error - 'tuple' object has no attribute 'insert'
# First convert tuple to list
temp = list(str_tuple)
temp.insert(2, "blueberry") # Insert "blueberry" at index 2
# Convert back to tuple
str_tuple = tuple(temp)
print("\tAfter insert (str_tuple):", str_tuple) 

temp = list(mixed_tuple)
temp.insert(1, 2.71)
mixed_tuple = tuple(temp)
print("\tAfter insert (mixed_tuple):", mixed_tuple)


print("\n\t   -----------------Add multiple items at the end of a tuple using extend() method-----------------")

# if you try to use extend() directly on a tuple, it will raise an AttributeError because tuples do not have an extend() method.
#nested_mix_tuple.extend([['hobby', 'reading'], [100, 200, 300]])

temp = list(nested_mix_tuple)
temp.extend([['hobby', 'reading'], [100, 200, 300]])
nested_mix_tuple = tuple(temp)
print("\tAfter extend (nested_mix_tuple):", nested_mix_tuple)

print ("\n----------------- 5. Python - Remove Items from a tuple using methods like remove(), pop(), and clear(). -----------------")
print("\t   -----------------Remove items from a tuple using methods like remove()-----------------")

tuple_one= ['BMW','Audi','Benz','Tata','Ford','Benz','Honda','Hyundai']
# if you try to use remove() directly on a tuple, it will raise an AttributeError because tuples do not have an remove() method.
# tuple_one.remove('Benz')  # Remove first occurrence of "Benz"
temp = list(tuple_one)
temp.remove("Benz")  # removes first occurrence
tuple_one = tuple(temp)
print("\tAfter remove 'Benz':", tuple_one)


print("\t   -----------------delete a tuple using del -----------------")

temp_tuple = tuple_one  # Create a copy to demonstrate clear
del tuple_one
#print(temp_tuple) #this will raise an error because the tuple no longer exists


print ("\n----------------- 6. Tuple - Unpacking -----------------")
print("\t   -----------------6.1 Unpacking the tuple into separate variables-----------------")
# Tuple unpacking allows you to assign the elements of a tuple to multiple variables in a single statement.
# The number of variables on the left side must match the number of elements in the tuple.  
employee = ("John", 30, "Engineer","Coventry")
name, age, profession,city = employee
print("\n\t Name:", name)
print("\n\t Age:", age)
print("\n\t Profession:", profession)
print("\n\t City:", city)

print ("\n----------------- 6. Tuple - Unpacking -----------------")
print("\t   -----------------6.1 Unpacking the tuple into separate variables-----------------")
# Tuple unpacking allows you to assign the elements of a tuple to multiple variables in a single statement.
# The number of variables on the left side must match the number of elements in the tuple.  
employee = ("John", 30, "Engineer","Coventry")
name, age, profession,city = employee
print("\n\t Name:", name)
print("\n\t Age:", age)
print("\n\t Profession:", profession)
print("\n\t City:", city)

print("\t   -----------------6.2 Unpacking with * operator-----------------")
# You can use the * operator to unpack remaining elements into a list.
employee = ("John", 30, "Single","Engineer",50000,"Coventry")
first, second, *rest = employee
print("\n\t First:", first)
print("\n\t Second:", second)
print("\n\t Rest:", rest)  # rest will be a list containing the remaining elements

name, *info, city = employee
print("\n\t Name:", name)
print("\n\t Info:", info)  # info will be a list containing the middle elements
print("\n\t City:", city)

# You can also ignore certain values during unpacking by using a placeholder variable, often an underscore (_).
print("\t   -----------------6.3 Unpacking and ignoring certain values-----------------")

_, *info, _ = employee
print("\n\t Info:", info)  # info will be a list containing the middle elements

print ("\n----------------- 7. Tuple - Loop -for, While . -----------------")
print("\t   -----------------7.1 Looping through a tuple using for loop-----------------")

mixed_tuple = (1, "John", 389.14, True,"Banana")
for item in mixed_tuple:
    print("\n\t Item:", item)
print("\t   -----------------7.2 Looping through a tuple using while loop-----------------")    
index = 0
while index < len(mixed_tuple):
    print("\n\t Item at index", index, ":", mixed_tuple[index])
    index +=  1


print ("\n----------------- . Tuple - Join -----------------")

int_tuple
print("\t   -----------------Join two tuples-----------------")
joined_tuple = int_tuple + (10, 11, 12)
print("\n\t Joined tuple:", joined_tuple)
joined_str_tuple = str_tuple + ("honeydew", "kiwi")
print("\n\t Joined str_tuple:", joined_str_tuple)
joined_int_str_tuple =int_tuple+str_tuple   
print("\n\t Joined int_tuple and str_tuple:", joined_int_str_tuple)
print("\t   -----------------Muiltiply a tuple-----------------")
muiltiplyed_tuple = mixed_tuple * 2
print("\n\t Muiltiplyed mixed_tuple:", muiltiplyed_tuple)

print ("\n----------------- . Tuple - Other Useful Tuple Methods  -----------------")

# count and index methods
tuple_num=(11,22,33,44,55,66,77,88,99,11,22,33,33,44,33,66,33,77)
count_33=tuple_num.count(33)
print("\n\t Count of 33 in tuple_num:", count_33)

index_77=tuple_num.index(77)
print("\n\t Index of 77 in tuple_num is:", index_77)



