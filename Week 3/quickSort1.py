def quickSort(arr):
    pivot = arr[0]
    smaller, equal, larger = [], [], []
    for i in arr:
        if i < pivot:
            smaller.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            larger.append(i)
    return smaller + equal + larger