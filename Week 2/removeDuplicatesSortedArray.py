def removeDuplicates(nums) -> int:
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums[i] = 'a'
        else:
            continue

    try:
        while True:
            nums.remove('a')
    except ValueError:
        pass

    return len(nums)
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))