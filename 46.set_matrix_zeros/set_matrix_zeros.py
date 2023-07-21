from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        zero_cols = []
        zero_rows = []
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zero_rows.append(row)
                    zero_cols.append(col)

        for k in range(rows):
            for l in range(cols):
                if k in zero_rows or l in zero_cols:
                    matrix[k][l] = 0
        return matrix
