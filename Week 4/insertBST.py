# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            root = TreeNode(val)
        else:
            self.insert(val, root)

        return root

    def insert(self, val, cur_node):
        if val < cur_node.val:
            if cur_node.left is None:
                cur_node.left = TreeNode(val)
            else:
                return self.insert(val, cur_node.left)
        else:
            if cur_node.right is None:
                cur_node.right = TreeNode(val)
            else:
                return self.insert(val, cur_node.right)



