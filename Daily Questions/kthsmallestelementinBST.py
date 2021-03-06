class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        output = []
        res = self.inorder(root, output)
        return res[k - 1]

    def inorder(self, node, output):
        if not node:
            return output
        else:
            self.inorder(node.left, output)
            output.append(node.val)
            self.inorder(node.right, output)
        return output