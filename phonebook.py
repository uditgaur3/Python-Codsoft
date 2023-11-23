class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("Phonebook is empty.")
        else:
            print("Contacts:")
            for name, phone_number in self.contacts.items():
                print(f"{name}: {phone_number}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Contact: {name}, Phone Number: {self.contacts[name]}")
        else:
            print(f"Contact '{name}' not found.")

def phonebook_app():
    phonebook = PhoneBook()

    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Quit")

        choice = input("Enter choice (1-4): ")

        if choice == '1':
            name = input("Enter the name: ")
            phone_number = input("Enter the phone number: ")
            phonebook.add_contact(name, phone_number)
        elif choice == '2':
            phonebook.view_contacts()
        elif choice == '3':
            name = input("Enter the name to search: ")
            phonebook.search_contact(name)
        elif choice == '4':
            print("Exiting phonebook application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    phonebook_app()
