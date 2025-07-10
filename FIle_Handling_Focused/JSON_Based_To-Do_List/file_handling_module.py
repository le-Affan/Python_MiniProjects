import json
import os

def load_data():
    if not os.path.exists("todo.json"):
        with open("todo.json", "w") as file:
            json.dump({}, file)

    with open("todo.json", "r") as file:
        return json.load(file)

def save_data(data):
    with open("todo.json",'w') as file:
        json.dump(data,file,indent=2)

def add_task():
    tasks=load_data()

    n=int(input("How many tasks do you want to add? "))
    i=1

    while i<=n:

        task_num=str(len(tasks)+1)
        task_desc=input("Enter Task Description: ")

        while True:
            task_status = input("Is the task completed? (Yes or No) ").lower()
            if task_status not in ['yes','no']:
                print('Please Enter Valid Answer')
                continue
            else:
                break
        i+=1

        tasks[task_num]=f"{task_desc} : {'Completed' if task_status=='yes' else 'Incomplete'}"

    save_data(tasks)

def view_task():
    tasks=load_data()

    if not tasks:
        print("No Tasks Added")
    else:
        for i in tasks:
            print(f"{i}:{tasks[i]}\n")

def mark_complete():
    tasks=load_data()

    while True:
        task_num=input("Enter Task Number for the task you want to mark as completed: ")

        if task_num in tasks and 'Incomplete' in tasks[task_num]:
            comp_task=str(tasks[task_num])
            tasks[task_num]=comp_task.replace('Incomplete','Completed')
            break

        else:
            print("Task doesn't exist")
            continue

    save_data(tasks)


def delete_task():
    tasks=load_data()

    while True:
        task_num = input("Enter Task Number for the task you want to delete: ")

        if task_num in tasks:
            del tasks[task_num]
            break
        else:
            print("Task doesn't exist")
            continue







