def sortArray(nums):
    mid = len(nums) // 2
    if len(nums) <= 1:
        return nums
    left = sortArray(nums[:mid])
    right = sortArray(nums[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    lidx, ridx = 0, 0
    while lidx < len(left) and ridx < len(right):
        if left[lidx] <= right[ridx]:
            merged.append(left[lidx])
            lidx += 1
        else:
            merged.append(right[ridx])
            ridx += 1
    if lidx == len(left):
        merged.extend(right[ridx:])
    if ridx == len(right):
        merged.extend(left[lidx:])

    return merged

# print(sortArray([5,2,3,1]))
# print(sortArray([5,1,1,2,0,0]))