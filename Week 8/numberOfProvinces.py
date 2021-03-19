class Solution:
    def findCircleNum(self, isConnected) -> int:
        counter = 0
        total = 0
        visited = set()
        # visited.add(1)
        for i in range(len(isConnected)):
            total += self.dfs(i + 1, isConnected, visited, counter)
        return total

    def dfs(self, startIndex, grid, visited, counter):
        for nextIndex, value in enumerate(grid[startIndex - 1]):
            # print(nextIndex, value)
            if value == 1 and nextIndex + 1 not in visited:
                visited.add(nextIndex + 1)
                counter += 1
                self.dfs(nextIndex + 1, grid, visited, counter)
        return counter
