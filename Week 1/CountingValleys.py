#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

# UDDDUDUU
def countingValleys(steps, path):
    current = 0
    count = 0
    for i in range(steps):
        if path[i] == 'U':
            current += 1
        else:
            current -= 1

        if current == 0 and path[i] == 'U':
            count += 1

    return count
    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()