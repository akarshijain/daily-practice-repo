class Solution:
    def capture_unsurrounded_regions(self, row, col, board):
        visited = set()
        visited.add((row, col))

        cell_q = deque()
        cell_q.append((row, col))

        board[row][col] = "#"

        while cell_q:
            old_row, old_col = cell_q.popleft()
            
            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            for dr, dc in directions:
                new_row, new_col = old_row + dr, old_col + dc

                if new_row not in range(len(board)) \
                    or new_col not in range(len(board[0])) \
                    or (new_row, new_col) in visited \
                    or board[new_row][new_col] == "X":
                    continue

                cell_q.append((new_row, new_col))
                visited.add((new_row, new_col))
                board[new_row][new_col] = "#"
                

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        unsurrounded_regions = set()
        for col in range(len(board[0])):
            if board[0][col] == "O":
                unsurrounded_regions.add((0, col))

            if board[-1][col] == "O":
                unsurrounded_regions.add((len(board) - 1, col))

        for row in range(len(board)):
            if board[row][0] == "O":
                unsurrounded_regions.add((row, 0))

            if board[row][-1] == "O":
                unsurrounded_regions.add((row, len(board[0]) - 1))
        
        for row, col in unsurrounded_regions:
            self.capture_unsurrounded_regions(row, col, board)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "#":
                    board[row][col] = "O"

        