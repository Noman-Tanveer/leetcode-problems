class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0]*n]*m
        cache[0] = [1]*n
        for row in cache:
            row[0]=1
        for i in range(1, m):
            for j in range(1, n):
                cache[i][j] = cache[i-1][j]+cache[i][j-1]
        return cache[-1][-1]
