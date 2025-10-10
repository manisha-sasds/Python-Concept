# Lists in Python- From Basics to Advanced Operations
#A list in Python is an ordered, mutable collection used to store multiple items in a single variable.# You can create a list by placing comma-separated values inside square brackets [].
print ("\n----------------- 1. Creating a  list -----------------")

# Integers
int_list = [1, 2, 3, 4, 5]
print("\n Created List of integers :=" , int_list)
# Creating a list of strings
str_list = ["apple", "banana", "cherry","date","fig","grape"]
print("\n Created List of strings:=", str_list)
# Creating a mixed list
mixed_list = [1, "hello", 3.14, True]
print("\n Created Mixed list with integers, strings, Boolean, float:=", mixed_list)
# Creating a nested list
nested_list = [1, 2, [3, 4], [5, 6]]
print("\n Nested list:=" , nested_list)
nested_mix_list=[[54,87,99],['Banaga','Mango','Orange'],[23.4,67.8,90.1],['age', 25,'height', 5.7  ]]
print("\n Nested mixed list with integers, strings, float is :=", nested_mix_list)
# Create a is using list() constructor
list_from_tuple = list((1, 2, 3))  # from tuple
print("\n Created List from tuple:=", list_from_tuple)
list_from_string = list("hello")  # from string
print("\n Created List from string:=", list_from_string)            

print ("\n----------------- 2. How to access List Elements by Indexing and Slicing -----------------")

# You can access individual elements in a list using their index. Note that Python uses zero-based indexing, meaning the first element is at index 0.
print("\n\t First element:", int_list[0])  # Output: 1
print("\n\t Second element:", str_list[1])  # Output: banana
print("\n\t Third element from end :", mixed_list[-3])  # Output: hello      
print("\n\t First element of nested list:", nested_list[2][0])  # Output: 3  
print("\n\t Second element of nested mixed list:", nested_mix_list[1][1])  # Output: Mango
print("\n\t Fourth element of nested mixed list:", nested_mix_list[3][3])  # Output: 5.7
print("\n\t First element of first list in nested mixed list:", nested_mix_list[0][0])  # Output: 54
print("\n\t Third element of third list in nested mixed list:", nested_mix_list[2][2])  # Output: 90.1

print ("\n----------------- 3. Slicing lists -----------------")
# You can extract a portion of a list using slicing. The syntax is list[start:end],
print("\n\t first three elements:", int_list[0:3])
print("\n\t from second element to end:", str_list[1:])
print("\n\t last two elements:", mixed_list[-2:])
print("\n\t first two elements:", nested_list[0:2])
print("\n\t first three lists:", nested_mix_list[0:3])
print("\n\t last two lists:", nested_mix_list[-2:])

print ("\n----------------- 4. Python - Add Items to a list using methods like append(), insert(), and extend() -----------------")
print("\t   -----------------Add one items at the end of a list using methods like append()-----------------")

int_list.append(66)
print("\n\t After append:", int_list) # only one item can be added
str_list.append("watermelon")
print("\n\t After append:", str_list)
mixed_list.append("welcome")
print("\n\t After append:", mixed_list)
nested_list.append([77, 88])
print("\n\t After append:", nested_list)
nested_mix_list.append(['weight', 60, 'city', 'Coventry'])
print("\n\t After append:", nested_mix_list)     


print("\n\t   -----------------Add new  one item at specific index in the list using insert() method-----------------")

int_list.insert(4, 0)  # Insert 0 at index 4
print("\n\t After insert at index 4:", int_list)
str_list.insert(2, "blueberry")  # Insert "blueberry" at index 2
print("\n\t After insert at index 2:", str_list)
mixed_list.insert(1, 2.71)  # Insert 2.71 at index 1
print("\n\t After insert at index 1:", mixed_list)
nested_list.insert(1, [111.5, 222.5])  # Insert [1.111, 222.5] at index 1
print("\n\t After insert at index 1:", nested_list)
nested_mix_list.insert(2, ['country', 'UK'])  # Insert ['country', 'UK'] at index 2
print("\n\t After insert at index 2:", nested_mix_list) 


print("\n\t   -----------------Add multiple items at the end of a list using extend() method-----------------")

