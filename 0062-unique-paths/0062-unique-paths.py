class Solution:
    def __init__(self):
        self.cache = {}

    def dfs(self, r, c, m, n):

        if r not in range(m) or c not in range(n):
            return 0

        if (r, c) in self.cache:
            return self.cache[(r, c)]

        if r == m - 1 and c == n - 1:
            return 1

        self.cache[(r, c)] = self.dfs(r+1, c, m, n) + self.dfs(r, c+1, m, n)

        return self.cache[(r, c)]

    def uniquePaths(self, m: int, n: int) -> int:
        return self.dfs(0, 0, m, n)

        