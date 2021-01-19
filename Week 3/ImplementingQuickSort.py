from random import randint


def create_array(size, maxi):
    return [randint(-1 * maxi, maxi) for _ in range(size)]


#Version 1
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    smaller, equal, larger = [], [], []
    pivot = arr[randint(0, len(arr)-1)]

    for i in arr:
        if i < pivot:
            smaller.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            larger.append(i)

    return quick_sort(smaller) + equal + quick_sort(larger)


arra = create_array(10, 1000)
print(arra)
print(quick_sort(arra))

#Version 2
# def quick_sort(arr, start, end):
#     if start < end:
#         pivot = partition(arr, start, end)
#         quick_sort(arr, start, pivot-1)
#         quick_sort(arr, pivot+1, end)
#     return arr
#
#
# def partition(arr, start, end):
#     pivot = arr[end]
#     pindex = start
#     for i in range(start, end):
#         if arr[i] <= pivot:
#             arr[i], arr[pindex] = arr[pindex], arr[i]
#             pindex += 1
#     arr[pindex], arr[end] = arr[end], arr[pindex]
#     return pindex
#
# arra = create_array(10, 1000)
# print(arra)
# print(quick_sort(arra, 0, len(arra)-1))
