from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dicti, result, mid = {}, [], len(arr) // 2
        for i in arr:
            if i in dicti:
                dicti[i] += 1
            else:
                dicti[i] = 1

        sorted_tuples = sorted(dicti.items(), key=lambda item: item[1], reverse=True)
        for i, j in sorted_tuples:
            if j >= mid:
                result.append(i)
                break
            else:
                result.append(i)
                mid -= j
        return len(result)