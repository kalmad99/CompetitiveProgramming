def diagonalDifference(arr):
    ltr = 0
    rtl = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                ltr += (arr[i][j])
            if i + j == len(arr)-1:
                rtl += (arr[i][j])
    return abs(rtl-ltr)