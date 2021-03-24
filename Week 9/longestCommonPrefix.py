from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlength = 201
        for i in strs:
            minlength = min(minlength, len(i))
        result = ""

        if minlength == 201:
            return ""

        for i in range(minlength):
            temp = set()
            for j in strs:
                temp.add(j[i])
            if len(temp) > 1:
                break
            else:
                result += j[i]
                temp.remove(j[i])
        return result


