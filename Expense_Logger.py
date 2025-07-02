def add_expense():
    n=int(input("Enter the number of expenses you want to log: "))
    i=0
    with open("expenses.txt","w") as file:

        while i<n:
            description=input("Enter expense description: ")
            try:
                amount=int(input("Enter the amount spent: "))
                file.write(f"{description} - Rs.{amount}\n")
                i+=1
            except ValueError:
                print("Invalid amount. Please enter a number.")

    with open("expenses.txt","r") as read_file:
        content=read_file.read()
        print(content)

add_expense()
