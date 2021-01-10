def largestPerimeter(A):
    finall = 0
    A = sorted(A)
    for i in range(len(A) - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            finall = (A[i] + A[i + 1] + A[i + 2])
    if finall == 0:
        return 0
    else:
        return finall


# print(largestPerimeter([2,1,2]))
# print(largestPerimeter([1,2,1]))
# print(largestPerimeter([3,2,3,4]))
# print(largestPerimeter([3,6,2,3]))


