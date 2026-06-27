import sys

def show_menu():
    print("\n==================================================")
    print("               CODSOFT CENTRAL CONTACT BOOK       ")
    print("==================================================")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact Details")
    print("5. Delete Contact Record")
    print("6. Exit Database Application")
    print("--------------------------------------------------")

def add_contact(contacts):
    print("\n--- ENTER NEW CONTACT DETAILS ---")
    name = input("Name: ").strip()
    if not name:
        print("Error: Name entry cannot be blank.")
        return
    
    phone = input("Phone Number: ").strip()
    email = input("Email Address: ").strip()
    address = input("Physical Address: ").strip()
    
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"Success! '{name}' has been added to your records.")

def view_contacts(contacts):
    if not contacts:
        print("\nYour Contact Book database is completely empty!")
        return
    
    print("\nSAVED CONTACTS LIST:")
    print(f"{'Name':<20} | {'Phone Number':<15}")
    print("-" * 40)
    for name, details in contacts.items():
        print(f"{name:<20} | {details['phone']:<15}")

def search_contact(contacts):
    if not contacts:
        print("\nDatabase empty. Nothing to search.")
        return
        
    query = input("\nEnter name or phone number to search: ").strip().lower()
    found = False
    
    print("\nSEARCH RESULTS:")
    for name, details in contacts.items():
        if query in name.lower() or query in details['phone']:
            print("-" * 30)
            print(f"Name:    {name}")
            print(f"Phone:   {details['phone']}")
            print(f"Email:   {details['email']}")
            print(f"Address: {details['address']}")
            found = True
            
    if not found:
        print("No matching records found in the system database.")

def update_contact(contacts):
    if not contacts:
        print("\nDatabase empty. Nothing to update.")
        return
        
    name = input("\nEnter the exact name of the contact to update: ").strip()
    if name in contacts:
        print(f"\nModifying data for '{name}'. Leave blank to keep current values.")
        
        new_phone = input(f"New Phone [{contacts[name]['phone']}]: ").strip()
        new_email = input(f"New Email [{contacts[name]['email']}]: ").strip()
        new_address = input(f"New Address [{contacts[name]['address']}]: ").strip()
        
        if new_phone: contacts[name]['phone'] = new_phone
        if new_email: contacts[name]['email'] = new_email
        if new_address: contacts[name]['address'] = new_address
        
        print(f"Success! Records updated for '{name}'.")
    else:
        print("Error: Contact name not found.")

def delete_contact(contacts):
    if not contacts:
        print("\nDatabase empty. Nothing to delete.")
        return
        
    name = input("\nEnter the exact name of the contact to delete: ").strip()
    if name in contacts:
        contacts.pop(name)
        print(f"Success! '{name}' has been scrubbed from the database.")
    else:
        print("Error: Contact name not found.")

def main():
    # Structural database dictionary mapping
    contacts = {}
    
    while True:
        try:
            show_menu()
            choice = input("Select an option (1-6): ").strip()
            
            if choice == '1':
                add_contact(contacts)
            elif choice == '2':
                view_contacts(contacts)
            elif choice == '3':
                search_contact(contacts)
            elif choice == '4':
                update_contact(contacts)
            elif choice == '5':
                delete_contact(contacts)
            elif choice == '6':
                print("\nExiting Contact Book. Records cleared from transient memory. Goodbye!")
                break
            else:
                print("Error: Invalid selection option. Please choose from 1 to 6.")
            print("==================================================")
            
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break

if __name__ == "__main__":
    main()