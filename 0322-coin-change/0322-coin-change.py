class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_coins = [float("inf")] * (amount + 1)

        num_coins[0] = 0

        for amt in range(1, amount + 1):
            for coin in coins:
                diff = amt - coin
                if diff >= 0:
                    num_coins[amt] = min(num_coins[amt], 1 + num_coins[diff])

        if num_coins[amount] == float("inf"):
            return -1

        return num_coins[amount]