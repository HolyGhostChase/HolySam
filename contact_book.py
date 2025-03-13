# Contact Book

contacts = {}  # Empty dictionary to store contacts

def add_contact():
    """Add a new contact"""
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(f"Contact {name} added!")

def view_contacts():
    """View all contacts"""
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def delete_contact():
    """Delete a contact"""
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Deleted contact {name}")
    else:
        print("Contact not found.")

while True:
    print("\nOptions:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Quit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")
