import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    counta = 0
    leftoverCount = 0
    repeated = n // len(s)
    leftoverString = s[:(n % len(s))]
    for i in leftoverString:
        if i == 'a':
            leftoverCount += 1
    for j in s:
        if j == 'a':
            counta += 1
    return (counta * repeated) + leftoverCount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
