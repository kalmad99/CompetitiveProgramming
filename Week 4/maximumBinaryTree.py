class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums) -> TreeNode:
        return self.helper(nums)

    def helper(self, nums):
        if len(nums) == 0:
            return None

        maxNode = max(nums)
        root = TreeNode(maxNode)

        index = nums.index(maxNode)
        left = nums[:index]
        right = nums[index + 1:]

        root.left = self.helper(left)
        root.right = self.helper(right)

        return root