# Python whifunction  — From Basics to Advanced
# The purpose of Functions is to Perform Certain Operation or Task and Provides Code Re-Usability.
# Anything followed by () means "CALL this":
print ("\n----------------- 1. Basic function definitions -----------------")
# def function_name(parameters):
     # code block
 #      return result

# Simple function that prints a message
def fisrt_function():
    print("This is my first function.")

fisrt_function() # called funation here 
print("\n\n")

print ("\n----------------- 2. function Parameters and argumnets -----------------")

def add(a, b):     # a, b → parameters
    return a + b

result = add(5, 3) # 5, 3 → arguments
print(result)
print("\n\n")

print ("\n----------------- 2.1 same number of  Parameters and argumnets -----------------")
# Function with same three number of parameters and arguments
def employee_info(name, age, department):
    print(f"Name: {name}, Age: {age}, Department: {department}")    
employee_info("Meena", 30, "HR")  # Correct number of arguments
print("\n\n")

print ("\n----------------- 2.2 Default Parameters Value -----------------")

def employee_info(name, age, department="General"):  # department has a default value
    print(f"Name: {name}, Age: {age}, Department: {department}")    

employee_info("Meena", 30, "HR")  # 'HR' overrides default value 
employee_info("Ravi", 28)  # here function is called without an argument so department uses default valu

print ("\n----------------- 2.3 Keyword Arguments -----------------")
# In keyword arguments, the names must match the parameter names exactly (same spelling, same case)
def employee_info(name, age, department):
    print(f"Name: {name}, Age: {age}, Department: {department}")
employee_info(age=25, name="Sophia", department="IT")  # Using keyword arguments
employee_info(department="Finance", name="John", age=32)  # Different order
print("\n\n")

print ("\n----------------- 2.4 Positional Arguments -----------------")

def student_info(name,age, grade, city):
    print(f"Name: {name}, Age: {age}, Grade: {grade}, City: {city}")

# When we pass values to a function without naming them, Python matches them by their position Using positional arguments (order matters)
student_info("Aarav", 23,"A", "Delhi")
# student_info("Meena", "B+", "Mumbai") # Missing age argument will raise an errorß

print("\n\n")

print ("\n----------------- 2.5 Mixing Positional and Keyword Arguments ---------------")

def book_info(title, author, year, genre):
    print(f"Title: {title}, Author: {author}, Year: {year}, Genre: {genre}")
# Mixing positional and keyword arguments
book_info("1984", author="George Orwell", year=1949, genre="Dystopian")
book_info("To Kill a Mockingbird", "Harper Lee", genre="Fiction", year=1960)
book_info(author="J.K. Rowling", title="Harry Potter and the Sorcerer's Stone", genre="Fantasy",year=1997)
print("\n\n")   

print ("\n----------------- 2.6 Positional-Only Arguments ---------------")
# In Python, we can define positional-only parameters using the '/' symbol in the function definition.
# Any parameter before the '/' must be provided as a positional argument and cannot be passed as a keyword argument.

def add(a, b, /):
    print(a + b)

add(672, 873)  # Valid call
# add(a=2, b=3) #  TypeError

print ("\n----------------- 2.7 Keyword-Only Arguments ---------------")
# we used a * (star) before department paramter that means this function does not allow positional arguments — only keyword arguments are allowed.
def my_function(*, department, location):
    print("My", department, "department is located in", location)
my_function(department="IT", location="New York")  # Valid call
# my_function("IT", "New York")  # TypeError        

print ("\n----------------- 2.8 Combining Positional-Only and Keyword-Only---------------")
# we can combine both positional-only and keyword-only parameters in a single function definition.
# In this example, 'a' and 'b' are positional-only parameters, while 'department' and 'location' are keyword-only parameters.
def employee_details(a, b, /, *, department, location):
    print(f"a: {a}, b: {b}, department: {department}, location: {location}")    
employee_details(1, 2, department="HR", location="London")  # Valid call
employee_details(1, 2, location="London",department="HR")  # Valid call

# employee_details(a=11, b=22, department="HR", location="London")  # TypeError
# employee_details(11, 22, "HR", "London")  # TypeError
print("\n\n")   

print ("\n----------------- 2.9  Passing Different Data Types ---------------")
# Functions can accept different data types as arguments, including integers, floats, strings, lists, dictionaries, and more.
def display_info(num, text, lst, dct):
    print(f"Number: {num} (Data Type: {type(num)})")
    print(f"Text: {text} (Data Type: {type(text)})")
    print(f"List: {lst} (Data Type: {type(lst)})")
    print(f"Dictionary: {dct} (DataType: {type(dct)})")
