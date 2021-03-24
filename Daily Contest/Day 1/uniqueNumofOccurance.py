class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictionary = {}
        res = []
        for i in arr:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1

        for i in dictionary.values():
            # print(i)
            if i not in res:
                res.append(i)
                continue
            else:
                return False
        return True