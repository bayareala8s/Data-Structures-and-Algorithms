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


###Python provides several types of loops to handle repetitive tasks efficiently. The primary loops in Python are `for` loops and `while` loops. Additionally, there are control statements like `break`, `continue`, and `pass` that help in managing these loops.

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
