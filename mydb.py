import json

class DataBase:
    def add_data(self, name, email, password):
        # Read the existing database from the JSON file
        with open("db.json", "r") as rf:
            database = json.load(rf)

            # Check if the provided email is already in the database
            if email in database:
                return 0  # Registration failed: Email already exists
            else:
                # Add the new user's information to the database
                database[email] = [name, password]

            # Write the updated database back to the JSON file
            with open("db.json", "w") as wf:
                json.dump(database, wf)

            return 1  # Registration successful

    def search(self, email, password):
        # Read the existing database from the JSON file
        with open("db.json", "r") as rf:
            database = json.load(rf)

            # Check if the provided email exists in the database
            if email in database:
                # Verify if the provided password matches the stored password
                if database[email][1] == password:
                    return 1  # Login successful
                else:
                    return 0  # Login failed: Incorrect password
            else:
                return 0  # Login failed: Email not found

# Example usage:
# db = DataBase()
# result = db.add_data("lucky", "lucky@example.com", "password123")
# if result == 1:
#     print("Registration successful!")
# else:
#     print("Registration failed: Email already exists")

# result = db.search("johndoe@example.com", "password123")
# if result == 1:
#     print("Login successful!")
# else:
#     print("Login failed: Incorrect email or password")
