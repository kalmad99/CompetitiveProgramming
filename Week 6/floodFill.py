class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        toBeRemovedColor = image[sr][sc]
        visited = set()
        n, m = len(image), len(image[0])
        image[sr][sc] = newColor
        self.dfs(sr, sc, image, visited, toBeRemovedColor, newColor, n, m)

        return image

    def dfs(self, i, j, image, visited, originalColor, newColor, n, m):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for direction in directions:
            # next_i and #next_j represent the next node we can jump on to
            next_i = i + direction[0]
            next_j = j + direction[1]

            if 0 <= next_i < n and 0 <= next_j < m and image[next_i][next_j] == originalColor:
                next_state = (next_i, next_j)
                # check if the new node found has been seen before to avoid cycles
                if next_state not in visited:
                    image[next_i][next_j] = newColor
                    visited.add(next_state)
                    self.dfs(next_i, next_j, image, visited, originalColor, newColor, n, m)

