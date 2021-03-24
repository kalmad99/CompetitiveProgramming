from typing import List


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A = sorted(A)
        total, i, j, val = 0, 0, 0, K
        neg = []
        for i in range(len(A)):
            if A[i] < 0:
                neg.append(A[i])
        while j < len(neg) and j < val:
            A[j] *= -1
            K -= 1
            j += 1

        small = A.index(min(A))
        if K % 2 != 0:
            A[small] *= -1

        for i in A:
            total += i
        return total