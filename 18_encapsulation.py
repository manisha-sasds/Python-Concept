# In python, using  Encapsulation concept we  can protect the data inside the calss as data members (attributes) and methods from direct access from outside the class. 
# We can achieve Encapsulation in python by using three access specifiers: Public, Protected and Private

print ("\n----------------- 1. PublicEncapsulation Concept in Python ---------------")
# Public members:  can be accessed from anywhere, both inside and outside the class.

class Student:
    school = "ABC School"      # class variable 1
    country = "USA"            # class variable 2

    def __init__(self, name, age):
        self.name = name # public attribute
        self.age = age # public attribute

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    @classmethod
    def school_info(cls):
        print(f"Students go to {cls.school} in {cls.country}")

    @staticmethod
    def school_rules():
        print("Be on time, respect teachers, and complete homework.")

# Create object
s1 = Student("Emma", 20)
s1.greet()

# Call class method
Student.school_info()

# Call static method
Student.school_rules()


print ("\n----------------- 2.Protected Encapsulation Concept in Python ---------------")
# In python, single leading underscore can be used for a variable or method name indicates that it is intended for internal use within the class or its subclasses.
# _var	variable	protected (by convention)
# _method()	method	protected (by convention)
# Protected Encapsulation used for internal use within class and subclasses only, not for external use. It Works with inheritance,Improves readability, and Prevents accidental misuse (by convention)

# Used for protected members
class Car:
    def __init__(self, brand):
        self.brand = brand          # public
        self._engine_status = "OFF" # protected

    def start_car(self):
        self._engine_status = "ON"
        print("Car started")

    def show_status(self):
        print(f"Brand: {self.brand}, Engine: {self._engine_status}")
# Create object
my_car = Car("Toyota")
print(f"Accessing public attribute: {my_car.brand}")          # Accessible
print(f"Accessing protected attribute: {my_car._engine_status}") # Accessible but discouraged
my_car._engine_status = "BROKEN" # Modifying protected attribute (discouraged)
# Access using class name
my_car.show_status()
my_car.start_car()  #Modifying protected attribute using method encouraged
my_car.show_status()


print("\n\n######## Used for protected method ######## \n")
class SmartTV:
    def __init__(self, brand):
        self.brand = brand
        self._volume = 10 # 🔒 protected attribute

    def increase_volume(self):
        self._set_volume(self._volume + 15)  # 🔒 protected method

    def decrease_volume(self):
        self._set_volume(self._volume - 12) # 🔒 protected method

    def _set_volume(self, value):   # 🔒 protected method
        if 0 <= value <= 100:
            self._volume = value
        else:
            print("Volume out of range")

    def show_volume(self):
        print(f"{self.brand} TV Volume: {self._volume}")

tv1 = SmartTV("Samsung")
tv1.show_volume()
tv1.increase_volume()  # Modifying protected attribute using method encouraged
tv1.show_volume()
tv1.decrease_volume()  # Modifying protected attribute using method encouraged
tv1.show_volume()
print("Accessing protected method directly (discouraged):") 
tv1._set_volume(70)  # Directly accessing protected method (discouraged)
tv1.show_volume()

# Real-world scenario
#An Electricity Company: 1- Tracks customer balance & usage, 2- Internal calculations should NOT be modified directly, 3-Child classes (like PremiumCustomer) can safely reuse logic
print("\n---- Base Energy Account ----")
print("\n---- Base Energy Account ----")

class EnergyAccount:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self._units_used = 0        # protected variable
        self._balance = 0.0         # protected variable

    def _add_units(self, units):    # protected method
        self._units_used += units
        print(f"{units} units added")

    def _calculate_bill(self, rate):  # protected method
        self._balance = self._units_used * rate
        print("Bill calculated internally")

    def show_summary(self):
        print(f"Customer: {self.customer_name}")
        print(f"Units Used: {self._units_used}")
        print(f"Total Bill: ${self._balance}")

cust1 = EnergyAccount("Moni Singh")
cust1._add_units(150)  # Modifying protected attribute using method encouraged
cust1._calculate_bill(6)  # Modifying protected attribute using method encouraged
cust1.show_summary()

print("\n---- Regular Customer ----")

class RegularCustomer(EnergyAccount):
    def consume_energy(self, units):
        self._add_units(units)
        self._calculate_bill(rate=5)  # $5 per unit

cust2= RegularCustomer("Ravi Kumar")
cust2.consume_energy(150)
cust2.show_summary()

print("\n---- Premium Customer with less rate=3 ----")

class PremiumCustomer(EnergyAccount):
    def consume_energy(self, units):
        self._add_units(units)
        self._calculate_bill(rate=3)  # Discounted rate
cust3= PremiumCustomer("Sophia Lee")
cust3.consume_energy(150)
cust3.show_summary()

print ("\n----------------- 3.Private Encapsulation Concept in Python ---------------")

# In python, double leading underscore can be used for a variable or method name to make it private to the class.
# It cannot be accessed directly from outside the class. Python performs name mangling to make these members private.
#__var	variable	name mangled
#__method()	method	name mangled
#_	parameter	unused variable
print ("\n----------------- 3.1 __var	variable ---------------")
print("\n--- Private Variable Example ---")

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private variable

    def show_balance(self):
        print(f"Balance: {self.__balance}")
acc = BankAccount("Alice", 5000)
acc.show_balance()
print("account owner is:",acc.owner)
# print(acc.__balance)  # Attempt to access private variable directly (will raise AttributeError)

print ("\n----------------- 3.2__method()	method ---------------")


print("\n--- Private Method Example ---")

class LoginSystem:
    def __validate_password(self, password):   # private method
        return password == "admin123"

    def login(self, password):
        if self.__validate_password(password):
            print("Login successful")
        else:
            print("Invalid password")

user = LoginSystem()
user.login("admin123")

# user.__validate_password("admin123") # Attempt to access private method directly (will raise AttributeError)ß

print ("\n----------------- 3.3 _  parameter ---------------")

# _	parameter is used as unused variable
for _ in range(3): 
    print("Processing...")

# _ is used to ignore the age value
user = ("Monk", 30, "India") 
name, _, country = user
print("Ignored age here ",name, country)

# Function to display student information _ is used to ignore age parameter
def student(name, _, country): # can not use two _ in same function
    print(f"Name: {name}, Age:{_},Country: {country}")

s1=student("Alice", 22, "USA")
s2=student("Bob", 25, "UK")

print("\n--- Real-Time Banking Example ---")

class SecureBankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private

    def __log_transaction(self, amount):   # private
        print(f"Transaction logged: {amount}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__log_transaction(amount)
            print("Deposit successful")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__log_transaction(-amount)
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"Balance: {self.__balance}")

acc = SecureBankAccount("Bob", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.show_balance()


# Why do we need Encapsulation?
# 1. It protects data by not allowing anyone to change important attributes or methods directly.
# 2. It allows us to control access to attributes and method by using getter and setter methods.
# 3. It helps in data hiding and prevents accidental modification of data.
# 4. It improves code maintainability. We can change the internal implementation without affecting external code, and it also improves readability.
# 5. It allows us to decide who can view or modify the data members and methods of a class, giving full control over the class.
# You already learned:✅ Public encapsulation

# Next steps➡ Protected (_var)➡ Private (__var)➡ Property decorators (@property)





