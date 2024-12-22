class Solution:
    def __init__(self):
        self.palindrome_substr = []
        self.substr = []

    def isPalindrome(self, s):
        return s == s[-1::-1]

    def getSubstrings(self, index, s):
        if index >= len(s):
            self.palindrome_substr.append(self.substr.copy())
            return

        for j in range(index, len(s)):
            if not self.isPalindrome(s[index : j+1]):
                continue
            self.substr.append(s[index : j+1])
            self.getSubstrings(j + 1, s)
            self.substr.pop()

        return

    def partition(self, s: str) -> List[List[str]]:
        self.getSubstrings(0, s)
        return self.palindrome_substr
        