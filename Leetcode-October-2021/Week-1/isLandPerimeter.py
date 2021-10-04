# https://leetcode.com/problems/island-perimeter/
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        P = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    P += 4
                    if i > 0 and grid[i - 1][j]:
                        P -= 2
                    if j > 0 and grid[i][j - 1]:
                        P -= 2
        return P
