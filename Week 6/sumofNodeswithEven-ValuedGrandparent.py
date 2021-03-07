class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = [0]
        if root.left:
            self.dfs(root.left, root, total)
        if root.right:
            self.dfs(root.right, root, total)

        return total[0]

    def dfs(self, node, parentNode, total):
        if not node:
            return 0

        print(node.val)
        if (node.left):
            if (parentNode.val % 2 == 0):
                total[0] += node.left.val
            self.dfs(node.left, node, total)

        if (node.right):
            if (parentNode.val % 2 == 0):
                total[0] += (node.right.val)
            self.dfs(node.right, node, total)

            
    # def sumEvenGrandparent(self, root: TreeNode) -> int:
    #     return self.dfs(root, 1, 1)
    #
    # def dfs(self, node, parent, grandparent):
    #     if not node:
    #         return 0
    #     ourContribution = node.val if grandparent % 2 == 0 else 0
    #     return ourContribution + self.dfs(node.left, node.val, parent) + self.dfs(node.right, node.val, parent)
