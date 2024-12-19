class Contact:
    def __init__(self):
        self.first_name = input("Enter First Name: ")
        self.last_name = input("Enter Last Name: ")
        self.address = input("Enter Address: ")
        self.city = input("Enter City: ")
        self.state = input("Enter State: ")
        self.zip_code = input("Enter Zip Code: ")
        self.phone_number = input("Enter Phone Number: ")
        self.email = input("Enter Email: ")

    def __str__(self):
        return (f"Name: {self.first_name} {self.last_name}\n"
                f"Address: {self.address}, {self.city}, {self.state} - {self.zip_code}\n"
                f"Phone: {self.phone_number}, Email: {self.email}")
