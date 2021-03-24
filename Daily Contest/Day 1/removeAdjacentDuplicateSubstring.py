class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append((s[i], 1))
            else:
                if stack[-1][0] == s[i] and stack[-1][1] < k:
                    ele = stack[-1][0]
                    freq = stack[-1][1]
                    stack.pop()
                    stack.append((ele, freq+1))
                else:
                    stack.append((s[i], 1))
                if stack[-1][1] == k:
                    stack.pop()

        res = ""
        for i, j in stack:
            res += (i*j)
        return res