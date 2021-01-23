class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))