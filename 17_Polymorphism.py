# Polymorphism = "Many Forms" (poly = many, morph = forms)
# It allows same function, operator or method to behave differently based on the object/class task at hand which makes it reuasable,flexibke, and essier to maintain.
# Python supports polymorphism mainly in 4 ways
# important points to remember about polymorphism:
# Polymorphism requires the same method name,parameters must be compatible — either the same or optional, required parameters must not differ when methods are called in a loop.

# This type of polymorphism , wont matter about the class names,inheritance, relationships between classes It only cares about Does this object have a same method in all classes?

class Circle:
    def draw(self, side):
        print("Draw a circle")
        area = 3.14 * side * side
        print(f"Area of Circle is: {area}")
        return area

class Square:
    def draw(self, side):
        print("Draw a square")
        area = side * side
        print(f"Area of Square is : {area}")
        return area

cr = Circle()
sq = Square()

for obj in [cr, sq]:
    obj.draw(20)

print("--------------- 2.  Polymorphism: concept in Operators Overloading -------------------")
# we can use same operator +,-,* ,etc operator behaves differently based on the data types
a = 10
b = 5
print("Addition of two integers:", a + b)  # Addition of integers       
x = "Hello, "
y = "World!"
print("Addition of two strings:", x + y)  # Addition of strings (concatenation)

# Sawme way len() function behaves differently based on the data type passed to it
print(len("Hello Rima"))     # string
print(len([1, 2, 3,56,46]))  # list
print(len({"Name":"Kiya","Age":36})) # Dict


print("--------------- 3.Polymorphism: Method Overloading -------------------")
# Method Overloading:  In the same class, when we use one or more methods with the same name but different parameters (different type or number of parameters), it is known as method overloading.
# Use case: Mathematical operations with different number of inputs
class MathOperations:
    def add(self, a, b, c=0,d=0):
        return a + b + c + d   
math_ops = MathOperations()
print("Addition of two numbers:", math_ops.add(10, 20))          # Calls add(a, b)
print("Addition of three numbers:", math_ops.add(10, 20, 30))  # Calls add(a, b, c) 
print("Addition of four numbers:", math_ops.add(10, 20, 30,40))  # Calls add(a, b, c,d)


print("--------------- 4. Polymorphism:Method Overriding( Inheritance )-------------------")
# Method Overriding: When a derived class has a method with the same name as a method in its base class, the derived class's method overrides the base class's method.  
# Use case: Payment processing system with different payment methods 
class Payment:
   def pay(self, amount):
        print("Paying amount")
class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class Cash(Payment):
    def pay(self, amount):
        print(f"Paid {amount} in Cash")

for p in (CreditCard(),UPI(),Cash()):
    p.pay(500)


