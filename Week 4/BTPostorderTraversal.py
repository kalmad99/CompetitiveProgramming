# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        return self.postOrder(root, res)

    def postOrder(self, node, output):
        if node is None:
            return output
        else:
            output = self.postOrder(node.left, output)
            output = self.postOrder(node.right, output)
            output.append(node.val)
        return output