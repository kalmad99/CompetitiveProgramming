from typing import List


class Solution:
    # Top Down
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        return self.dfs(triangle, 0, 0, memo)

    def dfs(self, triangle, depth, cur, memo):
        if (cur, depth) in memo:
            return memo[(cur, depth)]

        total = triangle[depth][cur]
        if depth == len(triangle) - 1:
            return total

        left = self.dfs(triangle, depth + 1, cur, memo)
        right = self.dfs(triangle, depth + 1, cur + 1, memo)
        total += min(left, right)
        memo[(cur, depth)] = total
        return total

    # #Bottom up
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     result, temp = triangle[-1], []
    #     i = 1
    #     for j in range(len(triangle)-i-1, -1,-1):
    #         for k in range(len(triangle[j])):
    #             temp.append(triangle[j][k] + min(result[k], result[k+1]))
    #         result = temp
    #         temp = []
    #         i+=1
    #     return result[0]



