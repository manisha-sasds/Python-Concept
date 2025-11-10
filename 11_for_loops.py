# Python for Loop — From Basics to Advanced
# In Python, a for loop is used to repeat actions over a sequence like a list, string, or range, so we don’t have to write the same code multiple times.
print ("\n----------------- 1. Simple for loop for numbers-----------------")
for i in 1,2,3,4,5 :
    print(i)
# for loop on List 
tasks_list =["Wash Dishes","Clean House","Cook Food"]
for tasks in tasks_list:
    print(" List of tasks=",tasks)
# for loop on String 
print
str ="WashDishes"
for x in str:
    print(" Each character of the str =",x)

# For loop on numeric range
print
for i in range(1, 6):  # 1,2,3,4,5
    print(i)
print("\n")
# range(start from = 5, stop at = 100, step moves by=10)
for i in range(5, 100,10):  # 5,15,25...85,95
    print(i)

print ("\n----------------- 2. For loop control-----------------")
print ("\n----------------- 2.1 For loop with else-----------------")
# a for loop can have an else block, which runs only if the loop finishes normally (no break).

# Create a dictionary
student = {
    "name": "Jhon",
    "age": 35,
    "grade": "A",
    "City" : "Coventry",
    "country": "UK"
}
for keys, values in student.items():
    print(f"{keys}: {values}")
else:
    print("Student information is available here")
print ("\n----------------- 2.2 For loop with break - Exit the loop-----------------")
print("\n----------------- 2.2 For loop with break - Exit the loop -----------------")

for key in student.keys():
    if key == "grade":
        print(f"{key}: (loop will stop here)")
        break
    print(f"{key}: {student[key]}")
else:
    print("Student information is available here")

print ("\n 2.3 For loop with continue - Skip current iterationlse---")
print("\n----------------- 2.3 For loop with continue - Exit the loop -----------------")
# continue skipsed the current iteration and moved to the next key.
for key in student.keys():
    if key == "grade":
        print(f"{key}: (loop will continue from here)")
        continue
    print(f"{key}: {student[key]}")
else:
    print("Student information is available here")

print ("\n----------------- 3. Nested For Loops -----------------")
print ("\n----------------- 3.1 For Loop inside a for loop-----------------")

for i in range(1,6):
    for x in range(7,11):
       print(f"({i},{x})") 

# Simple pyramid problem 
row=5
for x in range (1,row+1):
    print("*"*x)    
print("\n\n")

# Floyd’s Triangle 
rows=5
number=1
for i in range (1,rows+1):
    for j in range(1,i+1):
        print(number,end=' ')
        number+=1
    print()
print("\n\n")
# Reverse Triangle
n=5
for i in range(n,0,-1):
    for j in range (i,0,-1):
      print(j,end=' ')
    print()

print ("\n----------------- 4. Enumerate() and Zip() -----------------")
print ("\n----------------- 4.1 Enumerate()- when we want index and value. -----------------")
# Using enumerate() to get index and value from a list
colors = ["pink", "green", "blue", "yellow"]
for ind, col in enumerate(colors):
    print(f"Index: {ind}, Color: {col}")  
print ("\n")
# Using enumerate() with a starting index
for ind, col in enumerate(colors, start=11):
    print(f"Index: {ind}, Color: {col}")
print ("\n")

# Using enumerate() to get index and value from a string
word = "Python"
for ind, char in enumerate(word):
    print(f"Index: {ind}, Character: {char}")  
print ("\n")
# Using enumerate() with a starting index
for ind, char in enumerate(word, start=101):
    print(f"Index: {ind}, Character: {char}")
print ("\n")

person = {"name": "Bob", "age": 25, "city": "Coventry"}
# Using enumerate() with a starting index
for ind, (key, value) in enumerate(person.items(), start=51):
    print(f"Index: {ind}, Key: {key}, Value: {value}")  

# Using enumerate() outside the for loop
enum_obj=enumerate(["Audi", "BMW", "Ford", "Honda" ])
print(list(enum_obj))

print ("\n----------------- 4.2 zip()- when we want multiple lists together. -----------------")

# Using zip() to combine two lists
features = ["Age", "Salary", "Score"]
means = [29.5, 55000, 82.1]
for col, mean in zip(features, means):
    print(f"Average {col}: {mean}")

print ("\n")
# Using zip() to combine three lists
employee = ["Monika", "Ravi", "Sophia"]
departments = ["HR", "IT", "Finance"]
salaries = [60000, 75000, 80000]
for emp, dept, sal in zip(employee, departments, salaries):
    print(f"Employee name is: {emp},who works in Department: {dept}, Salary is : {sal}")

all_col=list(zip(employee, departments, salaries))

import pandas as pd 
data=pd.DataFrame(all_col,columns=["Employee","Department","Salary"])
print(data)

# Using zip() with uneven length lists
from itertools import zip_longest

names = ["Mike", "Jhon", "Sony"]
ages = [25, 30]

for name, age in zip_longest(names, ages, fillvalue=0):
    print(f"{name}: {age}")

# print ("\n----------------- 5. List, Dict, and Set Comprehensions -----------------")
# A comprehension is a shorter, faster, and cleaner way to create a list or a dict or set in Python — all in one line.
print ("\n----------------- 5.1 List Comprehensions -----------------")
# Creating a list of squares using a for loop
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print("Squares using for loop:", squares)   
# Creating a list of squares using list comprehension
squares_comp = [i ** 2 for i in range(1, 11)]
print("Squares using list comprehension:", squares_comp)

import time
# Traditional loop (slower)
start = time.time()
result = []
for i in range(1000000):
    result.append(i**2)
print(f"Loop: {time.time() - start:.4f}s")

# List comprehension (faster)
start = time.time()
result = [i**2 for i in range(1000000)]
print(f"Comprehension: {time.time() - start:.4f}s")

print ("\n----------------- 5.2 Dictionary Comprehensions -----------------")

# Creating a dictionary of squares using a for loop
squares_dict = {}
for i in range(1, 6):
    squares_dict[i] = i ** 2
print("Squares dict using for loop:", squares_dict)   
# Creating a dictionary of squares using dict comprehension
squares_dict_comp = {i: i ** 2 for i in range(1, 6)}
print("Squares dict using dict comprehension:", squares_dict_comp)

