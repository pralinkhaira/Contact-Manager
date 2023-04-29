import csv
import os

CONTACTS_FILE = 'contacts.csv'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_contacts():
    with open(CONTACTS_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def write_contacts(contacts):
    with open(CONTACTS_FILE, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['name', 'phone', 'email'])
        writer.writeheader()
        writer.writerows(contacts)

def display_contacts(contacts):
    if len(contacts) == 0:
        print('No contacts found.')
    else:
        for contact in contacts:
            print(f"{contact['name']} - {contact['phone']} - {contact['email']}")

def add_contact():
    name = input('Enter name: ')
    phone = input('Enter phone: ')
    email = input('Enter email: ')

    contacts = read_contacts()
    contacts.append({'name': name, 'phone': phone, 'email': email})
    write_contacts(contacts)

    print('Contact added successfully.')

def delete_contact():
    name = input('Enter name: ')

    contacts = read_contacts()
    contacts = [contact for contact in contacts if contact['name'] != name]
    write_contacts(contacts)

    print('Contact deleted successfully.')

def search_contact():
    query = input('Enter search query: ')

    contacts = read_contacts()
    matches = [contact for contact in contacts if query in contact['name'] or query in contact['phone'] or query in contact['email']]
    display_contacts(matches)

def show_menu():
    print('1. Add Contact')
    print('2. Delete Contact')
    print('3. Search Contact')
    print('4. Quit')

while True:
    clear_screen()
    print('Contact Manager\n')
    show_menu()

    choice = input('Enter choice: ')
    if choice == '1':
        add_contact()
    elif choice == '2':
        delete_contact()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        break
    else:
        print('Invalid choice. Please try again.')

print('Goodbye!')
