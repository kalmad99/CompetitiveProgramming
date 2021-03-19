class Solution:
    def productExceptSelf(self, nums):
        total = []
        prev = self.helper(nums)
        succ = (self.helper((nums)[::-1]))

        for i in range(len(prev)):
            total.append(prev[i] * succ[len(succ)-1-i])
        return total

    def helper(self, nums):
        result = [1]
        for i in range(len(nums) - 1):
            num = nums[i]
            result.append(result[-1] * num)