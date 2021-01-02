# Complete the sockMerchant function below.
# 9
# 10 20 20 10 10 30 50 10 20
import os

def sockMerchant(n, ar):
    emptyl = []
    result = 0
    count = 0
    for i in ar:
        if i in emptyl:
            continue
        else:
            emptyl.append(i)
    for j in emptyl:
        count = ar.count(j)
        if count%2==0:
            result += count/2
        else:
            result += count//2
    return int(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
