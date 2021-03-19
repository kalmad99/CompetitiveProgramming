class Solution:
    def pivotIndex(self, nums) -> int:
        left = 0
        total = 0
        for i in nums:
            total += i

        for i in range(len(nums)):
            if left != total - nums[i]:
                left += nums[i]
                total -= nums[i]
            else:
                return i
        return -1