display_info(42, "Hello, World!", [1, 2, 3], {"key": "value", "age": 30})
print("\n\n")   

print ("\n----------------- 2.10 Returning Different Data Types-------------")
# Functions can return different data types based on the logic implemented within them.
def calculate_area(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area  # Returns a float value    
result = calculate_area(5)
print(f"Area of circle with radius 5: {result} (Type: {type(result)})")
print("\n\n")
print ("\n----------------- 2.11  Arbitrary Arguments - *args ---------------")

# •parameter name is preceded by an asterisk (*) which allows the function to accept any number of positional arguments.
# These arguments are collected into a tuple named 'names' inside the function.
def arb_funt(*names):
    for name in names:
        print("Welcome", name)
arb_funt("Monika", "Ravi", "Sophia", "John") # we can pass any number of arguments here

print ("\n----------------- 2.12  Arbitrary Arguments - *args  with Regular Arguments ---------------")
# Here, 'greeting' is a regular parameter, and '*names' allows for any number of additional positional arguments.
def arb_funt(greeting,compnay_name, *names):
    for name in names:
        print(f"{greeting} {compnay_name} company {name}!")
arb_funt("Welcome to", "IBM", "Monika", "Ravi", "Sophia") # we can pass any number of arguments here

print ("\n----------------- 2.13  Arbitrary Keyword Arguments - **kwargs ---------------")
# Here, '**info' allows the function to accept any number of keyword arguments.
# These arguments are collected into a dictionary named info inside the function.

def arb_keyword_funt(**info):
    for key, value in info.items():
        print(f"{key} of the employee is  : {value}")       
arb_keyword_funt(name="Monika", age=30, department="HR", location="New York")
print("\n")

print ("\n------ 2.14  Arbitrary Keyword Arguments - Using **kwargs with Regular Arguments -----")
# Here, 'product_name' is a regular parameter, and '**attributes' allows for any number of additional keyword arguments.
# this function has one regular parameter and another attribute parameter as dictionary of keyword arguments.
def add_product(product_name, **attributes):
    print(f"Product: {product_name}")
    for key, value in attributes.items():
        print(f"  {key}: {value}")

# Example usage
add_product(
    "Smartphone",
    brand="Samsung",
    color="Black",
    storage="128GB",
    warranty="1 year"
)

print ("\n----------------- 2.15  Combining *args and **kwargs ---------------")
# the sequnece of parameters is important: regular parameters, *args, then **kwargs.

def combine_all(arg1, arg2, *args, **kwargs):
    print(f"arg1: {arg1}")
    print(f"arg2: {arg2}")
    print("Additional positional arguments (args):")
    for arg in args:
        print(f"  {arg}")
    print("Keyword arguments (kwargs):")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")
combine_all("Hello", 42, "extra1", "extra2", name="Kajal", age=42)  

####### Report Generator #######
print ("\n----------------- Report Generator using *args and **kwargs ---------------")
# This function generates a report with a title, subtitle, multiple sections, and additional metadata.
def generate_report(title, subtitle, *sections, **metadata):
    print(f"Report: {title}")
    print(f"Subtitle: {subtitle}")
    
    for i, section in enumerate(sections, start=1):
        print(f"Section {i}: {section}")
    
    if metadata:
        print("Report Metadata:")
        for key, value in metadata.items():
            print(f"  {key}: {value}")

generate_report(
    "Monthly Sales",
    "Q4 2025",
    "Summary", "Charts", "Analysis",
    author="David",
    department="Sales",
    confidential=True
)

print ("\n----------------- 2.16  Unpacking Arguments ---------------")
# Unpacking means breaking down a collection (like a list, tuple, or dictionary) into individual elements to pass them as separate arguments to a function.
def display_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")
# Unpacking a list/tuple into positional arguments
person_info = ["Monika", 28, "New York"]
display_info(*person_info) 

# Unpacking a dictionary into keyword arguments
person_dict = {"name": "Ravi", "age": 32, "city": "London"}
display_info(**person_dict)
print("\n\n")

# Unpacking *args and **kwargs in a function call
def my_fun1(name, age, *address,**marks):
    print(f"Name: {name}, Age: {age}\n")
    print("Address Details:")
    for addr in address:
        print(f"  {addr}")
    print("\n")
    print("Marks Details:")
    for subject, mark in marks.items():
        print(f"  {subject}: {mark}")   
gen_arg_name = ["Sophia", 24]
gen_arg_address = ("123 Main St", "Apt 4B", "New York")
gen_arg_marks = {"math":95, "science":88, "english":92, "grade":"A"}

result= my_fun1(*gen_arg_name, *gen_arg_address, **gen_arg_marks)
print("\n\n")


print ("\n----------------- 3. Return -----------------")
# return statement sends a value from a function back to the caller.
# Once Python executes a return statement, the function stops immediately — any code after it won’t run.
def funct_ret(num1, num2):
    total = num1 + num2
    return "Jhon", total, {"nick":"Sara","age":25,"add":total},(22, "Hi", 3.14)

name, total_value, info_dict, data_tuple = funct_ret(23, 45)
# Print each one
print("Name:", name)
print("Total:", total_value)
print("Dictionary:", info_dict)
print("Tuple:", data_tuple)
print(info_dict["add"]) 
print(info_dict["age"])   # Access the "add" value inside the dictionary
print(data_tuple[1])  
print("\n\n")

print ("\n----------------- 4. Scope of function Local and Global -----------------")
# In python scope gives the visbility to the variables.
# there are two types of scope in python-local scope and global scope.
#Python follows the LEGB rule for variable scope resolution:
# L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.
# E: Enclosing function locals — Names in the local scopes of any and all enclosing functions (def or lambda), from inner to outer.
# G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.
# B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...

print ("\n----------------- 4.1 Local Scope-----------------")
#  Variables defined inside a function are in the local scope and can only be accessed within that function.

def myfunc():
    x = 300                 # Local int variable to myfunc
    print("outer function  :", x)

    def myinnerfunc():
        print("inner function", x)  # Can access x from outer function (enclosing scope)
        y = 5667                 # Local to myinnerfunc
        print("inner function", y)

    myinnerfunc()
    print("inner function", x)

myfunc()

print ("\n----------------- 4.2 Global Scope-----------------")
x = 300  # Global variable
def myfunc():
    x = 200  # Local to myfunc
    print("1- Here x is local varibale to myfunc() = ", x)

    def myinnerfunc():
        print("2- Here x is local varibale from def myfunc()=", x)  # Local x from myfunc

    myinnerfunc()

    def myinnerfunc1():
        x=4000               # Local to myinnerfunc1
        print("3- Here x is local varibale from myinnerfunc1()=", x)
    myinnerfunc1()
    def myinnerfunc2():
        # print("4- Here x is main global varibale  =", x) # error because x is assigned a value later in this function
        global x
        print("4- Here x is main global varibale  =", x)
        x = 500.6767
        print("5- Here x is global varibale which is modified new value from 300 to 500.6767 ", x)

    myinnerfunc2()

myfunc()
print("6- Here x is global varibale ", x)

print ("\n----------------- 4.3 nonlocal keywords -----------------")
# A nonlocal variable is a variable that exists in an enclosing (outer) function, but not in the global scope.



def myfunc():
    x = 111  # Local to myfunc
    print("1- Here x is local varibale to myfunc() = ", x)

    def myinnerfunc():
        print("2- Here x is local varibale from def myfunc()=", x)  # Local x from myfunc
    myinnerfunc()
    def myinnerfunc1():
        x=2222               # Local to myinnerfunc1
        print("3- Here x is local varibale from myinnerfunc1()=", x)
    myinnerfunc1()
    def myinnerfunc2():
        nonlocal x
        print("4- Here x is main local varibale  =", x)
        x = 33333
        print("5- Here x is nonlocal varibale which is modified new value from 111 to 33333", x)

    myinnerfunc2()
    print("6- Here x is a modified local varibale ", x)

myfunc()
print("\n\n")
# bank account management 

bank_name = "HDFC Bank"
service_charge = 5  # charged for every withdrawal

def account_manager():
    print(f"Welcome to {bank_name}!")
    balance = 1000  # starting balance (Local to outer account_manager function)
    
    def show_balance():
        # Access global + local variables
        print(f"Current balance: {balance}£ ")
        print(f"Bank: {bank_name}, Service charge: {service_charge} £ per withdrawal")

    def deposit(amount):
        # modifies ONLY outer variable → needs nonlocal
        nonlocal balance
        balance += amount
        print(f"Deposited {amount}. New balance = {balance}£ ")

    def withdraw(amount):
        # modifies outer variable AND uses global var
        nonlocal balance
        total_deduction = amount + service_charge
        if balance >= total_deduction:
            balance -= total_deduction
            print(f"Withdrew {amount} (charge {service_charge}). Balance = {balance}£")
        else:
            print("Insufficient funds!")

    # Simulate transactions
    show_balance()
    deposit(500)
    withdraw(300)
    show_balance()
account_manager() # Call outer function
print("\n\n")

print ("\n----------------- 5. Lambda Functions -----------------")
# A function without name is called an lambdat function.
#it is needed quickly for a short period and is not reused anywhere else in the code.so we wroite lambda functioon in a single line.
# They can take any number of arguments but can only have a single expression.This single expression is evaluated and returned the result when we call the lambda function anywhere in the code.
# Syntax: lambda arguments: expression

# Example 1: A simple lambda function that adds two numbers

add = lambda x, y: x + y # here add variable  behaves like the function because it points to the function value.
print(type(add))  # <class 'function'>
result = add(3,7) 
print("Addition using lambda:", result)

# Create a function to compute nth-power transformation
def power_trans(n):
    return lambda x: x ** n
square = power_trans(2)  # Create a lambda function for squaring
cube = power_trans(3)    # Create a lambda function for cubing      
print("Square of 11:", square(11))  # Output: 121
print("Cube of 4:", cube(4))      # Output: 64

# Do not use lambda for complex operations or multiple statements, use regular function.
# complex_lambda = lambda x: x ** 2 if x > 0 else -x ** 2 if x < 0 else 0
# lambda has some built-in functions like map(), filter(), reduce(), and sorted() that work well with lambda functions.
print ("\n----------------- 5.1 Lambda buitl in functions map() -----------------")

# The map() -It takes a list,tuple etc  of items, applies a rule or function(this can be normal function or lambda) to each item, and gives you a new list with the results.syntax- map(function, iterable)

numbers = [11, 22, 33, 44, 55]
tripled_num=map(lambda x:x*3,numbers)
print(type(tripled_num))  # <class 'map'>
tripled_num=list(tripled_num) # converting map object to list
print("Tripled numbers using map and lambda:", tripled_num) # [33, 66, 99, 132, 165]

print ("\n----------------- 5.2 Lambda buitl in functions filter() -----------------")
# The filter() - It takes a list,tuple etc of items, applies a rule or function(this can be normal function or lambda) to each item, and gives you a new list with only those items that meet the condition true or false.
# syntax- filter(function, iterable)

numbers = [10, 15, 22, 33, 40, 55, 60]
even_numbers=filter(lambda x:x%2==0,numbers)
print(type(even_numbers))  # <class 'filter'>
even_numbers=list(even_numbers) # converting filter object to list
print("Even numbers using filter and lambda:", even_numbers) # [10, 22, 40, 60]
# Filter numbers greater than a threshold 25
greater_than_25 = filter(lambda x: x > 25, numbers)
greater_than_25 = list(greater_than_25)
print("Numbers greater than 25 using filter and lambda:", greater_than_25)  # [33, 40, 55, 60]
print("\n")

print ("\n----------------- 5.3 Lambda buitl in functions sorted() -----------------")
# The sorted() - It takes a list,tuple etc of items, applies a rule or function(this can be normal function or lambda) to each item, and gives you a new sorted list.
# syntax- sorted(iterable, key=function, reverse=bool)          
products = [
    {"name": "Laptop", "price": 800},
    {"name": "Smartphone", "price": 600},
    {"name": "Tablet", "price": 400}
]   
sorted_products = sorted(products, key=lambda x: x['price'])
print("Products sorted by price using sorted and lambda:")
for p in sorted_products:
    print(f"{p['name']}: ${p['price']}")
print("\n")
print
# Lambda has limitations: single expression, no statements, limited readability.

print ("\n----------------- 6. Recursion -----------------")
# Recursio is a function that call itself to solve a smaller problme of the bigger problem.
# every recursive function must have a base case (to stops the recursion) and a recursive case(This is where the function calls itself with smaller input.).
def countdown(n):
    if n == 0: # base cas
        print("Counting is Done!")
    else: # recursive case
       print(n)
       countdown(n - 1)
countdown(5)

# where do we use the recursion function?
# we use recursion function to solve Factorial Calculation,fibonacci Sequence,Tree Traversal,Graph Traversal,Divide and Conquer Algorithms(eg: Merge Sort, Quick Sort),Backtracking Algorithms(eg: N-Queens Problem, Sudoku Solver).
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(9))  # 34

print ("\n----------------- 7. Decorators -----------------")
# cosider we have three basic math functions: add, multiply, and divide. and we want to log each time one of these functions is called.

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

#( print("Function called") in each function) then that will be repetitive code.so we can use decorators to avoid this repetitive code.

def log(func): # func is parameter here which holds the reference of the function being decorated.
    def wrapper(*args, **kwargs): # create another function wrapper that wraps the original function.
        print("Function called:", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    return a + b        
@log
def multiply(a, b):
    return a * b
@log
def divide(a, b):
    return a / b
# Using the decorated functions
result1 = add(5, 3)
print("Addition Result:", result1)
result2 = multiply(4, 2)
print("Multiplication Result:", result2)
result3 = divide(10, 2)
print("Division Result:", result3)
print("\n\n")




