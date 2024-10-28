# password_manager.py

import json
import os
import getpass
from password_utils import generate_password, encrypt_password, decrypt_password

PASSWORD_FILE = "passwords.json"
KEY = b'Sixteen byte key'  # Replace with a secure key

# Load existing passwords from file
def load_passwords():
    if not os.path.exists(PASSWORD_FILE):
        return {}
    with open(PASSWORD_FILE, 'r') as f:
        return json.load(f)

# Save passwords to file
def save_passwords(passwords):
    with open(PASSWORD_FILE, 'w') as f:
        json.dump(passwords, f)

# Main application logic
def main():
    passwords = load_passwords()
    
    while True:
        print("\nPassword Manager")
        print("1. Generate a password")
        print("2. Store a password")
        print("3. Retrieve a password")
        print("4. Delete a password")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            try:
                length = int(input("Enter the desired password length: "))
                if length <= 0:
                    raise ValueError("Password length must be a positive integer.")
                password = generate_password(length)
                print(f"Generated Password: {password}")
            except ValueError as e:
                print(f"Invalid input: {e}")

        elif choice == '2':
            name = input("Enter the name of the service: ")
            password = getpass.getpass("Enter the password: ")
            encrypted_password = encrypt_password(password, KEY)
            passwords[name] = encrypted_password
            save_passwords(passwords)
            print(f"Password for {name} stored successfully.")

        elif choice == '3':
            name = input("Enter the name of the service: ")
            if name in passwords:
                try:
                    decrypted_password = decrypt_password(passwords[name], KEY)
                    print(f"Password for {name}: {decrypted_password}")
                except Exception as e:
                    print(f"Error retrieving password: {e}")
            else:
                print("Service not found.")

        elif choice == '4':
            name = input("Enter the name of the service to delete: ")
            if name in passwords:
                del passwords[name]
                save_passwords(passwords)
                print(f"Password for {name} deleted successfully.")
            else:
                print("Service not found.")

        elif choice == '5':
            print("Exiting the password manager.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
