class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_cells = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_cells.add((row, col))

        for row, col in zero_cells:
            matrix[row][col] = None
            for next_col in range(len(matrix[0])):
                if matrix[row][next_col] != 0:
                    matrix[row][next_col] = None

            for next_row in range(len(matrix)):
                if matrix[next_row][col] != 0:
                    matrix[next_row][col] = None


        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if not matrix[row][col]:
                    matrix[row][col] = 0

        

        