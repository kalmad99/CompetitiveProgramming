from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode):
        res = []
        queue = deque([root])

        while (len(queue) != 0):
            size = len(queue)
            cur_level = []
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            total = 0
            for i in cur_level:
                total += i
            res.append(total / len(cur_level))
            total = 0
        return res
