from .node import Node


class BST:
    def __init__(self):
        self.root = None

    def size(self):
        """
        Get the number of elements via recursive _size
        Complexity: O(log N)
        """
        return self._size(self.root)

    def _size(self, n):
        if n is None:
            return 0
        return 1 + self._size(n.left) + self._size(n.right)

    def search(self, data):
        """Search bst via recursive _search
        Complexity O(log N)
        """
        return self._search(self.root, data)

    def _search(self, root: Node, data):
        if root is None:
            return False
        if root.data == data:
            return True

        # if cond go right, else go left
        if data > root.data:
            return self._search(root.right, data)
        return self._search(root.left, data)

    def insert(self, data):
        if self.root:
            return self._insert(self.root, data)

        self.root = Node(data)
        return True

    def _insert(self, root, data):
        if root.data == data:  # data exists
            return False

        if data < root.data:  # go left
            if root.left:
                return self._insert(root.left, data)
            root.left = Node(data)
            return True

        if root.right:
            return self._insert(root.right, data)
        root.right = Node(data)
        return True

    def preorder(self, root):
        if root:
            print(f'{root.data} ')
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f'{root.data} ')
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(f'{root.data} ')
