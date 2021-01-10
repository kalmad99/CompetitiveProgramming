def findMedian(arr):
    negarr = []
    posarr = []
    finarr = []
    for i in arr:
        if i < 0:
            negarr.append(i)
        else:
            posarr.append(i)

    for i in range(len(negarr)):
        negarr[i] = -1 * negarr[i]

    negarr = sorting(negarr)
    for i in range(len(negarr) - 1, -1, -1):
        negarr[i] = -1 * negarr[i]
    posarr = sorting(posarr)

    for i in negarr:
        finarr.append(i)
    for i in posarr:
        finarr.append(i)

    return finarr[len(arr) // 2]


def sorting(arr):
    output = [0 for i in range(len(arr))]
    counter = [0 for i in range(20001)]

    for i in arr:
        counter[i] += 1

    for i in range(-10000, 10000):
        counter[i] += counter[i - 1]

    for i in range(len(arr)):
        output[counter[arr[i]] - 1] = arr[i]
        counter[arr[i]] -= 1

    return output

nums = [0, 1, 2, 4, 6, 5, 3]
print(findMedian(nums))