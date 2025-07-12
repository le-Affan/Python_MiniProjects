# Create a Python program that asks the user to enter a positive integer n
# and then generates the following patterns using nested loops:
# Right-angled Triangle Pattern
# Inverted Right-angled Triangle Pattern
# Number Pyramid
# Diamond Pattern (which I will do some other time cuz im bored)

# Requirements:
# Use nested loops to construct each pattern.
# Ensure your program takes n as input only once, and prints all 4 patterns one after another.
# Use clear formatting and spacing in your output.
# Assume user will always enter a valid positive integer.

n=int(input("Enter a positive integer: "))

for i in range(n+1):
    print('*'*i)

print('\n')

for i in range(n,0,-1):
    print('*'*i)

print('\n')

current_string=''
for i in range(1,n+1):
    current_number=str(i)
    current_string+=current_number
    print(current_string)

