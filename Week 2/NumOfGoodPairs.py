def numIdenticalPairs(self, nums: List[int]) -> int:
    counter = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if (i < j) and (nums[i] == nums[j]):
                counter += 1
    return counter