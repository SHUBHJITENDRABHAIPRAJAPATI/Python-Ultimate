"""
Contact Book
============
A simple contact management system.
"""

class ContactBook:
    """Manage contacts with name, phone, and email."""
    
    def __init__(self):
        """Initialize empty contact book."""
        self.contacts = {}
    
    def add_contact(self, name, phone, email):
        """Add a new contact."""
        self.contacts[name] = {
            "phone": phone,
            "email": email
        }
        print(f"✓ Contact added: {name}")
    
    def view_all_contacts(self):
        """Display all contacts."""
        if not self.contacts:
            print("\nNo contacts in your book!")
            return
        
        print("\n" + "=" * 50)
        print("Contact Book")
        print("=" * 50)
        for name, info in self.contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print("-" * 50)
    
    def search_contact(self, name):
        """Search for a contact by name."""
        if name in self.contacts:
            info = self.contacts[name]
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
        else:
            print(f"Contact '{name}' not found!")
    
    def delete_contact(self, name):
        """Delete a contact."""
        if name in self.contacts:
            del self.contacts[name]
            print(f"✓ Contact deleted: {name}")
        else:
            print(f"Contact '{name}' not found!")
    
    def update_contact(self, name, phone=None, email=None):
        """Update contact information."""
        if name in self.contacts:
            if phone:
                self.contacts[name]["phone"] = phone
            if email:
                self.contacts[name]["email"] = email
            print(f"✓ Contact updated: {name}")
        else:
            print(f"Contact '{name}' not found!")

def main():
    """Main function to run the contact book."""
    book = ContactBook()
    
    print("=" * 50)
    print("Contact Book Manager")
    print("=" * 50)
    
    while True:
        print("\n1. Add contact")
        print("2. View all contacts")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            book.add_contact(name, phone, email)
        
        elif choice == '2':
            book.view_all_contacts()
        
        elif choice == '3':
            name = input("Enter name to search: ")
            book.search_contact(name)
        
        elif choice == '4':
            name = input("Enter name to update: ")
            phone = input("Enter new phone (press Enter to skip): ")
            email = input("Enter new email (press Enter to skip): ")
            book.update_contact(
                name,
                phone if phone else None,
                email if email else None
            )
        
        elif choice == '5':
            name = input("Enter name to delete: ")
            book.delete_contact(name)
        
        elif choice == '6':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select 1-6.")

if __name__ == "__main__":
    main()
