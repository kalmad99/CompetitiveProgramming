import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    bcharged = b
    outf = []
    bactual = 0
    count = 0
    for i in range (len(bill)):
        if i!=k:
            outf.append(bill[i])
        else:
            continue
    for j in outf:
        bactual += j
    bactual = bactual//2
    if b-bactual == 0:
        print("Bon Appetit")
    else:
        print(b-bactual)
    
if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

