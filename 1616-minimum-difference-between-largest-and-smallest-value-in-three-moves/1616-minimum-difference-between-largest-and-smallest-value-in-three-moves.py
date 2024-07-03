class Solution:
    def minDifference(self, nums: List[int]) -> int:

        if len(nums) <= 4:
            return 0

        nums.sort()
        k = 3
        i = 0
        j = len(nums) - k - 1
        answer = float('inf')

        while j != len(nums):
            answer = min(answer, nums[j] - nums[i])
            i += 1
            j += 1

        return answer

