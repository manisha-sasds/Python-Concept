# module_04.py

# 5 variables
x1 = 1000
x2 = 2000
x3 = 3000
x4 = 4000
x5 = 5000


# 3 functions
def mul(a, b):
    return a * b

def square(a):
    return a * a

def cube(a):
    return a * a * a

# 2 classes
class Calculator:
    def addi(self, a, b,c):
        return a + b + c

    def sub(self, a, b):
        return a - b

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"
