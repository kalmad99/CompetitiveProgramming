# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            return self.handler(root, q, p)
        return self.handler(root, p, q)

    def handler(self, node, p, q):
        if p.val <= node.val <= q.val:
            return node
        elif p.val < node.val and q.val < node.val:
            return self.handler(node.left, p, q)
        elif p.val > node.val and q.val > node.val:
            return self.handler(node.right, p, q)
