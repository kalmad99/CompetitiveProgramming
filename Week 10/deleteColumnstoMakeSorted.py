from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = [True for _ in range(len(strs[0]))]
        counter = 0
        for i in range(len(strs) - 1):
            for j in range(len(strs[i])):
                if strs[i][j] <= strs[i + 1][j]:
                    continue
                else:
                    result[j] = False
                    continue

        for i in range(len(result)):
            if result[i] == False:
                counter += 1
        return counter
