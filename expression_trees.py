from collections import deque

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

def in_order(node):
    if node is None:
        return ''
    return in_order(node.left) + node.data + in_order(node.right)

def post_order(node):
    if node is None:
        return ''
    return post_order(node.left) + post_order(node.right) + node.data

def level_order(node):
    if node is None:
        return ''
    queue = deque([node])
    result = ''
    while queue:
        current = queue.popleft()
        result += current.data
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result

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

def edges_from_tree(node):
    edges = []
    def traverse(n):
        if n is not None:
            if n.left:
                edges.append(f"{n.data} {n.left.data}")
                traverse(n.left)
            if n.right:
                edges.append(f"{n.data} {n.right.data}")
                traverse(n.right)
    traverse(node)
    return edges

def print_tree_style(node, prefix="", is_left=True):
    if node is not None:
        if prefix == "":
            print(".")
        connector = "├l── " if is_left else "└r── "
        print(prefix + connector + node.data)
        if node.left or node.right:
            if node.left:
                print_tree_style(node.left, prefix + ("│   " if node.right else "    "), True)
            if node.right:
                print_tree_style(node.right, prefix + "    ", False)

def print_graph_edges(edges):
    print("Enter Nodes:")
    for edge in edges:
        print(edge)

def display_menu():
    print("Select the traversal type:")
    print("1. In-Order")
    print("2. Pre-Order")
    print("3. Post-Order")
    print("4. Level-Order")
    traversal_choice = input("Enter choice (1, 2, 3, or 4): ")

    print("\nSelect the display format:")
    print("1. Tree visualization (similar to 'tree' command)")
    print("2. Graph edges format")
    display_choice = input("Enter choice (1 or 2): ")

    return traversal_choice, display_choice

def print_all_trees(trees, traversal_choice, display_choice):
    traversal_func = {
        '1': in_order,
        '2': pre_order,
        '3': post_order,
        '4': level_order
    }[traversal_choice]

    for idx, tree in enumerate(trees):
        print(f"Tree {idx + 1}:")
        print(traversal_func(tree))  # This prints the expression in the selected traversal order
        edges = edges_from_tree(tree)
        if display_choice == '1':
            print_tree_style(tree)
        elif display_choice == '2':
            print_graph_edges(edges)
        print()

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

    traversal_choice, display_choice = display_menu()

    print("Traversals of all possible expression trees and their representations:")
    print_all_trees(trees, traversal_choice, display_choice)
