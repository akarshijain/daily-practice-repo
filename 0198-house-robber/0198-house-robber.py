class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        money_stashed = [0] * len(nums)

        money_stashed[0] = nums[0]
        money_stashed[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            money_stashed[i] = max(money_stashed[i - 1], nums[i] + money_stashed[i - 2])

        return money_stashed[-1]
        