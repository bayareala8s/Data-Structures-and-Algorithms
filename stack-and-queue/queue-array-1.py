 

class EmptyQueueError(Exception):
    pass

class Queue:
    
    def __init__(self):
        self.items = [] 
        self.front = 0
      
    def is_empty(self):
        return self.front == len(self.items)
    
    def size(self):
        return len(self.items)-self.front
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        
        x = self.items[self.front]
        self.items[self.front] = None
        self.front = self.front + 1
        return x
    
    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        
        return self.items[self.front]
        
    def display(self):
        print(self.items)
                     
###########################################################

if __name__ == "__main__":
    qu = Queue()

    while True:
        print("1.Enqueue") 
        print("2.Dequeue")
        print("3.Peek")
        print("4.Size") 
        print("5.Display")  
        print("6.Quit") 
         
        choice = int(input("Enter your choice : "))

        if choice == 1:
            x=int(input("Enter the element : "))
            qu.enqueue(x) 
        elif choice == 2:
            x=qu.dequeue() 
            print("Element deleted from the queue is : " , x) 
        elif choice == 3:
            print("Element at the front end is " , qu.peek()) 
        elif choice == 4:
            print("Size of queue ", qu.size()) 
        elif choice == 5:
            qu.display() 
        elif choice == 6:
          break;
        else:
          print("Wrong choice") 
        print()

