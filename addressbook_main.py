from contact import Contact

class AddressBookMain:
    def __init__(self):
        print("Welcome to Address Book")
        self.contacts = []

    def add_contact_to_add_book(self):
        new_contact = Contact()
        self.contacts.append(new_contact)
        print("Contact added successfully!")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts in the address book.")
        else:
            for contact in self.contacts:
                print(contact)

if __name__ == "__main__":
    address_book = AddressBookMain()

    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            address_book.add_contact_to_add_book()
        elif choice == "2":
            address_book.display_contacts()
        elif choice == "3":
            print("Exiting Address Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
