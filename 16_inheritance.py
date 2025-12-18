# Inheritance  concept in python allow a class to inherit attributes and methods from another class.
# The class which gives proerties, methods, constructor is called Base class or Parent class
# The class which recieves/inherits properties, methods, constructor is called Derived class or Child class

print ("\n----------------- 1 Inheritance  Concept---------------")

# Created Base class or Parent class 
class Parent:   
    def greet(self):
        print("Hello from Parent class")
        
    def cal(self,a,b):
     sum=a+b
     return sum

# Created Derived class or Child class that inherits from Parent class here
class Child(Parent):  
    pass
c = Child()
c.greet()
print(c.cal(20,40))

print ("\n----------------- 1 __init__() method in parent class ---------------")
# Example of Inheritance with __init__() method in Parent 


class Product:
   def __init__(self,name_of_Product, price,quantity):
       self.name = name_of_Product
       self.price = price
       self.quantity = quantity

class Book(Product):
       pass
b = Book("Python Programming", 29.99, 3)
print(f" Name of the Book is: {b.name},\n Price of the book is: {b.price},\n Quantity Available: {b.quantity}")


print ("\n----------------- 1.1 __init__() method in Child class ---------------")

class Product:
   def __init__(self,name_of_Product, price,quantity):
       self.name = name_of_Product
       self.price = price
       self.quantity = quantity

class Book(Product):
   def __init__(self,name_of_Product, price,quantity, author): # Here Child class has its own constructor which is overriding Parent class constructor
       super().__init__(name_of_Product, price,quantity)  # Calling Parent class constructor explicitly using super()
       self.author = author

b = Book("Python Programming", 29.99, 3, "John Doe")
print(f" Name of the Book is: {b.name},\n Price of the book is: {b.price},\n Quantity Available: {b.quantity},\n Author of the book is: {b.author}")

print ("\n----------------- 2 Single Inheritance Parent class Employee -> Child class Manager ---------------")


class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id) # Call Parent's __init__ so no need to repeat code
        self.department = department

emp1=Employee("Bob", 100)
print(f"Employee Information:\n Name: {emp1.name},\n ID: {emp1.emp_id}")
m = Manager("Alice", 101,"IT")
print(f"Manager Information:\n Name: {m.name},\n ID: {m.emp_id},\n Department: {m.department}")

print ("\n----------------- 3 Muiltilevel Inheritance Parent class Employee -> Child class Manager ---------------")
# Multi-Level Inheritance Example: three classes - Employee, Parent-Manager,TeamLead
# Super() is used to call the parent class constructor and call the next  method in the Method resolution order(MRO)

class Employee: # Grandparent class
    def __init__(self,company_name, emp_name, emp_id):
        self.company_name = company_name
        self.name = emp_name
        self.emp_id = emp_id    
    def work(self):
        print("Employee works")
class Manager(Employee): # Parent class
    def __init__(self,company_name, emp_name, emp_id, department):
        super().__init__(company_name, emp_name, emp_id)
        self.department = department
    def manage(self):
        print("Manager manages the team")
class TeamLead(Manager): # Child class
    def __init__(self,company_name, emp_name, emp_id, department, team_size):
        super().__init__(company_name, emp_name, emp_id, department)
        self.team_size = team_size   

    def lead(self):
        print("TeamLead leads the team")
   
emp1= Employee("IBM", "Boney", 100)
print(f"1-Employee Information: Company: {emp1.company_name},\n Name: {emp1.name},\n ID: {emp1.emp_id}")
emp1.work() 

m1= Manager("IBM", "Merry", "IT", 101)
print(f"2-Manager Information: Company: {m1.company_name},\n Name: {m1.name},\n ID: {m1.emp_id},\n Department: {m1.department}")
m1.work()
m1.manage()

tl = TeamLead("IBM", "Charlie", 102, "IT", 5)
print(f"3-Team Lead Information:\n Company: {tl.company_name},\n Name: {tl.name},\n ID: {tl.emp_id},\n Department: {tl.department},\n Team Size: {tl.team_size}")
tl.work()
tl.manage()
tl.lead()
print(----------------- 4  Multiple Inheritance: Two+ Parents → One Child  -------------------)
# When one Child class Manager inheris from  Two Parent classes Employee1 and Employee2 
class Employee1: # Parent class 1
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id    
    def work(self):
        print("Employee1 works")
