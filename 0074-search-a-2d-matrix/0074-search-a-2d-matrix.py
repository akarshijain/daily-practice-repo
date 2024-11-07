class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        up = 0
        down = len(matrix)

        row = 0

        while up <= down:
            mid = (up + down) // 2

            if mid not in range(len(matrix)):
                return False
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif matrix[mid][0] > target:
                down = mid - 1
            else:
                up = mid + 1

        left = 0
        right = len(matrix[0])

        while left <= right:
            mid = (left + right) // 2

            if mid not in range(len(matrix[0])):
                return False

            if matrix[row][mid] == target:
                return True

            if matrix[row][mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        return False