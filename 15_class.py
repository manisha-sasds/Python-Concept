# A class is a blueprint using it we can create several objects having similar properties and behavior. 
# When you create an object from a class, it inherits all the variables and functions defined inside that class.
# diffreence between class attribute and instaance artribute is that class attribute is shared across all instances of the class, while instance attribute is unique to each instance.
'''
Class classname: # Used class keyword to create a class named 
    <body of class> # Indented block containing class attributes and methods
'''

print ("\n----------------- 1  Create a simple class---------------")

class FirstClass: 
  # Class attributes hold class data
  x = 5000
  y= 6778
  z= 56.78
  fruits=["mango","grapes","banana","apple"]
  employee={"name":"moni", "age":34,"salary":7000}

# we are accessing class attributes directly via the class name 
print(FirstClass.x)
print(FirstClass.y)
print(FirstClass.z)
print(FirstClass.fruits)
print(FirstClass.employee)

print ("\n----------------- 1.2 Create object of a class and access class attributes ---------------")
myobj1=FirstClass()
print("myobj1  is created n gettinfo data from class attribute")
print(myobj1.x)
print(myobj1.y)
print(myobj1.fruits)
print(myobj1.employee)


print ("\n----------------- 1.3 Adding  new method to class and access class attributes  ---------------")

class FirstClass:
    # Class attributes
    x = 1000
    y = 3000
    fruits = ["mango", "grapes", "banana"]# Mutable 

    # Instance method
    def show_numbers(self,a,b):
        print(f"Class attrinutes are : x={self.x}, y={self.y}")  # Can access class attributes
        print(f"Method parameters are: a={a}, b={b}")  # Access method parameters
        addition = a + b + self.x + self.y
        print(f"Addition of a,b,x,y is: {addition}\n ")    
        return addition

    # Another instance method
    def add_fruit(self, newfruit):
        self.fruits.append(newfruit)  # Modifies the shared class attribute

# Accessing class attribute directly
print("Value of Class attributes x is :",FirstClass.x)  # 5000

# Creating objects
obj1 = FirstClass()
obj2 = FirstClass()

print("accessing method show_numbers using obj1 and obj2\n")
obj1.show_numbers(10,20)
obj2.show_numbers(111,555)

print("\nAdding fruit through obj1") 
obj1.add_fruit("apple")

# Check fruits list (shared class attribute)
print(obj1.fruits)  # ['mango', 'grapes', 'banana', 'apple']
print(obj2.fruits)  # ['mango', 'grapes', 'banana', 'apple']

# Changing fruits  attribute using obj1 object affects all objects This is OK for learning, but not good for real projects so we use instance attributes using __init__. 
print ("\n----------------- 2- Using __init__ method to create instance attributes ---------------")
# init method is used to create the instance attribute which is unique to each object and give each oject its own data.Here, we are creating instance attribute fruits which is unique to each object.
class FirstClass:
    # Class attributes
    x = 1000
    y = 3000

    def __init__(self):
        # Instance attribute
        self.fruits = ["mango", "grapes", "banana"] 
    def show_numbers(self,a,b):
        print(f"Class attrinutes are : x={self.x}, y={self.y}")  # Can access class attributes      
        print(f"Method parameters are: a={a}, b={b}")  # Access method parameters
        addition = a + b + self.x + self.y
        print(f"Addition of a,b,x,y is: {addition}\n ")
        return addition 
    def add_fruit(self, newfruit):
        self.fruits.append(newfruit)  # Modifies the instance attribute
# Creating objects with different fruit lists
obj1 = FirstClass()
obj2 = FirstClass()

obj1.add_fruit("apple")
print("Fruits in obj1:", obj1.fruits)  # ['mango', 'grapes', 'banana', 'apple']
print("Fruits in obj2:", obj2.fruits)  # ["mango", "grapes", "banana"]

print (" -------------------- Passing different values for each object ---------------")
class FirstClass:
    # Class attributes
    x = 1000
    y = 3000

    def __init__(self,fruits_list):
        # Instance attribute
        self.fruits = fruits_list # 
    def show_numbers(self,a,b):
        print(f"Class attrinutes are : x={self.x}, y={self.y}")  # Can access class attributes      
        print(f"Method parameters are: a={a}, b={b}")  # Access method parameters
        addition = a + b + self.x + self.y
        print(f"Addition of a,b,x,y is: {addition}\n ")
        return addition 
    def add_fruit(self, fruits):
        self.fruits.append(fruits)  # Modifies the instance attribute
# Creating objects with different fruit lists
obj1 = FirstClass(['watermelon', 'grapes', 'banana', 'Kiwi'])
obj2 = FirstClass(['Orange','Pinapple','Kiwi'])

