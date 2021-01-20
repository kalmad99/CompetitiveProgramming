def binarySearch(arr, target):
    mid = (len(arr)) // 2
    if len(arr) == 1:
        if arr[mid] == target:
            return mid
        return -1
    elif arr[mid] == target:
        return mid
    elif arr[mid] < target:
        res = binarySearch((arr[mid:]), target)
        if res != -1:
            return mid + res
        else:
            return -1
    else:
        return binarySearch((arr[:mid]), target)


# def search(arr, start, end, target):
#     # start = 0
#     # end = len(arr)-1
#     if start > end:
#         return -1
#     mid = (start + end)//2
#     print(mid)
#     if target == arr[mid]:
#         return mid
#     elif target < arr[mid]:
#         end = mid - 1
#         return search(arr, start, mid - 1, target)
#     else:
#         start = mid + 1
#         return search(arr,mid + 1, end, target)

# arr = [1, 4, 54, 123, 234]
# print(search(arr, 0, len(arr), 234))
# print(binarySearch([1, 4, 54, 123], 54))
print(binarySearch([-12,-1,0,3,5,9,12,24,34], 24))