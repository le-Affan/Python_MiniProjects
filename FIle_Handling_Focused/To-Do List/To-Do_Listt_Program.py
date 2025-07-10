# Requirements:
# User can add tasks
# User can view all tasks
# (Bonus) User can delete a task
# Save tasks to a todo.txt file
# Clean exit option
# Use file handling and exception handling

while True:

    choice = input("Enter your choice: 1-Add Task 2-View All Tasks 3-Delete a task 4-Exit ")

    if choice not in ["1", '2', '3', '4']:
        print("Please enter a valid choice")
        continue  #added to send control back to the start of the loop and avoid the rest of the code running unnessarily

    if choice == '1':
        task = input("What task do you want to add? ")
        with open("todo.txt", "a") as file:
            file.write(task + "\n")  #\n ensures all new tasks add to a new line

    elif choice == '2':
        with open("todo.txt", "r") as file:
            for line in file:
                print(line.strip())

    elif choice == '3':
        task = input("What task do you want to delete? ")
        with open("todo.txt", "r") as file:
            all_tasks = file.readlines()
            if task + "\n" in all_tasks:
                all_tasks.remove(task + "\n")
                with open("todo.txt", "w") as new_file:  #rewriting the file content without the deleted task
                    new_file.writelines(all_tasks)
            else:
                print("The task you want to delete does not exist in your To-Do List")

    elif choice == '4':
        print("Thank You, Have a Great Day")
        break
