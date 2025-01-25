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
    
    def delete(self, key) -> None:
        """
        case 1:
            - node is head of the linked list
            - absence of next node
        case 2:
            - want to delete head node, which
            points to a next node
        case 3:
            - we dont want to remove the head node
            - next & prev node is not None
        case 4:
            - we dont want to remove the head node
            - we want to remove the last node
        """
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                else:
                    next = cur.next
                    cur.next = None
                    next.prev = None
                    cur = None
                    self.head = next
                    return

            elif cur.data == key:
                if cur.next:
                    next = cur.next
                    prev = cur.prev
                    prev.next = next
                    next.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
            
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return

            cur = cur.next


                    

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.delete(3)

    dll.print_list()