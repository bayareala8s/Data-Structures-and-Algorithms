### Python arrays

In Python, arrays are a type of data structure used to store a collection of elements of the same data type. Python arrays can be created using different modules, each with its own characteristics and use cases. Here are some common ways to work with arrays in Python:

1. **Lists**: Python lists are a built-in data structure that can be used as arrays. Lists are flexible and can contain elements of different data types. You can create a list by enclosing comma-separated values within square brackets `[ ]`.

    ```python
    my_list = [1, 2, 3, 4, 5]
    ```

2. **Array Module**: The `array` module provides a way to create arrays that are more memory efficient compared to lists. However, arrays created using this module can only contain elements of a single data type.

    ```python
    import array
    my_array = array.array('i', [1, 2, 3, 4, 5])
    ```

    Here, `'i'` represents the type code for signed integers.

3. **NumPy Arrays**: NumPy is a powerful library for numerical computing in Python. It provides a multidimensional array object called `numpy.ndarray`, which offers efficient storage and operations on large arrays of data.

    ```python
    import numpy as np
    my_numpy_array = np.array([1, 2, 3, 4, 5])
    ```

    NumPy arrays support element-wise operations, broadcasting, and a wide range of mathematical functions.

4. **Array-like Objects**: Some libraries and modules provide array-like objects with additional functionalities. For example, the `array` module from the Python standard library provides the `array.array` object, while pandas provides the `Series` and `DataFrame` objects.

Arrays in Python are mutable, meaning you can modify their elements after creation. They support indexing and slicing operations for accessing elements or subarrays. Depending on your specific use case and requirements, you can choose the appropriate type of array in Python.


In Python, the time complexity of array and string operations can vary depending on the specific operation and the underlying data structure being used. Here's an overview of the typical time complexities for common array and string operations:

### Arrays:

1. **Accessing an Element by Index**: O(1)
   - Accessing an element in an array by its index is a constant-time operation because arrays provide direct access to elements based on their memory location.

2. **Appending an Element to the End (Dynamic Arrays)**: Amortized O(1)
   - Appending an element to the end of a dynamic array typically has an amortized constant-time complexity. However, occasionally, when the underlying array needs to be resized, it may require copying the entire array, resulting in a linear time complexity. 

3. **Inserting/Deleting an Element in the Middle**: O(n)
   - Inserting or deleting an element in the middle of an array requires shifting all subsequent elements, resulting in a linear time complexity.

4. **Searching for an Element**: O(n) (for unsorted arrays), O(log n) (for sorted arrays)
   - Linear search in an unsorted array has a time complexity of O(n) because it may require traversing the entire array. Binary search in a sorted array has a time complexity of O(log n) because it halves the search space with each comparison.

### Strings:

1. **Accessing a Character by Index**: O(1)
   - Accessing a character in a string by its index is a constant-time operation because strings are typically implemented as arrays of characters, and accessing an element by index is constant time.

2. **Concatenating Strings**: O(n + m)
   - Concatenating two strings of lengths n and m typically requires creating a new string and copying the characters from both strings into the new string, resulting in a linear time complexity.

3. **Substring Operations (Slicing)**: O(k)
   - Slicing a string to extract a substring of length k is a linear time operation because it involves copying the characters from the original string to create the substring.

4. **Searching for a Substring**: O(n * m)
   - Naive substring search algorithms have a time complexity of O(n * m), where n is the length of the string and m is the length of the substring being searched for. More efficient algorithms like Knuth-Morris-Pratt (KMP) or Boyer-Moore have better time complexities, typically O(n + m) or O(n), depending on the implementation.

These time complexities represent the worst-case scenarios for the respective operations. Actual performance may vary depending on factors such as hardware, software optimizations, and specific implementations.


### some common list methods in Python along with examples:

