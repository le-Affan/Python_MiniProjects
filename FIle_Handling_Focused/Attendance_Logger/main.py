# Build a console-based Attendance Logger where a user can:
# Mark attendance (with current date and time)
# View attendance log
# Exit the program

# Requirements:
# Use the datetime module to get the current date and time.
# Save attendance logs in a text file (e.g., attendance.txt).
# Each attendance entry should look like: Affan - 06/07/2025 17:45:32
# Create functions inside a separate module file to handle:
# Marking attendance
# Viewing attendance log

import datetime as dt
import attendance_module as am

while True:
    print("\nWelcome to class\n"
          "\nWhat would you like to do today?\n"
          "\n1.Mark Attendance\n"
          "2.View Attendance Logs\n"
          "3.Exit")

    try:
        choice=int(input("\nPlease Enter You Choice: "))
        if choice not in [1,2,3]:
            print("Please Enter A Valid Choice.")
            continue
    except ValueError:
        print("Please Enter A Valid Choice.")
        continue

    if choice==1:
        am.mark()

    if choice==2:
        am.view_logs()

    if choice==3:
        print("Have A Great Day!")
        break
