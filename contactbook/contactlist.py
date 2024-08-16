#python contact book with 
# contact information, 
# add contact, 
# view contact list,
# search contact , 
# update contact, 
# delete contact, 
# user interface

contact = {}


def display_contact():
    print("Name : \t\tContact Number : ")
    for key in contact :
        print("{}\t\t{}".format(key,contact.get(key)))


while True :
    choice = int(input("  1.Add new contact \n 2.Search contact \n 3.Display contact list \n 4.Update contact \n 5.Delete contact  \n 6.Exit \n Enter your choice :  "))
    if choice == 1 :   # adding new contact
        name = input("Enter the contact name : ")
        phone = input("Enter the phone number : ")
        contact[name] = phone

    elif choice == 2 :    # searching for a contact
        search_name = input("Search the contact name : ")
        if search_name in contact :
            print(search_name, "'s contact number is : ", contact[search_name])

        else:
            print("Name not found!")

    elif choice == 3 :    #display contact list
        if not contact :
            print("Empty Contact Book.")
        else:
             display_contact()  # called display_contact functon.
   
    elif choice == 4 :   # udpating  a contact
        update_contact = input("Enter the contact to be edited : ")
        if update_contact in contact :
            phone = input("Enter the phone number : ")
            contact[update_contact] = phone
            print("Contact Updated!")
        else:
            print("Name not found!")

    elif choice == 5 :  # deleting a contact 
        delete_contact = input("Enter the contact to be deleted : ")
        if delete_contact in contact:
            confirm = input("Do you want to delete this contact? yes/no ? ")
            if confirm == "yes" or confirm == "Yes":
                contact.pop(delete_contact)
            display_contact()

        else:
            print("Name not found!")

    else:
        break
