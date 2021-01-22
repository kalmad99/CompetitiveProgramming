# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.symmetry_checker(root.left, root.right)

    def symmetry_checker(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif (not p and q) or (p and not q):
            return False
        else:
            if p.val == q.val:
                return self.symmetry_checker(p.left, q.right) and self.symmetry_checker(p.right, q.left)
            else:
                return False

