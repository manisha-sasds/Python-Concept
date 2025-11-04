# In python match and case work together.
# We use match when wewe need cleaner, readable code instead of long if-elif-else chains.
print ("\n----------------- 1. match-case -----------------")

num1=float(input("Enter First number= "))
num2=float(input("Enter Second number= "))
operator=input("Enter Operator are +, - ,/, * = ")
match operator:
    case '+' :
        print(f"addition of {num1} and {num2}  is= ", sum)
    case '-':
        sub=num1-num2
        print(f"Subtraction of {num1} and {num2}  is= ", sub)
    case '*':
        mult=num1*num2
        print(f"multipilcatio of {num1} and {num2}  is= ", mult)
    case '/':
        if num2!=0:
            div=num1/num2
            print(f"division of {num1} and {num2}  is= ", round(div,4))
        else:   
            print("Error: Division by zero is not allowed")
    case _:
        print("Invalid operator entered.")
print ("\n----------------- 2. Multiple matches in one case  -----------------")

# we combine multiple values with the pipe symbol | (which means “OR”).
drink = input("Enter your drink (coffee, tea, juice, water): ").lower()

match drink:
    case "coffee" | "tea":
        print("That will be served hot ☕")
    case "juice" | "water":
        print("That will be served cold 🧊")
    case _:
        print("Sorry, we don’t serve that drink.")
print ("\n----------------- 3. if statement in case  -----------------")

month = 5
temperature = 17

match temperature:
    case t if 0 <= t <= 15 and month in (12, 1, 2):
        print("Cold winter day")
    case t if 16 <= t <= 25 and month in (3, 4, 5):
        print("Pleasant spring day")
    case t if 26 <= t <= 35 and month in (6, 7, 8):
        print("Hot summer day")
    case _:
        print("Normal day")
