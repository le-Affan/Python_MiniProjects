import json
import os


def load():
    if not os.path.exists("phonebook.json"):
        with open('phonebook.json', 'w') as file:
            json.dump({}, file)
    with open('phonebook.json', 'r') as file:
        return json.load(file)


def save(updated_data):
    with open('phonebook.json', 'w') as file:
        json.dump(updated_data, file, indent=2)


def add_contact():
    data = load()

    contact_key = input("Enter new contact name: ").capitalize()
    phone = input(f"Enter {contact_key}'s phone number: ")
    email = input(f"Enter {contact_key}'s email address: ")
    address = input(f"Enter {contact_key}'s address: ")

    details = {'Phone': phone, 'Email': email, 'Address': address}
    data[contact_key] = details

    save(data)


def view():
    data = load()

    if not data:
        print("No Contacts Added")
    else:
        for i in data:
            print(f"{i}:{data[i]}\n")


def search():
    data=load()

    search_key=input("Enter name of the contact you are looking for: ").capitalize()

    if search_key in data:
        return search_key
    else:
        print(f"No contact named '{search_key}' found in phone book")

def update():
    data=load()

    goal_contact=search()
    if not goal_contact:
        print("Contact you are looking for not found in the phonebook")
        return

    choice=int(input("""What do you want to update?
    1.Contact Name
    2.Phone Number
    3.Email ID
    4.Address
    """))

    if choice==1:
        new_key=input("Enter new contact name: ")
        data[new_key]=data[goal_contact]
        del data[goal_contact]

    elif choice==2:
        new_num=input("Enter new phone number: ")
        data[goal_contact]['Phone']=new_num

    elif choice==3:
        new_email=input("Enter new email address: ")
        data[goal_contact]['Email']=new_email

    elif choice==4:
        new_address=input("Enter new address: ")
        data[goal_contact]['Address']=new_address

    save(data)

def delete():
    data=load()

    goal_contact=search()
    if not goal_contact:
        print("Contact you are looking for not found in the phonebook")
        return

    del data[goal_contact]

    save(data)
