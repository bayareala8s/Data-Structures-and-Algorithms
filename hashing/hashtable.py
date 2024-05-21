class HashTable:
    def __init__(self, size=10):
        # Initialize the hash table with the given size
        self.size = size
        # Create a list of empty lists for storing the key-value pairs (chaining to handle collisions)
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        # Compute the hash value for the given key
        # Use the built-in hash function and take modulo with the size of the table
        return hash(key) % self.size

    def insert(self, key, value):
        # Insert a key-value pair into the hash table
        hash_key = self._hash(key)
        key_exists = False
        bucket = self.table[hash_key]

        # Check if the key already exists in the bucket
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break

        # If key exists, update the value
        if key_exists:
            bucket[i] = (key, value)
        else:
            # If key does not exist, append the new key-value pair
            bucket.append((key, value))

    def retrieve(self, key):
        # Retrieve the value associated with the given key
        hash_key = self._hash(key)
        bucket = self.table[hash_key]

        # Search for the key in the bucket
        for k, v in bucket:
            if key == k:
                return v
        return None

    def delete(self, key):
        # Delete the key-value pair from the hash table
        hash_key = self._hash(key)
        bucket = self.table[hash_key]

        # Search for the key in the bucket and delete it if found
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                del bucket[i]
                return True
        return False

    def display(self):
        # Display the contents of the hash table
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {i}: {bucket}")


# Example usage of the HashTable class
ht = HashTable()

# Insert some data
ht.insert("name", "John Doe")
ht.insert("age", 30)
ht.insert("email", "john.doe@example.com")

# Retrieve data
print("Name:", ht.retrieve("name"))  # Output: John Doe
print("Age:", ht.retrieve("age"))  # Output: 30
print("Email:", ht.retrieve("email"))  # Output: john.doe@example.com

# Delete data
ht.delete("age")
print("Age after deletion:", ht.retrieve("age"))  # Output: None

# Display the entire hash table
ht.display()


'''
Real-World Implementation: User Information Storage
Here’s how you can use the hash table to manage user information in a real-world scenario:
'''

class UserInformation:
    def __init__(self):
        self.ht = HashTable()

    def add_user(self, username, name, age, email):
        # Add user information to the hash table
        self.ht.insert(f"{username}_name", name)
        self.ht.insert(f"{username}_age", age)
        self.ht.insert(f"{username}_email", email)

    def get_user_info(self, username):
        # Retrieve user information from the hash table
        name = self.ht.retrieve(f"{username}_name")
        age = self.ht.retrieve(f"{username}_age")
        email = self.ht.retrieve(f"{username}_email")
        return {"name": name, "age": age, "email": email}

    def delete_user(self, username):
        # Delete user information from the hash table
        self.ht.delete(f"{username}_name")
        self.ht.delete(f"{username}_age")
        self.ht.delete(f"{username}_email")

# Example usage of the UserInformation class
ui = UserInformation()

# Add users
ui.add_user("johndoe", "John Doe", 30, "john.doe@example.com")
ui.add_user("janedoe", "Jane Doe", 25, "jane.doe@example.com")

# Retrieve user information
print(ui.get_user_info("johndoe"))  # Output: {'name': 'John Doe', 'age': 30, 'email': 'john.doe@example.com'}
print(ui.get_user_info("janedoe"))  # Output: {'name': 'Jane Doe', 'age': 25, 'email': 'jane.doe@example.com'}

# Delete a user
ui.delete_user("johndoe")
print(ui.get_user_info("johndoe"))  # Output: {'name': None, 'age': None, 'email': None}

'''
Explanation
HashTable Class:

Initialization: Initializes the hash table with a specified size and creates empty buckets for storing key-value pairs.
Hash Function: Computes the hash value for a given key.
Insert: Adds a key-value pair to the hash table, updating the value if the key already exists.
Retrieve: Retrieves the value associated with a given key.
Delete: Removes a key-value pair from the hash table.
Display: Shows the contents of the hash table.
UserInformation Class:

Initialization: Initializes an instance of the HashTable class.
Add User: Adds user information (name, age, email) to the hash table using a composite key (username_field).
Get User Info: Retrieves user information based on the username.
Delete User: Deletes user information based on the username.
Example Usage:

Demonstrates how to add, retrieve, and delete user information using the UserInformation class.
This code provides a practical implementation of a hash table and demonstrates its use in managing user information, 
showcasing how data can be efficiently stored, retrieved, and managed using a hash table.
'''

