def sortColors(nums):
    for i in range(len(nums) - 1):
        flag = 0
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
                flag = 1
        if flag == 0:
            break
    print(nums)


# sortColors([2,0,2,1,1,0])
# sortColors([2,0,1])
# sortColors([0])
# sortColors([1])
