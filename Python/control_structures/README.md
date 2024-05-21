### Control Structures in Python

Control structures in Python allow you to control the flow of your program’s execution. The primary control structures in Python include conditional statements and loops. Here, we’ll explore these control structures with complete real-world examples.

#### 1. Conditional Statements
Conditional statements allow you to execute code based on certain conditions. The primary conditional statements in Python are `if`, `elif`, and `else`.

**Example: A Simple E-commerce Discount System**

```python
# Define the total amount of purchase
total_amount = 150

# Apply discount based on the amount
if total_amount > 200:
    discount = 20  # 20% discount
elif total_amount > 100:
    discount = 10  # 10% discount
else:
    discount = 0   # No discount

# Calculate the final amount after discount
final_amount = total_amount - (total_amount * discount / 100)

print(f"Total Amount: ${total_amount}")
print(f"Discount Applied: {discount}%")
print(f"Final Amount to Pay: ${final_amount}")
```

In this example, the discount applied is based on the total amount of purchase.

#### 2. Loops
Loops allow you to execute a block of code repeatedly. Python provides `for` and `while` loops for this purpose.

**Example 1: Using a `for` Loop for a To-Do List Application**

```python
# Define a list of tasks
tasks = ["Send email to client", "Submit report", "Prepare presentation"]

# Iterate through the list and print each task
for task in tasks:
    print(f"Task: {task}")
```

This example iterates through a list of tasks and prints each task.

**Example 2: Using a `while` Loop for a Number Guessing Game**

```python
import random

# Generate a random number between 1 and 10
target_number = random.randint(1, 10)
attempts = 0

# Loop until the user guesses the correct number
while True:
    guess = int(input("Guess the number between 1 and 10: "))
    attempts += 1
    if guess < target_number:
        print("Too low! Try again.")
    elif guess > target_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
        break
```

In this example, the loop continues until the user guesses the correct number.

### Real-World Example: Customer Feedback System

Let’s combine conditional statements and loops to create a customer feedback system. This system will collect feedback from multiple customers and provide an average rating at the end.

```python
# Initialize variables to store total rating and number of feedbacks
total_rating = 0
feedback_count = 0

# Define a list of valid ratings
valid_ratings = [1, 2, 3, 4, 5]

# Loop to collect feedback from multiple customers
while True:
    rating = int(input("Please rate our service (1-5): "))
    if rating in valid_ratings:
        total_rating += rating
        feedback_count += 1
    else:
        print("Invalid rating. Please enter a rating between 1 and 5.")
    
    # Ask if there are more customers
    more_customers = input("Are there more customers to rate? (yes/no): ").lower()
    if more_customers != "yes":
        break

# Calculate the average rating
if feedback_count > 0:
    average_rating = total_rating / feedback_count
    print(f"Total feedbacks: {feedback_count}")
    print(f"Average Rating: {average_rating:.2f}")
else:
    print("No feedbacks received.")
```

In this example:
- We use a `while` loop to continuously collect feedback until no more customers are available.
- Conditional statements check for valid ratings and control the flow based on user input.
- At the end, we calculate and display the average rating based on the collected feedback.

These examples illustrate the use of control structures in real-world scenarios, highlighting how conditional statements and loops can be used to manage program flow effectively.


### Python provides several types of loops to handle repetitive tasks efficiently. The primary loops in Python are `for` loops and `while` loops. Additionally, there are control statements like `break`, `continue`, and `pass` that help in managing these loops.

### 1. `for` Loop

The `for` loop in Python is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string).

**Example: Processing a List of Student Grades**

Imagine we have a list of student grades, and we want to calculate the average grade.

```python
# List of student grades
grades = [85, 92, 78, 90, 88]

# Initialize total to 0
total = 0

# Iterate through the grades list
for grade in grades:
    total += grade

# Calculate average
average = total / len(grades)

print(f"The average grade is {average:.2f}")
```

In this example:
- The `for` loop iterates over each grade in the `grades` list.
- We accumulate the total of grades and then compute the average.

### 2. `while` Loop

The `while` loop in Python repeatedly executes a block of code as long as a given condition is true.

**Example: ATM Withdrawal Simulation**

Consider an ATM simulation where a user can withdraw money until their balance is zero.

