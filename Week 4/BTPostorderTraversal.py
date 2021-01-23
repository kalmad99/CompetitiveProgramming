# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def postorderTraversal(self, root: TreeNode):
        res = []
        return self.postOrder(root, res)

    def postOrder(self, node, output):
        if node is None:
            return output
        else:
            output = self.postOrder(node.left, output)
            output = self.postOrder(node.right, output)
            output.append(node.val)
        return output

# sn = Solution()
# tr = TreeNode(3)
# tr.left = TreeNode(5)
# tr.right = TreeNode(2)
# tr.left.left = TreeNode(1)
# tr.left.right = TreeNode(4)
# tr.right.left = TreeNode(6)
# output = []
# # print(sn.postOrder(tr, output))
# print(sn.inorder(tr, output))