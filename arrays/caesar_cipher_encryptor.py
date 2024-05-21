'''

The function `caesarCipherEncryptor(string, key)` is designed to encrypt a given string using the Caesar Cipher method. The Caesar Cipher is a type of substitution cipher where each character in the plaintext is 'shifted' a certain number of places down the alphabet. In this case, the `key` would be the number of places to shift.

Here's how it works:

1. Normalize the key to handle cases where the key is greater than 26 (the number of letters in the alphabet). This can be done by taking `key` modulo 26.

2. Iterate over each character in the string. For each character, calculate the new character after shifting by `key` places. If the new character exceeds 'z', wrap around to the start of the alphabet.

3. Append the new character to the result string.

Here's the Python code for this function:
'''

def caesar_cipher_encryptor(string, key):
    # Normalize the key to handle cases where the key is greater than 26
    key = key % 26

    # Initialize an empty list to store the encrypted characters
    result = []

    # Iterate over each character in the string
    for char in string:
        # Calculate the new character code after shifting by 'key' places
        new_char_code = ord(char) + key

        # If the new character code exceeds 'z', wrap around to the start of the alphabet
        if new_char_code > ord('z'):
            new_char_code = ord('a') + new_char_code - ord('z') - 1

        # Append the new character to the result list
        result.append(chr(new_char_code))

    # Join the result list into a string and return it
    return ''.join(result)

'''
This function works by iterating over each character in the string, shifting it by `key` places, and appending it to the result string. 
The time complexity is O(n), where n is the length of the string, and the space complexity is also O(n) because a new string is created.
'''

import unittest

class TestCaesarCipherEncryptor(unittest.TestCase):
    def test_lowercase_letters(self):
        result = caesar_cipher_encryptor("hello", 3)
        self.assertEqual(result, "khoor")

    def test_uppercase_letters(self):
        result = caesar_cipher_encryptor("world", 5)
        self.assertEqual(result, "btwqi")

    def test_with_digits(self):
        result = caesar_cipher_encryptor("abc", 1)
        self.assertEqual(result, "bcd")

    def test_empty_string(self):
        result = caesar_cipher_encryptor("", 3)
        self.assertEqual(result, "")

    def test_large_key(self):
        result = caesar_cipher_encryptor("hello", 30)
        self.assertEqual(result, "lipps")

    def test_negative_key(self):
        result = caesar_cipher_encryptor("hello", -3)
        self.assertEqual(result, "ebiil")

if __name__ == '__main__':
    unittest.main()


'''
The `caesar_cipher_encryptor` function in Python encrypts a given string using the Caesar Cipher method, which shifts each character in the string by a specified number of positions in the alphabet. Let's break down the code and explain it with a visual diagram.

### Python Code Explanation

```python
def caesar_cipher_encryptor(string, key):
    # Normalize the key to handle cases where the key is greater than 26
    key = key % 26

    # Initialize an empty list to store the encrypted characters
    result = []

    # Iterate over each character in the string
    for char in string:
        # Calculate the new character code after shifting by 'key' places
        new_char_code = ord(char) + key

        # If the new character code exceeds 'z', wrap around to the start of the alphabet
        if new_char_code > ord('z'):
            new_char_code = ord('a') + new_char_code - ord('z') - 1

        # Append the new character to the result list
        result.append(chr(new_char_code))

    # Join the result list into a string and return it
    return ''.join(result)
```

### Step-by-Step Explanation

1. **Normalize the Key**:
    - The key is normalized using modulo 26 (`key = key % 26`) to handle cases where the key is greater than 26, as there are only 26 letters in the English alphabet.

2. **Initialize Result List**:
    - An empty list `result` is initialized to store the encrypted characters.

3. **Iterate Over Each Character**:
    - The function iterates over each character in the input string.
    - For each character, the new character code is calculated by adding the key to the ASCII value of the character (`ord(char) + key`).

4. **Handle Wrap-Around**:
    - If the new character code exceeds the ASCII value of 'z', it wraps around to the start of the alphabet using the formula:
      ```python
      new_char_code = ord('a') + new_char_code - ord('z') - 1
      ```

5. **Append to Result List**:
    - The new character (after shifting) is converted back to a character using `chr(new_char_code)` and appended to the result list.

6. **Join and Return**:
    - The list of encrypted characters is joined into a single string and returned.

### Visual Diagram

Let's use an example to visualize how the function works. Suppose we want to encrypt the string `"xyz"` with a key of 2.

#### Initial String and Key
```
String: "xyz"
Key: 2
```

#### Step 1: Normalize Key
- `key = 2 % 26 = 2` (no change since 2 < 26)

#### Step 2: Initialize Result List
- `result = []`

#### Step 3: Iterate Over Each Character

1. **Character 'x'**:
   - ASCII value of 'x': `ord('x') = 120`
   - New character code: `120 + 2 = 122` (within 'a' to 'z')
   - New character: `chr(122) = 'z'`
   - Result: `result = ['z']`

2. **Character 'y'**:
   - ASCII value of 'y': `ord('y') = 121`
   - New character code: `121 + 2 = 123` (exceeds 'z')
   - Wrap around: `new_char_code = ord('a') + 123 - ord('z') - 1 = 97 + 123 - 122 - 1 = 97 + 1 = 98`
   - New character: `chr(98) = 'a'`
   - Result: `result = ['z', 'a']`

3. **Character 'z'**:
   - ASCII value of 'z': `ord('z') = 122`
   - New character code: `122 + 2 = 124` (exceeds 'z')
   - Wrap around: `new_char_code = ord('a') + 124 - ord('z') - 1 = 97 + 124 - 122 - 1 = 97 + 2 = 99`
   - New character: `chr(99) = 'b'`
   - Result: `result = ['z', 'a', 'b']`

#### Step 4: Join and Return
- Join the result list: `''.join(result) = 'zab'`
- Return the encrypted string: `'zab'`

### Diagram Representation

```plaintext
Input String: "xyz"
Key: 2

Step-by-Step Encryption:

1. Character 'x':
   - ASCII: 120
   - New Code: 120 + 2 = 122
   - New Character: 'z'
   - Result: ['z']

2. Character 'y':
   - ASCII: 121
   - New Code: 121 + 2 = 123 (wrap around)
   - Wrap Calculation: 97 + 123 - 122 - 1 = 98
   - New Character: 'a'
   - Result: ['z', 'a']

3. Character 'z':
   - ASCII: 122
   - New Code: 122 + 2 = 124 (wrap around)
   - Wrap Calculation: 97 + 124 - 122 - 1 = 99
   - New Character: 'b'
   - Result: ['z', 'a', 'b']

Final Encrypted String: "zab"
```

This detailed explanation and diagram illustrate how the `caesar_cipher_encryptor` function works, showing the 
step-by-step process of encrypting each character in the string by shifting it according to the given key and 
handling wrap-around cases.
'''
