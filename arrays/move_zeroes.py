'''
The function `move_zeroes(nums)` is designed to move all the zeroes in the input list `nums` to the end while maintaining the relative order of the non-zero elements. Here's how it works:

1. Initialize a position pointer `pos` at 0. This pointer will keep track of the position where the next non-zero element should be placed.

2. Iterate over the list. For each element, if it's not zero, place it at the position pointed to by `pos` and increment `pos`.

3. After all non-zero elements have been moved, fill the rest of the list with zeroes.

Here's the Python code for this function:
'''

def move_zeroes(nums):
    # Initialize position pointer
    pos = 0

    # Iterate over the list
    for i in range(len(nums)):
        # If the current element is not zero
        if nums[i] != 0:
            # Move the non-zero element to the position pointed by 'pos'
            nums[pos] = nums[i]
            # Increment 'pos'
            pos += 1

    # Fill the remaining positions with zeros
    for i in range(pos, len(nums)):
        nums[i] = 0

    # Return the modified list
    return nums

'''
This function works in-place, meaning it modifies the input list directly and does not create any new lists. 
The time complexity is O(n), where n is the length of the list, because it makes a single pass over the list. 
The space complexity is O(1), because it uses a fixed amount of space to store the position pointer and does not 
depend on the size of the input list.
'''
import unittest

class TestMoveZeroes(unittest.TestCase):
    def test_move_zeroes(self):
        self.assertEqual(move_zeroes([0,1,0,3,12]), [1,3,12,0,0])
        self.assertEqual(move_zeroes([0,0,1]), [1,0,0])
        self.assertEqual(move_zeroes([2,1,0,3,0,12]), [2,1,3,12,0,0])
        self.assertEqual(move_zeroes([0,0,0,0,1]), [1,0,0,0,0])

if __name__ == '__main__':
    unittest.main()

'''
The function `move_zeroes(nums)` is designed to move all the zeros in the input list `nums` to the end while maintaining the relative order of the non-zero elements. 
Here's a detailed explanation of the code along with a diagram to visualize the process.

### Python Code Explanation

```python
def move_zeroes(nums):
    # Initialize position pointer
    pos = 0

    # Iterate over the list
    for i in range(len(nums)):
        # If the current element is not zero
        if nums[i] != 0:
            # Move the non-zero element to the position pointed by 'pos'
            nums[pos] = nums[i]
            # Increment 'pos'
            pos += 1

    # Fill the remaining positions with zeros
    for i in range(pos, len(nums)):
        nums[i] = 0

    # Return the modified list
    return nums
```

### Step-by-Step Explanation

1. **Initialize Position Pointer:**
   - `pos` is set to 0. This pointer keeps track of the position where the next non-zero element should be placed.

2. **First Iteration (Move Non-Zero Elements):**
   - The function iterates through the list using a for loop.
   - For each element, if it is not zero, it is moved to the position indicated by `pos`, and `pos` is incremented.
   
3. **Second Iteration (Fill Zeros):**
   - After the first iteration, all non-zero elements are moved to the front of the list, up to index `pos - 1`.
   - The function then iterates from `pos` to the end of the list, filling these positions with zeros.

### Diagram

Let's visualize the process with an example input: `[0, 1, 0, 3, 12]`.

#### Initial State:
```
Index: 0  1  2  3  4
nums:  [0, 1, 0, 3, 12]
pos:   0
```

#### First Iteration (Move Non-Zero Elements):

1. **i = 0:** 
   - `nums[0]` is 0, so `pos` remains 0.
   
2. **i = 1:** 
   - `nums[1]` is 1, so `nums[0]` is set to 1.
   - `pos` is incremented to 1.
   ```
   Index: 0  1  2  3  4
   nums:  [1, 1, 0, 3, 12]
   pos:   1
   ```
   
3. **i = 2:** 
   - `nums[2]` is 0, so `pos` remains 1.
   
4. **i = 3:** 
   - `nums[3]` is 3, so `nums[1]` is set to 3.
   - `pos` is incremented to 2.
   ```
   Index: 0  1  2  3  4
   nums:  [1, 3, 0, 3, 12]
   pos:   2
   ```
   
5. **i = 4:** 
   - `nums[4]` is 12, so `nums[2]` is set to 12.
   - `pos` is incremented to 3.
   ```
   Index: 0  1  2  3  4
   nums:  [1, 3, 12, 3, 12]
   pos:   3
   ```

#### Second Iteration (Fill Zeros):

- The second for loop runs from `pos = 3` to the end of the list, setting each element to 0.
```
Index: 0  1  2  3  4
nums:  [1, 3, 12, 0, 0]
```

### Final State:

The list after the function completes is `[1, 3, 12, 0, 0]`.

### Summary:

- The function effectively moves all non-zero elements to the beginning of the list while maintaining their order.
- It then fills the remaining positions with zeros.
- The overall time complexity is O(n), where n is the length of the list, as it requires two passes over the list.

This function is particularly useful for applications where maintaining the order of elements is crucial while eliminating zero values or any specific value considered as a placeholder.
'''
