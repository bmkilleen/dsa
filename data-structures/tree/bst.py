class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


class BST:
    def __init__(self,):
        self.root = None

    """Alt. keep track with a size var as we add/delete"""

    def size(self):
        return self._size(self.root)

    def _size(self, root):
        if root is None:
            return 0
        return 1 + self._size(root.left) + self._size(root.right)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, root, value):
        if root is None:
            return False
        if root.data == value:
            return True
        elif value > root.data:
            return self.recur_search(root.right, value)
        else:
            return self.recur_search(root.left, value)

    def insert(self, value):
        if self.root:
            return self._insert(self.root, value)
        self.root = Node(value)
        return True

    def _insert(self, root, value):
        if root.value == value:
            return False

        if value < root.data:
            if root.left:
                return self._insert(root.left, value)
            root.left = Node(value)
            return True
        else:
            if root.right:
                return self._insert(root.right, value)
            root.right = Node(value)
            return True
