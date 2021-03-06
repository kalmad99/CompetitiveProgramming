def radixSort(arr):
    arr = maxDigit(arr)
    buckets = [[] for _ in range(10)]
    for i in range(len(arr[0])-1, -1, -1):
        for j in arr:
            buckets[int(j[i])].append(j)
        arr = sorting(buckets)
        buckets = [[] for _ in range(10)]

    return result(arr)


def sorting(bucket):
    arr = []
    for i in range(len(bucket)):
        for j in range(len(bucket[i])):
            arr.append(bucket[i][j])
    return arr


def maxDigit(arr):
    maxi = 0
    for i in arr:
        if len(str(i)) > maxi:
            maxi = len(str(i))

    for i in range(len(arr)):
        arr[i] = (maxi - len(str(arr[i]))) * '0' + str(arr[i])
    return arr


def result(arr):
    res = []
    for i in arr:
        res.append(int(i))
    return res


print(radixSort([100, 5, 25, 15, 50, 60]))