# Requirements:
# Console-based calculator
# User selects operation: +, -, *, /
# Takes two numbers as input
# Performs the operation and displays the result
# Handles invalid operations gracefully (like wrong input)
# Optional: Allow continuous calculations until the user exits
# Bonus Idea:
# Add an option to calculate percentage and power (^)

import math

op = input("Enter the operation you want to perform (+, -, *, /,%,^): ")

while op not in ["+", "-", "*", "/", "%", "^"]:
    print("Please enter a valid operator.")
    op = input("Enter the operation you want to perform (+, -, *, /,%,^): ")


try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    elif op == "%":
        print((a / 100) * b)
    elif op == "^":
        print(pow(a, b))
    else:
        print("Please select a valid operation")
except ValueError:
    print("Please enter a valid number")



