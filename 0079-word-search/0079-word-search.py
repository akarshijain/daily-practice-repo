class Solution:
    def dfs(self, row, col, index, word, board, visited):
        if index == len(word):
            return True

        if row not in range(len(board)) or \
            col not in range(len(board[0])) or \
            visited[row][col] or \
            board[row][col] != word[index]:
            return False

        visited[row][col] = True

        result =  self.dfs(row + 1, col, index + 1, word, board, visited) or \
                    self.dfs(row - 1, col, index + 1, word, board, visited) or \
                    self.dfs(row, col + 1, index + 1, word, board, visited)  or \
                    self.dfs(row, col - 1, index + 1, word, board, visited) 

        visited[row][col] = False

        return result


    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.dfs(row, col, 0, word, board, visited):
                        return True

        
        return False