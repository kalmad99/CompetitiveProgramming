class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        res = ""
        for i in S:
            if len(stack) == 0:
                stack.append(i)
            else:
                if stack[-1] == i:
                    stack.pop()
                else:
                    stack.append(i)
        for i in stack:
            res += i
        return res

# rd = Solution()
# print(rd.removeDuplicates("abbaca"))