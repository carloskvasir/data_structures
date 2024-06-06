# código que gera todas as possíveis árvores binárias de uma expressão matemática e garante que a travessia pré-ordem (pre-order traversal) retorne a expressão original. Utilizaremos as estruturas de dados da biblioteca padrão do Python
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
    for tree in trees:
        print(pre_order(tree))

if __name__ == '__main__':
    expr = "a+b*c-d/e"
    trees = generate_all_trees(expr)

    print("Pre-order traversals of all possible expression trees:")
    print_all_trees(trees)

