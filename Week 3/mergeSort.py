def create_random_array(size, max):
    from random import randint
    return [randint(-1 * max, max) for _ in range(size)]


def merge(a, b):
    merged = []
    aidx, bidx = 0,0
    while aidx<len(a) and bidx<len(b):
        if a[aidx] <= b[bidx]:
            merged.append(a[aidx])
            aidx += 1
        else:
            merged.append(b[bidx])
            bidx += 1

    if aidx == len(a):
        merged.extend(b[bidx:])
    else:
        merged.extend(a[aidx:])

    return merged


def merge_sort(A):
    mid = len(A)//2
    if len(A) <= 1:
        return A
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
    return merge(left, right)


randlist = create_random_array(10, 50)
print(randlist)
print(merge_sort(randlist))