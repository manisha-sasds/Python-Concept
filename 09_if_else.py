#  if-else Statement in Python
print ("\n----------------- 1. if Statement -----------------")
# In if statemment we can ues diffrenet mathematical comparison operators to execute a block of code only if a specified condition is true.

##----------------- Using != operator -----------------##
num1=22
num2=65
if num1!=num2:
    print(f"\n{num1} is not equal to {num2}")

print ("\n----------------- 2. if-else Statement -----------------")
##-----------------  Using <=operator -----------------##
if num1 <= num2:
    print(f"\n{num1} is less than {num2}")
else:
    print(f"\n{num1} is not less than or equal to {num2}")

print ("\n----------------- 2. if-elif-else Statement -----------------")
# The if-elif-else statement in Python allows you to check multiple conditions from top to bottom.
# The first condition that evaluates to True will execute its corresponding block of code, and the rest will be skipped.
# If none of the conditions are True, the code block under else will be executed.
credit_score = 750
if credit_score >= 800:
    print("\nExcellent credit score")
elif credit_score >= 700:
    print("\nGood credit score")
elif credit_score >= 600:
    print("\nFair credit score")
else:
    print("\nPoor credit score")


print ("\n----------------- 3. Nested if Statement -----------------")
age =25
license_years =3
accident_free_years =1
if age >= 18:
    if license_years >= 2:
        if accident_free_years == 0:
            print("\nEligible for premium insurance discount")
        else:
            print("\nEligible but higher premium due to accident history")
    else:
        print("\nNeed more driving experience to apply for discount")
else:
    print("\nYou must be at least 18 to apply for insurance ")

print ("\n----------------- 4. Python shorted if-else (ternary) operator -----------------")
a=55
b=34
if a>b: print("a is greater than b")

# If we are using if-else in a single line, we can use the ternary operator.
print("A is gretaer") if a>b else print("B is greater") 

max_value = a if a > b else b
print(f"\nThe maximum value between {a} and {b} is: {max_value}")
# multiple condition on single line

hour = 14
print("Good Morning") if hour < 12 else print("Good Afternoon") if hour < 18 else print("Good Evening")
# nested ternary operator
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(f"\nThe grade for score {score} is: {grade}")

print ("\n----------------- 5. Python Logical Operators and, or , not -----------------")

# Logical operators are used to combine conditional statements.
# and - Returns True if both statements are true
num1 = 10
num2 = 20
num3 = 15     
if num1 < num2 and num1 < num3:
    print(f"\n{num1} is the smallest number among {num1}, {num2}, and {num3}")      
if num2 > num1 and num2 > num3:
    print(f"\n{num2} is the largest number among {num1}, {num2}, and {num3}")  

# or - Returns True if one of the statements is true
has_ticket = False
is_vip = True

if has_ticket or is_vip:
    print("You can enter the concert.")
else:
    print("Access denied.")

# not - Reverse the result, returns False if the result is true 
is_logged_in = False
if not is_logged_in:
    print("Please log in to continue.\n")

# Multiple conditions with and, or, 
age = 22
has_passport = True
has_visa = False
if age >= 18 and (has_passport and has_visa):
    print("\n You can travel internationally.")
elif age >= 18 and (has_passport or has_visa):
    print("You have incomplete travel documents.")
else:
    print("Not eligible to travel.")

