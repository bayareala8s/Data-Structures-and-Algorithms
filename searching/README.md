### Searching

Here are some common searching methods implemented in Python with real-world examples, detailed explanations, and complexity analysis:

1. **Linear Search**: This is the simplest form of searching. It traverses the list sequentially and checks if the current element matches the target.

```python
def linear_search(arr, target):
    # Traverse the list from start to end
    for i in range(len(arr)):
        # If the current element matches the target, return its index
        if arr[i] == target:
            return i
    # If the target is not found, return -1
    return -1

# Real-world example: Searching for a book in a small library
books = ["Harry Potter", "Lord of the Rings", "Game of Thrones", "The Hobbit"]
print(linear_search(books, "The Hobbit"))  # Output: 3
```
**Time Complexity**: O(n) - In the worst case, we have to check all elements, so the time complexity is linear.
**Space Complexity**: O(1) - No extra space is required, so the space complexity is constant.

2. **Binary Search**: This is an efficient searching method for a sorted list. It works by repeatedly dividing the search interval in half.

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Real-world example: Searching for a word in a dictionary
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print(binary_search(words, "date"))  # Output: 3
```
**Time Complexity**: O(log n) - The list is repeatedly divided in half until the target is found.
**Space Complexity**: O(1) - No extra space is required, so the space complexity is constant.

3. **Jump Search**: This is an optimized version of linear search where we skip some elements by jumping ahead by fixed steps.

```python
import math

def jump_search(arr, target):
    n = len(arr)
    step = math.sqrt(n)

    prev = 0
    while arr[int(min(step, n)-1)] < target:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    while arr[int(prev)] < target:
        prev += 1

        if prev == min(step, n):
            return -1

    if arr[int(prev)] == target:
        return int(prev)

    return -1

# Real-world example: Searching for a movie in a sorted list of movies
movies = ["Avatar", "Endgame", "Frozen", "Inception", "Joker", "Lion King", "Mulan", "Nemo", "Up"]
print(jump_search(movies, "Lion King"))  # Output: 5
```
**Time Complexity**: O(√n) - We jump √n steps at a time, so in the worst case, we have to check √n blocks and √n elements in the final block.
**Space Complexity**: O(1) - No extra space is required, so the space complexity is constant.

4. **Interpolation Search**: This is an improved version of Binary Search for instances, where the values in a sorted array are uniformly distributed. 

```python
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        index = low + int(((float(high - low) / (arr[high] - arr[low])) * (target - arr[low]))
        if arr[index] == target:
            return index
        if arr[index] < target:
            low = index + 1
        else:
            high = index - 1
    return -1

# Real-world example: Searching for a specific temperature in a sorted list of temperatures
temperatures = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(interpolation_search(temperatures, 60))  # Output: 5
```
**Time Complexity**: O(log log n) for uniformly distributed data, O(n) in the worst case.
**Space Complexity**: O(1) - No extra space is required, so the space complexity is constant.

Please note that these search methods assume that the input list `arr` is sorted for Binary, Jump, and Interpolation search. If the list is not sorted, you would need to sort it before using these methods.


