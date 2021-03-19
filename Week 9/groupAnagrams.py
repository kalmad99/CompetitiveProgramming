class Solution:
    def groupAnagrams(self, strs):
        result = {}
        res = []
        for string in strs:
            alpha = [0 for _ in range(26)]
            for i in range(len(string)):
                alpha[ord(string[i]) - 97] += 1

            alpha = tuple(alpha)
            if alpha not in result:
                result[alpha] = [string]
            else:
                result[alpha].append(string)

        for val in result.values():
            res.append(val)
        return res