from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        in_island = []
        R = len(grid)
        C = len(grid[0])

        def grow_island(grid, pos):
            in_island.append(pos)
            to_check = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for inc_x, inc_y in to_check:
                x, y = pos[0] + inc_x, pos[1] + inc_y
                if 0<=x<=R-1 and 0<=y<=C-1 and grid[x][y]=='1':
                    grow_island(grid, [x, y])
            islands += 1

        for i in range(R):
            for j in range(C):
                if grid[i][j] == str(1) and [i,j] not in in_island:
                    grow_island(grid, [i,j])

        return islands

# Improved solution
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        R = len(grid)
        C = len(grid[0])

        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    islands += 1
        return islands

    def dfs(self,grid,i,j):
        grid[i][j] = 0
        for dr, dc in (1,0), (-1,0), (0,-1), (0,1):
            r = i + dr
            c = j + dc
            if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c]=='1':
                self.dfs(grid,r,c)
