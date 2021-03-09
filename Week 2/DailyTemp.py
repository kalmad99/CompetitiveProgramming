class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0 for _ in range(len(T))]
        stack = []
        for i in range(len(T) - 1, -1, -1):
            while len(stack) > 0 and T[i] >= stack[-1][0]:
                stack.pop()
            if len(stack) > 0 and T[i] < stack[-1][0]:
                res[i] = stack[-1][1] - i
            stack.append((T[i], i))
        return res
