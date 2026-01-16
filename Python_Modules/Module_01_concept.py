# Module means Python File which contains Functions,Classes,Vraiables,Constant, and Executable code.
# Module  can be reused in any other python file using import statement.
'''print ("\n----------------- 1. Types of Module in Python ---------------")
# Three Types of Modules 1. Built-in Modules, 2. Third-Party Modules, 3. User-Defined Modules.
print ("\n----------------- 1.1 User-Defined Modules (anyone can create their own Module) ---------------")
# To create a good Python module, follow this sequence: first write constants and variables, then functions, then classes, and finally executable code (optional).

'''
# Step 1: Create a Python file with module_02.py extension - which is our user-defined first module below same code is available in module_02.py and see the main.py file from wherre all othe code is execited. 
# ===== VARIABLES =====
x = 10
y = 5
str1 = "Simple module example" 

# ===== FUNCTIONS =====
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def is_even(n):
    return n % 2 == 0

# ===== CLASSES =====
class Person:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        return f"My name is {self.name}"


class Counter:
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1
        return self.count


# ===== RUN ONLY WHEN DIRECT YOU WANT TO CHECK THE CODE =====
if __name__ == "__main__":
    print("Running simple_module directly")
    print("add(2, 3):", add(2, 3))
    print("multiply(2, 3):", multiply(2, 3))
    print("is_even(4):", is_even(4))

print ("\n----------------- 1.2  Import Types  ---------------")
# Saved and Executed below code in main.py file

print ("\n----------------- 1.2.1  Import Entire Module  ---------------")

# Module can be imported suing five methods Method 1: Import Entire Module, Method 2: Import with Alias, Method 3: Import Specific Items,Method 4: Import with Custom , Method 5: Import All (NOT RECOMMENDED!)
# We can Import Entire Module so that we can access all Functions,Classes,Vraiables,Constant, and Executable code. 
# if we are importing module we need to write the import name before accessing Functions,Classes,Vraiables,Constant,

# Saved and Executed below code in main.py file

import module_02 # 1. Import Entire Module
print ("\n----------------- 1.2.1  Import Entire Module  ---------------")
# module_02.py variables can be accessed from another file using the module name.

print(module_02.x)
print(module_02.str1)

print(module_02.add(4, 5))
print(module_02.multiply(3, 4))
print(module_02.is_even(7))

obj1 = module_02.Person("John Bonita")
print(obj1.say_name())

count_obj = module_02.Counter()
print(count_obj.increase())

print ("\n----------------- 1.2.2  Import with Alias  ---------------")
import module_02 as mod # 2. Import with Alias mod is alias name for module_02

print(mod.x)
print(mod.str1) 
print(mod.add(10, 20))
print(mod.multiply(6, 7))
print(mod.is_even(10))
person_obj = mod.Person("Alice")
print(person_obj.say_name())
counter_obj = mod.Counter()
print(counter_obj.increase())

print("\n----------------- 1.2.3 Import Specific Items like Functions, Classes ,Vraiables  ---------------")

from module_02 import str1, add, Person # 3. Import Specific Items only  

print(str1)
print(add(15, 25))
person_obj1 = Person("Bob")
print(person_obj1.say_name())   

print("\n----------------- 1.2.4 Import Specific Items like Functions, Classes ,Vraiables with Custom Alias  ---------------")

from module_02 import str1 as st, multiply as mul, is_even as check_even, Counter as cnt # 4. Import with Custom Alias
print(st)
print(mul(20, 90))
print(check_even(144))
counter_obj1 = cnt()
print(counter_obj1.increase())  

print("\n----------------- 1.2.5 Import All (NOT RECOMMENDED!)  ---------------")
from module_02 import *  # 5. Import All (NOT RECOMMENDED!)
print(x)
print(str1)
print(add(5, 10))
print(multiply(7, 8))
print(is_even(22))
person_obj2 = Person("Charlie")
print(person_obj2.say_name())
counter_obj2 = Counter()
print(counter_obj2.increase())

print ("\n----------------- 1.2 Built-in Modules in Python ---------------")
# Built-in Modules are already installed with Python software so no installation needed.Examples: math, os, sys, datetime, random

import math          # Mathematical functions
import os            # Operating system
import sys           # System parameters
import datetime      # Dates and times
import random        # Random numbers
import itertools     # Iteration tools
from pathlib import Path    # File paths

# Math: calculate Euclidean distance
x1, y1 = 34, 489
x2, y2 = 12, 25
distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print("Distance:", distance)


# Random: shuffle dataset
dataset = [61,562,367,46,5]
random.shuffle(dataset)
print("Shuffled dataset:", dataset)

# Datetime: timestamp for logging
print("Current time:", datetime.datetime.now())

# Itertools: generate all pairs
items = ["A","B","C"]
pairs = list(itertools.combinations(items, 2))
print("Pairs:", pairs)


print ("\n----------------- 1.3  Third-Party Modules (Install via pip) in Python ---------------")
# Third-Party Modules are created by the Python community. It needs to install using pip install package_name.Examples: numpy, pandas, requests, matplotlib
# First Installing a Third-Party Module using pip numpy
# !pip3 install numpy
import numpy as np  # Numerical computing
# Create a numpy array and perform operations
arr = np.array([1, 2, 3, 4, 5])
print("Numpy array:", arr)
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Sum:", np.sum(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))
print("Sorted:", np.sort(arr))
print("Reshaped:\n", arr.reshape(5, 1))
# First Installing a Third-Party Module using pip pandas
# !pip3 install pandas
import pandas as pd  # Data manipulation
# Create a pandas DataFrame and perform operations
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print("Pandas DataFrame:\n", df)
print("Describe:\n", df.describe())
print("Sort by Age:\n", df.sort_values(by='Age'))
print("Filter Age > 28:\n", df[df['Age'] > 28])
print("Add Column:\n", df.assign(Salary=[50000, 60000, 70000]))
print("Group by Age:\n", df.groupby('Age').size())
