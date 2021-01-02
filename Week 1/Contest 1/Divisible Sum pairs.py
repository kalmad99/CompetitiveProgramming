import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    res = []
    fin = []
    count = 0
    for i in range(len(ar)-1):
        for j in range(i, len(ar)):
            if i<j and (ar[i]+ar[j])%k==0:
                res.append(i)
                res.append(j)
                fin.append(res)
                res = []
            else:
                continue
    return len(fin) 
    # print(fin)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
