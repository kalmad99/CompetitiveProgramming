from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root:
            return self.bfs(root)
        return 0

    def isLeaf(self, node):
        return not (node.left or node.right)

    def bfs(self, node):
        res = deque()
        res.append(node)
        level = 1
        while len(res) != 0:
            size = len(res)
            for i in range(size):

                if self.isLeaf(res[0]):
                    return level

                if (res[0].left):
                    res.append(res[0].left)

                if (res[0].right):
                    res.append(res[0].right)

                res.popleft()

            level += 1

        return level