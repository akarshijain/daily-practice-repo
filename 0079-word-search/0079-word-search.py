class Solution:
    def __init__(self):
        self.constructed_word = ""
        self.visited = set()

    def formWords(self, index, row, col, board, target_word):
        if self.constructed_word == target_word:
            return True

        if row not in range(len(board)) \
            or col not in range(len(board[0])) \
            or target_word[index] != board[row][col] \
            or (row, col) in self.visited: 
            return False

        self.constructed_word += board[row][col]
        self.visited.add((row, col))

        result = self.formWords(index + 1, row + 1, col, board, target_word) \
                    or self.formWords(index + 1, row, col + 1, board, target_word) \
                    or self.formWords(index + 1, row - 1, col, board, target_word) \
                    or self.formWords(index + 1, row, col - 1, board, target_word)

        self.constructed_word = self.constructed_word[:-1]
        self.visited.remove((row, col))
        
        return result

    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.formWords(0, row, col, board, word):
                        return True

        return False