# Objective:
# Create a program that manages a to-do list for the user.
# The to-do list will be stored in a JSON file named todo.json. Each task will have:
# A unique task number (key)
# A task description
# A completion status (True or False)
# The program should allow the user to:
# Add a new task
# View all tasks
# Mark a task as completed
# Delete a task
# Exit the program
# The program should handle missing files gracefully and create a new JSON file if none exists.

import json
import os
import file_handling_module as fh

while True:
    print("\nWhat would you like 'To-Do' today? ;)")
    print("1.Add Task\n"
          "2.View All Tasks\n"
          "3.Mark Task as Complete\n"
          "4.Delete a Task\n"
          "5.Exit")

    while True:
        try:
            choice=int(input("Enter Your Choice: "))
            assert choice in [1,2,3,4,5]

        except (ValueError,AssertionError):
            print("Please enter a valid choice")
            continue

        else:
            if choice == 1:
                fh.add_task()

            elif choice == 2:
                fh.view_task()

            elif choice == 3:
                fh.mark_complete()

            elif choice == 4:
                fh.delete_task()

            elif choice == 5:
                print("Have a great day!")
                break

    break






