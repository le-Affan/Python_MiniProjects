# Requirements:
# Simulate rolling a 6-sided dice
# Each time user types roll, a random number between 1 and 6 is displayed
# User can type exit to quit the game
# Use a while loop and random.randint()


import random

while True:
    choice=str(input("Do you want to roll or exit? "))
    if choice.lower()=="roll":
        print(f"Dice rolled {random.randint(1,6)}")
    elif choice.lower()=="exit":
        print("Game ended")
        break
    elif choice.lower() not in ["roll","exit"]:
        print("Please enter a valid choice")
