class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            sudoku_set = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in sudoku_set:
                    return False

                sudoku_set.add(board[row][col])

        for col in range(9):
            sudoku_set = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in sudoku_set:
                    return False

                sudoku_set.add(board[row][col])

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_set = set()
                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        if board[row][col] == ".":
                            continue
                        if board[row][col] in box_set:
                            return False
                        box_set.add(board[row][col])

        return True