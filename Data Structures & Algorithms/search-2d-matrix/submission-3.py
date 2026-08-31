from bisect import bisect_right
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = bisect_right(matrix, [target, float('inf')]) - 1
        col = bisect_right(matrix[row], target) - 1
        if row < 0 or col < 0: return False
        if row < len(matrix) - 1 and matrix[row + 1][0] == target:
            return True
        return matrix[row][col] == target
