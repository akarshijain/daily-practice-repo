class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])

        row = -1
        up = 0
        down = len(matrix) - 1

        while down >= up:
            mid = (down + up) // 2

            if matrix[mid][0] <= target <= matrix[mid][cols - 1]:
                row = mid
                break

            if target > matrix[mid][cols - 1]:
                up = mid + 1
            
            else:
                down = mid - 1

        if row == -1:
            return False

        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == matrix[row][mid]:
                return True

            if target < matrix[row][mid]:
                right = mid - 1

            if target > matrix[row][mid]:
                left = mid + 1

        return False
