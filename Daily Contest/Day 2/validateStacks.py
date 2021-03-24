class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stack = []
        pushindex, popindex = 0, 0
        while popindex < len(popped):
            if len(stack) == 0 and pushindex < len(pushed):
                stack.append(pushed[pushindex])
                pushindex += 1

            if stack[-1] == popped[popindex]:
                stack.pop()
                popindex += 1
            elif pushindex < len(pushed):
                stack.append(pushed[pushindex])
                pushindex += 1
            else:
                return False

        if len(stack) == 0:
            return True


res = Solution()
print(res.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))