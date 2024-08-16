from tkinter import *

operator = input("Enter an Operator (+,-,*,/): ")
num1 = float(input("Enter first number = "))
num2 = float(input("Enter second number = "))

if operator == '+' :
    result = num1 + num2
    print(result)

elif operator == "-" :
    result = num1 - num2
    print(result)

elif operator == "*" :
    result = num1 * num2
    print(result)

elif operator == "/" :
    result = num1 / num2
    print(result)

else:
    print("{operator}is not a valid operator !")
