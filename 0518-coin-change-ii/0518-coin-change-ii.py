class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        num_ways = [[0 for j in range(amount + 1)] for i in range(len(coins) + 1)]

        for row in range(len(num_ways)):
            num_ways[row][0] = 1

        for row in range(len(num_ways) - 2, -1, -1):
            for amt in range(amount + 1):
                if amt >= coins[row]:
                    num_ways[row][amt] = num_ways[row][amt - coins[row]] \
                                            + num_ways[row + 1][amt]

        return num_ways[0][amount]