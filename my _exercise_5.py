phone_book = {}


def add_new_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    phone_book[name] = number
    print(f"Contact {name} added successfully!")


def edit_contact():
    name = input("Enter contact name to edit: ")
    if name in phone_book:
        print(f"Contact found: {name} - {phone_book[name]}")
        choice = input("Enter 'U' to update or 'D' to delete: ").upper()
        if choice == 'U':
            new_number = input("Enter new number: ")
            phone_book[name] = new_number
            print(f"{name}'s number updated successfully!")
        elif choice == 'D':
            del phone_book[name]
            print(f"{name} deleted from contacts.")
        else:
            print("Invalid choice!")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in phone_book:
        del phone_book[name]
        print(f"{name} deleted from contacts.")
    else:
        print("Contact not found.")


def search_contact():
    name = input("Enter contact name to search: ")
    if name in phone_book:
        print(f"Contact found: {name} - {phone_book[name]}")
    else:
        print("Contact not found.")

# i define here my main loop:


while True:
    print("\nPhone Book Menu:")
    print("1. Add New Contact")
    print("2. Edit Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_new_contact()
    elif choice == '2':
        edit_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        search_contact()
    elif choice == '5':
        print("Exiting phone book.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
