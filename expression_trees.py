class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_operator(c):
    return c in ['+', '-', '*', '/']

def pre_order(node):
    if node is None:
        return ''
    return node.data + pre_order(node.left) + pre_order(node.right)

def generate_trees(expr, start, end):
    if start > end:
        return [None]

    trees = []
    for i in range(start, end + 1):
        if is_operator(expr[i]):
            left_trees = generate_trees(expr, start, i - 1)
            right_trees = generate_trees(expr, i + 1, end)

            for l in left_trees:
                for r in right_trees:
                    node = Node(expr[i])
                    node.left = l
                    node.right = r
                    trees.append(node)
    
    if not trees:
        trees.append(Node(expr[start]))

    return trees

def generate_all_trees(expr):
    return generate_trees(expr, 0, len(expr) - 1)

def print_all_trees(trees):
    for idx, tree in enumerate(trees):
        print(f"Tree {idx + 1}:")
        print(pre_order(tree))  # This prints the expression in prefix notation
        print_ascii_tree(tree)
        print()

def print_ascii_tree(node, prefix="", is_left=True):
    if node is not None:
        print(prefix + ("|-- " if is_left else "+-- ") + node.data)
        if node.left or node.right:
            if node.left:
                print_ascii_tree(node.left, prefix + ("|   " if node.right else "    "), True)
            if node.right:
                print_ascii_tree(node.right, prefix + "    ", False)

def infix_to_postfix(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2}
    stack = []
    output = []
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop())
    return ''.join(output)

if __name__ == '__main__':
    expr = "(a+(b/c)-d)*e"
    postfix_expr = infix_to_postfix(expr)
    trees = generate_all_trees(postfix_expr)

    print("Pre-order traversals of all possible expression trees and their ASCII representations:")
    print_all_trees(trees)
