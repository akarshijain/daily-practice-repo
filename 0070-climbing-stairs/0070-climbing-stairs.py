class Solution:
    def __init__(self):
        self.cache = {}

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        if n not in self.cache:
            self.cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return self.cache[n]

        

        

        return self.climbStairs(n-1) + self.climbStairs(n-2)