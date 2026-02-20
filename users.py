# users.py
from storage import load_data, save_data

USERS_FILE = "users.json"

class UserSystem:

    def register(self):
        users = load_data(USERS_FILE)

        username = input("Enter username: ")
        if any(user["username"] == username for user in users):
            print("Username already exists.")
            return

        password = input("Enter password (min 6 chars): ")
        if len(password) < 6:
            print("Password too short.")
            return

        users.append({"username": username, "password": password})
        save_data(USERS_FILE, users)
        print("Registration successful.")

    def login(self):
        users = load_data(USERS_FILE)

        username = input("Username: ")
        password = input("Password: ")

        for user in users:
            if user["username"] == username and user["password"] == password:
                print("Login successful.")
                return username

        print("Invalid credentials.")
        return None