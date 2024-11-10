class Solution:
    def __init__(self):
        self.keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        self.result = []
        self.subset = []

    def getLetterCombinations(self, index, digits):
        if index >= len(digits):
            self.result.append("".join(self.subset.copy()))
            return

        letters = self.keypad[digits[index]]
        for letter in letters:
            self.subset.append(letter)
            self.getLetterCombinations(index + 1, digits)
            self.subset.pop()

        return

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.getLetterCombinations(0, digits)
        return self.result
        