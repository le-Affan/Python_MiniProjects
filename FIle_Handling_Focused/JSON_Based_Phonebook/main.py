# Requirements:
# Add new contacts with details: Name, Phone Number, Email, and Address.
# View all saved contacts.
# Search for a contact by name.
# Update contact details.
# Delete a contact by name.
# Store and retrieve contact data from a JSON file.

#IMPORTANT NOTE: I am assuming the user enters valid input whenever asked for this program

import json
import phonebook_functions as pf

while True:
    choice=int(input("""What would you like to do today? 
    1.Add new contact
    2.View all contacts
    3.Search Contact
    4.Update a contact
    5.Delete Contact
    6.Exit"""))

    if choice==1:
        pf.add_contact()
    elif choice==2:
        pf.view()
    elif choice==3:
        data=pf.load()
        contact_name=pf.search()
        if not contact_name:
            print("No Contact Found")
        else:
            print(data[contact_name])
    elif choice==4:
        pf.update()
    elif choice==5:
        pf.delete()
    elif choice==6:
        print("Have a great day")
        break
