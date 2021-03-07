from collections import deque

#DFS
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1

        depth = 0
        for i in range(len(root.children)):
            cur_level = self.maxDepth(root.children[i])
            if cur_level > depth:
                depth = cur_level
        return depth + 1


#BFS
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children
#
#
# class Solution:
#     def maxDepth(self, root: 'Node') -> int:
#         if not root:
#             return 0
#         res = []
#         queue = deque([root])
#
#         while len(queue) > 0:
#             size = len(queue)
#             cur_level = []
#             for i in range(size):
#                 node = queue.popleft()
#                 if node.children:
#                     for i in range(len(node.children)):
#                         queue.append(node.children[i])
#                 cur_level.append(node.val)
#             res.append(cur_level)
#         return len(res)