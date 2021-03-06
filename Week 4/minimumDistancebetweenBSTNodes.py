from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        res = []
        queue = deque([root])

        while len(queue) != 0:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                res.append(node.val)

        mini = 100001
        res = sorted(res)
        for i in range(len(res) - 1):
            if res[i + 1] - res[i] < mini:
                mini = res[i + 1] - res[i]
        return mini