1. `append()`: Adds an element to the end of the list.

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```

2. `extend()`: Adds elements from another list to the end of the current list.

```python
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]
```

3. `insert()`: Inserts an element at a specified position in the list.

```python
my_list = [1, 2, 3]
my_list.insert(1, 'a')
print(my_list)  # Output: [1, 'a', 2, 3]
```

4. `remove()`: Removes the first occurrence of a specified value from the list.

```python
my_list = [1, 2, 3, 1]
my_list.remove(1)
print(my_list)  # Output: [2, 3, 1]
```

5. `pop()`: Removes and returns the element at a specified index in the list. If no index is specified, it removes and returns the last element.

```python
my_list = [1, 2, 3]
print(my_list.pop(1))  # Output: 2
print(my_list)          # Output: [1, 3]
```

6. `clear()`: Removes all elements from the list.

```python
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []
```

7. `index()`: Returns the index of the first occurrence of a specified value in the list.

```python
my_list = [1, 2, 3]
print(my_list.index(2))  # Output: 1
```

8. `count()`: Returns the number of occurrences of a specified value in the list.

```python
my_list = [1, 2, 2, 3]
print(my_list.count(2))  # Output: 2
```

9. `sort()`: Sorts the elements of the list in ascending order.

```python
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3]
```

10. `reverse()`: Reverses the order of the elements in the list.

```python
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]
```

These are some of the commonly used list methods in Python. They provide powerful capabilities for manipulating lists in various ways.

### Two pointers

The "two pointers" technique is a common approach used in algorithms and data structures to solve problems efficiently. It involves using two pointers or indices to traverse a sequence or array, typically from different ends or starting points. This technique is often employed to optimize the time complexity of algorithms.

Here's a brief overview of how the two pointers technique works:

1. **Two Pointers Initialization**: Initialize two pointers or indices, often named `left` and `right`, at different positions in the array or sequence.

2. **Traverse the Sequence**: Use the two pointers to traverse the sequence or array in a specific manner, such as moving towards each other, moving in opposite directions, or moving in the same direction at different speeds.

3. **Condition-Based Movement**: At each step of the traversal, update the positions of the pointers based on certain conditions or criteria. These conditions are often related to the problem being solved and may involve comparisons with elements in the sequence or array.

4. **Termination Condition**: Define a termination condition for the traversal based on the problem requirements. This condition determines when the traversal should stop.

The two pointers technique is particularly useful for solving problems involving arrays or sequences, such as finding pairs that satisfy certain conditions, searching for subarrays or substrings with specific properties, and detecting patterns or sequences within the data.

Here are some common applications of the two pointers technique:

1. **Two Sum**: Finding two numbers in an array that sum up to a specific target value.
2. **Reverse Array or String**: Reversing the elements of an array or characters of a string using two pointers.
3. **Palindrome Detection**: Checking if a string is a palindrome by comparing characters from both ends simultaneously.
4. **Merge Two Sorted Arrays**: Merging two sorted arrays into a single sorted array using two pointers to compare elements.

The two pointers technique can often lead to efficient solutions with a time complexity of O(n) or better, where n is the size of the input data. It's a versatile approach that can be adapted to various problem-solving scenarios.


- Given a string s, return true if it is a palindrome, false otherwise. 

One approach to determine if a string is a palindrome is to use the two pointers technique. You can use two pointers, one starting from the beginning of the string and the other starting from the end, and compare characters at corresponding positions. If all characters match, then the string is a palindrome.

Here's a Python function implementing this approach:

```python
def is_palindrome(s):
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Initialize two pointers
    left, right = 0, len(s) - 1
    
    # Continue comparing characters until the pointers meet
    while left < right:
        # If the characters at the left and right pointers don't match, it's not a palindrome
        if s[left] != s[right]:
            return False
        # Move the pointers towards each other
        left += 1
        right -= 1
    
    # If the loop completes without returning False, the string is a palindrome
    return True

# Example usage
string1 = "A man, a plan, a canal: Panama"
string2 = "racecar"

