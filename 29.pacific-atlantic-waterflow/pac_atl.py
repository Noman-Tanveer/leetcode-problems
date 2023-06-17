from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        R, C = len(heights), len(heights[0])

        atl_v = [[False] * C for _ in range(R)]
        pac_v = [[False] * C for _ in range(R)]
        atl_q, pac_q = deque(), deque()

        for col in range(C):
            pac_q.append((0, col))
            atl_q.append((R-1, col))
            pac_v[0][col] = True
            atl_v[R-1][col] = True

        for row in range(R):
            pac_q.append((row, 0))
            atl_q.append((row, C-1))
            pac_v[row][0] = True
            atl_v[row][C-1] = True

        def bfs(queue, visited):
            while queue:
                row, col = queue.popleft()
                # Check adjacent cells
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r, c = row + dr, col + dc
                    # Check if cell is within bounds and hasn't been visited yet
                    if 0 <= r < R and 0 <= c < C and not visited[r][c]:
                        # Check if cell can flow to the ocean
                        if heights[r][c] >= heights[row][col]:
                            visited[r][c] = True
                            queue.append((r, c))

        # Run BFS on both oceans starting from the boundary cells
        bfs(pac_q, pac_v)
        bfs(atl_q, atl_v)

        print(pac_v, atl_v)
        # Find the cells that can flow to both oceans
        result = []
        for row in range(R):
            for col in range(C):
                if pac_v[row][col] and atl_v[row][col]:
                    result.append([row, col])

        return result

# To be revisited
