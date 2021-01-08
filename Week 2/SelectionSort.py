def select(nums):
    for i in range(len(nums)-1):
        curmin = i
        for j in range(i+1, len(nums)):
            if nums[j]<nums[curmin]:
                curmin = j
        temp = nums[i]
        nums[i] = nums[curmin]
        nums[curmin] = temp
    return nums

print(select([2, 4, 1, 3, 5]))
print(select([1,2,3,4,5]))
print(select([2, 7, 4, 1, 5, 3]))