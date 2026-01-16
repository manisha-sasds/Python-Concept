
import module_02 # 1. Import Entire Module
# print ("\n----------------- 1 Import Entire Module  ---------------")
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

print("\n----------------- 2 Import with Alias  ---------------")
import module_02 as mod # 2. Import with Alias

print(mod.x)
print(mod.str1) 
print(mod.add(10, 20))
print(mod.multiply(6, 7))
print(mod.is_even(10))
person_obj = mod.Person("Alice")
print(person_obj.say_name())
counter_obj = mod.Counter()
print(counter_obj.increase())

print("\n----------------- 3 Import Specific Items like Functions, Classes ,Vraiables  ---------------")

from module_02 import str1, add, Person # 3. Import Specific Items only 

print(str1)
print(add(15, 25))
person_obj1 = Person("Bob")
print(person_obj1.say_name())   

print("\n----------------- 4 Import Specific Items like Functions, Classes ,Vraiables with Custom Alias  ---------------")

from module_02 import str1 as st, multiply as mul, is_even as check_even, Counter as cnt # 4. Import with Custom Alias
print(st)
print(mul(20, 90))
print(check_even(144))
counter_obj1 = cnt()
print(counter_obj1.increase())  

print("\n----------------- 5 Import All (NOT RECOMMENDED!)  ---------------")
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

 
import module_03 # Import Entire module_03 this you can write at the top also
print("\n----------------- module_03 Usage Example  ---------------")
print("Variables from module_03:")
print(module_03.x1)
print(module_03.x2)
sq=module_03.square(5)
print("Square of 5 using module_03.square():", sq)
mul_result=module_03.mul(4, 6)
print("Multiplication of 4 and 6 using module_03.mul():", mul_result)