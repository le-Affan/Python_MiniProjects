"""
Bank Account Simulator (Console-based)
--------------------------------------

A console-based bank account management system built using Python
Object-Oriented Programming (OOP) concepts.

Project Purpose:
This project was created to practice and demonstrate the core working of OOP in Python:
- Creating classes and objects
- Class and instance variables
- Instance methods
- List of objects (accounts)
- Basic user-driven menu interfaces

Features:
- Create multiple bank accounts with unique account numbers
- Deposit and withdraw money into/from a selected account
- Check account balance
- Display account holder details
- Display total number of accounts created

Important Note:
This project intentionally **does not handle all edge cases or banking technicalities**
(like preventing overdrafts, ensuring valid deposit amounts, etc.) because the focus
was to build familiarity with **OOP structure and object interactions** in Python,
not to develop a production-grade banking system.

Author: Affan Shaikh
Date: July 2025
"""


class BankAccount:
    account_count = 0
    account_number_seed = 1000

    def __init__(self, name, balance):
        BankAccount.account_number_seed += 1
        BankAccount.account_count += 1

        self.name = name
        self.account_number = BankAccount.account_number_seed
        self.balance = balance

    def deposit(self):
        dep_amt = int(input("Enter the deposit amount: "))
        self.balance = self.balance + dep_amt
        print(f"Rs.{dep_amt} was deposited successfully!")

    def withdrawal(self):
        with_amt = int(input("Enter the withdrawal amount: "))
        self.balance = self.balance - with_amt
        print(f"Rs.{with_amt} was withdraw successfully!")

    def check_balance(self):
        print(f"Your current balance is Rs.{self.balance}")

    def details(self):
        print(f"Account Holder's Name:{self.name}")
        print(f"Account Number:{self.account_number}")


accounts = []

while True:
    print("Welcome to the bank system")
    print("What would you like to do today?")
    print("1. Create New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Show Account Details")
    print("6. Show Total Accounts")
    print("7. Exit")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        name = input("Enter Account Holder's Name: ")
        while True:
            try:
                balance = int(input("Enter initial deposit amount (Minimum Rs.10,000): "))
                if balance < 10000:
                    print("Minimum Rs.10,000 required.")
                    continue
                break
            except ValueError:
                print("Please enter a valid amount.")

        account = BankAccount(name, balance)
        accounts.append(account)
        print(f"Congratulations on creating a new account. You account number is {account.account_number}")

    elif choice in [2, 3, 4, 5]:
        if len(accounts) == 0:
            print("You do not have an account with the bank")
            continue

        selected_acc = int(input("Enter your account number: "))
        found_acc = None

        for i in accounts:
            if i.account_number == selected_acc:
                found_acc = i

        if found_acc is None:
            print("Account Not Found.")
            continue

    if choice == 2:
        found_acc.deposit()

    elif choice == 3:
        found_acc.withdrawal()

    elif choice == 4:
        found_acc.check_balance()

    elif choice == 5:
        found_acc.details()

    elif choice == 6:
        print(f"You have a total of {len(accounts)} accounts with our bank")

    elif choice == 7:
        print("Thank You for banking with us")
        break
