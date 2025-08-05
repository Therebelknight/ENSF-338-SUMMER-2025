import random
import timeit
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def height(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)

    def balance(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return left_height - right_height


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.nodes = []

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            self.nodes.append(self.root)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.data:
            if node.left is None:
                node.left = Node(key)
                self.nodes.append(node.left)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
                self.nodes.append(node.right)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        while node:
            if key == node.data:
                return node
            elif key < node.data:
                node = node.left
            else:
                node = node.right
        return None

    def get_max_absolute_balance(self):
        return max(abs(node.balance()) for node in self.nodes)

tree = BinarySearchTree()
for i in range(1000):
    tree.insert(i)

tasks = []
original_list = list(range(1000))
for _ in range(1000):
    shuffled = original_list[:]
    random.shuffle(shuffled)
    tasks.append(shuffled)

search_times = []
max_balances = []

for task in tasks:
    start_time = timeit.default_timer()
    for key in task:
        tree.search(key)
    end_time = timeit.default_timer()

    elapsed_time = end_time - start_time
    average_time = elapsed_time / 1000
    max_balance = tree.get_max_absolute_balance()

    search_times.append(average_time)
    max_balances.append(max_balance)

plt.scatter(max_balances, search_times, alpha=0.5)
plt.xlabel("Max Absolute Balance")
plt.ylabel("Average Search Time (seconds)")
plt.title("Balance vs. Search Performance in BST")
plt.grid(True)
plt.show()

