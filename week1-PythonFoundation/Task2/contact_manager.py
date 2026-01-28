"""
File-Based Contact Manager
Store and manage contacts in a text file
"""

import json
from utils import validate_email, validate_phone, format_phone, capitalize_name, confirm_action

CONTACTS_FILE = "contacts.json"


def load_contacts():
    """Load contacts from file, return empty list if file doesn't exist"""
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(" No contacts file found. Starting fresh!")
        return []
    except json.JSONDecodeError:
        print(" Contacts file is corrupted. Starting fresh!")
        return []
    except Exception as e:
        print(f" Error loading contacts: {e}")
        return []


def save_contacts(contacts):
    """Save contacts to file"""
    try:
        with open(CONTACTS_FILE, "w") as file:
            json.dump(contacts, file, indent=4)
        print("Contacts saved successfully!")
        return True
    except Exception as e:
        print(f" Error saving contacts: {e}")
        return False


def add_contact(contacts):
    """Add a new contact"""
    print("\n--- Add New Contact ---")
    
    # Get name
    name = input("Enter name: ").strip()
    if not name:
        print(" Name cannot be empty!")
        return
    name = capitalize_name(name)
    
    # Get phone
    while True:
        phone = input("Enter phone number: ").strip()
        if validate_phone(phone):
            phone = format_phone(phone)
            break
        else:
            print(" Invalid phone number! Use format: 123-456-7890")
    
    # Get email
    while True:
        email = input("Enter email: ").strip().lower()
        if validate_email(email):
            break
        else:
            print(" Invalid email! Must contain @ and domain")
    
    # Optional address
    address = input("Enter address (optional): ").strip()
    
    # Create contact dictionary
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    
    contacts.append(contact)
    print(f" Contact '{name}' added successfully!")


def display_contacts(contacts):
    """Display all contacts"""
    if not contacts:
        print("\nNo contacts found!")
        return
    
    print("\n" + "=" * 70)
    print(f"{'Name':<20} {'Phone':<18} {'Email':<25}")
    print("=" * 70)
    
    for contact in contacts:
        print(f"{contact['name']:<20} {contact['phone']:<18} {contact['email']:<25}")
    
    print("=" * 70)
    print(f"Total contacts: {len(contacts)}")


def search_contact(contacts):
    """Search for a contact by name"""
    if not contacts:
        print("\n No contacts to search!")
        return
    
    search_term = input("\nEnter name to search: ").strip().lower()
    
    found_contacts = [c for c in contacts if search_term in c['name'].lower()]
    
    if not found_contacts:
        print(f"No contacts found matching '{search_term}'")
        return
    
    print(f"\n Found {len(found_contacts)} contact(s):")
    print("=" * 70)
    
    for i, contact in enumerate(found_contacts, 1):
        print(f"\n{i}. {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        if contact['address']:
            print(f"   Address: {contact['address']}")


def update_contact(contacts):
    """Update an existing contact"""
    if not contacts:
        print("\n📭 No contacts to update!")
        return
    
    search_term = input("\nEnter name of contact to update: ").strip().lower()
    
    found_indices = [i for i, c in enumerate(contacts) if search_term in c['name'].lower()]
    
    if not found_indices:
        print(f" No contacts found matching '{search_term}'")
        return
    
    if len(found_indices) > 1:
        print("\nMultiple contacts found:")
        for i in found_indices:
            print(f"{i + 1}. {contacts[i]['name']} - {contacts[i]['phone']}")
        
        index = int(input("Enter the number of contact to update: ")) - 1
    else:
        index = found_indices[0]
    
    contact = contacts[index]
    print(f"\nUpdating: {contact['name']}")
    print("(Press Enter to keep current value)")
    
    # Update name
    new_name = input(f"Name [{contact['name']}]: ").strip()
    if new_name:
        contact['name'] = capitalize_name(new_name)
    
    # Update phone
    new_phone = input(f"Phone [{contact['phone']}]: ").strip()
    if new_phone and validate_phone(new_phone):
        contact['phone'] = format_phone(new_phone)
    
    # Update email
    new_email = input(f"Email [{contact['email']}]: ").strip().lower()
    if new_email and validate_email(new_email):
        contact['email'] = new_email
    
    # Update address
    new_address = input(f"Address [{contact.get('address', '')}]: ").strip()
    if new_address:
        contact['address'] = new_address
    
    print("Contact updated successfully!")


def delete_contact(contacts):
    """Delete a contact"""
    if not contacts:
        print("\n📭 No contacts to delete!")
        return
    
    search_term = input("\nEnter name of contact to delete: ").strip().lower()
    
    found_indices = [i for i, c in enumerate(contacts) if search_term in c['name'].lower()]
    
    if not found_indices:
        print(f" No contacts found matching '{search_term}'")
        return
    
    if len(found_indices) > 1:
        print("\nMultiple contacts found:")
        for i in found_indices:
            print(f"{i + 1}. {contacts[i]['name']} - {contacts[i]['phone']}")
        
        index = int(input("Enter the number of contact to delete: ")) - 1
    else:
        index = found_indices[0]
    
    contact = contacts[index]
    
    if confirm_action(f"Delete '{contact['name']}'?"):
        contacts.pop(index)
        print(" Contact deleted successfully!")
    else:
        print("Deletion cancelled")


def main():
    """Main function to run contact manager"""
    contacts = load_contacts()
    
    while True:
        print("\n" + "=" * 50)
        print("   CONTACT MANAGER")
        print("=" * 50)
        print("  1. Add Contact")
        print("  2. View All Contacts")
        print("  3. Search Contact")
        print("  4. Update Contact")
        print("  5. Delete Contact")
        print("  6. Save & Exit")
        print("=" * 50)
        
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == "1":
                add_contact(contacts)
            elif choice == "2":
                display_contacts(contacts)
            elif choice == "3":
                search_contact(contacts)
            elif choice == "4":
                update_contact(contacts)
            elif choice == "5":
                delete_contact(contacts)
            elif choice == "6":
                save_contacts(contacts)
                print("\n👋 Goodbye!")
                break
            else:
                print("Invalid choice! Please enter 1-6")
        
        except KeyboardInterrupt:
            print("\n\n Interrupted! Saving contacts...")
            save_contacts(contacts)
            break
        except Exception as e:
            print(f" An error occurred: {e}")


if __name__ == "__main__":
    main()