class Employee2: # Parent class 2
    def __init__(self, company_name):
        self.company_name = company_name    
    def attend_meeting(self):
        print("Employee2 attends meeting")
class Manager(Employee1, Employee2): # Child class inheriting from both Parent classes
    def __init__(self, name, emp_id, company_name, department):
        Employee1.__init__(self, name, emp_id)  # Initialize Employee1 part
        Employee2.__init__(self, company_name)  # Initialize Employee2 part
        self.department = department   
    def manage(self):
        print("Manager manages the team")
emp1= Manager("David", 103, "Google", "HR")

print(f"Manager Information:\n Company: {emp1.company_name},\n Name: {emp1.name},\n ID: {emp1.emp_id},\n Department: {emp1.department}")
emp1.work()  # From Employee1
emp1.attend_meeting()  # From Employee2
emp1.manage()  # From Manager   

print ("\n----------------- 5 Hierarchical Inheritance One Parent → Multiple Children---------------")

class Worker: # Parent class
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay
    
    def calculate_salary(self):
        print(f" Worker.calculate_salary() called")
        return self.base_pay

class Developer(Worker): # Child class 1
    def __init__(self, name, base_pay, projects_completed): # Child class 1 constructor
        super().__init__(name, base_pay) # Call Parent's __init__()
        self.projects_completed = projects_completed
    
    def calculate_salary(self):
        print(f"  Developer.calculate_salary() called")
        project_bonus = self.projects_completed * 2000
        return self.base_pay + project_bonus

class Designer(Worker): # Child class 2
    def __init__(self, name, base_pay, designs_created): # Child class 2 constructor
        super().__init__(name, base_pay) # Call Parent's __init__()
        self.designs_created = designs_created

    def calculate_salary(self):
        print(f" Designer.calculate_salary() called")
        design_bonus = self.designs_created * 1500
        return self.base_pay + design_bonus

class Tester(Worker):
    def __init__(self, name, base_pay, bugs_found):
        super().__init__(name, base_pay)
        self.bugs_found = bugs_found
    
    def calculate_salary(self):
        print(f" Tester.calculate_salary() called")
        bug_bonus = self.bugs_found * 100
        return self.base_pay + bug_bonus
    
work=Worker("Keti", 3000)
print(f"Worker info: {work.name}, Salary: {work.calculate_salary()}")
dev=Developer("Lina", 4000, 5)
print(f"Developer info: {dev.name}, Salary: {dev.calculate_salary()}")
des=Designer("Mia", 3500, 4)
print(f"Designer info: {des.name}, Salary: {des.calculate_salary()}")
test=Tester("Nina", 3200, 50)
print(f"Tester info: {test.name}, Salary: {test.calculate_salary()}")

print ("\n----------------- 6 Diamond Inheritance one child access parent 1, parent 2 and parent 1, parent 2  access Grandparent---------------")
# Methods are resolved in MRO order (left-to-right, depth-first) which prevents duplicate initialization of Grandparent class

class Grandparent: # Grandparent class
    def __init__(self, address, **kwargs):
        super().__init__(**kwargs)
        self.address = address

    def show(self):
        print("This is Grandparent class method")

class Parent1(Grandparent):# Parent1 class
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name

    def show(self):
        print("This is Parent1 class method")
        super().show()

class Parent2(Grandparent): # Parent2 class
    def __init__(self, surname, **kwargs):
        super().__init__(**kwargs)
        self.surname = surname

    def show(self):
        print("This is Parent2 class method")
        super().show()

class Child(Parent1, Parent2): # Child class
    def __init__(self, address, name, surname):
        # Use **kwargs to pass arguments to parents
        super().__init__(address=address, name=name, surname=surname)
    def show(self):
        print("This is Child class method")
        super().show()  

# ----------------- Create object BEFORE deleting show -----------------
c = Child(address="123 Main St", name="Emma", surname="Stone")

print(f"Child Info BEFORE deleting show: Name: {c.name}, Surname: {c.surname}, Address: {c.address}")
c.show()  # Follows MRO: Child → Parent1 → Parent2 → Grandparent

print("MRO:", [cls.__name__ for cls in Child.__mro__])

# ----------------- Delete Child.show -----------------
print("\n--- Deleting Child.show ---")
del Child.show

c.show()  # Falls back to Parent1.show automatically
