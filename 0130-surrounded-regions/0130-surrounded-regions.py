class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cellq = deque()

        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row == 0 or row == len(board) - 1 or \
                    col == 0 or col == len(board[0]) - 1) and \
                    board[row][col] == "O":
                    cellq.append((row, col))

                    
        
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while cellq:
            old_row, old_col = cellq.popleft()
            board[old_row][old_col] = "T"
            for dr, dc in directions:
                new_row, new_col = old_row + dr, old_col + dc
                
                if new_row in range(len(board)) and \
                    new_col in range(len(board[0])) and \
                    board[new_row][new_col] == "O":

                    board[new_row][new_col] = "T"
                    cellq.append((new_row, new_col))

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    board[row][col] = "O"