```python
# Initial balance
balance = 500

# Loop until balance is zero
while balance > 0:
    # Prompt user for withdrawal amount
    withdrawal = int(input("Enter the amount to withdraw: "))
    
    if withdrawal > balance:
        print("Insufficient balance! Try a smaller amount.")
    else:
        balance -= withdrawal
        print(f"Withdrawal successful! Remaining balance: ${balance}")
    
    if balance == 0:
        print("Your account balance is zero. No further withdrawals possible.")
        break
```

In this example:
- The `while` loop runs as long as the balance is greater than zero.
- Inside the loop, the user is prompted to enter an amount to withdraw, and the balance is updated accordingly.

### 3. `break` Statement

The `break` statement is used to exit a loop prematurely when a certain condition is met.

**Example: Finding the First Even Number in a List**

```python
# List of numbers
numbers = [1, 3, 7, 9, 12, 15]

# Loop through the list
for number in numbers:
    if number % 2 == 0:
        print(f"First even number found: {number}")
        break
```

In this example:
- The loop iterates through the `numbers` list.
- When an even number is found, the `break` statement exits the loop.

### 4. `continue` Statement

The `continue` statement skips the current iteration and moves to the next iteration of the loop.

**Example: Skipping Negative Numbers in a List**

```python
# List of integers
numbers = [5, -3, 8, -1, 12, -7, 9]

# Loop through the list
for number in numbers:
    if number < 0:
        continue
    print(f"Processing number: {number}")
```

In this example:
- The loop processes each number in the `numbers` list.
- If a number is negative, the `continue` statement skips the current iteration.

### 5. `pass` Statement

The `pass` statement is a null operation; it is used as a placeholder for future code.

**Example: Placeholders in a Loop**

```python
# List of tasks
tasks = ["task1", "task2", "task3"]

# Loop through tasks
for task in tasks:
    if task == "task2":
        pass  # Placeholder for future code
    else:
        print(f"Executing {task}")
```

In this example:
- The `pass` statement acts as a placeholder for future code where additional logic for "task2" might be implemented later.

### Real-World Example: Inventory Management System

Let’s create a small inventory management system that uses different loops and control statements.

```python
# Sample inventory
inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}

# Main loop to manage inventory
while True:
    print("\nCurrent Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")
    
    action = input("Enter action (add/remove/check/exit): ").lower()
    
    if action == "exit":
        print("Exiting the inventory management system.")
        break
    
    elif action == "add":
        item = input("Enter the item to add: ").lower()
        quantity = int(input(f"Enter the quantity of {item} to add: "))
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity
        print(f"Added {quantity} of {item}.")
    
    elif action == "remove":
        item = input("Enter the item to remove: ").lower()
        if item in inventory:
            quantity = int(input(f"Enter the quantity of {item} to remove: "))
            if quantity > inventory[item]:
                print("Insufficient quantity to remove.")
            else:
                inventory[item] -= quantity
                print(f"Removed {quantity} of {item}.")
        else:
            print(f"{item} not found in inventory.")
    
    elif action == "check":
        item = input("Enter the item to check: ").lower()
        if item in inventory:
            print(f"{item}: {inventory[item]}")
        else:
            print(f"{item} not found in inventory.")
    
    else:
        print("Invalid action. Please try again.")
```

In this comprehensive example:
- A `while` loop is used to continuously manage the inventory until the user decides to exit.
- `for` loops display the current inventory.
- `if` and `elif` statements handle different actions like adding, removing, and checking items in the inventory.
- `break` statement is used to exit the loop when the user chooses to do so.

### In Python, `for` loops are used to iterate over a sequence of elements, such as lists, tuples, strings, dictionaries, sets, and even custom iterable objects. Here are different types of `for` loops in Python with detailed real-world examples.

### 1. Iterating Over a List

**Example: Sending Emails to a List of Users**

Imagine you have a list of email addresses and you want to send a message to each one.

```python
emails = ["alice@example.com", "bob@example.com", "charlie@example.com"]

for email in emails:
    print(f"Sending email to {email}")
```

In this example:
- The `for` loop iterates over each email in the `emails` list and prints a message for each one.

### 2. Iterating Over a Tuple

**Example: Processing Coordinates**

You have a tuple of coordinates and you want to process each coordinate.

```python
coordinates = [(1, 2), (3, 4), (5, 6)]

for x, y in coordinates:
    print(f"Coordinate: x={x}, y={y}")
```

In this example:
- The `for` loop iterates over each tuple in the `coordinates` list and unpacks the values.

