class Heap:
    def __init__(self):
        # Initializing the storage array to represent the heap
        self.storage = []

    def heapify(self, array):
        # Copy the input array to internal storage
        self.storage = array[:]
        # Apply move-down starting from the last non-leaf node to the root
        for i in reversed(range(len(self.storage)//2)):
            self.move_down(i)

    def enqueue(self, value):
        # Add new value to the end of the heap
        self.storage.append(value)
        # Restore heap property by moving it up as needed
        self.move_up(len(self.storage) - 1)

    def dequeue(self):
        # Remove and return the smallest element
        if not self.storage:
            return None
        root = self.storage[0]
        last = self.storage.pop()  # Remove last element
        if self.storage:
            # Replace root with the last element and fix the heap
            self.storage[0] = last
            self.move_down(0)
        return root

    def move_up(self, index):
        # Move element at index up until heap property is restored
        parent = (index - 1) // 2
        while index > 0 and self.storage[index] < self.storage[parent]:
            # Swap with parent if smaller
            self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
            index = parent
            parent = (index - 1) // 2

    def move_down(self, index):
        # Move element at index down until heap property is restored
        size = len(self.storage)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            # Find smallest among index, left, and right children
            if left < size and self.storage[left] < self.storage[smallest]:
                smallest = left
            if right < size and self.storage[right] < self.storage[smallest]:
                smallest = right

            # If already in correct place stop
            if smallest == index:
                break

            # Otherwise swap and continue
            self.storage[index], self.storage[smallest] = self.storage[smallest], self.storage[index]
            index = smallest

def test_heapify_sorted_heap():
    h = Heap()
    input_array = [1, 3, 5, 7, 9, 11]
    h.heapify(input_array)
    assert h.storage == [1, 3, 5, 7, 9, 11]
    print("Test for sorted passed")

def test_heapify_empty_array():
    h = Heap()
    h.heapify([])
    assert h.storage == []
    print("Test for empty passed")

def test_heapify_random_array():
    h = Heap()
    input_array = [10, 3, 5, 1, 8, 6]
    h.heapify(input_array)

    # Check all elements are still present
    assert sorted(h.storage) == sorted(input_array)

    # Dequeue to verify heap property
    output = []
    while h.storage:
        output.append(h.dequeue())

    assert output == sorted(input_array)
    print("Test for random passed")

try:
    test_heapify_sorted_heap()
    test_heapify_empty_array()
    test_heapify_random_array()
    print("All tests passed!")
except AssertionError:
    print("One or more tests failed.")
