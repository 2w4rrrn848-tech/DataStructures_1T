class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Node | None) -> bool:
    def validate(node, low=float("-inf"), high=float("inf")) -> bool:
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)

    return validate(root)


def is_valid_bst_iterative(root: Node | None) -> bool:
    if not root:
        return True

    stack = [(root, float("-inf"), float("inf"))]

    while stack:
        node, low, high = stack.pop()
        if not (low < node.val < high):
            return False
        if node.right:
            stack.append((node.right, node.val, high))
        if node.left:
            stack.append((node.left, low, node.val))

    return True


valid_tree = Node(5, Node(1), Node(8, Node(6), Node(9)))
invalid_tree = Node(5, Node(1), Node(8, Node(4), Node(9)))

print("Recursive Check:")
print("valid_tree:", is_valid_bst(valid_tree))
print("invalid_tree:", is_valid_bst(invalid_tree))

print("\nIterative Check:")
print("valid_tree:", is_valid_bst_iterative(valid_tree))
print("invalid_tree:", is_valid_bst_iterative(invalid_tree))