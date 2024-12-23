class Solution:
    def __init__(self):
        self.filled_columns = set()
        self.filled_positive_diagonals = set()
        self.filled_negative_diagonals = set()
        self.solution = []

    def placeQueens(self, n, row, chess_board):
        if row >= n:
            chess_board_copy = chess_board.copy()
            self.solution.append([''.join(row) for row in chess_board_copy])
            return

        for col in range(n):
            if col in self.filled_columns or \
                row + col in self.filled_positive_diagonals or \
                row - col in self.filled_negative_diagonals:
                continue

            chess_board[row][col] = "Q"
            self.filled_columns.add(col)
            self.filled_positive_diagonals.add(row + col)
            self.filled_negative_diagonals.add(row - col)

            self.placeQueens(n, row + 1, chess_board)

            chess_board[row][col] = "."
            self.filled_columns.remove(col)
            self.filled_positive_diagonals.remove(row + col)
            self.filled_negative_diagonals.remove(row - col)

        return



    def solveNQueens(self, n: int) -> List[List[str]]:
        chess_board = [['.'] * n for _ in range(n)]
        self.placeQueens(n, 0, chess_board)
        return self.solution