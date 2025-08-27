from functools import lru_cache
from typing import List

d = [1, 1, -1, -1, 1]

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def isOutside(i, j):
            return i < 0 or i >= n or j < 0 or j >= m

        @lru_cache(None)  
        def dfs(i, j, dir, turn, nxt):
            ans = 1
            x = grid[i][j]

            s, t = i + d[dir], j + d[dir + 1]
            if not isOutside(s, t):
                y = grid[s][t]
                if nxt == y:
                    ans = max(ans, 1 + dfs(s, t, dir, turn, nxt ^ 2))

            if not turn:
                newDir = (dir + 1) & 3  
                u, v = i + d[newDir], j + d[newDir + 1]
                if not isOutside(u, v):
                    z = grid[u][v]
                    if nxt == z:
                        ans = max(ans, 1 + dfs(u, v, newDir, 1, nxt ^ 2))

            return ans

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:  
                    for dir in range(4):
                        ans = max(ans, dfs(i, j, dir, 0, 2))

        return ans
