class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1
        L = 0
        R = rows
        M = (L + R) // 2
        while L <= R:
            M = (L + R) // 2
            if target < matrix[M][cols] and not (target >= matrix[M][0]):
                R = M - 1
            elif target > matrix[M][cols]:
                L = M + 1
            else:
                break
        L = 0
        R = cols
        M2 = (L + R) // 2
        while L <= R:
            M2 = (L + R) // 2
            if target < matrix[M][M2]:
                R = M2 - 1
            elif target > matrix[M][M2]:
                L = M2 + 1
            else:
                return True
        return False
