from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []
        res = []
        queue = deque([root])
        level = 0

        while (len(queue) != 0):
            size = len(queue)
            cur_level = []
            level += 1
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                cur_level.append(node.val)
            if level % 2 == 0:
                res.append(cur_level[::-1])
            else:
                res.append(cur_level)
        return res