int_list.extend([7, 8, 9])
print("\n\t  int lis extend:", int_list)  # multiple items can be added
str_list.extend(["elderberry", "fig", "pineapple"])
print("\n\t str list extend:", str_list)
mixed_list.extend([3.14, "world", True])
print("\n\t  mixed list extend:", mixed_list)
nested_list.extend([[9, 10], [11, 12]])
print("\n\t  nested list extend:", nested_list)
nested_mix_list.extend([['hobby', 'reading'], [100, 200, 300]])
print("\n\t nested mix list extend:", nested_mix_list) 


print ("\n----------------- 5. Python - Remove Items from a list using methods like remove(), pop(), and clear(). -----------------")
print("\t   -----------------Remove items from a list using methods like remove()-----------------")

list_one= ['BMW','Audi','Benz','Tata','Ford','Benz','Honda','Hyundai']
list_one.remove('Benz')  # Remove first occurrence of "Benz"
print("\n\t  After remove 'Benz':", list_one)
mixed_list.remove(3.14)  # Remove first occurrence of 3.14
print("\n\t  After remove True:", mixed_list)


print("\t   -----------------Remove items from a list using methods like pop()-----------------")

second_item = str_list.pop(1)  # Remove and return item at index 1              
print("\n\t After pop index 1:", str_list, "; Popped item:", second_item)
third_item = mixed_list.pop(2)  # Remove and return item at index 2
print("\n\t After pop index 2:", mixed_list, "; Popped item:", third_item)
first_nested = nested_list.pop(0)  # Remove and return item at index 0
print("\n\t After pop index 0:", nested_list, "; Popped item:", first_nested)
second_nested = nested_mix_list.pop(1)  # Remove and return item at index
print("\n\t After pop index 1:", nested_mix_list, "; Popped item:", second_nested)


print("\t   -----------------Remove all items from a list using clear() method-----------------")

temp_list = int_list.copy()  # Create a copy to demonstrate clear
temp_list.clear()
print("\n\t empty the list After clear:", temp_list)  # Output: []


print ("\n----------------- 6. Python - Other Useful List Methods and Functions. -----------------")
print("\t   -----------------find Length of a list-----------------")
# Length of a list
print("\n\t Length of str_list:", len(str_list))
print("\n\t Length of nested_mix_list:", len(nested_mix_list))    

print("\n\t   -----------------Count occurrences of an item in the list-----------------")
print("\n\t Count of 3 in int_list:", int_list.count(3))
print(mixed_list)
mixed_list.append(2.17) 
mixed_list.append(2.17) 
mixed_list.append(2.17) 
mixed_list.append('world')
print(mixed_list)
print("\n\t Count of 2.17 in mixed_list:", mixed_list.count(2.17))
      

print("\n\t   -----------------Find index of an item-----------------")
print ("\n\t int_list  := ", int_list)
print("\n\tIndex of number 4 in int_list:", int_list.index(4))
print("\n\t str_list:=" , str_list)
print("\n\tIndex of 'cherry' in str_list:", str_list.index("cherry"))      


print("\n\t   -----------------Sort a list (only works if all items are comparable)-----------------")

int_list.sort()
print("\n\t Sorted int_list:", int_list)
str_list.sort()
print("\n\t Sorted str_list:", str_list)         

print("\n\t   ----------------- Reverse a list-----------------")

int_list.reverse()
print("\n\t Reversed int_list:", int_list)
str_list.reverse()
print("\n\tReversed str_list:", str_list)

print("\n\t   ----------------- Copy a list-----------------")

copied_list = mixed_list.copy()
print("Copied mixed_list:", copied_list)        


print("\n\t   ----------------- Join two lists-----------------")

joined_list = int_list + [10, 11, 12]
print("\n\t Joined list:", joined_list)
joined_str_list = str_list + ["honeydew", "kiwi"]
print("\n\t Joined str_list:", joined_str_list)


print("\n\t   ----------------- Repeat a list-----------------")          

repeated_list = mixed_list * 2
print("\n\t Repeated mixed_list:", repeated_list)

print("\n\t   ----------------- Check if an item exists in a list -----------------")

print("\n\t Is 3 in int_list?", 3 in int_list)
print("\n\t Is 'banana' in str_list?", "banana" in str_list)


print("\n\t   -----------------List comprehension -----------------")

squared_list = [x**2 for x in int_list]
print(" \n\t Squared int_list using list comprehension:", squared_list)


uppercase_str_list = [s.upper() for s in str_list]
print("\n\t Uppercase str_list using list comprehension:", uppercase_str_list)

bool_list = [not b for b in mixed_list if isinstance(b, bool)]
print("\n\t Negated boolean values in mixed_list using list comprehension:", bool_list)

