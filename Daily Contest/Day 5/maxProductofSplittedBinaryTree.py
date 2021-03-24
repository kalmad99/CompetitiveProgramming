from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sortedwithIndex, result = [], []
        for i in range(len(mat)):
            sortedwithIndex.append((mat[i], i))
        sortedwithIndex = sorted(sortedwithIndex)

        for i in range(k):
            result.append(sortedwithIndex[i][1])
        return result