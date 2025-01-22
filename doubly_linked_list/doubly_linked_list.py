class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        return f"prev: {self.prev}, next: {self.next}, data: {self.data}"

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data) -> None:
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
    
    def prepend(self, data) -> None:
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
    
    def add_after_node(self, key, data) -> None:
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                next = cur.next
                cur.next = new_node
                new_node.next = next
                new_node.prev = cur
                next.prev = new_node
                # print(new_node.__str__())

            cur = cur.next

    def add_before_node(self, key, data) -> None:
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev
            
            cur = cur.next

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.prepend(0)
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.prepend(-1)
    dll.add_after_node(1, 11)
    dll.add_after_node(3, 99)
    dll.add_before_node(3, 77)

    dll.print_list()