class MinHeap:
    def __init__(self):
        self.heap = []
    
    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return str(self.heap)

    def insert(self, key, value):
        # O(log n)
        self.heap.append([key, value])
        self._sift_up(len(self.heap) - 1)

    def peek_min(self, key):
        # O(1)
        if not self.heap:
            raise IndexError("empty heap")
        return self.heap[0]

    def extract_min(self):
        # O(log n)
        if not self.heap:
            raise IndexError("empty heap")

        min_element = self.heap[0]
        last_element = self.heap.pop()

        if self.heap:
            self.heap[0] = last_element
            self._sift_down(0)
        
        return min_element

    def heapify(self, elements: list):
        # O(n)
        self.heap = list(elements)

        for i in reversed(range(self._parent(len(self.heap) - 1) + 1)):
            self._sift_down(i)

    def meld(self, other_heap):
        # O(n)
        combined_heap = self.heap + other_heap.heap
        self.heapify(combined_heap)

        other_heap.heap = []

    def _parent(self, index):
        # O(1)
        return (index + 1) // 2 if index != 0 else None

    def _left(self, index):
        # O(1)
        left = 2 * index + 1
        return left if left < len(self.heap) else None

    def _right(self, index):
        # O(1)
        right = 2 * index + 2
        return right if right < len(self.heap) else None

    def _sift_up(self, index):
        # O(log n)
        # swim
        parent_index = self._parent(index)

        while parent_index is not None and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = self._parent(index)

    def _sift_down(self, index):
        # O(log n)
        # sink
        while True:
            smallest = index

            left = self._left(index)
            right = self._right(index)

            if left is not None and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left

            if right is not None and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            
            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]

if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.heapify([[10, "10"], [9, "9"], [8, "8"], [7, "7"]])
    print(min_heap)

    import heapq
    my_list = [10, 9, 8, 7]
    heapq.heapify([10, 9, 8, 7])
    print(my_list)