print(is_palindrome(string1))  # Output: True
print(is_palindrome(string2))  # Output: True
```

This function first preprocesses the input string by converting it to lowercase and removing non-alphanumeric characters. Then, it initializes two pointers at the beginning and end of the string and compares characters at corresponding positions. If any pair of characters doesn't match, it returns `False`. If the loop completes without returning `False`, the string is a palindrome, and the function returns `True`.


- Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise.

You can solve this problem efficiently using the two pointers technique. Since the input array is sorted, you can use two pointers, one starting from the beginning and the other from the end of the array. By moving these pointers inward, you can determine if there exists a pair of numbers that sum to the target.

Here's how you can implement this in Python:

```python
def has_pair_with_sum(nums, target):
    # Initialize two pointers
    left, right = 0, len(nums) - 1
    
    # Continue until the pointers meet
    while left < right:
        current_sum = nums[left] + nums[right]
        
        # If the current sum equals the target, return True
        if current_sum == target:
            return True
        # If the current sum is less than the target, move the left pointer to the right
        elif current_sum < target:
            left += 1
        # If the current sum is greater than the target, move the right pointer to the left
        else:
            right -= 1
    
    # If the loop completes without finding a pair, return False
    return False

# Example usage
nums = [1, 2, 4, 7, 11]
target = 9
print(has_pair_with_sum(nums, target))  # Output: True

target = 13
print(has_pair_with_sum(nums, target))  # Output: False
```

In this implementation, the `has_pair_with_sum` function takes a sorted array `nums` and a target integer `target`. It initializes two pointers, `left` and `right`, and iterates through the array using the two pointers. If the sum of the numbers at the current positions of the pointers equals the target, it returns `True`. If the sum is less than the target, it moves the left pointer to the right to increase the sum, and if the sum is greater than the target, it moves the right pointer to the left to decrease the sum. If the loop completes without finding a pair, it returns `False`.


- Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

You can merge the two sorted arrays into a new sorted array by using the two pointers technique. Initialize two pointers, one for each array, and compare the elements at the corresponding positions. Add the smaller element to the new array, and move the pointer of the array from which the element was taken. Repeat this process until you reach the end of both arrays.

Here's how you can implement this in Python:

```python
def merge_sorted_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0
    
    # Compare elements from both arrays and add the smaller one to the merged array
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # Add any remaining elements from arr1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    
    # Add any remaining elements from arr2
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    
    return merged

# Example usage
arr1 = [1, 3, 5]
arr2 = [2, 4, 6, 7]

