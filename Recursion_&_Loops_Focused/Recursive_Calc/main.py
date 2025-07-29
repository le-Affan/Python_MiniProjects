# Create a Python program called recursive_calculator.py that uses recursion
# to perform basic mathematical operations like:
# Factorial
# Sum of Natural Numbers
# Power of a number (x^y)
# Assume the user enters valid input

x = int(input("Enter a positive integer: "))
# y = int(input("Enter another positive integer for exponent: "))

def factorial(x,product=1):
    if x == 0 or x == 1:
        return product
    else:
        factorial(x,product*x)


print(factorial(x))


