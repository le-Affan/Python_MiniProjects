# Requirements:
# Program randomly picks a number between 1 and 100
# User has to guess the number
# After each guess, program tells:
# “Too high” if guess > number
# “Too low” if guess < number
# “Correct” if guess == number
# Track number of attempts taken
# After the game ends, ask if they want to play again
# Optional Bonus:
# Limit maximum attempts to 7
# If player runs out of attempts — reveal number and end game
# Use a while loop and random module

import random

def prompt():
    a = int(input("Guess the number! "))
    return a

def game():
    n = random.randint(1, 100)
    i=1
    while i <= 8:
        rand_num=prompt()
        if rand_num > n:
            print("Too high")
        elif rand_num < n:
            print("Too Low")
        elif rand_num == n:
            print("Correct Guess!!")
            break
        i += 1
        if i == 8:
            print(f"Out Of Attempts! Your Number was {n}")
            break

game()

while True:
    choice=str(input("Do you want to play again? (Yes or No)"))

    if choice.capitalize() not in ["Yes","No"]:
        print("Please Enter A Valid Choice")

    if choice.capitalize()=="Yes":
        game()
    elif choice.capitalize()=="No":
        print("Thank You For Playing!")
        break


