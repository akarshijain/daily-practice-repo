class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
            
        num_ways = [0] * n

        num_ways[0] = 1
        num_ways[1] = 2

        for i in range(2, n):
            num_ways[i] = num_ways[i-1] + num_ways[i-2]

        return num_ways[n-1]