# Display a menu to:
# Add a contact
# View all contacts
# Search for a contact
# Delete a contact
# Exit

contact_book={}

while True:
    choice = input("Select your choice (a:Add Contact b:View Contacts c:Search Contact d:Delete Contact e:Exit)")

    if choice=="a":
        n=int(input("How many contacts do you want to add? "))
        i=0
        while i<n:
            name=input("Enter Contact Name: ")
            number=input("Enter Contact Number: ")
            contact_book[name]=number
            i+=1

    elif choice=="b":
        print(contact_book)

    elif choice=="c":
        name = input("Enter Contact Name: ")
        if name in contact_book:
            print (contact_book[name])
        else:
            print("Name not in contact book")

    elif choice=="d":
        name = input("Enter Contact Name: ")
        if name in contact_book:
            del contact_book[name]
            print("Contact successfully deleted")
        else:
            print("Name not in contact book")

    elif choice.lower()=="e":
        break

print("Have a great day!")




