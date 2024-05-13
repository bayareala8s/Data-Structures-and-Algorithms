### Queue

A queue is a linear data structure that follows a specific order in which operations are performed. The order is First In First Out (FIFO). This means that the data that is added first will be the first one to be removed. This is similar to a real-world queue, such as people standing in line to buy tickets for a concert - the person who comes first gets the ticket first.

The main operations of a queue are:

1. **Enqueue**: Adds an element to the end of the queue. This operation inserts an element at the rear of the queue.

2. **Dequeue**: Removes an element from the front of the queue. This operation removes an element from the front of the queue and returns it.

3. **IsEmpty**: Checks if the queue is empty. This operation returns true if the queue is empty and false otherwise.

4. **IsFull**: Checks if the queue is full. This operation returns true if the queue is full and false otherwise. This is more relevant in the context of a queue implemented using an array with a fixed size.

5. **Peek/Front**: Gets the value of the front of the queue without removing it. This operation returns the front element of the queue.


Here is a Python implementation of a Queue using an array (list in Python). In this implementation, the front of the queue is at the beginning of the list for efficient dequeue operations.

```python
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """
        This method adds an item to the end of the queue.
        """
        self.queue.append(item)

    def dequeue(self):
        """
        This method removes an item from the front of the queue.
        """
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        """
        This method returns the number of items in the queue.
        """
        return len(self.queue)

    def is_empty(self):
        """
        This method checks if the queue is empty.
        """
        return self.size() == 0

    def peek(self):
        """
        This method returns the item at the front of the queue without removing it.
        """
        if self.is_empty():
            return None
        return self.queue[0]
```

Now, let's create a real-world example. We'll use the queue to simulate a printer queue. This is a common use case for a queue because a printer can only handle one print job at a time, so print jobs are processed in the order they are received.

```python
def printer_queue(queue, jobs):
    """
    This function simulates a printer queue.
    """
    # Add all print jobs to the queue
    for job in jobs:
        queue.enqueue(job)

    while not queue.is_empty():
        # Process the next job in the queue
        current_job = queue.dequeue()
        print(f"Processing job: {current_job}")

# Create a new queue
queue = Queue()

# Simulate a printer queue
print_jobs = ["job1", "job2", "job3", "job4", "job5"]
printer_queue(queue, print_jobs)
```

In this example, we first add all the print jobs to the queue. Then, we process each job in the order they were received until the queue is empty. Since a queue is a FIFO (first in, first out) data structure, the jobs are processed in the order they were added to the queue.


### Common operations performed on a queue

1. **Enqueue**: This operation adds an element to the end of the queue.

2. **Dequeue**: This operation removes an element from the front of the queue.

3. **Peek/Front**: This operation returns the first element of the queue without removing it.

4. **IsEmpty**: This operation checks if the queue is empty.

5. **IsFull**: This operation checks if the queue is full. This is more relevant in the context of a queue implemented using an array with a fixed size.

6. **Size**: This operation returns the number of elements in the queue.

