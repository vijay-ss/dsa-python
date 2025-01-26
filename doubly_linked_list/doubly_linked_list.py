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
    
    def delete_by_key(self, key) -> None:
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

    def delete_node(self, node) -> None:
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
            if cur == node and cur == self.head:
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

            elif cur == node:
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

    def reverse(self) -> None:
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev

    def remove_duplicates(self) -> None:
        cur = self.head
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt

    def pairs_with_sum(self, sum_val) -> None:
        pairs = list()
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_val:
                    pairs.append((p.data, q.data))
                q = q.next
            p = p.next
        
        return pairs

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
    dll.append(3)
    dll.append(4)
    dll.remove_duplicates()
    dll.print_list()
    print(dll.pairs_with_sum(5))
    # print("printing reverse")
    # dll.reverse()