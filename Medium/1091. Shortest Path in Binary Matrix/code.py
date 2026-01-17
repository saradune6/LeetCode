from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        q = deque([(0, 0, 1)])  
        grid[0][0] = 1          

        while q:
            r, c, d = q.popleft()
            if r == n - 1 and c == n - 1:
                return d

            for nr in range(max(0, r - 1), min(n, r + 2)):
                for nc in range(max(0, c - 1), min(n, c + 2)):
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr, nc, d + 1))

        return -1
