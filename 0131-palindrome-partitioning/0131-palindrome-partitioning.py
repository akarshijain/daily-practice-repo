class Solution:
    def __init__(self):
        self.substring = []
        self.result = []

    def isPalindrome(self, substr):
        return substr == substr[-1::-1]

    def dfs(self, index, s):
        if index >= len(s):
            self.result.append(self.substring.copy())
            return

        for i in range(index, len(s)):
            substr = s[index:i+1]
            if not self.isPalindrome(substr):
                continue
            self.substring.append(substr)
            self.dfs(i+1, s)
            self.substring.pop()

        return

    def partition(self, s: str) -> List[List[str]]:
        self.dfs(0, s)
        return self.result