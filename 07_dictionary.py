
# Dictionaries in Python - From Basics to Advanced Operations
# A dictionary in Python is an unordered, mutable collection that stores data in key-value pairs.
# Each key is unique and is used to access its corresponding value.
# You can create a dictionary by placing comma-separated key-value pairs inside curly braces {}.

print ("\n----------------- 1. Create a  dictionary -----------------")

# Create a dictionary
student = {
    "name": "Jhon",
    "age": 35,
    "grade": "A",
    "City" : "Coventry",
    "country": "UK"

}

print("\n Created dictionary:", student)
print ("\n----------------- 2. Second way to Creating a  dictionary using dict constructor ()-----------------")
student_from_constructor = dict(name="Jhon", age=35, grade="B",City="Coventry", country="UK")
print("\n Created dictionary using dict() constructor:", student_from_constructor)  

print ("\n----------------- 3. How to access dictionary Elements  -----------------")
print("\t   -----------------3.1 Access one value using key-name or use .get method ----------------")
# Access values using value key-name insode []
print(student["name"])   # Jhon
print(student["age"])    # 35

# Access values using .get() method
print(student.get("City"))   # Coventry
print(student.get("country")) # UK

print("\n   -----------------3.2 Access all keys suing .keys() method ---------------\n-")
print(student.keys())

print("\n\t   -----------------3.3 Access all Values  uing .values() method ----------------")
print(student.values())

print("\n\t   -----------------3.4 Access all key-value pairs using .items() method ----------------")
print(student.items())

print("\n\t   -----------------3.5 Check if a key exist  ----------------")
if "country" in student:
    print("country key  is present in the student dictionary.")
else:
    print("country key is not present in the student dictionary.")


print ("\n\n----------------- 4. How t andd and  modify dictionary Elements  -----------------")   
print("\t   -----------------4.1 Add new key-value pair ----------------")
# Add a new key-value pair
student["hobby"] = ["reading","traveling"]
print("After adding new key-value pair:", student)

print("\t   -----------------4.2 Modify value of existing key ----------------")
# Modify value of existing key
print("Original country and grade:", student)
student["country"] = "USA"
student["grade"] = "A+"
print("After value update:", student)


print("\n   -----------------5 Remove items from Dict ----------------")
print("\t   -----------------5.1  pop() method ----------------")
# There are several ways to remove items from a dictionary.
# Using pop() method to remove a key-value pair
removed_grade = student.pop("grade")
print("After popping grade:", student) 
print("Popped grade value:", removed_grade)


print("\t   -----------------5.2  popitem() method ----------------")   
# Using popitem() method to remove the last inserted key-value pair
last_item = student.popitem()
print("After popping last item:", student) 
print("Popped item:", last_item)
print("\t   -----------------5.3  del keyword ----------------")
# Remove a key-value pair using del
del student["age"]
print("After deleting age using del:", student) 

# Using clear() method to remove all items
student.clear()
print("After clearing all items the student dict is empty :", student)

print("\t   -----------------6 Loop in Dictionary ----------------")

# Loop through keys
for x in student:
    print(f" Key: {x}, Value: {student[x]}")

# Loop through keys using .keys() method
print("\n")
for x in student.keys():
    print(f"Key: {x}")  

# Loop through values
print("\n")
for x in student.values():
    print(f"Value: {x}")    
# Loop through key-value pairs
print("\n")
for x, y in student.items():
    print(f"Key: {x}, Value: {y}")    

print("\t   -----------------7 Nested Dictionary ----------------")
# A nested dictionary means a dictionary inside another dictionary.It allows you to store hierarchical or structured data like data that has levels or groups within groups.

company = {
    "HR": {
        "manager": "Luca",
        "employees": ["Tom", "Lily", "Sam","Moni"],
        "location": "New York"
    },
    "IT": {
        "manager": "Bob",
        "employees": ["John", "Mona", "Ravi"],
        "location": "London"
    },
    "Finance": {
        "manager": "Sophia",
        "employees": ["Sonia", "Kate"],
        "location": "Toronto"
    }
}

print (company)

print("\t   -----------------7.1 Access Nested Dictionary Elements ----------------")

print(company["Finance"])
print(company["HR"]["manager"])
print(company["IT"]["employees"][1])
print(company.get("IT").get("location"))
print(company.get("IT").get("employees")[2])


print("\t   -----------------7.2 Add Nested Dictionary Elements ----------------")

company["IT"]["employees"].append("Andy")
print(company["IT"]["employees"])


company.update({"Marketing": {
"manager":"Lisa",
"employees":["Tina","Lina","Meena"],
"location":"UK"
}})
print (company)

print("\t   -----------------7.3 Modify Nested Dictionary Elements ----------------")
company["Finance"]="Finance_UK"
print("Modified companys Finance dept name as:  ", company["Finance"])

company["IT"]["employees"][1]="Monalisa"
print(company["IT"]["employees"][1])

company.get("IT").get("employees")[2]="Jaymala"
print(company.get("IT").get("employees")[2])



print("\t   -----------------7.4 Remove Nested Dictionary Elements ----------------")
company["IT"]["employees"].remove("John")
print(company["IT"]["employees"])

del company["Finance"]
print (company)     

del company["HR"]["location"]
print (company)