import unittest

class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.ht = HashTable()

    def test_insert_and_retrieve(self):
        self.ht.insert("name", "John Doe")
        self.assertEqual(self.ht.retrieve("name"), "John Doe")

    def test_insert_update_and_retrieve(self):
        self.ht.insert("name", "John Doe")
        self.ht.insert("name", "Jane Doe")
        self.assertEqual(self.ht.retrieve("name"), "Jane Doe")

    def test_retrieve_non_existent_key(self):
        self.assertIsNone(self.ht.retrieve("non_existent"))

    def test_delete_key(self):
        self.ht.insert("name", "John Doe")
        self.ht.delete("name")
        self.assertIsNone(self.ht.retrieve("name"))

    def test_delete_non_existent_key(self):
        self.assertFalse(self.ht.delete("non_existent"))

    def test_collision_handling(self):
        self.ht.insert("name1", "John Doe")
        self.ht.insert("name2", "Jane Doe")
        self.assertEqual(self.ht.retrieve("name1"), "John Doe")
        self.assertEqual(self.ht.retrieve("name2"), "Jane Doe")


'''
Unit Test Cases for HashTable Class
'''

class TestUserInformation(unittest.TestCase):

    def setUp(self):
        self.ui = UserInformation()

    def test_add_and_get_user_info(self):
        self.ui.add_user("johndoe", "John Doe", 30, "john.doe@example.com")
        user_info = self.ui.get_user_info("johndoe")
        self.assertEqual(user_info["name"], "John Doe")
        self.assertEqual(user_info["age"], 30)
        self.assertEqual(user_info["email"], "john.doe@example.com")

    def test_add_multiple_users(self):
        self.ui.add_user("johndoe", "John Doe", 30, "john.doe@example.com")
        self.ui.add_user("janedoe", "Jane Doe", 25, "jane.doe@example.com")
        user_info_john = self.ui.get_user_info("johndoe")
        user_info_jane = self.ui.get_user_info("janedoe")
        self.assertEqual(user_info_john["name"], "John Doe")
        self.assertEqual(user_info_jane["name"], "Jane Doe")

    def test_delete_user(self):
        self.ui.add_user("johndoe", "John Doe", 30, "john.doe@example.com")
        self.ui.delete_user("johndoe")
        user_info = self.ui.get_user_info("johndoe")
        self.assertIsNone(user_info["name"])
        self.assertIsNone(user_info["age"])
        self.assertIsNone(user_info["email"])

    def test_delete_non_existent_user(self):
        self.ui.delete_user("non_existent")
        user_info = self.ui.get_user_info("non_existent")
        self.assertIsNone(user_info["name"])
        self.assertIsNone(user_info["age"])
        self.assertIsNone(user_info["email"])

if __name__ == '__main__':
    unittest.main()

'''
Explanation of Unit Test Cases
TestHashTable Class:

setUp: Initializes a new HashTable instance before each test.
test_insert_and_retrieve: Tests inserting and retrieving a key-value pair.
test_insert_update_and_retrieve: Tests updating an existing key and retrieving the updated value.
test_retrieve_non_existent_key: Tests retrieving a non-existent key, expecting None.
test_delete_key: Tests deleting a key and ensuring it no longer exists.
test_delete_non_existent_key: Tests deleting a non-existent key, expecting False.
test_collision_handling: Tests inserting and retrieving multiple keys that may cause collisions.
TestUserInformation Class:

setUp: Initializes a new UserInformation instance before each test.
test_add_and_get_user_info: Tests adding a user and retrieving their information.
test_add_multiple_users: Tests adding multiple users and retrieving their information.
test_delete_user: Tests deleting a user and ensuring their information is removed.
test_delete_non_existent_user: Tests deleting a non-existent user and ensuring the returned information is None.
Running the Tests
You can run these tests by saving the code into a Python file (e.g., test_hash_table.py) and running it with the following command:

bash
Copy code
python -m unittest test_hash_table.py
This will execute the unit tests and display the results, showing which tests passed and which (if any) failed.

'''