contacts = {}

def add_contact():
    name = input("Enter name: ")
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = [phone, email, address]
    print("Contact added!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, details in contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {details[0]}")
            print(f"Email: {details[1]}")
            print(f"Address: {details[2]}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        details = contacts[name]
        print(f"\nName: {name}")
        print(f"Phone: {details[0]}")
        print(f"Email: {details[1]}")
        print(f"Address: {details[2]}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("New phone (leave blank to keep same): ")
        email = input("New email (leave blank to keep same): ")
        address = input("New address (leave blank to keep same): ")
        if phone:
            contacts[name][0] = phone
        if email:
            contacts[name][1] = email
        if address:
            contacts[name][2] = address
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def menu():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add")
        print("2. View All")
        print("3. Search")
        print("4. Update")
        print("5. Delete")
        print("6. Exit")

        choice = input("Choose (1-6): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


menu()
