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
