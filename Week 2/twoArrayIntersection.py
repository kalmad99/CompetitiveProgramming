def intersection(nums1, nums2):
    intersection = []
    finall = []
    bigger = []
    cur = []
    count = 0
    if len(nums1) < len(nums2):
        cur = nums2
        bigger = nums1
        maxlen = len(nums2)
    else:
        cur = nums1
        bigger = nums2
        maxlen = len(nums1)

    for i in cur:
        if i in bigger:
            intersection.append(i)

    for i in intersection:
        if i in finall:
            continue
        else:
            finall.append(i)

    return finall

# print(intersection([1,2,2,1], [2,2]))
# print(intersection([4,9,5], [9,4,9,8,4]))