print(merge_sorted_arrays(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6, 7]
```

In this implementation, the `merge_sorted_arrays` function takes two sorted arrays `arr1` and `arr2` as input. It initializes two pointers, `i` and `j`, for each array and iterates through both arrays using these pointers. It compares the elements at the current positions of the pointers and adds the smaller one to the `merged` array. After reaching the end of one array, it adds any remaining elements from the other array. Finally, it returns the merged array.


- Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

You can solve this problem by iterating through both strings using two pointers, one for each string. At each step, compare the characters at the current positions of the pointers. If they match, move both pointers to the next character in their respective strings. If they don't match, only move the pointer for the second string. Continue this process until you reach the end of the first string.

Here's how you can implement this in Python:

```python
def is_subsequence(s, t):
    # Initialize pointers for both strings
    i, j = 0, 0
    
    # Iterate through both strings
    while i < len(s) and j < len(t):
        # If characters match, move both pointers
        if s[i] == t[j]:
            i += 1
        # Move pointer for string t
        j += 1
    
    # If all characters of s have been matched, s is a subsequence of t
    return i == len(s)

# Example usage
s = "abc"
t = "ahbgdc"
print(is_subsequence(s, t))  # Output: True

s = "axc"
t = "ahbgdc"
print(is_subsequence(s, t))  # Output: False
```

In this implementation, the `is_subsequence` function takes two strings `s` and `t` as input. It initializes two pointers, `i` and `j`, for each string and iterates through both strings using these pointers. If the characters at the current positions of the pointers match, it moves both pointers to the next character in their respective strings. If they don't match, it only moves the pointer for string `t`. After reaching the end of string `s`, if the pointer `i` is equal to the length of `s`, it means all characters of `s` have been matched in `t`, and `s` is a subsequence of `t`.

- Write a function that reverses a string. The input string is given as an array of characters s.

You can reverse the string in-place by using two pointers technique. Initialize two pointers, one at the beginning of the string and the other at the end. Swap the characters at the positions pointed to by the two pointers, and then move the pointers towards each other until they meet in the middle of the string.

Here's how you can implement this in Python:

```python
def reverse_string(s):
    # Initialize pointers
    left, right = 0, len(s) - 1
    
    # Reverse the string in-place
    while left < right:
        # Swap characters at left and right pointers
        s[left], s[right] = s[right], s[left]
        # Move pointers towards each other
        left += 1
        right -= 1

# Example usage
input_string = ['h', 'e', 'l', 'l', 'o']
reverse_string(input_string)
print(input_string)  # Output: ['o', 'l', 'l', 'e', 'h']
```

In this implementation, the `reverse_string` function takes an array of characters `s` as input. It initializes two pointers, `left` and `right`, at the beginning and end of the array, respectively. It then iterates through the array using these pointers, swapping the characters at the positions pointed to by the two pointers, and moving the pointers towards each other until they meet in the middle of the array. This effectively reverses the string in-place.


- Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

You can solve this problem efficiently using a two-pointer approach. Since the original array is sorted in non-decreasing order, you can use two pointers to iterate over the array from both ends. Compare the squares of the elements pointed to by the pointers and add the larger squared value to the result array. Move the pointers inward until they meet in the middle of the array.

Here's how you can implement this in Python:

```python
def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    index = n - 1
    
    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2
        
        if left_square > right_square:
            result[index] = left_square
            left += 1
        else:
            result[index] = right_square
            right -= 1
        index -= 1
    
    return result

# Example usage
nums = [-4, -1, 0, 3, 10]
result = sorted_squares(nums)
print(result)  # Output: [0, 1, 9, 16, 100]
```

In this implementation:

- We initialize a result array of the same length as the input array `nums`.
- We use two pointers, `left` starting from the beginning of the array and `right` starting from the end of the array.
- We iterate over the array using these pointers and compare the squares of the elements pointed to by the pointers.
- We add the larger squared value to the result array at the corresponding index.
- We move the pointers inward until they meet in the middle of the array.
- Finally, we return the result array containing the squares of each number sorted in non-decreasing order.

This solution has a time complexity of O(n), where n is the number of elements in the input array `nums`, since we only iterate over the array once.


### Sliding window

The sliding window technique is a useful algorithmic pattern for solving problems involving arrays or strings. It involves creating a window of a fixed size that moves or "slides" across the array or string, typically from left to right. The window maintains a subset of elements or characters, and you perform some operation on this subset.

Here's a step-by-step guide on how to implement the sliding window technique:

1. **Initialization**: Initialize two pointers, typically `left` and `right`, to define the boundaries of the window. Set them to the starting position.

2. **Expand the Window**: Move the `right` pointer to expand the window, adding elements or characters to the window until you reach a condition where the window no longer satisfies a specific constraint (e.g., a maximum size or a certain property).

3. **Shrink the Window**: Once the window no longer satisfies the constraint, move the `left` pointer to shrink the window, removing elements or characters from the window until the constraint is satisfied again.

4. **Update the Result**: Keep track of the result as the window moves, depending on the problem requirements. For example, you might calculate a sum, find the maximum or minimum value, or perform some other operation on the elements or characters within the window.

5. **Repeat**: Continue moving the window until the `right` pointer reaches the end of the array or string.

The sliding window technique is commonly used to solve problems related to substring or subarray manipulation, such as finding the maximum sum of a subarray, finding the smallest substring containing all characters of a given set, or finding the longest substring without repeating characters.

Here's a simple example of using the sliding window technique to find the maximum sum of a subarray (also known as the "maximum sum subarray problem"):

```python
def max_subarray_sum(nums):
    max_sum = float('-inf')
    current_sum = 0
    left = 0

    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum < nums[right]:
            current_sum -= nums[left]
            left += 1
        
        max_sum = max(max_sum, current_sum)

    return max_sum
```

In this example, we maintain a sliding window defined by the `left` and `right` pointers. We iterate through the array, adding elements to the current sum as we expand the window (`right` pointer). If the current sum becomes negative (indicating that it's better to start a new window), we shrink the window from the left side (`left` pointer). Finally, we update the maximum sum as the window moves.


- Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k. 

You can solve this problem using the sliding window technique. Here's how you can approach it:

1. Initialize two pointers, `left` and `right`, to define the boundaries of the window. Set them to the starting position.

2. Iterate through the array while moving the `right` pointer to expand the window. Keep track of the current sum of the elements within the window.

3. While the current sum exceeds the target value `k`, move the `left` pointer to shrink the window, subtracting the element at the left end of the window from the current sum.

4. Update the maximum length of the subarray as the window moves.

5. Repeat steps 2-4 until the `right` pointer reaches the end of the array.

Here's the implementation in Python:

```python
def max_subarray_length(nums, k):
    max_length = 0
    current_sum = 0
    left = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        # Shrink the window if the current sum exceeds k
        while current_sum > k and left <= right:
            current_sum -= nums[left]
            left += 1

        # Update the maximum length of the subarray
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage
nums = [1, 2, 3, 4, 5]
k = 11
print(max_subarray_length(nums, k))  # Output: 3 (since [1, 2, 3] has sum <= 11)
```

In this implementation:

- We maintain a sliding window defined by the `left` and `right` pointers.
- We iterate through the array while expanding the window (`right` pointer) and updating the current sum.
- If the current sum exceeds the target value `k`, we shrink the window from the left side (`left` pointer) until the current sum is within the limit.
- We update the maximum length of the subarray as the window moves.
- Finally, we return the maximum length of the subarray found.

- You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"


To solve this problem, you can use the sliding window technique. Here's how you can approach it:

1. Initialize two pointers, `left` and `right`, to define the boundaries of the window. Set them to the starting position.

2. Iterate through the binary string while moving the `right` pointer to expand the window. Keep track of the count of zeros encountered within the window.

3. While the count of zeros within the window exceeds 1, move the `left` pointer to shrink the window, subtracting the count of zeros encountered at the left end of the window.

4. Update the maximum length of the substring containing only "1" as the window moves.

5. Repeat steps 2-4 until the `right` pointer reaches the end of the binary string.

Here's the implementation in Python:

```python
def longest_substring_of_ones(s):
    max_length = 0
    left = 0
    zero_count = 0

    for right in range(len(s)):
        if s[right] == '0':
            zero_count += 1

        # Shrink the window if the count of zeros exceeds 1
        while zero_count > 1:
            if s[left] == '0':
                zero_count -= 1
            left += 1

        # Update the maximum length of the substring
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage
binary_string = "110101011"
print(longest_substring_of_ones(binary_string))  # Output: 6 (substring "101011" has length 6)
```

In this implementation:

- We maintain a sliding window defined by the `left` and `right` pointers.
- We iterate through the binary string while expanding the window (`right` pointer) and updating the count of zeros encountered within the window.
- If the count of zeros within the window exceeds 1, we shrink the window from the left side (`left` pointer) until the count of zeros within the window is at most 1.
- We update the maximum length of the substring containing only "1" as the window moves.
- Finally, we return the maximum length of the substring found.

- Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k


To solve this problem, you can use the sliding window technique. Here's how you can approach it:

1. Initialize two pointers, `left` and `right`, to define the boundaries of the window. Set them to the starting position.

2. Iterate through the array while moving the `right` pointer to expand the window. Keep track of the product of all the elements within the window.

3. While the product of all elements within the window is greater than or equal to `k`, move the `left` pointer to shrink the window, dividing the product by the element at the left end of the window.

4. Update the count of valid subarrays as the window moves.

5. Repeat steps 2-4 until the `right` pointer reaches the end of the array.

Here's the implementation in Python:

```python
def count_subarrays(nums, k):
    count = 0
    product = 1
    left = 0

    for right in range(len(nums)):
        product *= nums[right]

        # Shrink the window if the product is greater than or equal to k
        while product >= k and left <= right:
            product //= nums[left]
            left += 1

        # Update the count of valid subarrays
        count += right - left + 1

    return count

# Example usage
nums = [10, 5, 2, 6]
k = 100
print(count_subarrays(nums, k))  # Output: 8
```

In this implementation:

- We maintain a sliding window defined by the `left` and `right` pointers.
- We iterate through the array while expanding the window (`right` pointer) and updating the product of all elements within the window.
- If the product of all elements within the window is greater than or equal to `k`, we shrink the window from the left side (`left` pointer) until the product is less than `k`.
- We update the count of valid subarrays as the window moves.
- Finally, we return the count of valid subarrays found.
