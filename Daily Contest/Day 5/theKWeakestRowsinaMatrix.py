# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        total, best = self.total(root), [0]
        self.total(root, total, best)
        return best[0] % (10 ** 9 + 7)

    def total(self, node, total=0, best=[0]):
        if not node:
            return 0
        result = self.total(node.left, total, best) + node.val + self.total(node.right, total, best)
        remaining = total - result
        best[0] = max(best[0], remaining * result)
        print(remaining, total, best[0])
        return result