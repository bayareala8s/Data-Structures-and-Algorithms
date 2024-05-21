# HashTable

### Hash Table Data Structure

A **hash table** (or hash map) is a data structure that provides an efficient way to store and retrieve key-value pairs. It is widely used due to its average-case time complexity of O(1) for insertion, deletion, and retrieval operations. Here’s a detailed description of the hash table data structure:

#### Key Components

1. **Hash Function**:
   - A hash function is used to map keys to their corresponding bucket or slot in the hash table. It takes a key and returns an integer (the hash code), which is then mapped to an index in the table.
   - A good hash function should distribute keys uniformly across the table to minimize collisions.

2. **Buckets**:
   - The hash table consists of an array (or list) of buckets. Each bucket can store one or more key-value pairs.
   - In case of collisions (when multiple keys hash to the same index), the bucket can store multiple items. Common ways to handle collisions include chaining and open addressing.

3. **Collision Handling**:
   - **Chaining**: Each bucket contains a list (or another data structure) to store multiple key-value pairs. When a collision occurs, the new key-value pair is added to the list.
   - **Open Addressing**: When a collision occurs, the algorithm probes the table to find the next available slot. Methods include linear probing, quadratic probing, and double hashing.

#### Basic Operations

1. **Insertion**:
   - Compute the hash code of the key.
   - Map the hash code to an index in the table.
   - Handle collisions (if any) and store the key-value pair in the corresponding bucket.

2. **Retrieval**:
   - Compute the hash code of the key.
   - Map the hash code to an index in the table.
   - Search the bucket for the key and return the associated value.

3. **Deletion**:
   - Compute the hash code of the key.
   - Map the hash code to an index in the table.
   - Search the bucket for the key and remove the key-value pair.

#### Advantages

- **Fast Access**: Provides average-case O(1) time complexity for insertions, deletions, and lookups.
- **Scalability**: Efficiently handles large datasets.

#### Disadvantages

- **Memory Usage**: May require more memory than other data structures due to the need for extra space to handle collisions.
- **Performance Degradation**: Performance can degrade to O(n) in the worst case (e.g., when all keys hash to the same index).

### Real-World Example

Consider a real-world application where we need to store and manage user information (e.g., name, age, email). A hash table can be used to efficiently store and retrieve user data based on unique usernames.

#### Python Implementation Example

Here is a simple implementation of a hash table in Python, including basic operations and a real-world use case for managing user information.

```python
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self._hash(key)
        key_exists = False
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = (key, value)
        else:
            bucket.append((key, value))

    def retrieve(self, key):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        for k, v in bucket:
            if key == k:
                return v
        return None

    def delete(self, key):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                del bucket[i]
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {i}: {bucket}")

class UserInformation:
    def __init__(self):
        self.ht = HashTable()

    def add_user(self, username, name, age, email):
        self.ht.insert(f"{username}_name", name)
        self.ht.insert(f"{username}_age", age)
        self.ht.insert(f"{username}_email", email)

    def get_user_info(self, username):
        name = self.ht.retrieve(f"{username}_name")
        age = self.ht.retrieve(f"{username}_age")
        email = self.ht.retrieve(f"{username}_email")
        return {"name": name, "age": age, "email": email}

    def delete_user(self, username):
        self.ht.delete(f"{username}_name")
        self.ht.delete(f"{username}_age")
        self.ht.delete(f"{username}_email")

# Example usage
ui = UserInformation()
ui.add_user("johndoe", "John Doe", 30, "john.doe@example.com")
print(ui.get_user_info("johndoe"))
ui.delete_user("johndoe")
print(ui.get_user_info("johndoe"))
```

### Explanation of the Example

- **HashTable Class**:
  - Initializes with a fixed size and creates buckets.
  - Implements a hash function to map keys to indices.
  - Provides methods for insertion, retrieval, and deletion of key-value pairs.
  - Handles collisions using chaining.

- **UserInformation Class**:
  - Uses the `HashTable` class to store and manage user information.
  - Adds user information with composite keys.
  - Retrieves and deletes user information based on the username.

This example demonstrates how a hash table can be used in a practical application to efficiently manage and retrieve user data.


