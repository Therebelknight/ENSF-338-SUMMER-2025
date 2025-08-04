import timeit
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

class Binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key <= node.data:
            if node.left_child is None:
                node.left_child = Node(key)
            else:
                self._insert(node.left_child, key)
        else:
            if node.right_child is None:
                node.right_child = Node(key)
            else:
                self._insert(node.right_child, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.data == key:
            return node
        if key > node.data:
            return self._search(node.right_child, key)
        else:
            return self._search(node.left_child, key)

def binary_search(arr, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if key == arr[mid]:
        return mid
    elif key > arr[mid]:
        return binary_search(arr, key, mid + 1, high)
    else:
        return binary_search(arr, key, low, mid - 1)

def measure_binary_search_tree(shuffled):
    tree = Binary_search_tree()
    for x in shuffled:
        tree.insert(x)
    binary_search_tree_time = timeit.timeit(lambda: [tree.search(element) for element in shuffled], number=10)
    return binary_search_tree_time, binary_search_tree_time / 10

def measure_binary_search(shuffled):
    sorted_vec = sorted(shuffled)
    binary_search_time = timeit.timeit(lambda: [binary_search(sorted_vec, element, 0, len(sorted_vec) - 1) for element in shuffled], number=10)
    return binary_search_time, binary_search_time / 10

vec = list(range(10_000))
random.shuffle(vec)
total_tree_time, average_tree_time = measure_binary_search_tree(vec)
total_time, average_time = measure_binary_search(vec)

print(f"Binary Search Tree's average search time is {average_tree_time:.6f} seconds and the total search time is {total_tree_time:.6f}.")
print(f"Binary Search's average search time is {average_time:.6f} seconds and the total search time is {total_time:.6f}.")

# Question 4
# Binary search on a sorted array is significantly faster due to its logarithmic time complexity
# and efficient use of memory, as arrays are stored contiguously. In contrast, the binary search
# tree in this implementation is unbalanced, which can lead to degraded performance with linear
# time complexity in the worst case. Additionally, the tree structure introduces overhead from pointer-based
# navigation, making it less efficient overall.

