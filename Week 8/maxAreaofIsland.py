class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        result = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    result = max(result, self.dfs(i, j, grid, visited))
        return result

    def dfs(self, sr, sc, grid, visited):
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        res = 1
        for direction in directions:
            nextcoor = nextr, nextc = sr + direction[0], sc + direction[1]

            if (0 <= nextr < len(grid) and
                    0 <= nextc < len(grid[0]) and
                    nextcoor not in visited and
                    grid[nextr][nextc] == 1):
                visited.add(nextcoor)
                res += self.dfs(nextr, nextc, grid, visited)
        return res
