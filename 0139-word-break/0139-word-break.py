class Solution:
    def __init__(self):
        self.memo = {}

    def dfs(self, index, s, wordDict): 
        if index in self.memo:
            return self.memo[index]

        if index == len(s):
            return True

        for word in wordDict:
            if s[index:].startswith(word):
                if self.dfs(index + len(word), s, wordDict):
                    self.memo[index] = True
                    return True

        self.memo[index] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.dfs(0, s, wordDict)


       