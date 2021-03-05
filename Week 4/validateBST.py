class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        output = []
        res = self.helper(root, output)
        for i in range(len(res) - 1):
            if res[i] < res[i + 1]:
                continue
            else:
                return False
        return True

    def helper(self, node, output):
        if not node:
            return output
        else:
            self.helper(node.left, output)
            output.append(node.val)
            self.helper(node.right, output)
        return output
