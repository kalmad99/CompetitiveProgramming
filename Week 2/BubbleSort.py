def bubble(nums):
    for j in range(len(nums)-1):
        flag = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp
                flag = 1
        if flag == 0:
            break
    return nums

print(bubble([2, 4, 1, 3, 5]))
print(bubble([1,2,3,4,5]))
print(bubble([2, 7, 4, 1, 5, 3]))