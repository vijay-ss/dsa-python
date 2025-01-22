class Node:
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def print_forward(self):
        if self.head is None:
            print("linked list is empty")
            return
        
        itr = self.head
        ll_str = ""
        while itr:
            ll_str += str(itr.data) + " <--> " if itr.next else str(itr.data)
            itr = itr.next
        print(ll_str)
    
    def print_backward(self):
        if self.head is None:
            print("linked list is empty")
            return
        
        last_node = self.get_last_node()
        itr = last_node
        ll_str = ""
        while itr:
            ll_str += itr.data + " <--> "
            itr = itr.prev
        print(f"linked list in reverse: {ll_str}")
    
    def get_last_node(self):
        itr = self.head
        while itr:
            itr = itr.next
        
        return itr

    def get_length(self) -> int:
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next
        
        return count
    
    def insert_at_beginning(self, data: any) -> None:
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = Node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
    
    def insert_at_end(self, data: any) -> None:
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
    
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def insert_at(self, index: int, data: any) -> None:
        if index < 0 or index > self.get_length():
            raise Exception("invalid index!")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
        
            itr = itr.next
            count += 1


    def insert_values(self, data_list: list[any]) -> None:
        """Removes/replaces all values in the linked list
        with a new list of values.
        """
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid index!")
        
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count += 1


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()