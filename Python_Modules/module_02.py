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