obj1.add_fruit("apple")
print("Fruits in obj1:", obj1.fruits)  # ['watermelon', 'grapes', 'banana', 'Kiwi', 'apple']
print("Fruits in obj2:", obj2.fruits)  # ['Orange', 'Pinapple', 'Kiwi']
print ("\n----------------- 3 - Using  Self  ---------------")
# self as it is the convention in Python and makes your code more readable, but you can use any name instead of ‘Self’
# Self-parameter gives the reference to the current instance of the class,  and using self we can access the properties/variable and methods belon to the class
# Without self, Python would not know which object's properties you want to access:
# print ("\n----------------- 3.1 - Program of Online Shopping Cart Using  Self   ---------------")

class Shooping:
    def __init__(self, user,age):
        self.name=user
        self.age=age
        self.list_item=[]

    def add_item(self,item):
        self.list_item.append(item)
        print(f"Added {item}")

    def show_cart(self):
        return f"{self.name}'s cart: {self.list_item}"

        # create objects 
cust1=Shooping("Jhon",34)
cust2=Shooping("Meena",29)

cust1.add_item("Mac Laptop")
cust1.add_item("Head phone")
cust1.add_item("Mouse")

print(cust1.show_cart())

print ("\n----------------- 3.2 - Program of Online Shopping Cart Using first pareter name as self_alt instead Self and access instance variable name  ---------------")

class Shooping:
    def __init__(self_alt, user,age):
        self_alt.name=user
        self_alt.age=age
        self_alt.list_item=[]

    def add_item(self_alt_m,item):
        self_alt_m.list_item.append(item)
        print(f"Added {item}")

    def show_cart(self_alt_2):
        print(f"Customer Name is :{self_alt_2.name}") #  access instance variable name
        return f"{self_alt_2.name}'s cart: {self_alt_2.list_item}"

# create objects 
cust1=Shooping("Jhon",34)
cust2=Shooping("Meena",29)

cust2.add_item("Clock")
cust2.add_item("Wall paint")
cust2.add_item("Bag")

print(cust2.show_cart())


print ("\n----------------- 4  - Python Class Properies ---------------")
# In python Properies = Variables there are 
# two types of varaible  1. Class Variables  - Class Properties
#                        2. Instance Variables - Object Properties 
print ("\n----------------- 4.1   - Python Class Properies ---------------")
# create, modify, and delete class variables

class Employee:
    Comp_name="Google" # class variables
    Office_code="PE123B" # class variables

emp1=Employee()
emp2=Employee()

print(f'Emp1 information is : {emp1.Comp_name}')
print(emp1.Office_code)

print(f'emp2 information is : {emp2.Comp_name}')
emp2.Office_code="GC879M"
print(emp2.Office_code) #  modified class variables
del emp1 #  deleted class variables
# print(f'Emp1 information is : {emp1.Comp_name}') #### NameError: name 'emp1' is not defined. Did you mean: 'emp2'?

print ("\n----------------- 4.2   - Python Instance Properies ---------------")
# create, modify, and delete Instance variables

class Employee:
    Comp_name="Google" # class variables
    Office_code="PE123B" # class variables

    def __init__(self, first_name,last_name,age):
        self.name=first_name # Instance variables
        self.last=last_name
        self.age=age

emp1=Employee("Jhon","Keet",34)
emp2=Employee("Sara","Das",40)

print(f'Emp1 information is : {emp1.Comp_name}')
print(emp1.name)
print(emp1.Office_code)

print(f'emp2  information is : {emp2.Comp_name}')
print(emp2.name)
emp2.Office_code="GC879M"

print(emp2.Office_code) #  modified class variables
del emp1 #  deleted class variables
del emp2.name # deleted instance variables
# print(f'Emp1 information is : {emp1.Comp_name}') #### NameError: name 'emp1' is no
# print(emp2.name) ### AttributeError: 'Employee' object has no attribute 'name'


# print ("\n----------------- 5 - Python Class Methods ---------------")
# In python there are Three types of Methods
#                        1. Class Methods  
#                        2. Instance Methods
#                        3. Static Methods   
print ("\n----------------- 5.1 Class Methods  ---------------")

class Employee:

    # ----- Here are Class  Variables which can be shared by all objects -----
    company_name = "TechSoft"
    company_location = "Bangalore"
    company_strength = 200
    company_revenue = "10 Crore"

    # ----- Class Method takes cls parameter (Operate on class variables) -----
    @classmethod
    def show_company_info(cls):
        print("\n[CLASS METHOD] Company Info:")
        print(f"Name: {cls.company_name}")
        print(f"Location: {cls.company_location}")
        print(f"Strength: {cls.company_strength}")
        print(f"Revenue: {cls.company_revenue}")

    @classmethod
    def update_company_strength(cls, new_strength):
        cls.company_strength = new_strength
        print(f"\n[CLASS METHOD] Updated company strength to {cls.company_strength}")
# Updating company strength using class method
Employee.update_company_strength(260)
# Accessing class method using class name
Employee.show_company_info()


print ("\n----------------- 5.2 Instance Methods  ---------------")

