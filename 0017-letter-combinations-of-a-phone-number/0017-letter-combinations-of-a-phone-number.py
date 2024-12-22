class Solution:
    def __init__(self):
        self.num_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        self.combination = []
        self.all_combinations = []

    def getCombination(self, index, digits):
        if index >= len(digits):
            self.all_combinations.append(''.join(self.combination.copy()))
            return

        letters = self.num_map[digits[index]]

        for letter in letters:
            self.combination.append(letter)
            self.getCombination(index + 1, digits)
            self.combination.pop()

        return

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        self.getCombination(0, digits)
        return self.all_combinations