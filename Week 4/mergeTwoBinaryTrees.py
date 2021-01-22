# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        newTree = TreeNode()
        if t1 is None:
            newTree = t2
            return newTree
        elif t2 is None:
            newTree = t1
            return newTree
        newTree.left = self.mergeTrees(t1.left, t2.left)
        newTree.val = t1.val + t2.val
        newTree.right = self.mergeTrees(t1.right, t2.right)
        return newTree