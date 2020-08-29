class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self._root = None

    def insert(self, data):
        # if the tree is empty
        if self._root is None:
            self._root = Node(data)
            return

        # if the tree is not empty
        self._insert(data, self._root)

    def _insert(self, data, root):
        if data < root.data:
            # insert the node only if the left child is Empty
            if root.left is None:
                root.left = Node(data)
            else:
                self._insert(data, root.left)
        elif data > root.data:
            # insert the node only if the right child is Empty
            if root.right is None:
                root.right = Node(data)
            else:
                self._insert(data, root.right)
        else:
            print("Value already exists")

    def preorder_traversal(self):
        self._preorder_traversal(self._root)

    def _preorder_traversal(self, root):
        if root is None:
            return
        print(root.data)
        self._preorder_traversal(root.left)
        self._preorder_traversal(root.right)


if __name__ == "__main__":
    bst = BST()
    bst.insert(6)
    bst.insert(4)
    bst.insert(8)
    bst.insert(2)
    bst.insert(5)
    bst.insert(9)
    bst.preorder_traversal() # 6 4 2 5 8 9

    """
                6
            4        8
         2    5  None   9
    """
