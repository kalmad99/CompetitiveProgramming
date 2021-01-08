def insert(nums):
    for i in range(len(nums)):
        value = nums[i]
        cutoff = i
        while cutoff > 0 and nums[cutoff-1] > value:
            nums[cutoff] = nums[cutoff-1]
            cutoff -= 1
        nums[cutoff] = value
    return nums

print(insert([2, 4, 1, 3, 5]))
print(insert([1,2,3,4,5]))
print(insert([2, 7, 4, 1, 5, 3]))