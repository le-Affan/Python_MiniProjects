import datetime as dt


def mark():
    name = input("Enter Your Name: ")
    date_and_time = dt.datetime.now()
    last_time = dt.time(8, 59, 59)
    late_mark = False

    if date_and_time.time() > last_time:
        print("You are late for the class!")
        late_mark = True

    with open("attendance_logs.txt", "a") as file:
        if late_mark == False:
            file.write(f"{name}-{date_and_time}\n")
            print("Attendance Marked Successfully")
        elif late_mark == True:
            file.write(f"{name}-{date_and_time} (LATE)\n")
            print("Attendance Marked Successfully")




def view_logs():
    with open("attendance_logs.txt", "r") as file:
        entries=file.readlines()

        for entry in entries:
            print(entry.strip())


