import timeit
import random
import sys
sys.setrecursionlimit(20000)


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

def measure_binary_search_tree(vec):
    tree = Binary_search_tree()
    for x in vec:
        tree.insert(x)
    binary_search_tree_time = timeit.timeit(lambda: [tree.search(element) for element in vec], number=10)
    return binary_search_tree_time, binary_search_tree_time / 10

vec = list(range(10_000))
total_time_sorted, average_time_sorted = measure_binary_search_tree(vec)
random.shuffle(vec)
total_time_shuffled, average_time_shuffled = measure_binary_search_tree(vec)

print(f"\nTime performance with a sorted vector || Average= {average_time_sorted} || Total= {total_time_sorted}")
print(f"\nTime performance with a shuffled vector || Average= {average_time_shuffled} || Total= {total_time_shuffled}")

# Question 4
# Inserting sorted data into a binary search tree leads to an unbalanced structure that resembles a linked list,
# causing search operations to take linear time. This is because each new element becomes the right child of the
# previous one, increasing the tree’s depth. In contrast, inserting shuffled data results in a more balanced tree,
# where nodes are distributed more evenly, allowing searches to complete in logarithmic time. As a result, the tree built
# from shuffled data performs significantly better, with faster average and total search times.
