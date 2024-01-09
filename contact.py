class ContactManagementSystem:
    def _init_(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email):
        contact = {
            'Name': name,
            'Phone Number': phone_number,
            'Email': email
        }
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contact List:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"Contact {index}:")
                for key, value in contact.items():
                    print(f"{key}: {value}")
                print()

    def edit_contact(self, index, name, phone_number, email):
        if index >= 1 and index <= len(self.contacts):
            contact = {
                'Name': name,
                'Phone Number': phone_number,
                'Email': email
            }
            self.contacts[index - 1] = contact
            print("Contact edited successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if index >= 1 and index <= len(self.contacts):
            del self.contacts[index - 1]
            print("Contact deleted successfully.")
        else:
            print("Invalid contact index.")

# Example usage
contact_manager = ContactManagementSystem()

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")
   
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        contact_manager.add_contact(name, phone, email)
    elif choice == '2':
        contact_manager.view_contacts()
    elif choice == '3':
        index = int(input("Enter the index of contact to edit: "))
        name = input("Enter new name: ")
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contact_manager.edit_contact(index, name, phone, email)
    elif choice == '4':
        index = int(input("Enter the index of contact to delete: "))
        contact_manager.delete_contact(index)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please choose between 1-5.")