# Contact Manager

This is a command-line interface (CLI) application for managing contacts. It allows users to add, delete, and search for contacts using a CSV file as a storage backend.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/PralinKhaira/Contact-Manager.git
   ```

2. Install Python 3 if you haven't already. You can download it from the official website: https://www.python.org/downloads/

3. Navigate to the `contact-manager` directory and install the required packages:

   ```
   cd contact-manager
   pip install -r requirements.txt
   ```

4. Run the application:

   ```
   python contact_manager.py
   ```

## Usage

To use the application, simply run the `contact_manager.py` script in your terminal:

```
python contact_manager.py
```

You will be presented with a menu of options:

1. Add Contact
2. Delete Contact
3. Search Contact
4. Quit

Choose the option that corresponds to the action you want to perform.

### Add Contact

To add a contact, choose option 1 from the menu. You will be prompted to enter the contact's name, phone number, and email address. The contact will be added to the CSV file.

### Delete Contact

To delete a contact, choose option 2 from the menu. You will be prompted to enter the name of the contact you want to delete. The contact will be removed from the CSV file.

### Search Contact

To search for a contact, choose option 3 from the menu. You will be prompted to enter a search query. The application will search the CSV file for contacts that match the query and display the results.

### Quit

To exit the application, choose option 4 from the menu.

## Contributing

If you would like to contribute to this project, please submit a pull request with your proposed changes.

## Requirements

This application requires Python 3 and the csv and os modules.

## License

This project is licensed under the GNU License. See the [LICENSE](LICENSE) file for details.

## Update Notes

`Update V1.1 (28-05-2023)`

- Input Validation: Added checks to ensure valid data entry for name, phone number, and email using regular expressions.
- Error Handling: Implemented basic error handling to handle exceptions during file operations or user input, displaying error messages when necessary.
- File Path Handling: The code assumes 'contacts.csv' is in the same directory, but can be modified to handle file paths dynamically.
- Additional Contact Fields: Added 'address' and 'birthday' fields to the contact structure, updating CSV file structure and related functions.
- Sorting and Filtering: Introduced 'Sort Contacts' menu option to sort contacts by name or phone number, displaying the sorted contacts.
