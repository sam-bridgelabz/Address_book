from contact import Contact
from address_book import AddressBook

class AddressBookMain:
    def __init__(self):
        print("Welcome to Address Book")
        self.address_book = AddressBook()

    def add_contact(self):
        new_contact = Contact()
        self.address_book.add_contact(new_contact)

    def display_contacts(self):
        self.address_book.display_contacts()

    def edit_contact(self):
        name = input("Enter the first or last name of the contact to edit: ")
        self.address_book.edit_contact(name)

    def delete_contact(self):
        name = input("Enter the first or last name of the contact to delete: ")
        self.address_book.delete_contact(name)

if __name__ == "__main__":
    address_book = AddressBookMain()

    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("4. Delete Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            address_book.add_contact()
        elif choice == "2":
            address_book.display_contacts()
        elif choice == "3":
            address_book.edit_contact()
        elif choice == "4":
            address_book.delete_contact()
        elif choice == "5":
            print("Exiting Address Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