class Employee1:

    company_name = "TechSoft"
    def __init__(self, name_of_emp, age, salary,position): # Constructor to initialize instance variablesß
        # Instance Variables unique to each object
        self.name = name_of_emp
        self.age = age
        self.salary = salary
        self.position = position

    # ----- Instance Method takes self parameter (Operate on instance variables) -----
    def show_employee_info(self,id): # Instance Method to show employee info
        print("\n[INSTANCE METHOD] Employee Info:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Position: {self.position}")
        print(f"ID: {id}")
        print(f"Company: {self.company_name}")  # Accessing class variable using self.
 
    def calculate_annual_salary(self):   # Instance Method to calculate annual salary
        annual_salary = self.salary * 12
        print(f"\n[INSTANCE METHOD] Annual Salary of {self.name} is: {annual_salary}")
        return annual_salary
    
    def access_class_var_instance(self):
        print("\n[INSTANCE METHOD] Accessing Class Variables from Instance:")
        return self.name,Employee1.company_name # Accessing class variable using class name  and instance variable using self.

# Creating objects
emp1 = Employee1("Jhon", 34, 2300, "Developer")
emp2 = Employee1("Sara", 29, 250000,"Designer")

# Accessing instance method using objects
print(" Emplyeee's Information is : ",emp2.show_employee_info("ID876456"))
print(" Emplyee's   Annual Salary is:", emp1.calculate_annual_salary())
emp_name,company_name= emp2.access_class_var_instance()
print(f"Emplyee {emp_name} Works for : {company_name}" ) 

print("\n----------------- 5.3 Static Methods   ---------------")
class Employee2:

    tax_rate = 0.10
    bonus_rate = 0.05
    min_salary = 10000
    max_salary = 150000

    @staticmethod
    def company_policy():
        print("\n[STATIC METHOD] Company Policy:")
        print("-> Work 8 hours daily")
        print("-> Follow company rules")

    @staticmethod
    def calculate_tax(amount):
        print(f"\n[STATIC METHOD] Tax on {amount}: {amount * Employee2.tax_rate}")

Employee2.company_policy()
Employee2.calculate_tax(50000)

print ("\n----------------- 5.4 Access, Modify, Delete Mothods   ---------------")

class Employee3:
    company_name = "TechSoft"
    company_location = "Bangalore"
    company_strength = 200
    company_revenue = "10 Crore"
    # Considered a static variable 
    tax_rate = 0.10

    @classmethod
    def update_company_strength(cls, new_strength):
        cls.company_strength = new_strength
        print(f"\n[CLASS METHOD] Updated company strength to {cls.company_strength}")

    def __init__(self, name_of_emp, age, salary,position): # Constructor to initialize instance variablesß
        # Instance Variables unique to each object
        self.name = name_of_emp
        self.age = age
        self.salary = salary
        self.position = position
    
    def calculate_annual_salary(self):   # Instance Method to calculate annual salary
        annual_salary = self.salary * 12
        print(f"\n[INSTANCE METHOD] Annual Salary of {self.name} is: {annual_salary}")
        return annual_salary
    
    @staticmethod
    def calculate_tax(amount):
        print(f"\n[STATIC METHOD] Tax on {amount}: {amount * Employee3.tax_rate}")
        return amount * Employee3.tax_rate
    
    @classmethod
    def show_company_info(cls):
        print("\n[CLASS METHOD] Company Info:")
        print(f"Name: {cls.company_name}")
        print(f"Location: {cls.company_location}")
        print(f"Strength: {cls.company_strength}")
        print(f"Revenue: {cls.company_revenue}")
  
    # print ("\n----------------- Access variables n methids   ---------------")
    def show_employee_details(self,id): # Instance Method to show employee all informtio
        print("\n[INSTANCE METHOD] Employee Info:")
        print(f"Name: {self.name}")
        print(f"ID: {id}")
        Employee3.show_company_info() # Accessing class method using class name
        
        self.calculate_annual_salary() # Accessing instance method using self
        Employee3.calculate_tax(self.salary) # Accessing static method using class name

    # print ("\n----------------- Modifing  variables n methids   ---------------")
    def updated_employee_details(self,id): # Instance Method to show employee all informtio
        print("\n[INSTANCE METHOD] Employee Info Updated:")
        self.name= "Farsha" # Modifying instance variable
        print(f"Name: {self.name}")
        id= "ID998877"  # Modifying method parameter
        print(f"ID: {id}")
        Employee3.update_company_strength(300) # Modifying class variable using class method
        Employee3.show_company_info() # Accessing class method using class name
        self.calculate_annual_salary() # Accessing instance method using self
        Employee3.calculate_tax(self.salary) # Accessing static method using class name

    
   # print ("\n----------------- Deleting methids   ---------------")

   # del calculate_tax  # Deleting static method
   # del update_company_strength # Deleting class method
   # del calculate_annual_salary # Deleting instance method

# Creating objects
emp1 = Employee3("Fara", 34, 2370, "UI/UX Developer")
emp2 = Employee3("Merry", 29, 27000,"Database Designer") 

# Accessing instance method using objects
emp2.show_employee_details("ID123456")
emp2.updated_employee_details("ID123456")



