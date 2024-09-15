class Solution:
    def rob(self, nums: List[int]) -> int:
        sum1, sum2 = 0, 0
        result = -1

        for num in nums:
            result = max(num + sum1, sum2)
            sum1 = sum2
            sum2 = result

        return result