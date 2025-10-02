########### Variable ###########

# In Python, A variable is a user-deinined name which stores a value in memory.

# 1 Rules for Naming Variables

#  1.1 Must start with a letter or underscore (_)

name ='John'
print('Name of the Employee:-',name)

_name ='Mark'
print('Name of the Employee:-',_name)

# 1.2 Cannot start with a number

# 0name ='John'   # SyntaxError: invalid decimal literal

# 1.3 Can include letters, numbers, and underscores

employee_name_1 ='Sonia'
print('Name of the New Employee:-',employee_name_1)

# 1.4 Case-sensitive (Name ≠ name)
name ='John'
print('Name of the Employee:-',name)

Name ='Kohli'
print('Name of the Employee:-',Name)
# 1.5 Cannot use reserved keywords (if, class, for, etc.)


# 2 Assigning tyes of data in Single and Multiple  Variables
# 2.1 Assigning tyes of data in Single   Variables
number=10 # Interger  data 
number_1='10' # String data 
value = 8.7        # Float
value = True   # Boolean

print(type(number)) # Gives data type of a variable int
print(type(number_1)) # Gives data type of a variable string
print(type(value)) # Gives data type of a variable float 
print(type(value)) # Gives data type of a variable bolean

print(number+number)
print(number*number)
print(number**number)
print(number/3) # float value 
print(number//3) # Give onlly decimal number 

# 2.2 Assigning tyes of data in Multiple  Variables

x, y, z = 10, 20, 30
print(x, y, z)   # Output: 10 20 30

fruits, cars = ['Banana', 'Grapes','Apple'],['Audi','BMW','Tesla']
print(fruits,cars)


# 3  Types of Variables
# 3.1 Local Variable

def my_function():
    local_var = "I am a local variable"
    print(local_var)
my_function()
# print(local_var)  # This will raise an error because local_var is not accessible outside

# 3.2 Global Variable
global_var = "I am a global variable"
def my_function():
    print(global_var)
my_function()   # This will work because global_var is accessible inside the function
print('Variable outside the function',global_var)  # This will also work because global_var is accessible outside the function              

# 3.3 Class & Instance Variables


class Car:
    wheels = 4   # Class variable
    
    def __init__(self, brand):
        self.brand = brand   # Instance variable

c1 = Car("BMW")
print(c1.brand)   # Instance
print(Car.wheels) # Class