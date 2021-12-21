class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value


def preorder(root):
    print(root.val, end=' ')
    if root.left:
        root.left.preorder()
    if root.right:
        root.right.preorder()


def inorder(root):
    if root.left:
        root.left.inorder()
    print(root.val, end=' ')
    if root.right:
        root.right.inorder()


def postorder(root):
    if root.left:
        root.left.postorder()
    if root.right:
        root.right.postorder()
    print(root.val, end=' ')


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("Pre-order Traversal: ", root.preorder())
print("In-order Traversal: ", root.inorder())
print("Post-order Traversal: ", root.postorder())
