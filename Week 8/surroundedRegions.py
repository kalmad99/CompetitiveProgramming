from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited, beFlipped, counter = set(), [], 0
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == 'O' and (i, j) not in visited:
                    visited.add((i, j))
                    beFlipped.append((i, j))
                    if self.dfs(i, j, board, visited, beFlipped):
                        while len(beFlipped) > 0:
                            cur = beFlipped.pop()
                            board[cur[0]][cur[1]] = 'X'
                    else:
                        while len(beFlipped) > 0:
                            cur = beFlipped.pop()
        return

    def dfs(self, sr, sc, grid, visited, beFlipped):
        directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]
        result = True
        if (sr >= len(grid) - 1 or sr <= 0) or (sc >= len(grid[0]) - 1 or sc <= 0):
            result = False

        for direction in directions:
            newcoor = newr, newc = direction[0] + sr, direction[1] + sc
            if (0 <= newr < len(grid) and
                    0 <= newc < len(grid[0]) and
                    newcoor not in visited and
                    grid[newr][newc] == 'O'):
                visited.add(newcoor)
                beFlipped.append(newcoor)
                result = self.dfs(newr, newc, grid, visited, beFlipped) and result
        return result