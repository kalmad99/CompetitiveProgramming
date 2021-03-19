from collections import deque


class Solution:
    def orangesRotting(self, grid) -> int:
        row, column = len(grid), len(grid[0])
        queue = deque()
        freshcount = 0

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    freshcount += 1

        if freshcount == 0:
            return 0

        return self.bfs(grid, queue, row, column)

    def bfs(self, grid, queue, row, column):
        visited = set([])
        minute = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while len(queue) > 0:
            minute += 1

            size = len(queue)
            for _ in range(size):  # level by level
                cur = queue.popleft()
                for direction in directions:
                    newr = direction[0] + cur[0]
                    newc = direction[1] + cur[1]
                    if 0 <= newr < row and 0 <= newc < column and grid[newr][newc] == 1:
                        newcoor = (newr, newc)
                        if newcoor not in visited:
                            grid[newr][newc] = 2
                            queue.append(newcoor)
                            visited.add(newcoor)
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    return -1

        return minute - 1