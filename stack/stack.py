class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0
    
    def __len__(self):
        # O(1)
        return self.size
    
    def __repr__(self) -> str:
        # O(N)
        items = []
        current_item = self.top

        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next
        
        return "(top) "  + ", ".join(items)
    
    def push(self, value):
        # O(1)
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

        self.size += 1

    def pop(self):
        # O(1)
        if self.top is None:
            raise ValueError("stack is empty")
        
        pop_value = self.top.value
        self.top = self.top.next

        self.size -= 1

        return pop_value

    def peek(self):
        # O(1)
        if self.top is None:
            raise ValueError("stack is empty")
        
        return self.top.value

    def is_empty(self) -> bool:
        # O(1)
        return self.top is None


def reverse_string(stack: Stack, input_str: str) -> str:
    for i in input_str:
        stack.push(i)

    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    stack.push(1)
    stack.push(5)
    stack.push(34)
    stack.push(99)
    stack.push(7)
    print(stack)
    print(stack.peek())
    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.is_empty())

    stack = Stack()
    print(reverse_string(stack, "Hello"))