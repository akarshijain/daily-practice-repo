class Solution:
    def __init__(self):
        self.visit = set()
    def dfs(self, board, row, col, word, word_len):
        if word_len == len(word):
            return True

        if row not in range(len(board)) \
            or col not in range(len(board[0])) \
            or board[row][col] != word[word_len] \
            or (row, col) in self.visit:
                return False

        self.visit.add((row, col))

        answer = (self.dfs(board, row + 1, col, word, word_len+1) or
        self.dfs(board, row - 1, col, word, word_len+1) or
        self.dfs(board, row, col + 1, word, word_len+1) or
        self.dfs(board, row, col - 1, word, word_len+1))

        self.visit.remove((row, col))

        return answer

    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(board, row, col, word, 0):
                    return True
        
        return False