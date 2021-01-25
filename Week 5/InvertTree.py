# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            return self.handler(root)

    def handler(self, node):
        # if node.left or node.right:
        if node:
            # print(node.val)
            temp = node.left
            node.left = node.right
            node.right = temp
            self.handler(node.left)
            self.handler(node.right)
        return node

