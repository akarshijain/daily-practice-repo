class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_coins = [float("inf")] * (amount + 1)

        num_coins[0] = 0

        for target_value in range(1, len(num_coins)):
            for coin_value in coins:
                diff_amount = target_value - coin_value

                if diff_amount < 0:
                    continue

                num_coins[target_value] = min(num_coins[target_value], 1 + num_coins[diff_amount])

        if num_coins[-1] == float("inf"):
            return -1

        return num_coins[-1]
