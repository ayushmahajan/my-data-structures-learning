class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)


if __name__ == "__main__":
    binary_tree = BinaryTree(5)
    binary_tree.root.left = Node(7)
    binary_tree.root.right = Node(8)
    binary_tree.root.left.left = Node(1)
    binary_tree.root.left.right = Node(2)
    binary_tree.root.right.left = Node(4)
