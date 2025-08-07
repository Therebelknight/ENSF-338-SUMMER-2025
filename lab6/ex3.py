import sys

# Define a node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Check if a token is an operator
def is_operator(token):
    return token in {"+", "-", "*", "/"}

# Parse the expression to build the tree
def parse_expression(tokens):
    stack = []

    for token in tokens:
        if token == ")":
            right = stack.pop()
            operator = stack.pop()
            left = stack.pop()
            stack.pop()  
            node = Node(operator)
            node.left = left
            node.right = right
            stack.append(node)
        elif token in {"+", "-", "*", "/", "("} or token.isdigit():
            if token.isdigit():
                stack.append(Node(int(token)))
            else:
                stack.append(token)
    return stack[0]

# Computing the expression using post order traversal
def evaluate(node):
    if node is None:
        return 0
    if not node.left and not node.right:
        return node.value
    left_val = evaluate(node.left)
    right_val = evaluate(node.right)
    if node.value == "+":
        return left_val + right_val
    elif node.value == "-":
        return left_val - right_val
    elif node.value == "*":
        return left_val * right_val
    elif node.value == "/":
        return left_val / right_val

if __name__ == "__main__":
    expression = sys.argv[1]
    tokens = expression.strip().split()
    root = parse_expression(tokens)
    result = evaluate(root)
    print(int(result) if result == int(result) else result)