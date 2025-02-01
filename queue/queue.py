class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def _len__(self):
        # O(1)
        return self.size
    
    def __repr__(self):
        # O(N)
        items = []
        current_item = self.front

        while current_item is not None:
            items.append(current_item.value)
            current_item = current_item.next
        
        return ", ".join(str(i) for i in items)

    def enqueue(self, value):
        # O(1)
        new_node = Node(value)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1

    def dequeue(self):
        # O(1)
        if self.front is None:
            raise IndexError("queue is empty")
        
        dequeue_value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear is None
        
        self.size -= 1

        return dequeue_value

    def peek(self):
        # O(1)
        if self.front is None:
            raise IndexError("queue is empty")
        
        return self.front.value

    def is_empty(self) -> bool:
        # O(1)
        return self.front is None


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue({
        'company': 'shopify',
        'timestamp': '15 apr, 11.01 AM',
        'price': 131.1
    })
    queue.enqueue({
        'company': 'shopify',
        'timestamp': '15 apr, 11.02 AM',
        'price': 132
    })
    queue.enqueue({
        'company': 'shopify',
        'timestamp': '15 apr, 11.03 AM',
        'price': 135
    })

    print(queue)
    print("removing from queue...")
    print(queue.dequeue())
    print(queue.size)