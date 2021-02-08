class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.helper(root, targetSum)

    def helper(self, node, target):
        if not node:
            return False
        if not node.left and not node.right and target - node.val == 0:
            return True
        return self.helper(node.left, target - node.val) or self.helper(node.right, target - node.val)

