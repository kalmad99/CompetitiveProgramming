# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        output = []
        total = 0
        output = self.postorder(root, output)
        for i in output:
            if i <= high and i >= low:
                total += i
            else:
                continue

        return total

    def postorder(self, node, output):
        total = 0
        if node is None:
            return output
        else:
            output = self.postorder(node.left, output)
            output = self.postorder(node.right, output)
            output.append(node.val)

        return output