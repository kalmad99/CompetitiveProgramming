class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    counter += len(grid[i])-j
                    break
                else:
                    continue
        return counter

            