### 3. Iterating Over a Dictionary

**Example: Inventory Management**

You have a dictionary representing an inventory and you want to print each item and its quantity.

```python
inventory = {"apple": 10, "banana": 5, "orange": 8}

for item, quantity in inventory.items():
    print(f"Item: {item}, Quantity: {quantity}")
```

In this example:
- The `for` loop iterates over each key-value pair in the `inventory` dictionary.

### 4. Iterating Over a String

**Example: Counting Vowels in a String**

You want to count the number of vowels in a given string.

```python
text = "Hello, World!"
vowels = "aeiouAEIOU"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

print(f"Number of vowels: {vowel_count}")
```

In this example:
- The `for` loop iterates over each character in the `text` string and counts the vowels.

### 5. Iterating Over a Set

**Example: Checking Unique Elements**

You have a set of unique IDs and you want to verify each one.

```python
unique_ids = {101, 102, 103, 104}

for uid in unique_ids:
    print(f"Verifying ID: {uid}")
```

In this example:
- The `for` loop iterates over each unique ID in the `unique_ids` set.

### 6. Using `range()`

**Example: Generating a Sequence of Numbers**

You want to generate a sequence of numbers from 0 to 9.

```python
for i in range(10):
    print(f"Number: {i}")
```

In this example:
- The `for` loop iterates over a sequence of numbers generated by `range(10)`.

### 7. Nested `for` Loops

**Example: Multiplication Table**

You want to create a multiplication table.

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print("-----")
```

In this example:
- The outer `for` loop iterates over the numbers 1 to 5.
- The inner `for` loop also iterates over the numbers 1 to 5, creating a multiplication table.

### 8. List Comprehensions

**Example: Squaring Numbers**

You want to create a list of squares for the numbers 1 to 5.

```python
squares = [x ** 2 for x in range(1, 6)]
print(squares)
```

In this example:
- A list comprehension is used to create a list of squared numbers.

### 9. Enumerate

**Example: Indexing a List**

You want to print each item in a list along with its index.

```python
items = ["apple", "banana", "cherry"]

for index, item in enumerate(items):
    print(f"Index: {index}, Item: {item}")
```

In this example:
- The `enumerate` function is used to get both the index and value of each item in the `items` list.

### 10. Zipping Lists

**Example: Pairing Items from Two Lists**

You have two lists, one with names and one with scores, and you want to pair them.

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"Name: {name}, Score: {score}")
```

In this example:
- The `zip` function is used to pair items from the `names` and `scores` lists.

### Real-World Example: Analyzing Sales Data

Let’s create a comprehensive example that uses different types of `for` loops to analyze sales data.

```python
# Sales data for each region
sales_data = {
    "North": [1200, 1300, 1150, 1400],
    "South": [1000, 950, 1050, 1100],
    "East": [1150, 1250, 1200, 1300],
    "West": [1300, 1350, 1400, 1450]
}

# Initialize total sales
total_sales = 0
region_count = 0

# Iterate over each region and their sales
for region, sales in sales_data.items():
    print(f"Region: {region}")
    
    # Calculate total sales for the region
    region_total = sum(sales)
    total_sales += region_total
    region_count += 1
    
    # Calculate average sales for the region
    region_average = region_total / len(sales)
    
    print(f"Total Sales: {region_total}")
    print(f"Average Sales: {region_average:.2f}\n")

# Calculate overall average sales
overall_average = total_sales / region_count
print(f"Overall Total Sales: {total_sales}")
print(f"Overall Average Sales: {overall_average:.2f}")
```

In this example:
- We iterate over a dictionary of sales data using a `for` loop.
- We calculate and print the total and average sales for each region.
- We also calculate the overall total and average sales across all regions.

This comprehensive guide demonstrates the versatility of `for` loops in Python and how they can be applied to various real-world scenarios.

### In Python, the `range()` function is commonly used with loops, especially `for` loops, to generate a sequence of numbers. Here are different ways to use `range()` with loops along with detailed real-world examples:

### 1. Basic `for` Loop with `range()`

**Example: Printing Numbers from 0 to 9**

```python
for i in range(10):
    print(i)
```

In this example:
- `range(10)` generates numbers from 0 to 9.
- The `for` loop iterates over this sequence, printing each number.

### 2. Specifying Start and Stop

**Example: Printing Numbers from 5 to 14**

```python
for i in range(5, 15):
    print(i)
```

