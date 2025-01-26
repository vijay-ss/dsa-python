class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        
        itr = self.head
        ll_str = ""
        while itr:
            ll_str += str(itr.data) + " --> " if itr.next else str(itr.data)
            itr = itr.next
        print(ll_str)

    def get_length(self) -> int:
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next
        
        return count
    
    def insert_at_beginning(self, data: any) -> None:
        node = Node(data, self.head)
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
                itr.next = node
                break
        
            itr = itr.next
            count += 1
    
    def insert_after_value(self, data_after, data_to_insert) -> None:
        if self.head is None:
            return
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next


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
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1
    
    def remove_by_value(self, data) -> None:
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")
    ll.print()
    ll.remove_by_value("orange")
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()