def twoSum(nums, target):
    result = []
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
                return result
            else:
                continue

print(twoSum([2,7,11,15], 9))