In this example:
- `range(5, 15)` generates numbers from 5 to 14.
- The `for` loop iterates over this range, printing each number.

### 3. Specifying Start, Stop, and Step

**Example: Printing Even Numbers from 0 to 18**

```python
for i in range(0, 20, 2):
    print(i)
```

In this example:
- `range(0, 20, 2)` generates numbers from 0 to 18 in steps of 2.
- The `for` loop iterates over this sequence, printing each even number.

### 4. Reverse Iteration

**Example: Countdown from 10 to 1**

```python
for i in range(10, 0, -1):
    print(i)
```

In this example:
- `range(10, 0, -1)` generates numbers from 10 to 1 in reverse order.
- The `for` loop iterates over this sequence, printing each number.

### Real-World Examples Using `range()`

### 1. Generating a Sequence of IDs

**Example: Assigning IDs to New Employees**

```python
employee_count = 5
employee_ids = []

for i in range(1, employee_count + 1):
    employee_ids.append(f"EMP{i:03}")

print(employee_ids)
```

In this example:
- `range(1, employee_count + 1)` generates numbers from 1 to the number of employees.
- Each number is used to create a unique employee ID in the format `EMP001`, `EMP002`, etc.

### 2. Creating a Multiplication Table

**Example:  Multiplication Table for a Given Number**

```python
number = 7
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
```

In this example:
- `range(1, 11)` generates numbers from 1 to 10.
- The `for` loop iterates over this range, printing the multiplication table for the specified number.

### 3. Simulating a Simple Voting System

**Example: Collecting Votes for Candidates**

```python
candidates = ["Alice", "Bob", "Charlie"]
votes = [0] * len(candidates)

# Simulate voting
num_voters = 10

for i in range(num_voters):
    vote = int(input(f"Voter {i + 1}, vote for (0: Alice, 1: Bob, 2: Charlie): "))
    if 0 <= vote < len(candidates):
        votes[vote] += 1
    else:
        print("Invalid vote.")

# Display voting results
for i in range(len(candidates)):
    print(f"{candidates[i]}: {votes[i]} votes")
```

In this example:
- `range(num_voters)` generates numbers from 0 to the number of voters minus one.
- The `for` loop simulates each voter casting a vote and increments the corresponding candidate's vote count.

### 4. Generating Fibonacci Series

**Example: Generating First N Fibonacci Numbers**

```python
n = 10
fib_series = [0, 1]

for i in range(2, n):
    next_number = fib_series[-1] + fib_series[-2]
    fib_series.append(next_number)

print(f"First {n} Fibonacci numbers: {fib_series}")
```

In this example:
- `range(2, n)` generates numbers from 2 to n-1.
- The `for` loop calculates the next Fibonacci number by summing the last two numbers in the series and appends it to the list.

### 5. Processing Multiple Files

**Example: Renaming a Batch of Files**

```python
import os

files = ["report1.txt", "report2.txt", "report3.txt"]

for i in range(len(files)):
    new_name = f"renamed_report_{i + 1}.txt"
    os.rename(files[i], new_name)
    print(f"Renamed {files[i]} to {new_name}")
```

In this example:
- `range(len(files))` generates indices from 0 to the length of the files list minus one.
- The `for` loop iterates over each file, renaming it according to the new naming convention.

### 6. Generating Random Data

**Example: Generating Random Test Scores for Students**

```python
import random

num_students = 5
test_scores = []

for i in range(num_students):
    score = random.randint(50, 100)
    test_scores.append(score)

print(f"Generated test scores: {test_scores}")
```

In this example:
- `range(num_students)` generates numbers from 0 to the number of students minus one.
- The `for` loop generates a random test score for each student and appends it to the list.

### 7. Analyzing Temperature Data

**Example: Calculating Average Temperature Over a Week**

```python
temperatures = [70, 72, 68, 65, 74, 73, 71]

total_temp = 0

for temp in range(len(temperatures)):
    total_temp += temperatures[temp]

average_temp = total_temp / len(temperatures)
print(f"The average temperature over the week is {average_temp:.2f}°F")
```

In this example:
- `range(len(temperatures))` generates indices from 0 to the length of the temperatures list minus one.
- The `for` loop calculates the total temperature, which is then used to compute the average.

These examples demonstrate the flexibility and utility of the `range()` function in various real-world scenarios, showing how it can be used to generate sequences for iteration and automate repetitive tasks.
