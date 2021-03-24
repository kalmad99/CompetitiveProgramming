# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        total, result, counter = {0: 1}, 0, [0]
        if not root:
            return 0
        else:
            self.dfs(root, total, result, counter, sum)
            return counter[0]

    def dfs(self, node, total, result, counter, k):
        if not node.left and not node.right:
            if result + node.val - k in total:
                counter[0] += total[result + node.val - k]
            return
        else:
            result += node.val
            if result - k in total:
                counter[0] += total[result - k]

            if result in total:
                total[result] += 1
            else:
                total[result] = 1

        if node.left:
            self.dfs(node.left, total, result, counter, k)

        if node.right:
            self.dfs(node.right, total, result, counter, k)

        if total[result] == 1:
            total.pop(result)
        else:
            total[result] -= 1
        result -= node.val