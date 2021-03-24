from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        return self.dfs(0, 0, grid, memo)

    def dfs(self, sr, sc, grid, memo):
        if (sr, sc) in memo:
            return memo[(sr, sc)]

        if sr >= len(grid):
            return 1000
        if sc >= len(grid[0]):
            return 1000

        total = grid[sr][sc]
        if sr == len(grid) - 1 and sc == len(grid[0]) - 1:
            return total

        right = self.dfs(sr, sc + 1, grid, memo)
        down = self.dfs(sr + 1, sc, grid, memo)
        total += min(right, down)
        memo[(sr, sc)] = total
        return total