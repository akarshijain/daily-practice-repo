class Solution:
    def maxRob(self, nums: List[int]) -> int:
        print(nums)
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.maxRob(nums[:-1]), self.maxRob(nums[-1:0:-1]))