from contact import Contact
from address_book import AddressBook

class AddressBookMain:
    def __init__(self):
        print("============= Welcome to Address Book ====================")
        self.address_book_dir = {}

    def add_addressbook(self):
        add_book_name = input("-->> Enter name of address book: ")
        if add_book_name in self.address_book_dir:
            print(f"-->> Address book with name {add_book_name} already present <<--")
        else:
            self.address_book_dir[add_book_name]=AddressBook()
            print(f"-->> Address book with name {add_book_name} created <<--")

    def display_add_book(self):
        print("***********************************************************")
        for name,value in self.address_book_dir.items():
            print("\n------------------------------------------------------")
            print(f"Address Book Name:{name}")
            for contact_obj in value.contacts:
                print(f"Content: {contact_obj} \n")
            print("------------------------------------------------------\n")
        print("***********************************************************")

    def add_contact(self):
        add_book_name = input("-->> Enter name of address book: ")
        new_contact = Contact()
        try:
            add_book = self.address_book_dir.get(add_book_name)
            add_book.add_contact(new_contact)
        except Exception as e:
            print(f"Address Book: {add_book_name} not found...")

    def add_multiple_contacts(self):
        add_book_name = input("--> Enter name of address book: ")
        try:
            address_book = self.address_book_dir.get(add_book_name)
            address_book.add_multiple_contacts()
        except Exception as e:
            print(f"Address Book: {add_book_name} not found...")

    def display_contacts(self):
        add_book_name = input("--> Enter name of address book: ")
        try:
            address_book = self.address_book_dir.get(add_book_name)
            address_book.display_contacts()
        except Exception as e:
            print(f"Address Book: {add_book_name} not found...")

    def edit_contact(self):
        add_book_name = input("--> Enter name of address book: ")
        try:
            address_book = self.address_book_dir.get(add_book_name)
            name = input("-->> Enter the first or last name of the contact to edit: ")
            address_book.edit_contact(name)
        except Exception as e:
            print(f"Address Book: {add_book_name} not found...")

    def delete_contact(self):
        add_book_name = input("--> Enter name of address book: ")
        try:
            address_book = self.address_book_dir.get(add_book_name)
            name = input("-->> Enter the first or last name of the contact to delete: <<--")
            address_book.delete_contact(name)
        except Exception as e:
            print(f"Address Book: {add_book_name} not found...")

if __name__ == "__main__":
    address_book_main = AddressBookMain()

    while True:
        print("\n-->> Options: <<--")
        print("0. Add Address Book")
        print("1. Display AddressBook")
        print("2. Add Contact")
        print("3. Add Multiple Contacts")
        print("4. Display Contacts")
        print("5. Edit Contact")
        print("6. Delete Contact")
        print("7. Exit")

        choice = input("-->> Enter your choice: ")

        if choice == "0":
            address_book_main.add_addressbook()
        elif choice == "1":
            address_book_main.display_add_book()
        elif choice == "2":
            address_book_main.add_contact()
        elif choice == "3":
            address_book_main.add_multiple_contacts()
        elif choice == "4":
            address_book_main.display_contacts()
        elif choice == "5":
            address_book_main.edit_contact()
        elif choice == "6":
            address_book_main.delete_contact()
        elif choice == "7":
            print(" == Exiting Address Book. Goodbye! ==")
            break
        else:
            print("== Invalid choice. Please try again. ==")
