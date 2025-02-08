class Node:

    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.value = None

    def __repr__(self):
        return f"{self.key}, {self.value}"

class BinarySearchTree:

    def __init__(self):
        self.root = None
    
    def __contains__(self, key):
        pass

    def __iter__(self):
        pass

    def __repr__(self):
        pass

    def insert(self, key, value):
        pass

    def search(self, key):
        pass

    def delete(self, key):
        pass

    def traverse(self, order):
        pass

    def _delete(self, key):
        pass

    def _successor(self, node):
        pass

    def _predecessor(self, node):
        pass

    def _in_order_traversal(self):
        pass

    def _pre_order_traversal(self):
        pass

    def _post_order_traversal(self):
        pass



if __name__ == "__main__":
    tree = BinarySearchTree()