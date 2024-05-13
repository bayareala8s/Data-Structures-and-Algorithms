### Queue

A queue is a linear data structure that follows a specific order in which operations are performed. The order is First In First Out (FIFO). This means that the data that is added first will be the first one to be removed. This is similar to a real-world queue, such as people standing in line to buy tickets for a concert - the person who comes first gets the ticket first.

The main operations of a queue are:

1. **Enqueue**: Adds an element to the end of the queue. This operation inserts an element at the rear of the queue.

2. **Dequeue**: Removes an element from the front of the queue. This operation removes an element from the front of the queue and returns it.

3. **IsEmpty**: Checks if the queue is empty. This operation returns true if the queue is empty and false otherwise.

4. **IsFull**: Checks if the queue is full. This operation returns true if the queue is full and false otherwise. This is more relevant in the context of a queue implemented using an array with a fixed size.

5. **Peek/Front**: Gets the value of the front of the queue without removing it. This operation returns the front element of the queue.


Here is a basic implementation of a queue in Python:

