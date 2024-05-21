def two_sum(nums, target):
    # Create a dictionary to store the numbers and their indices
    num_to_index = {}

    # Iterate through the array
    for index, num in enumerate(nums):
        # Calculate the complement that would add up to the target with the current number
        complement = target - num

        # Check if the complement is already in the dictionary
        if complement in num_to_index:
            # If found, return the indices of the complement and the current number
            return [num_to_index[complement], index]

        # If not found, store the current number and its index in the dictionary
        num_to_index[num] = index

    # If no solution is found, return an empty list
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(f"Indices of numbers that add up to {target} are: {result}")
# Output: Indices of numbers that add up to 9 are: [0, 1]


'''
Explanation:
Initialize Dictionary:

We create an empty dictionary num_to_index to keep track of the numbers we've seen and their corresponding indices.
Iterate Through the Array:

We use enumerate to get both the index and the value of each element in the array nums.
Calculate the Complement:

For each number num, we calculate its complement as target - num.
Check for the Complement:

We check if the complement is already in the dictionary num_to_index.
If the complement exists, it means we have found the two numbers that add up to the target. We return the indices of the complement and the current number.
Store the Number and Index:

If the complement is not found, we store the current number and its index in the dictionary num_to_index.
Return Result:

If the loop completes without finding a solution, we return an empty list (though the problem guarantees that there will be a solution, so this line may not be necessary).
Example Walkthrough:
Let's walk through the example nums = [2, 7, 11, 15] with target = 9.

First Iteration:

index = 0, num = 2
complement = 9 - 2 = 7
7 is not in num_to_index
Add 2 to num_to_index with index 0: {2: 0}
Second Iteration:

index = 1, num = 7
complement = 9 - 7 = 2
2 is in num_to_index with index 0
Return [0, 1]
The solution is found in the second iteration, where the numbers at indices 0 and 1 (i.e., 2 and 7) add up to the target 9.

This approach efficiently finds the solution in O(n) time complexity by leveraging the hash table for constant time lookups.
'''

import unittest

def two_sum(nums, target):
    # Create a dictionary to store the numbers and their indices
    num_to_index = {}

    # Iterate through the array
    for index, num in enumerate(nums):
        # Calculate the complement that would add up to the target with the current number
        complement = target - num

        # Check if the complement is already in the dictionary
        if complement in num_to_index:
            # If found, return the indices of the complement and the current number
            return [num_to_index[complement], index]

        # If not found, store the current number and its index in the dictionary
        num_to_index[num] = index

    # If no solution is found, return an empty list
    return []

class TestTwoSum(unittest.TestCase):
    def test_example_case(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(two_sum(nums, target), [0, 1])

    def test_multiple_solutions(self):
        nums = [1, 2, 3, 4, 5]
        target = 6
        self.assertIn(two_sum(nums, target), [[1, 3], [2, 4]])

    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8
        self.assertEqual(two_sum(nums, target), [2, 4])

    def test_zero_sum(self):
        nums = [0, 4, 3, 0]
        target = 0
        self.assertEqual(two_sum(nums, target), [0, 3])

    def test_large_numbers(self):
        nums = [1000000, 500000, 500000]
        target = 1000000
        self.assertEqual(two_sum(nums, target), [1, 2])

    def test_no_solution(self):
        # Even though the problem guarantees a solution, we'll add a test case for robustness.
        nums = [1, 2, 3]
        target = 7
        self.assertEqual(two_sum(nums, target), [])

    def test_identical_numbers(self):
        nums = [3, 3]
        target = 6
        self.assertEqual(two_sum(nums, target), [0, 1])

if __name__ == '__main__':
    unittest.main()
'''
Explanation of Unit Test Cases
test_example_case:

Tests the basic example provided in the problem statement.
nums = [2, 7, 11, 15] and target = 9 should return [0, 1].
test_multiple_solutions:

Tests a case where there are multiple possible pairs that add up to the target.
nums = [1, 2, 3, 4, 5] and target = 6 could return either [1, 3] or [2, 4].
test_negative_numbers:

Tests a case with negative numbers.
nums = [-1, -2, -3, -4, -5] and target = -8 should return [2, 4].
test_zero_sum:

Tests a case where the target sum is zero and includes zero in the list.
nums = [0, 4, 3, 0] and target = 0 should return [0, 3].
test_large_numbers:

Tests a case with large numbers.
nums = [1000000, 500000, 500000] and target = 1000000 should return [1, 2].
test_no_solution:

Although the problem guarantees a solution, this tests robustness for cases with no solution.
nums = [1, 2, 3] and target = 7 should return [].
test_identical_numbers:

Tests a case with identical numbers that add up to the target.
nums = [3, 3] and target = 6 should return [0, 1].
Running the Tests
To run these tests, save the code to a Python file (e.g., test_two_sum.py) and run it using the following command:

bash
Copy code
python -m unittest test_two_sum.py
This will execute the unit tests and display the results, indicating which tests passed and which (if any) failed.
'''