class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts in the address book.")
        else:
            for contact in self.contacts:
                print(contact)

    def edit_contact(self, name):
        for contact in self.contacts:
            if contact.first_name.lower() == name.lower() or contact.last_name.lower() == name.lower():
                print("Contact found. Please enter new details:")
                contact.first_name = input("Enter First Name: ")
                contact.last_name = input("Enter Last Name: ")
                contact.address = input("Enter Address: ")
                contact.city = input("Enter City: ")
                contact.state = input("Enter State: ")
                contact.zip_code = input("Enter Zip Code: ")
                contact.phone_number = input("Enter Phone Number: ")
                contact.email = input("Enter Email: ")
                print("Contact updated successfully!")
                return
        print("Contact not found.")
